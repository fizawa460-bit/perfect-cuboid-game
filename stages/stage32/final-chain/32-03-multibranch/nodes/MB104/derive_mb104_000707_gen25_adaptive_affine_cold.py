#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
RUNKEY = HERE / "runkeys" / "000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
RESIDUAL = HERE / "MB104-000707-GEN24-X60-SINGLETON-RESIDUAL30.json"
PARENT = HERE / "run_mb104_000707_fibration_shell_local_exact.py"
RETAINED = HERE / "run_mb104_000707_fibration_isotropic_shells.py"
CARRY_SOURCE = HERE / "MB104-000707-GEN23-X60-SINGLETON-CARRY-SOURCE.json"
CARRY_INDEX = HERE / "MB104-000707-GEN23-X60-SINGLETON-CARRY-INDEX.json"
CARRY_VERIFIER = HERE / "verify_mb104_000707_gen23_x60_singleton_carry.py"
SCHEMA = "STAGE32_MB104_000707_GEN25_ADAPTIVE_AFFINE_COLD_V1"
FIXED = (62, 61, 60)
FORBIDDEN_SPLIT = {59, 60, 61, 62}
MAX_SHARDS = 8

def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def frac(v) -> Fraction:
    return Fraction(int(v.p), int(v.q)) if hasattr(v, "p") else Fraction(int(v), 1)

def fpair(v: Fraction) -> list[int]:
    return [int(v.numerator), int(v.denominator)]

def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=REPO, text=True).strip()

def lock_before_parent_import() -> dict:
    key = json.loads(RUNKEY.read_text(encoding="utf-8"))
    sl = key["source_locks"]
    paths = {
        "local_exact_engine_git_blob": PARENT,
        "runner_git_blob": RETAINED,
        "gen23_carry_source_git_blob": CARRY_SOURCE,
        "gen23_carry_index_git_blob": CARRY_INDEX,
        "gen23_carry_verifier_git_blob": CARRY_VERIFIER,
        "gen24_residual_git_blob": RESIDUAL,
    }
    verified = {}
    for field, path in paths.items():
        want = sl[field]
        got = git_blob(path)
        if got != want:
            raise SystemExit(f"source-lock mismatch before parent import: {field}: {got} != {want}")
        verified[field] = got
    return verified

def residual_rows() -> list[dict]:
    raw = json.loads(RESIDUAL.read_text(encoding="utf-8"))
    if raw["schema"] != "STAGE32_MB104_000707_GEN24_X60_SINGLETON_RESIDUAL30_V1":
        raise SystemExit("unexpected residual schema")
    if int(raw["source_generation"]) != 23:
        raise SystemExit("unexpected residual source generation")
    if int(raw["complete_singleton_child_count"]) != 281 or int(raw["residual_timeout_singleton_count"]) != 30:
        raise SystemExit("Gen23 carry/residual counts drifted")
    rows = raw["residual_singletons"]
    if len(rows) != 30:
        raise SystemExit("residual row count drifted")
    for row in rows:
        if row.get("solver_result") != "unknown" or row.get("reason") != "timeout":
            raise SystemExit("non-timeout leaf present in residual30")
    return rows

def build_context(parent) -> dict:
    p = parent.problem_payload(0, 8)
    q = p["q"]
    prow = p["prow"]
    free = [j for j in range(63) if j not in FIXED]
    pos = {j: k for k, j in enumerate(free)}
    A = Matrix([[int(q[i][j]) for j in free] for i in free])
    Ainv = A.inv()
    a = Matrix([int(prow[i]) for i in free])
    ainv = Ainv * a
    s = frac((a.T * ainv)[0])
    if s <= 0:
        raise SystemExit("nonpositive affine dual norm")
    linear = p["linear"]
    weights = {j: sum(abs(int(linear[r][j])) for r in range(140)) for j in range(63)}
    return {
        "p": p,
        "q": q,
        "prow": prow,
        "free": free,
        "pos": pos,
        "Ainv": Ainv,
        "a": a,
        "ainv": ainv,
        "s": s,
        "weights": weights,
        "global_bounds": p["contract"]["coordinate_bounds"],
        "norm": int(p["shell"]["hperp_norm"]),
        "pc": int(p["pc"]),
    }

def exact_leaf_contract(ctx: dict, row: dict) -> dict:
    q = ctx["q"]
    prow = ctx["prow"]
    free = ctx["free"]
    pos = ctx["pos"]
    Ainv = ctx["Ainv"]
    a = ctx["a"]
    ainv = ctx["ainv"]
    s = ctx["s"]
    fixed = {
        62: int(row["primary_value"]),
        61: int(row["fixed_x61_value"]),
        60: int(row["fixed_x60_value"]),
    }
    d = Matrix([sum(int(q[i][f]) * fixed[f] for f in FIXED) for i in free])
    c = sum(fixed[i] * int(q[i][j]) * fixed[j] for i in FIXED for j in FIXED)
    rhs = ctx["pc"] - sum(int(prow[f]) * fixed[f] for f in FIXED)
    dinv = Ainv * d
    R = Fraction(ctx["norm"] - c, 1) + frac((d.T * dinv)[0])
    h = Fraction(rhs, 1) + frac((a.T * dinv)[0])
    residual_energy = R - h * h / s
    base_center = -dinv + ainv * (h / s)
    candidates = []
    if residual_energy >= 0:
        for j in free:
            if j in FORBIDDEN_SPLIT:
                continue
            k = pos[j]
            variance = frac(Ainv[k, k]) - frac(ainv[k]) * frac(ainv[k]) / s
            if variance < 0:
                raise SystemExit(f"negative conditioned variance at x{j}")
            radius2 = residual_energy * variance
            center = frac(base_center[k])
            glo, ghi = map(int, ctx["global_bounds"][j])
            values = [v for v in range(glo, ghi + 1) if (Fraction(v, 1) - center) ** 2 <= radius2]
            if values:
                candidates.append({
                    "coordinate_0based": j,
                    "bound": [values[0], values[-1]],
                    "domain_size": len(values),
                    "all140_weight": ctx["weights"][j],
                    "center": fpair(center),
                    "radius_squared": fpair(radius2),
                })
    identity = {
        "primary_value": int(row["primary_value"]),
        "secondary_residue": int(row["secondary_residue"]),
        "fixed_x61_value": int(row["fixed_x61_value"]),
        "x60_residue": int(row["x60_residue"]),
        "fixed_x60_value": int(row["fixed_x60_value"]),
        "source_canonical_sha256": row["canonical_sha256"],
    }
    if residual_energy < 0:
        return {**identity, "status": "REAL_EMPTY_NORM_PLUS_P_NECESSARY_CONDITION", "conditioned_residual_energy": fpair(residual_energy), "selected_coordinate": None, "intervals": [], "interval_child_count": 0}
    if not candidates:
        return {**identity, "status": "INTEGER_PROJECTION_EMPTY_NORM_PLUS_P_NECESSARY_CONDITION", "conditioned_residual_energy": fpair(residual_energy), "selected_coordinate": None, "intervals": [], "interval_child_count": 0}
    chosen = min(candidates, key=lambda z: (z["domain_size"], -z["all140_weight"], z["coordinate_0based"]))
    lo, hi = chosen["bound"]
    n = hi - lo + 1
    shard_count = min(MAX_SHARDS, n)
    intervals = [[lo + (n * r) // shard_count, lo + (n * (r + 1)) // shard_count - 1] for r in range(shard_count)]
    if intervals[0][0] != lo or intervals[-1][1] != hi:
        raise SystemExit("partition endpoint failure")
    for left, right in zip(intervals, intervals[1:]):
        if left[1] + 1 != right[0]:
            raise SystemExit("partition gap/overlap")
    if int(chosen["coordinate_0based"]) in FORBIDDEN_SPLIT:
        raise SystemExit("forbidden coordinate selected")
    return {**identity, "status": "ADAPTIVE_AFFINE_CONDITIONED_SPLIT", "conditioned_residual_energy": fpair(residual_energy), "selected_coordinate": chosen, "intervals": intervals, "interval_child_count": len(intervals)}

def main() -> None:
    verified = lock_before_parent_import()
    rows = residual_rows()
    parent = importlib.import_module("run_mb104_000707_fibration_shell_local_exact")
    ctx = build_context(parent)
    leaves = [exact_leaf_contract(ctx, row) for row in rows]
    split = [r for r in leaves if r["status"] == "ADAPTIVE_AFFINE_CONDITIONED_SPLIT"]
    empty = [r for r in leaves if r["status"] != "ADAPTIVE_AFFINE_CONDITIONED_SPLIT"]
    hist = {}
    domains = []
    total_children = 0
    for row in split:
        j = str(int(row["selected_coordinate"]["coordinate_0based"]))
        hist[j] = hist.get(j, 0) + 1
        domains.append(int(row["selected_coordinate"]["domain_size"]))
        total_children += int(row["interval_child_count"])
    domains.sort()
    median = None
    if domains:
        m = len(domains)
        median = domains[m // 2] if m % 2 else [domains[m // 2 - 1], domains[m // 2]]
    out = {
        "schema": SCHEMA,
        "status": "COLD_ADAPTIVE_AFFINE_SUCCESSOR_DESIGNED_NO_HEAVY_EXECUTION_NO_CREDIT",
        "source_generation": 23,
        "carried_complete_x60_singletons": 281,
        "residual_timeout_leaf_count": 30,
        "recompute_carried_complete_regions": False,
        "retired_successor_coordinate_0based": 59,
        "forbidden_split_coordinates_0based": sorted(FORBIDDEN_SPLIT),
        "method": "PER_LEAF_AFFINE_CONDITIONED_DUAL_ELLIPSOID",
        "selection_rule": "MIN_EXACT_AFFINE_CONDITIONAL_INTEGER_DOMAIN__MAX_ALL140_ABS_LINEAR_WEIGHT__MIN_INDEX__EXCLUDING_X59_X60_X61_X62",
        "source_locks_verified_before_parent_import": verified,
        "residual_file_sha256": hashlib.sha256(RESIDUAL.read_bytes()).hexdigest(),
        "leaves": leaves,
        "summary": {
            "split_leaf_count": len(split),
            "necessary_condition_empty_leaf_count": len(empty),
            "selected_coordinate_histogram": hist,
            "total_interval_child_count": total_children,
            "maximum_interval_child_count": 240,
            "maximum_conditional_domain": max(domains) if domains else 0,
            "median_conditional_domain": median,
            "planned_effective_heavy_concurrency_after_future_audit": 4,
        },
        "heavy_surface_present": False,
        "heavy_armed": False,
        "execution_authorized": False,
        "credit_firewall": {
            "numerical_fibration_shell_credit": False,
            "effectivity_credit": False,
            "semiampleness_credit": False,
            "global_fibration_optimum_credit": False,
            "MB104_complete": False,
            "stage32_03_complete": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    if len(leaves) != 30 or any(r.get("selected_coordinate") and int(r["selected_coordinate"]["coordinate_0based"]) == 59 for r in leaves):
        raise SystemExit("successor design invariant failure")
    if total_children > 240:
        raise SystemExit("successor child-count budget exceeded")
    out["canonical_sha256_without_this_field"] = csha(out)
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
