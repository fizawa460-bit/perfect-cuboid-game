#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CERT_PATH = Path(__file__).with_name("CERTIFICATE.json")


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    require(cert["schema"] == "STAGE32_MB103_AUT_PROFILE_QUOTIENT_V1", "schema")
    require(cert["status"] == "RETAINED_NO_CREDIT", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    aut = cert["automorphism_contract"]
    require(aut["exceptional_node_count"] == 48, "48-node action")
    require(aut["group"] == "Aut(S)", "group")
    require(aut["group_order"] == 1536, "published group order")

    fields = set(cert["node_packet_fields"])
    required_fields = {
        "r_i",
        "M_i",
        "branch_multiplicities_m_ij",
        "resolved_landing_partition",
        "intrinsic_branch_delta_values",
        "pairwise_local_intersection_multiplicities",
        "Delta_i_exc",
        "multibranch_membership",
    }
    require(required_fields <= fields, "complete transported packet")

    tr = cert["transport_contract"]
    for key in [
        "node_labels_may_permute",
        "actual_resolved_landing_points_are_transported",
        "branch_multiplicities_preserved",
        "resolved_landing_partition_preserved_up_to_transport",
        "local_delta_data_preserved",
        "pairwise_intersection_data_preserved",
        "multibranch_membership_preserved",
    ]:
        require(tr[key] is True, f"transport {key}")
    require(tr["raw_chart_labels_A_lt_B_A_gt_B_A_eq_B_are_orbit_invariants"] is False,
            "chart-label firewall")

    orb = cert["orbit_contract"]
    require("exists phi in Aut(S)" in orb["equivalence"], "exact orbit equivalence")
    require("lexicographically least" in orb["complete_key"], "complete orbit key semantics")
    require(orb["scalar_summaries_are_complete_orbit_keys"] is False,
            "scalar summaries not complete")
    scalars = set(orb["necessary_scalar_invariants"])
    for key in ["N", "N_MB", "R", "M", "Delta_exc", "d", "D^2", "normalization_genus_g", "Delta_total"]:
        require(key in scalars, f"missing scalar invariant {key}")

    mat = cert["materialization_firewall"]
    require(mat["node_permutation_table_materialized_in_repo"] is False,
            "no false materialization claim")
    require(mat["materialization_required_before_MB105_production_orbit_dedup"] is True,
            "MB105 materialization gate")
    require(mat["semantic_quotient_defined_without_materialization"] is True,
            "semantic quotient retained")
    require(mat["finite_degree_window_proved"] is False, "no premature finite window")
    require(mat["finite_picard_enumeration_released"] is False, "no premature enumeration")

    for lock in cert["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"source drift {lock['path']}")

    ext = cert["external_source_lock"]
    require(ext["repository"] == "MichaelStollBayreuth/Verification", "upstream repo")
    require(ext["commit"] == "51233ed5ef2bf228fac9416c66db9adc0ebcaadd", "upstream commit")
    require(ext["path"] == "Cuboids/cuboids.magma", "upstream path")
    require(ext["blob_sha1"] == "0422b69847f2afb97cb7b3ed02ebef91279f61b1", "upstream blob")
    features = set(ext["required_features"])
    for feature in [
        "48 singular points",
        "nine explicit automorphism coordinate substitutions",
        "permutations on known curves and singular points",
        "descent of action to Pic(S)",
        "AutS generated in GL(64,Z)",
        "Aut(S) order 1536",
    ]:
        require(feature in features, f"upstream feature {feature}")

    fw = cert["credit_firewall"]
    require(fw["mb101_retained"] and fw["mb102_retained"] and fw["mb103_retained"],
            "retained chain")
    for key in [
        "mb104_complete",
        "mb105_complete",
        "finite_picard_enumeration_released",
        "r29_lg2_mb_discharged",
        "receiver_credit",
        "effectivity_credit",
        "final_milestone_credit",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ]:
        require(fw[key] is False, f"credit firewall {key}")
    require(cert["next_node"] == "MB104", "next node")

    print("PASS: MB103 exact Aut(S) profile quotient semantics retained with zero receiver credit")


if __name__ == "__main__":
    main()
