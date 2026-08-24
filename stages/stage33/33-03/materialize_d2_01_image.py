#!/usr/bin/env python3
"""Materialize the exact finite d2_01 image in H^2(V4,U_D).

The previous leaves certify Pic(Ubar)^V4=(Z/2)^2, U_D=Z^14 with trivial
V4 action, and rank_F2(d2_01)=2.  This leaf computes the two actual H^2
classes.  In the Smith basis H^2(V4,Z^14) is identified with the 28 F2
coordinates given by the cc/ct quadratic-character values for each of the
14 unit directions.
"""
import ast
import hashlib
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
PICU_SCRIPT = ROOT / "extract_picu_quotient_action.py"

# Execute only the deterministic setup prefix of the already source-locked
# Pic(Ubar) action calculator.  This gives the exact Smith transforms S,T,
# the pinned Testa--Stoll source core and the Magma action program, without
# submitting its original request.
src = PICU_SCRIPT.read_text(encoding="utf-8")
cut = 'payload = urllib.parse.urlencode({"input": code}).encode()\n'
if src.count(cut) != 1:
    raise SystemExit("could not isolate PicU action setup prefix")
prefix = src.split(cut, 1)[0]
ns = {"__name__": "stage33_03_d2_01_setup", "__file__": str(PICU_SCRIPT)}
exec(compile(prefix, str(PICU_SCRIPT) + "[setup-only]", "exec"), ns)

extra = ns["extra"]
marker = 'printf "STAGE33_03_PICU_END\\n";'
if extra.count(marker) != 1:
    raise SystemExit("could not locate PicU Magma output marker")
inject = r'''
for jj in [57,58] do
  printf "D2_CC_FULL_ROW_%o=%o\n", jj-56, [Scc[jj,kk] : kk in [1..64]];
  printf "D2_CT_FULL_ROW_%o=%o\n", jj-56, [Sct[jj,kk] : kk in [1..64]];
end for;
'''
extra2 = extra.replace(marker, inject + "\n" + marker, 1)
code = "SetColumns(0);\nquick := true;\n" + ns["core"] + "\n" + extra2

payload = urllib.parse.urlencode({"input": code}).encode()
req = urllib.request.Request(
    ns["MAGMA_URL"], data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": ns["MAGMA_REFERER"],
        "User-Agent": "perfect-cuboid-stage33/2.0",
    }, method="POST",
)
resp, magma_attempt = ns["urlopen_retry"](req, 240, "Magma calculator d2_01")
with resp:
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
(ROOT / "d2-01-image-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_03_PICU_END" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "Assertion failed", "User error")
):
    print(stdout)
    raise SystemExit("d2_01 PicU lift materialization failed")

def full_row(gen, j):
    m = re.search(rf"^D2_{gen}_FULL_ROW_{j}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing D2_{gen}_FULL_ROW_{j}")
    row = ast.literal_eval(m.group(1).strip())
    if len(row) != 64:
        raise SystemExit("bad full transformed Pic action row width")
    return [int(x) for x in row]

cc_rows = [full_row("CC", 1), full_row("CC", 2)]
ct_rows = [full_row("CT", 1), full_row("CT", 2)]

# Exact transformed boundary action.  D=S*M*T; hence transformed domain row
# coordinates act by S*P*S^-1.  Rows 59..72 are the Smith-kernel basis U_D.
S = ns["S"]
D = ns["D"]
Sinv = S.inv()
if any(getattr(x, "q", 1) != 1 for x in Sinv):
    raise SystemExit("Smith left transform inverse is not integral")n
raw_gal = json.loads((ROOT / "galois-action-raw.json").read_text())
finite = json.loads((ROOT / "finite-transgression-ranks.json").read_text())
picu = json.loads((ROOT / "picu-integral-action.json").read_text())
if finite["rank_d2_01"] != 2:
    raise SystemExit("finite d2_01 rank lock is not 2")
if picu["torsion_joint_fixed_dimension_f2"] != 2:
    raise SystemExit("PicU fixed torsion lock is not dimension 2")

def perm_matrix(perm):
    if sorted(perm) != list(range(1, 73)):
        raise SystemExit("bad boundary permutation")
    P = sp.zeros(72, 72)
    for j, v in enumerate(perm):
        P[j, v - 1] = 1
    return P

Pcc = perm_matrix([int(x) for x in raw_gal["boundary_perm_cc_1based"]])
Pct = perm_matrix([int(x) for x in raw_gal["boundary_perm_ct_1based"]])
ADcc = S * Pcc * Sinv
ADct = S * Pct * Sinv
I72 = sp.eye(72)
if ADcc * ADcc != I72 or ADct * ADct != I72 or ADcc * ADct != ADct * ADcc:
    raise SystemExit("transformed boundary V4 action failed")
# The audited rank-14 unit lattice is pointwise fixed.
if ADcc[58:72, 0:58] != sp.zeros(14, 58) or ADct[58:72, 0:58] != sp.zeros(14, 58):
    raise SystemExit("unit kernel is not preserved")
if ADcc[58:72, 58:72] != sp.eye(14) or ADct[58:72, 58:72] != sp.eye(14):
    raise SystemExit("unit V4 action is not trivial in Smith basis")

# D has rank 58, with torsion diagonal entries 57,58 equal to 2 up to sign.
diag = [int(D[j, j]) for j in range(58)]
if [abs(x) for x in diag] != [1] * 56 + [2, 2]:
    raise SystemExit("unexpected Smith diagonal")

def lift_difference(action_row, torsion_index):
    r = action_row[:]
    r[torsion_index] -= 1
    # A fixed quotient class means r lies in im(D); in Smith coordinates this
    # is directly divisible by the first 58 diagonal entries and zero after.
    if any(r[j] != 0 for j in range(58, 64)):
        raise SystemExit("fixed PicU torsion representative acquired free quotient part")
    a = [0] * 72
    for j in range(58):
        if r[j] % diag[j] != 0:
            raise SystemExit("Pic difference is not integrally liftable through D")
        a[j] = r[j] // diag[j]
    avec = sp.Matrix([a])
    if list(avec * D) != r:
        raise SystemExit("integral divisor lift verification failed")
    return avec

def rowints(v):
    return [int(v[0, j]) for j in range(v.cols)]

AD = {
    "id": I72,
    "cc": ADcc,
    "ct": ADct,
    "cct": ADcc * ADct,
}
bits = {"id": (0, 0), "cc": (1, 0), "ct": (0, 1), "cct": (1, 1)}
bybits = {v: k for k, v in bits.items()}
def mul(g, h):
    return bybits[(bits[g][0] ^ bits[h][0], bits[g][1] ^ bits[h][1])]

images = []
for t in range(2):
    zero = sp.zeros(1, 72)
    acc = lift_difference(cc_rows[t], t)
    act = lift_difference(ct_rows[t], t)
    # For right actions: p^(cc*ct)-p = (p^cc-p)^ct + (p^ct-p).
    acct = acc * ADct + act
    lifts = {"id": zero, "cc": acc, "ct": act, "cct": acct}

    cocycle = {}
    for g in bits:
        for h in bits:
            c = lifts[g] * AD[h] + lifts[h] - lifts[mul(g, h)]
            if c * D != sp.zeros(1, 64):
                raise SystemExit("transgression 2-cochain escaped the unit kernel")
            if any(int(c[0, j]) != 0 for j in range(58)):
                raise SystemExit("kernel vector has non-unit Smith coordinates")
            cocycle[(g, h)] = c

    # Verify the normalized 2-cocycle identity.  The unit action is trivial.
    for g in bits:
        for h in bits:
            for k in bits:
                lhs = (cocycle[(g, h)] * AD[k] + cocycle[(mul(g, h), k)]
                       - cocycle[(g, mul(h, k))] - cocycle[(h, k)])
                if lhs != sp.zeros(1, 72):
                    raise SystemExit("d2_01 cocycle identity failed")

    ucc = rowints(cocycle[("cc", "cc")])[58:72]
    uct = rowints(cocycle[("ct", "ct")])[58:72]
    ucross = rowints(cocycle[("cc", "ct")])[58:72]
    ureverse = rowints(cocycle[("ct", "cc")])[58:72]
    cc_f2 = [x & 1 for x in ucc]
    ct_f2 = [x & 1 for x in uct]
    packed = cc_f2 + ct_f2
    images.append({
        "torsion_generator": f"torsion_2_{'a' if t == 0 else 'b'}",
        "smith_pic_coordinate_1based": 57 + t,
        "u_cc_cc_unit_coordinates": ucc,
        "u_ct_ct_unit_coordinates": uct,
        "u_cc_ct_unit_coordinates": ucross,
        "u_ct_cc_unit_coordinates": ureverse,
        "cc_quadratic_character_coefficients_f2": cc_f2,
        "ct_quadratic_character_coefficients_f2": ct_f2,
        "h2_v4_unit_basis_vector_f2_cc_then_ct": packed,
    })

def rank_f2(rows):
    a = [r[:] for r in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col] & 1), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(len(a)):
            if i != rank and (a[i][col] & 1):
                a[i] = [(x ^ y) for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank

image_rank = rank_f2([x["h2_v4_unit_basis_vector_f2_cc_then_ct"] for x in images])
if image_rank != 2:
    raise SystemExit(f"materialized d2_01 image rank {image_rank} disagrees with exact rank 2")

smith_payload = {
    "D": [int(x) for x in D],
    "S": [int(x) for x in S],
    "T": [int(x) for x in ns["T"]],
}
smith_hash = hashlib.sha256(json.dumps(smith_payload, separators=(",", ":")).encode()).hexdigest()
cert = {
    "schema": "STAGE33_03_D2_01_EXACT_IMAGE_V1",
    "source_locks": {
        "galois_action_raw_sha256": raw_gal["canonical_sha256"],
        "picu_integral_action_sha256": picu["canonical_sha256"],
        "finite_transgression_ranks_sha256": finite["canonical_sha256"],
        "smith_D_S_T_sha256": smith_hash,
        "submitted_magma_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "magma_stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
    },
    "magma_request_attempt": magma_attempt,
    "unit_smith_basis_rank": 14,
    "h2_v4_unit_identification": "H^2(V4,Z^14) ~= Hom(V4,Q/Z)^14 ~= (Z/2)^28; coordinates cc[14] then ct[14]",
    "pic_u_fixed_torsion_basis": ["torsion_2_a", "torsion_2_b"],
    "torsion_generator_images": images,
    "image_f2_rank": image_rank,
    "rank_matches_finite_hypercohomology_edge_result": True,
    "finite_d2_01_image_exact": True,
    "absolute_d2_01_image_supported_on_visible_V4_quadratic_characters": True,
    "next_exact_leaf": "L33-03-ABSOLUTE-N-CHARACTER-INFLATION-RESTRICTION-AND-d2_11",
    "br0b_all_primary_classes_accounted": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "d2-01-image.json").write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "image_f2_rank": image_rank,
    "torsion_generator_images_f2": [x["h2_v4_unit_basis_vector_f2_cc_then_ct"] for x in images],
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
