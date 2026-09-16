#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PRODUCER = HERE / "derive_two_tier_qa_predomain_picard_lp_bound.py"
PRODUCER_BLOB = "837d647cfcbc96bbe384e564f449cd7042a46d48"
SCHEMA = "STAGE32EX5_HPADJ20_ROW_SHARD_CERT_V1"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_producer():
    req(PRODUCER.is_file() and git_blob(PRODUCER) == PRODUCER_BLOB, "HPADJ20 producer blob drift")
    spec = importlib.util.spec_from_file_location("hpadj20_locked_for_row_shard", PRODUCER)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ20 producer")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def deterministic_partition(rows: list[tuple], shard_count: int) -> tuple[list[list[tuple]], list[int]]:
    """Greedy deterministic partition by a conservative cubic row-cost proxy."""
    req(shard_count > 0, "shard_count must be positive")
    buckets: list[list[tuple]] = [[] for _ in range(shard_count)]
    loads = [0 for _ in range(shard_count)]
    weighted = []
    for row_index, row in enumerate(rows):
        row_id, g, d = row
        h = int(d) // 2
        weight = (h + 1) ** 3
        weighted.append((weight, row_index, row_id, g, d))
    for weight, row_index, row_id, g, d in sorted(weighted, key=lambda x: (-x[0], x[1])):
        target = min(range(shard_count), key=lambda i: (loads[i], i))
        buckets[target].append((row_index, row_id, int(g), int(d)))
        loads[target] += weight
    for bucket in buckets:
        bucket.sort(key=lambda x: x[0])
    flattened = sorted(x[0] for bucket in buckets for x in bucket)
    req(flattened == list(range(len(rows))), "partition coverage drift")
    return buckets, loads


def assignment_digest(bucket: list[tuple], shard_index: int, shard_count: int) -> str:
    payload = {
        "shard_index": shard_index,
        "shard_count": shard_count,
        "rows": [list(x) for x in bucket],
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_context():
    p20 = load_producer()
    h19 = p20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    cells, p14 = h17.exact_cells(h16)
    counter = p14.load_counter()
    req(h19.Q_BENCHMARK == p20.Q_BENCHMARK, "HPADJ19 q benchmark drift")
    req(h19.HPADJ15_BENCHMARK == p20.HPADJ15_BENCHMARK, "HPADJ19 HPADJ15 benchmark drift")
    req(p14.EXPECTED_SURVIVOR_ENVELOPE == 6703403803993209250491, "survivor envelope drift")
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178, "FULL178 row coverage")
    H = max(d // 2 for _, _, d in rows)
    req(H == 96, "FULL178 hmax drift")
    BC = counter.build_bc_exact_parity(H)
    profiles, hist_classes, strict_profile_classes, nonminimum_tuples = p20.build_two_tier_profiles(H, counter, h19)
    return p20, h19, h18, h17, h16, cells, p14, counter, rows, BC, profiles, (
        hist_classes, strict_profile_classes, nonminimum_tuples
    )


def cheap_validate_certificate(path: Path, shard_index: int, shard_count: int) -> dict:
    req(path.is_file(), f"missing certificate {path}")
    data = json.loads(path.read_text())
    req(data.get("schema") == SCHEMA, "shard certificate schema drift")
    req(int(data.get("shard_index", -1)) == shard_index, "shard certificate index drift")
    req(int(data.get("shard_count", -1)) == shard_count, "shard certificate count drift")
    locks = data.get("source_locks", {})
    req(locks.get("hpadj20_producer_git_blob") == PRODUCER_BLOB, "shard producer lock drift")
    req(locks.get("row_shard_worker_git_blob") == git_blob(Path(__file__)), "shard worker lock drift")
    req(data.get("canonical_sha256_without_this_field") == canonical(data), "shard certificate canonical drift")
    rows = data.get("assignment", {}).get("rows", [])
    req(rows and len({int(x[0]) for x in rows}) == len(rows), "shard assignment duplicate/empty drift")
    req(data["assignment"].get("sha256") == assignment_digest(
        [tuple(x) for x in rows], shard_index, shard_count
    ), "shard assignment digest drift")
    return data


def compute_shard(shard_index: int, shard_count: int) -> dict:
    (
        p20, h19, h18, _h17, h16, cells, p14, counter, rows, BC, profiles, profile_meta
    ) = load_context()
    buckets, loads = deterministic_partition(rows, shard_count)
    req(0 <= shard_index < shard_count, "shard_index out of range")
    assigned = buckets[shard_index]
    req(assigned, "empty shard assignment")

    total_obj = Fraction(0, 1)
    parent_total_obj = Fraction(0, 1)
    cell_floor_sum = 0
    parent_cell_floor_sum = 0
    total_pre_terms = 0
    total_pre_blocks = 0
    positive_q_capacity = 0
    parent_positive_q_capacity = 0
    nonzero_post_cells = 0
    strict_survivor_tiers = 0
    strict_cell_count = 0
    diagnostic_records = []
    seen = set()
    started = time.monotonic()

    for local_pos, (row_index, row_id, g, d) in enumerate(assigned, 1):
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = counter.ceil_div(d - 16 * g + 16, 4)
        A = [[sum(mult for _, mult in profiles[a][sa]) for sa in range(4)] for a in range(h + 1)]
        req(all(A[a][sa] == counter.triple_free_count(a, sa) for a in range(h + 1) for sa in range(4)),
            f"A profile population mismatch row {row_id}")
        cell_caps = {interval: defaultdict(int) for interval in h18.PLANNED}
        parent_caps = {interval: defaultdict(int) for interval in h18.PLANNED}
        cell_blocks = {interval: 0 for interval in h18.PLANNED}

        for b in range(h + 1):
            interval = h16.shard_for_b(b)
            for c in range(h + 1):
                bcv = BC[b][c]
                if not any(any(pair) for pair in bcv):
                    continue
                c3 = counter.component3(d, b, c)
                if c3 < 0:
                    continue
                qsurv, strict_here = p20.survivor_profiles(h16, h19, profiles, h, g, b, c)
                strict_survivor_tiers += strict_here

                for a in range(h + 1):
                    avec = A[a]
                    if not any(avec):
                        continue
                    M = a + b + c
                    ca = counter.component_a(d, a)
                    if ca < 0:
                        continue
                    srem = min(16, d) + ca + c3

                    for sbc, pair in enumerate(bcv):
                        for r in (0, 1):
                            left_count = int(pair[r])
                            if not left_count:
                                continue
                            for sa, right_total in enumerate(avec):
                                if not right_total:
                                    continue
                                qinfo = qsurv[a][sa]
                                req(qinfo is not None, f"missing q profile {(a,sa)}")
                                req(sum(v[2] for v in qinfo["tiers"]) == int(right_total),
                                    f"q tier population mismatch {(a,sa)}")
                                parent_q = int(qinfo["parent"][r])
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
                                for e in range(lo, hi + 1, 2):
                                    if e in excluded:
                                        continue
                                    B = 19 * d - 5 * e + 1
                                    req(B > 0 and B % 2 == 1, f"normal block drift {(g,d,e,B)}")
                                    req(B - 1 >= 8 * h, f"q interval domain too short {(g,d,e,B)}")
                                    parent_count = left_count * int(right_total)
                                    cell_blocks[interval] += parent_count
                                    parent_caps[interval][(parent_q, B)] += parent_count * B
                                    tier_count = 0
                                    for s0, s1, mult in qinfo["tiers"]:
                                        q_s = s0 if r == 0 else s1
                                        count = left_count * int(mult)
                                        tier_count += count
                                        cell_caps[interval][(int(q_s), B)] += count * B
                                    req(tier_count == parent_count, "two-tier block population drift")

        for interval_pos, interval in enumerate(h18.PLANNED):
            key = (interval, int(g), int(d))
            req(key in cells, f"missing exact post-mass cell {key}")
            seen.add(key)
            info = cells[key]
            Mpost = int(info["post_mass"])
            Pexact = int(info["pre_mass"])
            pre_cap_here = sum(cell_caps[interval].values())
            parent_cap_here = sum(parent_caps[interval].values())
            req(pre_cap_here == Pexact, f"HPADJ20 exact pre-domain terminal mass mismatch {key}: {pre_cap_here} != {Pexact}")
            req(parent_cap_here == Pexact, f"HPADJ19 replay pre-domain terminal mass mismatch {key}: {parent_cap_here} != {Pexact}")

            blocks_here = int(cell_blocks[interval])
            recovered_blocks = 0
            for e, term_cap in info["pre_e_term_caps"].items():
                B = 19 * d - 5 * int(e) + 1
                req(int(term_cap) % B == 0, f"pre-e term cap not block-divisible {key,e}")
                recovered_blocks += int(term_cap) // B
            req(blocks_here == recovered_blocks, f"exact pre-domain block mass mismatch {key}")

            obj, cap, poscap, used = h18.optimize_cell_exact_predomain(cell_caps[interval], Mpost)
            pobj, pcap, pposcap, pused = h18.optimize_cell_exact_predomain(parent_caps[interval], Mpost)
            req(cap == pcap == Pexact, f"LP capacity mismatch {key}")
            req(obj <= pobj, f"two-tier LP weakened HPADJ19 replay {key}")
            if obj < pobj:
                strict_cell_count += 1
            if Mpost:
                nonzero_post_cells += 1
            total_obj += obj
            parent_total_obj += pobj
            cell_floor = obj.numerator // obj.denominator
            parent_cell_floor = pobj.numerator // pobj.denominator
            req(cell_floor <= parent_cell_floor, f"cell floor weakened HPADJ19 replay {key}")
            cell_floor_sum += cell_floor
            parent_cell_floor_sum += parent_cell_floor
            total_pre_terms += cap
            total_pre_blocks += blocks_here
            positive_q_capacity += poscap
            parent_positive_q_capacity += pposcap

            compact = {
                "row_id": row_id,
                "b_interval": list(interval),
                "g": int(g),
                "d": int(d),
                "exact_pre_mass": Pexact,
                "exact_pre_blocks": blocks_here,
                "exact_post_mass": Mpost,
                "hpadj19_replay_ratio_bin_count": len(parent_caps[interval]),
                "hpadj20_ratio_bin_count": len(cell_caps[interval]),
                "hpadj19_replay_used_ratio_bins": pused,
                "hpadj20_used_ratio_bins": used,
                "hpadj19_replay_cell_integer_upper": parent_cell_floor,
                "hpadj20_cell_integer_upper": cell_floor,
            }
            diagnostic_records.append({
                "row_index": row_index,
                "interval_position": interval_pos,
                "record": compact,
            })

        elapsed = time.monotonic() - started
        rate = elapsed / local_pos
        eta = rate * (len(assigned) - local_pos)
        print(
            f"HPADJ20_SHARD_PROGRESS shard={shard_index}/{shard_count} "
            f"row={local_pos}/{len(assigned)} row_id={row_id} d={d} "
            f"elapsed_s={elapsed:.1f} eta_s={eta:.1f}",
            file=sys.stderr,
            flush=True,
        )

    expected_seen = {
        (interval, int(g), int(d))
        for _row_index, _row_id, g, d in assigned
        for interval in h18.PLANNED
    }
    req(seen == expected_seen, "shard exact cell key-set mismatch")
    hist_classes, strict_profile_classes, nonminimum_tuples = profile_meta
    out = {
        "schema": SCHEMA,
        "route_id": "HPADJ-20_ex5",
        "status": "EXACT_ROW_SHARD_COMPLETE_HOSTILE_AUDIT_REQUIRED",
        "shard_index": shard_index,
        "shard_count": shard_count,
        "source_locks": {
            "hpadj20_producer_git_blob": PRODUCER_BLOB,
            "row_shard_worker_git_blob": git_blob(Path(__file__)),
            "hpadj19_parent_blob_sha1": p20.PARENT_BLOB,
            "full178_manifest_blob_sha1": p14.LOCKS["manifest_blob"],
            "hpadj10_counter_blob_sha1": p14.LOCKS["hpadj10_counter_blob"],
        },
        "assignment": {
            "strategy": "DETERMINISTIC_GREEDY_FULL178_ROW_WEIGHT_HPLUS1_CUBED",
            "rows": [list(x) for x in assigned],
            "estimated_weight": loads[shard_index],
            "sha256": assignment_digest(assigned, shard_index, shard_count),
        },
        "profile": {
            "exact_histogram_class_count": hist_classes,
            "strict_two_tier_class_count": strict_profile_classes,
            "nonminimum_tuple_count_in_full_H96_profile": nonminimum_tuples,
        },
        "totals": {
            "hpadj19_replay_rational_objective_numerator": parent_total_obj.numerator,
            "hpadj19_replay_rational_objective_denominator": parent_total_obj.denominator,
            "hpadj20_rational_objective_numerator": total_obj.numerator,
            "hpadj20_rational_objective_denominator": total_obj.denominator,
            "hpadj19_replay_cellwise_integer_floor_sum": parent_cell_floor_sum,
            "hpadj20_cellwise_integer_floor_sum": cell_floor_sum,
            "pre_hpadj08_exact_terminal_mass": total_pre_terms,
            "pre_hpadj08_exact_block_mass": total_pre_blocks,
            "hpadj19_replay_positive_q_terminal_capacity": parent_positive_q_capacity,
            "hpadj20_positive_q_terminal_capacity": positive_q_capacity,
            "nonzero_post_mass_cells": nonzero_post_cells,
            "strict_survivor_tier_instances": strict_survivor_tiers,
            "strict_lp_cell_count": strict_cell_count,
        },
        "diagnostic_records": diagnostic_records,
        "credit_firewall": {
            "partial_output_credit": False,
            "stage32_main_credit": False,
            "full178_completion_credit": False,
            "theorem_credit": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard-index", type=int, required=True)
    ap.add_argument("--shard-count", type=int, required=True)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--verify-existing", type=Path)
    args = ap.parse_args()

    if args.verify_existing is not None:
        data = cheap_validate_certificate(args.verify_existing, args.shard_index, args.shard_count)
        print("VALID_REUSABLE_HPADJ20_SHARD=" + data["canonical_sha256_without_this_field"])
        return

    req(args.output is not None, "--output is required for computation")
    out = compute_shard(args.shard_index, args.shard_count)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n")
    print(json.dumps({
        "shard_index": args.shard_index,
        "shard_count": args.shard_count,
        "rows": len(out["assignment"]["rows"]),
        "certificate": str(args.output),
        "canonical": out["canonical_sha256_without_this_field"],
        "candidate_floor_partial": out["totals"]["hpadj20_cellwise_integer_floor_sum"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
