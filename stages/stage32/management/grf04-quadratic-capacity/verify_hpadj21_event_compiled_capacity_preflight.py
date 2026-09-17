#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

# This is a zero-credit MAIN-side algorithmic preflight.  It does not consume
# the specialist result.  Instead it source-locks one retained HPADJ21 research
# boundary and checks that replacing repeated pointwise e-expansion by exact
# interval-difference compilation preserves the cell LP inputs/results on real
# FULL178 rows.

HPADJ21_HEAD = "3d4b9e190aa6d9feba596e60c8a6cecfa325b5d0"
ROW_WORKER_BLOB = "68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
PILOT_BLOB = "266c7eb92fc971df24733f651c245cd14a32e494"
HPADJ20_BLOB = "837d647cfcbc96bbe384e564f449cd7042a46d48"
TARGET_ROW_IDS = ("g0-d008", "g1-d008")


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def add_even_interval(events, survivor: int, lo: int, hi: int, count: int, excluded: set[int]) -> int:
    """Add count on every even e in [lo,hi] except excluded, by differences.

    The direct retained worker executes exactly the corresponding
    ``for e in range(lo, hi+1, 2)`` loop.  Therefore this is an exact compiler,
    not a relaxation or a new mathematical restriction.
    """
    req(lo % 2 == 0 and hi % 2 == 0 and lo <= hi, "invalid even interval")
    req(count >= 0, "negative interval multiplicity")
    if not count:
        return 0
    events[lo][survivor] += count
    events[hi + 2][survivor] -= count
    updates = 2
    for ex in excluded:
        if lo <= ex <= hi and ex % 2 == 0:
            events[ex][survivor] -= count
            events[ex + 2][survivor] += count
            updates += 2
    return updates


def materialize_caps(events, d: int):
    caps = defaultdict(int)
    if not events:
        return caps, 0
    running = defaultdict(int)
    materialized_pairs = 0
    lo = min(events)
    hi = max(events)
    req(lo % 2 == 0 and hi % 2 == 0, "event parity drift")
    for e in range(lo, hi + 1, 2):
        for survivor, delta in events.get(e, {}).items():
            running[int(survivor)] += int(delta)
            req(running[int(survivor)] >= 0, "difference compiler produced negative running mass")
        B = 19 * d - 5 * e + 1
        if B <= 0:
            continue
        for survivor, count in running.items():
            if count:
                caps[(int(survivor), int(B))] += int(count) * int(B)
                materialized_pairs += 1
    req(all(v >= 0 for v in caps.values()), "negative compiled capacity")
    return caps, materialized_pairs


def compiled_row(worker, row_index: int) -> dict:
    p = worker.load_pilot()
    h20 = p.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_main_event_preflight")
    p14 = p15.load_parent()
    counter = p14.load_counter()

    manifest = counter.load_locked_json(
        p14.MANIFEST,
        p14.LOCKS["manifest_blob"],
        p14.LOCKS["manifest_canonical"],
        "FULL178 manifest",
    )
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178, "FULL178 row coverage")
    row_id, g0, d0 = rows[row_index]
    g, d = int(g0), int(d0)
    cells, BC = p.exact_pilot_cells(p15, p14, counter, [(row_id, g, d)])
    h = d // 2
    two_profiles, _, _, _ = h20.build_two_tier_profiles(h, counter, h19)
    full_profiles, classes_gt2, tuples_above_second = p.full_profiles(h, counter, h19)

    legacy = 8 if g == 0 else 4
    K = counter.ceil_div(d - 16 * g + 16, 4)
    A = [
        [sum(mult for _, mult in full_profiles[a][sa]) for sa in range(4)]
        for a in range(h + 1)
    ]
    two_events = {interval: defaultdict(lambda: defaultdict(int)) for interval in p15.PLANNED}
    full_events = {interval: defaultdict(lambda: defaultdict(int)) for interval in p15.PLANNED}

    direct_e_tier_iterations = 0
    event_updates = 0
    accepted_tier_intervals = 0

    for b in range(h + 1):
        interval = p15.shard_for_b(b)
        for c in range(h + 1):
            bcv = BC[b][c]
            if not any(any(pair) for pair in bcv):
                continue
            c3 = counter.component3(d, b, c)
            if c3 < 0:
                continue
            two_surv, _ = h20.survivor_profiles(h16, h19, two_profiles, h, g, b, c)
            full_surv = p.full_survivors(h16, full_profiles, h, g, b, c)

            for a in range(h + 1):
                if not any(A[a]):
                    continue
                M = a + b + c
                ca = counter.component_a(d, a)
                if ca < 0:
                    continue
                srem = min(16, d) + ca + c3

                for sbc, pair in enumerate(bcv):
                    for parity in (0, 1):
                        left = int(pair[parity])
                        if not left:
                            continue
                        for sa, right in enumerate(A[a]):
                            if not right:
                                continue
                            ti = two_surv[a][sa]
                            fi = full_surv[a][sa]
                            req(ti is not None and fi is not None, "missing q profile")
                            req(sum(x[2] for x in ti["tiers"]) == int(right), "two-tier population drift")
                            req(sum(x[2] for x in fi["tiers"]) == int(right), "full-hist population drift")

                            support = sbc + sa
                            qneed = K - support
                            if qneed > 0 and srem < qneed:
                                continue
                            lower = max(legacy, K, d - 4 * g + 4, M, M + max(0, qneed))
                            upper = min((19 * d) // 5, 3 * d, 3 * d - (b - c))
                            if lower > upper:
                                continue
                            excluded = set()
                            e_n358 = 3 * d - (b - c)
                            if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                                excluded.add(e_n358)
                            if g == 1 and d == 8:
                                excluded.add(8)
                            lo = lower if lower % 2 == 0 else lower + 1
                            hi = upper if upper % 2 == 0 else upper - 1
                            if lo > hi:
                                continue
                            valid_e_count = (hi - lo) // 2 + 1
                            valid_e_count -= sum(1 for ex in excluded if lo <= ex <= hi and ex % 2 == 0)
                            req(valid_e_count >= 0, "negative valid-e count")

                            for tiers, target in ((ti["tiers"], two_events[interval]), (fi["tiers"], full_events[interval])):
                                for s0, s1, mult in tiers:
                                    survivor = int(s0 if parity == 0 else s1)
                                    count = left * int(mult)
                                    if not count:
                                        continue
                                    direct_e_tier_iterations += valid_e_count
                                    event_updates += add_even_interval(
                                        target, survivor, lo, hi, count, excluded
                                    )
                                    accepted_tier_intervals += 1

    two_total = Fraction(0, 1)
    full_total = Fraction(0, 1)
    two_floor = 0
    full_floor = 0
    strict_cells = 0
    records = []
    materialized_pairs = 0

    for interval_position, interval in enumerate(p15.PLANNED):
        two_caps, n1 = materialize_caps(two_events[interval], d)
        full_caps, n2 = materialize_caps(full_events[interval], d)
        materialized_pairs += n1 + n2
        key = (interval, g, d)
        info = cells[key]
        P = int(info["pre_mass"])
        Mpost = int(info["post_mass"])
        req(sum(two_caps.values()) == P, f"compiled two-tier pre-mass mismatch {key}")
        req(sum(full_caps.values()) == P, f"compiled full-hist pre-mass mismatch {key}")
        tobj, _, _, _ = h18.optimize_cell_exact_predomain(two_caps, Mpost)
        fobj, _, _, _ = h18.optimize_cell_exact_predomain(full_caps, Mpost)
        req(fobj <= tobj, f"compiled full histogram weakened HPADJ20 {key}")
        strict = fobj < tobj
        strict_cells += int(strict)
        two_total += tobj
        full_total += fobj
        tf = tobj.numerator // tobj.denominator
        ff = fobj.numerator // fobj.denominator
        two_floor += tf
        full_floor += ff
        records.append(
            {
                "interval_position": interval_position,
                "pre_mass": P,
                "post_mass": Mpost,
                "hpadj20_num": tobj.numerator,
                "hpadj20_den": tobj.denominator,
                "hpadj20_floor": tf,
                "hpadj21_num": fobj.numerator,
                "hpadj21_den": fobj.denominator,
                "hpadj21_floor": ff,
                "strict": strict,
            }
        )

    return {
        "row": {"index": row_index, "row_id": row_id, "g": g, "d": d},
        "profile": {
            "classes_with_more_than_two_qA_bins": classes_gt2,
            "tuples_above_second_qA_level": tuples_above_second,
        },
        "totals": {
            "hpadj20_rational_num": two_total.numerator,
            "hpadj20_rational_den": two_total.denominator,
            "hpadj21_rational_num": full_total.numerator,
            "hpadj21_rational_den": full_total.denominator,
            "hpadj20_cellwise_floor_sum": two_floor,
            "hpadj21_cellwise_floor_sum": full_floor,
            "strict_cell_count": strict_cells,
            "floor_improvement": two_floor - full_floor,
        },
        "cell_records": records,
        "compiler_accounting": {
            "direct_e_tier_iterations_replaced": direct_e_tier_iterations,
            "difference_event_updates": event_updates,
            "accepted_tier_intervals": accepted_tier_intervals,
            "materialized_survivor_e_pairs": materialized_pairs,
        },
    }


def normalized_direct(d: dict) -> dict:
    return {
        "row": d["row"],
        "profile": {
            "classes_with_more_than_two_qA_bins": d["profile"]["classes_with_more_than_two_qA_bins"],
            "tuples_above_second_qA_level": d["profile"]["tuples_above_second_qA_level"],
        },
        "totals": {
            k: d["totals"][k]
            for k in (
                "hpadj20_rational_num",
                "hpadj20_rational_den",
                "hpadj21_rational_num",
                "hpadj21_rational_den",
                "hpadj20_cellwise_floor_sum",
                "hpadj21_cellwise_floor_sum",
                "strict_cell_count",
                "floor_improvement",
            )
        },
        "cell_records": [
            {
                k: r[k]
                for k in (
                    "interval_position",
                    "pre_mass",
                    "post_mass",
                    "hpadj20_num",
                    "hpadj20_den",
                    "hpadj20_floor",
                    "hpadj21_num",
                    "hpadj21_den",
                    "hpadj21_floor",
                    "strict",
                )
            }
            for r in d["cell_records"]
        ],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, required=True)
    args = ap.parse_args()
    root = args.source_root.resolve()
    row_worker = root / "stages/stage32-ex5/hpadj-21_ex5/run_full_hist_row.py"
    pilot = root / "stages/stage32-ex5/hpadj-21_ex5/strictness_pilot_bounded_exact.py"
    hpadj20 = root / "stages/stage32-ex5/hpadj-20_ex5/derive_two_tier_qa_predomain_picard_lp_bound.py"

    # Fail closed before importing any retained specialist producer.
    req(row_worker.is_file() and git_blob(row_worker) == ROW_WORKER_BLOB, "retained HPADJ21 row-worker drift")
    req(pilot.is_file() and git_blob(pilot) == PILOT_BLOB, "retained HPADJ21 pilot drift")
    req(hpadj20.is_file() and git_blob(hpadj20) == HPADJ20_BLOB, "retained HPADJ20 parent drift")
    worker = load_module(row_worker, "main_hpadj21_retained_row_worker")

    # Resolve row indices from the source-locked manifest rather than assuming
    # manifest ordering.
    p = worker.load_pilot()
    h20 = p.load_parent(); h19 = h20.load_parent(); h18 = h19.load_parent(); h17 = h18.load_parent(); h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_main_event_index")
    p14 = p15.load_parent(); counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    index_by_id = {str(row_id): i for i, (row_id, _g, _d) in enumerate(rows)}
    req(all(row_id in index_by_id for row_id in TARGET_ROW_IDS), "bounded real-row target missing")

    results = []
    for row_id in TARGET_ROW_IDS:
        idx = index_by_id[row_id]
        direct = worker.compute_row(idx)
        compiled = compiled_row(worker, idx)
        req(normalized_direct(direct) == {k: compiled[k] for k in ("row", "profile", "totals", "cell_records")},
            f"event-compiled capacity mismatch on {row_id}")
        acc = compiled["compiler_accounting"]
        req(acc["direct_e_tier_iterations_replaced"] > 0, f"empty direct expansion accounting {row_id}")
        req(acc["difference_event_updates"] > 0, f"empty event accounting {row_id}")
        results.append({
            "row_id": row_id,
            "row_index": idx,
            "floor_improvement": compiled["totals"]["floor_improvement"],
            "strict_cell_count": compiled["totals"]["strict_cell_count"],
            **acc,
        })

    out = {
        "schema": "STAGE32_MAIN_HPADJ21_EVENT_COMPILED_CAPACITY_PREFLIGHT_V1",
        "status": "BOUNDED_REAL_ROWS_EXACT_EQUIVALENCE_PASS__ZERO_MAIN_CREDIT",
        "source_boundary": {
            "hpadj21_exact_head": HPADJ21_HEAD,
            "row_worker_blob_sha1": ROW_WORKER_BLOB,
            "bounded_pilot_blob_sha1": PILOT_BLOB,
            "hpadj20_parent_blob_sha1": HPADJ20_BLOB,
        },
        "compiler_identity": "For each fixed survivor tier, direct addition on every even e in an admissible interval equals a +count event at lo and -count event at hi+2, with excluded even points represented by -count/+count point events. Materializing the prefix sums therefore gives the identical (survivor,B) capacity multiset.",
        "bounded_real_row_results": results,
        "next_exact_step": "Use this exact event compiler in a separately partitioned FULL178 numerical replay; keep source locks, no-additive-subtraction semantics, resume-first evidence, and hostile-audit gate.",
        "semantics": {
            "population_changed": False,
            "post_mass_changed": False,
            "lp_objective_changed": False,
            "new_pruning_claimed": False,
            "full178_replay_run": False,
            "main_credit_changed": False,
            "theorem_credit_changed": False,
            "effectivity_credit_changed": False,
            "endpoint_credit_changed": False,
            "merge_authorized": False,
        },
    }
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
