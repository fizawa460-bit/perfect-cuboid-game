#!/usr/bin/env python3
"""Verify Goal4AP: the Q-defined unit lattice forces an infinite algebraic Brauer layer."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4ap-algebraic-brauer-unit-character-infinite-layer.json")
SRC = P("stages/stage35-ex/35ex-35/goal4ap-algebraic-brauer-unit-character-infinite-layer-source-lock.md")
G4Y_SRC = P("stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift-source-lock.md")
G4Y_ART = P("stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json")
G4AO = P("stages/stage35-ex/35ex-35/goal4ao-source-marked-two-class-bm-nonempty.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "b291b617552e7280cbf0c1eb3f54eb4f69e86888cb21d2d52ba891ad4030779a"
SRC_BLOB = "6b6c20f9aebce3210f70cf8fd19d9dfd0120077a"
G4Y_SRC_BLOB = "2c5cc829b508a917f071a624f6a3bb9419864a77"
G4Y_ART_BLOB = "9351c92747365838cda92d98854ad136df1847d5"
G4AO_CANON = "e86b7318aa7593b99ab83bed49dbcd2bdbac05e0c828088e7c9917efd97ff858"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def canon(obj: dict) -> str:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)
    return got

assert blob(SRC) == SRC_BLOB
assert blob(G4Y_SRC) == G4Y_SRC_BLOB
assert blob(G4Y_ART) == G4Y_ART_BLOB

src = SRC.read_text()
for marker in (
    "Br_a(U) ~= H^2(Q,UPic(Ubar))",
    "H^1(N,Pic(Ubar)) = Hom_cts(N,Z^35) = 0",
    "H^1(Q,Pic(Ubar)) ~= H^1(G,Pic(Ubar)) ~= Z/2 x Z/2",
    "H^2(Q,K) ~= Hom_cts(G_Q,Q/Z)^3",
    "coker(d2^(0,1)) is infinite",
    "Br_a(U) is infinite",
):
    assert marker in src, marker

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["brauer_manin_obstruction_obtained"] is False
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

y = json.loads(G4Y_ART.read_text())
up = y["extended_picard_complex"]
assert up["unit_kernel_rank"] == 3
assert up["unit_kernel_galois_action_trivial"] is True
assert up["visible_Q_defined_units"] == ["p+x", "q+y", "w+z"]
assert up["pic_Ubar_rank"] == 35
assert y["goal4x_H1_source"]["structure"] == "Z/2 x Z/2"
assert y["two_step_lift"]["both_goal4x_generators_survive_to_H2_UPic"] is True
assert y["two_step_lift"]["full_algebraic_brauer_group_dimension_claimed"] is False
assert y["extended_picard_complex"]["full_Br_a_U_computed"] is False

ao = json.loads(G4AO.read_text())
assert ao["canonical_sha256"] == G4AO_CANON
assert ao["route_result"]["source_marked_local_relaxation_known_two_class_BM_set_nonempty"] is True

art = json.loads(ART.read_text())
canon(art)
assert art["source_locks"]["goal4ap_source"]["blob_sha1"] == SRC_BLOB
u = art["upic_inputs"]
assert u["K_galois_action"] == "trivial"
assert u["picard_action_factors_through"] == "Gal(Q(i,sqrt(2))/Q) ~= C2 x C2"
assert u["absolute_H1_inflation_iso_from_V4"] is True
assert u["H1_Q_Pic_Ubar"] == "Z/2 x Z/2"
f = art["hypercohomology_filtration"]
assert f["only_q_rows"] == [0, 1]
assert f["right_piece"] == "Z/2 x Z/2"
assert f["right_piece_realized_by_goal4y_lifts"] is True
uc = art["unit_character_layer"]
assert uc["K_is_trivial_Z3"] is True
assert uc["character_group_infinite"] is True
assert uc["d2_01_image_finitely_generated_torsion_hence_finite"] is True
assert uc["left_piece_infinite"] is True
assert uc["left_piece_has_infinite_2_primary_part"] is True
r = art["result"]
assert r["Br_a_U_infinite"] is True
assert r["known_A_B_span_exhausts_Br_a_U"] is False
assert r["finite_algebraic_brauer_basis_strategy_valid"] is False
assert r["unit_character_local_evaluation_pairing_computed"] is False
assert all(v is False for v in art["credit_firewall"].values())

print("STAGE35_EX_GOAL4AP_ALGEBRAIC_BRAUER_UNIT_LAYER=PASS")
print("Br_a_U_infinite=true")
print("known_A_B_span_exhausts_Br_a_U=false")
print("next=" + r["next"])
print("canonical_sha256=" + EXPECTED)
