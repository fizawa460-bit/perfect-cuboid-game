#!/usr/bin/env python3
"""Verify Goal4BB: every finite Brauer subgroup is non-obstructing on A_src^loc."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bb-arbitrary-finite-brauer-subgroup-nonobstruction.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bb-arbitrary-finite-brauer-subgroup-nonobstruction-source-lock.md")
BA = P("stages/stage35-ex/35ex-35/goal4ba-finite-visible-brauer-truncation-nonobstruction.json")
AR = P("stages/stage35-ex/35ex-35/goal4ar-full-brauer-bm-endpoint-equivalence.json")
AO = P("stages/stage35-ex/35ex-35/goal4ao-source-marked-two-class-bm-nonempty.json")
AN_SRC = P("stages/stage35-ex/35ex-35/goal4an-known-two-class-upc-bm-nonempty-source-lock.md")
O22 = P("stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "5e6de05be48bff4121f1177ea62e70c09b6db67348da991c9139003bb3db73cb"
SRC_BLOB = "c852a5d1c5b821809cea37eb24c2bd13eaccaf09"
BA_BLOB = "e0723b9686fabfe09782be2d9e783fc7d89c72da"
AR_BLOB = "4c9dccefb9a63d1a4a9e78fd53b89a4c6adfdf36"
AO_BLOB = "3b39f15aed87e66558c9cbc02cc02529e98a9692"
AN_SRC_BLOB = "694b23125c59dfd3cd44152c982ac6667391fbf0"
O22_BLOB = "537ca589cd45112cca4c8f8091f5c8c77264e70d"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


for path, want in ((SRC,SRC_BLOB),(BA,BA_BLOB),(AR,AR_BLOB),(AO,AO_BLOB),(AN_SRC,AN_SRC_BLOB),(O22,O22_BLOB)):
    assert blob(path) == want, (path, blob(path), want)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

ba = json.loads(BA.read_text())
assert ba["canonical_sha256"] == "86aa145782a998c32ef4cf451ae4ce6ad790f4ce09e15ecd7cbf63167bf1c213"
assert ba["result"]["every_finite_visible_character_truncation_with_A_B_BM_nonempty"] is True
assert ba["result"]["arbitrary_finite_Brauer_subgroup_nonobstructing_proved"] is False

ar = json.loads(AR.read_text())
assert ar["result"]["full_Brauer_BM_nonempty_iff_positive_source_marked_Q_point_nonempty"] is True
assert ar["result"]["finite_additional_Brauer_shortcut_ruled_out"] is False

ao = json.loads(AO.read_text())
assert ao["local_population"]["name"] == "A_src^loc"
assert ao["two_adic_anchor"]["v2_x"] == 4
assert ao["two_adic_anchor"]["such_deformations_exist_in_every_sufficiently_small_neighborhood"] is True

o22 = json.loads(O22.read_text())
assert o22["common_zero_specialization"]["point"] == {"x":"272/225","y":"0","p":"353/225","q":"1","z":"272/225","w":"353/225"}
assert o22["common_zero_specialization"]["smooth_on_affine_surface"] is True
assert o22["common_zero_specialization"]["outside_selected_open_only_because"] == "y=0"
assert o22["restricted_product_repair"]["integral_U_PC_Zl_point_for_every_prime_l_ge_173"] is True
assert o22["restricted_product_repair"]["smooth_Fl_point_lifts_to_Zl"] is True

src = SRC.read_text()
for marker in (
    "(BB-LOC)", "(BB-P*)", "(BB-F)", "(BB-2)", "(BB-BAD)", "(BB-GOOD)",
    "(BB-MATCH)", "(BB-THEOREM)", "(BB-FINITE)",
    "for **every finite set `F subset Br(U)`**",
    "finite_additional_Brauer_shortcut_ruled_out=true",
    "35EX-35_GOAL4BC_POST_GOAL4AS_LEDGER_EXHAUSTION_FRESH_VIEW_AUDIT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["schema"] == "STAGE35_EX_GOAL4BB_ARBITRARY_FINITE_BRAUER_SUBGROUP_NONOBSTRUCTION_V1"
assert art["unit"] == "35EX-35_GOAL4BB_ARBITRARY_FINITE_BRAUER_SUBGROUP_NONOBSTRUCTION_PREFLIGHT"
assert art["authority"]["state_schema"] == V74
assert art["authority"]["hostile_review_id"] == 5142248509
assert art["stacked_parent"]["exact_head_sha"] == "540721b4046a0849fc6fe162025e6c8d46898850"
assert art["stacked_parent"]["aggregate_run"] == 34301954559
assert art["stacked_parent"]["aggregate_job"] == 102311776547
assert art["stacked_parent"]["hostile_audited"] is False

locks = art["source_locks"]
assert locks["goal4bb_source"]["blob_sha1"] == SRC_BLOB
assert locks["goal4ba"]["blob_sha1"] == BA_BLOB
assert locks["goal4ar"]["blob_sha1"] == AR_BLOB
assert locks["goal4ao"]["blob_sha1"] == AO_BLOB
assert locks["goal4an_source"]["blob_sha1"] == AN_SRC_BLOB
assert locks["obvious_35ex22"]["blob_sha1"] == O22_BLOB

th = art["finite_set_theorem"]
assert th["input"].startswith("any finite set F=")
assert th["algebraicity_required"] is False
assert th["explicit_symbol_required"] is False
assert th["common_bad_set_exists"] is True
assert th["common_local_constancy_neighborhood_exists"] is True
assert th["simultaneous_two_adic_source_marking"] is True
assert th["good_prime_integral_evaluations_zero"] is True
assert th["all_local_invariant_vectors_match_rational_anchor"] is True
assert th["global_reciprocity_closes_each_class"] is True
assert th["conclusion"] == "(A_src^loc)^F != empty"

anc = art["anchor_and_good_primes"]
assert anc["anchor_in_U_Q"] is True
assert anc["anchor_outside_U_PC_only_y_zero"] is True
assert anc["v2_x"] == 4
assert anc["integral_open_point_every_prime_ge_173"] is True
assert anc["smooth_hensel_points"] is True

res = art["result"]
assert res["every_finite_subset_BrU_BM_nonempty"] is True
assert res["every_finite_Brauer_subgroup_BM_nonempty"] is True
assert res["finite_additional_Brauer_shortcut_ruled_out"] is True
assert res["finite_transcendental_classes_included"] is True
assert res["full_infinite_Brauer_BM_nonempty_claimed"] is False
assert res["full_Brauer_route_endpoint_equivalent_retained"] is True
assert res["Brauer_group_explicitly_computed"] is False
assert res["transcendental_Brauer_group_computed"] is False
assert res["infinite_intersection_required_for_any_Brauer_obstruction"] is True

ledger = art["goal4as_ledger"]
assert ledger["post_ledger_fresh_audit_required"] is True
for key in ("marked_kummer_common_cover","canonical_height","nonlinear_full_endpoint_descent","finite_additional_brauer_shortcut","super_sqrt_amplification","cross_face_norm_torsor","linked_selmer_cassels_common_cover"):
    assert key in ledger

assert art["next"]["unit"] == "35EX-35_GOAL4BC_POST_GOAL4AS_LEDGER_EXHAUSTION_FRESH_VIEW_AUDIT"
for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BB_ARBITRARY_FINITE_BRAUER_SUBGROUP=PASS")
print("every_finite_subset_BrU_BM_nonempty=true")
print("every_finite_Brauer_subgroup_BM_nonempty=true")
print("finite_brauer_shortcut_ruled_out=true")
print("full_infinite_Brauer_BM_nonempty=false")
print("canonical_sha256=" + EXPECTED)
