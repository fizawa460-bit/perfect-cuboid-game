#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
state = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))

assert state["schema"] == "STAGE32EX1_MAIN_COMPACT_STATE_V20_POST1728_COMPLETED_AUDITED_HANDOFF"
assert state["stage"] == "32EX1"
assert state["current"]["status"] == "COMPLETED_AUDITED_HANDOFF"
assert state["current"]["stop_semantics"] == "LANE_COMPLETE_NO_ACTIVE_FRONTIER_ATTACK"
assert state["current"]["next_route"] == "NONE_WITHOUT_EXPLICIT_REENTRY"

authority = state["authority"]
assert authority["terminal_claim_id"] == "S32.EX1.ALL_V6_GENUS1_CARRIERS_EXCLUDED_CANDIDATE.V2"
assert authority["terminal_claim_authority"] == "AUDITED"
assert authority["terminal_audit_review_id"] == 5147627146
assert authority["promotion_adapter_id"] == "S32.ADAPTER.EX1_V6_CARRIER_TO_MAIN_V6_CARRIER.V1"
assert authority["promotion_adapter_authority"] == "AUDITED"
assert authority["promotion_audit_review_id"] == 5147810198
assert authority["main_v6_negative_claim_id"] == "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2"
assert authority["main_v6_negative_claim_authority"] == "AUDITED"

assert state["completion_contract"]["terminal_outcome"] == "ALL_V6_GENUS1_CARRIERS_EXCLUDED"
assert state["completion_contract"]["terminal_result_consumed_by_main_through_explicit_adapter"] is True
assert state["frontier"]["all_v6_genus1_carriers_excluded_audited"] is True
assert state["frontier"]["full_target_closure"] is True
assert state["frontier"]["active_research"] is False
assert state["frontier"]["active_frontier_refs"] == []

credit = state["credit"]
assert credit["full_target_closure"] is True
assert credit["all_v6_genus1_carriers_excluded"] is True
assert credit["main_handoff_completed"] is True
assert credit["Q602_excluded"] is False
assert credit["O210_excluded"] is False
assert credit["stage32_closed"] is False

assert state["audit"]["terminal"] == {
    "status":"PASS","pr":1728,"review_id":5147627146,
    "exact_head":"e3c4a04d5010e6dca9428722e334890e2614297a"
}
assert state["audit"]["promotion"] == {
    "status":"PASS","pr":1728,"review_id":5147810198,
    "exact_head":"89ba026f05f9fe5344c0f0fb41fe8c2366032877"
}

for rel in state["current_leaf_working_set"]:
    assert (Path(__file__).resolve().parents[2] / rel).is_file(), rel

print("PASS_STAGE32EX1_COMPLETED_AUDITED_HANDOFF_POST1728")
