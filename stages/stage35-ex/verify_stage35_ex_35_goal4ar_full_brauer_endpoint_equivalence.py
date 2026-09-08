#!/usr/bin/env python3
"""Verify Goal4AR: full Brauer–Manin orthogonality is endpoint-equivalent."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4ar-full-brauer-bm-endpoint-equivalence.json")
SRC = P("stages/stage35-ex/35ex-35/goal4ar-full-brauer-bm-endpoint-equivalence-source-lock.md")
AQ = P("stages/stage35-ex/35ex-35/goal4aq-unit-character-bm-endpoint-equivalence.json")
S31 = P("stages/stage35-ex/35ex-31/primitive-source-marking-endpoint-equivalence.md")
POLICY = P("docs/research-os/policies/cycle-exploration-safety-protocol.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "203bc01c9e3824bdb556ab08e43b015de7923b6cfa0cd4bd2acfe804a827cceb"
SRC_BLOB = "f3eb04236023b3f73e3de3c64a461e4fcc7d3609"
AQ_CANON = "21d865d7a15d6f9b66f87361c0ac49de9eaac89947395d04686ea747d1a7956e"
S31_BLOB = "01aa855c32289a467fb66759e25dc90f18df9f80"
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
assert blob(S31) == S31_BLOB
assert blob(POLICY) == POLICY_BLOB

aq = json.loads(AQ.read_text())
assert aq["canonical_sha256"] == AQ_CANON
assert aq["result"]["source_marked_unit_BM_nonempty_iff_positive_source_marked_Q_point_nonempty"] is True
assert aq["result"]["positive_source_marked_Q_point_nonempty_iff_stage35_E1_counterexample_population_nonempty"] is True
assert aq["result"]["full_unit_character_route"] == "ENDPOINT_EQUIVALENT_BLOCKER"

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["brauer_manin_obstruction_obtained"] is False
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

src = SRC.read_text()
for marker in (
    "B_unit subset Br_a(U) subset Br(U)",
    "(A_src^loc)^(Br(U)) subset (A_src^loc)^(B_unit)",
    "diagonal adelic point",
    "global reciprocity",
    "(AR-EQUIV)",
    "FINITE_TRANSCENDENTAL_SHORTCUT_RULED_OUT=false",
    "EXHAUSTIVE_VIEW_AUDIT",
    "BLIND_REDISCOVERY",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4ar_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4aq"]["canonical_sha256"] == AQ_CANON
assert art["source_locks"]["goal4aq"]["exact_head_sha"] == "c1dc9ff4d84a87d6301e78c00d35b69aa16a07f7"
assert art["source_locks"]["goal4aq"]["aggregate_run"] == 34281502796
assert art["source_locks"]["goal4aq"]["aggregate_job"] == 102248643350

st = art["set_theory"]
assert st["unit_layer_subset"] == "B_unit subset Br_a(U) subset Br(U)"
assert st["orthogonality_inclusion"] == "A_src^loc^Br(U) subset A_src^loc^B_unit"
assert st["goal4aq_unit_equivalence"] is True

dc = art["diagonal_converse"]
assert dc["positive_source_marked_Q_point_defines_diagonal_adele_in_A_src_loc"] is True
assert dc["diagonal_rational_point_orthogonal_to_all_BrU_by_global_reciprocity"] is True

r = art["result"]
assert r["full_Brauer_BM_nonempty_iff_unit_layer_BM_nonempty"] is True
assert r["full_Brauer_BM_nonempty_iff_positive_source_marked_Q_point_nonempty"] is True
assert r["positive_source_marked_Q_point_nonempty_iff_stage35_E1_counterexample_population_nonempty"] is True
assert r["full_Brauer_route"] == "ENDPOINT_EQUIVALENT_BLOCKER"
assert r["transcendental_Brauer_group_needed_for_equivalence"] is False
assert r["finite_additional_Brauer_shortcut_ruled_out"] is False

cy = art["cycle"]
assert cy["exhaustive_view_audit_required"] is True
assert cy["blind_rediscovery_required"] is True
assert cy["split_triggered"] is False

fw = art["credit_firewall"]
assert fw["transcendental_brauer_group_computed"] is False
assert fw["finite_transcendental_shortcut_ruled_out"] is False
assert fw["brauer_manin_obstruction_obtained"] is False
assert fw["E1_proved"] is False
assert fw["stage35_closed"] is False
assert fw["perfect_cuboid_existence_claim"] is False
assert fw["perfect_cuboid_nonexistence_claim"] is False

print("STAGE35_EX_GOAL4AR_FULL_BRAUER_ENDPOINT_EQUIVALENCE=PASS")
print("full_Brauer_route=ENDPOINT_EQUIVALENT_BLOCKER")
print("finite_additional_Brauer_shortcut_ruled_out=false")
print("fresh_exhaustive_view_audit_required=true")
print("canonical_sha256=" + EXPECTED)
