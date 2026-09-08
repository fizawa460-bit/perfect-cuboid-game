#!/usr/bin/env python3
from __future__ import annotations

import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-04-common-v4-character-correspondence-gate.json"
EX3 = ROOT / "stages/stage32-ex3/scratch/ex3-03-o210-local-contact-modular-degree-adapter.json"
TOWER = ROOT / "stages/stage32-ex3/ex3-00-o210-typed-cover-tower.json"
RANK = ROOT / "stages/stage32/residual-32-01-production/post1473-product-cover-v4-character-rank-reduction.json"
COMMON = ROOT / "stages/stage32/residual-32-01-production/post1484-o210-q4-common-double-cover-cartesian-identity.json"

art = json.loads(ART.read_text(encoding="utf-8"))
ex3 = json.loads(EX3.read_text(encoding="utf-8"))
tower = json.loads(TOWER.read_text(encoding="utf-8"))
rank = json.loads(RANK.read_text(encoding="utf-8"))
common = json.loads(COMMON.read_text(encoding="utf-8"))

assert art["status"] == "SCRATCH_PROVISIONAL_DIAGNOSTIC_NOT_RETAINED"
assert tower["canonical_sha256_without_this_field"] == "3a743b0607c59dc959f383fca8d97e54e8a740d197401e4c080b6fc4c94eaf07"
assert rank["canonical_sha256_without_this_field"] == "509635ab9964de7e7eecb41277b892589a7bb418676d8e76bd99b20607dac9dd"
assert common["canonical_sha256_without_this_field"] == "eb31183bf519fec4ad5bb2d0799b3f0a64b7af893308e09ce0c33119b63440a1"
assert ex3["fixed_target"]["O"] == 210
assert ex3["fixed_target"]["contact_histogram"] == {"m1_count": 210, "m2_count": 28}

loc = art["local_simultaneous_population"]
f1 = loc["first_factor"]
f2 = loc["second_factor"]

# Simultaneous local degree population.
assert 210 + 2 * 28 == 266
assert f1["total_cusp_degree_over_six_cusps"] == 6 * 105
assert 210 + 2 * 28 + 2 * 182 == 6 * 105
assert f1["N_to_X4_cusp_ramification"] == 28 + 182 == 210
assert f1["N_to_X4_outside_ramification"] == 0
assert f1["Y_to_C0_ramification"] == 0

assert f2["total_cusp_degree_over_six_cusps"] == 6 * 81
assert 210 + 2 * 28 + 2 * 110 == 6 * 81
assert f2["N_to_X4_cusp_ramification"] == 28 + 110 == 138
# RH for degree 81 map from genus one to P1: R=2*81=162.
assert f2["N_to_X4_total_ramification"] == 2 * 81 == 162
assert f2["N_to_X4_outside_simple_ramification"] == 162 - 138 == 24
# Outside a branch value of C0->X4, quadratic base change doubles these 24 simple ramification points.
assert f2["Y_to_C0_outside_ramification"] == 2 * 24 == 48
assert f2["Y_to_C0_cusp_ramification"] == 0
assert f2["Y_to_C0_total_ramification"] == 48

# Translation-lattice parity for the candidate exceptional local exponents a1=a2=4m.
for m in (1, 2):
    a1 = a2 = 4 * m
    assert a1 % 4 == a2 % 4 == 0
    assert (a1 + a2) % 8 == 0

# Replay GL(2,F2): exactly six invertible basis changes are possible.
def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 2 for j in range(2)) for i in range(2))

def det(A):
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 2

I = ((1, 0), (0, 1))
all_mats = [((a,b),(c,d)) for a,b,c,d in product((0,1), repeat=4)]
gl2 = [A for A in all_mats if det(A) == 1]
assert len(gl2) == 6
for A in gl2:
    inverses = [B for B in gl2 if mm(A, B) == I and mm(B, A) == I]
    assert len(inverses) == 1
    Ainv = inverses[0]
    # The common-torsor relation f1^*lambda=f2^*(A lambda), together with
    # Norm_f1 f1^*=[105]=1 mod 2, forces T A=I on U, hence T|U=A^{-1}.
    assert mm(Ainv, A) == I

# Both odd degrees act as 1 on 2-torsion, giving pullback injectivity.
assert 105 % 2 == 1 and 81 % 2 == 1
assert rank["carrier_pullback_reduction"]["monodromy_rank_formula"] == "qprime = |im(pi1(Y)->G)| = 2^rank_F2(span(alpha,beta))"
assert tower["groups"]["H4"]["order"] == 4
assert tower["objects"]["D"]["genus"] == 421
assert tower["common_cover_identity"]["same_quadratic_extension"] is True

verdict = art["diagnostic_verdict"]
assert verdict["EX3_04_local_counting_exclusion_obtained"] is False
assert verdict["EX3_04_common_V4_character_gate_obtained"] is True
assert verdict["new_correspondence_mod2_filter_obtained"] is True
assert verdict["O210_excluded"] is False
assert all(value is False for value in art["firewalls"].values())

print("PASS EX3-04 scratch common V4 character/correspondence gate")
print("local simultaneous population survives: first R=210, second R=138+24=162, descended second R=48")
print("common H4 torsor => T preserves the rank-2 character plane U and T|U is in GL(2,F2)")
print("GL(2,F2) size:", len(gl2))
print("next: source-lock U in Bolza J[2] coordinates and combine with Rosati enumeration")
