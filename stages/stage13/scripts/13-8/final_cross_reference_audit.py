#!/usr/bin/env python3
"""Stage13-8c final cross-reference/scope audit.

This script adds no analytic theorem.  It checks the frozen Stage12 -> Stage13
bridge ledger against the locked Stage13 constants and finite checksum, and
records the conditions required to close Task 13-8.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
STAGE13 = ROOT / "stages" / "stage13"

I = {
    "ab": 0.659705248705705,
    "ac": 0.3026997526726076,
    "bc": 0.2712955487578571,
}
P_EXPECTED = {
    "ab": 0.5347369332313988,
    "ac": 0.24535917783225203,
    "bc": 0.21990388893634913,
}

CPROJ = {"ab": 168424, "ac": 86472, "bc": 81520}
RAW = {"ab": 84212, "ac": 43236, "bc": 40760}
EXACT = {"ab": 84146, "ac": 43180, "bc": 40704}
OVERLAP = {"ab_ac": 33, "ab_bc": 33, "ac_bc": 23}
TRIPLE = 0


def close(x: float, y: float, tol: float = 5e-15) -> bool:
    return abs(x - y) <= tol


def main() -> None:
    bridge_path = STAGE13 / "data" / "13-8" / "bridge_ledger_report.json"
    final7_path = STAGE13 / "data" / "13-7" / "consolidation_audit_report.json"
    main_path = STAGE13 / "main.md"
    roadmap_path = STAGE13 / "roadmap.md"
    readme_path = STAGE13 / "README.md"
    stage12_readme = ROOT / "stages" / "stage12" / "README.md"
    stage12_final = ROOT / "stages" / "stage12" / "final.md"

    required_paths = [
        bridge_path,
        final7_path,
        main_path,
        roadmap_path,
        readme_path,
        stage12_readme,
        stage12_final,
    ]
    missing = [str(p.relative_to(ROOT)) for p in required_paths if not p.exists()]

    bridge = json.loads(bridge_path.read_text()) if bridge_path.exists() else {}
    final7 = json.loads(final7_path.read_text()) if final7_path.exists() else {}
    main_text = main_path.read_text() if main_path.exists() else ""
    stage12_readme_text = stage12_readme.read_text() if stage12_readme.exists() else ""

    p = {q: 8.0 * I[q] / math.pi**2 for q in I}
    overlap_sum = sum(OVERLAP.values())

    checks = {
        "required_sources_exist": not missing,
        "I_sum_pi2_over_8": close(sum(I.values()), math.pi**2 / 8.0),
        "P_sum_one": close(sum(p.values()), 1.0),
        "P_matches_locked_vector": all(close(p[q], P_EXPECTED[q]) for q in I),
        "directional_factor_two_exact": all(CPROJ[q] == 2 * RAW[q] for q in RAW),
        "total_factor_two_exact": sum(CPROJ.values()) == 2 * sum(RAW.values()),
        "finite_exact_one_directional_checksum": (
            EXACT["ab"] == RAW["ab"] - OVERLAP["ab_ac"] - OVERLAP["ab_bc"] + TRIPLE
            and EXACT["ac"] == RAW["ac"] - OVERLAP["ab_ac"] - OVERLAP["ac_bc"] + TRIPLE
            and EXACT["bc"] == RAW["bc"] - OVERLAP["ab_bc"] - OVERLAP["ac_bc"] + TRIPLE
        ),
        "finite_exact_one_total_checksum": (
            sum(EXACT.values())
            == sum(CPROJ.values()) // 2 - 2 * overlap_sum + 3 * TRIPLE
        ),
        "bridge_audit_reports_no_new_gap": (
            bridge.get("bridge_gap_audit", {}).get("new_mathematical_bridge_lemma_required") is False
        ),
        "stage13_7_exact_one_unconditional": (
            final7.get("status", {}).get("exact_one_directional_limit_unconditional") is True
        ),
        "stage13_7_pair_overlap_lower_order": (
            final7.get("overlap_audit", {}).get("pair_overlaps") == "o(B(log B)^3)"
        ),
        "stage13_7_triple_overlap_lower_order": (
            final7.get("overlap_audit", {}).get("triple_overlap") == "o(B(log B)^3)"
        ),
        "perfect_cuboid_nonexistence_not_assumed": (
            final7.get("final_exact_one_theorem", {}).get("perfect_cuboid_nonexistence_assumed") is False
        ),
        "main_contains_section_8": "## §8. Task 13-8" in main_text,
        "main_contains_direct_category_bridge": "\\frac12C^{\\rm proj}_{\\rm prim,q}(B)" in main_text,
        "main_contains_direct_total_bridge": "\\frac12C_{\\rm prim}(B)" in main_text,
        "stage12_is_frozen_r09": "frozen at R09" in stage12_readme_text,
        "stage12_scope_remains_oriented_only": "primitive oriented count" in stage12_readme_text,
    }

    hard_failures = [k for k, v in checks.items() if not v]
    complete = not hard_failures

    report = {
        "metadata": {
            "stage": "13-8c",
            "scope": "final cross-reference, notation, dependency and freeze-boundary audit; no new analytic theorem",
            "classification": "PASS_STAGE13_8_COMPLETE" if complete else "FAIL_REPAIR_REQUIRED",
        },
        "source_ledger": {
            "stage12_frozen_entry": "stages/stage12/README.md + stages/stage12/final.md",
            "stage13_8a_interface": "stages/stage13/data/13-8/bridge_ledger_report.json",
            "stage13_8b_canonical": "stages/stage13/main.md §8",
            "stage13_7_final": "stages/stage13/data/13-7/consolidation_audit_report.json",
        },
        "notation_ledger": {
            "C_prim": "frozen Stage12 primitive oriented distinguished-face record count",
            "C_prim_q_proj": "Stage12 primitive oriented records projecting to canonical face q",
            "A_q": "Stage13 primitive canonical raw incidence count for face q, overlaps retained",
            "O_qr": "primitive canonical pair-overlap count",
            "T": "primitive canonical three-face overlap count",
            "N_q": "primitive canonical exactly-one count in direction q",
            "P_q": "8 I_q/pi^2, the normalized chamber constant",
        },
        "exact_interface": {
            "category": "C_prim,q^proj(B)=2 A_q(B)",
            "total": "C_prim(B)=2 sum_q A_q(B)",
            "exact_one_category": "N_q(B)=A_q(B)-the two incident pair overlaps+T(B)",
            "exact_one_total": "N1(B)=C_prim(B)/2-2 sum_pair O_qr(B)+3T(B)",
        },
        "asymptotic_interface": {
            "projected_stage12": "C_prim,q^proj(B) ~ [kappa/(12 pi)] P_q B(log B)^3",
            "raw": "A_q(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3",
            "exact_one": "N_q(B)=(1/2)C_prim,q^proj(B)+o(B(log B)^3)",
            "total": "N1(B)=(1/2)C_prim(B)+o(B(log B)^3)",
        },
        "scope_boundary": {
            "stage12_reopened": False,
            "stage12_supplies": [
                "C_prim definition and primitive/oriented convention",
                "C_prim(B) ~ kappa/(12 pi) B(log B)^3",
                "kappa/eta local-factor ledger and eta=pi*kappa",
            ],
            "stage13_supplies": [
                "factor-2 canonical projection",
                "directional chamber/raw constants",
                "fixed-prime pair/triple overlap lower-order theorem",
                "exactly-one transfer",
            ],
            "independent_publication_review_completed": False,
        },
        "finite_B100000": {
            "projected_stage12": CPROJ,
            "raw": RAW,
            "pair_overlap": OVERLAP,
            "triple": TRIPLE,
            "exact_one": EXACT,
        },
        "checks": checks,
        "missing_sources": missing,
        "hard_failures": hard_failures,
        "decision": {
            "stage13_8_complete": complete,
            "new_mathematical_bridge_gap_found": False if complete else None,
            "stage12_reopened": False,
            "next": "Stage13-9 main structural theorem" if complete else "repair Stage13-8",
        },
    }

    out = STAGE13 / "data" / "13-8" / "final_cross_reference_audit_report.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["decision"], indent=2))
    if hard_failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
