#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import time

from pairing_prefix_engine import (
    PairingTransform,
    PrefixMembershipOracle,
    canonical_pairing_key,
    close_permutation_group,
)

SCHEMA = "STAGE32_RESIDUAL32_01_PAIRING_PREFIX_CALIBRATION_V1"
ASSIGNMENT_ORDER = list(range(10)) + [48]
REPRESENTATIVES = [
    {"m": 1, "genus": 0, "degree": 16, "exceptional_mass": 8},
    {"m": 2, "genus": 0, "degree": 8, "exceptional_mass": 8},
    {"m": 4, "genus": 0, "degree": 12, "exceptional_mass": 8},
    {"m": 8, "genus": 0, "degree": 10, "exceptional_mass": 8},
]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def run_probe(oracle: PrefixMembershipOracle, rep: dict, node_limit: int) -> dict:
    e = int(rep["exceptional_mass"])
    d = int(rep["degree"])
    normal_mass = 19 * d - 5 * e
    values: list[int] = []
    nodes = 0
    membership_prunes = 0
    terminal_prefixes = 0
    terminal_hash = hashlib.sha256()
    exhausted = False
    max_depth_reached = 0
    started = time.perf_counter()

    def dfs(depth: int, exceptional_used: int, normal_used: int) -> None:
        nonlocal nodes, membership_prunes, terminal_prefixes, exhausted, max_depth_reached
        if exhausted:
            return
        max_depth_reached = max(max_depth_reached, depth)
        if depth == len(ASSIGNMENT_ORDER):
            terminal_prefixes += 1
            terminal_hash.update(json.dumps(values, separators=(",", ":")).encode() + b"\n")
            return
        idx = ASSIGNMENT_ORDER[depth]
        upper = e - exceptional_used if idx < 48 else normal_mass - normal_used
        for value in range(upper + 1):
            nodes += 1
            if nodes > node_limit:
                exhausted = True
                return
            values.append(value)
            if oracle.feasible(values):
                if idx < 48:
                    dfs(depth + 1, exceptional_used + value, normal_used)
                else:
                    dfs(depth + 1, exceptional_used, normal_used + value)
            else:
                membership_prunes += 1
            values.pop()
            if exhausted:
                return

    dfs(0, 0, 0)
    return {
        **rep,
        "normal_mass": normal_mass,
        "assignment_order": ASSIGNMENT_ORDER,
        "node_limit": node_limit,
        "nodes_visited": min(nodes, node_limit),
        "membership_prunes": membership_prunes,
        "terminal_prefixes_before_stop": terminal_prefixes,
        "terminal_prefix_stream_sha256": terminal_hash.hexdigest(),
        "max_depth_reached": max_depth_reached,
        "node_budget_exhausted": exhausted,
        "probe_complete": not exhausted,
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "credit_scope": "PAIRING_LATTICE_PREFIX_COST_PROFILE_ONLY",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--aut", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--node-limit", type=int, default=250000)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    transform = PairingTransform.from_core(core)
    t0 = time.perf_counter()
    oracle = PrefixMembershipOracle(transform, ASSIGNMENT_ORDER)
    oracle_seconds = time.perf_counter() - t0

    aut = json.loads(args.aut.read_text())
    group = close_permutation_group(aut["permutations_1based"])
    assert len(group) == 1536

    gram = core["basis_gram"]
    h = core["hyperplane"]
    known = core["known_classes"]

    def pairing(u, v):
        return sum(int(u[i]) * int(gram[i][j]) * int(v[j]) for i in range(64) for j in range(64))

    hp = tuple(pairing(cls, h) for cls in known)
    assert canonical_pairing_key(hp, group) == hp

    profiles = [run_probe(oracle, rep, args.node_limit) for rep in REPRESENTATIVES]
    payload = {
        "schema": SCHEMA,
        "engine": "LOCAL_OFFLINE_EXACT_SELECTED_PAIRING_PREFIX_HNF_MEMBERSHIP_V1",
        "transform_certificate": transform.certificate,
        "oracle_certificate": oracle.certificate(),
        "oracle_build_seconds": round(oracle_seconds, 6),
        "aut_group_order": len(group),
        "leaf_aut_canonicalization_exact": True,
        "prefix_aut_canonical_augmentation_implemented": False,
        "representatives": profiles,
        "representative_m_classes": [1, 2, 4, 8],
        "full_178_row_sweep_authorized": False,
        "B18_RELEASE_AUTHORIZED": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2": "NOT_DISCHARGED",
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "next_engineering_gate": "EXACT_PREFIX_AUT_CANONICAL_AUGMENTATION_AND_LEAF_COST_ADAPTER",
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "schema": SCHEMA,
        "aut_group_order": len(group),
        "m_classes": payload["representative_m_classes"],
        "nodes": {str(p["m"]): p["nodes_visited"] for p in profiles},
        "prunes": {str(p["m"]): p["membership_prunes"] for p in profiles},
        "sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
