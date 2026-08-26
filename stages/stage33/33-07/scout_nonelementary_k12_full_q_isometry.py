#!/usr/bin/env python3
"""Deterministic exact full-finite-q scout on retained k1/k2 Q2+2Q survivors.

This leaf deliberately samples only a small quantile-spaced set of the exact
104,028 full source-symmetry orbit representatives.  For each sampled H it
reconstructs the actual subgroup in A0=(Z/8)^10+(Z/16)^4, computes H^perp/H by
an integral-kernel plus Smith decomposition, transports the discriminant
pairing to Smith coordinates, and runs the same exact mixed-modulus Z3
finite-quadratic-module isometry test already used by the elementary q256
census.

The output is a scouting certificate only.  SAT/UNSAT is exact for sampled
records, but no unsampled candidate is classified and no endpoint/glue/HS
credit is granted.
"""
import hashlib
import json
import math
import os
import struct
import time
from collections import Counter
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp
from z3 import BitVec, BitVecVal, Extract, Or, Solver, ULT, Xor, sat, unsat

HERE = Path(__file__).resolve().parent
MODS0 = [8] * 10 + [16] * 4
QDIAG = [2] * 10 + [1] * 4
TARGET_MODS = [2] * 4 + [4] * 6 + [8] * 4
RECORD = struct.Struct("<BHI")
Q2_CERT_LOCK = "18d33892d04de286bfa8aa006fb8e4d133d7b51472e950c51bc74cc67a366300"
Q2_BIN_LOCK = "4eebb36004d88917a233a7f449056e9d20082de94018d9ce4b48bbbbfe144c36"
TARGET_Q_LOCK = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"
K1_CERT_LOCK = "702758b2c085db70b48577531377b5c8dace827f3080f43486fbcf0fd0605cf2"
K2_CERT_LOCK = "cfa87933b595744811b8ea2e04bf71ea39b75b0c3a9255437c4bc507b3846a95"
IN_CERT = HERE / "nonelementary-k12-exact-q2-2q-profile-filter.json"
IN_BIN = HERE / "nonelementary-k12-exact-q2-2q-profile-surviving-orbits.bin"
OUT = HERE / "nonelementary-k12-full-q-isometry-scout.json"


def canonical_sha(doc):
    d = dict(doc)
    stored = d.pop("canonical_sha256", None)
    raw = json.dumps(d, sort_keys=True, separators=(",", ":")).encode()
    return stored, hashlib.sha256(raw).hexdigest()


q2cert = json.loads(IN_CERT.read_text())
stored, rehash = canonical_sha(q2cert)
if stored != rehash or stored != Q2_CERT_LOCK:
    raise SystemExit("Q2 retained certificate hash regression")
binary = IN_BIN.read_bytes()
if hashlib.sha256(binary).hexdigest() != Q2_BIN_LOCK:
    raise SystemExit("Q2 survivor binary hash regression")
if len(binary) != 104028 * RECORD.size:
    raise SystemExit("Q2 survivor binary framing regression")

sources = {
    1: json.loads((HERE / "nonelementary-k1-q2-2q-cc-orbits.json").read_text()),
    2: json.loads((HERE / "nonelementary-k2-q2-2q-skeleton-orbits.json").read_text()),
}
if sources[1].get("canonical_sha256") != K1_CERT_LOCK:
    raise SystemExit("k1 skeleton source lock moved")
if sources[2].get("canonical_sha256") != K2_CERT_LOCK:
    raise SystemExit("k2 skeleton source lock moved")

target = json.loads((HERE / "picard-discriminant-compact.json").read_text())
if target.get("canonical_sha256") != TARGET_Q_LOCK:
    raise SystemExit("endpoint finite-q source lock moved")
TARGET_B8 = [[
    -int(x) % (16 if i == j else 8) for j, x in enumerate(row)
] for i, row in enumerate(target["discriminant_bilinear_numerator_over_8_reduced"])]


def canon(rows):
    pivots = {}
    for raw in rows:
        row = int(raw)
        for pivot in sorted(pivots, reverse=True):
            if (row >> pivot) & 1:
                row ^= pivots[pivot]
        if not row:
            continue
        pivot = row.bit_length() - 1
        for old in list(pivots):
            if (pivots[old] >> pivot) & 1:
                pivots[old] ^= row
        pivots[pivot] = row
    return tuple(pivots[p] for p in sorted(pivots, reverse=True))


def complement(base, whole):
    current = list(canon(base))
    out = []
    for vector in canon(whole):
        before = len(canon(current))
        after = canon(current + [vector])
        if len(after) > before:
            current.append(vector)
            out.append(vector)
    return tuple(out)


def order4_corrections(p_basis, quotient_basis, solution):
    q = len(quotient_basis)
    out = []
    for generator in range(len(p_basis)):
        correction = 0
        for bit, vector in enumerate(quotient_basis):
            if (int(solution) >> (q * generator + bit)) & 1:
                correction ^= int(vector)
        out.append(correction)
    return tuple(out)


def actual_row(low_bits, high_bits):
    row = []
    for j in range(14):
        normalized = ((int(low_bits) >> j) & 1) + 2 * ((int(high_bits) >> j) & 1)
        scale = 2 if j < 10 else 4
        row.append((scale * normalized) % MODS0[j])
    return tuple(row)


def actual_order2_row(bits):
    return tuple((4 if j < 10 else 8) if ((int(bits) >> j) & 1) else 0 for j in range(14))


def reconstruct_rows(kind, skeleton_index, solution):
    rep = sources[kind]["orbit_representatives"][int(skeleton_index)]
    p_basis = tuple(map(int, rep["P_basis_bits"]))
    w_basis = tuple(map(int, rep["W_basis_bits"]))
    if len(p_basis) != kind or len(w_basis) != 9 - kind:
        raise SystemExit("skeleton type regression")
    quotient_basis = complement(w_basis, canon(1 << j for j in range(14)))
    corrections = order4_corrections(p_basis, quotient_basis, solution)
    rows = [actual_row(p, c) for p, c in zip(p_basis, corrections)]
    rows.extend(actual_order2_row(w) for w in complement(p_basis, w_basis))
    expected = 9 - kind
    if len(rows) != expected:
        raise SystemExit(f"generator-count regression k{kind}: {len(rows)} != {expected}")
    return rows


def q32(a):
    return sum(c * int(x) * int(x) for c, x in zip(QDIAG, a)) % 32


def b16(a, b):
    return sum(c * int(x) * int(y) for c, x, y in zip(QDIAG, a, b)) % 16


def verify_isotropic(rows):
    for i, row in enumerate(rows):
        if q32(row):
            raise SystemExit("reconstructed H generator is not isotropic")
        for j in range(i):
            if b16(row, rows[j]):
                raise SystemExit("reconstructed H generators are not orthogonal")


def quotient_data(rows):
    count = len(rows)
    congruences = [[int(h[j]) * (16 // MODS0[j]) for j in range(14)] for h in rows]
    augmented = sp.Matrix([
        congruences[i] + [-16 * int(i == j) for j in range(count)]
        for i in range(count)
    ])
    diagonal, left, right = smith_normal_decomp(augmented, domain=ZZ)
    if left * augmented * right != diagonal:
        raise SystemExit("orthogonal-kernel Smith transform regression")
    rank = sum(diagonal[i, i] != 0 for i in range(min(diagonal.shape)))
    basis = sp.Matrix([
        [int(right[i, j]) for i in range(14)]
        for j in range(rank, right.cols)
    ])
    if basis.shape != (14, 14) or abs(int(basis.det())) != 512:
        raise SystemExit("orthogonal-kernel basis/index regression")
    basis_inverse = basis.inv()

    relation_rows = []
    for j, modulus in enumerate(MODS0):
        period = [0] * 14
        period[j] = modulus
        relation_rows.append(period)
    relation_rows.extend(rows)
    coordinates = []
    for relation in relation_rows:
        vector = sp.Matrix([relation]) * basis_inverse
        if any(x.q != 1 for x in vector):
            raise SystemExit("H/ambient relation is not integral in Hperp basis")
        coordinates.append([int(x) for x in vector])
    relations = sp.Matrix(coordinates)
    qdiag, qleft, qright = smith_normal_decomp(relations, domain=ZZ)
    if qleft * relations * qright != qdiag:
        raise SystemExit("quotient Smith transform regression")
    invariant_factors = [abs(int(qdiag[i, i])) for i in range(14)]
    if invariant_factors != TARGET_MODS:
        raise SystemExit(f"quotient invariant-factor regression: {invariant_factors}")

    pairing16 = sp.zeros(14)
    for a in range(14):
        for b in range(14):
            pairing16[a, b] = sum(
                (16 // MODS0[j]) * int(basis[a, j]) * int(basis[b, j])
                for j in range(14)
            )
    right_inverse = qright.inv()
    transported16 = right_inverse * pairing16 * right_inverse.T
    if any(int(transported16[i, j]) % 2 for i in range(14) for j in range(14)):
        raise SystemExit("quotient pairing denominator regression")
    pairing8 = [[
        int(transported16[i, j] // 2) % (16 if i == j else 8)
        for j in range(14)
    ] for i in range(14)]
    return pairing8


def qnum(row, B):
    return sum(row[a] * B[a][b] * row[b] for a in range(14) for b in range(14)) % 16


def bnum(x, y, B):
    return sum(x[a] * B[a][b] * y[b] for a in range(14) for b in range(14)) % 8


def gf2_rank(rows):
    pivots = {}
    for row in rows:
        x = sum((int(v) & 1) << j for j, v in enumerate(row))
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def solve_isometry(Bc, timeout_ms):
    P = [[BitVec(f"p_{i}_{j}", 4) for j in range(14)] for i in range(14)]
    solver = Solver()
    solver.set(timeout=timeout_ms)
    solver.set(random_seed=0)
    for i, mi in enumerate(TARGET_MODS):
        for j, mj in enumerate(TARGET_MODS):
            solver.add(ULT(P[i][j], BitVecVal(mj, 4)))
            step = mj // math.gcd(mi, mj)
            if step > 1:
                solver.add((P[i][j] & BitVecVal(step - 1, 4)) == BitVecVal(0, 4))

    def q4(row):
        z = BitVecVal(0, 4)
        for a in range(14):
            for b in range(14):
                z = z + row[a] * BitVecVal(TARGET_B8[a][b] % 16, 4) * row[b]
        return z

    def b3(x, y):
        z = BitVecVal(0, 3)
        for a in range(14):
            xa = Extract(2, 0, x[a])
            for b in range(14):
                z = z + xa * BitVecVal(TARGET_B8[a][b] % 8, 3) * Extract(2, 0, y[b])
        return z

    for i in range(14):
        solver.add(q4(P[i]) == BitVecVal(Bc[i][i] % 16, 4))
    for i in range(14):
        for j in range(i):
            solver.add(b3(P[i], P[j]) == BitVecVal(Bc[i][j] % 8, 3))

    def bit0(x):
        return Extract(0, 0, x) == BitVecVal(1, 1)

    def xorall(values):
        z = values[0]
        for value in values[1:]:
            z = Xor(z, value)
        return z

    for lo, hi in ((0, 4), (4, 10), (10, 14)):
        n = hi - lo
        for mask in range(1, 1 << n):
            selected = [lo + r for r in range(n) if (mask >> r) & 1]
            solver.add(Or(*[
                xorall([bit0(P[r][c]) for r in selected])
                for c in range(lo, hi)
            ]))

    t0 = time.perf_counter()
    result = solver.check()
    elapsed = time.perf_counter() - t0
    if result == unsat:
        return "UNSAT", None, elapsed
    if result != sat:
        return "UNKNOWN", None, elapsed
    model = solver.model()
    W = [[model.eval(P[i][j], model_completion=True).as_long() for j in range(14)] for i in range(14)]
    for i, mi in enumerate(TARGET_MODS):
        for j, mj in enumerate(TARGET_MODS):
            if not (0 <= W[i][j] < mj) or (mi * W[i][j]) % mj:
                raise SystemExit("SAT witness hom verification failed")
    for i in range(14):
        if qnum(W[i], TARGET_B8) != Bc[i][i] % 16:
            raise SystemExit("SAT witness q verification failed")
        for j in range(i):
            if bnum(W[i], W[j], TARGET_B8) != Bc[i][j] % 8:
                raise SystemExit("SAT witness b verification failed")
    ranks = []
    for lo, hi in ((0, 4), (4, 10), (10, 14)):
        ranks.append(gf2_rank([[W[i][j] & 1 for j in range(lo, hi)] for i in range(lo, hi)]))
    if ranks != [4, 6, 4]:
        raise SystemExit("SAT witness automorphism rank regression")
    witness_hash = hashlib.sha256(json.dumps(W, separators=(",", ":")).encode()).hexdigest()
    return "SAT", witness_hash, elapsed


def quantile_sample(records, n):
    if n <= 0 or not records:
        return []
    if n >= len(records):
        return list(records)
    if n == 1:
        return [records[len(records) // 2]]
    indices = []
    for i in range(n):
        idx = (i * (len(records) - 1)) // (n - 1)
        if not indices or idx != indices[-1]:
            indices.append(idx)
    return [records[i] for i in indices]


all_records = {1: [], 2: []}
for ordinal, offset in enumerate(range(0, len(binary), RECORD.size)):
    kind, skeleton_index, solution = RECORD.unpack_from(binary, offset)
    if kind not in all_records:
        raise SystemExit(f"unexpected kind in Q2 survivor binary: {kind}")
    all_records[kind].append((ordinal, int(skeleton_index), int(solution)))
if len(all_records[1]) != 28076 or len(all_records[2]) != 75952:
    raise SystemExit("Q2 survivor kind-count regression")

sample_per_kind = int(os.environ.get("SAMPLE_PER_KIND", "8"))
timeout_ms = int(os.environ.get("Z3_TIMEOUT_MS", "60000"))
selected = []
for kind in (1, 2):
    selected.extend((kind,) + record for record in quantile_sample(all_records[kind], sample_per_kind))

cache = {}
results = []
status_counts = Counter()
kind_counts = {"k1": Counter(), "k2": Counter()}
for kind, ordinal, skeleton_index, solution in selected:
    t0 = time.perf_counter()
    rows = reconstruct_rows(kind, skeleton_index, solution)
    verify_isotropic(rows)
    B8 = quotient_data(rows)
    quotient_seconds = time.perf_counter() - t0
    bkey = hashlib.sha256(json.dumps(B8, separators=(",", ":")).encode()).hexdigest()
    if bkey not in cache:
        status, witness_hash, solve_seconds = solve_isometry(B8, timeout_ms)
        cache[bkey] = (status, witness_hash, solve_seconds)
    else:
        status, witness_hash, solve_seconds = cache[bkey]
    status_counts[status] += 1
    kind_counts[f"k{kind}"][status] += 1
    results.append({
        "kind": kind,
        "binary_record_ordinal": ordinal,
        "skeleton_orbit_index": skeleton_index,
        "affine_solution_mask": solution,
        "b8_sha256": bkey,
        "full_q_isometry_status": status,
        "sat_witness_sha256": witness_hash,
        "quotient_seconds": round(quotient_seconds, 6),
        "solver_seconds_for_distinct_b8": round(solve_seconds, 6),
    })

certificate = {
    "schema": "STAGE33_07_NONELEMENTARY_K12_FULL_Q_ISOMETRY_SCOUT_V1",
    "source_q2_certificate_sha256": Q2_CERT_LOCK,
    "source_q2_survivor_binary_sha256": Q2_BIN_LOCK,
    "source_q2_survivor_record_count": 104028,
    "source_counts": {"k1": 28076, "k2": 75952},
    "source_k1_skeleton_certificate_sha256": K1_CERT_LOCK,
    "source_k2_skeleton_certificate_sha256": K2_CERT_LOCK,
    "source_endpoint_picard_discriminant_sha256": TARGET_Q_LOCK,
    "sample_strategy": "deterministic quantile-spaced records independently within k1 and k2",
    "sample_per_kind_requested": sample_per_kind,
    "sample_count": len(selected),
    "distinct_raw_B8_matrices_in_sample": len(cache),
    "status_counts": dict(sorted(status_counts.items())),
    "status_counts_by_kind": {k: dict(sorted(v.items())) for k, v in kind_counts.items()},
    "z3_timeout_ms_per_distinct_B8": timeout_ms,
    "results": results,
    "sampled_full_q_isometry_exact_where_status_is_SAT_or_UNSAT": True,
    "full_q_exhaustive_certified": False,
    "endpoint_finite_q_certified": False,
    "endpoint_full_action_certified": False,
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "next_exact_leaf": "L33-07-USE-FULL-Q-SCOUT-TO-CHOOSE-EXHAUSTIVE-CLASSIFICATION-OR-ACTION-FIRST",
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
OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "sample_count": certificate["sample_count"],
    "distinct_raw_B8": certificate["distinct_raw_B8_matrices_in_sample"],
    "status_counts": certificate["status_counts"],
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
