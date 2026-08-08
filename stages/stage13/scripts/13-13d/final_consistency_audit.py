#!/usr/bin/env python3
"""Stage13-13d deterministic final consistency audit."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PROOF = ROOT / "stages/stage13/13-13c/stage13-final-proof.md"
ROADMAP = ROOT / "stages/stage13/13-13/roadmap.md"
REPORT = ROOT / "stages/stage13/data/13-13d/final_consistency_audit.json"

LOCKED_I = {
    "ab": 0.659705248705705,
    "ac": 0.3026997526726076,
    "bc": 0.2712955487578571,
}
LOCKED_P = {
    "ab": 0.5347369332313988,
    "ac": 0.24535917783225203,
    "bc": 0.21990388893634913,
}
SIMPSON_N = 200
TOL = 1e-9


def simpson(f, a: float, b: float, n: int = SIMPSON_N) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return total * h / 3.0


def theta_max(phi: float) -> float:
    return math.atan(1.0 / math.sin(phi))


def chamber_integral(kind: str) -> float:
    lo, hi = math.pi / 4.0, math.pi / 2.0
    if kind == "ab":
        return simpson(theta_max, lo, hi)

    def outer(phi: float) -> float:
        tm = theta_max(phi)
        cp, sp = math.cos(phi), math.sin(phi)

        def inner(theta: float) -> float:
            st, ct = math.sin(theta), math.cos(theta)
            leg = cp if kind == "ac" else sp
            denom = math.sqrt((st * leg) ** 2 + ct**2)
            return st / denom

        return simpson(inner, 0.0, tm)

    return simpson(outer, lo, hi)


def square_or_zero(a: int, p: int) -> bool:
    a %= p
    return a == 0 or pow(a, (p - 1) // 2, p) == 1


def inert_unit_check(p: int) -> dict:
    circle = [
        (x, y)
        for x in range(p)
        for y in range(p)
        if (x * x + y * y - 1) % p == 0
    ]
    hyperbola = [
        (z, d)
        for z in range(p)
        for d in range(p)
        if (d * d - z * z - 1) % p == 0
    ]
    accepted = sum(
        1
        for x, _y in circle
        for z, _d in hyperbola
        if square_or_zero(x * x + z * z, p)
    )
    expected_total = p * p - 1
    expected_accepted = (p + 1) ** 2 // 2
    alpha = (p + 1) / (2 * (p - 1))
    lam = (p + 5) / (2 * (p + 1))
    return {
        "p": p,
        "total": len(circle) * len(hyperbola),
        "expected_total": expected_total,
        "accepted": accepted,
        "expected_accepted": expected_accepted,
        "alpha_p": round(alpha, 15),
        "lambda_p": round(lam, 15),
        "pass": (
            len(circle) == p + 1
            and len(hyperbola) == p - 1
            and len(circle) * len(hyperbola) == expected_total
            and accepted == expected_accepted
            and (p < 7 or lam <= 0.75)
        ),
    }


def require_tokens(text: str, tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in text]


def build_report() -> dict:
    proof = PROOF.read_text(encoding="utf-8")
    roadmap = ROADMAP.read_text(encoding="utf-8")

    i_vals = {q: chamber_integral(q) for q in ("ab", "ac", "bc")}
    p_vals = {q: 8.0 * i_vals[q] / math.pi**2 for q in i_vals}
    j_vals = {q: 2.0 * i_vals[q] / math.pi for q in i_vals}

    chamber_ok = (
        all(abs(i_vals[q] - LOCKED_I[q]) < TOL for q in i_vals)
        and abs(sum(i_vals.values()) - math.pi**2 / 8.0) < TOL
    )
    direction_ok = (
        all(abs(p_vals[q] - LOCKED_P[q]) < TOL for q in p_vals)
        and abs(sum(p_vals.values()) - 1.0) < TOL
    )
    jq_ok = abs(sum(j_vals.values()) - math.pi / 4.0) < TOL

    bridge = {
        "B": 100000,
        "stage12_projected": [168424, 86472, 81520],
        "raw_incidence": [84212, 43236, 40760],
        "raw_total": 168208,
        "pair_overlap_total": 89,
        "triple_overlap": 0,
        "exactly_one": [84146, 43180, 40704],
        "exactly_one_total": 168030,
    }
    bridge_ok = (
        all(
            bridge["stage12_projected"][i] == 2 * bridge["raw_incidence"][i]
            for i in range(3)
        )
        and sum(bridge["raw_incidence"]) == bridge["raw_total"]
        and sum(bridge["exactly_one"]) == bridge["exactly_one_total"]
        and 2 * bridge["raw_total"] == sum(bridge["stage12_projected"])
        and bridge["exactly_one_total"]
        == bridge["raw_total"]
        - 2 * bridge["pair_overlap_total"]
        + 3 * bridge["triple_overlap"]
    )

    theorem_tokens = [
        "RAW_DIRECTIONAL=A_q(B) ~ kappa*I_q/(3*pi^3) B(log B)^3",
        "PAIR_OVERLAP=O_qr(B)=o(B(log B)^3)",
        "TRIPLE_OVERLAP=T(B)=o(B(log B)^3)",
        "EXACT_ONE_DIRECTIONAL=N_q(B) ~ kappa*I_q/(3*pi^3) B(log B)^3",
        "EXACT_ONE_TOTAL=N1(B) ~ kappa/(24*pi) B(log B)^3",
        "DIRECTION_LIMIT=P_q=8*I_q/pi^2",
        "CHAMBER_SUM=sum I_q=pi^2/8",
        "JQ_BRIDGE=J_q=2*I_q/pi",
        "INERT_LOCAL_MULTIPLIER=lambda_p=(p+5)/(2*(p+1))",
        "NO_PERFECT_CUBOID_NONEXISTENCE_ASSUMPTION=true",
    ]
    missing_theorem_tokens = require_tokens(proof, theorem_tokens)

    provenance_marker = "## 18. Provenance and supersession"
    core = proof.split(provenance_marker, 1)[0]
    stale_tokens = [
        "Stage13-7jb",
        "Stage13-7jf",
        "D_q/K_q",
        "lambda_p<=1/2+O(1/p)",
        "lambda_p\\le1/2+O(1/p)",
    ]
    stale_core_hits = [token for token in stale_tokens if token in core]

    roadmap_tokens = [
        "STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT",
        "CANONICAL_CONSTANTS_REPRODUCED=true",
        "STALE_SUPERSEDED_FORMULAS_IN_CANONICAL_FILES=0",
        "NEXT=13-13e",
    ]
    missing_roadmap_tokens = require_tokens(roadmap, roadmap_tokens)

    inert_checks = [inert_unit_check(p) for p in (7, 11, 19, 23)]
    inert_ok = all(item["pass"] for item in inert_checks)

    checks = {
        "chamber_integrals": chamber_ok,
        "normalized_direction_vector": direction_ok,
        "jq_bridge": jq_ok,
        "finite_bridge_B100000": bridge_ok,
        "inert_unit_character_counts": inert_ok,
        "canonical_theorem_lock_tokens": not missing_theorem_tokens,
        "superseded_formula_core_scan": not stale_core_hits,
        "roadmap_completion_lock": not missing_roadmap_tokens,
    }
    passed = all(checks.values())

    return {
        "stage": "13-13d",
        "status": "PASS" if passed else "FAIL",
        "simpson_n": SIMPSON_N,
        "tolerance": TOL,
        "checks": checks,
        "chamber_integrals": {q: round(i_vals[q], 15) for q in i_vals},
        "locked_chamber_integrals": LOCKED_I,
        "chamber_sum": round(sum(i_vals.values()), 15),
        "pi2_over_8": round(math.pi**2 / 8.0, 15),
        "direction_vector": {q: round(p_vals[q], 15) for q in p_vals},
        "locked_direction_vector": LOCKED_P,
        "direction_sum": round(sum(p_vals.values()), 15),
        "jq": {q: round(j_vals[q], 15) for q in j_vals},
        "jq_sum": round(sum(j_vals.values()), 15),
        "pi_over_4": round(math.pi / 4.0, 15),
        "finite_bridge_B100000": bridge,
        "inert_local_checks": inert_checks,
        "missing_theorem_tokens": missing_theorem_tokens,
        "stale_superseded_core_hits": stale_core_hits,
        "missing_roadmap_tokens": missing_roadmap_tokens,
        "canonical_constants_reproduced": chamber_ok
        and direction_ok
        and jq_ok
        and inert_ok,
        "stale_superseded_formulas_in_canonical_files": len(stale_core_hits),
        "theorem_changed": False,
        "next": "13-13e",
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
        committed = REPORT.read_text(encoding="utf-8")
        if committed != text:
            print("committed report is stale; run with --write-report")
            return 3

    print(text, end="")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
