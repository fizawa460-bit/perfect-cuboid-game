#!/usr/bin/env python3
from __future__ import annotations

import argparse
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
    "boundary_blob": "95b8e71647d169f23d3933d8cc95f0015fec503c",
    "boundary_canonical": "7bba444fd43a65000f819c8d08caf12832e93f37a1465026fab80e6b15770321",
    "repair_blob": "36b697a5dfd1cadc9dcc93a13f56c5b29e2a16f3",
    "repair_canonical": "3562c86ddbef03b92a694b23587ba9a2fdb7615beee663af120b496d15f60a4b",
    "result_blob": "749c6e38b79cc1e6783635fbac43acccb004e1ad",
    "result_canonical": "2b710888bd332e4c402f086ae0e5177acfd96a003a6bb30991b2f67e131b2e74",
    "certificate_blob": "29ef2acf15e6649f5db90935f53b65a9388f7db4",
    "certificate_canonical": "9dc6d1976b171dc1b71df1e767200a62cba9683ebc2d722819b92f8cd1e617c3",
    "producer_blob": "8d022e45ee65e30cbaee19e4cc25855edbe0d468",
    "historical_full178_result_blob": "f9a01c3e673dc630a3446ac4560c72c4f76db812",
    "historical_full178_result_canonical": "625e289a1a9f086b5e02f247665a7f9ac4b7fe72eaacd3011fe73a0e96041953",
}

AUTHORITATIVE_HPADJ08_REVIEW_ID = 5208789388
DEPRECATED_EMBEDDED_REVIEW_ID = 5205760920
DEPRECATED_EMBEDDED_FULL178_BLOB = "f9a9ebf7ccca2baa9a9fe3a933a42aee8aa51cb3"
DEPRECATED_EMBEDDED_FULL178_CANONICAL = "d7a3af4b10466bffcd11f8559823861f50f1b30e266ba391c3718b1f688ef8b3"
HPADJ08_AUDITED_HEAD = "36eab50192cf80ec5ed48aba40f4a56076759fea"
HPADJ08_SOURCE_HEAD = "b11a9820af4a02148112a6ae235bc3a51d134ef2"
HPADJ08_SOURCE_RUN = 34935380596
HPADJ08_REMOVED_TERMINALS = 40886299509963924857401


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--hpadj08-root", required=True)
    args = ap.parse_args()

    # Fail closed on the repair and audit-boundary identities before consuming
    # the retained row-stratified result.
    repair = load_locked_json(REPAIR, LOCKS["repair_blob"], LOCKS["repair_canonical"], "HPADJ12 provenance repair")
    boundary = load_locked_json(BOUNDARY, LOCKS["boundary_blob"], LOCKS["boundary_canonical"], "HPADJ12 audit boundary")
    result = load_locked_json(RESULT, LOCKS["result_blob"], LOCKS["result_canonical"], "HPADJ12 row-stratified result")
    cert = load_locked_json(CERT, LOCKS["certificate_blob"], LOCKS["certificate_canonical"], "HPADJ08 row certificate")
    req(PRODUCER.is_file() and git_blob(PRODUCER) == LOCKS["producer_blob"], "HPADJ12 producer blob drift")

    historical_root = Path(args.hpadj08_root).resolve()
    historical_result_path = historical_root / "stages/stage32-ex5/hpadj-08_ex5/FULL178-RESULT.json"
    historical = load_locked_json(
        historical_result_path,
        LOCKS["historical_full178_result_blob"],
        LOCKS["historical_full178_result_canonical"],
        "hostile-audited HPADJ08 FULL178 result",
    )
    req(historical["source_exact_head"] == HPADJ08_SOURCE_HEAD, "historical HPADJ08 source head drift")
    req(historical["source_run_id"] == HPADJ08_SOURCE_RUN, "historical HPADJ08 source run drift")
    req(historical["coverage"]["rows"] == 178, "historical HPADJ08 row coverage drift")
    req(historical["coverage"]["all_shards_success"] is True, "historical HPADJ08 shard-success drift")
    req(historical["stored_exact_square_candidate_rejected_terminals"] == HPADJ08_REMOVED_TERMINALS, "historical HPADJ08 rejected-total drift")

    req(repair["authoritative_audit"]["pr"] == 1812, "HPADJ08 PR drift")
    req(repair["authoritative_audit"]["review_id"] == AUTHORITATIVE_HPADJ08_REVIEW_ID, "HPADJ08 authoritative review drift")
    req(repair["authoritative_audit"]["audited_exact_head"] == HPADJ08_AUDITED_HEAD, "HPADJ08 audited-head drift")
    req(repair["authoritative_audit"]["audit_result"] == "PASS", "HPADJ08 audit result drift")

    auth_result = repair["authoritative_full178_result"]
    req(auth_result["blob_sha1"] == LOCKS["historical_full178_result_blob"], "repair authoritative FULL178 blob drift")
    req(auth_result["canonical_sha256"] == LOCKS["historical_full178_result_canonical"], "repair authoritative FULL178 canonical drift")
    req(auth_result["source_exact_head"] == HPADJ08_SOURCE_HEAD, "repair HPADJ08 source-head drift")
    req(auth_result["source_run_id"] == HPADJ08_SOURCE_RUN, "repair HPADJ08 source-run drift")
    req(auth_result["stored_exact_square_candidate_rejected_terminals"] == HPADJ08_REMOVED_TERMINALS, "repair HPADJ08 rejected-total drift")

    cert_info = repair["certificate"]
    req(cert_info["embedded_hpadj08_hostile_audit_review_id"] == DEPRECATED_EMBEDDED_REVIEW_ID, "deprecated embedded review-id drift")
    req(cert_info["embedded_hpadj08_full178_result_blob_sha1"] == DEPRECATED_EMBEDDED_FULL178_BLOB, "deprecated embedded FULL178 blob drift")
    req(cert_info["embedded_hpadj08_full178_result_canonical_sha256"] == DEPRECATED_EMBEDDED_FULL178_CANONICAL, "deprecated embedded FULL178 canonical drift")
    req(repair["semantics"]["embedded_review_id_is_deprecated_typo"] is True, "review-id typo not explicitly deprecated")
    req(repair["semantics"]["embedded_full178_result_identity_is_deprecated_typo"] is True, "FULL178 identity typo not explicitly deprecated")
    req(repair["semantics"]["repair_changes_mathematical_count"] is False, "provenance repair changed mathematical count")

    # The original compressed row certificate is retained byte-for-byte. Its
    # two stale provenance fields are accepted only because the locked repair
    # and the independently checked historical result supersede them.
    req(cert["source"]["hpadj08_hostile_audit_review_id"] == DEPRECATED_EMBEDDED_REVIEW_ID, "certificate embedded review-id drift")
    req(cert["source"]["hpadj08_full178_result_blob_sha1"] == DEPRECATED_EMBEDDED_FULL178_BLOB, "certificate embedded FULL178 blob drift")
    req(cert["source"]["hpadj08_full178_result_canonical_sha256"] == DEPRECATED_EMBEDDED_FULL178_CANONICAL, "certificate embedded FULL178 canonical drift")
    req(cert["aggregate"]["stored_exact_square_candidate_rejected_terminals"] == HPADJ08_REMOVED_TERMINALS, "certificate rejected-total drift")

    # The pre-repair derived result is also intentionally retained byte-exact;
    # its stale review id is superseded by this final repaired boundary.
    req(result["sources"]["hpadj08_hostile_audit_review_id"] == DEPRECATED_EMBEDDED_REVIEW_ID, "expected pre-repair result provenance drift")
    req(result["sources"]["hpadj08_audited_exact_head"] == HPADJ08_AUDITED_HEAD, "result HPADJ08 head drift")

    locks = boundary["source_locks"]
    req(locks["provenance_repair_blob_sha1"] == LOCKS["repair_blob"], "boundary repair blob lock drift")
    req(locks["provenance_repair_canonical_sha256"] == LOCKS["repair_canonical"], "boundary repair canonical lock drift")
    req(locks["row_reject_certificate_blob_sha1"] == LOCKS["certificate_blob"], "boundary certificate blob lock drift")
    req(locks["row_reject_certificate_canonical_sha256"] == LOCKS["certificate_canonical"], "boundary certificate canonical lock drift")
    req(locks["row_stratified_producer_blob_sha1"] == LOCKS["producer_blob"], "boundary producer blob lock drift")
    req(locks["row_stratified_result_blob_sha1"] == LOCKS["result_blob"], "boundary result blob lock drift")
    req(locks["row_stratified_result_canonical_sha256"] == LOCKS["result_canonical"], "boundary result canonical lock drift")

    audit = boundary["authoritative_hpadj08_audit"]
    req(audit["pr"] == 1812, "boundary HPADJ08 PR drift")
    req(audit["review_id"] == AUTHORITATIVE_HPADJ08_REVIEW_ID, "boundary authoritative review drift")
    req(audit["audited_exact_head"] == HPADJ08_AUDITED_HEAD, "boundary HPADJ08 head drift")
    req(audit["audit_result"] == "PASS", "boundary HPADJ08 audit result drift")
    boundary_result = boundary["authoritative_hpadj08_full178_result"]
    req(boundary_result["blob_sha1"] == LOCKS["historical_full178_result_blob"], "boundary authoritative FULL178 blob drift")
    req(boundary_result["canonical_sha256"] == LOCKS["historical_full178_result_canonical"], "boundary authoritative FULL178 canonical drift")
    req(boundary_result["source_exact_head"] == HPADJ08_SOURCE_HEAD, "boundary source head drift")
    req(boundary_result["source_run_id"] == HPADJ08_SOURCE_RUN, "boundary source run drift")

    b = boundary["candidate_bound"]
    rbg = result["block_geometry"]
    rcb = result["candidate_bound"]
    req(b["full178_rows"] == rbg["full178_rows"] == 178, "FULL178 row-count drift")
    req(b["hpadj08_removed_terminals"] == rbg["hpadj08_removed_terminals"] == HPADJ08_REMOVED_TERMINALS, "removed-terminal count drift")
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
        "authoritative_hpadj08_full178_blob": LOCKS["historical_full178_result_blob"],
        "authoritative_hpadj08_full178_canonical": LOCKS["historical_full178_result_canonical"],
        "deprecated_embedded_review_id": DEPRECATED_EMBEDDED_REVIEW_ID,
        "row_stratified_refined_survivor_upper_bound": refined_upper,
        "improvement_vs_hpadj11_upper_bound": b["improvement_vs_hpadj11_upper_bound"],
        "main_credit": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
