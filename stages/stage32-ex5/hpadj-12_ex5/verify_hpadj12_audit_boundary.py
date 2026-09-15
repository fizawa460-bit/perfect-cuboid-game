#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOUNDARY = HERE / "AUDIT-BOUNDARY.json"
REPAIR = HERE / "PROVENANCE-REPAIR.json"
RESULT = HERE / "ROW-STRATIFIED-RESULT.json"
CERT = HERE / "HPADJ08-ROW-REJECT-CERTIFICATE.json"
PRODUCER = HERE / "derive_row_stratified_removed_block_bound.py"

LOCKS = {
    "boundary_blob": "a0cb558a082ec035b663dbf8a4e6679dd8bb6439",
    "boundary_canonical": "e886871e818f3af80d582509937789c7d0db3bc5b4d4b7e3a32b9bd2e1dc0a47",
    "repair_blob": "ebb8f6f64bc393e907ea9ace8fb6bbb003be6df5",
    "repair_canonical": "0eed2308cce3ca17f1ce0cad9c6ac98b7d01784266c91a29b29ee0b2446a7aa6",
    "result_blob": "749c6e38b79cc1e6783635fbac43acccb004e1ad",
    "result_canonical": "2b710888bd332e4c402f086ae0e5177acfd96a003a6bb30991b2f67e131b2e74",
    "certificate_blob": "29ef2acf15e6649f5db90935f53b65a9388f7db4",
    "producer_blob": "8d022e45ee65e30cbaee19e4cc25855edbe0d468",
}

AUTHORITATIVE_HPADJ08_REVIEW_ID = 5208789388
DEPRECATED_EMBEDDED_REVIEW_ID = 5205760920
HPADJ08_AUDITED_HEAD = "36eab50192cf80ec5ed48aba40f4a56076759fea"


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(value: dict) -> str:
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_locked_json(path: Path, blob: str, canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(git_blob(path) == blob, f"{label} blob drift")
    value = json.loads(path.read_text())
    req(value.get("canonical_sha256_without_this_field") == canon, f"{label} stored canonical drift")
    req(canonical(value) == canon, f"{label} canonical drift")
    return value


def main() -> None:
    # Fail closed on the repaired provenance and frozen audit boundary before
    # interpreting the row-stratified mathematical result.
    repair = load_locked_json(REPAIR, LOCKS["repair_blob"], LOCKS["repair_canonical"], "HPADJ12 provenance repair")
    boundary = load_locked_json(BOUNDARY, LOCKS["boundary_blob"], LOCKS["boundary_canonical"], "HPADJ12 audit boundary")
    result = load_locked_json(RESULT, LOCKS["result_blob"], LOCKS["result_canonical"], "HPADJ12 row-stratified result")
    req(CERT.is_file() and git_blob(CERT) == LOCKS["certificate_blob"], "HPADJ08 row certificate blob drift")
    req(PRODUCER.is_file() and git_blob(PRODUCER) == LOCKS["producer_blob"], "HPADJ12 producer blob drift")

    req(repair["authoritative_audit"]["pr"] == 1812, "HPADJ08 PR drift")
    req(repair["authoritative_audit"]["review_id"] == AUTHORITATIVE_HPADJ08_REVIEW_ID, "HPADJ08 authoritative review drift")
    req(repair["authoritative_audit"]["audited_exact_head"] == HPADJ08_AUDITED_HEAD, "HPADJ08 audited-head drift")
    req(repair["authoritative_audit"]["audit_result"] == "PASS", "HPADJ08 audit result drift")
    req(repair["certificate"]["embedded_hpadj08_hostile_audit_review_id"] == DEPRECATED_EMBEDDED_REVIEW_ID, "deprecated embedded review-id drift")
    req(repair["semantics"]["embedded_review_id_is_deprecated_typo"] is True, "provenance typo not explicitly deprecated")
    req(repair["semantics"]["repair_changes_mathematical_count"] is False, "provenance repair changed mathematical count")

    # The pre-repair result is retained byte-for-byte.  Its stale review-id is
    # deliberately recognized here and superseded only by the locked repair.
    req(result["sources"]["hpadj08_hostile_audit_review_id"] == DEPRECATED_EMBEDDED_REVIEW_ID, "expected pre-repair result provenance drift")
    req(result["sources"]["hpadj08_audited_exact_head"] == HPADJ08_AUDITED_HEAD, "result HPADJ08 head drift")

    locks = boundary["source_locks"]
    req(locks["provenance_repair_blob_sha1"] == LOCKS["repair_blob"], "boundary repair blob lock drift")
    req(locks["provenance_repair_canonical_sha256"] == LOCKS["repair_canonical"], "boundary repair canonical lock drift")
    req(locks["row_reject_certificate_blob_sha1"] == LOCKS["certificate_blob"], "boundary certificate blob lock drift")
    req(locks["row_stratified_producer_blob_sha1"] == LOCKS["producer_blob"], "boundary producer blob lock drift")
    req(locks["row_stratified_result_blob_sha1"] == LOCKS["result_blob"], "boundary result blob lock drift")
    req(locks["row_stratified_result_canonical_sha256"] == LOCKS["result_canonical"], "boundary result canonical lock drift")

    audit = boundary["authoritative_hpadj08_audit"]
    req(audit["pr"] == 1812, "boundary HPADJ08 PR drift")
    req(audit["review_id"] == AUTHORITATIVE_HPADJ08_REVIEW_ID, "boundary authoritative review drift")
    req(audit["audited_exact_head"] == HPADJ08_AUDITED_HEAD, "boundary HPADJ08 head drift")
    req(audit["audit_result"] == "PASS", "boundary HPADJ08 audit result drift")

    b = boundary["candidate_bound"]
    rbg = result["block_geometry"]
    rcb = result["candidate_bound"]
    req(b["full178_rows"] == rbg["full178_rows"] == 178, "FULL178 row-count drift")
    req(b["hpadj08_removed_terminals"] == rbg["hpadj08_removed_terminals"], "removed-terminal count drift")
    req(b["pre_hpadj08_x4_complete_blocks"] == rbg["pre_hpadj08_x4_complete_blocks"], "pre-block count drift")
    req(b["row_stratified_removed_complete_block_lower_bound"] == rbg["row_stratified_removed_complete_block_lower_bound"], "removed-block lower-bound drift")
    req(b["hpadj08_survivor_complete_block_upper_bound"] == rbg["hpadj08_survivor_complete_block_upper_bound"], "survivor-block upper-bound drift")
    req(b["hpadj08_survivor_envelope_terminals"] == rcb["hpadj08_survivor_envelope_terminals"], "survivor-envelope drift")
    req(b["row_stratified_refined_survivor_upper_bound"] == rcb["row_stratified_refined_survivor_upper_bound"], "row-stratified upper-bound drift")
    req(b["improvement_vs_hpadj11_upper_bound"] == rcb["improvement_vs_hpadj11_upper_bound"], "HPADJ11 improvement drift")
    req(b["improvement_vs_td01_upper_bound"] == rcb["improvement_vs_td01_upper_bound"], "TD01 improvement drift")

    survivor_blocks = b["pre_hpadj08_x4_complete_blocks"] - b["row_stratified_removed_complete_block_lower_bound"]
    req(survivor_blocks == b["hpadj08_survivor_complete_block_upper_bound"], "survivor-block arithmetic drift")
    refined_upper = (b["hpadj08_survivor_envelope_terminals"] + survivor_blocks) // 2
    req(refined_upper == b["row_stratified_refined_survivor_upper_bound"], "parity upper-bound arithmetic drift")
    req(b["hpadj11_previous_upper_bound"] - refined_upper == b["improvement_vs_hpadj11_upper_bound"], "HPADJ11 improvement arithmetic drift")
    req(b["td01_previous_upper_bound"] - refined_upper == b["improvement_vs_td01_upper_bound"], "TD01 improvement arithmetic drift")

    req(boundary["semantics"]["same_picard64_character_refinement_not_additive_subtraction"] is True, "same-character refinement firewall drift")
    req(boundary["semantics"]["main_consumption_performed"] is False, "producer performed MAIN consumption")
    req(boundary["semantics"]["main_handoff_built"] is False, "pre-audit MAIN handoff unexpectedly built")
    req(boundary["semantics"]["hostile_audit_required_before_main_handoff_or_consumption"] is True, "hostile-audit gate drift")
    req(all(v is False for v in boundary["firewalls"].values()), "credit/merge firewall opened")

    print(json.dumps({
        "status": "PASS_HPADJ12_REPAIRED_AUDIT_BOUNDARY",
        "boundary_canonical": LOCKS["boundary_canonical"],
        "authoritative_hpadj08_review_id": AUTHORITATIVE_HPADJ08_REVIEW_ID,
        "deprecated_embedded_review_id": DEPRECATED_EMBEDDED_REVIEW_ID,
        "row_stratified_refined_survivor_upper_bound": refined_upper,
        "improvement_vs_hpadj11_upper_bound": b["improvement_vs_hpadj11_upper_bound"],
        "main_credit": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
