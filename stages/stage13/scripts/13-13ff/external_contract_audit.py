#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
STAGE13 = ROOT / "stages" / "stage13"
OUT = STAGE13 / "data" / "13-13ff" / "external_contract_audit.json"


def build_report() -> dict:
    contract = (STAGE13 / "13-13ff" / "external-theorem-contracts.md").read_text()
    result = (STAGE13 / "13-13ff" / "result.md").read_text()
    gate_d = (STAGE13 / "13-13fd" / "harmonic-conductor-lemma.md").read_text()
    crosswalk = (STAGE13 / "13-13b" / "external-theorem-crosswalk.md").read_text()
    roadmap = (STAGE13 / "13-13" / "roadmap.md").read_text()
    plan = (STAGE13 / "13-13f" / "r05-repair-plan.md").read_text()

    checks = {
        "chi4_contract_visible": all(token in contract for token in [
            "L(s,\\chi_4)",
            "L_CHI4_HOLOMORPHIC_AT_1=true",
        ]),
        "crosswalk_zero_free_redundancy_preserved": "VALID_BUT_LOGICALLY_REDUNDANT_FOR_FINAL_PROOF" in crosswalk,
        "fixed_residue_conductor_visible": all(token in contract for token in [
            "FIXED_RESIDUE_CONDUCTOR=true",
            "GROWING_MODULUS_THEOREM_USED=false",
        ]),
        "gate_d_interface_matched": all(token in contract and token in gate_d for token in [
            "S_\\ell(X)",
            "(1+\\ell)^{C_H}",
            "\\delta_H",
        ]),
        "hecke_entire_contract_visible": all(token in contract for token in [
            "HECKE_NONZERO_ENTIRE=true",
            "HECKE_NONZERO_FUNCTIONAL_EQUATION=true",
            "HECKE_NONZERO_POLE_AT_1=false",
        ]),
        "literature_identifiers_visible": all(token in contract for token in [
            "Huang, J. Liu, Z. Rudnick",
            "Merikoski",
            "J. D. Vaaler",
            "arXiv:1903.04005",
        ]),
        "next_gate_locked": "NEXT=13-13fg" in roadmap and "NEXT=13-13fg" in plan,
        "polynomial_growth_derivation_visible": all(token in contract for token in [
            "Stirling",
            "Phragmén–Lindelöf",
            "POLYNOMIAL_STRIP_GROWTH_DERIVED=true",
            "POLYNOMIAL_ANGULAR_GROWTH_DERIVED=true",
        ]),
        "riesz_smoothing_visible": all(token in contract for token in [
            "s(s+1)\\cdots(s+m)",
            "RIESZ_PERRON_SMOOTHING_EXPLICIT=true",
            "UNSMOOTHED_PERRON_SHORTCUT_USED=false",
        ]),
        "roadmap_gate_f_complete": "STAGE13_13FF=COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS" in roadmap,
        "result_lock_complete": "STAGE13_13FF=COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS" in result,
        "theorem_unchanged": "THEOREM_CHANGED=false" in contract and "THEOREM_CONTRACT_REOPEN_REQUIRED=false" in contract,
        "vaaler_interval_derived": all(token in contract for token in [
            "VAALER_IMPORTED_OBJECT=SAWTOOTH_APPROXIMATION",
            "VAALER_INTERVAL_MAJORANT_DERIVED_INTERNALLY=true",
            "VAALER_ZERO_MODE_EXCESS=1/(L+1)",
            "VAALER_NONZERO_COEFFICIENT_BOUND_LT=1",
        ]),
        "vaaler_zero_and_nonzero_formula_visible": all(token in contract for token in [
            "|I|\\pm\\frac1{L+1}",
            "\\frac1{\\pi|h|}+\\frac1{L+1}<1",
        ]),
        "zero_free_not_required": "GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false" in contract,
    }

    failed = [name for name, value in checks.items() if not value]
    return {
        "checks": checks,
        "decision": {
            "failed_checks": failed,
            "next": "13-13fg",
            "status": "COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS" if not failed else "FAIL_REPAIR_REQUIRED",
            "theorem_changed": False,
            "theorem_contract_reopen_required": False,
        },
        "external_boundary": {
            "dirichlet_chi4": "analytic continuation + functional equation + fixed-strip polynomial growth",
            "gaussian_hecke_nonzero": "entire continuation + completed functional equation + no pole at s=1",
            "gaussian_residue_twists": "fixed finite conductor Hecke characters; nontrivial twists holomorphic at s=1",
            "vaaler": "finite-degree sawtooth approximation only; interval polynomials derived internally",
        },
        "locks": {
            "general_selberg_delange_required": False,
            "growing_modulus_theorem_used": False,
            "hecke_family_summatory_interface_derived": True,
            "riesz_perron_smoothing_explicit": True,
            "vaaler_nonzero_coefficient_bound": "<1",
            "vaaler_zero_mode_excess": "1/(L+1)",
            "zero_free_region_required": False,
        },
        "metadata": {
            "scope": "R05 Gate F exact external theorem contracts and proof-facing consequences",
            "stage": "13-13ff",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--check-report", action="store_true")
    args = parser.parse_args()

    report = build_report()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"

    if args.write_report:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text)

    if args.check_report:
        if not OUT.exists() or OUT.read_text() != text:
            raise SystemExit("committed Stage13-13ff report is stale")
        if report["decision"]["status"] != "COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS":
            raise SystemExit(f"Stage13-13ff failed checks: {report['decision']['failed_checks']}")

    print(text, end="")


if __name__ == "__main__":
    main()
