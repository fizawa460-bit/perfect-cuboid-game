#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import pathlib
import time

from aut_equivariant_pairing_adapter import (
    AutEquivariantPrefixCanonicalAugmentation,
    EquivariantPrefixMembershipOracle,
    NORMAL_LABEL_MAX,
)
from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import RETAINED_BUNDLE_SHA256

ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "full178-manifest.json"
KNOWN_LABEL_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
SCHEMA = "STAGE32_RESIDUAL32_01_FULL178_PREFIX_WORK_UNIT_V1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module_payload(path: pathlib.Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-")
    return int(g[1:]), int(d[1:])


def manifest_rows() -> dict[str, int]:
    x = json.loads(MANIFEST.read_text())
    digest = x.pop("canonical_sha256_without_this_field")
    assert csha(x) == digest == EXPECTED_MANIFEST_SHA256
    out: dict[str, int] = {}
    for m_text, ids in x["m_class_rows"].items():
        for row_id in ids:
            assert row_id not in out
            out[row_id] = int(m_text)
    assert len(out) == 178
    return out


def budget_state(labels: list[int], prefix: list[int], e: int, d: int) -> tuple[int, int]:
    exceptional = 0
    normal = 0
    for label, value in zip(labels, prefix):
        if label > NORMAL_LABEL_MAX:
            exceptional += value
        else:
            normal += value
    assert exceptional <= e
    assert normal <= 19 * d - 5 * e
    return exceptional, normal


def next_upper(labels: list[int], prefix: list[int], e: int, d: int) -> int:
    exceptional, normal = budget_state(labels, prefix, e, d)
    label = labels[len(prefix)]
    if label > NORMAL_LABEL_MAX:
        return e - exceptional
    return 19 * d - 5 * e - normal


def run_partition(oracle, aut, labels: list[int], *, e: int, d: int, node_limit: int,
                  prefix: list[int], next_min: int | None, next_max: int | None) -> dict:
    if prefix and (not oracle.feasible(prefix) or not aut.canonical(prefix)):
        return {"complete": True, "nodes": 0, "membership_prunes": 0, "symmetry_prunes": 0,
                "terminal_count": 0, "terminal_stream_sha256": hashlib.sha256().hexdigest(),
                "elapsed_seconds": 0.0, "empty_by_prefix_filter": True}
    budget_state(labels, prefix, e, d)
    values = list(prefix)
    nodes = membership = symmetry = terminals = 0
    exhausted = False
    terminal_hash = hashlib.sha256()
    started = time.perf_counter()
    start_depth = len(prefix)

    def dfs(depth: int, exceptional_used: int, normal_used: int) -> None:
        nonlocal nodes, membership, symmetry, terminals, exhausted
        if exhausted:
            return
        if depth == len(labels):
            terminals += 1
            terminal_hash.update(json.dumps(values, separators=(",", ":")).encode() + b"\n")
            return
        label = labels[depth]
        upper = e - exceptional_used if label > NORMAL_LABEL_MAX else 19 * d - 5 * e - normal_used
        lo, hi = 0, upper
        if depth == start_depth and next_min is not None:
            lo = max(lo, int(next_min))
        if depth == start_depth and next_max is not None:
            hi = min(hi, int(next_max))
        if lo > hi:
            return
        for value in range(lo, hi + 1):
            nodes += 1
            if nodes > node_limit:
                exhausted = True
                return
            values.append(value)
            if not oracle.feasible(values):
                membership += 1
            elif not aut.canonical(values):
                symmetry += 1
            elif label > NORMAL_LABEL_MAX:
                dfs(depth + 1, exceptional_used + value, normal_used)
            else:
                dfs(depth + 1, exceptional_used, normal_used + value)
            values.pop()
            if exhausted:
                return

    ex0, no0 = budget_state(labels, prefix, e, d)
    dfs(start_depth, ex0, no0)
    return {
        "complete": not exhausted,
        "nodes": min(nodes, node_limit),
        "membership_prunes": membership,
        "symmetry_prunes": symmetry,
        "terminal_count": terminals,
        "terminal_stream_sha256": terminal_hash.hexdigest(),
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "empty_by_prefix_filter": False,
    }


def normalize_unit(unit: dict) -> dict:
    kind = unit["kind"]
    out = {"kind": kind, "row_id": unit["row_id"]}
    if kind == "ROW_TAIL":
        out["e_start"] = int(unit["e_start"])
    elif kind == "STRATUM_PARTITION":
        out["e"] = int(unit["e"])
        out["prefix"] = [int(v) for v in unit.get("prefix", [])]
        out["next_min"] = int(unit["next_min"])
        out["next_max"] = int(unit["next_max"])
    else:
        raise ValueError(f"unknown work-unit kind: {kind}")
    out["work_unit_id"] = "wu-" + csha(out)[:20]
    return out


def split_partition(unit: dict, *, e: int, d: int, labels: list[int]) -> list[dict]:
    prefix = list(unit.get("prefix", []))
    lo = int(unit["next_min"])
    hi = int(unit["next_max"])
    if lo < hi:
        mid = (lo + hi) // 2
        return [normalize_unit({"kind": "STRATUM_PARTITION", "row_id": unit["row_id"], "e": e,
                                "prefix": prefix, "next_min": lo, "next_max": mid}),
                normalize_unit({"kind": "STRATUM_PARTITION", "row_id": unit["row_id"], "e": e,
                                "prefix": prefix, "next_min": mid + 1, "next_max": hi})]
    new_prefix = prefix + [lo]
    if len(new_prefix) >= len(labels):
        raise RuntimeError("single-leaf partition exceeded node ceiling")
    upper = next_upper(labels, new_prefix, e, d)
    mid = upper // 2
    children = [normalize_unit({"kind": "STRATUM_PARTITION", "row_id": unit["row_id"], "e": e,
                                "prefix": new_prefix, "next_min": 0, "next_max": mid})]
    if mid < upper:
        children.append(normalize_unit({"kind": "STRATUM_PARTITION", "row_id": unit["row_id"], "e": e,
                                       "prefix": new_prefix, "next_min": mid + 1, "next_max": upper}))
    return children


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=pathlib.Path, required=True)
    ap.add_argument("--marking", type=pathlib.Path, required=True)
    ap.add_argument("--work-unit-json", required=True)
    ap.add_argument("--node-limit", type=int, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    rows = manifest_rows()
    unit = normalize_unit(json.loads(args.work_unit_json))
    row_id = unit["row_id"]
    if row_id not in rows:
        raise ValueError(f"row not in audited residual manifest: {row_id}")
    genus, degree = parse_row_id(row_id)
    m = 16 // math.gcd(degree, 16)
    assert rows[row_id] == m
    emin = 8 if genus == 0 else 4
    emax = (19 * degree) // 5

    bundle = load_module_payload(args.retained, "stage32_picard_retained")
    assert bundle["canonical_sha256"] == RETAINED_BUNDLE_SHA256
    marking = load_module_payload(args.marking, "stage32_marking_retained")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    oracle = EquivariantPrefixMembershipOracle(adapter, KNOWN_LABEL_ORDER)
    aut = AutEquivariantPrefixCanonicalAugmentation(
        marking["aut_action"]["permutations_1based"], KNOWN_LABEL_ORDER,
        marking["aut_action"]["canonical_sha256_without_this_field"],
    )

    remaining = args.node_limit
    completed: list[dict] = []
    unresolved: list[dict] = []
    telemetry: list[dict] = []

    if unit["kind"] == "ROW_TAIL":
        start = max(emin, int(unit["e_start"]))
        for e in range(start, emax + 1):
            if remaining <= 0:
                unresolved.append(normalize_unit({"kind": "ROW_TAIL", "row_id": row_id, "e_start": e}))
                break
            root = normalize_unit({"kind": "STRATUM_PARTITION", "row_id": row_id, "e": e,
                                   "prefix": [], "next_min": 0, "next_max": e})
            result = run_partition(oracle, aut, KNOWN_LABEL_ORDER, e=e, d=degree,
                                   node_limit=remaining, prefix=[], next_min=0, next_max=e)
            remaining -= result["nodes"]
            telemetry.append({"e": e, "work_unit_id": root["work_unit_id"], **result})
            if result["complete"]:
                completed.append({"e": e, "partition": root, "terminal_count": result["terminal_count"],
                                  "terminal_stream_sha256": result["terminal_stream_sha256"]})
                continue
            unresolved.extend(split_partition(root, e=e, d=degree, labels=KNOWN_LABEL_ORDER))
            if e < emax:
                unresolved.append(normalize_unit({"kind": "ROW_TAIL", "row_id": row_id, "e_start": e + 1}))
            break
    else:
        e = int(unit["e"])
        assert emin <= e <= emax
        result = run_partition(oracle, aut, KNOWN_LABEL_ORDER, e=e, d=degree,
                               node_limit=remaining, prefix=unit["prefix"],
                               next_min=unit["next_min"], next_max=unit["next_max"])
        telemetry.append({"e": e, "work_unit_id": unit["work_unit_id"], **result})
        if result["complete"]:
            completed.append({"e": e, "partition": unit, "terminal_count": result["terminal_count"],
                              "terminal_stream_sha256": result["terminal_stream_sha256"]})
        else:
            unresolved.extend(split_partition(unit, e=e, d=degree, labels=KNOWN_LABEL_ORDER))

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "phase": "FULL178_EXACT_PAIRING_PREFIX_PRODUCTION",
        "prefix_stage_only": True,
        "row_id": row_id,
        "genus": genus,
        "degree": degree,
        "m": m,
        "exceptional_mass_range": [emin, emax],
        "input_work_unit": unit,
        "node_limit": args.node_limit,
        "nodes_used": args.node_limit - remaining,
        "completed_prefix_partitions": completed,
        "unresolved_exact_child_work_units": unresolved,
        "telemetry": telemetry,
        "unknown_count": len(unresolved),
        "unknown_is_unsat": False,
        "row_prefix_stage_complete": len(unresolved) == 0,
        "numerical_row_complete": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2": "NOT_DISCHARGED",
        "B18_RELEASE_AUTHORIZED": False,
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "PERFECT_CUBOID_EXISTENCE_CLAIM": False,
        "PERFECT_CUBOID_NONEXISTENCE_CLAIM": False,
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"row_id": row_id, "nodes_used": payload["nodes_used"],
                      "completed": len(completed), "unresolved": len(unresolved),
                      "sha256": payload["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
