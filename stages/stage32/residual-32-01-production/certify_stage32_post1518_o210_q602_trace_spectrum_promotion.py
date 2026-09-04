#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTROLLER = ROOT / "stages/stage32/controller.json"
CERT_PATH = "stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum.json"
NOTE_PATH = "stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum-source-note.md"
AUDITED_MATH_VERIFIER = "stages/stage32/residual-32-01-production/certify_stage32_post1518_o210_q602_residue73_trace_spectrum.py"
PROMOTION_VERIFIER = "stages/stage32/residual-32-01-production/certify_stage32_post1518_o210_q602_trace_spectrum_promotion.py"
WORKFLOW = ".github/workflows/stage32-post1518-o210-q602-residue73-trace-spectrum.yml"
EXPECTED_CANONICAL = "4925170377af7c77a97d36e562cdabd58241030f22a9644f1fa2a8ee627002c3"
AUDITED_HEAD = "14735cd3948ab1c560550becfa843b7ac7a4b8ba"
AUDIT_REVIEW = 5108941088
AUDITED_RUN = 33833603582
AUDITED_JOB = 100901507149
AUDITED_MATH_VERIFIER_BLOB = "d2417b610aec657df00eacaa524c467ef5a4711c"
AUDITED_WORKFLOW_BLOB = "6d4452f145c811fecc8d5a8352b1da67e6c368cf"
CERT_BLOB = "9d65d760de99cfb2985956e0c845be3b2b601c87"
NOTE_BLOB = "41f0b99bd097fbeb30a215145e5aee84c64aced8"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    ctl = json.loads(CONTROLLER.read_text())
    assert ctl["schema"] == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V245_POST1518_Q602_TRACE_SPECTRUM_AUDITED_MERGE_RELEASED"
    assert ctl["stage"] == 32 and ctl["stage32_closed"] is False
    assert ctl["status"] == "STAGE32_O210_Q602_AUDITED_RESIDUE73_18_VALUE_DIAGONAL_SPECTRUM_MERGE_RELEASED"
    assert ctl["advance_allowed"] is True
    assert ctl["merge_allowed"] is True
    assert ctl["checkpoint_merge_ready"] is True
    assert ctl["active_pr"] == {"number":1518,"branch":"stage32-post1505-trace-parity-bridge","automatic_merge_authorized":True}

    cert_path = ROOT / CERT_PATH
    note_path = ROOT / NOTE_PATH
    math_verifier_path = ROOT / AUDITED_MATH_VERIFIER
    cert = json.loads(cert_path.read_text())
    assert blob_sha1(cert_path) == CERT_BLOB
    assert blob_sha1(note_path) == NOTE_BLOB
    assert blob_sha1(math_verifier_path) == AUDITED_MATH_VERIFIER_BLOB
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert cert["exact_spectrum"]["residue73_q602_vector_count"] == 13674752
    assert cert["exact_spectrum"]["diagonal_intersection_values"] == [118,126,134,142,150,158,166,174,182,190,198,206,214,222,230,238,246,254]
    assert cert["decision"]["Q602_excluded"] is False and cert["decision"]["O210_excluded"] is False

    audit = ctl["post1518_hostile_reaudit_pass"]
    assert audit["review_id"] == AUDIT_REVIEW
    assert audit["audited_exact_head"] == AUDITED_HEAD
    assert audit["exact_head_ci"] == {"run_id":AUDITED_RUN,"job_id":AUDITED_JOB,"result":"SUCCESS"}
    assert audit["verdict"] == "PASS"
    assert audit["authority_promotion"] == "AUDITED_NECESSARY_18_VALUE_TRACE_AND_DIAGONAL_SPECTRUM_ONLY"
    assert audit["audited_math_verifier_blob_sha1"] == AUDITED_MATH_VERIFIER_BLOB
    assert audit["audited_workflow_blob_sha1"] == AUDITED_WORKFLOW_BLOB

    bundle = ctl["post1518_q602_residue73_trace_spectrum"]
    assert bundle["status"] == "AUDITED_EXACT_AFTER_HOSTILE_REAUDIT"
    assert bundle["certificate_path"] == CERT_PATH and bundle["certificate_blob_sha1"] == CERT_BLOB
    assert bundle["source_note_path"] == NOTE_PATH and bundle["source_note_blob_sha1"] == NOTE_BLOB
    assert bundle["canonical_sha256"] == EXPECTED_CANONICAL
    assert bundle["audited_math_verifier_path"] == AUDITED_MATH_VERIFIER
    assert bundle["audited_math_verifier_blob_sha1"] == AUDITED_MATH_VERIFIER_BLOB
    assert bundle["necessary_diagonal_values"] == cert["exact_spectrum"]["diagonal_intersection_values"]
    assert bundle["Q602_excluded"] is False and bundle["O210_excluded"] is False

    req = ctl["required_lightweight_verifier"]
    assert req["path"] == PROMOTION_VERIFIER
    assert req["workflow"] == WORKFLOW
    assert req["role"] == "AUDITED_PROMOTION_SUCCESSOR_SAFE_REPLAY"
    assert req["verifier_blob_sha1"] == blob_sha1(ROOT / PROMOTION_VERIFIER)
    assert req["workflow_blob_sha1"] == blob_sha1(ROOT / WORKFLOW)
    assert ctl["audit_required_before_promotion"] is False

    assert ctl["current_item"] == "O210_Q602_AUDITED_18_VALUE_DIAGONAL_SPECTRUM_RETAINED_GEOMETRY_TEST"
    leaf = ctl["current_leaf"]
    assert leaf["status"] == "AUDITED_EXACT_NECESSARY_18_VALUE_DIAGONAL_SPECTRUM"
    assert leaf["O212_and_later_blocked"] is True
    assert "18" in leaf["target"] and "retained common-cover" in leaf["target"]

    scope = ctl["math_scope"]
    assert scope["fixed_z_O210_q4_exact_v6_carrier"] == "OPEN_WITH_AUDITED_Q602_CANONICAL_RESIDUE73_18_VALUE_DIAGONAL_SPECTRUM"
    assert scope["fixed_z_O212_through_O266_qprime4"] == "BLOCKED_BEHIND_O210"
    ops = ctl["operations"]
    assert ops["heavy_compute_authorized"] is False and ops["full178_scaleout_authorized"] is False
    assert ops["retained_asset_research_authorized"] is True

    fw = ctl["firewalls"]
    assert fw["O210_closed"] is False and fw["Q602_excluded"] is False
    assert fw["geometric_realization_of_lattice_points_inferred"] is False
    assert fw["receiver_credit"] is False and fw["route_credit"] is False
    assert fw["theorem_credit"] is False and fw["endpoint_credit"] is False
    assert fw["perfect_cuboid_existence_claim"] is False and fw["perfect_cuboid_nonexistence_claim"] is False

    release = ctl["post1518_merge_release"]
    assert release["authorized_by_user"] is True
    assert release["hostile_reaudit_review_id"] == AUDIT_REVIEW
    assert release["mathematical_scope_unchanged"] is True
    assert release["Q602_excluded"] is False and release["O210_excluded"] is False
    assert release["O212_plus_authorized"] is False
    print("PASS: Stage32 #1518 hostile-audited 18-value trace/diagonal spectrum is promoted for merge; O210/Q602 remain open and O212+ blocked.")


if __name__ == "__main__":
    main()
