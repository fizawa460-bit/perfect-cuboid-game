#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT = ROOT / "stages/stage34/34-02/d2-stageA2-receiver-level-closure-assembly-preaudit.json"


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_locked(path: str, expected_blob: str):
    p = ROOT / path
    data = p.read_bytes()
    assert git_blob_sha(data) == expected_blob, (path, git_blob_sha(data), expected_blob)
    return json.loads(data)


def main():
    cert = json.loads(CERT.read_text())
    assert cert["schema"] == "STAGE34_02C_D2_STAGEA2_RECEIVER_LEVEL_CLOSURE_ASSEMBLY_PREAUDIT_V2"
    locked = {k: load_locked(*v) for k, v in cert["source_locks"].items()}

    pop = locked["global_population_contract"]
    assert pop["receiver"] == "R29-EXT-CHANG-C"
    assert pop["resolved_interface_status"]["P1_exact_object_and_population_closed"] is True
    assert pop["mw_basis_evidence"]["all_seven_source_free_lattices_span_full_free_part_authoritative"] is True

    cover = locked["exact_face3_cover_reduction"]
    assert cover["genus5_cover"]["receiver_equivalence"] == "For non-pole Q in E_q(Q), F3(Q) square iff Q lies in the projection of C_q(Q)."

    poles = locked["pole_torsion_lock"]
    assert poles["receiver_adapter"]["pole_points_in_receiver"] is False
    assert poles["receiver_adapter"]["nonpole_face3_square_equivalence_has_receiver_hole"] is False
    assert poles["order"]["pole_points"] == 4

    split = locked["split_to_receiver_pullback"]
    eq = split["fiber_product_equivalence_for_receiver"]
    assert eq["forward"].startswith("Every non-torsion rational C_q point has a unique surviving squareclass d in {1,2}")
    assert "matching finite non-pole x" in eq["receiver_target"]
    assert split["d1"]["receiver_exception"].endswith("outside the audited non-torsion receiver population.")
    assert split["d2"]["receiver_exception"].endswith("outside the non-torsion receiver population.")

    reconstruction = locked["reconstruction_factor_cover"]
    assert reconstruction["d1"]["reconstruction_cover"] == "W^2=H1(T,S)"
    assert reconstruction["d2"]["reconstruction_cover"] == "W^2=H2(T,S)"

    support = locked["odd_squareclass_support"]
    assert support["universal_template"]["H"] == "U*V*A*B"
    assert support["odd_prime_pattern_lemma"]["support"].startswith("If U*V*A*B is a rational square")

    two = locked["two_adic_pattern"]
    assert two["branch_upper_bound_before_real_and_Qp_filter"]["total_over_all_fourteen_cases"] == 29952

    promotion = locked["all_factor_hostile_promotion"]
    assert promotion["hostile_reaudit"]["review_id"] == 5087246610
    assert promotion["hostile_reaudit"]["result"] == "PASS"
    assert promotion["promotion"]["D2_all_factor_branches_closed"] is True
    assert promotion["promotion"]["authoritative_remaining_branches"] == 0
    assert promotion["promotion"]["authoritative_remaining_sign_orbits"] == 0
    assert "R29-EXT-CHANG-C receiver population" in promotion["promotion"]["scope"]

    assert cert["semantic_boundary"]["candidate_B_factor_cover_pointset_empty_required"] is False
    assert cert["semantic_boundary"]["direct_cover_rational_points_complete_required"] is False
    assert cert["assembly_result_candidate"]["receiver_face3_square_points_remaining"] == 0
    assert cert["assembly_result_candidate"]["all_non_torsion_receiver_points_face3_nonsquare"] is True
    assert cert["promotion_gate"]["requires_fresh_hostile_audit_of_this_receiver_level_implication"] is True
    assert cert["firewalls"]["direct_cover_rational_points_complete"] is False
    assert cert["firewalls"]["all_multiples_closed"] is False
    assert cert["firewalls"]["R29_EXT_CHANG_C_closed"] is False
    assert cert["firewalls"]["parent_route_closed"] is False
    assert cert["firewalls"]["merge_authorized"] is False

    print("PASS_EXACT_RECEIVER_LEVEL_CLOSURE_ASSEMBLY_PREAUDIT_ONLY")


if __name__ == "__main__":
    main()
