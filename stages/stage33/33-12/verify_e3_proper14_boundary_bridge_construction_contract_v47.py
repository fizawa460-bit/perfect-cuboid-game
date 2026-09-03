#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-proper14-boundary-bridge-construction-contract-v47.json"
EXPECTED_DOMAIN = [
    "A2_02", "A2_03", "A2_24", "A2_25", "A2_26", "A2_04", "A2_01",
    "A2_07", "A2_05", "A2_10", "A2_08", "A2_09", "A2_16", "A2_15",
]


def main() -> None:
    d = json.loads(CERT.read_text(encoding="utf-8"))
    assert d["schema"] == "stage33.e3.proper14_boundary_bridge_construction_contract.v47"
    assert d["micro_goal"] == "A1_1_DEFINE_FINITE_NEW_CONSTRUCTION_CONTRACT_FOR_P_W"
    assert d["parent_absence_lock_commit"] == "b4decf905bdca3045d5caf8889349ab4fe1a970c"
    bridge = d["bridge"]
    assert bridge["name"] == "P_W"
    assert bridge["field"] == "F2"
    assert bridge["matrix_shape"] == [14, 14]
    assert bridge["materialized"] is False
    assert bridge["usable_for_e3"] is False
    assert d["domain_order"] == EXPECTED_DOMAIN
    assert d["codomain_order"] == [f"proper14_axis_{i}" for i in range(1, 15)]
    cols = d["required_columns"]
    assert len(cols) == 14
    for i, (col, label) in enumerate(zip(cols, EXPECTED_DOMAIN), start=1):
        assert col == {"column": i, "domain_label": label, "status": "UNMATERIALIZED"}
    contract = d["column_acceptance_contract"]
    assert contract["proper14_image_f2_length"] == 14
    assert contract["entries_allowed"] == [0, 1]
    assert contract["exact_provenance_required"] is True
    assert contract["positional_inference_forbidden"] is True
    assert contract["existing_bridge_search_forbidden_by_v46"] is True
    gate = d["bridge_completion_gate"]
    assert gate["all_14_columns_materialized"] is True
    assert gate["rank_14_required_before_treating_as_basis_identification"] is True
    assert gate["inverse_check_required_if_rank_14"] is True
    assert gate["a1_2_e3_mapping_allowed_only_after_gate"] is True
    assert d["e3_target_after_bridge_only"] == {
        "proper14_mask_decimal": 20,
        "proper14_support_one_based": [3, 5],
        "mapping_executed": False,
    }
    assert d["stage33_credit"]["progress_big_tasks"] == "6/11"
    assert d["stage33_credit"]["stage33_12_exact_closed"] is False
    assert d["stage33_credit"]["merge_allowed"] is False
    assert d["status"] == "PASS_EXACT_A1_1_FINITE_P_W_CONSTRUCTION_CONTRACT"
    assert d["next_exact_leaf"] == "A1_1_C1_CONSTRUCT_PROPER14_IMAGE_OF_A2_02_BY_NEW_EXACT_DERIVATION_NOT_BY_SEARCH"
    print("PASS: V47 finite P_W construction contract")


if __name__ == "__main__":
    main()
