#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648ab-popov-k12-affine-class-pointwise-nonselection.json"
NOTE = HERE / "post1648ab-popov-k12-affine-class-pointwise-nonselection-source-note.md"
AA = HERE / "post1648aa-deraux-weierstrass-orbit-b9-fixed-pair-nonselection.json"
W = HERE / "post1648w-rains-st12-theta-torsor-cohomology-nonselection.json"

EXPECTED_CERT_CANONICAL = "84ce4096aac5adf829df9bf001a28b7b92a7e0e513d122e5f55ce49b77825874"
EXPECTED_NOTE_BLOB = "e38996abe3bc587c82aa0390bf3b7defc22a01ca"
EXPECTED_AA_BLOB = "c989058beb079cc36fb1d52f58707986e8b4320b"
EXPECTED_AA_CANONICAL = "a0ca0342db4902e737f28aa5f0de447cca2a2fce71f8cf0cdd2775d51804f7c7"
EXPECTED_W_BLOB = "5a3e5c6292f93d463e540f4c88f7c00f64a2c476"
EXPECTED_W_CANONICAL = "af2fa5b0f5e64a33040f2135015745aeb22ea7f94a1c454730e00bab7a4c3aad"


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert canonical_sha(cert) == EXPECTED_CERT_CANONICAL
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT_CANONICAL
    assert git_blob_sha(NOTE) == EXPECTED_NOTE_BLOB

    aa = json.loads(AA.read_text(encoding="utf-8"))
    assert git_blob_sha(AA) == EXPECTED_AA_BLOB
    assert canonical_sha(aa) == EXPECTED_AA_CANONICAL
    assert aa["canonical_sha256_without_this_field"] == EXPECTED_AA_CANONICAL
    assert aa["deraux_affine_A2_replay"]["orbit_size"] == 6
    assert aa["B9_fixed_pair_test"]["fixed_pair_difference_counts_total"] == {"L1": 4, "L2": 4, "L3": 4}
    assert aa["semantic_boundary"]["two_sided_set_level_anchor_obtained"] is True
    assert aa["semantic_boundary"]["pointwise_source_to_target_weierstrass_binding_obtained"] is False

    w = json.loads(W.read_text(encoding="utf-8"))
    assert git_blob_sha(W) == EXPECTED_W_BLOB
    assert canonical_sha(w) == EXPECTED_W_CANONICAL
    assert w["canonical_sha256_without_this_field"] == EXPECTED_W_CANONICAL
    assert w["H1_exact_calculation"]["H1_count"] == 2
    assert w["H1_exact_calculation"]["unique_nonzero_class_representative_count"] == 16
    assert [x["line"] for x in w["H1_exact_calculation"]["retained_W_lines_occurring_as_T_component"]] == ["L1", "L2", "L3"]

    popov = cert["external_source_lock"]["popov"]
    assert "Table 2 entries [K12] and [K12]*" in popov["locators"]
    assert cert["class_level_bridge"]["shephard_todd_group_number"] == 12
    assert cert["class_level_bridge"]["abstract_group"] == "GL(2,F3)"
    assert cert["class_level_bridge"]["popov_split_class"] == "[K12], c=0"
    assert cert["class_level_bridge"]["popov_nonsplit_class"] == "[K12]*, c(r1)=c(r2)=0, c(r3)=((1+i)/2)e3"
    assert cert["class_level_bridge"]["popov_affine_class_materialized"] is True
    assert cert["class_level_bridge"]["actual_integral_conjugating_g_materialized"] is False
    assert cert["class_level_bridge"]["pointwise_image_of_source_infinity_materialized"] is False
    assert cert["class_level_bridge"]["pointwise_image_of_source_zero_materialized"] is False

    boundary = cert["semantic_boundary"]
    assert boundary["popov_cocycle_is_a_cohomology_representative_not_a_pointwise_bolza_marking"] is True
    assert boundary["basepoint_change_is_coboundary"] is True
    assert boundary["popov_table_basis_explicitly_bound_to_stage32_retained_basis"] is False
    assert boundary["popov_reflection_generators_explicitly_bound_to_kkk_named_curve_generators"] is False
    assert boundary["krr_alpha_infinity_equals_zero_promoted_through_unspecified_conjugating_g"] is False
    assert boundary["post1648AA_set_level_six_point_anchor_upgraded_to_pointwise_anchor"] is False
    assert boundary["rains_H1_class_identified_with_popov_H1_class"] is False

    decision = cert["decision"]
    assert decision["popov_k12_star_affine_class_materialized"] is True
    assert decision["popov_k12_star_route_selects_pointwise_weierstrass_image"] is False
    assert decision["absolute_delta0inf_retained_W_line_identified"] is False
    assert decision["survivors_current_credit"] == [73, 97, 235]
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False

    fw = cert["firewalls"]
    assert fw["scratch_result_promoted_to_MAIN_authority"] is False
    assert fw["scratch_result_promoted_to_current_credit"] is False
    assert fw["cohomology_class_promoted_to_pointwise_marking"] is False
    assert fw["unspecified_krr_g_promoted_to_explicit_adapter"] is False
    assert fw["bounded_route_block_promoted_to_global_nonexistence"] is False

    print("POST1648AB_POPOV_K12_AFFINE_CLASS_POINTWISE_NONSELECTION_COMPLETE")
    print("popov_K12_split=c0 nonsplit=K12star_explicit_H1_class")
    print("basepoint_change=1-coboundary pointwise_g_materialized=false")
    print("AA_two_sided_set_anchor=6 pointwise_binding=false")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")


if __name__ == "__main__":
    main()
