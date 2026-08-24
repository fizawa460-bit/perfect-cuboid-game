#!/usr/bin/env python3
"""Compute H^1(V4,UPic) and the two finite transgression ranks exactly.

This deliberately reuses the source-locked Stage33-03 total-complex builder but
submits an H1-only Magma job. The previous implementation appended H1 Smith
forms after the already-certified H2 Smith forms; that exceeded the public
Magma calculator CPU window even though the H2 job itself passed.
"""
import hashlib
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "compute_v4_hypercohomology.py"

base_src = BASE.read_text(encoding="utf-8")
cut = '\ncode = "SetColumns(0);\\nquick := true;\\n" + source_core + "\\n" + extra\n'
if base_src.count(cut) != 1:
    raise SystemExit("could not isolate finite-V4 calculator setup prefix")
prefix = base_src.split(cut, 1)[0]
ns = {"__name__": "stage33_03_h1_setup", "__file__": str(BASE)}
exec(compile(prefix, str(BASE) + "[setup-only]", "exec"), ns)

extra = ns["extra"]

old_chain = """D0 := TotalDiff(0);
D1 := TotalDiff(1);
D2 := TotalDiff(2);
assert D0*D1 eq ZeroMatrix(Z,Nrows(D0),Ncols(D1));
assert D1*D2 eq ZeroMatrix(Z,Nrows(D1),Ncols(D2));

"""
new_chain = """D0 := TotalDiff(0);
D1 := TotalDiff(1);
assert D0*D1 eq ZeroMatrix(Z,Nrows(D0),Ncols(D1));

"""
if extra.count(old_chain) != 1:
    raise SystemExit("could not isolate D0/D1 chain block")
extra = extra.replace(old_chain, new_chain, 1)

h2_start = extra.index("// H^2 = ker(D2)/im(D1).")
out_end_tag = 'printf "STAGE33_03_V4_HYPER_END'
out_end = extra.index(out_end_tag, h2_start)
out_end = extra.index("\n", out_end)

h1_block = r"""// H^1 = ker(D1)/im(D0) from the exact same integral total complex.
S1, _, V1 := SmithForm(Transpose(D1));
r1h := Rank(D1);
n1h := Nrows(D1);
kdim1 := n1h-r1h;
V1inv := V1^-1;
Coords1 := D0*Transpose(V1inv);
for rr0 in [1..Nrows(Coords1)] do
  for cc0 in [1..r1h] do
    assert Coords1[rr0,cc0] eq 0;
  end for;
end for;
Brel1 := Submatrix(Coords1,1,r1h+1,Nrows(Coords1),kdim1);
SB1 := SmithForm(Brel1);
rr1h := Rank(Brel1);
diag1 := [Abs(Z!SB1[j,j]) : j in [1..rr1h]];
tors1 := [d : d in diag1 | d ne 1];
free1 := kdim1-rr1h;
assert forall{d : d in tors1 | d in [2,4]};
printf "STAGE33_03_V4_H1_BEGIN\\n";
printf "D0_RANK=%o\\n", Rank(D0);
printf "D1_RANK=%o\\n", r1h;
printf "KERNEL_D1_RANK=%o\\n", kdim1;
printf "H1_FREE_RANK=%o\\n", free1;
printf "H1_TORSION=%o\\n", tors1;
printf "STAGE33_03_V4_H1_END\\n";
"""
h1_extra = extra[:h2_start] + h1_block + extra[out_end + 1:]

code = "SetColumns(0);\nquick := true;\n" + ns["source_core"] + "\n" + h1_extra
summary = {
    "schema": "STAGE33_03_FINITE_V4_UPIC_H1_REQUEST_V2",
    "upstream_git_blob_sha1": ns["actual_blob"],
    "stage32_artifact_id": ns["STAGE32_ARTIFACT_ID"],
    "stage32_artifact_sha256": ns["STAGE32_ARTIFACT_SHA256"],
    "stage32_core_canonical_sha256": ns["STAGE32_CORE_CANONICAL_SHA256"],
    "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    "resolution": "same tensor-product 2-periodic C2xC2 resolution as finite H2 certificate",
    "totalization": "same exact [Div_D degree 0 -> Pic degree 1] complex; H1-only Smith computation",
    "finite_h2_recomputed": False,
}
(ROOT / "finite-transgression-ranks-request-summary.json").write_text(
    json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)

payload = urllib.parse.urlencode({"input": code}).encode()
req = urllib.request.Request(
    ns["MAGMA_URL"],
    data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": ns["MAGMA_REFERER"],
        "User-Agent": "perfect-cuboid-stage33/1.8",
    },
    method="POST",
)
resp, magma_attempt = ns["urlopen_retry"](req, 300, "Magma calculator H1")
with resp:
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
(ROOT / "v4-h1-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_03_V4_H1_END" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "Assertion failed", "User error")
):
    print(stdout)
    raise SystemExit("finite V4 UPic H1 computation failed")

def scalar(name):
    m = re.search(rf"^{name}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    return m.group(1).strip()

def intlist(s):
    s = s.strip()
    if s == "[]":
        return []
    return [int(x.strip()) for x in s[1:-1].split(",") if x.strip()]

free = int(scalar("H1_FREE_RANK"))
tors = intlist(scalar("H1_TORSION"))
if free != 0 or any(x != 2 for x in tors) or len(tors) > 2:
    raise SystemExit(f"unexpected H1(V4,UPic): free={free}, tors={tors}")

h1dim = len(tors)
r01 = 2 - h1dim
r11 = 4 - r01
if (r01, r11) not in ((0, 4), (1, 3), (2, 2)):
    raise SystemExit("transgression rank pair escaped certified envelope")

env = json.loads((ROOT / "finite-transgression-envelope.json").read_text())
finite = json.loads((ROOT / "finite-v4-hypercohomology.json").read_text())
if [r01, r11] not in env["possible_rank_pairs"]:
    raise SystemExit("exact rank pair disagrees with certified envelope")

cert = {
    "schema": "STAGE33_03_FINITE_V4_TRANSGRESSION_RANKS_V2",
    "source_locks": {
        "finite_transgression_envelope_sha256": env["canonical_sha256"],
        "finite_v4_hypercohomology_sha256": finite["canonical_sha256"],
        "h1_request_summary": summary,
    },
    "magma_request_attempt": magma_attempt,
    "H1_V4_UPic": {"free_rank": 0, "torsion_invariants": tors, "f2_dimension": h1dim},
    "H1_V4_unit_lattice": 0,
    "PicU_V4_invariant_dimension_f2": 2,
    "rank_d2_01": r01,
    "rank_d2_11": r11,
    "finite_transgression_rank_pair_exact": True,
    "absolute_kernel_character_terms_still_open": True,
    "next_exact_leaf": "L33-03-ABSOLUTE-N-CHARACTER-INFLATION-RESTRICTION-AND-d2_11",
    "br0b_all_primary_classes_accounted": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "finite-transgression-ranks.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "H1_V4_UPic": f"(Z/2)^{h1dim}",
    "rank_d2_01": r01,
    "rank_d2_11": r11,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
