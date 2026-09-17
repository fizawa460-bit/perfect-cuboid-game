#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict

HMAX = 96
EXPECTED_CLASSES = 286
EXPECTED_STRICT_CLASSES = 185
EXPECTED_ORDERED_TRIPLES = 156849
EXPECTED_NONMINIMUM_TUPLES = 155916
EXPECTED_TUPLES_ABOVE_SECOND = 154989
EXPECTED_EXACT_QA_BINS = 21856
EXPECTED_MAX_QA_BINS_PER_CLASS = 628


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def main() -> None:
    classes = 0
    strict_classes = 0
    ordered_triples = 0
    nonminimum_tuples = 0
    tuples_above_second = 0
    exact_bins = 0
    max_bins = 0

    for a in range(HMAX + 1):
        hist = [defaultdict(int) for _ in range(4)]
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                support = int(x2 > 0) + int(x3 > 0) + int(x7 > 0)
                q = x2 * x2 + x3 * x3 + x7 * x7
                hist[support][q] += 1

        for support in range(4):
            if not hist[support]:
                continue
            classes += 1
            keys = sorted(hist[support])
            total = sum(hist[support].values())
            ordered_triples += total
            exact_bins += len(keys)
            max_bins = max(max_bins, len(keys))

            q0 = keys[0]
            m0 = hist[support][q0]
            req(m0 > 0, f"empty minimum bin {(a, support)}")

            if len(keys) == 1:
                # HPADJ20 and the exact histogram coincide on this class.
                req(total == m0, f"single-bin multiplicity drift {(a, support)}")
                continue

            strict_classes += 1
            q1 = keys[1]
            req(q1 > q0, f"second qA level not strict {(a, support)}")

            # HPADJ20 semantics: minimum tuples retain q0; every nonminimum
            # tuple receives q1 as a common lower bound. HPADJ21 semantics:
            # every exact qA bin is retained. Thus every exact tuple keeps the
            # same population/capacity and its refined qA is >= its HPADJ20
            # lower bound, with equality on q0/q1 and possible strict increase
            # only above q1.
            nonminimum = total - m0
            req(nonminimum > 0, f"missing nonminimum population {(a, support)}")
            nonminimum_tuples += nonminimum

            above_second = 0
            for q in keys:
                coarse_q = q0 if q == q0 else q1
                req(q >= coarse_q, f"exact qA below HPADJ20 lower bound {(a, support,q)}")
                if q > q1:
                    above_second += hist[support][q]
            tuples_above_second += above_second

    req(classes == EXPECTED_CLASSES, "class-count drift")
    req(strict_classes == EXPECTED_STRICT_CLASSES, "strict-class-count drift")
    req(ordered_triples == EXPECTED_ORDERED_TRIPLES, "ordered-triple population drift")
    req(nonminimum_tuples == EXPECTED_NONMINIMUM_TUPLES, "nonminimum population drift")
    req(tuples_above_second == EXPECTED_TUPLES_ABOVE_SECOND, "above-second population drift")
    req(exact_bins == EXPECTED_EXACT_QA_BINS, "exact-qA bin-count drift")
    req(max_bins == EXPECTED_MAX_QA_BINS_PER_CLASS, "maximum qA-bin count drift")

    # Load-bearing theorem used by the MAIN preflight:
    # for any fixed cap multiset C, S(q)=#{c in C:c>=q} is nonincreasing.
    # Since each refined tuple has q_refined >= q_HPADJ20, it has
    # S(q_refined)/B <= S(q_HPADJ20)/B for the same positive B. Population,
    # capacities and post-mass constraints are unchanged. Hence for every
    # feasible LP selection x, refined_objective(x) <= coarse_objective(x);
    # taking maxima preserves the inequality. No independence/additive
    # subtraction assumption is used.
    print("PASS: HPADJ21 exact-qA is a same-population pointwise refinement of HPADJ20 for all a<=96")
    print(f"classes={classes} strict_classes={strict_classes} ordered_triples={ordered_triples}")
    print(f"nonminimum={nonminimum_tuples} above_second={tuples_above_second} exact_qA_bins={exact_bins} max_bins={max_bins}")
    print("PASS: threshold-survivor monotonicity implies every fixed-post-mass HPADJ21 LP optimum is <= HPADJ20")
    print("ZERO_MAIN_CREDIT: structural certificate only; no FULL178 census or authority transition")


if __name__ == "__main__":
    main()
