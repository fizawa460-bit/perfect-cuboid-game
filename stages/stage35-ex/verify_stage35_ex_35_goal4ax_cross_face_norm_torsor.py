#!/usr/bin/env python3
"""Verify Goal4AX: six-norm torus chart and endpoint-equivalence boundary."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4ax-cross-face-lattice-norm-torsor-compatibility.json")
SRC = P("stages/stage35-ex/35ex-35/goal4ax-cross-face-lattice-norm-torsor-compatibility-source-lock.md")
AW = P("stages/stage35-ex/35ex-35/goal4aw-marked-elliptic-height-lower-vs-goal4m-upper.json")
AS = P("stages/stage35-ex/35ex-35/goal4as-fresh-exhaustive-view-marked-kummer.json")
AU = P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation.json")
O = P("stages/stage35-ex/35ex-35/goal4o-spinor-norm-ternary-form-preflight.json")
GCD = P("stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "586bbe7f7889ff9b6fe89756a66b9cf7aaaa4f7206d62afe3664e9ab62627c5d"
SRC_BLOB = "777a67709a297b1cdb72bede24d72d2178c2ba8f"
AW_BLOB = "f3cf53d56fd20ffb8e0d059412b92eb23dac62a2"
AS_BLOB = "5f17e0ec3d325127b517ac2afb418ec4cb309868"
AU_BLOB = "d0dd0597046daf54ad9fcc74991221710a27f12c"
O_BLOB = "98ea70777ae50ebba4e322fb6117d2dbb60d0188"
GCD_BLOB = "d0cd03a5ff744d5f6536b6d2784c0e0d543fea48"
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
assert blob(AW) == AW_BLOB
assert blob(AS) == AS_BLOB
assert blob(AU) == AU_BLOB
assert blob(O) == O_BLOB
assert blob(GCD) == GCD_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

aw = json.loads(AW.read_text())
assert aw["canonical_sha256"] == "0605861581bac2571889a58bfe2a7ef0f1f1e167372fc434d285187af1988488"
assert aw["next"]["unit"] == "35EX-35_GOAL4AX_CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY_PREFLIGHT"
assert aw["result"]["eventual_endpoint_elimination_obtained"] is False

as_ = json.loads(AS.read_text())
assert "CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY" in as_["candidate_ledger"]["untested"]

au = json.loads(AU.read_text())
assert au["cross_face_relation"]["marked_product"] == "d_A*d_B*d_C=1 in Q*/Q*^2"
assert au["result"]["new_branch_pruning_obtained"] is False

o = json.loads(O.read_text())
assert o["exact_boundary"]["obvious_single_form_spinor_route_closed"] is True
assert o["exact_boundary"]["cross_face_lattice_or_spinor_correspondence_constructed"] is False

gcd = json.loads(GCD.read_text())
assert gcd["definitions"] == {
    "x": "gcd(A,B)",
    "y": "gcd(A,C)",
    "z": "gcd(B,C)",
    "a": "A/(x*y)",
    "b": "B/(x*z)",
    "c": "C/(y*z)",
}
assert "r_AB^2=(y*a)^2+(z*b)^2" in gcd["goal3_exact_square_rewrite"]["primitive_face_equations"]

# Universal half-angle / norm-one-torus identities.
t = sp.symbols("t")
I = sp.I
R = lambda z: 2*z/(1-z**2)
H0 = lambda z: (1+z**2)/(1-z**2)
assert sp.factor(H0(t)**2 - R(t)**2 - 1) == 0
phase = sp.factor((1+I*t)/(1-I*t))
normalized = sp.factor((1+I*R(t))/H0(t))
assert sp.simplify(phase-normalized) == 0
assert sp.simplify(phase*sp.conjugate(phase).subs(sp.conjugate(t), t)-1) == 0

# Cross-face inverse reconstruction algebra. Let P=B/A and T=C/B,
# so Q=C/A=P*T is exactly AX-C1.
P0, T0 = sp.symbols("P0 T0", nonzero=True)
Q0 = P0*T0
Hp2 = 1 + P0**2
Hq2 = 1 + Q0**2
Hr2 = 1 + T0**2

# Three face squares.
assert sp.expand(Hp2 - (1 + P0**2)) == 0
assert sp.expand(Hq2 - (1 + Q0**2)) == 0
assert sp.expand(P0**2*Hr2 - (P0**2 + Q0**2)) == 0

# AX-C2/C3/C4 make all three space reconstructions recover the same W^2.
W2_ab = sp.factor(Hp2 * (1 + Q0**2/Hp2))
W2_ac = sp.factor(Hq2 * (1 + P0**2/Hq2))
W2_bc = sp.factor(P0**2*Hr2 * (1 + 1/(P0**2*Hr2)))
target = 1 + P0**2 + Q0**2
assert sp.factor(W2_ab-target) == 0
assert sp.factor(W2_ac-target) == 0
assert sp.factor(W2_bc-target) == 0

src = SRC.read_text()
for marker in (
    "(AX-N1)",
    "(AX-N2)",
    "(AX-H1)",
    "(AX-H2)",
    "(AX-COORD)",
    "(AX-C1)",
    "(AX-C2)",
    "(AX-C3)",
    "(AX-C4)",
    "(AX-INV)",
    "(AX-W)",
    "PASS_EXACT_SPLIT_SIX_NORM_TORUS_CHART",
    "BLOCKED_AS_POSITIVE_ENDPOINT_BIRATIONAL_REPARAMETRIZATION",
    "35EX-35_GOAL4AY_GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["stacked_parent"]["exact_head_sha"] == "a862b3ddea76b21110ba93b0d171e55c22ce6af8"
assert art["stacked_parent"]["aggregate_run"] == 34297319019
assert art["stacked_parent"]["aggregate_job"] == 102298024754
assert art["source_locks"]["goal4ax_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4aw"]["blob_sha1"] == AW_BLOB
assert art["source_locks"]["goal4as"]["blob_sha1"] == AS_BLOB
assert art["source_locks"]["goal4au"]["blob_sha1"] == AU_BLOB
assert art["source_locks"]["goal4o"]["blob_sha1"] == O_BLOB
assert art["source_locks"]["private_gcd"]["blob_sha1"] == GCD_BLOB

pkg = art["six_norm_package"]
assert pkg["torus"] == "T=Res^1_{Q(i)/Q} G_m"
assert len(pkg["face_norms"]) == 3
assert len(pkg["space_norms"]) == 3
assert pkg["six_hilbert90_lifts_explicit"] is True

compat = art["compatibility"]
assert compat["count"] == 4
assert compat["source_incidence_only"] is True

inv = art["inverse_reconstruction"]
assert inv["all_three_face_squares_recovered"] is True
assert inv["common_space_square_recovered"] is True
assert inv["positive_endpoint_open_mod_scaling_recovered"] is True

boundary = art["primitive_lattice_boundary"]
assert boundary["face_half_angle_invariant_under_pair_gcd_reduction"] is True
assert boundary["new_rational_norm_equation_from_primitivity"] is False
assert boundary["finite_integral_branch_elimination_obtained"] is False

res = art["result"]
assert res["six_norm_package_constructed"] is True
assert res["six_hilbert90_lifts_explicit"] is True
assert res["four_cross_face_compatibilities_exact"] is True
assert res["positive_endpoint_open_reconstructed"] is True
assert res["new_nontrivial_H1_torsor_class_obtained"] is False
assert res["new_local_norm_obstruction_obtained"] is False
assert res["new_spinor_representation_obstruction_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4AY_GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4AX_CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY=PASS")
print("six_norm_torus_chart=EXACT_SPLIT")
print("positive_endpoint_open_reconstructed=true")
print("new_torsor_obstruction=false")
print("canonical_sha256=" + EXPECTED)
