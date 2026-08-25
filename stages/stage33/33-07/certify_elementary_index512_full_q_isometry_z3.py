#!/usr/bin/env python3
"""Decide the full finite quadratic-module isometry for the retained order-512 glue candidate.

The preceding elementary-candidate shard only compared necessary invariants.
This shard asks for an explicit automorphism of

    A = (Z/2)^4 + (Z/4)^6 + (Z/8)^4

carrying the candidate discriminant quadratic form to the exact endpoint
transcendental discriminant form.  The witness is solved as a finite bit-vector
problem and then independently checked with ordinary Python integer arithmetic.

Important firewall: even a positive answer here identifies only the finite
quadratic form.  It does NOT identify the actual integral index-512 K3 glue and
it does NOT prove simultaneous conjugacy of the endpoint cc/ct actions.
"""

import hashlib
import json
import math
from pathlib import Path

from z3 import BitVec, BitVecVal, Extract, Or, Solver, ULT, Xor, sat

HERE = Path(__file__).resolve().parent
CAND = json.loads((HERE / "elementary-index512-glue-candidate.json").read_text())
TGT = json.loads((HERE / "picard-discriminant-compact.json").read_text())

TARGET_LOCK = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"
if TGT["canonical_sha256"] != TARGET_LOCK:
    raise SystemExit("target discriminant compact source lock moved")
if CAND["source_locks"]["target_picard_discriminant_sha256"] != TARGET_LOCK:
    raise SystemExit("candidate target source lock moved")
if CAND["candidate_H_type"] != "(Z/2)^9" or CAND["candidate_H_order"] != 512:
    raise SystemExit("elementary glue candidate regression")
if CAND["candidate_overlattice_smith"] != [2] * 4 + [4] * 6 + [8] * 4:
    raise SystemExit("candidate Smith regression")

mods = [int(x) for x in CAND["candidate_overlattice_smith"]]
Bc = [[int(x) for x in row] for row in CAND["candidate_discriminant_B8_smith_coords"]]
Bt = [[int(x) for x in row] for row in CAND["target_transcendental_B8_smith_coords"]]
if mods != [2] * 4 + [4] * 6 + [8] * 4:
    raise SystemExit("mixed-modulus order regression")
if len(Bc) != 14 or len(Bt) != 14 or any(len(r) != 14 for r in Bc + Bt):
    raise SystemExit("quadratic matrix shape regression")

# Row i is the image of the i-th candidate Smith generator in target Smith
# coordinates.  Four bits are enough for residues 0..7 and for q numerators
# modulo 16.  Well-definedness of Z/m_i -> Z/m_j forces divisibility by
# m_j/gcd(m_i,m_j).
P = [[BitVec(f"p_{i}_{j}", 4) for j in range(14)] for i in range(14)]
s = Solver()
s.set(timeout=540000)
s.set(random_seed=0)

for i, mi in enumerate(mods):
    for j, mj in enumerate(mods):
        s.add(ULT(P[i][j], BitVecVal(mj, 4)))
        step = mj // math.gcd(mi, mj)
        if step > 1:
            s.add((P[i][j] & BitVecVal(step - 1, 4)) == BitVecVal(0, 4))


def q4(row):
    """Return x B x mod 16 as a 4-bit expression."""
    acc = BitVecVal(0, 4)
    for a in range(14):
        for b in range(14):
            acc = acc + row[a] * BitVecVal(Bt[a][b] % 16, 4) * row[b]
    return acc


def b3(row1, row2):
    """Return x B y mod 8 as a 3-bit expression."""
    acc = BitVecVal(0, 3)
    for a in range(14):
        xa = Extract(2, 0, row1[a])
        for b in range(14):
            yb = Extract(2, 0, row2[b])
            acc = acc + xa * BitVecVal(Bt[a][b] % 8, 3) * yb
    return acc


# A quadratic map is determined by q on generators and the associated bilinear
# pairing on generator pairs.  These equalities therefore certify the full
# finite quadratic form, not only value distributions on selected filtrations.
for i in range(14):
    s.add(q4(P[i]) == BitVecVal(Bc[i][i] % 16, 4))
for i in range(14):
    for j in range(i + 1, 14):
        s.add(b3(P[i], P[j]) == BitVecVal(Bc[i][j] % 8, 3))

# Endomorphisms of a finite 2-group are automorphisms iff the induced map on
# A/2A is invertible.  The order constraints make that mod-2 matrix block lower
# triangular by invariant-factor order, so it is enough to force the three
# equal-order diagonal blocks (4,6,4) to be nonsingular over F2.  We avoid a
# determinant polynomial: every nonzero row combination must be nonzero.
def bit0(x):
    return Extract(0, 0, x) == BitVecVal(1, 1)


def xor_all(values):
    out = values[0]
    for v in values[1:]:
        out = Xor(out, v)
    return out


for lo, hi in ((0, 4), (4, 10), (10, 14)):
    n = hi - lo
    for mask in range(1, 1 << n):
        nonzero_columns = []
        selected = [lo + r for r in range(n) if (mask >> r) & 1]
        for col in range(lo, hi):
            nonzero_columns.append(xor_all([bit0(P[row][col]) for row in selected]))
        s.add(Or(*nonzero_columns))

result = s.check()
if result != sat:
    raise SystemExit(f"full finite quadratic-module isometry solver result: {result}")
model = s.model()
witness = [[model.eval(P[i][j], model_completion=True).as_long() for j in range(14)] for i in range(14)]

# Independent exact verification, intentionally not using z3 expressions.
def qnum(row, B):
    return sum(row[a] * B[a][b] * row[b] for a in range(14) for b in range(14)) % 16


def bnum(row1, row2, B):
    return sum(row1[a] * B[a][b] * row2[b] for a in range(14) for b in range(14)) % 8


def gf2_rank(rows):
    piv = {}
    for row in rows:
        x = sum((int(v) & 1) << j for j, v in enumerate(row))
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                break
    return len(piv)


for i, mi in enumerate(mods):
    for j, mj in enumerate(mods):
        x = witness[i][j]
        if not (0 <= x < mj):
            raise SystemExit("witness residue range verification failed")
        if (mi * x) % mj != 0:
            raise SystemExit("witness homomorphism well-definedness failed")
for i in range(14):
    if qnum(witness[i], Bt) != Bc[i][i] % 16:
        raise SystemExit(f"witness q verification failed at generator {i}")
    for j in range(i):
        if bnum(witness[i], witness[j], Bt) != Bc[i][j] % 8:
            raise SystemExit(f"witness bilinear verification failed at pair {(i, j)}")
block_ranks = []
for lo, hi in ((0, 4), (4, 10), (10, 14)):
    block = [[witness[i][j] & 1 for j in range(lo, hi)] for i in range(lo, hi)]
    rank = gf2_rank(block)
    block_ranks.append(rank)
    if rank != hi - lo:
        raise SystemExit("witness A/2A automorphism verification failed")

cert = {
    "schema": "STAGE33_07_ELEMENTARY_INDEX512_FULL_FINITE_Q_ISOMETRY_V1",
    "stage": "33",
    "unit": "33-07",
    "source_locks": {
        "target_picard_discriminant_sha256": TARGET_LOCK,
        "elementary_candidate_sha256": CAND["canonical_sha256"],
        "scaled_coordinate_k3_action_sha256": CAND["source_locks"]["scaled_coordinate_k3_action_sha256"],
    },
    "group": "(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4",
    "source_form": "elementary index-512 candidate discriminant form",
    "target_form": "exact endpoint transcendental discriminant form",
    "explicit_isometry_matrix_rows_source_to_target": witness,
    "isometry_homomorphism_well_defined_exact": True,
    "a_mod_2_diagonal_block_ranks": block_ranks,
    "a_mod_2_automorphism_exact": True,
    "generator_q_equalities_mod16_exact": True,
    "generator_pair_bilinear_equalities_mod8_exact": True,
    "full_finite_quadratic_form_isometry_certified": True,
    "necessary_filter_only_status_upgraded": True,
    "actual_index512_glue_identified": False,
    "why_actual_glue_not_yet_identified": "finite discriminant-form isometry does not identify the actual integral overlattice embedding H inside A_L0",
    "simultaneous_endpoint_cc_ct_action_conjugacy_certified": False,
    "candidate_promoted_to_endpoint_T_lattice": False,
    "new_residual_kernel": "R33-BR2A-INDEX512-GLUE-ENDPOINT-V4-ACTION-CONJUGACY",
    "next_exact_leaf": "L33-07-LIFT-SCALED-COORDINATE-ACTIONS-THROUGH-CANDIDATE-H-AND-MATCH-ENDPOINT-CC-CT-CONJUGACY",
    "unit_status": "RUNNING_REPAIR",
    "unit_closed": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
raw = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
(HERE / "elementary-index512-full-finite-q-isometry.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "solver": "z3 finite bit-vector exact",
    "full_finite_quadratic_form_isometry_certified": True,
    "a_mod_2_block_ranks": block_ranks,
    "actual_index512_glue_identified": False,
    "simultaneous_endpoint_cc_ct_action_conjugacy_certified": False,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
