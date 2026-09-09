#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
state = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))

assert state["schema"] == "STAGE32EX2_MAIN_COMPACT_STATE_V2_POST1728_DOMINATED"
assert state["stage"] == "32EX2"
assert state["current"]["status"] == "DOMINATED_BY_AUDITED_V6_NONEXISTENCE"
assert state["current"]["stop_semantics"] == "LANE_DOMINATED_NO_ACTIVE_FRONTIER_ATTACK"
assert state["current"]["next_route"] == "NONE_WITHOUT_EXPLICIT_REENTRY"

authority = state["authority"]
assert authority["dominating_claim_id"] == "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2"
assert authority["dominating_claim_authority"] == "AUDITED"
assert authority["dominating_audit_review_id"] == 5147810198
assert authority["source_pr"] == 1728

cc = state["completion_contract"]
assert cc["lane_terminal_outcome_independently_established"] is False
assert cc["dominated_by_external_audited_population_decision"] is True
assert cc["reentry_requires_new_target_not_already_contained_in_audited_v6_negative_population"] is True

front = state["frontier"]
assert front["EX2_independently_proved_population_wide_no_genus1_member"] is False
assert front["dominated_by_audited_main_v6_nonexistence"] is True
assert front["active_research"] is False
assert front["active_frontier_refs"] == []

credit = state["credit"]
assert credit["full_target_closure"] is False
assert credit["stage32_main_credit_from_EX2"] is False
assert credit["Q602_excluded"] is False
assert credit["O210_excluded"] is False
assert credit["stage32_closed"] is False

for rel in state["current_leaf_working_set"]:
    assert (ROOT / rel).is_file(), rel

print("PASS_STAGE32EX2_DOMINATED_BY_AUDITED_V6_NONEXISTENCE_POST1728")
