#!/usr/bin/env python3
"""Exact full finite-q plus simultaneous endpoint V4 census on 33 k1 survivors.

The predecessor exhaustively classified all 104,028 k1/k2 Q[2]+2Q profile
survivors by characteristic action-filtration invariants and retained exactly
33 k1 full source-symmetry orbit representatives.  This leaf reconstructs each
H <= A0, computes Q=H^perp/H and its exact quadratic form, transports all
retained scaled cc/ct action classes, and asks one mixed-modulus SMT query for
a single isometry P that simultaneously preserves the full finite quadratic
module and intertwines both endpoint V4 generators.

UNSAT is therefore an exact rejection of that H.  SAT witnesses are
independently checked with ordinary integer arithmetic.  No actual glue or
arithmetic Hochschild-Serre credit is granted by this finite calculation.
"""
import hashlib
import json
import math
import os
import runpy
import struct
import time
from collections import Counter
from pathlib import Path

import sympy as sp
from z3 import And, BitVec, BitVecVal, Extract, Or, Solver, ULT, Xor, sat, unsat

HERE = Path(__file__).resolve().parent
ACTION_CERT = HERE / "nonelementary-k12-action-filtration-certified.json"
ACTION_BIN = HERE / "nonelementary-k12-action-filtration-survivors.bin"
OUT = HERE / "nonelementary-k1-action33-simultaneous-q-v4-certified.json"
RECORD = struct.Struct("<BHI")

ACTION_CERT_LOCK = "24d7ba71fbde251960543376735adc0bbae89042ec696e5b5f37d251fe658424"
ACTION_BIN_LOCK = "aca9bf325b2ade00fd8c1abda4b5129847661ce328af89bda1a403493e07df82"
K3_CERT_LOCK = "d94ade52089dbed370bb89f747a592738da82ef65372444828a2f0d5836d419b"
TARGET_LOCK = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"
ACTION_LOCK = "a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20"
MODS0 = [8] * 10 + [16] * 4
MODS = [2] * 4 + [4] * 6 + [8] * 4

def canonical_rehash(doc):
    d = dict(doc)
    stored = d.pop("canonical_sha256", None)
    got = hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return stored, got

pred = json.loads(ACTION_CERT.read_text())
stored, got = canonical_rehash(pred)
if stored != got or stored != ACTION_CERT_LOCK:
    raise SystemExit("action-filtration predecessor certificate moved")
if pred.get("survivor_count") != 33 or pred.get("survivor_count_by_kind") != {"k1": 33, "k2": 0}:
    raise SystemExit("action-filtration predecessor survivor count moved")
if not pred.get("full_action_filtration_exhaustive_certified"):
    raise SystemExit("action-filtration predecessor is not exhaustive")

raw_survivors = ACTION_BIN.read_bytes()
if len(raw_survivors) != 33 * RECORD.size:
    raise SystemExit("action survivor binary framing regression")
if hashlib.sha256(raw_survivors).hexdigest() != ACTION_BIN_LOCK:
    raise SystemExit("action survivor binary hash regression")
records = [RECORD.unpack_from(raw_survivors, i) for i in range(0, len(raw_survivors), RECORD.size)]
if any(kind != 1 for kind, _, _ in records):
    raise SystemExit("non-k1 record survived predecessor")

k3 = json.loads((HERE / "nonelementary-k3-full-q4-retained.json").read_text())
if k3.get("certificate_canonical_sha256") != K3_CERT_LOCK:
    raise SystemExit("k3 retained certificate moved")
if not k3.get("full_target_Q4_condition_certified_for_k3") or not k3.get("k3_abstract_type_rejected"):
    raise SystemExit("k3 exact rejection lock moved")

# Reuse the exact action transport / materialized-H decoder. Force zero scout
# samples so importing the namespace performs only source-lock regressions.
old_n = os.environ.get("SAMPLE_PER_KIND")
old_t = os.environ.get("Z3_TIMEOUT_MS")
os.environ["SAMPLE_PER_KIND"] = "0"
os.environ["Z3_TIMEOUT_MS"] = "1"
ns = runpy.run_path(str(HERE / "scout_nonelementary_k12_action_filtration.py"))
if old_n is None:
    os.environ.pop("SAMPLE_PER_KIND", None)
else:
    os.environ["SAMPLE_PER_KIND"] = old_n
if old_t is None:
    os.environ.pop("Z3_TIMEOUT_MS", None)
else:
    os.environ["Z3_TIMEOUT_MS"] = old_t

if ns["ACTION_LOCK"] != ACTION_LOCK or ns["TARGET_LOCK"] != TARGET_LOCK:
    raise SystemExit("imported action/target source lock moved")
reconstruct_rows = ns["reconstruct_rows"]
verify_isotropic = ns["verify_isotropic"]
subgroup = ns["subgroup"]
quotient_context = ns["quotient_context"]
classes = ns["classes"]
sig = ns["sig"]
jsig = ns["jsig"]
compose = ns["compose"]
TCC = ns["TCC"]
TCT = ns["TCT"]
TJ = ns["TJ"]
CCt = ns["CCt"]
CTt = ns["CTt"]
base = ns["base"]
TARGET_B8 = base["TARGET_B8"]
qnum = base["qnum"]
bnum = base["bnum"]
gf2_rank = base["gf2_rank"]

def pairing8_from_context(B, Ti):
    pairing16 = sp.zeros(14)
    for a in range(14):
        for b in range(14):
            pairing16[a, b] = sum(
                (16 // MODS0[j]) * int(B[a, j]) * int(B[b, j])
                for j in range(14)
            )
    transported16 = Ti * pairing16 * Ti.T
    if any(int(transported16[i, j]) % 2 for i in range(14) for j in range(14)):
        raise SystemExit("quotient pairing denominator regression")
    return [[
        int(transported16[i, j] // 2) % (16 if i == j else 8)
        for j in range(14)
    ] for i in range(14)]

def zsum(values, bits=4):
    z = BitVecVal(0, bits)
    for value in values:
        z = z + value
    return z

def bit0(x):
    return Extract(0, 0, x) == BitVecVal(1, 1)

def xorall(values):
    z = values[0]
    for value in values[1:]:
        z = Xor(z, value)
    return z

def solve_simultaneous(Bs, ccclasses, ctclasses, prefix, timeout_ms):
    P = [[BitVec(f"{prefix}_p_{i}_{j}", 4) for j in range(14)] for i in range(14)]
    solver = Solver()
    solver.set(timeout=timeout_ms)
    solver.set(random_seed=0)

    for i, mi in enumerate(MODS):
        for j, mj in enumerate(MODS):
            solver.add(ULT(P[i][j], BitVecVal(mj, 4)))
            step = mj // math.gcd(mi, mj)
            if step > 1:
                solver.add((P[i][j] & BitVecVal(step - 1, 4)) == BitVecVal(0, 4))

    def q4(row):
        return zsum([
            row[a] * BitVecVal(TARGET_B8[a][b] % 16, 4) * row[b]
            for a in range(14) for b in range(14)
        ])

    def b3(x, y):
        z = BitVecVal(0, 3)
        for a in range(14):
            xa = Extract(2, 0, x[a])
            for b in range(14):
                z = z + xa * BitVecVal(TARGET_B8[a][b] % 8, 3) * Extract(2, 0, y[b])
        return z

    for i in range(14):
        solver.add(q4(P[i]) == BitVecVal(Bs[i][i] % 16, 4))
    for i in range(14):
        for j in range(i):
            solver.add(b3(P[i], P[j]) == BitVecVal(Bs[i][j] % 8, 3))

    for lo, hi in ((0, 4), (4, 10), (10, 14)):
        n = hi - lo
        for mask in range(1, 1 << n):
            selected = [lo + r for r in range(n) if (mask >> r) & 1]
            solver.add(Or(*[
                xorall([bit0(P[r][c]) for r in selected])
                for c in range(lo, hi)
            ]))

    def intertwine_constraints(source_action, target_action):
        conditions = []
        for i in range(14):
            for j, mj in enumerate(MODS):
                left = zsum([
                    BitVecVal(int(source_action[i][k]) % 16, 4) * P[k][j]
                    for k in range(14)
                ])
                right = zsum([
                    P[i][k] * BitVecVal(int(target_action[k][j]) % 16, 4)
                    for k in range(14)
                ])
                conditions.append(
                    ((left - right) & BitVecVal(mj - 1, 4)) == BitVecVal(0, 4)
                )
        return And(*conditions)

    if not ccclasses or not ctclasses:
        raise SystemExit("empty necessary action class list entered simultaneous solver")
    solver.add(Or(*[intertwine_constraints(A, CCt) for A, _ in ccclasses]))
    solver.add(Or(*[intertwine_constraints(A, CTt) for A, _ in ctclasses]))

    t0 = time.perf_counter()
    result = solver.check()
    elapsed = time.perf_counter() - t0
    if result == unsat:
        return "UNSAT", None, [], [], elapsed
    if result != sat:
        return "UNKNOWN", None, [], [], elapsed

    model = solver.model()
    W = [[model.eval(P[i][j], model_completion=True).as_long() for j in range(14)] for i in range(14)]
    for i, mi in enumerate(MODS):
        for j, mj in enumerate(MODS):
            if not (0 <= W[i][j] < mj) or (mi * W[i][j]) % mj:
                raise SystemExit("SAT witness hom verification failed")
    for i in range(14):
        if qnum(W[i], TARGET_B8) != Bs[i][i] % 16:
            raise SystemExit("SAT witness q verification failed")
        for j in range(i):
            if bnum(W[i], W[j], TARGET_B8) != Bs[i][j] % 8:
                raise SystemExit("SAT witness bilinear verification failed")
    ranks = []
    for lo, hi in ((0, 4), (4, 10), (10, 14)):
        ranks.append(gf2_rank([[W[i][j] & 1 for j in range(lo, hi)] for i in range(lo, hi)]))
    if ranks != [4, 6, 4]:
        raise SystemExit("SAT witness automorphism rank regression")

    def intertwines(source_action, target_action):
        for i in range(14):
            for j, mj in enumerate(MODS):
                left = sum(int(source_action[i][k]) * W[k][j] for k in range(14)) % mj
                right = sum(W[i][k] * int(target_action[k][j]) for k in range(14)) % mj
                if left != right:
                    return False
        return True

    cm = [i for i, (A, _) in enumerate(ccclasses) if intertwines(A, CCt)]
    tm = [i for i, (A, _) in enumerate(ctclasses) if intertwines(A, CTt)]
    if not cm or not tm:
        raise SystemExit("SAT witness failed independent simultaneous action verification")
    witness_hash = hashlib.sha256(json.dumps(W, separators=(",", ":")).encode()).hexdigest()
    return "SAT", witness_hash, cm, tm, elapsed

timeout_ms = int(os.environ.get("Z3_TIMEOUT_MS", "120000"))
results = []
status_counts = Counter()
total_solver_seconds = 0.0

for ordinal, (kind, skeleton_index, solution) in enumerate(records):
    rows = reconstruct_rows(kind, skeleton_index, solution)
    verify_isotropic(rows)
    H = subgroup(rows, kind)
    B, Bi, T, Ti = quotient_context(rows)
    Bs = pairing8_from_context(B, Ti)

    cc_all = classes(rows, "cc", B, Bi, T, Ti, H)
    ct_all = classes(rows, "ct", B, Bi, T, Ti, H)
    cc_fixed = [(A, m) for A, m in cc_all if sig(A) == TCC]
    ct_fixed = [(A, m) for A, m in ct_all if sig(A) == TCT]

    cc_keep = set()
    ct_keep = set()
    pair_count = 0
    for ci, (A, _) in enumerate(cc_fixed):
        for ti, (C, _) in enumerate(ct_fixed):
            if compose(A, C) == compose(C, A) and jsig(A, C) == TJ:
                cc_keep.add(ci)
                ct_keep.add(ti)
                pair_count += 1
    if not pair_count:
        raise SystemExit("predecessor ACTION_FILTRATION_MATCH record lost its joint pair")
    cc_joint = [cc_fixed[i] for i in sorted(cc_keep)]
    ct_joint = [ct_fixed[i] for i in sorted(ct_keep)]

    status, witness_hash, cm, tm, elapsed = solve_simultaneous(
        Bs, cc_joint, ct_joint, f"r{ordinal}", timeout_ms
    )
    if status == "UNKNOWN":
        raise SystemExit(f"simultaneous finite-q/V4 solver timed out on record {ordinal}")
    total_solver_seconds += elapsed
    status_counts[status] += 1
    results.append({
        "ordinal": ordinal,
        "kind": kind,
        "skeleton_orbit_index": int(skeleton_index),
        "affine_solution_mask": int(solution),
        "cc_induced_class_count": len(cc_all),
        "ct_induced_class_count": len(ct_all),
        "cc_fixed_filtration_class_count": len(cc_fixed),
        "ct_fixed_filtration_class_count": len(ct_fixed),
        "joint_filtration_pair_count": pair_count,
        "cc_joint_participating_class_count": len(cc_joint),
        "ct_joint_participating_class_count": len(ct_joint),
        "status": status,
        "solver_seconds": round(elapsed, 6),
        "sat_witness_sha256": witness_hash,
        "sat_matching_cc_class_indices": cm,
        "sat_matching_ct_class_indices": tm,
    })

survivors = [r for r in results if r["status"] == "SAT"]
nonelementary_eliminated = len(survivors) == 0
cert = {
    "schema": "STAGE33_07_NONELEMENTARY_K1_ACTION33_SIMULTANEOUS_FULL_Q_V4_EXACT_V1",
    "source_action_filtration_certificate_sha256": ACTION_CERT_LOCK,
    "source_action_filtration_survivor_binary_sha256": ACTION_BIN_LOCK,
    "source_action_filtration_input_count": 104028,
    "source_action_filtration_survivor_count": 33,
    "source_action_filtration_survivor_count_by_kind": {"k1": 33, "k2": 0},
    "source_k3_full_q4_certificate_sha256": K3_CERT_LOCK,
    "source_action_sha256": ACTION_LOCK,
    "source_endpoint_sha256": TARGET_LOCK,
    "records_checked": 33,
    "records_checked_by_kind": {"k1": 33, "k2": 0},
    "all_33_action_filtration_survivors_checked_exactly_once": True,
    "single_isometry_simultaneously_constrains_full_q_cc_ct": True,
    "sat_witnesses_independently_verified": True,
    "z3_timeout_ms_per_record": timeout_ms,
    "total_solver_seconds": round(total_solver_seconds, 6),
    "status_counts": dict(sorted(status_counts.items())),
    "survivor_count": len(survivors),
    "survivors": survivors,
    "k2_type_eliminated_by_predecessor_action_filtration": True,
    "k3_type_eliminated_by_exact_full_q4": True,
    "k1_type_eliminated_by_simultaneous_full_q_v4": nonelementary_eliminated,
    "all_non_elementary_index512_types_eliminated": nonelementary_eliminated,
    "full_finite_q_plus_simultaneous_v4_exact_on_all_action_filtration_survivors": True,
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "stage33_09_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
    "next_exact_leaf": (
        "L33-07-REDUCE-TO-ELEMENTARY-REP88-AND-TEST-ACTUAL-GLUE-HS-COMPATIBILITY"
        if nonelementary_eliminated
        else "L33-07-IMPOSE-SEVEN-SIGN-AND-INTEGRAL-GLUE-COMPATIBILITY-ON-NONELEMENTARY-SURVIVORS"
    ),
    "results": results,
}
raw = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "records_checked": cert["records_checked"],
    "status_counts": cert["status_counts"],
    "survivors": cert["survivor_count"],
    "all_non_elementary_index512_types_eliminated": cert["all_non_elementary_index512_types_eliminated"],
    "solver_seconds": cert["total_solver_seconds"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
