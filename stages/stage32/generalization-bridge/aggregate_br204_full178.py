#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path

EXPECTED_B = set(range(97))
EXPECTED_STATES = 4_070_710
EXPECTED_BC_ASSIGNMENT_MASS = 174_683_387_305
EXPECTED_BASE_BLOB = "b7fc7e0c6c889c92cb152d4e8b54d05d2b71a5d1"
DEFAULT_ENVELOPE = 6_703_403_803_993_209_250_491
DEFAULT_MAIN_BOUND = 179_119_009_547_804_181_594


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def raw_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.suffix == ".gz":
        return gzip.decompress(data)
    return data


def parse_unit(path: Path, worker_blob: str) -> dict:
    raw = raw_bytes(path)
    lines = raw.decode("utf-8").splitlines()
    req(lines and lines[0].startswith("META\t"), f"missing META {path}")
    m = lines[0].split("\t")
    req(len(m) == 10, f"META field count {path}")
    _, b, states, mass, tail_mass, wblob, base_blob, mu_sha, terminal_sha, eval_parts = m
    b = int(b)
    req(b in EXPECTED_B, f"b outside range {path}")
    req(wblob == worker_blob, f"worker blob drift b={b}")
    req(base_blob == EXPECTED_BASE_BLOB, f"base BR204 blob drift b={b}")
    k8: dict[tuple[int, int], int] = {}
    mu: dict[tuple[int, int], tuple[int, int]] = {}
    sum_line = None
    tail_line = None
    for line in lines[1:]:
        p = line.split("\t")
        if p[0] == "K":
            req(len(p) == 4, f"K field count b={b}")
            key = (int(p[1]), int(p[2]))
            req(key[0] > 0 and key[1] > 0, f"nonpositive K key b={b}")
            req(key not in k8, f"duplicate K key b={b}")
            k8[key] = int(p[3])
        elif p[0] == "M":
            req(len(p) == 5, f"M field count b={b}")
            key = (int(p[1]), int(p[2]))
            cap, tail = int(p[3]), int(p[4])
            req(key[0] > 0 and key[1] > 0, f"nonpositive M key b={b}")
            req(0 <= tail <= cap, f"tail outside mu cap b={b}")
            req(key not in mu, f"duplicate M key b={b}")
            mu[key] = (cap, tail)
        elif p[0] == "TAIL":
            req(len(p) == 13 and tail_line is None, f"bad TAIL b={b}")
            tail_line = tuple(int(x) for x in p[1:])
        elif p[0] == "SUM":
            req(len(p) == 4 and sum_line is None, f"bad SUM b={b}")
            sum_line = tuple(int(x) for x in p[1:])
        else:
            raise SystemExit(f"FAIL: unknown record {p[0]} b={b}")
    req(sum_line is not None, f"missing SUM b={b}")
    req(tail_line is not None, f"missing TAIL b={b}")
    req(sum(k8.values()) == sum_line[0], f"K SUM drift b={b}")
    req(sum(v[0] for v in mu.values()) == sum_line[1], f"M SUM drift b={b}")
    req(sum(v[1] for v in mu.values()) == sum_line[2], f"tail SUM drift b={b}")
    for key, (cap, _) in mu.items():
        req(key in k8 and cap <= k8[key], f"mu exceeds K8 b={b} key={key}")

    (
        tail_base_states, non_tail_base_states, tail_slot_assignment_mass,
        tail_slot_evaluation_cells, k8_lgt8_raw_objective,
        k8_tail_slot_raw_objective, mu_lgt8_raw_objective,
        mu_tail_slot_raw_objective, k8_lgt8_positive_capacity,
        k8_tail_slot_positive_capacity, mu_lgt8_positive_capacity,
        mu_tail_slot_positive_capacity,
    ) = tail_line
    states_i = int(states)
    mass_i = int(mass)
    tail_mass_i = int(tail_mass)
    req(tail_base_states + non_tail_base_states == states_i, f"tail base partition drift b={b}")
    req(0 <= tail_slot_assignment_mass <= mass_i, f"tail assignment mass outside total b={b}")
    req(tail_slot_assignment_mass == tail_mass_i, f"META/TAIL tail mass drift b={b}")
    req(0 <= mu_lgt8_raw_objective <= k8_lgt8_raw_objective, f"mu L>8 objective exceeds K8 b={b}")
    req(0 <= mu_tail_slot_raw_objective <= k8_tail_slot_raw_objective, f"mu tail-slot objective exceeds K8 b={b}")
    req(0 <= mu_lgt8_positive_capacity <= k8_lgt8_positive_capacity, f"mu L>8 capacity exceeds K8 b={b}")
    req(0 <= mu_tail_slot_positive_capacity <= k8_tail_slot_positive_capacity, f"mu tail-slot capacity exceeds K8 b={b}")
    req(mu_tail_slot_positive_capacity == sum_line[2], f"TAIL/SUM mu tail capacity drift b={b}")

    return {
        "b": b,
        "states": states_i,
        "mass": mass_i,
        "tail_mass": tail_mass_i,
        "worker_blob": wblob,
        "base_blob": base_blob,
        "mu_sha": mu_sha,
        "terminal_sha": terminal_sha,
        "eval_parts": int(eval_parts),
        "k8": k8,
        "mu": mu,
        "tail": {
            "base_states_L_gt_8": tail_base_states,
            "base_states_L_le_8": non_tail_base_states,
            "tail_slot_assignment_mass": tail_slot_assignment_mass,
            "tail_slot_evaluation_cells": tail_slot_evaluation_cells,
            "k8_L_gt_8_raw_objective": k8_lgt8_raw_objective,
            "k8_tail_slot_raw_objective": k8_tail_slot_raw_objective,
            "mu_L_gt_8_raw_objective": mu_lgt8_raw_objective,
            "mu_tail_slot_raw_objective": mu_tail_slot_raw_objective,
            "k8_L_gt_8_positive_capacity": k8_lgt8_positive_capacity,
            "k8_tail_slot_positive_capacity": k8_tail_slot_positive_capacity,
            "mu_L_gt_8_positive_capacity": mu_lgt8_positive_capacity,
            "mu_tail_slot_positive_capacity": mu_tail_slot_positive_capacity,
        },
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "source_path": str(path),
    }


def discover(input_dirs: list[Path], worker_blob: str) -> dict[int, dict]:
    out: dict[int, dict] = {}
    source_rank: dict[int, int] = {}
    # Earlier directories have priority, so current-run artifacts should be listed first.
    for rank, d in enumerate(input_dirs):
        if not d.exists():
            continue
        candidates = sorted([*d.rglob("br204-b-*.tsv"), *d.rglob("br204-b-*.tsv.gz")])
        for p in candidates:
            u = parse_unit(p, worker_blob)
            b = u["b"]
            if b not in out:
                out[b] = u
                source_rank[b] = rank
            elif source_rank[b] == rank:
                req(out[b]["sha256"] == u["sha256"], f"conflicting duplicate b={b} in same input priority")
            # A later input directory is carry-only fallback; a validated current unit wins.
    return out


def solve_lp(bins: dict[tuple[int, int], int], envelope: int,
             tail_bins: dict[tuple[int, int], int] | None = None) -> dict:
    tail_bins = tail_bins or {}
    req(envelope > 0, "nonpositive LP envelope")
    for key, tail in tail_bins.items():
        req(key in bins, f"tail key absent from bins {key}")
        req(0 <= tail <= bins[key], f"global tail outside cap {key}")

    classes: dict[Fraction, dict[str, int]] = {}
    for (s, B), cap in bins.items():
        req(cap >= 0, f"negative capacity {(s, B)}")
        if not cap:
            continue
        ratio = Fraction(s, B)
        c = classes.setdefault(ratio, {"capacity": 0, "tail": 0, "members": 0})
        c["capacity"] += cap
        c["tail"] += tail_bins.get((s, B), 0)
        c["members"] += 1

    remaining = envelope
    value = Fraction(0, 1)
    used_classes = 0
    cutoff = None
    forced_tail = 0
    selected_classes_total_tail_capacity = 0
    for ratio in sorted(classes, reverse=True):
        c = classes[ratio]
        capacity = c["capacity"]
        tail = c["tail"]
        if remaining <= 0:
            break
        take = min(remaining, capacity)
        value += ratio * take
        forced_tail += max(0, take - (capacity - tail))
        if take and tail:
            selected_classes_total_tail_capacity += tail
        remaining -= take
        used_classes += 1
        if remaining == 0:
            cutoff = {
                "ratio_num": ratio.numerator,
                "ratio_den": ratio.denominator,
                "take": take,
                "class_capacity": capacity,
                "class_tail_capacity": tail,
                "member_bin_count": c["members"],
                "partial_class": take < capacity,
            }
            break

    req(remaining == 0, "positive-ratio capacity does not cover envelope")
    req(cutoff is not None, "LP cutoff missing")
    return {
        "exact_num": value.numerator,
        "exact_den": value.denominator,
        "upper_floor": value.numerator // value.denominator,
        "remainder": value.numerator % value.denominator,
        "positive_capacity": sum(bins.values()),
        "bin_count": sum(1 for cap in bins.values() if cap),
        "ratio_class_count": len(classes),
        "used_ratio_class_count": used_classes,
        "cutoff": cutoff,
        "forced_tail_selected_capacity": forced_tail,
        "selected_ratio_classes_total_tail_capacity": selected_classes_total_tail_capacity,
    }


def command_plan(args) -> None:
    units = discover([Path(x) for x in args.input_dir], args.worker_blob)
    missing = sorted(EXPECTED_B - set(units))
    out = {
        "schema": "STAGE32_BR204_HEAVY_RESUME_PLAN_V2",
        "worker_blob": args.worker_blob,
        "validated_units": sorted(units),
        "missing_units": missing,
        "complete": not missing,
    }
    Path(args.out).write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    print(json.dumps(missing, separators=(",", ":")))


def command_aggregate(args) -> None:
    units = discover([Path(x) for x in args.input_dir], args.worker_blob)
    req(set(units) == EXPECTED_B, f"unit coverage mismatch missing={sorted(EXPECTED_B-set(units))}")
    req(sum(u["states"] for u in units.values()) == EXPECTED_STATES, "H96 refined-state census drift")
    req(sum(u["mass"] for u in units.values()) == EXPECTED_BC_ASSIGNMENT_MASS, "H96 BC mass drift")
    mu_shas = {u["mu_sha"] for u in units.values()}
    term_shas = {u["terminal_sha"] for u in units.values()}
    req(len(mu_shas) == 1, "mu-table SHA drift across units")
    req(len(term_shas) == 1, "terminal SHA drift across units")

    k8: dict[tuple[int, int], int] = {}
    mu: dict[tuple[int, int], int] = {}
    tail: dict[tuple[int, int], int] = {}
    unit_rows = []
    tail_totals = {
        "base_states_L_gt_8": 0,
        "base_states_L_le_8": 0,
        "tail_slot_assignment_mass": 0,
        "tail_slot_evaluation_cells": 0,
        "k8_L_gt_8_raw_objective": 0,
        "k8_tail_slot_raw_objective": 0,
        "mu_L_gt_8_raw_objective": 0,
        "mu_tail_slot_raw_objective": 0,
        "k8_L_gt_8_positive_capacity": 0,
        "k8_tail_slot_positive_capacity": 0,
        "mu_L_gt_8_positive_capacity": 0,
        "mu_tail_slot_positive_capacity": 0,
    }
    for b in sorted(units):
        u = units[b]
        for key, cap in u["k8"].items():
            k8[key] = k8.get(key, 0) + cap
        for key, (cap, tcap) in u["mu"].items():
            mu[key] = mu.get(key, 0) + cap
            tail[key] = tail.get(key, 0) + tcap
        for key in tail_totals:
            tail_totals[key] += u["tail"][key]
        unit_rows.append({
            "b": b,
            "states": u["states"],
            "bc_assignment_mass": u["mass"],
            "bc_tail_slot_assignment_mass": u["tail_mass"],
            "qbc_tail_attribution_digest_sha256": u["sha256"],
            "raw_bytes": u["bytes"],
        })

    req(tail_totals["base_states_L_gt_8"] + tail_totals["base_states_L_le_8"] == EXPECTED_STATES,
        "global L<=8/L>8 base-state partition drift")
    req(tail_totals["tail_slot_assignment_mass"] == sum(u["tail_mass"] for u in units.values()),
        "global tail assignment mass drift")

    for key, cap in mu.items():
        req(key in k8 and cap <= k8[key], f"global mu exceeds K8 key={key}")
    for key, cap in tail.items():
        req(key in mu and cap <= mu[key], f"global tail exceeds mu key={key}")

    envelope = int(args.envelope)
    main_bound = int(args.main_bound)
    k8_lp = solve_lp(k8, envelope)
    mu_lp = solve_lp(mu, envelope, tail)
    req(Fraction(mu_lp["exact_num"], mu_lp["exact_den"]) <=
        Fraction(k8_lp["exact_num"], k8_lp["exact_den"]), "mu LP is not <= K8 LP")

    stream = hashlib.sha256()
    for key in sorted(k8):
        stream.update(f"K\t{key[0]}\t{key[1]}\t{k8[key]}\n".encode())
    for key in sorted(mu):
        stream.update(f"M\t{key[0]}\t{key[1]}\t{mu[key]}\t{tail.get(key,0)}\n".encode())

    raw_tail_gate = (
        tail_totals["base_states_L_gt_8"] > 0
        and tail_totals["tail_slot_assignment_mass"] > 0
        and tail_totals["k8_L_gt_8_raw_objective"] > 0
        and tail_totals["k8_tail_slot_raw_objective"] > 0
    )
    strong_tail_gate = raw_tail_gate and mu_lp["forced_tail_selected_capacity"] > 0

    result = {
        "schema": "STAGE32_BR204_FULL178_GLOBAL_BIN_UNION_RESULT_V2",
        "status": "HEAVY_RESULT_ZERO_CREDIT_REQUIRES_HOSTILE_AUDIT",
        "population": {
            "H": 96,
            "unit_count": 97,
            "refined_states": EXPECTED_STATES,
            "bc_assignment_mass": EXPECTED_BC_ASSIGNMENT_MASS,
        },
        "source_locks": {
            "worker_blob": args.worker_blob,
            "base_compact_mu_blob": EXPECTED_BASE_BLOB,
            "mu_table_sha256": next(iter(mu_shas)),
            "terminal_syndrome_sha256": next(iter(term_shas)),
        },
        "envelope": envelope,
        "k8_full178": k8_lp,
        "mu_full178": mu_lp,
        "mu_le_k8": True,
        "qbc_tail": {
            **tail_totals,
            "forced_selected_tail_slot_capacity_at_mu_lp": mu_lp["forced_tail_selected_capacity"],
            "addendum_full178_half_gate_candidate": raw_tail_gate,
            "strong_global_lp_tail_slot_gate_candidate": strong_tail_gate,
            "formal_br205_gate_passed": False,
        },
        "comparison_to_audited_main_v40": {
            "main_bound": main_bound,
            "mu_candidate_floor": mu_lp["upper_floor"],
            "strictly_below_current_main": mu_lp["upper_floor"] < main_bound,
            "potential_nonadditive_tightening": max(0, main_bound - mu_lp["upper_floor"]),
        },
        "global_bin_stream_sha256": stream.hexdigest(),
        "units": unit_rows,
        "credit": {
            "stage32_main": False,
            "full178_complete": False,
            "theorem": False,
            "effectivity": False,
            "receiver": False,
            "endpoint": False,
            "perfect_cuboid": False,
            "merge": False,
        },
    }
    Path(args.out).write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "k8_floor": k8_lp["upper_floor"],
        "mu_floor": mu_lp["upper_floor"],
        "forced_tail": mu_lp["forced_tail_selected_capacity"],
        "raw_tail_gate": raw_tail_gate,
        "strong_tail_gate": strong_tail_gate,
    }, sort_keys=True))


def command_self_test() -> None:
    bins = {(2, 5): 10, (1, 3): 10}
    tails = {(2, 5): 3}
    x = solve_lp(bins, 12, tails)
    req((x["exact_num"], x["exact_den"]) == (14, 3), "toy LP exact value")
    req(x["upper_floor"] == 4, "toy LP floor")
    req(x["forced_tail_selected_capacity"] == 3, "toy tail attribution")

    # Equal-ratio bins must be treated as one ratio class for forced-tail logic.
    tie_bins = {(1, 2): 5, (2, 4): 5}
    tie_tails = {(1, 2): 5, (2, 4): 0}
    y = solve_lp(tie_bins, 5, tie_tails)
    req((y["exact_num"], y["exact_den"]) == (5, 2), "tie LP exact value")
    req(y["forced_tail_selected_capacity"] == 0, "tie-class forced tail must be order-independent")
    req(y["cutoff"]["partial_class"] is True, "tie cutoff should be partial class")

    # Exact exhaustion at a ratio-class boundary is valid and must retain a cutoff receipt.
    z = solve_lp({(3, 5): 10}, 10, {})
    req((z["exact_num"], z["exact_den"]) == (6, 1), "exact-boundary LP value")
    req(z["cutoff"]["partial_class"] is False, "exact-boundary cutoff should be full class")
    print("PASS BR204 aggregator self-test")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("plan")
    p.add_argument("--input-dir", action="append", default=[])
    p.add_argument("--worker-blob", required=True)
    p.add_argument("--out", required=True)

    a = sub.add_parser("aggregate")
    a.add_argument("--input-dir", action="append", default=[])
    a.add_argument("--worker-blob", required=True)
    a.add_argument("--envelope", default=str(DEFAULT_ENVELOPE))
    a.add_argument("--main-bound", default=str(DEFAULT_MAIN_BOUND))
    a.add_argument("--out", required=True)

    sub.add_parser("self-test")
    args = ap.parse_args()
    if args.cmd == "plan":
        command_plan(args)
    elif args.cmd == "aggregate":
        command_aggregate(args)
    else:
        command_self_test()


if __name__ == "__main__":
    main()
