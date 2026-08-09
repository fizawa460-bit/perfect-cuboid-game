#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
T32 = ROOT / "stages/stage14/14-t32/result.md"
T33 = ROOT / "stages/stage14/14-t33/result.md"
TH0 = ROOT / "stages/stage14/14-tH0/result.md"
FROZEN = ROOT / "stages/stage14/data/tH0/roadworks_architecture_summary.json"


def require(text: str, marker: str, source: str) -> None:
    if marker not in text:
        raise AssertionError(f"missing marker in {source}: {marker}")


def build_summary() -> dict:
    t32 = T32.read_text(encoding="utf-8")
    t33 = T33.read_text(encoding="utf-8") if T33.exists() else ""
    th0 = TH0.read_text(encoding="utf-8")

    for marker in [
        "STAGE14_T32=COMPLETE_SPLIT_TORUS_NORM_CORRELATION_AND_UNIFIED_COFACTOR_SKELETON",
        "VISIBLE_INVISIBLE_SUPER_SQRT_NORM_SKELETON_UNIFIED=true",
        "SPLIT_AUXILIARY_PRIME_RESTRICTION_REQUIRED_FOR_TORUS_BOUND=true",
        "ANGULAR_COMPLETE_CORRELATION_CLOSED=true",
        "NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false",
    ]:
        require(t32, marker, "Stage14-t32")

    t33_present = bool(t33)
    if t33_present:
        for marker in [
            "STAGE14_T33=COMPLETE_QUADRATIC_HECKE_VALUE_TRANSFER_AND_MELLIN_SPECTRAL_BOUNDARY",
            "QUADRATIC_HECKE_VALUE_SYMBOL_IDENTIFIED=true",
            "GOLDMAKHER_LOUVEL_QUADRATIC_LARGE_SIEVE_DIRECTLY_SUFFICIENT=false",
            "ALL_CHARACTER_MELLIN_HECKE_SIEVE_OBJECT_DEFINED=true",
        ]:
            require(t33, marker, "Stage14-t33")
        higher_order = "HIGHER_ORDER_MELLIN_MODES_REQUIRED=true" in t33
        if not higher_order:
            require(t33, "Higher-order modes are unavoidable", "Stage14-t33")
    else:
        higher_order = False

    for marker in [
        "STAGE14_TH0=COMPLETE_INDEPENDENT_T_SUPPORT_ROADWORKS_ARCHITECTURE",
        "TH_MINIMUM_FROZEN_T_INPUT=Stage14-t32",
        "TH_REQUIRES_T33_OR_LATER_TO_ADVANCE=false",
        "TH_CAN_ADVANCE_WHILE_T_IS_STALLED=true",
        "TH_CAN_ADVANCE_WHILE_T_IS_AHEAD=true",
        "TH_MUST_NOT_REQUIRE_A_FUTURE_T_RESULT_FOR_NEXT_STAGE=true",
        "TH_BLOCKED_SUBTOOL_IS_PARKED_NOT_PROPAGATED_AS_WAITING_STAGE=true",
        "TH_DOES_NOT_CLAIM_T_PROOF_CLOSURE=true",
        "NEXT=Stage14-tH1",
    ]:
        require(th0, marker, "Stage14-tH0")

    return {
        "stage": "Stage14-tH0",
        "status": "COMPLETE_INDEPENDENT_T_SUPPORT_ROADWORKS_ARCHITECTURE",
        "minimum_frozen_t_input": "Stage14-t32",
        "requires_t33_or_later_to_advance": False,
        "t32_contract": {
            "unified_gaussian_norm_skeleton": "N(U)=m,N(V)=k*delta,k|epsilon*m,epsilon*ell*m*delta/2<=B",
            "visible_invisible_unified": True,
            "split_auxiliary_prime_restriction": True,
            "angular_complete_correlation_closed": True,
            "norm_index_hyperbolic_power_saving_proved": False,
        },
        "t33_optional_snapshot": {
            "present_at_th0_freeze": t33_present,
            "quadratic_hecke_value_symbol_identified": t33_present,
            "quadratic_only_large_sieve_directly_sufficient": False,
            "higher_order_mellin_modes_required": higher_order,
            "all_character_mellin_hecke_object_defined": t33_present,
            "is_progress_prerequisite": False,
        },
        "operating_contract": {
            "pull_not_push_handoff": True,
            "can_advance_while_t_stalled": True,
            "can_advance_while_t_ahead": True,
            "stage_number_coupled_to_t_stage_number": False,
            "only_merged_stable_t_interfaces": True,
            "future_t_result_required_for_next_stage": False,
            "blocked_subtool_parked_not_waiting_stage": True,
            "claims_t_proof_closure": False,
            "new_q_stage_required_to_advance": False,
        },
        "default_roadmap": [
            ["Stage14-tH1", "Gaussian primary/ray-class normalisation"],
            ["Stage14-tH2", "divisor-coupled norm-index hyperbola engine"],
            ["Stage14-tH3", "all-order character/conductor adapter"],
            ["Stage14-tH4", "weighted Mellin/Hecke large-sieve toolbox"],
            ["Stage14-tH5", "Gaussian norm coefficient/collision energy"],
            ["Stage14-tH6", "abstract power-saving transfer ledger"],
            ["Stage14-tH7", "stress test and park/continue gate"],
        ],
        "proof_boundary": {
            "gaussian_hecke_large_sieve_transfer_proved": False,
            "all_character_mellin_hecke_large_sieve_proved": False,
            "norm_index_hyperbolic_correlation_power_saving_proved": False,
            "a11_power_saving_proved": False,
            "t_o_sqrt_b_proved": False,
            "perfect_cuboid_nonexistence_proved": False,
        },
        "next": "Stage14-tH1",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="rewrite frozen summary")
    args = parser.parse_args()

    summary = build_summary()
    rendered = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"

    if args.write:
        FROZEN.parent.mkdir(parents=True, exist_ok=True)
        FROZEN.write_text(rendered, encoding="utf-8")
        print(FROZEN)
        return

    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if frozen != summary:
        raise AssertionError(
            "frozen tH0 summary differs semantically; run roadworks_architecture_audit.py --write"
        )

    print("Stage14-tH0 roadworks architecture audit: OK")


if __name__ == "__main__":
    main()
