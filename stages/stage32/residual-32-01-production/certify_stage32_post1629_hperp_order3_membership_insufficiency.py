#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT_FILE = HERE / "post1629-hperp-order3-membership-insufficiency.json"
DIAGNOSTIC_FILE = HERE / "diagnose_stage32_hperp_order3_label1_action.py"


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

    require(cert["schema"] == "STAGE32_POST1629_HPERP_ORDER3_MEMBERSHIP_INSUFFICIENCY_V1", "schema moved")
    require(cert["status"] == "PASS_EXACT_BOUNDED_NEGATIVE_PENDING_HOSTILE_AUDIT", "status moved")
    require(cert["fixed_target"]["surviving_residues_decimal"] == [73, 97, 235], "fixed survivors moved")

    lock = cert["source_locks"]["diagnostic"]
    require(lock["path"] == "stages/stage32/residual-32-01-production/diagnose_stage32_hperp_order3_label1_action.py", "diagnostic path moved")
    actual_blob = git_blob_sha1(DIAGNOSTIC_FILE)
    require(actual_blob == lock["blob_sha1"], f"diagnostic blob moved: {actual_blob}")

    raw = subprocess.check_output([sys.executable, str(DIAGNOSTIC_FILE)], text=True)
    diag = json.loads(raw)

    require(diag["schema"] == lock["schema"], "diagnostic schema moved")
    require(diag["source_lock"]["post1588_canonical_sha256"] == cert["source_locks"]["post1588_canonical_sha256"], "post1588 lock moved")
    require(diag["source_lock"]["post1563_canonical_sha256"] == cert["source_locks"]["post1563_canonical_sha256"], "post1563 lock moved")
    require(diag["source_lock"]["all140_retained_coordinates_sha256"] == cert["source_locks"]["all140_retained_coordinates_sha256"], "retained coordinates lock moved")

    inp = diag["principal_b3_retained_input"]
    expected_inp = cert["principal_b3_retained_input"]
    for key in ("membership_in_full_stoll_group", "outside_H", "order", "explicit_stoll_word_source_locked", "candidate_superset"):
        require(inp[key] == expected_inp[key], f"principal b3 input moved: {key}")

    sweep = diag["order3_sweep"]
    frozen = cert["finite_sweep"]
    actual = {
        "retained_stoll_group_order": diag["retained_stoll_group_order"],
        "retained_stoll_generator_count": diag["retained_stoll_generator_count"],
        "order3_element_count": sweep["order3_element_count"],
        "label1_image_cardinality": len(sweep["label1_image_set"]),
        "fix_label1_count": sweep["fix_label1_count"],
        "move_label1_count": sweep["move_label1_count"],
        "fix_label1_mod_exceptional_span_count": sweep["fix_label1_mod_exceptional_span_count"],
        "move_label1_mod_exceptional_span_count": sweep["move_label1_mod_exceptional_span_count"],
        "separator_same_count": sweep["separator_same_count"],
        "separator_flip_count": sweep["separator_flip_count"],
    }
    require(actual == frozen, f"finite sweep moved: {actual} != {frozen}")

    # The bounded negative conclusion requires genuine ambiguity, not merely a search miss.
    require(frozen["label1_image_cardinality"] > 1, "label1 action unexpectedly unique")
    require(0 < frozen["fix_label1_count"] < frozen["order3_element_count"], "label1 fixed/moved ambiguity disappeared")
    require(0 < frozen["fix_label1_mod_exceptional_span_count"] < frozen["order3_element_count"], "quotient ambiguity disappeared")
    require(0 < frozen["separator_same_count"] < frozen["order3_element_count"], "separator ambiguity disappeared")

    boundary = diag["decision_boundary"]
    frozen_boundary = cert["exact_negative_consequence"]
    require(boundary["exact_principal_b3_label1_image_identified"] == frozen_boundary["exact_principal_b3_label1_image_identified"], "label1 identification boundary moved")
    require(boundary["principal_b3_label1_noninvariance_forced_by_membership_order"] == frozen_boundary["principal_b3_label1_noninvariance_forced_by_membership_order"], "label1 noninvariance boundary moved")
    require(boundary["principal_b3_quotient_noninvariance_forced_by_membership_order"] == frozen_boundary["principal_b3_quotient_noninvariance_forced_by_membership_order"], "quotient noninvariance boundary moved")
    require(boundary["principal_b3_separator_flip_forced_by_membership_order"] == frozen_boundary["principal_b3_separator_flip_forced_by_membership_order"], "separator boundary moved")
    require(boundary["residue_specific_commutator_obtained"] is False, "unexpected residue commutator credit")
    require(boundary["q602_residue_elimination_credit"] is False, "unexpected Q602 elimination credit")
    require(boundary["Q602_excluded"] is False and boundary["O210_excluded"] is False, "unexpected endpoint exclusion credit")
    require(boundary["surviving_residues_decimal"] == [73, 97, 235], "diagnostic survivors moved")

    decision = cert["decision"]
    require(decision["result"] == "PASS_EXACT_ORDER3_MEMBERSHIP_INSUFFICIENCY", "decision result moved")
    require(decision["controller_change_authorized"] is False, "controller promotion unexpectedly authorized")
    require(decision["surviving_residues_decimal"] == [73, 97, 235], "certificate survivors moved")

    print(json.dumps({
        "schema": "STAGE32_POST1629_HPERP_ORDER3_MEMBERSHIP_INSUFFICIENCY_VERIFY_V1",
        "status": "PASS",
        "order3_element_count": frozen["order3_element_count"],
        "label1_image_cardinality": frozen["label1_image_cardinality"],
        "fix_label1_count": frozen["fix_label1_count"],
        "fix_label1_mod_exceptional_span_count": frozen["fix_label1_mod_exceptional_span_count"],
        "separator_same_count": frozen["separator_same_count"],
        "surviving_residues_decimal": decision["surviving_residues_decimal"],
        "controller_change_authorized": False,
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
