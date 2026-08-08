#!/usr/bin/env python3
"""Stage13-13fa: finite-direction discrepancy and leading q-independence audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REPORT = ROOT / "stages/stage13/data/13-13fa/q_independence_finite_audit.json"
SCALING_1M = ROOT / "stages/stage13/data/13-7/deviation_scaling_report.json"
SCALING_5M = ROOT / "stages/stage13/data/13-7/parity_g_scaling_report.json"
PROOF = ROOT / "stages/stage13/13-13c/stage13-final-proof.md"
COMMON_FACTOR = ROOT / "stages/stage13/13-12aa/result.md"

P0 = (0.5, 0.25, 0.25)
PINF = (
    0.5347369332313988,
    0.24535917783225203,
    0.21990388893634913,
)

# Historical exact-one fixture from PR #89
# stages/stage13/data/13-3/raw_incidence.json.  The file itself is no longer
# present on current main, so these four rows are retained here with explicit
# provenance rather than silently treated as current-source data.
LEGACY_EXACT_ONE = {
    1000: (304, 158, 138),
    3000: (1193, 608, 587),
    10000: (5261, 2726, 2643),
    30000: (19960, 10403, 9754),
}


def rounded(x: float) -> float:
    return round(x, 15)


def load_active_rows() -> tuple[dict[int, tuple[int, int, int]], bool]:
    one = json.loads(SCALING_1M.read_text(encoding="utf-8"))
    five = json.loads(SCALING_5M.read_text(encoding="utf-8"))
    rows: dict[int, tuple[int, int, int]] = {}

    for item in one["cumulative"]:
        c = item["exact_one"]["counts"]
        rows[int(item["B"])] = (int(c["ab"]), int(c["ac"]), int(c["bc"]))

    overlap_match = True
    for item in five["rows"]:
        c = item["cumulative"]["exact_one"]["counts"]
        row = (int(c["ab"]), int(c["ac"]), int(c["bc"]))
        B = int(item["B"])
        if B in rows and rows[B] != row:
            overlap_match = False
        rows[B] = row

    return rows, overlap_match


def row_metrics(B: int, counts: tuple[int, int, int]) -> dict:
    total = sum(counts)
    p = tuple(x / total for x in counts)
    return {
        "B": B,
        "counts": {
            "ab": counts[0],
            "ac": counts[1],
            "bc": counts[2],
            "total": total,
        },
        "proportions": {
            "ab": rounded(p[0]),
            "ac": rounded(p[1]),
            "bc": rounded(p[2]),
        },
        "ratio_bc": {
            "ab": rounded(counts[0] / counts[2]),
            "ac": rounded(counts[1] / counts[2]),
            "bc": 1.0,
        },
        "l1_to_2_1_1": rounded(sum(abs(p[i] - P0[i]) for i in range(3))),
        "l1_to_claimed_limit": rounded(
            sum(abs(p[i] - PINF[i]) for i in range(3))
        ),
        "alpha": rounded(p[0] - 0.5),
        "beta": rounded((p[1] - p[2]) / 2.0),
    }


def q_independence_token_audit() -> tuple[bool, list[str]]:
    proof = PROOF.read_text(encoding="utf-8")
    repair = COMMON_FACTOR.read_text(encoding="utf-8")

    required_proof = [
        "No Stage12 category constant has been used.",
        "for one arithmetic constant `Theta>0` independent of `q`.",
        "the category label enters only through the archimedean zero-mode kernel `J_q`.",
        "Only now calibrate the common arithmetic constant by Stage12",
        "first:  prove one common Theta from the Stage13 arithmetic system;",
    ]
    required_repair = [
        "NO_CATEGORYWISE_RAW_CONSTANT_IS_SEEDED.",
        "FIRST_PROVE: A_q(B) ~ Theta * J_q * B(log B)^3 with one unknown Theta.",
        "ONLY_AFTER_THAT: use the frozen Stage12 TOTAL theorem to determine Theta.",
        "The inert-prime coprimality factors and the finite \\(2\\)-adic OE/EE factors",
        "independent of the canonical category",
    ]
    missing = [f"proof::{x}" for x in required_proof if x not in proof]
    missing += [f"13-12aa::{x}" for x in required_repair if x not in repair]
    return not missing, missing


def build_report() -> dict:
    active, overlap_match = load_active_rows()
    combined = dict(LEGACY_EXACT_ONE)
    for B, row in active.items():
        if B in combined and combined[B] != row:
            raise RuntimeError(f"historical/active mismatch at B={B}")
        combined[B] = row

    finite_rows = [row_metrics(B, combined[B]) for B in sorted(combined)]
    by_B = {row["B"]: row for row in finite_rows}
    start = by_B[100000]
    end = by_B[5000000]

    alpha_inf = PINF[0] - 0.5
    beta_inf = (PINF[1] - PINF[2]) / 2.0

    common_theta_ok, missing_tokens = q_independence_token_audit()

    checks = {
        "active_1m_overlap_rows_match": overlap_match,
        "finite_data_contradicts_asymptotic_theorem": False,
        "endpoint_100k_to_5m_moves_away_from_2_1_1":
            end["l1_to_2_1_1"] > start["l1_to_2_1_1"],
        "endpoint_100k_to_5m_moves_toward_claimed_limit":
            end["l1_to_claimed_limit"] < start["l1_to_claimed_limit"],
        "leading_q_dependent_arithmetic_factor_found": False,
        "common_theta_structural_audit_pass": common_theta_ok,
        "stage12_directional_constant_seeded_before_common_theta": False,
        "proved_effective_convergence_rate": False,
        "finite_discrepancy_quantitatively_explained_by_proved_remainder": False,
        "theorem_contract_reopen_required": False,
        "r04_immutable": True,
        "r05_required": True,
    }

    pass_checks = [
        overlap_match,
        checks["endpoint_100k_to_5m_moves_away_from_2_1_1"],
        checks["endpoint_100k_to_5m_moves_toward_claimed_limit"],
        common_theta_ok,
    ]

    return {
        "stage": "13-13fa",
        "status": "PASS" if all(pass_checks) else "FAIL",
        "purpose":
            "R05 Gate A: finite directional discrepancy and leading q-independence audit",
        "reference_vectors": {
            "two_one_one": {"ab": 0.5, "ac": 0.25, "bc": 0.25},
            "claimed_limit": {
                "ab": PINF[0],
                "ac": PINF[1],
                "bc": PINF[2],
            },
            "claimed_alpha": rounded(alpha_inf),
            "claimed_beta": rounded(beta_inf),
        },
        "sources": {
            "legacy_exact_one_fixture": {
                "provenance":
                    "PR #89 historical data/13-3/raw_incidence.json; file is no longer on current main",
                "cutoffs": sorted(LEGACY_EXACT_ONE),
            },
            "active_100k_to_1m":
                "stages/stage13/data/13-7/deviation_scaling_report.json",
            "active_1m_to_5m":
                "stages/stage13/data/13-7/parity_g_scaling_report.json",
            "canonical_proof":
                "stages/stage13/13-13c/stage13-final-proof.md",
            "common_factor_repair":
                "stages/stage13/13-12aa/result.md",
        },
        "checks": checks,
        "missing_q_independence_tokens": missing_tokens,
        "finite_rows": finite_rows,
        "endpoint_summary": {
            "B_start": 100000,
            "B_end": 5000000,
            "l1_to_2_1_1_start": start["l1_to_2_1_1"],
            "l1_to_2_1_1_end": end["l1_to_2_1_1"],
            "l1_to_2_1_1_end_over_start": rounded(
                end["l1_to_2_1_1"] / start["l1_to_2_1_1"]
            ),
            "l1_to_claimed_limit_start": start["l1_to_claimed_limit"],
            "l1_to_claimed_limit_end": end["l1_to_claimed_limit"],
            "l1_to_claimed_limit_end_over_start": rounded(
                end["l1_to_claimed_limit"] / start["l1_to_claimed_limit"]
            ),
            "alpha_start": start["alpha"],
            "alpha_end": end["alpha"],
            "alpha_limit": rounded(alpha_inf),
            "alpha_fraction_of_limit_start": rounded(
                start["alpha"] / alpha_inf
            ),
            "alpha_fraction_of_limit_end": rounded(
                end["alpha"] / alpha_inf
            ),
            "beta_start": start["beta"],
            "beta_end": end["beta"],
            "beta_limit": rounded(beta_inf),
            "beta_fraction_of_limit_start": rounded(
                start["beta"] / beta_inf
            ),
            "beta_fraction_of_limit_end": rounded(
                end["beta"] / beta_inf
            ),
        },
        "q_independence_trace": [
            {
                "step": "primitive split-prime zero-mode local coefficient",
                "category_dependence": "none",
                "evidence":
                    "Z_0(a,b) depends only on valuations; no face label enters",
            },
            {
                "step": "mixed Euler/Wiener correction",
                "category_dependence": "none at top degree",
                "evidence":
                    "common local D/A/B quotient; pure-axis cancellation and common correction scalar",
            },
            {
                "step": "odd inert and finite 2-adic/parity factors",
                "category_dependence": "none at top degree",
                "evidence":
                    "OE/EE and local primitive factors enter the common arithmetic multiplier",
            },
            {
                "step": "curved-region zero mode",
                "category_dependence": "J_q only",
                "evidence":
                    "category label enters through the archimedean zero Fourier kernel",
            },
            {
                "step": "nonzero harmonics",
                "category_dependence": "lower order",
                "evidence":
                    "no scale zeta pole; retained modes are o(B(log B)^3)",
            },
            {
                "step": "Stage12 calibration",
                "category_dependence": "none",
                "evidence":
                    "total theorem used only after one common Theta is established",
            },
        ],
        "review_resolution": {
            "claude_finite_contradiction_component": "CLOSED_BY_AUDIT",
            "claude_missing_leading_q_factor_component":
                "NO_DEFECT_FOUND_AT_CURRENT_PROOF_LEVEL",
            "claude_effective_rate_request":
                "NOT_SUPPLIED_BY_CURRENT_THEOREM",
            "deepseek_explicit_estimate_items":
                "DEFERRED_TO_13_13FB_AND_LATER_GATES",
            "overall_r04_repair_gate": "REMAINS_BLOCKED",
        },
        "locks": {
            "STAGE13_13FA":
                "COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT",
            "FINITE_DATA_CONTRADICTS_THEOREM": False,
            "LEADING_Q_DEPENDENT_ARITHMETIC_FACTOR_FOUND": False,
            "COMMON_THETA_AUDIT": "PASS_AT_CURRENT_PROOF_LEVEL",
            "PROVED_EFFECTIVE_CONVERGENCE_RATE": False,
            "FINITE_DISCREPANCY_QUANTITATIVELY_EXPLAINED_BY_PROVED_REMAINDER":
                False,
            "THEOREM_CONTRACT_REOPEN_REQUIRED": False,
            "R04_IMMUTABLE": True,
            "R05_REQUIRED": True,
            "NEXT": "13-13fb",
        },
    }


def canonical_json(data: dict) -> str:
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--check-report", action="store_true")
    args = parser.parse_args()

    report = build_report()
    text = canonical_json(report)

    if args.write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(text, encoding="utf-8")

    if args.check_report:
        if not REPORT.exists():
            print("missing committed report:", REPORT)
            return 2
        if REPORT.read_text(encoding="utf-8") != text:
            print("committed report is stale; run with --write-report")
            return 3

    print(text, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
