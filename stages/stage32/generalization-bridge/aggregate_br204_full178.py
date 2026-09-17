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
        elif p[0] == "SUM":
            req(len(p) == 4 and sum_line is None, f"bad SUM b={b}")
            sum_line = tuple(int(x) for x in p[1:])
        else:
            raise SystemExit(f"FAIL: unknown record {p[0]} b={b}")
    req(sum_line is not None, f"missing SUM b={b}")
    req(sum(k8.values()) == sum_line[0], f"K SUM drift b={b}")
    req(sum(v[0] for v in mu.values()) == sum_line[1], f"M SUM drift b={b}")
    req(sum(v[1] for v in mu.values()) == sum_line[2], f"tail SUM drift b={b}")
    for key, (cap, _) in mu.items():
        req(key in k8 and cap <= k8[key], f"mu exceeds K8 b={b} key={key}")
    return {
        "b": b,
        "states": int(states),
        "mass": int(mass),
        "tail_mass": int(tail_mass),
        "worker_blob": wblob,
        "base_blob": base_blob,
        "mu_sha": mu_sha,
        "terminal_sha": terminal_sha,
        "eval_parts": int(eval_parts),
        "k8": k8,
        "mu": mu,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "source_path": str(path),
    }


def discover(input_dirs: list[Path], worker_blob: str) -> dict[int, dict]:
    out: dict[int, dict] = {}
    # Earlier directories have priority, so current-run artifacts should be listed first.
    for d in input_dirs:
        if not d.exists():
            continue
        candidates = sorted([*d.rglob("br204-b-*.tsv"), *d.rglob("br204-b-*.tsv.gz")])
        for p in candidates:
            u = parse_unit(p, worker_blob)
            out.setdefault(u["b"], u)
    return out


def solve_lp(bins: dict[tuple[int, int], int], envelope: int,
             tail_bins: dict[tuple[int, int], int] | None = None) -> dict:
    tail_bins = tail_bins or {}
    items = sorted(
        ((Fraction(s, B), cap, s, B) for (s, B), cap in bins.items() if cap),
        key=lambda z: z[0],
        reverse=True,
    )
    remaining = envelope
    value = Fraction(0, 1)
    used = 0
    cutoff = None
    forced_tail = 0
    selected_tail_bin_capacity = 0
    for ratio, capacity, s, B in items:
        if remaining <= 0:
            break
        take = min(remaining, capacity)
        value += ratio * take
        tail = tail_bins.get((s, B), 0)
        req(0 <= tail <= capacity, f"global tail outside cap {(s,B)}")
        forced_tail += max(0, take - (capacity - tail))
        if take and tail:
            selected_tail_bin_capacity += tail
        remaining -= take
        used += 1
        if take < capacity:
            cutoff = (s, B, take, capacity)
            break
    req(remaining == 0, "positive-ratio capacity does not cover envelope")
    req(cutoff is not None, "fractional LP cutoff missing")
    return {
        "exact_num": value.numerator,
        "exact_den": value.denominator,
        "upper_floor": value.numerator // value.denominator,
        "remainder": value.numerator % value.denominator,
        "positive_capacity": sum(bins.values()),
        "bin_count": len(items),
        "used_bin_count": used,
        "cutoff": list(cutoff),
        "forced_tail_selected_capacity": forced_tail,
        "selected_bins_total_tail_capacity": selected_tail_bin_capacity,
    }


def command_plan(args) -> None:
    units = discover([Path(x) for x in args.input_dir], args.worker_blob)
    missing = sorted(EXPECTED_B - set(units))
    out = {
        "schema": "STAGE32_BR204_HEAVY_RESUME_PLAN_V1",
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
    for b in sorted(units):
        u = units[b]
        for key, cap in u["k8"].items():
            k8[key] = k8.get(key, 0) + cap
        for key, (cap, tcap) in u["mu"].items():
            mu[key] = mu.get(key, 0) + cap
            tail[key] = tail.get(key, 0) + tcap
        unit_rows.append({
            "b": b, "states": u["states"], "bc_assignment_mass": u["mass"],
            "bc_tail_assignment_mass": u["tail_mass"], "sha256": u["sha256"],
            "raw_bytes": u["bytes"],
        })

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

    result = {
        "schema": "STAGE32_BR204_FULL178_GLOBAL_BIN_UNION_RESULT_V1",
        "status": "HEAVY_RESULT_ZERO_CREDIT_REQUIRES_HOSTILE_AUDIT",
        "population": {
            "H": 96, "unit_count": 97, "refined_states": EXPECTED_STATES,
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
            "bc_tail_assignment_mass": sum(u["tail_mass"] for u in units.values()),
            "positive_capacity": sum(tail.values()),
            "forced_selected_capacity_at_mu_lp": mu_lp["forced_tail_selected_capacity"],
            "formal_br205_tail_activity_gate_candidate":
                mu_lp["forced_tail_selected_capacity"] > 0,
        },
        "comparison_to_audited_main_v40": {
            "main_bound": main_bound,
            "mu_candidate_floor": mu_lp["upper_floor"],
            "strictly_below_current_main": mu_lp["upper_floor"] < main_bound,
            "potential_nonadditive_tightening":
                max(0, main_bound - mu_lp["upper_floor"]),
        },
        "global_bin_stream_sha256": stream.hexdigest(),
        "units": unit_rows,
        "credit": {
            "stage32_main": False, "full178_complete": False, "theorem": False,
            "effectivity": False, "receiver": False, "endpoint": False,
            "perfect_cuboid": False, "merge": False,
        },
    }
    Path(args.out).write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "k8_floor": k8_lp["upper_floor"],
        "mu_floor": mu_lp["upper_floor"],
        "forced_tail": mu_lp["forced_tail_selected_capacity"],
    }, sort_keys=True))


def command_self_test() -> None:
    bins = {(2, 5): 10, (1, 3): 10}
    tails = {(2, 5): 3}
    x = solve_lp(bins, 12, tails)
    req((x["exact_num"], x["exact_den"]) == (14, 3), "toy LP exact value")
    req(x["upper_floor"] == 4, "toy LP floor")
    req(x["forced_tail_selected_capacity"] == 3, "toy tail attribution")
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
