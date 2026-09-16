#!/usr/bin/env python3
import json
from pathlib import Path

CERT_PATH = Path(__file__).with_name("KNOWN-CONIC-MULTIBRANCH-CERTIFICATE.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    require(cert["schema"] == "STAGE32_MB104_KNOWN_CONIC_MB_EXCLUSION_V1", "schema")
    require(cert["status"] == "RETAINED_EXACT_POPULATION_ADAPTER_MB104_INCOMPLETE", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    src = cert["source_lock"]
    require(src["repository"] == "MichaelStollBayreuth/Verification", "source repo")
    require(src["commit"] == "51233ed5ef2bf228fac9416c66db9adc0ebcaadd", "source commit")
    require(src["blob_sha1"] == "0422b69847f2afb97cb7b3ed02ebef91279f61b1", "source blob")
    require(src["known_a_conic_count"] == 32, "conic count")

    rep = cert["representative_family"]
    require(rep["reduced_plane_equation"] == "b2^2+b3^2-c^2=0", "representative conic")
    require(rep["gradient"] == "(2*b2,2*b3,-2*c)", "gradient")
    require(rep["smooth_projective_conic_in_characteristic_zero"] is True, "smooth representative")

    sym = cert["symmetry_contract"]
    require(sym["four_source_families_of_eight"] is True, "4x8 families")
    require(sym["all_32_obtained_by_coordinate_sign_symmetry"] is True, "symmetry coverage")
    require(sym["all_32_smooth_geometrically_integral"] is True, "all smooth")

    norm = cert["normalization_contract"]
    require(norm["smooth_integral_curve_normalization_is_isomorphism"] is True, "normalization iso")
    require(norm["preimage_count_of_each_curve_point"] == 1, "one normalization preimage")
    require(norm["for_every_met_box_node_r_i"] == 1, "r_i=1")
    require(norm["receiver_requires_exists_r_i_ge"] == 2, "receiver threshold")
    require(norm["known_32_conics_in_multibranch_receiver"] is False, "conics excluded")

    btva = cert["btva_consequence"]
    require(btva["genus0_multibranch_carrier_is_nonconic"] is True, "g0 MB nonconic")
    require(btva["genus0_multibranch_min_distinct_nodes"] == 7, "g0 node support")
    require(btva["genus0_multibranch_node_support_spans_P6"] is True, "g0 full span")

    fw = cert["credit_firewall"]
    for key in [
        "MB104_complete",
        "finite_degree_window_proved_population_wide",
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

    print("PASS: all 32 known plane conics are smooth and cannot satisfy the multibranch receiver condition")


if __name__ == "__main__":
    main()
