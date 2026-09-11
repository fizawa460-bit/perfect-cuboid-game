#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

CONTRACT = HERE / "JOINT_TRANSPORT_SUPPORT_SATURATION_CONTRACT.md"
LOCAL_VERIFIER = HERE / "verify_n358_joint_transport_support_saturation.py"
EXACT_VERIFIER = HERE / "verify_n358_exact_incremental_census.py"
RESULT = HERE / "RESULT.json"
STATE = HERE / "STATE.json"
HANDOFF = HERE / "AUDIT-HANDOFF.json"
N356_CONTRACT = HERE.parent / "N356" / "OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CAP_CONTRACT.md"
N357_CONTRACT = HERE.parent / "N357" / "TRANSPORT_SUPPORT_CAPACITY_CONTRACT.md"
N357_RESULT = HERE.parent / "N357" / "RESULT.json"
N357_RECEIPT = HERE.parent / "N357" / "HOSTILE-AUDIT-PASS.json"
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"

LOCKS = {
    "contract": (CONTRACT, "a9a6836dc201feefd37bebb2f6c0ef42e8faaee4"),
    "local_lemma_verifier": (LOCAL_VERIFIER, "63666cdb0f3d14676f0ab5dac561501279e8c2a0"),
    "exact_census_verifier": (EXACT_VERIFIER, "c07a7e358a6253919194189377d6ed56f95e047a"),
    "result": (RESULT, "e42c2b6cc6128c4666372b0c3f3c172afc006d7f"),
    "state": (STATE, "03d6ef2f410b2afc234ee426566a1db5ce57515b"),
    "audit_handoff": (HANDOFF, "d82a71002b5a2f233d7f88b1ba49dee107d93cc4"),
    "n356_contract": (N356_CONTRACT, "d2353cab9c175a680067c7ad4c24759b6dd15df3"),
    "n357_contract": (N357_CONTRACT, "8a2a0048d216de9d177dc581dc208b51c6436442"),
    "n357_result": (N357_RESULT, "50014d453266ad79101910a943d14388bd3ef6ec"),
    "n357_audit_receipt": (N357_RECEIPT, "e9f93fb1b2bfeb68b72598632522d164fee715c6"),
    "full178_manifest": (MANIFEST, "0a46b34e278688240656b4977e9cb7f589e90e06"),
}

EXPECTED_RESULT_CANONICAL = "383921ed9387693a8cfa300a9629f629f3a20ed4272979508441c7b13af5a287"
EXPECTED_N357_CANONICAL = "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53"
EXPECTED_N357_REVIEW = 5183069892
EXPECTED_SOURCE_STRATA = 17_128
EXPECTED_SOURCE_TERMINALS = 47_598_978_285_064_933_810_198
EXPECTED_AFFECTED_STRATA = 2_540
EXPECTED_AFFECTED_ROWS = 76
EXPECTED_REJECTED_EXCEPTIONAL = 11_344_256_366_314_850
EXPECTED_REJECTED_TERMINALS = 9_274_971_107_798_843_958
EXPECTED_REMAINING_STRATA = 17_128
EXPECTED_REMAINING_TERMINALS = 47_589_703_313_957_134_966_240
EXPECTED_STREAM = "206538209460c6b7b9cb3cc33e601a2cbf75fa084f9693af379e660ed6cf9625"
EXPECTED_EXACT_BLOB = LOCKS["exact_census_verifier"][1]


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical_sha256_without_field(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def require_false(mapping: dict, keys: tuple[str, ...], label: str) -> None:
    for key in keys:
        if mapping.get(key) is not False:
            raise ValueError(f"{label} firewall regression: {key}")


def run_verifier(path: Path, expected_marker: str) -> str:
    proc = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = proc.stdout
    if proc.returncode != 0:
        raise ValueError(f"verifier failed: {path}\n{output}")
    if expected_marker not in output:
        raise ValueError(f"verifier marker missing: {path}: {expected_marker}")
    return output


def main() -> None:
    for name, (path, expected) in LOCKS.items():
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"{name} source-lock regression: {actual} != {expected}")

    result = json.loads(RESULT.read_text())
    state = json.loads(STATE.read_text())
    handoff = json.loads(HANDOFF.read_text())
    receipt = json.loads(N357_RECEIPT.read_text())
    result357 = json.loads(N357_RESULT.read_text())

    if result.get("schema") != "STAGE32_32_01_178_N358_EXACT_INCREMENTAL_CENSUS_V1":
        raise ValueError("N358 RESULT schema regression")
    if result.get("status") != "AUDIT_CANDIDATE_EXACT_INCREMENTAL_CENSUS_NO_MAIN_CREDIT":
        raise ValueError("N358 RESULT status regression")
    canonical = canonical_sha256_without_field(result)
    if canonical != EXPECTED_RESULT_CANONICAL:
        raise ValueError(f"N358 RESULT canonical regression: {canonical}")
    if result.get("canonical_sha256_without_this_field") != EXPECTED_RESULT_CANONICAL:
        raise ValueError("N358 RESULT self-canonical regression")

    if receipt.get("status") != "PASS" or receipt.get("review_id") != EXPECTED_N357_REVIEW:
        raise ValueError("N357 hostile-audit authority regression")
    if result357.get("canonical_sha256_without_this_field") != EXPECTED_N357_CANONICAL:
        raise ValueError("N357 RESULT canonical regression")
    consumed = receipt.get("consumed_counts", {})
    if consumed.get("remaining_strata") != EXPECTED_SOURCE_STRATA or consumed.get("remaining_terminals") != EXPECTED_SOURCE_TERMINALS:
        raise ValueError("N357 retained authority count regression")

    agg = result.get("aggregate", {})
    expected_agg = {
        "source_strata": EXPECTED_SOURCE_STRATA,
        "source_terminals": EXPECTED_SOURCE_TERMINALS,
        "affected_strata": EXPECTED_AFFECTED_STRATA,
        "affected_rows": EXPECTED_AFFECTED_ROWS,
        "incremental_rejected_exceptional_prefixes": EXPECTED_REJECTED_EXCEPTIONAL,
        "incremental_rejected_terminals": EXPECTED_REJECTED_TERMINALS,
        "candidate_remaining_strata": EXPECTED_REMAINING_STRATA,
        "candidate_remaining_terminals": EXPECTED_REMAINING_TERMINALS,
        "affected_record_stream_sha256": EXPECTED_STREAM,
    }
    for key, value in expected_agg.items():
        if agg.get(key) != value:
            raise ValueError(f"N358 RESULT aggregate regression: {key}")
    if EXPECTED_SOURCE_TERMINALS - EXPECTED_REJECTED_TERMINALS != EXPECTED_REMAINING_TERMINALS:
        raise ValueError("N358 partition identity regression")

    audited_input = result.get("audited_input", {})
    if audited_input.get("review_id") != EXPECTED_N357_REVIEW:
        raise ValueError("N358 audited-input review regression")
    if audited_input.get("remaining_strata") != EXPECTED_SOURCE_STRATA or audited_input.get("remaining_terminals") != EXPECTED_SOURCE_TERMINALS:
        raise ValueError("N358 audited-input count regression")
    if audited_input.get("result_canonical_sha256") != EXPECTED_N357_CANONICAL:
        raise ValueError("N358 audited-input canonical regression")

    semantics = result.get("semantics", {})
    if semantics.get("external_hostile_audit_required_before_credit") is not True:
        raise ValueError("N358 hostile-audit firewall regression")
    require_false(
        semantics,
        (
            "main_pruning_credit", "full178_complete", "heavy_compute_authorized",
            "merge_authorized", "n104_release", "n350_producer_registered",
            "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
            "production_complete", "receiver_credit", "stage32_closed",
            "theorem_credit", "endpoint_credit",
        ),
        "N358 RESULT",
    )

    if state.get("schema") != "STAGE32_32_01_178_N358_RESEARCH_STATE_V2":
        raise ValueError("N358 STATE schema regression")
    if state.get("status") != "AUDIT_REQUIRED_EXACT_INCREMENTAL_CENSUS_FROZEN_NO_MAIN_CREDIT":
        raise ValueError("N358 STATE status regression")
    cand = state.get("candidate", {})
    state_expected = {
        "exact_incremental_rejected_exceptional_prefixes": EXPECTED_REJECTED_EXCEPTIONAL,
        "exact_incremental_rejected_terminals": EXPECTED_REJECTED_TERMINALS,
        "affected_strata": EXPECTED_AFFECTED_STRATA,
        "affected_rows": EXPECTED_AFFECTED_ROWS,
        "candidate_remaining_strata": EXPECTED_REMAINING_STRATA,
        "candidate_remaining_terminals": EXPECTED_REMAINING_TERMINALS,
        "result_canonical_sha256": EXPECTED_RESULT_CANONICAL,
        "exact_census_verifier_blob_sha1": EXPECTED_EXACT_BLOB,
        "affected_record_stream_sha256": EXPECTED_STREAM,
    }
    for key, value in state_expected.items():
        if cand.get(key) != value:
            raise ValueError(f"N358 STATE candidate regression: {key}")
    credit = state.get("credit", {})
    require_false(
        credit,
        (
            "n358_main_pruning_credit", "full178_complete", "n350_producer_registered",
            "production_complete", "n104_release", "receiver_credit", "theorem_credit",
            "endpoint_credit", "stage32_closed", "perfect_cuboid_existence_claim",
            "perfect_cuboid_nonexistence_claim", "heavy_compute_authorized", "merge_authorized",
        ),
        "N358 STATE",
    )

    if handoff.get("schema") != "STAGE32_32_01_178_N358_AUDIT_HANDOFF_V1":
        raise ValueError("N358 AUDIT-HANDOFF schema regression")
    if handoff.get("status") != "READY_FOR_INDEPENDENT_HOSTILE_AUDIT_NO_MAIN_CREDIT":
        raise ValueError("N358 AUDIT-HANDOFF status regression")
    hcand = handoff.get("candidate", {})
    handoff_expected = {
        "incremental_rejected_terminals": EXPECTED_REJECTED_TERMINALS,
        "affected_strata": EXPECTED_AFFECTED_STRATA,
        "candidate_remaining_strata": EXPECTED_REMAINING_STRATA,
        "candidate_remaining_terminals": EXPECTED_REMAINING_TERMINALS,
        "result_canonical_sha256": EXPECTED_RESULT_CANONICAL,
        "affected_record_stream_sha256": EXPECTED_STREAM,
    }
    for key, value in handoff_expected.items():
        if hcand.get(key) != value:
            raise ValueError(f"N358 AUDIT-HANDOFF candidate regression: {key}")

    hlocks = handoff.get("source_locks", {})
    handoff_lock_expectations = {
        "contract": LOCKS["contract"][1],
        "local_lemma_verifier": LOCKS["local_lemma_verifier"][1],
        "exact_census_verifier": LOCKS["exact_census_verifier"][1],
        "result": LOCKS["result"][1],
        "state": LOCKS["state"][1],
        "n357_result": LOCKS["n357_result"][1],
        "n357_audit_receipt": LOCKS["n357_audit_receipt"][1],
        "full178_manifest": LOCKS["full178_manifest"][1],
    }
    for key, expected in handoff_lock_expectations.items():
        if hlocks.get(key, {}).get("blob_sha1") != expected:
            raise ValueError(f"N358 AUDIT-HANDOFF retained source-lock regression: {key}")
    require_false(
        handoff.get("firewalls", {}),
        (
            "n358_main_pruning_credit", "full178_complete", "production_complete",
            "n104_release", "receiver_credit", "theorem_credit", "endpoint_credit",
            "stage32_closed", "merge_authorized",
        ),
        "N358 AUDIT-HANDOFF",
    )

    local_output = run_verifier(LOCAL_VERIFIER, "PASS_N358_JOINT_TRANSPORT_SUPPORT_SATURATION")
    exact_output = run_verifier(EXACT_VERIFIER, "PASS_N358_EXACT_INCREMENTAL_CENSUS_AUDIT_CANDIDATE")

    print(json.dumps({
        "verdict": "PASS_N358_FROZEN_AUDIT_BOUNDARY_RETAINED_ARTIFACT_IDENTITY",
        "result_canonical_sha256": canonical,
        "source_strata": EXPECTED_SOURCE_STRATA,
        "source_terminals": EXPECTED_SOURCE_TERMINALS,
        "affected_strata": EXPECTED_AFFECTED_STRATA,
        "affected_rows": EXPECTED_AFFECTED_ROWS,
        "incremental_rejected_terminals": EXPECTED_REJECTED_TERMINALS,
        "candidate_remaining_strata": EXPECTED_REMAINING_STRATA,
        "candidate_remaining_terminals": EXPECTED_REMAINING_TERMINALS,
        "affected_record_stream_sha256": EXPECTED_STREAM,
        "local_lemma_exact_replay": "PASS_N358_JOINT_TRANSPORT_SUPPORT_SATURATION" in local_output,
        "exact_census_replay": "PASS_N358_EXACT_INCREMENTAL_CENSUS_AUDIT_CANDIDATE" in exact_output,
        "retained_artifact_identity_fail_closed": True,
        "n358_main_pruning_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
