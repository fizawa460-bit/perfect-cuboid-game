#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNKEY = HERE / "runkeys" / "000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
RESIDUAL = HERE / "MB104-000707-GEN24-X60-SINGLETON-RESIDUAL30.json"
PARENT = HERE / "run_mb104_000707_fibration_shell_local_exact.py"
RETAINED = HERE / "run_mb104_000707_fibration_isotropic_shells.py"
SCHEMA = "STAGE32_MB104_000707_GEN24_NEXTCOORD_COLD_PREFLIGHT_V1"
EXCLUDED = {60, 61, 62}
SHARDS = 8


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def lock_before_exec() -> dict:
    key = json.loads(RUNKEY.read_text(encoding="utf-8"))
    sl = key["source_locks"]
    expected = {
        str(PARENT.relative_to(Path.cwd())): sl["local_exact_engine_git_blob"],
        str(RETAINED.relative_to(Path.cwd())): sl["runner_git_blob"],
    }
    for rel, want in expected.items():
        got = git_blob(Path(rel))
        if got != want:
            raise SystemExit(f"source-lock mismatch before exec: {rel}: {got} != {want}")
    return expected


def residual_rows() -> list[dict]:
    raw = json.loads(RESIDUAL.read_text(encoding="utf-8"))
    if raw["schema"] != "STAGE32_MB104_000707_GEN24_X60_SINGLETON_RESIDUAL30_V1":
        raise SystemExit("unexpected residual schema")
    rows = raw["residual_singletons"]
    if int(raw["complete_singleton_child_count"]) != 281 or int(raw["residual_timeout_singleton_count"]) != 30:
        raise SystemExit("Gen23 carry/residual counts drifted")
    if len(rows) != 30:
        raise SystemExit("residual row count drifted")
    for row in rows:
        if row.get("solver_result") != "unknown" or row.get("reason") != "timeout":
            raise SystemExit("non-timeout leaf present in residual30")
    return rows


def choose_contract(parent) -> dict:
    payload = parent.problem_payload(0, 8)
    bounds = [tuple(map(int, pair)) for pair in payload["contract"]["coordinate_bounds"]]
    linear = payload["linear"]
    candidates = [j for j, (lo, hi) in enumerate(bounds) if j not in EXCLUDED and hi > lo]
    if not candidates:
        raise SystemExit("no remaining nontrivial exact coordinate domain")
    domains = {j: bounds[j][1] - bounds[j][0] + 1 for j in candidates}
    weights = {j: sum(abs(int(linear[r][j])) for r in range(140)) for j in candidates}
    j = min(candidates, key=lambda t: (domains[t], -weights[t], t))
    lo, hi = bounds[j]
    n = hi - lo + 1
    intervals = [[lo + (n * r) // SHARDS, lo + (n * (r + 1)) // SHARDS - 1] for r in range(SHARDS)]
    nonempty = [x for x in intervals if x[0] <= x[1]]
    if not nonempty or nonempty[0][0] != lo or nonempty[-1][1] != hi:
        raise SystemExit("next-coordinate partition endpoint failure")
    for a, b in zip(nonempty, nonempty[1:]):
        if a[1] + 1 != b[0]:
            raise SystemExit("next-coordinate partition gap/overlap")
    ranked = sorted(candidates, key=lambda t: (domains[t], -weights[t], t))
    return {
        "coordinate_0based": j,
        "bound": [lo, hi],
        "domain_size": n,
        "all140_weight": weights[j],
        "shard_count": SHARDS,
        "intervals": intervals,
        "nonempty_interval_count": len(nonempty),
        "coverage_is_exact_disjoint": True,
        "selection_rule": "MIN_EXACT_DOMAIN__MAX_ALL140_ABS_LINEAR_WEIGHT__MIN_INDEX__EXCLUDING_X62_X61_X60",
        "selection_rank_top8": [
            {"coordinate_0based": t, "domain_size": domains[t], "all140_weight": weights[t]}
            for t in ranked[:8]
        ],
        "bound_method": payload["contract"]["bound_method"],
        "dual_diagonal_sha256": payload["contract"]["dual_diagonal_sha256"],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    verified = lock_before_exec()
    rows = residual_rows()
    parent = importlib.import_module("run_mb104_000707_fibration_shell_local_exact")
    contract = choose_contract(parent)
    payload = {
        "schema": SCHEMA,
        "status": "COLD_PREPARED_NO_HEAVY_EXECUTION_NO_CREDIT",
        "source_generation": 23,
        "carried_complete_x60_singletons": 281,
        "residual_timeout_leaf_count": 30,
        "recompute_carried_complete_regions": False,
        "fixed_coordinates_per_residual_leaf": [62, 61, 60],
        "next_coordinate_contract": contract,
        "planned_packet_count": 30,
        "planned_interval_child_count": 30 * contract["nonempty_interval_count"],
        "planned_effective_heavy_concurrency": 4,
        "heavy_armed": False,
        "execution_authorized": False,
        "source_locks_verified_before_parent_import": verified,
        "residual_file_sha256": hashlib.sha256(RESIDUAL.read_bytes()).hexdigest(),
        "credit_firewall": {
            "numerical_fibration_shell_credit": False,
            "effectivity_credit": False,
            "semiampleness_credit": False,
            "global_fibration_optimum_credit": False,
            "MB104_complete": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = parent.csha(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
