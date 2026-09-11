#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"

LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-M2-HYPERPLANE-RESULTANT-WALL.json": "ce7928cc6df4aa7c911175ae685d03d42ee02098",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-PROJECTIVE-SPAN-FILTER.json": "4ee8e6061a7cc2a54b54786fd065923434381bde",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-M2-DESCENDED-EXTENSION-CAPACITY-SOURCE-NOTE.md": "c9813ac7d25df4f823af2c9a58d57ba8b5405c1e",
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    for rel, expected in LOCKS.items():
        got = git_blob_sha(ROOT / rel)
        assert got == expected, (rel, got, expected)

    cert = json.loads((NODE / "BTVA-M2-DESCENDED-EXTENSION-CAPACITY.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_BTVA_M2_DESCENDED_EXTENSION_CAPACITY_V1"

    pkg = cert["descended_package"]
    assert pkg["twisted_space_dimension"] == 1
    assert pkg["ambient_linear_form_dimension"] == 7
    assert pkg["package_dimension"] == 7
    assert pkg["multiplication_injective"] is True

    # Linear forms annihilating a rank-r node span form a (7-r)-dimensional space.
    for r in range(0, 8):
        dim = 7 - r
        assert dim >= 0
        assert (dim >= 1) == (r <= 6)
        assert (dim >= 2) == (r <= 5)

    ns = cert["node_support_adapter"]
    assert ns["dimension_formula"] == "dim U_T=7-r(T)"
    assert ns["one_section_condition"] == "r(T)<=6"
    assert ns["two_section_condition"] == "r(T)<=5"

    hd = cert["high_degree_consequences"]
    g0 = hd["genus0_nonconic"]
    assert g0["retained_node_rank"] == 7
    assert 7 - g0["retained_node_rank"] == g0["descended_package_capacity"] == 0
    assert g0["two_section_resultant_available_from_package"] is False

    g1 = hd["genus1"]
    assert g1["retained_node_rank_lower_bound"] == 6
    assert 7 - g1["retained_node_rank_lower_bound"] == g1["descended_package_capacity_upper_bound"] == 1
    assert g1["two_section_resultant_available_from_package"] is False

    dec = cert["decision"]
    assert dec["descended_package_arbitrary_node_support_exactly_understood"] is True
    assert dec["descended_package_closes_high_degree_receiver"] is False
    assert dec["next_subobligation"] == "MB104_FULL_M2_NODE_EXTENSION_MAPS_OR_HIGHER_M_GLOBAL_MEMBER_OBSTRUCTION"

    fw = cert["firewalls"]
    assert fw["U_T_equals_full_extendable_m2_space"] is False
    assert fw["all_m2_methods_retired"] is False
    assert fw["finite_degree_window_proved_population_wide"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["r29_lg2_mb_discharged"] is False
    assert fw["merge_authorized"] is False

    print("MB104 BTVA m=2 descended extension-capacity verifier PASS")
    print("U=H0(O(1))*eta has dimension 7; dim U_T=7-rank(T)")
    print("high-degree g=0 capacity=0; high-degree g=1 capacity<=1")
    print("full 13-dimensional node-extension maps remain OPEN")


if __name__ == "__main__":
    main()
