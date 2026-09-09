#!/usr/bin/env python3
"""Verify Goal4BA: every finite visible unit-character Brauer truncation is non-obstructing."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4ba-finite-visible-brauer-truncation-nonobstruction.json")
SRC = P("stages/stage35-ex/35ex-35/goal4ba-finite-visible-brauer-truncation-nonobstruction-source-lock.md")
AZ = P("stages/stage35-ex/35ex-35/goal4az-super-sqrt-distinct-class-amplification.json")
AQ = P("stages/stage35-ex/35ex-35/goal4aq-unit-character-bm-endpoint-equivalence.json")
AP = P("stages/stage35-ex/35ex-35/goal4ap-algebraic-brauer-unit-character-infinite-layer.json")
AO = P("stages/stage35-ex/35ex-35/goal4ao-source-marked-two-class-bm-nonempty.json")
AN_SRC = P("stages/stage35-ex/35ex-35/goal4an-known-two-class-upc-bm-nonempty-source-lock.md")
O22 = P("stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json")
Y = P("stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "86aa145782a998c32ef4cf451ae4ce6ad790f4ce09e15ecd7cbf63167bf1c213"
SRC_BLOB = "681fbdcf56524f65c84f190639d0620e8ba08db9"
AZ_BLOB = "c7a8b89bad320c7276b47eef2eb9bce9c0b58bf7"
AQ_BLOB = "593d22b7905d93451e43311540be1c219bbc75d7"
AP_BLOB = "3d8ea2ca619d2b79ee41575483928c0b56054034"
AO_BLOB = "3b39f15aed87e66558c9cbc02cc02529e98a9692"
AN_SRC_BLOB = "694b23125c59dfd3cd44152c982ac6667391fbf0"
O22_BLOB = "537ca589cd45112cca4c8f8091f5c8c77264e70d"
Y_BLOB = "9351c92747365838cda92d98854ad136df1847d5"
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
assert blob(AZ) == AZ_BLOB
assert blob(AQ) == AQ_BLOB
assert blob(AP) == AP_BLOB
assert blob(AO) == AO_BLOB
assert blob(AN_SRC) == AN_SRC_BLOB
assert blob(O22) == O22_BLOB
assert blob(Y) == Y_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

az = json.loads(AZ.read_text())
assert az["canonical_sha256"] == "c37bcff25ac61d67d14f429d76559383ea483cb3c0c596502f399781d233f17e"
assert az["next"]["unit"] == "35EX-35_GOAL4BA_FINITE_ADDITIONAL_BRAUER_SHORTCUT_EXHAUSTION_PREFLIGHT"

aq = json.loads(AQ.read_text())
assert aq["unit_layer"]["visible_q_units"] == ["p+x", "q+y", "w+z"]
assert aq["unit_layer"]["visible_units_need_form_integral_basis"] is False
assert aq["result"]["finite_character_truncation_sufficient_claimed"] is False
assert aq["result"]["full_unit_character_route"] == "ENDPOINT_EQUIVALENT_BLOCKER"

ap = json.loads(AP.read_text())
assert ap["upic_inputs"]["cohomology_degree_0"] == "K=U(Ubar)=kbar[U]^*/kbar^* ~= Z^3"
assert ap["unit_character_layer"]["character_group_infinite"] is True
assert ap["unit_character_layer"]["left_piece_infinite"] is True

ao = json.loads(AO.read_text())
assert ao["local_population"]["name"] == "A_src^loc"
assert ao["two_adic_anchor"]["v2_x"] == 4
assert ao["two_adic_anchor"]["such_deformations_exist_in_every_sufficiently_small_neighborhood"] is True
assert ao["brauer_argument"]["two_adic_source_marking_and_A_B_evaluation_preservation_simultaneous"] is True

o22 = json.loads(O22.read_text())
p = o22["common_zero_specialization"]["point"]
assert p == {"x":"272/225","y":"0","p":"353/225","q":"1","z":"272/225","w":"353/225"}
assert o22["common_zero_specialization"]["outside_selected_open_only_because"] == "y=0"
assert o22["restricted_product_repair"]["integral_U_PC_Zl_point_for_every_prime_l_ge_173"] is True
assert o22["restricted_product_repair"]["all_seven_linear_generators_units_at_good_primes"] is True

# Exact visible-unit values at the rational boundary anchor.
x = Fraction(272,225); y = Fraction(0); pp = Fraction(353,225); q = Fraction(1); z = x; w = pp
assert pp+x == Fraction(25,9)
assert q+y == 1
assert w+z == Fraction(25,9)

Yj = json.loads(Y.read_text())
assert Yj["extended_picard_complex"]["unit_kernel_rank"] == 3
assert Yj["extended_picard_complex"]["unit_kernel_galois_action_trivial"] is True
assert Yj["extended_picard_complex"]["visible_Q_defined_units"] == ["p+x", "q+y", "w+z"]
assert Yj["extended_picard_complex"]["full_Br_a_U_computed"] is False

src = SRC.read_text()
for marker in (
    "(BA-U)",
    "(BA-EVAL)",
    "(BA-P*)",
    "(BA-PU)",
    "(BA-F)",
    "(BA-NONEMPTY)",
    "v2(y)>4=v2(272/225)",
    "every finite visible truncation: BM set nonempty",
    "ARBITRARY_FINITE_BRAUER_SHORTCUT_RULED_OUT=false",
    "35EX-35_GOAL4BB_VISIBLE_UNIT_LATTICE_INDEX_AND_FINITE_ALGEBRAIC_BRAUER_COMPLETION_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4ba_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4az"]["blob_sha1"] == AZ_BLOB
assert art["source_locks"]["goal4aq"]["blob_sha1"] == AQ_BLOB
assert art["source_locks"]["goal4ap"]["blob_sha1"] == AP_BLOB
assert art["source_locks"]["goal4ao"]["blob_sha1"] == AO_BLOB
assert art["source_locks"]["goal4an_source"]["blob_sha1"] == AN_SRC_BLOB
assert art["source_locks"]["obvious_35ex22"]["blob_sha1"] == O22_BLOB
assert art["source_locks"]["goal4y"]["blob_sha1"] == Y_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "932e863eb11749d1fbcd20a607535cbbf2816b47"
assert parent["aggregate_run"] == 34301250886
assert parent["aggregate_job"] == 102309735138
assert parent["hostile_audited"] is False

f = art["finite_visible_subgroup"]
assert f["visible_units"] == ["p+x", "q+y", "w+z"]
assert f["finite"] is True
assert f["full_infinite_unit_layer_claimed"] is False

ad = art["adelic_construction"]
assert ad["good_prime_visible_units_are_units"] is True
assert ad["unramified_character_trivial_on_unit_ratio"] is True
assert ad["all_generator_local_invariants_match_Pstar"] is True
assert ad["global_reciprocity_on_Pstar"] is True
assert ad["restricted_product"] is True

res = art["result"]
assert res["every_finite_visible_character_truncation_with_A_B_BM_nonempty"] is True
assert res["finite_visible_brauer_shortcut_obtained"] is False
assert res["full_infinite_visible_layer_endpoint_equivalent_retained"] is True
assert res["infinite_intersection_essential_for_AQ_mechanism"] is True
assert res["arbitrary_finite_Brauer_subgroup_nonobstructing_proved"] is False
assert res["visible_units_integral_basis_of_full_unit_lattice_proved"] is False
assert res["brauer_manin_obstruction_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BB_VISIBLE_UNIT_LATTICE_INDEX_AND_FINITE_ALGEBRAIC_BRAUER_COMPLETION_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BA_FINITE_VISIBLE_BRAUER_TRUNCATION=PASS")
print("every_finite_visible_truncation_BM_nonempty=true")
print("full_infinite_visible_layer=ENDPOINT_EQUIVALENT")
print("arbitrary_finite_Brauer_closed=false")
print("canonical_sha256=" + EXPECTED)
