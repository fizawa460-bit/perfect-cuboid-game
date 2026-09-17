#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "HPADJ21-KNOWN-STRICT-SUBSET-MAIN-PREFLIGHT.json"

CURRENT = 179119009547804181594
LOW = [
    (140762240, 136851462),
    (131566445, 128162327),
    (11900366, 11784236),
    (11097422, 10976320),
    (43219165, 42512379),
    (40225506, 39592140),
]
HIGH = 1312541087822068106
EXPECTED_LOW = 8892280
EXPECTED_GAIN = 1312541087830960386
EXPECTED_BOUND = 177806468459973221208


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def greedy(cap: dict[Fraction, int], mass: int) -> Fraction:
    req(0 <= mass <= sum(cap.values()), "mass outside capacity")
    rem = mass
    out = Fraction(0, 1)
    for ratio, amount in sorted(cap.items(), reverse=True):
        take = min(rem, amount)
        out += ratio * take
        rem -= take
        if rem == 0:
            break
    req(rem == 0, "greedy did not cover mass")
    return out


def check_generic_downshift_monotonicity() -> None:
    # Exact finite sanity-check of the load-bearing LP order: splitting capacity at
    # one ratio into capacity at equal/lower ratios cannot increase the greedy
    # fixed-mass maximum.  The mathematical reason is tail-capacity dominance;
    # these exhaustive small cases protect the implementation convention.
    ratios = [Fraction(0), Fraction(1, 7), Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1)]
    for i, coarse_ratio in enumerate(ratios):
        lower = ratios[: i + 1]
        for total in range(1, 8):
            for moved in range(total + 1):
                for low_ratio in lower:
                    coarse = {coarse_ratio: total}
                    refined: dict[Fraction, int] = {}
                    refined[coarse_ratio] = total - moved
                    refined[low_ratio] = refined.get(low_ratio, 0) + moved
                    for mass in range(total + 1):
                        req(greedy(refined, mass) <= greedy(coarse, mass), "downshift monotonicity regression")


def main() -> None:
    data = json.loads(CERT.read_text())
    req(data["schema"] == "STAGE32_MAIN_HPADJ21_KNOWN_STRICT_SUBSET_PREFLIGHT_V1", "schema drift")
    req(data["status"].endswith("ZERO_MAIN_CREDIT"), "credit firewall drift")
    req(data["current_authority"]["authoritative_remaining_terminals"] == CURRENT, "V41 authority drift")
    req(data["structural_monotonicity"]["population_change"] is False, "population change forbidden")
    req(data["structural_monotonicity"]["post_mass_change"] is False, "post-mass change forbidden")
    req(data["structural_monotonicity"]["same_picard_character"] is True, "character drift")
    req(data["structural_monotonicity"]["additive_independence_assumed"] is False, "independence assumption forbidden")

    low = sum(a - b for a, b in LOW)
    req(low == EXPECTED_LOW, "low-d arithmetic drift")
    rows = data["measured_strict_subset"]["bounded_low_d_cells"]
    req(len(rows) == len(LOW), "low-d witness count drift")
    req(sum(int(r["floor_improvement"]) for r in rows) == EXPECTED_LOW, "retained low-d sum drift")
    req(data["measured_strict_subset"]["bounded_low_d_floor_improvement_sum"] == EXPECTED_LOW, "low-d retained total drift")

    high = int(data["measured_strict_subset"]["near_max_row"]["floor_improvement_vs_hpadj20"])
    req(high == HIGH, "near-max row improvement drift")
    gain = low + high
    req(gain == EXPECTED_GAIN, "known strict-subset gain drift")
    req(data["measured_strict_subset"]["known_measured_floor_improvement_sum"] == EXPECTED_GAIN, "retained gain drift")
    req(CURRENT - gain == EXPECTED_BOUND, "candidate-bound arithmetic drift")
    req(data["candidate"]["candidate_upper_bound"] == EXPECTED_BOUND, "candidate bound drift")
    req(data["candidate"]["candidate_tightening_vs_v41"] == EXPECTED_GAIN, "candidate tightening drift")
    req(data["candidate"]["full178_numeric_replay_complete"] is False, "must remain pre-full178")
    req(data["candidate"]["all_other_cells_conservatively_left_at_hpadj20"] is True, "unmeasured-cell firewall drift")
    req(data["candidate"]["exact_rejected_identity_set_claimed"] is False, "identity-set claim forbidden")

    fw = data["firewalls"]
    for k in (
        "stage32_main_pruning_credit", "current_main_incremental_credit", "full178_complete",
        "effectivity_credit", "receiver_credit", "theorem_credit", "endpoint_credit",
        "perfect_cuboid_credit", "merge_authorized",
    ):
        req(fw[k] is False, f"firewall opened: {k}")

    check_generic_downshift_monotonicity()
    print(f"PASS: HPADJ21 known-strict subset MAIN preflight; candidate={EXPECTED_BOUND}; tightening={EXPECTED_GAIN}; zero MAIN credit")


if __name__ == "__main__":
    main()
