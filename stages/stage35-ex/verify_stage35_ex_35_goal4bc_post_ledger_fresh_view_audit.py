#!/usr/bin/env python3
"""Verify Goal4BC: Goal4AS ledger exhaustion and fresh blind/Arsenal-deduplicated route selection."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bc-post-goal4as-ledger-exhaustion-fresh-view-audit.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bc-post-goal4as-ledger-exhaustion-fresh-view-audit-source-lock.md")
BB = P("stages/stage35-ex/35ex-35/goal4bb-arbitrary-finite-brauer-subgroup-nonobstruction.json")
AS = P("stages/stage35-ex/35ex-35/goal4as-fresh-exhaustive-view-marked-kummer.json")
L = P("stages/stage35-ex/35ex-35/goal4l-stage14-pythagorean-elliptic-rankjump-receiver.json")
AU = P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation.json")
POL = P("docs/research-os/policies/repository-asset-discovery.md")
IDX = P("docs/arsenal/index.json")
CARD = P("docs/arsenal/cards/formal/S34-W03.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "8fc7c10847b7d819fa267696eca84439304b15f253a7ca9a0f37b0e2e2ab89ea"
LOCKS = {
    SRC: "dfd13d7c96a7c87da19409c173805e5f64b57519",
    BB: "54190746afae7e6e8fece7b065311a5ae0b36023",
    AS: "5f17e0ec3d325127b517ac2afb418ec4cb309868",
    L: "0717ca307162d5559a005801848288daa91285fd",
    AU: "d0dd0597046daf54ad9fcc74991221710a27f12c",
    POL: "bf001d4ff4375281a901d52c147c35c28643b8a3",
    IDX: "82cbbe88b2a3afc7f3a13d34ce0ca6a43004ea98",
    CARD: "1d5275321f42768a6414d4610ac912c63be43f96",
}
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

for path, want in LOCKS.items():
    assert blob(path) == want, (path, blob(path), want)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bb = json.loads(BB.read_text())
assert bb["canonical_sha256"] == "5e6de05be48bff4121f1177ea62e70c09b6db67348da991c9139003bb3db73cb"
assert bb["result"]["every_finite_Brauer_subgroup_BM_nonempty"] is True
assert bb["result"]["full_infinite_Brauer_BM_nonempty_claimed"] is False
assert bb["next"]["unit"] == "35EX-35_GOAL4BC_POST_GOAL4AS_LEDGER_EXHAUSTION_FRESH_VIEW_AUDIT"

asj = json.loads(AS.read_text())
old = set(asj["blind_pass"]["generated_lenses"])
assert old == {
    "MARKED_ELLIPTIC_2DESCENT_KUMMER",
    "CANONICAL_HEIGHT_LOWER_VS_ENDPOINT_UPPER",
    "GENUINE_NONLINEAR_FULL_ENDPOINT_DESCENT",
    "FINITE_EXPLICIT_BRAUER_SHORTCUT",
    "LINKED_SELMER_CASSELS_COMMON_COVER",
    "AMPLIFICATION_OR_STRONGER_COUNTING",
    "CROSS_FACE_NORM_LATTICE_SPINOR_TORSOR",
}

lj = json.loads(L.read_text())
assert lj["birational_adapter"]["elliptic_curve"] == "E_q: Y^2=X*(X-1)*(X+q^2)"
assert lj["rank_jump_receiver"]["new_receiver_obtained"] is True
assert lj["torsion_exclusion_on_physical_endpoint"]["conclusion"] == "every physical endpoint maps to a non-torsion E_q(Q) point"

auj = json.loads(AU.read_text())
assert auj["result"]["cross_face_marked_kummer_product_one_obtained"] is True
assert auj["cross_face_relation"]["marked_product"] == "d_A*d_B*d_C=1 in Q*/Q*^2"
assert auj["cross_face_relation"]["any_d_i_trivial_forced"] is False
assert auj["relation_to_goal4j"]["common_selmer_complex_constructed"] is False

card = CARD.read_text()
assert "RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION" in card
assert "B(Q) intersect K(Q) = empty" in card
assert "receiver branch closed = allowed" in card
assert "factor cover Q-pointset complete = not implied" in card

src = SRC.read_text()
for marker in (
    "BC-B1", "BC-B2", "BC-B3", "BC-B4", "BC-B5",
    "SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_RECEIVER",
    "GCD_RESERVOIR_QUADRATIC_RECIPROCITY_CYCLE",
    "FINITE_CONDUCTOR_BOUNDARY_ESCAPE_VS_HEIGHT",
    "DERIVED_FOURTH_SQUARE_DEFECT_TWO_CYCLE",
    "S34-W03",
    "35EX-35_GOAL4BD_SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
x = dict(art)
got = x.pop("canonical_sha256")
calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
assert got == calc == EXPECTED, (got, calc)
assert art["authority"]["state_schema"] == V74
assert art["stacked_parent"]["exact_head_sha"] == "72f9163b39041e2b5c13d8e511b534b018015ef8"
assert art["stacked_parent"]["aggregate_run"] == 34303063969
assert art["stacked_parent"]["aggregate_job"] == 102315193038
assert art["stacked_parent"]["hostile_audited"] is False

led = art["goal4as_ledger_exhaustion"]
assert led["all_original_lenses_exact_tested"] is True
assert len([k for k in led if k != "all_original_lenses_exact_tested"]) == 7

blind = art["blind_pass"]
assert blind["executed_before_arsenal"] is True
assert len(blind["generated_lenses"]) == 5
assert "SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_RECEIVER" in blind["generated_lenses"]

dedup = art["arsenal_dedup"]
assert dedup["matching_router"] == "S34-W03"
assert dedup["router_constructs_missing_receiver"] is False
assert dedup["router_grants_current_closure"] is False
assert dedup["selected_lens_survives_dedup"] is True

sel = art["selected_new_view"]
assert sel["id"] == "SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_RECEIVER"
assert sel["three_cyclic_maps_source_locked"] is True
assert sel["joint_receiver_materialized_yet"] is False
assert sel["selmer_or_cassels_obstruction_claimed"] is False

assert art["priority_order"][0] == sel["id"]
assert art["next"]["unit"] == "35EX-35_GOAL4BD_SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_PREFLIGHT"
assert len(art["next"]["required_outputs"]) == 5
for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BC_POST_LEDGER_FRESH_VIEW_AUDIT=PASS")
print("goal4as_original_lenses_exhausted=true")
print("blind_pass_before_arsenal=true")
print("selected=SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_RECEIVER")
print("joint_receiver_materialized=false")
print("next=35EX-35_GOAL4BD_SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_PREFLIGHT")
print("canonical_sha256=" + EXPECTED)
