#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PATH = HERE / "FEASIBILITY-AUDIT.json"


def canonical_without_hash(payload):
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    payload = json.loads(PATH.read_text())
    require(payload["schema"] == "STAGE32_MAIN_SECOND_STRIKE_FEASIBILITY_AUDIT_V1", "schema drift")
    require(payload["status"] == "COLD_AUDIT_HANDOFF_NO_RESEARCH_EXECUTION_NO_CREDIT", "audit must stay cold")
    require(payload["authority_boundary"]["authority_changed_by_this_audit"] is False, "authority mutation forbidden")

    findings = {item["id"]: item for item in payload["findings"]}
    require(set(findings) == {
        "SECOND_STRIKE.HPADJ08",
        "SECOND_STRIKE.N401_EX5",
        "SECOND_STRIKE.CUT_THEOREM_MINING",
        "SECOND_STRIKE.REVERSE_REALIZATION",
    }, "finding set drift")
    require(findings["SECOND_STRIKE.HPADJ08"]["dedup_disposition"] == "DO_NOT_CREATE_A_DUPLICATE_HPADJ08_THEOREM_FAMILY", "HPADJ dedup firewall missing")
    require(findings["SECOND_STRIKE.N401_EX5"]["existing_route"]["n401_audit_review_id"] == 5203957365, "N401 audit lock drift")
    require(findings["SECOND_STRIKE.N401_EX5"]["existing_route"]["n401_result_blob_sha1"] == "d24b2100c90bd6e0f575572765a35fafaaa89196", "N401 result blob drift")
    require(findings["SECOND_STRIKE.CUT_THEOREM_MINING"]["existing_route"]["hostile_audit_passed"] is False, "CUT201 audit must not be promoted")
    require(findings["SECOND_STRIKE.CUT_THEOREM_MINING"]["existing_route"]["candidate_pruned_terminals"] == 25538, "CUT201 candidate count drift")

    require(payload["main_audit_decision"]["estimated_10e21_to_10e22_reduction_supported_now"] is False, "unsupported reduction forecast")
    require(payload["main_audit_decision"]["new_cross_lane_demand_created"] is False, "audit PR must not reprioritize live lanes")
    require(payload["main_audit_decision"]["merge_ready"] is False, "merge readiness forbidden")

    firewalls = payload["credit_firewall"]
    require(firewalls["noncredit_probe_only"] is True, "noncredit scope missing")
    for key, value in firewalls.items():
        if key == "noncredit_probe_only":
            continue
        require(value is False, f"credit/authority firewall must be false: {key}")

    expected = canonical_without_hash(payload)
    require(payload["canonical_sha256_without_this_field"] == expected, "canonical hash mismatch")
    print("PASS: Stage32 second-strike feasibility audit is cold, deduplicated, source-locked, and grants no credit")


if __name__ == "__main__":
    main()
