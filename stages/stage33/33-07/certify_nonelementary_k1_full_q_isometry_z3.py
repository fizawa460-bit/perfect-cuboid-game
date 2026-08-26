#!/usr/bin/env python3
"""Decide full finite-q isometry for the explicit non-elementary k=1 witness.

The witness already has the endpoint abelian invariant factors and matching
Q[2] value distribution.  This script asks for an actual mixed-modulus
automorphism carrying its complete discriminant quadratic form to the locked
endpoint form.  Either SAT or UNSAT concerns this explicit witness only; it
does not classify the full k=1 abstract branch or identify the actual glue.
"""
import hashlib
import json
import math
from pathlib import Path

from z3 import BitVec, BitVecVal, Extract, Or, Solver, ULT, Xor, sat, unsat

HERE = Path(__file__).resolve().parent
WITNESS_LOCK = "2969437c45ba713b90f0e168ccd00d1b81c465594d1dfb8a77569c5558885cd8"
TARGET_LOCK = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"

witness = json.loads((HERE / "nonelementary-exact-quotient-action-witnesses.json").read_text())
target = json.loads((HERE / "picard-discriminant-compact.json").read_text())
if witness.get("canonical_sha256") != WITNESS_LOCK:
    raise SystemExit("non-elementary witness source lock moved")
if target.get("canonical_sha256") != TARGET_LOCK:
    raise SystemExit("endpoint finite-q source lock moved")

name = "k1_Z4_plus_Z2_7"
record = witness["records"][name]
if not record["Q2_profile_matches_endpoint"]:
    raise SystemExit("k1 witness no longer passes the Q2 prefilter")
if record["twoQ_profile_matches_endpoint"]:
    raise SystemExit("k1 witness no longer has the independently locked 2Q mismatch")
mods = [int(x) for x in record["quotient_invariant_factors"]]
if mods != [2] * 4 + [4] * 6 + [8] * 4:
    raise SystemExit("mixed-modulus target regression")
Bc = [[int(x) for x in row] for row in record["source_quotient_B8_smith_coordinates"]]
Bt = [[-int(x) for x in row] for row in target["discriminant_bilinear_numerator_over_8_reduced"]]
if any(len(row) != 14 for row in Bc + Bt) or len(Bc) != 14 or len(Bt) != 14:
    raise SystemExit("finite-q matrix shape regression")

# Row i is the image of source Smith generator i in target Smith coordinates.
P = [[BitVec(f"p_{i}_{j}", 4) for j in range(14)] for i in range(14)]
solver = Solver()
solver.set(timeout=540000)
solver.set(random_seed=0)
for i, mi in enumerate(mods):
    for j, mj in enumerate(mods):
        solver.add(ULT(P[i][j], BitVecVal(mj, 4)))
        step = mj // math.gcd(mi, mj)
        if step > 1:
            solver.add((P[i][j] & BitVecVal(step - 1, 4)) == BitVecVal(0, 4))


def q4(row):
    acc = BitVecVal(0, 4)
    for a in range(14):
        for b in range(14):
            acc += row[a] * BitVecVal(Bt[a][b] % 16, 4) * row[b]
    return acc


def b3(row1, row2):
    acc = BitVecVal(0, 3)
    for a in range(14):
        xa = Extract(2, 0, row1[a])
        for b in range(14):
            acc += xa * BitVecVal(Bt[a][b] % 8, 3) * Extract(2, 0, row2[b])
    return acc


for i in range(14):
    solver.add(q4(P[i]) == BitVecVal(Bc[i][i] % 16, 4))
    for j in range(i):
        solver.add(b3(P[i], P[j]) == BitVecVal(Bc[i][j] % 8, 3))


def bit0(x):
    return Extract(0, 0, x) == BitVecVal(1, 1)


def xor_all(values):
    out = values[0]
    for value in values[1:]:
        out = Xor(out, value)
    return out


for lo, hi in ((0, 4), (4, 10), (10, 14)):
    for mask in range(1, 1 << (hi - lo)):
        selected = [lo + r for r in range(hi - lo) if (mask >> r) & 1]
        solver.add(Or(*[
            xor_all([bit0(P[row][col]) for row in selected])
            for col in range(lo, hi)
        ]))

result = solver.check()
if result not in (sat, unsat):
    raise SystemExit(f"full finite-q solver non-decision: {result}")


def qnum(row, B):
    return sum(row[a] * B[a][b] * row[b] for a in range(14) for b in range(14)) % 16


def bnum(row1, row2, B):
    return sum(row1[a] * B[a][b] * row2[b] for a in range(14) for b in range(14)) % 8


def gf2_rank(rows):
    pivots = {}
    for row in rows:
        x = sum((int(value) & 1) << j for j, value in enumerate(row))
        while x:
            pivot = x.bit_length() - 1
            if pivot in pivots:
                x ^= pivots[pivot]
            else:
                pivots[pivot] = x
                break
    return len(pivots)


matrix = None
block_ranks = None
if result == sat:
    model = solver.model()
    matrix = [[model.eval(P[i][j], model_completion=True).as_long() for j in range(14)] for i in range(14)]
    for i, mi in enumerate(mods):
        for j, mj in enumerate(mods):
            if not 0 <= matrix[i][j] < mj or (mi * matrix[i][j]) % mj:
                raise SystemExit("isometry homomorphism verification failed")
        if qnum(matrix[i], Bt) != Bc[i][i] % 16:
            raise SystemExit("isometry q verification failed")
        for j in range(i):
            if bnum(matrix[i], matrix[j], Bt) != Bc[i][j] % 8:
                raise SystemExit("isometry bilinear verification failed")
    block_ranks = []
    for lo, hi in ((0, 4), (4, 10), (10, 14)):
        block = [[matrix[i][j] & 1 for j in range(lo, hi)] for i in range(lo, hi)]
        block_ranks.append(gf2_rank(block))
    if block_ranks != [4, 6, 4]:
        raise SystemExit("isometry A/2A verification failed")

certificate = {
    "schema": "STAGE33_07_NONELEMENTARY_K1_FULL_FINITE_Q_ISOMETRY_V1",
    "source_locks": {
        "nonelementary_exact_witness_sha256": WITNESS_LOCK,
        "endpoint_picard_discriminant_sha256": TARGET_LOCK,
    },
    "witness_name": name,
    "group": "(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4",
    "solver": "z3 finite bit-vector exact",
    "solver_result": str(result).upper(),
    "full_finite_quadratic_form_isometry_certified_for_this_witness": result == sat,
    "explicit_isometry_matrix_rows_source_to_target": matrix,
    "a_mod_2_diagonal_block_ranks": block_ranks,
    "specific_witness_rejected": result == unsat,
    "independent_2Q_profile_rejection_source_locked": True,
    "abstract_k1_type_rejected": False,
    "actual_index512_glue_identified": False,
    "endpoint_full_action_conjugacy_certified": False,
    "arithmetic_HS_closed": False,
    "next_exact_leaf": (
        "L33-07-TRANSPORT-CC-CT-SEVEN-SIGNS-THROUGH-K1-FINITE-Q-ISOMETRIES-AND-TEST-SIMULTANEOUS-ENDPOINT-CONJUGACY"
        if result == sat else
        "L33-07-SEARCH-K1-STRUCTURAL-BRANCH-FOR-ANOTHER-Q-FILTRATION-COMPATIBLE-WITNESS-OR-PROVE-TYPE-REJECTION"
    ),
    "unit_status": "RUNNING_REPAIR",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "stage33_09_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
raw = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
certificate["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
(HERE / "nonelementary-k1-full-q-isometry.json").write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + "\n"
)
print(json.dumps({
    "success": True,
    "solver_result": certificate["solver_result"],
    "full_finite_q_isometry": certificate["full_finite_quadratic_form_isometry_certified_for_this_witness"],
    "specific_witness_rejected": certificate["specific_witness_rejected"],
    "certificate_sha256": certificate["canonical_sha256"],
    "next": certificate["next_exact_leaf"],
}, indent=2, sort_keys=True))
