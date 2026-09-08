#!/usr/bin/env python3
"""Verify Goal4AS: fresh breadth audit and physical marked Kummer slice."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4as-fresh-exhaustive-view-marked-kummer.json")
SRC = P("stages/stage35-ex/35ex-35/goal4as-fresh-exhaustive-view-marked-kummer-source-lock.md")
AR = P("stages/stage35-ex/35ex-35/goal4ar-full-brauer-bm-endpoint-equivalence.json")
K = P("stages/stage35-ex/35ex-35/goal4k-ratio-discriminant-biquartic-quotient-preflight.json")
L = P("stages/stage35-ex/35ex-35/goal4l-stage14-pythagorean-elliptic-rankjump-receiver.json")
I = P("stages/stage35-ex/35ex-35/goal4i-v2-infinite-descent-self-map-preflight.json")
J = P("stages/stage35-ex/35ex-35/goal4j-linked-congruent-number-selmer-coupling-preflight.json")
M = P("stages/stage35-ex/35ex-35/goal4m-stage14-global-triple-population-height-transfer.json")
N = P("stages/stage35-ex/35ex-35/goal4n-post-sqrt-exact-zero-finite-height-preflight.json")
O = P("stages/stage35-ex/35ex-35/goal4o-spinor-norm-ternary-form-preflight.json")
POLICY = P("docs/research-os/policies/cycle-exploration-safety-protocol.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "a17b7100e82c2fa81e4ca150384c7ebe3e076ed10ee3b28e9d26304afc987f29"
SRC_BLOB = "d9e249b42fd2c0f446c3513b9f085d5f6d97d581"
AR_CANON = "203bc01c9e3824bdb556ab08e43b015de7923b6cfa0cd4bd2acfe804a827cceb"
K_BLOB = "7943d5f1f76354fbca6e89d42a0fc90b10e976c7"
L_BLOB = "0717ca307162d5559a005801848288daa91285fd"
I_BLOB = "d9121d2fdb9b202bc0ffc72678e74e9ccb5a87c2"
J_BLOB = "f74b4bfb3128ada4312255371e35d3473744cb13"
M_BLOB = "1c7a3e9e23dd8bbc41fc331b8c43e4023f5d3909"
N_BLOB = "53d7497debe46b421364c3c6c93b66e20fb3123f"
O_BLOB = "98ea70777ae50ebba4e322fb6117d2dbb60d0188"
POLICY_BLOB = "4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)

assert blob(SRC) == SRC_BLOB
assert blob(K) == K_BLOB
assert blob(L) == L_BLOB
assert blob(I) == I_BLOB
assert blob(J) == J_BLOB
assert blob(M) == M_BLOB
assert blob(N) == N_BLOB
assert blob(O) == O_BLOB
assert blob(POLICY) == POLICY_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["brauer_manin_obstruction_obtained"] is False
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

ar = json.loads(AR.read_text())
assert ar["canonical_sha256"] == AR_CANON
assert ar["result"]["full_Brauer_route"] == "ENDPOINT_EQUIVALENT_BLOCKER"
assert ar["result"]["finite_additional_Brauer_shortcut_ruled_out"] is False
assert ar["cycle"]["exhaustive_view_audit_required"] is True
assert ar["cycle"]["blind_rediscovery_required"] is True

k = json.loads(K.read_text())
assert k["denominator_cleared_face_squares"]["F_plus"] == "A_V*(U^2+1)+2*B_V*U"
assert k["denominator_cleared_face_squares"]["F_minus"] == "A_V*(U^2+1)-2*B_V*U"
l = json.loads(L.read_text())
assert l["birational_adapter"]["elliptic_curve"] == "E_q: Y^2=X*(X-1)*(X+q^2)"
assert l["torsion_exclusion_on_physical_endpoint"]["conclusion"] == "every physical endpoint maps to a non-torsion E_q(Q) point"

i = json.loads(I.read_text())
assert i["descent_gate"]["common_scalar_two_descent"]["available"] is False
assert i["result"]["genuine_nonlinear_v2_infinite_descent_constructed"] is False
j = json.loads(J.read_text())
assert j["selmer_coupling_verdict"]["cross_twist_selmer_pruning_obtained"] is False
m = json.loads(M.read_text())
assert m["derived_triple_population_corollary"]["conclusion"] == "T(B)<<B^{1/2+o(1)}"
n = json.loads(N.read_text())
assert n["exact_current_asset_verdict"]["effective_global_height_bound_obtained"] is False
assert n["exact_current_asset_verdict"]["full_endpoint_strict_descent_self_map_obtained"] is False
o = json.loads(O.read_text())
assert o["exact_boundary"]["obvious_single_form_spinor_route_closed"] is True
assert o["exact_boundary"]["cross_face_spinor_method_proved_impossible"] is False

# Exact symbolic replay of the new blind-derived Kummer identity.
u, v, z = sp.symbols("u v z", nonzero=True)
U = u**2
V = v**2
A = (1 + V)**2
B = V**2 - 6*V + 1
Fp = A*(U**2 + 1) + 2*B*U
Fm = A*(U**2 + 1) - 2*B*U
p = (v**2 - 1)/(2*v)
q = (p**2 - 1)/(2*p)
h = (p**2 + 1)/(2*p)
c = (p**2 - 1)/(2*p**2)
X = c*(z-p)/(z+1/p)

assert sp.factor(sp.together(q**2 + 1 - h**2)) == 0
assert sp.factor(sp.together(X + q**2 - q*h*(p*z-1)/(p*z+1))) == 0

Kroot = (
    (u**2 + 1)*(v**2 + 1)**2*(v**2 - 2*v - 1)*(v**2 + 2*v - 1)
    /(8*v**2*(v**2 - 1))
)
assert sp.factor(sp.together(q*h*(p**2*Fp - Fm) - Kroot**2)) == 0

x = sp.symbols("x")
a = -(2*q**2 + 1)
b = q**2*(q**2 + 1)
assert sp.factor(sp.together(a**2 - 4*b - 1)) == 0
e1_left = x**3 + (4*q**2 + 2)*x**2 + x
e1_fact = x*(x + (h-q)**2)*(x + (h+q)**2)
assert sp.factor(sp.together(e1_left - e1_fact)) == 0

src = SRC.read_text()
for marker in (
    "BLIND_REDISCOVERY pass",
    "(AS-3)",
    "delta(P) = ([X],[X-1],[X+q^2]) = (d,d,1)",
    "UNMARKED_XPLUSQ2_SQUARE_EXISTENCE_AS_A_CLOSURE_RECEIVER",
    "PHYSICAL_MARKED_POINT_RESIDUAL_KUMMER_CLASS_D_LOCAL_SUPPORT",
    "CYCLE_ROUTE_STATUS=PASS_NEW_GATE_FROM_STRONGER_VIEW",
    "CYCLE_EXHAUSTIVE_VIEW_AUDIT=true",
    "CYCLE_BLIND_REDISCOVERY=true",
    "CYCLE_SPLIT_TRIGGERED=false",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4as_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4ar"]["canonical_sha256"] == AR_CANON
assert art["source_locks"]["goal4ar"]["exact_head_sha"] == "17be899d6d236f899492fda650fd506ab5a96cf0"
assert art["source_locks"]["goal4ar"]["aggregate_run"] == 34282922559
assert art["source_locks"]["goal4ar"]["aggregate_job"] == 102253438874

blind = art["blind_pass"]
assert blind["executed"] is True
assert blind["arsenal_route_recommendations_consulted_during_generation"] is False
assert len(blind["generated_lenses"]) == 7

kd = art["marked_kummer_derivation"]
assert kd["literal_square_identity_exact"] is True
assert kd["X_plus_q2_squareclass_trivial"] is True
assert kd["two_torsion_excluded_by_goal4l"] is True
assert kd["residual_squareclass_exists"] is True
assert kd["kummer_shape"] == "delta(P)=([X],[X-1],[X+q^2])=(d,d,1)"
assert kd["full_selmer_dimension_one_claimed"] is False

iso = art["isogeny_boundary"]
assert iso["a2_minus_4b"] == 1
assert iso["selected_new_information"] == "SPECIFIC_PHYSICAL_MARKED_POINT_RESIDUAL_CLASS_d"

ledger = art["candidate_ledger"]
assert ledger["live"] == ["PHYSICAL_MARKED_POINT_RESIDUAL_KUMMER_CLASS_D_LOCAL_SUPPORT"]
assert ledger["live_count"] == 1
assert ledger["untested_count"] == 6
assert ledger["split_triggered"] is False

cy = art["cycle_exit"]
assert cy["CYCLE_ROUTE_STATUS"] == "PASS_NEW_GATE_FROM_STRONGER_VIEW"
assert cy["CYCLE_ACTIVE_RECEIVER"] == "PHYSICAL_GOAL4L_MARKED_POINT_WITH_KUMMER_CLASS_(d,d,1)"
assert cy["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert cy["CYCLE_BLIND_REDISCOVERY"] is True
assert cy["CYCLE_SPLIT_TRIGGERED"] is False
assert cy["CYCLE_NEW_VIEW_SOURCE"] == "BLIND"

assert art["next"]["unit"] == "35EX-35_GOAL4AT_MARKED_RESIDUAL_KUMMER_SQUARECLASS_LOCAL_SUPPORT_PREFLIGHT"

fw = art["credit_firewall"]
for key in (
    "d_trivial_proved",
    "finite_squareclass_family_proved",
    "two_selmer_group_computed",
    "two_divisibility_proved",
    "infinite_descent_proved",
    "canonical_height_contradiction_obtained",
    "finite_brauer_shortcut_obtained",
    "brauer_manin_obstruction_obtained",
    "E1_proved",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert fw[key] is False, key

print("STAGE35_EX_GOAL4AS_FRESH_EXHAUSTIVE_VIEW_MARKED_KUMMER=PASS")
print("kummer_shape=(d,d,1)")
print("live_candidate=PHYSICAL_MARKED_POINT_RESIDUAL_KUMMER_CLASS_D_LOCAL_SUPPORT")
print("split_triggered=false")
print("canonical_sha256=" + EXPECTED)
