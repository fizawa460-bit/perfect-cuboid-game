#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT_PATH = "stages/stage32/residual-32-01-production/post1518-o210-q602-18-diagonal-retained-geometry-test.json"
VERIFIER_PATH = "stages/stage32/residual-32-01-production/certify_stage32_post1518_o210_q602_18_diagonal_retained_geometry_test.py"
WORKFLOW_PATH = ".github/workflows/stage32-post1518-o210-q602-18-diagonal-retained-geometry-test.yml"
EXPECTED_CANONICAL = "d7de2bdb834cf6d231261e414962547fe1d65e3d9c7c9613caa6fe5ab64dd275"
EXPECTED_VALUES = [118,126,134,142,150,158,166,174,182,190,198,206,214,222,230,238,246,254]
AUDIT_REVIEW = 5109035402
AUDITED_HEAD = "316d509464a1c146824bd0717f54b4441e14dc59"
AUDITED_RUN = 33834804292
AUDITED_JOB = 100904998426


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_lock(lock: dict):
    p = ROOT / lock["path"]
    assert p.is_file(), p
    assert blob_sha1(p) == lock["blob_sha1"], p
    if p.suffix == ".json":
        d = json.loads(p.read_text())
        if "canonical_sha256" in lock:
            assert canonical_sha256(d) == lock["canonical_sha256"], p
        return d
    return p.read_text()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    assert Path(args.check).as_posix() == CERT_PATH
    cert = json.loads((ROOT / CERT_PATH).read_text())
    assert cert["schema"] == "STAGE32_POST1518_O210_Q602_18_DIAGONAL_RETAINED_GEOMETRY_BOUNDED_TEST_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    locks = cert["source_locks"]
    spectrum = load_lock(locks["audited_trace_spectrum"])
    oldgeom = load_lock(locks["post1500_geometry_negative"])
    load_lock(locks["post1500_repair_source_note"])
    incidence = load_lock(locks["marked_exceptional_incidence"])
    cusp = load_lock(locks["v4_cusp_quotient"])
    arsenal = load_lock(locks["arsenal_index"])
    pw05 = load_lock(locks["arsenal_s32_pw05"])
    note = load_lock(locks["source_note"])

    assert locks["audited_trace_spectrum"]["hostile_reaudit_review"] == 5108941088
    assert spectrum["exact_spectrum"]["diagonal_intersection_values"] == EXPECTED_VALUES
    assert spectrum["decision"]["Q602_excluded"] is False and spectrum["decision"]["O210_excluded"] is False
    assert oldgeom["status"] == "AUDITED_NEGATIVE"
    assert oldgeom["result"]["new_geometric_exclusion_certified"] is False
    assert any("intersection/multiplicity/ramification" in x for x in oldgeom["required_new_evidence"])

    checks = incidence["checks"]
    assert len(incidence["rows"]) == 48
    assert checks["distinct_realized_boundary_pair_count"] == 12
    assert checks["each_realized_boundary_pair_node_count"] == 4
    assert incidence["firewalls"]["incidence_is_not_histogram_exclusion"] is True
    assert incidence["firewalls"]["ramification_support_is_not_global_correspondence_existence"] is True
    assert cusp["exact_group_checks"]["V4_quotient_cusp_count"] == 6
    assert cusp["quotient_geometry"]["six_quotient_cusps_are_Weierstrass_points"] is True
    assert cusp["firewalls"]["abstract_cusp_orbits_not_yet_retained_boundary_label_identification"] is True
    assert arsenal["registry_contract"]["authority_order"][0] == "active stage controller and current source locks"
    assert "FINITE_GROUP_EQUIVARIANT_RECONSTRUCTION" in pw05
    assert "semantic/geometric identification merely from reconstructed algebra" in pw05

    inp = cert["audited_input"]
    assert inp == {"O":210,"Q":602,"canonical_residue":73,"diagonal_value_count":18,"diagonal_values":EXPECTED_VALUES}
    r = cert["bounded_result"]
    assert r["input_diagonal_value_count"] == r["output_diagonal_value_count"] == 18
    assert r["output_diagonal_values"] == EXPECTED_VALUES and r["pruning"] == "18 -> 18"
    assert r["new_exact_scalar_predicate_found"] is False
    assert r["new_geometric_exclusion_certified"] is False
    assert r["Q602_excluded"] is False and r["O210_excluded"] is False and r["O212_plus_authorized"] is False
    assert r["global_repository_absence_claim"] is False and r["theorem_absence_claim"] is False
    assert r["geometric_realization_inferred"] is False
    assert "does **not** mean that all 18 are geometrically realizable" in note
    fw = cert["firewalls"]
    assert all(fw[k] is False for k in ["lattice_survival_implies_geometric_realization","bounded_search_implies_repo_absence","bounded_search_implies_theorem_absence","heavy_compute_authorized","full178_credit","effectivity_credit","receiver_credit","route_credit","theorem_credit","endpoint_credit","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"])

    ctl = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    assert ctl["stage"] == 32 and ctl["stage32_closed"] is False
    assert ctl["math_scope"]["fixed_z_O212_through_O266_qprime4"] == "BLOCKED_BEHIND_O210"
    cfw = ctl["firewalls"]
    assert cfw["O210_closed"] is False and cfw["Q602_excluded"] is False
    assert cfw["geometric_realization_of_lattice_points_inferred"] is False
    assert cfw["receiver_credit"] is False and cfw["route_credit"] is False and cfw["theorem_credit"] is False and cfw["endpoint_credit"] is False

    schema = ctl["schema"]
    b = ctl["post1520_q602_18_diagonal_retained_geometry_test_provisional"]
    assert b["certificate_path"] == CERT_PATH and b["certificate_blob_sha1"] == blob_sha1(ROOT / CERT_PATH)
    assert b["canonical_sha256"] == EXPECTED_CANONICAL
    assert b["source_note_blob_sha1"] == blob_sha1(ROOT / b["source_note_path"])
    assert b["workflow"] == WORKFLOW_PATH and b["workflow_blob_sha1"] == blob_sha1(ROOT / WORKFLOW_PATH)
    assert b["pruning"] == "18 -> 18" and b["surviving_diagonal_values"] == EXPECTED_VALUES

    if schema == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V246_POST1520_Q602_RETAINED_GEOMETRY_18_TO_18_PROVISIONAL":
        assert ctl["advance_allowed"] is False and ctl["merge_allowed"] is False and ctl["checkpoint_merge_ready"] is False
        assert ctl["active_pr"] == {"number":1520,"branch":"stage32-post1518-retained-geometry-18-bounded-test","automatic_merge_authorized":False}
        assert ctl["current_item"] == "O210_Q602_PROVISIONAL_RETAINED_GEOMETRY_18_TO_18_HOSTILE_AUDIT"
        assert ctl["current_leaf"]["status"] == "PROVISIONAL_EXACT_BOUNDED_NEGATIVE_PENDING_HOSTILE_AUDIT"
        assert b["status"] == "PROVISIONAL_EXACT_BOUNDED_NEGATIVE_PENDING_HOSTILE_AUDIT"
        assert b["verifier_blob_sha1"] == blob_sha1(ROOT / VERIFIER_PATH)
        assert ctl["audit_required_before_promotion"] is True
        assert ctl["handoff"]["fresh_head_required"] is True and ctl["handoff"]["do_not_merge"] is True
    elif schema == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V247_POST1520_Q602_RETAINED_GEOMETRY_18_TO_18_AUDITED":
        assert ctl["advance_allowed"] is True and ctl["merge_allowed"] is True and ctl["checkpoint_merge_ready"] is True
        assert ctl["active_pr"] == {"number":1521,"branch":"stage32-post1520-audited-promotion","automatic_merge_authorized":False}
        audit = ctl["post1520_hostile_audit_pass"]
        assert audit["review_id"] == AUDIT_REVIEW and audit["audited_exact_head"] == AUDITED_HEAD
        assert audit["exact_head_ci"] == {"run_id":AUDITED_RUN,"job_id":AUDITED_JOB,"result":"SUCCESS"}
        assert audit["verdict"] == "PASS"
        assert audit["authority_promotion"] == "AUDITED_BOUNDED_RETAINED_GEOMETRY_18_TO_18_NONPRUNING_ONLY"
        assert b["status"] == "AUDITED_EXACT_BOUNDED_NEGATIVE_AFTER_HOSTILE_AUDIT"
        assert b["authority_effect"].startswith("AUDITED_BOUNDED_18_TO_18_NONPRUNING_ONLY")
        assert ctl["current_item"] == "O210_Q602_NEW_SCALAR_COUPLING_ROUTE_SELECTION"
        assert ctl["current_leaf"]["status"] == "AUDITED_BOUNDED_NEGATIVE_18_TO_18"
        assert ctl["audit_required_before_promotion"] is False
        assert ctl["handoff"]["do_not_merge"] is False
    else:
        raise AssertionError(f"unsupported controller schema: {schema}")

    print("PASS: Stage32 retained-geometry test remains exact 18->18 under pending/audited successor authority; no Q602/O210 exclusion or realization credit.")

if __name__ == "__main__":
    main()
