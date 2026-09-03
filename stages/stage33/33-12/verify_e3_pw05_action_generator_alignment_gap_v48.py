#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-pw05-action-generator-alignment-gap-v48.json"
V47 = HERE / "e3-proper14-boundary-bridge-construction-contract-v47.json"
SOURCE = ROOT / "stages/stage33/33-11f/stage33-11f-source-lock.json"
TARGET = ROOT / "stages/stage33/33-07/proper-brauer2-from-discriminant.json"
PW05 = ROOT / "docs/arsenal/cards/provisional/S33-PW05.md"
S30W01 = ROOT / "docs/arsenal/cards/formal/S30-W01.md"

EXPECTED_ACTIONS = [
    "sign_a1", "sign_a2", "sign_a3", "sign_b1", "sign_b2", "sign_b3",
    "sign_c", "swap12", "swap13",
]
EXPECTED_WORKING = [
    "A2_02", "A2_03", "A2_24", "A2_25", "A2_26", "A2_04", "A2_01",
    "A2_07", "A2_05", "A2_10", "A2_08", "A2_09", "A2_16", "A2_15",
]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    d = load(CERT)
    v47 = load(V47)
    source = load(SOURCE)
    target = load(TARGET)

    assert d["schema"] == "stage33.e3.pw05_action_generator_alignment_gap.v48"
    assert d["parent_contract_commit"] == "bb9ab7dd258c152acc9f0a97c435419111a98e91"
    assert d["arsenal_route"]["primary"].startswith("S33-PW05:")
    assert d["arsenal_route"]["formal_parent"].startswith("S30-W01:")
    assert d["arsenal_route"]["cards_are_routing_not_live_stage_authority"] is True

    assert source["canonical_sha256"] == d["source_module"]["canonical_sha256"]
    assert source["exact_source_actions"]["coefficient_field"] == "F2"
    assert source["exact_source_actions"]["dimension"] == 26
    assert source["exact_source_actions"]["action_names"] == EXPECTED_ACTIONS
    assert d["source_module"]["action_names"] == EXPECTED_ACTIONS

    assert target["canonical_sha256"] == d["target_module"]["canonical_sha256"]
    assert len(target["proper_Br2_cc_action_f2"]) == 14
    assert len(target["proper_Br2_ct_action_f2"]) == 14
    assert all(len(row) == 14 for row in target["proper_Br2_cc_action_f2"])
    assert all(len(row) == 14 for row in target["proper_Br2_ct_action_f2"])
    assert d["target_module"]["action_names"] == ["cc", "ct"]

    assert v47["domain_order"] == EXPECTED_WORKING
    assert d["source_module"]["working_14_order_from_v47"] == EXPECTED_WORKING

    pw05_text = PW05.read_text(encoding="utf-8")
    s30_text = S30W01.read_text(encoding="utf-8")
    assert "EQUIVARIANT_SOURCE_TARGET_COMPATIBILITY_AUDIT" in pw05_text
    assert "both modules/bases/actions explicit" in pw05_text
    assert "positive diagnostic as geometric identification" in pw05_text
    assert "FINITE_EQUIVARIANT_ACTION_IDENTIFICATION" in s30_text
    assert "source/common-model anchor" in s30_text

    gap = d["exact_gap"]
    assert gap["required_object"] == "COMMON_ACTION_GENERATOR_ALIGNMENT"
    assert gap["cc_source_word_or_matrix_materialized"] is False
    assert gap["ct_source_word_or_matrix_materialized"] is False
    assert gap["common_generator_set_for_pw05_equations_materialized"] is False
    assert gap["working_14_stability_under_aligned_cc_ct_checked"] is False
    assert gap["intertwiner_space_computation_authorized"] is False
    assert gap["repository_search_required"] is False

    assert d["p_w"] == {
        "materialized": False,
        "columns_materialized": 0,
        "e3_mask20_mapped": False,
    }
    assert d["stage33_credit"]["progress_big_tasks"] == "6/11"
    assert d["stage33_credit"]["stage33_12_exact_closed"] is False
    assert d["stage33_credit"]["merge_allowed"] is False
    assert d["status"] == "PASS_EXACT_A1_1_ARSENAL_ROUTE_COMMON_ACTION_GENERATOR_ALIGNMENT_NOT_YET_MATERIALIZED"
    assert d["next_exact_leaf"]["name"] == "A1_1_G1_MATERIALIZE_SOURCE_DERIVED_CC_CT_TO_A2_ACTION_GENERATOR_MAP"

    print("PASS: V48 Arsenal-routed common action-generator alignment gap")


if __name__ == "__main__":
    main()
