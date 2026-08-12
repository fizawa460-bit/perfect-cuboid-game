#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT_DIR = ROOT / "stages" / "stage15" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from paired_enumerator import enumerate_paired, face_mask, is_square  # noqa: E402

STAGE14_LOCK = ROOT / "stages" / "stage14" / "data" / "14-num-alpha11-diag8" / "extended_denominator_summary.json"


def brute_force(bound: int) -> dict[tuple[int, int, int], tuple[int, bool]]:
    out: dict[tuple[int, int, int], tuple[int, bool]] = {}
    b2 = bound * bound
    for a in range(1, bound):
        for b in range(a + 1, bound):
            ab = a * a + b * b
            if ab + (b + 1) * (b + 1) > b2:
                break
            cmax = math.isqrt(b2 - ab)
            for c in range(b + 1, cmax + 1):
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                mask = face_mask(a, b, c)
                if mask.bit_count() < 2:
                    continue
                r2 = a * a + b * b + c * c
                out[(a, b, c)] = (mask, is_square(r2))
    return out


def generated_map(bound: int) -> dict[tuple[int, int, int], tuple[int, bool]]:
    exact_two, triples, _ = enumerate_paired(bound, materialize_rows=True)
    out: dict[tuple[int, int, int], tuple[int, bool]] = {}
    for row in exact_two:
        out[(row["a"], row["b"], row["c"])] = (int(row["face_mask"], 2), bool(row["space_integral"]))
    for row in triples:
        out[(row["a"], row["b"], row["c"])] = (0b111, bool(row["space_integral"]))
    return out


def main() -> None:
    small_bound = 300
    brute = brute_force(small_bound)
    generated = generated_map(small_bound)
    if generated != brute:
        missing = sorted(set(brute) - set(generated))[:10]
        extra = sorted(set(generated) - set(brute))[:10]
        changed = sorted(k for k in set(brute) & set(generated) if brute[k] != generated[k])[:10]
        raise AssertionError(f"B={small_bound} brute mismatch missing={missing} extra={extra} changed={changed}")

    _, _, summary = enumerate_paired(100_000, materialize_rows=False)
    frozen = json.loads(STAGE14_LOCK.read_text(encoding="utf-8"))
    lock = next(row for row in frozen["rows"] if row["B"] == 100_000)
    if summary["N2_direction_a_b_c"] != lock["pair"]:
        raise AssertionError(f"Stage14 direction lock mismatch: {summary['N2_direction_a_b_c']} != {lock['pair']}")
    if summary["N2_total"] != lock["N2"]:
        raise AssertionError(f"Stage14 N2 lock mismatch: {summary['N2_total']} != {lock['N2']}")
    if summary["N3_total"] != 0:
        raise AssertionError(f"Stage14 triple lock mismatch: N3={summary['N3_total']}")
    if not summary["diagnostics"]["exact_two_glue_multiplicity_one"]:
        raise AssertionError("exact-two glue multiplicity failed")
    if not summary["diagnostics"]["triple_glue_multiplicity_three"]:
        raise AssertionError("triple glue multiplicity failed")

    print("STAGE15_COMPARISON_CONTRACT_PROVED=true")
    print("BRUTE_FORCE_B300_MATCH=true")
    print("STAGE14_B100K_N2_LOCK_MATCH=true")
    print("EXACT_TWO_GLUE_MULTIPLICITY_ONE=true")
    print("TRIPLE_GLUE_MULTIPLICITY_THREE=true")
    print("PAIRED_ENUMERATOR_VALIDATED=true")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
