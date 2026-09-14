#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[3]
proof = root / "stages/stage32/proof"
md = proof / "LGS-MB101-102-REENTRY-PREFLIGHT.md"
contract_path = proof / "LGS-MB101-102-REENTRY-CONTRACT.json"
locks_path = proof / "LGS-MB101-102-SOURCE-LOCKS.json"
result_path = proof / "LGS-MB101-102-REENTRY-RESULT.json"

contract = json.loads(contract_path.read_text())
locks = json.loads(locks_path.read_text())
result = json.loads(result_path.read_text())
text = md.read_text()

assert contract["schema"] == "STAGE32_LGS_MB101_MB102_REENTRY_PREFLIGHT_V1"
assert contract["historical_blocker"] == "LGS_MISSING_POPULATION_WIDE_GLOBAL_TO_LOCAL_DEFECT_ADAPTER"
assert all(contract["forbidden"].values())

assert locks["schema"] == "STAGE32_LGS_MB101_MB102_SOURCE_LOCKS_V1"
assert locks["status"] == "EXACT_SOURCE_LOCKED"
assert locks["historical_lgs"]["route_id"] == "EX5R-LGS-001"
assert locks["historical_lgs"]["audited_exact_head"] == "79c601b636857eaaaa97ad4c22e682e681341bad"
assert locks["historical_lgs"]["hostile_audit_review"] == 5141459384
assert locks["historical_lgs"]["route_universe"]["blob_sha1"] == "68de8dc99f8947fb24873ad6c9903cfaa8491f93"
assert locks["historical_lgs"]["terminal_blocker_ledger"]["blob_sha1"] == "77bfa2a82ee117d3c3e0d61ba0dba182071323e9"
assert locks["mb_reconnection_sources"]["mb101"]["blob_sha1"] == "282fc94d8d5feb0221cf6bf096ed4b0030883563"
assert locks["mb_reconnection_sources"]["mb102"]["blob_sha1"] == "f852f66c67343b6a553b5c20e15dc0a0f55d5226"
assert locks["mb_reconnection_sources"]["mb101"]["receiver"] == "R29-LG2-MB"
assert locks["mb_reconnection_sources"]["mb102"]["receiver"] == "R29-LG2-MB"
assert locks["mb_reconnection_sources"]["mb102"]["parent_mb101_blob_sha1"] == locks["mb_reconnection_sources"]["mb101"]["blob_sha1"]
assert locks["credit"]["receiver_credit"] is False
assert locks["credit"]["stage32_main_credit"] is False
assert locks["credit"]["merge_authorized"] is False

assert result["schema"] == "STAGE32_LGS_MB101_MB102_REENTRY_RESULT_V1"
assert result["status"] == "REOPENED_MB_SUBROUTE_ONLY_NO_CREDIT"
assert result["overall_outcome"] == "DIRECT_RECONNECT"
assert result["scope_split"]["R29_LG2_MB"]["outcome"] == "DIRECT_RECONNECT"
assert result["scope_split"]["R29_LG2_MB"]["post_adapter_frontier_reached"] is True
assert result["scope_split"]["R29_LG2_EFF"]["outcome"] == "SEMANTIC_ADAPTER_GAP"
assert result["scope_split"]["R29_LG2_EFF"]["post_adapter_frontier_reached"] is False
for key, value in result["historical_requirements_now_satisfied_on_mb_side"].items():
    assert value is True, key
for key, value in result["not_satisfied"].items():
    assert value is True, key
assert result["new_smallest_blocker"]["code"] == "LGS_MB_MISSING_EXHAUSTIVE_LOCAL_DEFECT_RANGE_AND_DELTA_OFF_CONTROL"
assert result["finite_exception_reduction_obtained"] is False
assert result["mathematical_effect"]["new_pruning_terminals"] == 0
assert result["mathematical_effect"]["stage32_main_authority_changed"] is False
assert result["audit_required_before_credit"] is True
assert result["merge_authorized"] is False

for token in (
    "DIRECT_RECONNECT",
    "SEMANTIC_ADAPTER_GAP",
    "LGS_MB_MISSING_EXHAUSTIVE_LOCAL_DEFECT_RANGE_AND_DELTA_OFF_CONTROL",
    "LGS_MB_02_POPULATION_COMPLETE_LOCAL_DEFECT_RANGE_OR_BOUND_PREFLIGHT",
):
    assert token in text
assert "FINITE_EXCEPTION_REDUCTION is not obtained" in text
assert "MB101/102 are an exact ledger, not an obstruction" in text
assert "no Stage32 MAIN authority or pruning mutation" in text

print("PASS_STAGE32_LGS_MB101_MB102_REENTRY_MB_ONLY_DIRECT_RECONNECT_NO_CREDIT")
