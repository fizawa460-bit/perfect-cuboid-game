#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RETAINED = HERE / "V48-FULL-SUPPORT-384-MIN-BOUND-RETAINED.json"
AGGREGATE = HERE / "aggregate_v48_full_support_min_bound.py"
WORKFLOW = ROOT / ".github/workflows/stage32-01-178-exact-tset-probe.yml"

RETAINED_BLOB = "4d6d811015b6b1cdf660ab337864f8c19aab07aa"
AGGREGATE_BLOB = "af6abbd54f589bd1a1e9f43380b7de4aad61c8d8"
WORKFLOW_BLOB = "d9735d0de240d447f5ccc514f5c09e2a01708fa9"
RETAINED_CANON = "35b21eebce181747ad4b0511873fa09009b4258f3f9e408bbca4e2c3cecf88e8"

EXPECTED_RESULT = {
    "covered_v48_current": "37911631052805557219",
    "covered_raw_full_support_sum_over_eligible_coordinates": "37708203428994199408",
    "covered_min_replacement_sum": "37884738096346667673",
    "certified_tightening_vs_v48": "26892956458889546",
    "candidate_global_upper_bound_if_promoted": "128443319161854584903",
}


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    req(RETAINED.is_file() and blob(RETAINED) == RETAINED_BLOB, "retained blob drift")
    req(AGGREGATE.is_file() and blob(AGGREGATE) == AGGREGATE_BLOB, "aggregate blob drift")
    req(WORKFLOW.is_file() and blob(WORKFLOW) == WORKFLOW_BLOB, "workflow blob drift")

    wf = WORKFLOW.read_text()
    req("# lifecycle: RETIRED" in wf, "workflow is not retired")
    req("workflow_dispatch:" in wf, "retired replay lost manual dispatch")
    req("\n  push:" not in wf, "retired replay still has push trigger")
    req("contents: write" not in wf, "retired replay still has write permission")

    o = json.loads(RETAINED.read_text())
    req(canon(o) == RETAINED_CANON == o["canonical_sha256_without_this_field"], "retained canonical drift")
    req(o["schema"] == "STAGE32_32_01_178_V48_FULL_SUPPORT_384_MIN_BOUND_V1", "schema drift")
    req(o["status"] == "EXACT_SOURCE_MATCHED_384_COORDINATE_UPPER_BOUND_CANDIDATE__ZERO_MAIN_CREDIT", "status drift")

    ex = o["execution"]
    req(ex["workflow_run_id"] == 36065170090, "workflow run drift")
    req(ex["execution_head"] == "eca91b1718a9bcd69069ebc3020cdb382f48c6b3", "execution head drift")
    req(ex["aggregate_blob_sha1"] == AGGREGATE_BLOB, "execution aggregate lock drift")
    req(ex["result_retained_by_workflow"] is True, "retention provenance drift")

    cov = o["coverage"]
    expected_cov = {
        "expected_coordinates": 384,
        "v48_receipts": 384,
        "raw_support_receipts": 384,
        "eligible_current_worker_coordinates": 383,
        "source_ineligible_coordinates": 1,
        "strict_replacement_coordinates": 383,
        "unchanged_coordinates": 1,
        "gaps": 0,
        "overlaps": 0,
    }
    req(cov == expected_cov, "coverage drift")
    req(o["result"] == EXPECTED_RESULT, "result drift")

    bad = o["source_ineligible_coordinates"]
    req(len(bad) == 1, "source-ineligible cardinality drift")
    b = bad[0]
    req((b["row_index"], b["b"]) == (22, 47), "source-ineligible coordinate drift")
    req(b["path"] == "local-support-qbc/row022-b047.json", "source-ineligible path drift")
    req(b["blob_sha1"] == "0f161fa0df18966a8bc38f0160edd76f4f9cc1fe", "source-ineligible blob drift")
    req(b["worker_blob_sha1"] == "2c1abfd6d921122d9cf6a67a2f2251b95318e5fd", "source-ineligible worker drift")

    req(len(o["strict_coordinates"]) == 383, "strict coordinate list drift")
    comp = o["composition"]
    req(comp["additive_subtraction"] is False, "additive accounting forbidden")
    req(comp["statistical_independence"] is False, "independence assumption forbidden")
    req(comp["exact_intersection_identity_set_claimed"] is False, "identity-set overclaim")
    req(comp["uncovered_v48_population_unchanged"] is True, "uncovered population drift")

    fw = o["firewalls"]
    req(fw["hostile_audit_required_before_promotion"] is True, "audit firewall drift")
    for k in (
        "main_credit_changed",
        "full178_numerical_census_changed",
        "effectivity_credit",
        "receiver_credit",
        "route_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "merge",
    ):
        req(fw[k] is False, "credit firewall drift: " + k)

    print("V48_FULL_SUPPORT_384_MIN_BOUND_RETAINED=PASS")
    print("CERTIFIED_TIGHTENING_VS_V48=" + o["result"]["certified_tightening_vs_v48"])
    print("CANDIDATE_GLOBAL_UPPER_BOUND=" + o["result"]["candidate_global_upper_bound_if_promoted"])


if __name__ == "__main__":
    main()
