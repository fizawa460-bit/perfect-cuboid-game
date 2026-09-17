#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path

EXPECTED_B = set(range(97))
D_BANDS = ((8, 54), (56, 100), (102, 146), (148, 192))
EXPECTED_UNITS = {
    (b, d_lo, d_hi)
    for b in EXPECTED_B
    for d_lo, d_hi in D_BANDS
    if d_hi >= max(8, 2 * b)
}
EXPECTED_SUBUNITS = 250
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
    req(len(m) == 12, f"META field count {path}")
    _, b, d_lo, d_hi, states, mass, tail_mass, wblob, base_blob, mu_sha, terminal_sha, eval_parts = m
    b, d_lo, d_hi = int(b), int(d_lo), int(d_hi)
    unit = (b, d_lo, d_hi)
    req(unit in EXPECTED_UNITS, f"unexpected BR204 subunit {unit} path={path}")
    tag = f"b={b} d={d_lo}..{d_hi}"
    req(wblob == worker_blob, f"worker blob drift {tag}")
    req(base_blob == EXPECTED_BASE_BLOB, f"base BR204 blob drift {tag}")
    k8: dict[tuple[int, int], int] = {}
    mu: dict[tuple[int, int], tuple[int, int]] = {}
    sum_line = None
    tail_line = None
    for line in lines[1:]:
        q = line.split("\t")
        if q[0] == "K":
            req(len(q) == 4, f"K field count {tag}")
            key = (int(q[1]), int(q[2]))
            req(key[0] > 0 and key[1] > 0, f"nonpositive K key {tag}")
            req(key not in k8, f"duplicate K key {tag}")
            k8[key] = int(q[3])
        elif q[0] == "M":
            req(len(q) == 5, f"M field count {tag}")
            key = (int(q[1]), int(q[2]))
            cap, tail = int(q[3]), int(q[4])
            req(key[0] > 0 and key[1] > 0, f"nonpositive M key {tag}")
            req(0 <= tail <= cap, f"tail outside mu cap {tag}")
            req(key not in mu, f"duplicate M key {tag}")
            mu[key] = (cap, tail)
        elif q[0] == "TAIL":
            req(len(q) == 13 and tail_line is None, f"bad TAIL {tag}")
            tail_line = tuple(int(x) for x in q[1:])
        elif q[0] == "SUM":
            req(len(q) == 4 and sum_line is None, f"bad SUM {tag}")
            sum_line = tuple(int(x) for x in q[1:])
        else:
            raise SystemExit(f"FAIL: unknown record {q[0]} {tag}")
    req(sum_line is not None, f"missing SUM {tag}")
    req(tail_line is not None, f"missing TAIL {tag}")
    req(sum(k8.values()) == sum_line[0], f"K SUM drift {tag}")
    req(sum(v[0] for v in mu.values()) == sum_line[1], f"M SUM drift {tag}")
    req(sum(v[1] for v in mu.values()) == sum_line[2], f"tail SUM drift {tag}")
    for key, (cap, _) in mu.items():
        req(key in k8 and cap <= k8[key], f"mu exceeds K8 {tag} key={key}")

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
    req(tail_base_states + non_tail_base_states == states_i, f"tail base partition drift {tag}")
    req(0 <= tail_slot_assignment_mass <= mass_i, f"tail assignment mass outside total {tag}")
    req(tail_slot_assignment_mass == tail_mass_i, f"META/TAIL tail mass drift {tag}")
    req(0 <= mu_lgt8_raw_objective <= k8_lgt8_raw_objective, f"mu L>8 objective exceeds K8 {tag}")
    req(0 <= mu_tail_slot_raw_objective <= k8_tail_slot_raw_objective, f"mu tail-slot objective exceeds K8 {tag}")
    req(0 <= mu_lgt8_positive_capacity <= k8_lgt8_positive_capacity, f"mu L>8 capacity exceeds K8 {tag}")
    req(0 <= mu_tail_slot_positive_capacity <= k8_tail_slot_positive_capacity, f"mu tail-slot capacity exceeds K8 {tag}")
    req(mu_tail_slot_positive_capacity == sum_line[2], f"TAIL/SUM mu tail capacity drift {tag}")

    return {
        "unit": unit,
        "b": b,
        "d_lo": d_lo,
        "d_hi": d_hi,
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
def discover(input_dirs: list[Path], worker_blob: str) -> dict[tuple[int, int, int], dict]:
    out: dict[tuple[int, int, int], dict] = {}
    source_rank: dict[tuple[int, int, int], int] = {}
    # Earlier directories have priority, so current-run artifacts should be listed first.
    for rank, d in enumerate(input_dirs):
        if not d.exists():
            continue
        candidates = sorted([*d.rglob("br204-u-b*-d*-*.tsv"), *d.rglob("br204-u-b*-d*-*.tsv.gz")])
        for p in candidates:
            u = parse_unit(p, worker_blob)
            key = u["unit"]
            if key not in out:
                out[key] = u
                source_rank[key] = rank
            elif source_rank[key] == rank:
                req(out[key]["sha256"] == u["sha256"], f"conflicting duplicate subunit={key} in same input priority")
            # A later input directory is carry-only fallback; a validated current subunit wins.
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
    missing = sorted(EXPECTED_UNITS - set(units))
    missing_rows = [{"b": b, "d_lo": d_lo, "d_hi": d_hi} for b, d_lo, d_hi in missing]
    out = {
        "schema": "STAGE32_BR204_HEAVY_RESUME_PLAN_V3_B_D_BANDS",
        "worker_blob": args.worker_blob,
        "expected_subunit_count": EXPECTED_SUBUNITS,
        "validated_subunits": [
            {"b": b, "d_lo": d_lo, "d_hi": d_hi}
            for b, d_lo, d_hi in sorted(units)
        ],
        "missing_units": missing_rows,
        "complete": not missing,
    }
    Path(args.out).write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    print(json.dumps(missing_rows, separators=(",", ":")))


def command_aggregate(args) -> None:
    units = discover([Path(x) for x in args.input_dir], args.worker_blob)
    req(set(units) == EXPECTED_UNITS,
        f"subunit coverage mismatch missing={sorted(EXPECTED_UNITS-set(units))} extra={sorted(set(units)-EXPECTED_UNITS)}")
    req(len(units) == EXPECTED_SUBUNITS, "BR204 subunit-count drift")

    by_b: dict[int, list[dict]] = {b: [] for b in EXPECTED_B}
    for key in sorted(units):
        by_b[key[0]].append(units[key])

    static_rows: dict[int, dict] = {}
    for b in sorted(EXPECTED_B):
        xs = by_b[b]
        req(xs, f"no subunits for b={b}")
        expected_for_b = {u for u in EXPECTED_UNITS if u[0] == b}
        req({x["unit"] for x in xs} == expected_for_b, f"d-band coverage drift b={b}")
        first = xs[0]
        for x in xs[1:]:
            req(x["states"] == first["states"], f"static state census drift across bands b={b}")
            req(x["mass"] == first["mass"], f"static BC mass drift across bands b={b}")
            req(x["tail_mass"] == first["tail_mass"], f"static tail mass drift across bands b={b}")
            req(x["mu_sha"] == first["mu_sha"], f"mu SHA drift across bands b={b}")
            req(x["terminal_sha"] == first["terminal_sha"], f"terminal SHA drift across bands b={b}")
            for k in ("base_states_L_gt_8", "base_states_L_le_8", "tail_slot_assignment_mass"):
                req(x["tail"][k] == first["tail"][k], f"static TAIL field {k} drift across bands b={b}")
        static_rows[b] = first

    req(sum(u["states"] for u in static_rows.values()) == EXPECTED_STATES, "H96 refined-state census drift")
    req(sum(u["mass"] for u in static_rows.values()) == EXPECTED_BC_ASSIGNMENT_MASS, "H96 BC mass drift")
    mu_shas = {u["mu_sha"] for u in static_rows.values()}
    term_shas = {u["terminal_sha"] for u in static_rows.values()}
    req(len(mu_shas) == 1, "mu-table SHA drift across b units")
    req(len(term_shas) == 1, "terminal SHA drift across b units")

    k8: dict[tuple[int, int], int] = {}
    mu: dict[tuple[int, int], int] = {}
    tail: dict[tuple[int, int], int] = {}
    subunit_rows = []

    static_tail_totals = {
        "base_states_L_gt_8": 0,
        "base_states_L_le_8": 0,
        "tail_slot_assignment_mass": 0,
    }
    dynamic_tail_totals = {
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

    for b, u in static_rows.items():
        for key in static_tail_totals:
            static_tail_totals[key] += u["tail"][key]

    for key in sorted(units):
        u = units[key]
        for bin_key, cap in u["k8"].items():
            k8[bin_key] = k8.get(bin_key, 0) + cap
        for bin_key, (cap, tcap) in u["mu"].items():
            mu[bin_key] = mu.get(bin_key, 0) + cap
            tail[bin_key] = tail.get(bin_key, 0) + tcap
        for name in dynamic_tail_totals:
            dynamic_tail_totals[name] += u["tail"][name]
        subunit_rows.append({
            "b": u["b"],
            "d_lo": u["d_lo"],
            "d_hi": u["d_hi"],
            "static_states_for_b": u["states"],
            "static_bc_assignment_mass_for_b": u["mass"],
            "qbc_tail_attribution_digest_sha256": u["sha256"],
            "raw_bytes": u["bytes"],
        })

    tail_totals = {**static_tail_totals, **dynamic_tail_totals}
    req(tail_totals["base_states_L_gt_8"] + tail_totals["base_states_L_le_8"] == EXPECTED_STATES,
        "global L<=8/L>8 base-state partition drift")
    req(tail_totals["tail_slot_assignment_mass"] == sum(u["tail_mass"] for u in static_rows.values()),
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
        "schema": "STAGE32_BR204_FULL178_GLOBAL_BIN_UNION_RESULT_V3_B_D_BANDS",
        "status": "HEAVY_RESULT_ZERO_CREDIT_REQUIRES_HOSTILE_AUDIT",
        "population": {
            "H": 96,
            "b_unit_count": 97,
            "durable_subunit_count": EXPECTED_SUBUNITS,
            "d_bands": [list(x) for x in D_BANDS],
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
        "subunits": subunit_rows,
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
        "durable_subunits": EXPECTED_SUBUNITS,
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
    req(len(EXPECTED_UNITS) == EXPECTED_SUBUNITS, "expected subunit census")
    for b in sorted(EXPECTED_B):
        cover = [
            (d_lo, d_hi) for bb, d_lo, d_hi in EXPECTED_UNITS if bb == b
        ]
        for d in range(max(8, 2 * b), 193, 2):
            req(sum(d_lo <= d <= d_hi for d_lo, d_hi in cover) == 1,
                f"d coverage/disjointness failed b={b} d={d}")
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
