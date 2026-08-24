#!/usr/bin/env python3
"""Hostile-audit verifier for the five free H^1(V4,Pic(Ubar)) classes.

The production extension proof inferred that the finite d2_11 restriction to
H^1(V4,Pic(Ubar)_free) is zero from total rank(d2_11)=2 and a rank-two torsion
image. Rank equality alone does not imply that restriction is zero, because a
free-side image could lie inside the same rank-two target subspace.

This verifier computes the five free-side d2_11 images directly from the
source-locked two-term complex in Smith coordinates. It exports an exact
F2^14 H^3(V4,U_D) vector for every free class and checks the combined image
against the already-audited total rank.
"""
import ast
import hashlib
import itertools
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parent
PICU_SCRIPT = ROOT / "extract_picu_quotient_action.py"

# Reuse the exact Stage32/source-locked Smith and Magma setup, stopping before
# the original remote request.
src = PICU_SCRIPT.read_text(encoding="utf-8")
cut = 'payload = urllib.parse.urlencode({"input": code}).encode()\n'
if src.count(cut) != 1:
    raise SystemExit("could not isolate PicU action setup prefix")
prefix = src.split(cut, 1)[0]
ns = {"__name__": "stage33_03_audit_free_d2_setup", "__file__": str(PICU_SCRIPT)}
exec(compile(prefix, str(PICU_SCRIPT) + "[audit-setup-only]", "exec"), ns)

# Export the full transformed Picard rows of the six free quotient lifts for
# each nontrivial V4 element. This is enough to act on any chosen free lift
# without printing the full 64x64 matrices.
extra = ns["extra"]
marker = 'printf "STAGE33_03_PICU_END\\n";'
if extra.count(marker) != 1:
    raise SystemExit("could not locate PicU Magma output marker")
inject = r'''
Scct := Scc*Sct;
for jj in [59..64] do
  printf "AUDIT_FREE_CC_ROW_%o=%o\n", jj-58, [Scc[jj,kk] : kk in [1..64]];
  printf "AUDIT_FREE_CT_ROW_%o=%o\n", jj-58, [Sct[jj,kk] : kk in [1..64]];
  printf "AUDIT_FREE_CCT_ROW_%o=%o\n", jj-58, [Scct[jj,kk] : kk in [1..64]];
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
        "User-Agent": "perfect-cuboid-stage33-audit/1.0",
    }, method="POST",
)
resp, magma_attempt = ns["urlopen_retry"](req, 240, "Magma calculator audit free d2_11")
with resp:
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
(ROOT / "audit-free-d2-11-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_03_PICU_END" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "Assertion failed", "User error")
):
    print(stdout)
    raise SystemExit("audit free d2_11 Picard-row materialization failed")


def full_rows(prefix):
    found = {}
    for m in re.finditer(rf"^{prefix}_(\d+)=(.+)$", stdout, re.M):
        found[int(m.group(1))] = [int(x) for x in ast.literal_eval(m.group(2).strip())]
    if set(found) != set(range(1, 7)) or any(len(v) != 64 for v in found.values()):
        raise SystemExit(f"incomplete {prefix} rows")
    return [found[j] for j in range(1, 7)]

free_pic_rows = {
    "cc": full_rows("AUDIT_FREE_CC_ROW"),
    "ct": full_rows("AUDIT_FREE_CT_ROW"),
    "cct": full_rows("AUDIT_FREE_CCT_ROW"),
}

# Exact transformed boundary action and Smith differential D=S*M*T.
S, D = ns["S"], ns["D"]
Sinv = S.inv()
if any(getattr(x, "q", 1) != 1 for x in Sinv):
    raise SystemExit("Smith left transform inverse is not integral")
raw_gal = json.loads((ROOT / "galois-action-raw.json").read_text())
h1 = json.loads((ROOT / "absolute-h1-picu-exact.json").read_text())
finite = json.loads((ROOT / "finite-transgression-ranks.json").read_text())
d201 = json.loads((ROOT / "d2-01-image.json").read_text())


def perm_matrix(perm):
    P = sp.zeros(72, 72)
    if sorted(perm) != list(range(1, 73)):
        raise SystemExit("bad boundary permutation")
    for j, v in enumerate(perm):
        P[j, v - 1] = 1
    return P

Pcc = perm_matrix([int(x) for x in raw_gal["boundary_perm_cc_1based"]])
Pct = perm_matrix([int(x) for x in raw_gal["boundary_perm_ct_1based"]])
I72 = sp.eye(72)
AD = {
    "id": I72,
    "cc": S * Pcc * Sinv,
    "ct": S * Pct * Sinv,
}
AD["cct"] = AD["cc"] * AD["ct"]
if AD["cc"] * AD["cc"] != I72 or AD["ct"] * AD["ct"] != I72 or AD["cc"] * AD["ct"] != AD["ct"] * AD["cc"]:
    raise SystemExit("transformed boundary action is not V4")
for g in ("cc", "ct", "cct"):
    if AD[g][58:72, 0:58] != sp.zeros(14, 58) or AD[g][58:72, 58:72] != sp.eye(14):
        raise SystemExit("unit kernel action is not trivial")

diag = [int(D[j, j]) for j in range(58)]
if [abs(x) for x in diag] != [1] * 56 + [2, 2]:
    raise SystemExit("unexpected Smith diagonal")

bits = {"id": (0, 0), "cc": (1, 0), "ct": (0, 1), "cct": (1, 1)}
bybits = {v: k for k, v in bits.items()}
def mul(g, h):
    return bybits[(bits[g][0] ^ bits[h][0], bits[g][1] ^ bits[h][1])]

# Act on a Picard lift supported only in the six free quotient coordinates.
def pic_act_free_lift(row64, g):
    if g == "id":
        return row64[:]
    if any(row64[j] for j in range(58)):
        raise SystemExit("pic_act_free_lift received non-free-supported row")
    out = [0] * 64
    for i in range(6):
        a = int(row64[58 + i])
        if a:
            out = [x + a * y for x, y in zip(out, free_pic_rows[g][i])]
    return out

def free6_act(v6, g):
    row = [0] * 58 + [int(x) for x in v6]
    return pic_act_free_lift(row, g)[58:64]

def add(*rows):
    return [sum(xs) for xs in zip(*rows)]
def neg(row):
    return [-x for x in row]

def lift_pic_image_row(r):
    if any(r[j] != 0 for j in range(58, 64)):
        raise SystemExit("Pic coboundary has nonzero free quotient coordinates")
    a = [0] * 72
    for j in range(58):
        if r[j] % diag[j] != 0:
            raise SystemExit(f"Pic coboundary not liftable through Smith D at {j+1}")
        a[j] = r[j] // diag[j]
    avec = sp.Matrix([a])
    if list(avec * D) != r:
        raise SystemExit("divisor lift verification failed")
    return avec

# Scalar bar complex for H^3(V4,Z)=Z/2 and a canonical parity extractor.
G = [(0, 0), (1, 0), (0, 1), (1, 1)]
def gmul(a, b): return (a[0] ^ b[0], a[1] ^ b[1])
def tuples(n): return list(itertools.product(G, repeat=n))
def differential(n):
    dom, cod = tuples(n), tuples(n + 1)
    pos = {t: i for i, t in enumerate(dom)}
    M = [[0] * len(dom) for _ in cod]
    for r, gs in enumerate(cod):
        terms = [(1, gs[1:])]
        for i in range(n):
            terms.append(((-1) ** (i + 1), gs[:i] + (gmul(gs[i], gs[i + 1]),) + gs[i + 2:]))
        terms.append(((-1) ** (n + 1), gs[:-1]))
        for sgn, t in terms:
            M[r][pos[t]] += sgn
    return sp.Matrix(M)

B2, B3 = differential(2), differential(3)
S3dm, U3dm, V3dm = smith_normal_decomp(DomainMatrix.from_Matrix(B3).convert_to(ZZ))
S3, V3 = S3dm.to_Matrix(), V3dm.to_Matrix()
r3 = B3.rank()
K3 = V3[:, r3:]
if K3.shape != (64, 12) or B3 * K3 != sp.zeros(256, 12):
    raise SystemExit("bad saturated scalar H3 kernel")
C = K3.gauss_jordan_solve(B2)[0]
if any(sp.Rational(x).q != 1 for x in C):
    raise SystemExit("bar B2 escaped integral H3 kernel")
C = sp.Matrix([[int(x) for x in row] for row in C.tolist()])
Sqdm, Uqdm, Vqdm = smith_normal_decomp(DomainMatrix.from_Matrix(C).convert_to(ZZ))
Sq, Uq = Sqdm.to_Matrix(), Uqdm.to_Matrix()
diagq = [abs(int(Sq[i, i])) for i in range(min(Sq.shape)) if Sq[i, i] != 0]
if diagq != [1] * 11 + [2]:
    raise SystemExit(f"unexpected H3(V4,Z) Smith invariants {diagq}")
pivrows = list(K3.T.rref()[1])
if len(pivrows) != 12:
    raise SystemExit("could not choose H3 kernel pivot rows")
minor = K3[pivrows, :]
minor_inv = minor.inv()
if any(sp.Rational(x).q != 1 for x in minor_inv):
    # Integral inverse is not required; coordinates below are checked integral.
    pass

def h3_bit(cvals):
    c = sp.Matrix([int(x) for x in cvals])
    if B3 * c != sp.zeros(256, 1):
        raise SystemExit("computed d2_11 target is not a scalar 3-cocycle")
    x = minor_inv * c[pivrows, :]
    if K3 * x != c or any(sp.Rational(y).q != 1 for y in x):
        raise SystemExit("scalar H3 cocycle has nonintegral kernel coordinates")
    ux = Uq * sp.Matrix([int(y) for y in x])
    return int(ux[11]) & 1

# Build each explicit free H1 cocycle, lift it to Pic, and transgress twice.
free_basis = h1["finite_free_H1_cocycle_basis"]
if len(free_basis) != 5 or finite["rank_d2_11"] != 2:
    raise SystemExit("free H1 / total d2 rank regression")
results = []
for rep in free_basis:
    a6 = [int(x) for x in rep["cc_value_free_coordinates"]]
    b6 = [int(x) for x in rep["ct_value_free_coordinates"]]
    if len(a6) != 6 or len(b6) != 6:
        raise SystemExit("bad free H1 representative width")
    # Verify the two involution relations and the commuting-square relation.
    if any(add(a6, free6_act(a6, "cc"))):
        raise SystemExit("free H1 cc involution cocycle relation failed")
    if any(add(b6, free6_act(b6, "ct"))):
        raise SystemExit("free H1 ct involution cocycle relation failed")
    cct6_a = add(free6_act(a6, "ct"), b6)
    cct6_b = add(free6_act(b6, "cc"), a6)
    if cct6_a != cct6_b:
        raise SystemExit("free H1 commuting cocycle relation failed")
    p = {
        "id": [0] * 64,
        "cc": [0] * 58 + a6,
        "ct": [0] * 58 + b6,
        "cct": [0] * 58 + cct6_a,
    }
    two = {}
    for g in bits:
        for h in bits:
            r = add(pic_act_free_lift(p[g], h), p[h], neg(p[mul(g, h)]))
            two[(g, h)] = lift_pic_image_row(r)
    three = {}
    for g in bits:
        for h in bits:
            for k in bits:
                c = two[(g, h)] * AD[k] + two[(mul(g, h), k)] - two[(g, mul(h, k))] - two[(h, k)]
                if c * D != sp.zeros(1, 64) or any(int(c[0, j]) != 0 for j in range(58)):
                    raise SystemExit("free d2_11 3-cochain escaped unit kernel")
                three[(g, h, k)] = [int(c[0, j]) for j in range(58, 72)]
    h3vec = []
    triples = tuples(3)
    label = {v: bybits[v] for v in G}
    for u in range(14):
        vals = [three[(label[g], label[h], label[k])][u] for g, h, k in triples]
        # Our right-cochain differential is the negative of the scalar left-bar
        # convention above; sign does not affect the order-two H3 class.
        h3vec.append(h3_bit(vals))
    results.append({
        "class_id": rep["class_id"],
        "h3_v4_unit_coordinates_f2": h3vec,
        "d2_11_zero": not any(h3vec),
    })


def f2_rank(rows):
    a = [[int(x) & 1 for x in row] for row in rows]
    rank = 0
    if not a:
        return 0
    for c in range(len(a[0])):
        p = next((i for i in range(rank, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[rank], a[p] = a[p], a[rank]
        for i in range(len(a)):
            if i != rank and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank

free_vectors = [r["h3_v4_unit_coordinates_f2"] for r in results]
free_rank = f2_rank(free_vectors)
torsion_vectors = [[int(x) & 1 for x in z["cc_quadratic_character_coefficients_f2"]] for z in d201["torsion_generator_images"]]
if len(torsion_vectors) != 2 or f2_rank(torsion_vectors) != 2:
    raise SystemExit("torsion d2_11 image-vector lock regression")
combined_rank = f2_rank(torsion_vectors + free_vectors)
if combined_rank != finite["rank_d2_11"]:
    raise SystemExit(f"direct combined d2_11 rank {combined_rank} != audited total {finite['rank_d2_11']}")

cert = {
    "schema": "STAGE33_03_HOSTILE_AUDIT_FREE_D2_11_DIRECT_V1",
    "audited_claim": "finite d2_11 restriction to the five H1(V4,PicU_free) classes is zero",
    "method": "direct chain-level transgression from exact Smith complex and source-locked full free-lift Picard action rows",
    "source_locks": {
        "stage32_artifact_sha256": ns["STAGE32_ARTIFACT_SHA256"],
        "stage32_core_canonical_sha256": ns["STAGE32_CORE_CANONICAL_SHA256"],
        "upstream_git_blob_sha1": ns["UPSTREAM_BLOB"],
        "galois_action_raw_sha256": raw_gal["canonical_sha256"],
        "absolute_h1_picu_exact_sha256": h1["canonical_sha256"],
        "finite_transgression_ranks_sha256": finite["canonical_sha256"],
        "d2_01_exact_image_sha256": d201["canonical_sha256"],
        "submitted_magma_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "magma_stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
    },
    "magma_request_attempt": magma_attempt,
    "scalar_H3_V4_Z": "Z/2",
    "free_class_results": results,
    "free_d2_11_image_rank_f2": free_rank,
    "free_d2_11_restriction_zero": free_rank == 0,
    "torsion_d2_11_image_rank_f2": f2_rank(torsion_vectors),
    "combined_direct_d2_11_image_rank_f2": combined_rank,
    "audited_total_d2_11_rank_f2": finite["rank_d2_11"],
    "rank_consistency_exact": True,
}
rawc = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(rawc).hexdigest()
(ROOT / "audit-free-d2-11-direct.json").write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "free_d2_11_image_rank_f2": free_rank,
    "free_d2_11_restriction_zero": free_rank == 0,
    "combined_direct_d2_11_image_rank_f2": combined_rank,
    "free_class_vectors": results,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
