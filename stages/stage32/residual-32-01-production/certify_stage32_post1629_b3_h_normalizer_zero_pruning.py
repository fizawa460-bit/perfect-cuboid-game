#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT_FILE = HERE / "post1629-b3-h-normalizer-zero-pruning.json"
DIAG_FILE = HERE / "diagnose_stage32_hperp_b3_h_normalizer_action.py"


def canonical_sha(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if claimed != calc:
        raise SystemExit(f"certificate canonical mismatch: {claimed} != {calc}")
    return calc


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(cond: bool, message: str) -> None:
    if not cond:
        raise SystemExit(message)


def main() -> None:
    cert = json.loads(CERT_FILE.read_text())
    canonical_sha(cert)
    require(cert["schema"] == "STAGE32_POST1629_B3_H_NORMALIZER_ZERO_PRUNING_V1", "schema moved")
    require(cert["status"] == "PASS_EXACT_BOUNDED_NEGATIVE_PENDING_HOSTILE_AUDIT", "status moved")
    require(cert["fixed_target"]["surviving_residues_decimal"] == [73, 97, 235], "fixed survivors moved")

    lock = cert["source_locks"]["diagnostic"]
    require(git_blob_sha1(DIAG_FILE) == lock["blob_sha1"], "H-normalizer diagnostic blob moved")
    diag = json.loads(subprocess.check_output([sys.executable, str(DIAG_FILE)], text=True))
    require(diag["schema"] == lock["schema"], "diagnostic schema moved")
    require(diag["source_lock"]["post1550_canonical_sha256"] == cert["source_locks"]["post1550_canonical_sha256"], "post1550 lock moved")
    require(diag["source_lock"]["retained_H_asset_canonical_sha256"] == cert["source_locks"]["retained_H_asset_canonical_sha256"], "H asset lock moved")
    require(diag["source_lock"]["post1588_canonical_sha256"] == cert["source_locks"]["post1588_canonical_sha256"], "post1588 lock moved")
    require(diag["source_lock"]["retained_all140_coordinates_sha256"] == cert["source_locks"]["all140_retained_coordinates_sha256"], "retained coordinates lock moved")

    f = diag["finite_filter"]
    frozen = cert["finite_filter"]
    actual = {
        "retained_stoll_group_order": f["retained_stoll_group_order"],
        "order3_element_count": f["order3_element_count"],
        "H_normalizing_order3_count": f["H_normalizing_order3_count"],
        "H_cycling_order3_candidate_count": f["H_cycling_order3_candidate_count"],
        "label1_image_cardinality": f["label1_image_cardinality"],
        "fix_label1_count": f["fix_label1_count"],
        "move_label1_count": f["move_label1_count"],
        "fix_label1_mod_exceptional_span_count": f["fix_label1_mod_exceptional_span_count"],
        "move_label1_mod_exceptional_span_count": f["move_label1_mod_exceptional_span_count"],
        "separator_same_count": f["separator_same_count"],
        "separator_flip_count": f["separator_flip_count"],
    }
    require(actual == frozen, f"finite H-normalizer filter moved: {actual} != {frozen}")
    require(frozen["H_cycling_order3_candidate_count"] == frozen["order3_element_count"] == 128, "zero-pruning identity moved")
    require(frozen["H_normalizing_order3_count"] == 128, "H-normalizer count moved")
    require(frozen["label1_image_cardinality"] == 28, "label1 image ambiguity moved")
    require(0 < frozen["fix_label1_count"] < 128, "label1 fixed/moved ambiguity disappeared")
    require(0 < frozen["fix_label1_mod_exceptional_span_count"] < 128, "quotient ambiguity disappeared")
    require(0 < frozen["separator_same_count"] < 128, "separator ambiguity disappeared")

    boundary = diag["decision_boundary"]
    neg = cert["exact_negative_consequence"]
    require(boundary["exact_principal_b3_member_identified"] == neg["exact_principal_b3_member_identified"] is False, "member identification boundary moved")
    require(boundary["exact_principal_b3_label1_image_identified"] == neg["exact_principal_b3_label1_image_identified"] is False, "label1 identification boundary moved")
    require(boundary["principal_b3_label1_noninvariance_forced"] == neg["principal_b3_label1_noninvariance_forced"] is False, "label1 noninvariance boundary moved")
    require(boundary["principal_b3_quotient_noninvariance_forced"] == neg["principal_b3_quotient_noninvariance_forced"] is False, "quotient noninvariance boundary moved")
    require(boundary["principal_b3_separator_flip_forced"] == neg["principal_b3_separator_flip_forced"] is False, "separator boundary moved")

    decision = cert["decision"]
    require(decision["result"] == "PASS_EXACT_H_NORMALIZER_ZERO_PRUNING", "decision result moved")
    require(decision["controller_change_authorized"] is False, "controller promotion unexpectedly authorized")
    require(decision["residue_specific_commutator_obtained"] is False, "unexpected commutator credit")
    require(decision["q602_residue_elimination_credit"] is False, "unexpected Q602 elimination credit")
    require(decision["Q602_excluded"] is False and decision["O210_excluded"] is False, "unexpected endpoint credit")
    require(decision["surviving_residues_decimal"] == [73, 97, 235], "certificate survivors moved")

    print(json.dumps({
        "schema": "STAGE32_POST1629_B3_H_NORMALIZER_ZERO_PRUNING_VERIFY_V1",
        "status": "PASS",
        "order3_element_count": frozen["order3_element_count"],
        "H_normalizing_order3_count": frozen["H_normalizing_order3_count"],
        "H_cycling_order3_candidate_count": frozen["H_cycling_order3_candidate_count"],
        "label1_image_cardinality": frozen["label1_image_cardinality"],
        "surviving_residues_decimal": decision["surviving_residues_decimal"],
        "controller_change_authorized": False,
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
