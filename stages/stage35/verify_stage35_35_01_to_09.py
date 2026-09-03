#!/usr/bin/env python3
"""Lightweight aggregate verifier for promoted Stage35 35-01..35-09 state.

This deliberately performs no bounded fiber search and no heavy computation.
It checks source locks/state contracts and independently replays the exact
algebraic adapters that are load-bearing for the current Class-3 sharpening.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]


def load(rel: str):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)


def run(rel: str):
    subprocess.run([sys.executable, str(ROOT / rel)], cwd=ROOT, check=True)


# 35-01: exact Stage29 source-lock verifier.
run("stages/stage35/35-01/verify_35_01.py")

# 35-02: selected Q-defined direct fibration and coverage adapter.
j02 = load("stages/stage35/35-02/q-field-physical-fibration-ledger.json")
fib = j02["selected_primary_attack_fibration"]
assert fib["id"] == "TS-S-R3-Q1"
assert fib["base_field"] == "Q" and fib["Q_defined"] is True
assert fib["physical_affine_parameter"] == "t=(e+d)/z"
assert fib["global_physical_endpoint_coverage"] is True
assert j02["retained_field_firewall"]["all_28_Q_defined_certified"] is False
assert j02["retained_field_firewall"]["all_15_Q_defined_certified"] is False

# 35-03: exact inverse/forward reconstruction algebra.
t, d = sp.symbols("t d", nonzero=True)
r = (t**2 - 1) / (t**2 + 1)
s = 2*t / (t**2 + 1)
e = r*d
z = s*d
assert sp.factor(e**2 + z**2 - d**2) == 0
assert sp.factor((e + d) / z - t) == 0
assert sp.factor((t**2 + 1)*e - (t**2 - 1)*d) == 0
assert sp.factor((t**2 + 1)*z - 2*t*d) == 0
j03 = load("stages/stage35/35-03/direct-endpoint-reconstruction.json")
assert j03["residual_lift_contract"]["additional_squareclass_condition_required"] is False
assert j03["residual_lift_contract"]["exact_endpoint_reconstruction_complete"] is True

# 35-04: receiver-matched target is locked but explicitly unproved.
j04 = load("stages/stage35/35-04/minimal-uniform-theorem.json")
assert j04["replacement_theorem"]["id"] == "T35-R3-PHYS-EMPTY"
assert j04["replacement_theorem"]["parameter_base"] == "Q_{>1}"
assert j04["exact_receiver_match"]["every_physical_endpoint_maps_to_some_t_in_Q_gt_1"] is True
assert j04["credit_boundary"]["replacement_theorem_proved"] is False

# 35-05: independently replay rank-drop criterion and bad divisor pullback.
a, b = sp.symbols("a b")
M = sp.Matrix([
    [a, 1, 0, -1, 0],
    [a, 0, 1, 0, -1],
    [-b, 1, 1, 0, 0],
])
minors = []
for cols in __import__("itertools").combinations(range(5), 3):
    minors.append(sp.factor(M[:, cols].det().subs(b, 1-a)))
# Every nonzero minor is generated, up to sign, by 1, a, a-1, a+1.
allowed = {sp.Integer(1), a, a-1, a+1}
for m in minors:
    if m == 0:
        continue
    normalized = sp.factor(m)
    if normalized.could_extract_minus_sign():
        normalized = -normalized
    assert normalized in allowed, (m, normalized)

T, U = sp.symbols("T U")
num = T**2 - U**2
den = T**2 + U**2
assert sp.factor((num**2 - den**2) - (-4*T**2*U**2)) == 0  # alpha=1
assert sp.factor((num**2 + den**2) - 2*(T**4 + U**4)) == 0  # alpha=-1
bad_divisor = sp.factor(T*U*(T**2-U**2)*(T**2+U**2)*(T**4+U**4))
j05 = load("stages/stage35/35-05/bad-fiber-and-exceptional-locus.json")
assert j05["bad_parameter_pullback"]["squarefree_bad_parameter_divisor"] == "T*U*(T^2-U^2)*(T^2+U^2)*(T^4+U^4)=0"
assert j05["bad_parameter_pullback"]["geometric_bad_parameter_count"] == 10
assert j05["physical_rational_intersection"]["bad_divisor_intersect_Q_gt_1"] == "empty"
assert j05["physical_rational_intersection"]["all_physical_parameter_fibers_smooth"] is True
assert bad_divisor != 0

# 35-06: the literature-negative statement is bounded, not an absence oracle.
j06 = load("stages/stage35/35-06/uniform-attack-branch-ledger.json")
scan = j06["targeted_literature_check"]
assert scan["applicable_uniform_closure_theorem_found_in_source_locked_material"] is False
assert scan["global_literature_absence_claim"] is False
assert j06["outcome"]["uniform_theorem_proved"] is False

# 35-07: no finite reduction, therefore S34-W02 remains locked.
j07 = load("stages/stage35/35-07/finite-reduction-assessment.json")
assert j07["outcome"]["globally_exhaustive_finite_fiber_reduction_proved"] is False
assert j07["outcome"]["S34_W02_unlocked"] is False
assert j07["outcome"]["reduced_to_class2"] is False

# 35-08: exact quotient formulas, cubic RHS discriminants, boundary sections.
run("stages/stage35/35-08/verify_35_08.py")
j08 = load("stages/stage35/35-08/elliptic-quotient-structure.json")
assert "cubic_rhs_discriminants" in j08
assert "elliptic_discriminants" not in j08
assert j08["cubic_rhs_discriminants"]["weierstrass_discriminant_relation"] == "Delta=16*disc_X(f) for these displayed models"
assert j08["proof_experiment_findings"]["specialization_surjectivity_proved"] is False

# 35-09 / MAIN: retained Class3 only; no receiver/endpoint promotion.
j09 = load("stages/stage35/35-09/decision-certificate.json")
assert j09["classification"] == "CLASS3_RETAINED_WITH_SHARPER_MINIMAL_THEOREM"
assert j09["negative_results"]["global_literature_absence_claim"] is False
assert j09["anti_loop"]["broad_external_literature_search_is_not_declared_exhausted"] is True
for key in ["uniform_arithmetic_theorem_proved", "receiver_matched_replacement_theorem_proved", "globally_exhaustive_finite_fiber_reduction_proved", "R29_FIB2_closed", "J12_PARAMETRIC_closed", "stage35_closed", "new_theorem_credit"]:
    assert j09["promotion"][key] is False, key

state = load("stages/stage35/MAIN-STATE.json")
assert state["decision"]["classification"] == "CLASS3_RETAINED_WITH_SHARPER_MINIMAL_THEOREM"
assert state["promotion_gates"]["R29_FIB2_closed"] is False
assert state["promotion_gates"]["stage35_closed"] is False
assert state["claims"]["perfect_cuboid_nonexistence_claim"] is False

print("PASS STAGE35_35_01_TO_09_AGGREGATE_LIGHTWEIGHT_V1")
