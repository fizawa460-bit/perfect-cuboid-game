#!/usr/bin/env python3
"""Verify Goal4AZ: exact super-sqrt amplification exponent gate and current mechanism fail-close."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4az-super-sqrt-distinct-class-amplification.json")
SRC = P("stages/stage35-ex/35ex-35/goal4az-super-sqrt-distinct-class-amplification-source-lock.md")
AY = P("stages/stage35-ex/35ex-35/goal4ay-derived-cuboid-involution-nonlinear-descent.json")
M = P("stages/stage35-ex/35ex-35/goal4m-stage14-global-triple-population-height-transfer.json")
N = P("stages/stage35-ex/35ex-35/goal4n-post-sqrt-exact-zero-finite-height-preflight.json")
L = P("stages/stage35-ex/35ex-35/goal4l-stage14-pythagorean-elliptic-rankjump-receiver.json")
AS = P("stages/stage35-ex/35ex-35/goal4as-fresh-exhaustive-view-marked-kummer.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "c37bcff25ac61d67d14f429d76559383ea483cb3c0c596502f399781d233f17e"
SRC_BLOB = "793e37effd8f34c751a1e57137703c7c7fd600be"
AY_BLOB = "2cb4e8fc58690b4a820c02c5e0e52ec0a299333c"
M_BLOB = "1c7a3e9e23dd8bbc41fc331b8c43e4023f5d3909"
N_BLOB = "53d7497debe46b421364c3c6c93b66e20fb3123f"
L_BLOB = "0717ca307162d5559a005801848288daa91285fd"
AS_BLOB = "5f17e0ec3d325127b517ac2afb418ec4cb309868"
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
assert blob(AY) == AY_BLOB
assert blob(M) == M_BLOB
assert blob(N) == N_BLOB
assert blob(L) == L_BLOB
assert blob(AS) == AS_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

ay = json.loads(AY.read_text())
assert ay["canonical_sha256"] == "513e4085d1f5309a52580c3f716db0de6e549a07619351e4098e3b159766c41d"
assert ay["derived_operator"]["involution"] is True
assert ay["result"]["classical_operator_universal_strict_descent_ruled_out"] is True
assert ay["result"]["all_possible_nonlinear_descent_maps_proved_impossible"] is False
assert ay["next"]["unit"] == "35EX-35_GOAL4AZ_SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION_PREFLIGHT"

m = json.loads(M.read_text())
assert m["derived_triple_population_corollary"]["conclusion"] == "T(B)<<B^{1/2+o(1)}"
assert m["derived_triple_population_corollary"]["strict_subsqrt_power_saving_obtained"] is False

n = json.loads(N.read_text())
amp = [x for x in n["logical_gate"]["sufficient_conversion_mechanisms_checked"] if x["id"] == "SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION"]
assert len(amp) == 1
assert amp[0]["current_asset_available"] is False
assert "positive scaling" in amp[0]["equivalences_not_counted_as_amplification"]

l = json.loads(L.read_text())
assert l["torsion_exclusion_on_physical_endpoint"]["conclusion"] == "every physical endpoint maps to a non-torsion E_q(Q) point"
assert l["credit_boundary"]["Goal4K_receiver_endpoint_equivalence_claimed"] is False

asj = json.loads(AS.read_text())
assert "SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION_OR_STRONGER_COUNTING" in asj["candidate_ledger"]["untested"]

# Exact exponent bookkeeping: if 2*rho>kappa, choose epsilon halfway inside the gap.
rho, kappa = sp.symbols("rho kappa", positive=True)
epsilon = rho/(2*kappa) - sp.Rational(1, 4)
margin = sp.factor(rho - kappa*(sp.Rational(1, 2) + epsilon))
assert sp.expand(margin - (2*rho-kappa)/4) == 0
# Equality rho/kappa=1/2 gives zero margin, hence no strict power contradiction.
assert sp.simplify(margin.subs(rho, kappa/2)) == 0
# Linear orbit rho=1 requires kappa<2.
assert sp.simplify((2*rho-kappa).subs(rho, 1)) == 2-kappa

# Raw derived operator squares to positive scaling by A*B*C.
A, B, C = sp.symbols("A B C", nonzero=True)
def D(t):
    a, b, c = t
    return (a*b, a*c, b*c)
d2 = D(D((A, B, C)))
expected = (A*B*C*A, A*B*C*B, A*B*C*C)
for got, want in zip(d2, expected):
    assert sp.expand(got-want) == 0

src = SRC.read_text()
for marker in (
    "(AZ-1)",
    "(AZ-2)",
    "(AZ-3)",
    "(AZ-4)",
    "rho/kappa > 1/2",
    "#Orbit_D(P) <= 2",
    "Goal4K_receiver_endpoint_equivalence_claimed=false",
    "FAIL_CLOSE_CURRENT_SOURCE_LOCKED_AMPLIFICATION_MECHANISMS",
    "35EX-35_GOAL4BA_FINITE_ADDITIONAL_BRAUER_SHORTCUT_EXHAUSTION_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4az_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4ay"]["blob_sha1"] == AY_BLOB
assert art["source_locks"]["goal4m"]["blob_sha1"] == M_BLOB
assert art["source_locks"]["goal4n"]["blob_sha1"] == N_BLOB
assert art["source_locks"]["goal4l"]["blob_sha1"] == L_BLOB
assert art["source_locks"]["goal4as"]["blob_sha1"] == AS_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "d544357536ed92d7ab56c48d303e45f1073f6c5e"
assert parent["aggregate_run"] == 34300718726
assert parent["aggregate_job"] == 102307753849
assert parent["hostile_audited"] is False

gate = art["amplifier_gate"]
assert gate["contradiction_condition"] == "rho/kappa>1/2"
assert gate["equality_case_sufficient"] is False
assert gate["linear_orbit_requirement"] == "rho=1 requires kappa<2"

mech = art["mechanism_audit"]
assert mech["derived_cuboid"]["primitive_orbit_upper_bound"] == 2
assert mech["derived_cuboid"]["amplifier"] is False
assert mech["elliptic_multiplication"]["infinitely_many_receiver_points"] is True
assert mech["elliptic_multiplication"]["full_endpoint_reconstruction_for_arbitrary_multiple"] is False
assert mech["elliptic_multiplication"]["primitive_space_diagonal_polynomial_height_transfer"] is False
assert mech["euler_brick_quadratic_jumps"]["full_endpoint_fourth_square_preservation"] is False

res = art["result"]
assert res["super_sqrt_exponent_gate_derived"] is True
assert res["derived_operator_orbit_at_most_two"] is True
assert res["current_source_locked_endpoint_amplifier_found"] is False
assert res["all_possible_amplifiers_proved_impossible"] is False
assert res["super_sqrt_distinct_class_amplification_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BA_FINITE_ADDITIONAL_BRAUER_SHORTCUT_EXHAUSTION_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4AZ_SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION=PASS")
print("required_exponent_ratio=rho/kappa>1/2")
print("derived_orbit_upper_bound=2")
print("current_endpoint_amplifier=false")
print("canonical_sha256=" + EXPECTED)
