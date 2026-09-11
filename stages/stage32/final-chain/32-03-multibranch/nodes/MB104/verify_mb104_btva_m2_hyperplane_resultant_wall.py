#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
NOTE = NODE / "BTVA-M2-HYPERPLANE-RESULTANT-WALL-SOURCE-NOTE.md"
CERT = NODE / "BTVA-M2-HYPERPLANE-RESULTANT-WALL.json"
NOTE_BLOB = "d48bcaf6e160daa22b1948119d99787abf0059a9"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    assert git_blob_sha(NOTE) == NOTE_BLOB
    cert = json.loads(CERT.read_text())
    assert cert["schema"] == "STAGE32_MB104_BTVA_M2_HYPERPLANE_RESULTANT_WALL_V1"

    m2 = cert["m2_reflexive_space"]
    assert m2["symmetric_degree"] == 2
    assert m2["h0_reflexive"] == 13
    assert m2["displayed_generator_count"] == 13

    # BTVA Table-1 character multiplicities give the same total dimension.
    fingerprint = [3, 3, 3, 1, 1, 1, 1]
    assert sum(fingerprint) == 13

    hv = cert["hyperplane_vanishing_contract"]
    assert hv["dimension"] == 1
    assert hv["two_independent_sections_available"] is False

    rh = cert["btva_resultant_hypothesis"]
    assert rh["symmetric_degree"] == 2
    assert rh["required_independent_sections"] == 2
    assert hv["dimension"] < rh["required_independent_sections"]
    assert rh["hypothesis_satisfied_on_cuboid"] is False

    anc = cert["ancillary_scope"]
    assert anc["constructs_reflexive_double_dual"] is True
    assert anc["records_13_degree_zero_forms"] is True
    assert anc["arbitrary_node_subset_extension_matrix_retained"] is False
    assert anc["population_wide_N_ge_14_resultant_retained"] is False

    dec = cert["decision"]
    assert dec["retire_immediate_two_section_m2_hyperplane_resultant_route"] is True
    assert dec["degree_two_differential_methods_fully_retired"] is False
    assert dec["next_subobligation"] == "MB104_N_GE_14_NODE_EXTENSION_MATRIX_OR_HIGHER_M_GLOBAL_MEMBER_OBSTRUCTION"

    fw = cert["firewalls"]
    assert fw["hyperplane_twist_dimension_one_equals_global_regular_m2_dimension_one"] is False
    assert fw["full_13_space_arbitrary_subset_extension_rank_known"] is False
    assert fw["all_m2_methods_impossible_claimed"] is False
    assert fw["finite_degree_window_proved_population_wide"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["r29_lg2_mb_discharged"] is False
    assert fw["merge_authorized"] is False

    print("MB104 BTVA m=2 hyperplane-resultant wall verifier PASS")
    print("h0(reflexive m=2)=13; dim hyperplane-vanishing twist=1")
    print("BTVA two-section hyperplane-resultant hypothesis therefore fails at m=2")
    print("arbitrary-node extension matrices / higher-m actual sections remain OPEN")


if __name__ == "__main__":
    main()
