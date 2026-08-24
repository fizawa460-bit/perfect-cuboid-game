#!/usr/bin/env python3
import hashlib
import io
import json
import os
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parent
REPO = "fizawa460-bit/perfect-cuboid-game"
BR0A_ARTIFACT_ID = 9505735040
BR0A_ARTIFACT_URL = f"https://api.github.com/repos/{REPO}/actions/artifacts/{BR0A_ARTIFACT_ID}/zip"
BR0A_ARTIFACT_SHA256 = "75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87"
BR0A_CERTIFICATE_SHA256 = "2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1"
UPSTREAM_URL = (
    "https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/"
    "51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"
)
UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
STOP_MARKER = "// Genus 3 hyperelliptic curves of degree 8"
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER = "https://magma.maths.usyd.edu.au/calc/"
RETRY_DELAYS = (0, 5, 15, 30)

FACTOR_NAMES = [
    "b3-a2", "b3+a2", "b2-a3", "b2+a3", "c-b1", "c+b1",
    "b1-a3", "b1+a3", "b3-a1", "b3+a1", "c-b2", "c+b2",
    "b2-a1", "b2+a1", "b1-a2", "b1+a2", "c-b3", "c+b3",
]


class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        newreq = super().redirect_request(req, fp, code, msg, headers, newurl)
        if newreq is not None and urllib.parse.urlsplit(req.full_url).netloc != urllib.parse.urlsplit(newurl).netloc:
            newreq.remove_header("Authorization")
        return newreq


def urlopen_retry(req, timeout, label, opener=None):
    last = None
    op = opener or urllib.request.build_opener()
    for attempt, delay in enumerate(RETRY_DELAYS, 1):
        if delay:
            time.sleep(delay)
        try:
            return op.open(req, timeout=timeout), attempt
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            print(f"{label} transient failure {attempt}/{len(RETRY_DELAYS)}: {exc}")
    raise last


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def download_br0a():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN required")
    req = urllib.request.Request(
        BR0A_ARTIFACT_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/1.9",
        },
    )
    opener = urllib.request.build_opener(StripCrossHostAuthRedirect())
    with opener.open(req, timeout=60) as resp:
        raw = resp.read()
    if hashlib.sha256(raw).hexdigest() != BR0A_ARTIFACT_SHA256:
        raise SystemExit("BR0A artifact digest mismatch")
    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        name = next((n for n in zf.namelist() if n.endswith("br0a-artifact-certificate.json")), None)
        if name is None:
            raise SystemExit("missing BR0A certificate")
        cert_bytes = zf.read(name)
    if hashlib.sha256(cert_bytes).hexdigest() != BR0A_CERTIFICATE_SHA256:
        raise SystemExit("BR0A certificate digest mismatch")
    return json.loads(cert_bytes)


def row_coefficients_in_lattice(v, K):
    piv = list(K.rref()[1])
    if len(piv) != K.rows:
        raise SystemExit("lattice basis lost rank")
    minor = K[:, piv]
    coeff = sp.Matrix(1, K.rows, [v[j] for j in piv]) * minor.inv()
    if coeff * K != sp.Matrix(1, K.cols, v):
        return None
    if any(sp.Rational(x).q != 1 for x in coeff):
        return None
    return [int(x) for x in coeff]


def independent_rows(rows):
    out = []
    inds = []
    rank = 0
    for i, row in enumerate(rows):
        r2 = sp.Matrix(out + [row]).rank()
        if r2 > rank:
            out.append(row)
            inds.append(i)
            rank = r2
    return inds, out


br0a = download_br0a()
K = sp.Matrix(br0a["unit_divisor_relation_kernel_basis"])
if K.shape != (14, 72) or K.rank() != 14:
    raise SystemExit("unexpected audited unit lattice")
Bpic = sp.Matrix(br0a["boundary_to_pic_matrix"])
if Bpic.shape != (72, 64):
    raise SystemExit("unexpected boundary-to-Pic matrix")

req = urllib.request.Request(UPSTREAM_URL, headers={"User-Agent": "perfect-cuboid-stage33/1.9"})
resp, upstream_attempt = urlopen_retry(req, 60, "upstream fetch")
with resp:
    upstream = resp.read()
if git_blob_sha(upstream) != UPSTREAM_BLOB:
    raise SystemExit("upstream blob mismatch")
text = upstream.decode("utf-8")
source_core = text[:text.index(STOP_MARKER)]

extra = r'''
forms := [
  b3-a2, b3+a2, b2-a3, b2+a3, c-b1, c+b1,
  b1-a3, b1+a3, b3-a1, b3+a1, c-b2, c+b2,
  b2-a1, b2+a1, b1-a2, b1+a2, c-b3, c+b3
];
assert #forms eq 18;
printf "STAGE33_04_QUNIT_BEGIN\n";
for k in [1..#forms] do
  f := forms[k];
  C := Scheme(S, f);
  CC := C;
  sm := [];
  for j in [1..24] do
    m := 0;
    while IsSubscheme(C1s[j], CC) do
      m +:= 1;
      CC := Difference(CC, C1s[j]);
    end while;
    Append(~sm, m);
  end for;
  assert Dimension(CC) lt 1;
  pm := [pt in C select Multiplicity(C, pt) else 0 : pt in pts];
  printf "FACTOR=%o\n", k;
  printf "SIDE=%o\n", sm;
  printf "POINT=%o\n", pm;
end for;
printf "STAGE33_04_QUNIT_END\n";
'''
code = "SetColumns(0);\nquick := true;\n" + source_core + "\n" + extra
payload = urllib.parse.urlencode({"input": code}).encode()
req = urllib.request.Request(
    MAGMA_URL,
    data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage33/1.9",
    },
    method="POST",
)
resp, magma_attempt = urlopen_retry(req, 300, "Magma calculator")
with resp:
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
(ROOT / "q-unit-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_04_QUNIT_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "Assertion failed", "User error")):
    print(stdout)
    raise SystemExit("Q-unit divisor materialization failed")

blocks = re.findall(r"FACTOR=(\d+)\nSIDE=\[(.*?)\]\nPOINT=\[(.*?)\]", stdout, re.S)
if len(blocks) != 18:
    raise SystemExit(f"expected 18 factor blocks, got {len(blocks)}")

def ints(s):
    return [int(x.strip()) for x in s.replace("\n", " ").split(",") if x.strip()]

divisors = []
for k_s, side_s, point_s in blocks:
    k = int(k_s)
    side = ints(side_s)
    point = ints(point_s)
    if len(side) != 24 or len(point) != 48:
        raise SystemExit(f"bad divisor shape for factor {k}")
    divisors.append(side + point)
if len(divisors) != 18:
    raise SystemExit("factor parse regression")

# All 18 forms are linear sections of the same O(1), hence their resolved
# boundary divisors must have the same Picard class.  This also checks the
# exceptional multiplicities returned by Magma against the audited Picard map.
classes = [sp.Matrix(1, 72, v) * Bpic for v in divisors]
if any(c != classes[0] for c in classes[1:]):
    raise SystemExit("linear-factor divisors do not have a common Picard class")

ratio_rows = [[a - b for a, b in zip(divisors[i], divisors[0])] for i in range(1, 18)]
ratio_names = [f"({FACTOR_NAMES[i]})/({FACTOR_NAMES[0]})" for i in range(1, 18)]
if any(row_coefficients_in_lattice(v, K) is None for v in ratio_rows):
    raise SystemExit("an explicit factor ratio escaped the audited unit lattice")
inds, basis_rows = independent_rows(ratio_rows)
if len(basis_rows) != 14:
    raise SystemExit(f"explicit factor-ratio span has rank {len(basis_rows)}, expected 14")
B = sp.Matrix(basis_rows)
if any(row_coefficients_in_lattice(v, B) is None for v in K.tolist()):
    raise SystemExit("explicit Q-unit divisor lattice is a proper sublattice of audited U_D")
if any(row_coefficients_in_lattice(v, K) is None for v in B.tolist()):
    raise SystemExit("explicit Q-unit divisor lattice exceeds audited U_D")

selected = []
for basis_index, ratio_index in enumerate(inds, 1):
    factor_index = ratio_index + 1
    row = ratio_rows[ratio_index]
    selected.append({
        "unit_id": f"QUNIT_{basis_index:02d}",
        "function": ratio_names[ratio_index],
        "numerator_factor": FACTOR_NAMES[factor_index],
        "denominator_factor": FACTOR_NAMES[0],
        "divisor_vector_72": row,
        "coordinates_in_audited_unit_basis": row_coefficients_in_lattice(row, K),
    })

cert = {
    "schema": "STAGE33_04_EXPLICIT_Q_UNIT_LATTICE_V1",
    "source_locks": {
        "upstream_git_blob_sha1": UPSTREAM_BLOB,
        "br0a_artifact_id": BR0A_ARTIFACT_ID,
        "br0a_artifact_sha256": BR0A_ARTIFACT_SHA256,
        "br0a_certificate_sha256": BR0A_CERTIFICATE_SHA256,
        "unit_kernel_sha256": br0a["unit_divisor_relation_kernel_basis_sha256"],
        "boundary_to_pic_sha256": br0a["boundary_to_pic_matrix_sha256"],
    },
    "upstream_fetch_attempt": upstream_attempt,
    "magma_request_attempt": magma_attempt,
    "candidate_linear_factor_count": 18,
    "all_factor_divisors_supported_on_physical_boundary": True,
    "all_factor_divisors_have_common_picard_class": True,
    "factor_divisors_72": [
        {"factor": name, "divisor_vector_72": vec}
        for name, vec in zip(FACTOR_NAMES, divisors)
    ],
    "explicit_q_unit_count": 14,
    "explicit_q_units": selected,
    "explicit_q_unit_divisor_lattice_rank": 14,
    "explicit_q_unit_divisor_lattice_equals_audited_U_D": True,
    "all_units_defined_over_Q": True,
    "next_exact_leaf": "L33-04-LIFT-EXPLICIT-QUNIT-SYMBOL-FIRST-RESIDUES-AND-QUOTIENT",
    "q_defined_brauer_class_independence_certified": False,
    "physical_open_unramified_kernel_complete": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "explicit-q-units.json").write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "explicit_q_unit_count": 14,
    "explicit_q_unit_lattice_rank": 14,
    "lattice_equals_audited_U_D": True,
    "selected_units": [u["function"] for u in selected],
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
