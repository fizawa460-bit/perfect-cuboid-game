#!/usr/bin/env python3
import ast
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
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp

ROOT = pathlib.Path(__file__).resolve().parent
REPO = "fizawa460-bit/perfect-cuboid-game"
STAGE32_ARTIFACT_ID = 9486641560
STAGE32_ARTIFACT_URL = f"https://api.github.com/repos/{REPO}/actions/artifacts/{STAGE32_ARTIFACT_ID}/zip"
STAGE32_ARTIFACT_SHA256 = "cae5c9b5aa00d9a730510c9f0e01ab609acef9d759fcc93f64708da123d6813d"
STAGE32_CORE_CANONICAL_SHA256 = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
UPSTREAM_URL = (
    "https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/"
    "51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"
)
UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
SKIP_START = "// Genus 3 hyperelliptic curves of degree 8"
SKIP_END = "// Set up the intersection pairing"
STOP_MARKER = "// The automorphism group (see Proposition 4)"
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER = "https://magma.maths.usyd.edu.au/calc/"
RETRY_DELAYS = (0, 5, 15, 30)


class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        newreq = super().redirect_request(req, fp, code, msg, headers, newurl)
        if newreq is not None and urllib.parse.urlsplit(req.full_url).netloc != urllib.parse.urlsplit(newurl).netloc:
            newreq.remove_header("Authorization")
        return newreq


def urlopen_retry(req, timeout, label):
    last = None
    for attempt, delay in enumerate(RETRY_DELAYS, 1):
        if delay:
            time.sleep(delay)
        try:
            return urllib.request.urlopen(req, timeout=timeout), attempt
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            print(f"{label} transient failure {attempt}/{len(RETRY_DELAYS)}: {exc}")
    raise last


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def download_stage32():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN required")
    req = urllib.request.Request(
        STAGE32_ARTIFACT_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/1.6",
        },
    )
    opener = urllib.request.build_opener(StripCrossHostAuthRedirect())
    with opener.open(req, timeout=60) as resp:
        raw = resp.read()
    if hashlib.sha256(raw).hexdigest() != STAGE32_ARTIFACT_SHA256:
        raise SystemExit("Stage32 artifact digest mismatch")
    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        core = json.loads(zf.read("picard-core.json"))
    if core.get("canonical_sha256_without_this_field") != STAGE32_CORE_CANONICAL_SHA256:
        raise SystemExit("Stage32 Picard core canonical hash mismatch")
    if core.get("rank") != 64 or core.get("known_class_count") != 140:
        raise SystemExit("Stage32 Picard core shape mismatch")
    return core


def flatten_matrix(M):
    return [int(M[i, j]) for i in range(M.rows) for j in range(M.cols)]


core32 = download_stage32()
known = core32["known_classes"]
prim_inds = [int(x) for x in core32["basis_known_indices_1based"]]
if len(prim_inds) != 64 or len(set(prim_inds)) != 64:
    raise SystemExit("bad Stage32 primitive basis index list")
boundary_inds = list(range(1, 25)) + list(range(93, 141))
M = sp.Matrix([known[j-1] for j in boundary_inds])
D, S, T = smith_normal_decomp(M, domain=ZZ)
if D != S*M*T:
    raise SystemExit("Stage32 Smith decomposition identity failed")
diag = [abs(int(D[i, i])) for i in range(58)]
if diag != [1]*56 + [2, 2]:
    raise SystemExit(f"unexpected Pic(Ubar) Smith diagonal tail: {diag[-6:]}")
Tflat = flatten_matrix(T)

req = urllib.request.Request(UPSTREAM_URL, headers={"User-Agent": "perfect-cuboid-stage33/1.6"})
resp, upstream_attempt = urlopen_retry(req, 60, "upstream fetch")
with resp:
    upstream = resp.read()
actual_blob = git_blob_sha(upstream)
if actual_blob != UPSTREAM_BLOB:
    raise SystemExit("upstream blob mismatch")
text = upstream.decode("utf-8")
i0 = text.index(SKIP_START)
i1 = text.index(SKIP_END, i0)
i2 = text.index(STOP_MARKER, i1)
core = text[:i0] + "\n// Stage33-03 quotient action skips unused degree-8 curves.\n" + text[i1:i2]

prim_literal = "[" + ",".join(map(str, prim_inds)) + "]"
t_literal = "[" + ",".join(map(str, Tflat)) + "]"
extra = f'''
actperm := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]])
                         where e := Eltseq(g @@ qPic)>;
ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
permcc := [Position(C1s, actcc(C)) : C in C1s]
            cat [#C1s+Position(C2s, actcc(C)) : C in C2s]
            cat [#C1s+#C2s+Position(C3s, actcc(C)) : C in C3s]
            cat [#Cs+Position(pts, Pr6![ccL(a) : a in Eltseq(pt)]) : pt in pts];
ccPic := Matrix(Integers(), [Eltseq(actperm(Pic.j, permcc)) : j in [1..64]]);
ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
permct := [Position(C1s, actct(C)) : C in C1s]
            cat [#C1s+Position(C2s, actct(C)) : C in C2s]
            cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s]
            cat [#Cs+Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];
ctPic := Matrix(Integers(), [Eltseq(actperm(Pic.j, permct)) : j in [1..64]]);

prim_inds := {prim_literal};
A := Matrix(Integers(), [Eltseq(qPic(Big.j)) : j in prim_inds]);
assert Abs(Determinant(A)) eq 1;
AinvQ := ChangeRing(A,Rationals())^-1;
Ainv := Matrix(Integers(),64,64,[Integers()!x : x in Eltseq(AinvQ)]);
Ccc := A*ccPic*Ainv;
Cct := A*ctPic*Ainv;
assert Ccc*Ccc eq IdentityMatrix(Integers(),64);
assert Cct*Cct eq IdentityMatrix(Integers(),64);
assert Ccc*Cct eq Cct*Ccc;

Tstage := Matrix(Integers(),64,64,{t_literal});
TinvQ := ChangeRing(Tstage,Rationals())^-1;
Tinv := Matrix(Integers(),64,64,[Integers()!x : x in Eltseq(TinvQ)]);
Scc := Tinv*Ccc*Tstage;
Sct := Tinv*Cct*Tstage;
qinds := [57..64];
// torsion generators 57,58 may not acquire free coordinates
for j in [57,58] do
  assert forall{{k : k in [59..64] | Scc[j,k] eq 0}};
  assert forall{{k : k in [59..64] | Sct[j,k] eq 0}};
end for;

printf "STAGE33_03_PICU_BEGIN\\n";
printf "A_DET=%o\\n", Determinant(A);
printf "CC_TRACE_PRIM=%o\\n", Trace(Ccc);
printf "CT_TRACE_PRIM=%o\\n", Trace(Cct);
printf "CCT_TRACE_PRIM=%o\\n", Trace(Ccc*Cct);
for j in qinds do
  printf "PICU_CC_ROW_%o=%o\\n", j-56, [Scc[j,k] : k in qinds];
end for;
for j in qinds do
  printf "PICU_CT_ROW_%o=%o\\n", j-56, [Sct[j,k] : k in qinds];
end for;
printf "STAGE33_03_PICU_END\\n";
'''
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra
payload = urllib.parse.urlencode({"input": code}).encode()
req = urllib.request.Request(
    MAGMA_URL,
    data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage33/1.6",
    },
    method="POST",
)
resp, magma_attempt = urlopen_retry(req, 180, "Magma calculator")
with resp:
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
(ROOT / "picu-action-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_03_PICU_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")):
    print(stdout)
    raise SystemExit("Pic(Ubar) quotient action materialization failed")


def scalar(name):
    m = re.search(rf"^{name}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    return m.group(1).strip()


def rows(prefix):
    found = {}
    for m in re.finditer(rf"^{prefix}_(\d+)=(.+)$", stdout, re.M):
        found[int(m.group(1))] = ast.literal_eval(m.group(2).replace(" ", ""))
    if set(found) != set(range(1,9)):
        raise SystemExit(f"incomplete {prefix}: {found.keys()}")
    return [found[j] for j in range(1,9)]

cc_raw, ct_raw = rows("PICU_CC_ROW"), rows("PICU_CT_ROW")
if any(len(r) != 8 for r in cc_raw + ct_raw):
    raise SystemExit("bad quotient action row width")

# Mixed coordinates: first two targets are modulo 2, last six are integral.
def normalize(A):
    return [[int(x)%2 if j < 2 else int(x) for j,x in enumerate(row)] for row in A]

cc, ct = normalize(cc_raw), normalize(ct_raw)


def apply_row(row, A):
    out = [0]*8
    for i, coeff in enumerate(row):
        for j in range(8):
            out[j] += coeff*A[i][j]
    out[0] %= 2
    out[1] %= 2
    return out


def compose(A,B):
    return [apply_row(row,B) for row in A]

identity = [[1 if i==j else 0 for j in range(8)] for i in range(8)]
if compose(cc,cc) != identity or compose(ct,ct) != identity or compose(cc,ct) != compose(ct,cc):
    raise SystemExit("mixed Pic(Ubar) V4 action check failed")

# Fixed torsion subgroup: free part is zero for torsion elements, so only the
# top-left 2x2 matrices matter. Compute joint fixed dimension over F2.
def rank2(rows2):
    a = [[x&1 for x in r] for r in rows2]
    r=0
    for c in range(2):
        p=next((u for u in range(r,len(a)) if a[u][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for u in range(len(a)):
            if u!=r and a[u][c]:
                a[u]=[x^y for x,y in zip(a[u],a[r])]
        r+=1
    return r

constraints=[]
for A8 in (cc,ct):
    for i in range(2):
        constraints.append([(A8[i][j] ^ (1 if i==j else 0)) & 1 for j in range(2)])
torsion_fixed_dim = 2-rank2(constraints)

free_cc = [row[2:] for row in cc[2:]]
free_ct = [row[2:] for row in ct[2:]]
if int(scalar("CC_TRACE_PRIM")) != 34 or int(scalar("CT_TRACE_PRIM")) != 56 or int(scalar("CCT_TRACE_PRIM")) != 30:
    raise SystemExit("primitive-basis Picard traces do not match source trace lock")

out = {
    "schema": "STAGE33_03_PICU_INTEGRAL_V4_ACTION_V1",
    "source_locks": {
        "stage32_artifact_id": STAGE32_ARTIFACT_ID,
        "stage32_artifact_sha256": STAGE32_ARTIFACT_SHA256,
        "stage32_core_canonical_sha256": STAGE32_CORE_CANONICAL_SHA256,
        "upstream_git_blob_sha1": actual_blob,
        "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    },
    "basis_bridge": {
        "primitive_basis_known_indices_1based": prim_inds,
        "primitive_to_source_basis_determinant": int(scalar("A_DET")),
        "unimodular": abs(int(scalar("A_DET"))) == 1,
    },
    "pic_u_group": {"free_rank":6,"torsion":[2,2]},
    "generator_order": ["torsion_2_a","torsion_2_b","free_1","free_2","free_3","free_4","free_5","free_6"],
    "cc_mixed_action": cc,
    "ct_mixed_action": ct,
    "torsion_joint_fixed_dimension_f2": torsion_fixed_dim,
    "torsion_joint_fixed_subgroup_order": 2**torsion_fixed_dim,
    "exact_checks": {
        "basis_bridge_unimodular": True,
        "source_and_primitive_picard_traces_match": True,
        "torsion_generators_map_to_torsion": True,
        "mixed_actions_square_to_identity": True,
        "mixed_actions_commute": True,
    },
    "next_exact_leaf": "L33-03-TWO-PRIMARY-UPIC-TRANSGRESSION",
    "two_primary_transgression_complete": False,
    "br0b_all_primary_classes_accounted": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
out["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "picu-integral-action.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
    "success": True,
    "basis_bridge_det": out["basis_bridge"]["primitive_to_source_basis_determinant"],
    "torsion_joint_fixed_dimension_f2": torsion_fixed_dim,
    "torsion_joint_fixed_subgroup_order": 2**torsion_fixed_dim,
    "next_exact_leaf": out["next_exact_leaf"],
    "certificate_sha256": out["canonical_sha256"],
},indent=2,sort_keys=True))
