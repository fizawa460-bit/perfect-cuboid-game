#!/usr/bin/env python3
from __future__ import annotations

import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTROLLER = ROOT / "stages/stage32/controller.json"
CERT_PATH = "stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum.json"
NOTE_PATH = "stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum-source-note.md"
AUDITED_MATH_VERIFIER = "stages/stage32/residual-32-01-production/certify_stage32_post1518_o210_q602_residue73_trace_spectrum.py"
PROMOTION_VERIFIER = "stages/stage32/residual-32-01-production/certify_stage32_post1518_o210_q602_trace_spectrum_promotion.py"
SUCCESSOR_VERIFIER = "stages/stage32/residual-32-01-production/certify_stage32_post1518_o210_q602_18_diagonal_retained_geometry_test.py"
WORKFLOW = ".github/workflows/stage32-post1518-o210-q602-residue73-trace-spectrum.yml"
SUCCESSOR_WORKFLOW = ".github/workflows/stage32-post1518-o210-q602-18-diagonal-retained-geometry-test.yml"
EXPECTED_CANONICAL = "4925170377af7c77a97d36e562cdabd58241030f22a9644f1fa2a8ee627002c3"
AUDITED_HEAD = "14735cd3948ab1c560550becfa843b7ac7a4b8ba"
AUDIT_REVIEW = 5108941088
AUDITED_RUN = 33833603582
AUDITED_JOB = 100901507149
AUDITED_MATH_VERIFIER_BLOB = "d2417b610aec657df00eacaa524c467ef5a4711c"
AUDITED_WORKFLOW_BLOB = "6d4452f145c811fecc8d5a8352b1da67e6c368cf"
CERT_BLOB = "9d65d760de99cfb2985956e0c845be3b2b601c87"
NOTE_BLOB = "41f0b99bd097fbeb30a215145e5aee84c64aced8"
EXPECTED_VALUES = [118,126,134,142,150,158,166,174,182,190,198,206,214,222,230,238,246,254]


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
    assert ctl["stage"] == 32 and ctl["stage32_closed"] is False

    cert_path = ROOT / CERT_PATH
    note_path = ROOT / NOTE_PATH
    math_verifier_path = ROOT / AUDITED_MATH_VERIFIER
    cert = json.loads(cert_path.read_text())
    assert blob_sha1(cert_path) == CERT_BLOB
    assert blob_sha1(note_path) == NOTE_BLOB
    assert blob_sha1(math_verifier_path) == AUDITED_MATH_VERIFIER_BLOB
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert cert["exact_spectrum"]["residue73_q602_vector_count"] == 13674752
    assert cert["exact_spectrum"]["diagonal_intersection_values"] == EXPECTED_VALUES
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
    assert bundle["necessary_diagonal_values"] == EXPECTED_VALUES
    assert bundle["Q602_excluded"] is False and bundle["O210_excluded"] is False

    fw = ctl["firewalls"]
    assert fw["O210_closed"] is False and fw["Q602_excluded"] is False
    assert fw["geometric_realization_of_lattice_points_inferred"] is False
    assert fw["receiver_credit"] is False and fw["route_credit"] is False
    assert fw["theorem_credit"] is False and fw["endpoint_credit"] is False
    assert fw["perfect_cuboid_existence_claim"] is False and fw["perfect_cuboid_nonexistence_claim"] is False
    assert ctl["math_scope"]["fixed_z_O212_through_O266_qprime4"] == "BLOCKED_BEHIND_O210"
    release = ctl["post1518_merge_release"]
    assert release["authorized_by_user"] is True and release["hostile_reaudit_review_id"] == AUDIT_REVIEW
    assert release["Q602_excluded"] is False and release["O210_excluded"] is False and release["O212_plus_authorized"] is False

    schema = ctl["schema"]
    if schema == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V245_POST1518_Q602_TRACE_SPECTRUM_AUDITED_MERGE_RELEASED":
        assert ctl["advance_allowed"] is True and ctl["merge_allowed"] is True and ctl["checkpoint_merge_ready"] is True
        assert ctl["active_pr"] == {"number":1518,"branch":"stage32-post1505-trace-parity-bridge","automatic_merge_authorized":True}
        req = ctl["required_lightweight_verifier"]
        assert req["path"] == PROMOTION_VERIFIER and req["workflow"] == WORKFLOW
        assert req["role"] == "AUDITED_PROMOTION_SUCCESSOR_SAFE_REPLAY"
        assert ctl["audit_required_before_promotion"] is False
        assert ctl["current_item"] == "O210_Q602_AUDITED_18_VALUE_DIAGONAL_SPECTRUM_RETAINED_GEOMETRY_TEST"
    elif schema == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V246_POST1520_Q602_RETAINED_GEOMETRY_18_TO_18_PROVISIONAL":
        assert ctl["advance_allowed"] is False and ctl["merge_allowed"] is False and ctl["checkpoint_merge_ready"] is False
        assert ctl["active_pr"] == {"number":1520,"branch":"stage32-post1518-retained-geometry-18-bounded-test","automatic_merge_authorized":False}
        assert ctl["current_item"] == "O210_Q602_PROVISIONAL_RETAINED_GEOMETRY_18_TO_18_HOSTILE_AUDIT"
        successor = ctl["post1520_q602_18_diagonal_retained_geometry_test_provisional"]
        assert successor["pruning"] == "18 -> 18" and successor["surviving_diagonal_values"] == EXPECTED_VALUES
        assert ctl["audit_required_before_promotion"] is True
    elif schema == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V247_POST1520_Q602_RETAINED_GEOMETRY_18_TO_18_AUDITED":
        assert ctl["advance_allowed"] is True and ctl["merge_allowed"] is True and ctl["checkpoint_merge_ready"] is True
        assert ctl["active_pr"] == {"number":1521,"branch":"stage32-post1520-audited-promotion","automatic_merge_authorized":False}
        assert ctl["current_item"] == "O210_Q602_NEW_SCALAR_COUPLING_ROUTE_SELECTION"
        successor = ctl["post1520_q602_18_diagonal_retained_geometry_test_provisional"]
        assert successor["status"] == "AUDITED_EXACT_BOUNDED_NEGATIVE_AFTER_HOSTILE_AUDIT"
        assert successor["pruning"] == "18 -> 18" and successor["surviving_diagonal_values"] == EXPECTED_VALUES
        audit1520 = ctl["post1520_hostile_audit_pass"]
        assert audit1520["review_id"] == 5109035402
        assert audit1520["audited_exact_head"] == "316d509464a1c146824bd0717f54b4441e14dc59"
        assert audit1520["verdict"] == "PASS"
        assert ctl["audit_required_before_promotion"] is False
    else:
        raise AssertionError(f"unsupported successor controller: {schema}")

    print("PASS: Stage32 hostile-audited #1518 18-value spectrum remains immutable and valid under current successor authority; Q602/O210 open, O212+ blocked.")

if __name__ == "__main__":
    main()
