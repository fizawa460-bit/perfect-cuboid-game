#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import csv
import json
import math
from collections import Counter
from pathlib import Path

from paired_enumerator import MASK_TO_DIRECTION, enumerate_paired, face_mask, generate_leg_index, is_square

SMALL_PRIMES = (2, 3, 5, 7, 11, 13)
DEFAULT_GRID = (1000, 2000, 5000, 10000, 20000, 50000, 100000)


def nearest_square_delta(r2: int) -> int:
    q = math.isqrt(r2)
    lower = r2 - q * q
    upper = (q + 1) * (q + 1) - r2
    return -lower if lower < upper else upper


def compact_exact_two(max_bound: int) -> list[dict]:
    """Exact Stage15 B2 rows with only the fields needed by the Stage15-3 diagnostics."""
    by_leg, _ = generate_leg_index(max_bound)
    objects: dict[tuple[int, int, int], dict[str, int]] = {}

    for shared, entries in by_leg.items():
        for i, x in enumerate(entries):
            for y in entries[i + 1 :]:
                r2 = shared * shared + x * x + y * y
                if r2 > max_bound * max_bound:
                    continue
                a, b, c = sorted((shared, x, y))
                if not (a < b < c):
                    continue
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                mask = face_mask(a, b, c)
                if mask.bit_count() < 2:
                    raise ArithmeticError(f"glued pair lost square face: {(a,b,c,mask)}")
                key = (a, b, c)
                old = objects.get(key)
                if old is None:
                    objects[key] = {"mask": mask, "R2": r2, "source_count": 1}
                else:
                    if old["mask"] != mask or old["R2"] != r2:
                        raise ArithmeticError(f"inconsistent duplicate: {key}")
                    old["source_count"] += 1

    rows: list[dict] = []
    for (a, b, c), info in objects.items():
        mask = info["mask"]
        if mask.bit_count() != 2:
            continue
        if info["source_count"] != 1:
            raise ArithmeticError(f"exact-two multiplicity failure: {(a,b,c,info['source_count'])}")
        r2 = info["R2"]
        delta = nearest_square_delta(r2)
        rows.append(
            {
                "a": a,
                "b": b,
                "c": c,
                "R2": r2,
                "space_integral": is_square(r2),
                "direction": MASK_TO_DIRECTION[mask],
                "Delta_R": delta,
                "delta_R": delta / (2.0 * math.sqrt(r2)),
            }
        )
    rows.sort(key=lambda row: (row["R2"], row["a"], row["b"], row["c"]))
    return rows


def local_slope(y0: float, y1: float, x0: float, x1: float) -> float | None:
    if y0 <= 0 or y1 <= 0:
        return None
    return math.log(y1 / y0) / math.log(x1 / x0)


def valuation_flags(n: int, p: int) -> tuple[bool, int]:
    divisible = False
    parity = 0
    while n and n % p == 0:
        n //= p
        divisible = True
        parity ^= 1
    return divisible, parity


def squareclass_signature(n: int) -> str:
    if n == 0:
        return "ZERO"
    return "".join(str(valuation_flags(n, p)[1]) for p in SMALL_PRIMES)


def quantiles(values: list[float], probs: tuple[float, ...]) -> dict[str, float]:
    ordered = sorted(values)
    if not ordered:
        return {}
    out = {}
    for p in probs:
        i = int(round(p * (len(ordered) - 1)))
        out[str(p)] = ordered[i]
    return out


def build_summary(rows: list[dict], grid: list[int], max_bound: int) -> dict:
    if not grid or max(grid) > max_bound:
        raise ValueError("grid must be nonempty and bounded by max_bound")
    r2s = [row["R2"] for row in rows]
    cumulative = []
    previous = None

    for bound in grid:
        stop = bisect.bisect_right(r2s, bound * bound)
        sub = rows[:stop]
        m2 = len(sub)
        n2 = sum(1 for row in sub if row["space_integral"])
        mdir = Counter(row["direction"] for row in sub)
        ndir = Counter(row["direction"] for row in sub if row["space_integral"])
        ratio = n2 / m2 if m2 else None
        rec = {
            "B": bound,
            "M2": m2,
            "N2": n2,
            "survival_ratio": ratio,
            "M2_direction": {d: mdir[d] for d in "abc"},
            "N2_direction": {d: ndir[d] for d in "abc"},
            "M2_over_B_logB5": m2 / (bound * math.log(bound) ** 5),
            "M2_local_loglog_slope": None,
            "N2_local_loglog_slope": None,
            "ratio_local_loglog_slope": None,
        }
        if previous is not None:
            rec["M2_local_loglog_slope"] = local_slope(previous["M2"], m2, previous["B"], bound)
            rec["N2_local_loglog_slope"] = local_slope(previous["N2"], n2, previous["B"], bound)
            if previous["survival_ratio"] and ratio:
                rec["ratio_local_loglog_slope"] = local_slope(
                    previous["survival_ratio"], ratio, previous["B"], bound
                )
        cumulative.append(rec)
        previous = rec

    deltas = [row["delta_R"] for row in rows]
    abs_deltas = [abs(x) for x in deltas]
    edges = [round(-0.5 + 0.1 * i, 1) for i in range(11)]
    hist = [0] * 10
    for x in deltas:
        i = min(9, max(0, int((x + 0.5) / 0.1)))
        hist[i] += 1

    direction = {}
    for d in "abc":
        sub = [row for row in rows if row["direction"] == d]
        direction[d] = {
            "count": len(sub),
            "N2": sum(1 for row in sub if row["space_integral"]),
            "R2_mod8": dict(sorted(Counter(row["R2"] % 8 for row in sub).items())),
            "mean_abs_normalized_defect": sum(abs(row["delta_R"]) for row in sub) / len(sub),
        }

    def prime_stats(use_delta: bool) -> dict[str, dict[str, int]]:
        out = {}
        for p in SMALL_PRIMES:
            divisible = odd = zero = 0
            for row in rows:
                n = abs(row["Delta_R"]) if use_delta else row["R2"]
                if n == 0:
                    zero += 1
                    continue
                div, parity = valuation_flags(n, p)
                divisible += int(div)
                odd += parity
            out[str(p)] = {"divisible": divisible, "odd_valuation": odd, "zero": zero}
        return out

    n2_max = sum(1 for row in rows if row["space_integral"])
    top_r2 = Counter(squareclass_signature(row["R2"]) for row in rows).most_common(12)
    top_delta = Counter(squareclass_signature(abs(row["Delta_R"])) for row in rows).most_common(12)

    summary = {
        "stage": "Stage15-3",
        "classification": "MATCHED_NUMERICAL_AB_COMPARISON",
        "common_cutoff": "R<=B",
        "max_bound": max_bound,
        "grid": cumulative,
        "max_bound_summary": {
            "M2": len(rows),
            "N2": n2_max,
            "survival_ratio": n2_max / len(rows),
            "direction": direction,
        },
        "space_defect": {
            "definition": "Delta_R=nearestSquare(R2)-R2; normalized=Delta_R/(2R)",
            "signed_quantiles": quantiles(deltas, (0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99)),
            "absolute_quantiles": quantiles(abs_deltas, (0.1, 0.25, 0.5, 0.75, 0.9, 0.99)),
            "mean_signed": sum(deltas) / len(deltas),
            "mean_absolute": sum(abs_deltas) / len(abs_deltas),
            "histogram_edges": edges,
            "histogram_counts": hist,
        },
        "local_arithmetic": {
            "R2_mod8": dict(sorted(Counter(row["R2"] % 8 for row in rows).items())),
            "abs_Delta_mod8": dict(sorted(Counter(abs(row["Delta_R"]) % 8 for row in rows).items())),
            "small_primes": list(SMALL_PRIMES),
            "R2_prime_stats": prime_stats(False),
            "abs_Delta_prime_stats": prime_stats(True),
            "squareclass_signature_note": (
                "bit j is parity of v_p for p in [2,3,5,7,11,13]; local signature only"
            ),
            "R2_top_squareclass_signatures": [
                {"signature": sig, "count": count} for sig, count in top_r2
            ],
            "abs_Delta_top_squareclass_signatures": [
                {"signature": sig, "count": count} for sig, count in top_delta
            ],
        },
        "predeclared_interpretation_gates": {
            "minimum_N2_for_global_slope_interpretation": 200,
            "minimum_N2_per_direction_for_directional_rate_interpretation": 50,
            "current_global_N2": n2_max,
            "current_directional_N2": {d: direction[d]["N2"] for d in "abc"},
            "global_slope_gate_pass": n2_max >= 200,
            "directional_rate_gate_pass": all(direction[d]["N2"] >= 50 for d in "abc"),
        },
        "claims": {
            "counts_exact_on_grid": True,
            "finite_data_only": True,
            "survival_asymptotic_inferred": False,
            "directional_survival_law_inferred": False,
        },
    }
    return summary


def crosscheck_with_stage15_1(rows: list[dict], validation_bound: int = 2000) -> None:
    _, _, old = enumerate_paired(validation_bound, materialize_rows=False)
    sub = [row for row in rows if row["R2"] <= validation_bound * validation_bound]
    m2 = len(sub)
    n2 = sum(1 for row in sub if row["space_integral"])
    if m2 != old["M2_total"] or n2 != old["N2_total"]:
        raise ArithmeticError((m2, n2, old["M2_total"], old["N2_total"]))


def assert_no_three_mod_four_prime(rows: list[dict], primes: tuple[int, ...] = (3, 7, 11, 19, 23, 31)) -> None:
    for row in rows:
        for p in primes:
            if row["R2"] % p == 0:
                raise ArithmeticError(f"primitive R2 unexpectedly divisible by {p}: {row}")


def write_tsv(path: Path, summary: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "B", "M2", "N2", "survival_ratio", "M2_local_loglog_slope", "N2_local_loglog_slope",
        "ratio_local_loglog_slope", "M2_over_B_logB5", "M2_a", "M2_b", "M2_c", "N2_a", "N2_b", "N2_c",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for rec in summary["grid"]:
            writer.writerow(
                {
                    "B": rec["B"],
                    "M2": rec["M2"],
                    "N2": rec["N2"],
                    "survival_ratio": rec["survival_ratio"],
                    "M2_local_loglog_slope": rec["M2_local_loglog_slope"],
                    "N2_local_loglog_slope": rec["N2_local_loglog_slope"],
                    "ratio_local_loglog_slope": rec["ratio_local_loglog_slope"],
                    "M2_over_B_logB5": rec["M2_over_B_logB5"],
                    "M2_a": rec["M2_direction"]["a"], "M2_b": rec["M2_direction"]["b"], "M2_c": rec["M2_direction"]["c"],
                    "N2_a": rec["N2_direction"]["a"], "N2_b": rec["N2_direction"]["b"], "N2_c": rec["N2_direction"]["c"],
                }
            )


def main() -> None:
    parser = argparse.ArgumentParser(description="Stage15-3 exact matched M2/N2 numerical comparison")
    parser.add_argument("--max-bound", type=int, default=100000)
    parser.add_argument("--grid", default=",".join(map(str, DEFAULT_GRID)))
    parser.add_argument("--json", type=Path)
    parser.add_argument("--tsv", type=Path)
    parser.add_argument("--skip-crosscheck", action="store_true")
    args = parser.parse_args()

    grid = [int(x) for x in args.grid.split(",") if x]
    rows = compact_exact_two(args.max_bound)
    if not args.skip_crosscheck:
        crosscheck_with_stage15_1(rows, min(2000, args.max_bound))
    assert_no_three_mod_four_prime(rows)
    summary = build_summary(rows, grid, args.max_bound)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.tsv:
        write_tsv(args.tsv, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
