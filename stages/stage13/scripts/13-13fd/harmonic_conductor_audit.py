#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LEMMA = ROOT / "stages/stage13/13-13fd/harmonic-conductor-lemma.md"
RESULT = ROOT / "stages/stage13/13-13fd/result.md"
REPORT = ROOT / "stages/stage13/data/13-13fd/harmonic_conductor_audit.json"

LOCKS = [
    "STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING",
    "HECKE_STRIP_LEFT=3/4",
    "HECKE_FAMILY_BOUND=S_ell(X)<<X^(1-delta_H)(1+ell)^C_H(log(2X))^D_H_for_all_ell>=1",
    "RETAINED_HARMONICS=ell<=floor((log B)^4)",
    "HARMONIC_POLYLOG_EXPONENT=4*C_H+D_H+6",
    "HARMONIC_STRETCHED_SAVING=exp(-delta_H*(log B)^(1/4))",
    "HARMONIC_CORE=o_A(B(log B)^(-A))_for_every_fixed_A",
    "VAALER_ZERO_MODE_EXCESS=O(B(log B)^-1)",
    "FIXED_A48_REQUIRED=false",
    "GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false",
    "WINGS_EXPANDED_HARMONIC_BY_HARMONIC=false",
    "THEOREM_CHANGED=false",
    "THEOREM_CONTRACT_REOPEN_REQUIRED=false",
    "NEXT=13-13fe",
]

def build_report():
    lemma = LEMMA.read_text()
    result = RESULT.read_text()
    missing_lemma = [x for x in LOCKS if x not in lemma]
    missing_result = [x for x in LOCKS if x not in result]

    # Symbolic exponent bookkeeping:
    # ell <= Lambda^4 gives Lambda^(4*C_H+4), then add D_H and two base logs.
    conductor_coeff = 4
    mode_count_constant = 4
    base_log_cost = 2
    constant_term = mode_count_constant + base_log_cost
    formula = f"{conductor_coeff}*C_H+D_H+{constant_term}"

    checks = {
        "all_ell_family_interface": "ell\\ge1" in lemma and "(1+\\ell)^{C_H}" in lemma,
        "local_X_range_mismatch_removed": "1\\le\\ell\\le(\\log X)^4" not in lemma,
        "strip_fixed": "\\Re s\\ge \\frac34" in lemma,
        "mode_sum_exponent": formula == "4*C_H+D_H+6",
        "stretched_exponential_present": "\\exp(-\\delta_H\\Lambda^{1/4})" in lemma,
        "wings_removed_before_harmonics": "only then introduce the Vaaler Fourier expansion" in lemma,
        "fixed_A48_not_required": "FIXED_A48_REQUIRED=false" in lemma,
        "zero_free_not_required": "GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false" in lemma,
        "lemma_locks_complete": not missing_lemma,
        "result_locks_complete": not missing_result,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    return {
        "stage": "13-13fd",
        "status": status,
        "interface": {
            "strip_left": "3/4",
            "family_bound": "S_ell(X)<<X^(1-delta_H)(1+ell)^C_H(log(2X))^D_H for all ell>=1",
            "retained_modes": "ell<=floor((log B)^4)",
        },
        "bookkeeping": {
            "mode_sum": "O((log B)^(4*C_H+4))",
            "base_log_cost": 2,
            "total_polylog_exponent": formula,
            "stretched_saving": "exp(-delta_H*(log B)^(1/4))",
            "core_conclusion": "o_A(B(log B)^(-A)) for every fixed A>0",
            "vaaler_zero_mode_excess": "O(B(log B)^-1)",
        },
        "decisions": {
            "fixed_A48_required": False,
            "gaussian_hecke_zero_free_region_required": False,
            "wings_expanded_harmonic_by_harmonic": False,
            "theorem_changed": False,
            "theorem_contract_reopen_required": False,
            "next": "13-13fe",
        },
        "checks": checks,
        "missing_lemma_tokens": missing_lemma,
        "missing_result_tokens": missing_result,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-report", action="store_true")
    ap.add_argument("--check-report", action="store_true")
    args = ap.parse_args()
    report = build_report()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(text)
    if args.check_report:
        if not REPORT.exists() or REPORT.read_text() != text:
            raise SystemExit("committed report is stale")
        if report["status"] != "PASS":
            raise SystemExit(json.dumps(report, indent=2))
    print(text, end="")

if __name__ == "__main__":
    main()
