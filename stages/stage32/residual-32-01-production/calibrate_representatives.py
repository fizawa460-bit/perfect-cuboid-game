#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import time

from pairing_prefix_engine import (
    EXCEPTIONAL_BASIS_POSITIONS,
    RETAINED_BUNDLE_SHA256,
    RetainedBasisPairingTransform,
    PrefixMembershipOracle,
)

SCHEMA = "STAGE32_RESIDUAL32_01_RETAINED_BASIS_PREFIX_CALIBRATION_V1"
EXCEPTIONAL_BASIS_COUNT = len(EXCEPTIONAL_BASIS_POSITIONS)
ASSIGNMENT_ORDER = list(range(10)) + [EXCEPTIONAL_BASIS_COUNT]
REPRESENTATIVES = [
    {"m": 1, "genus": 0, "degree": 16, "exceptional_mass": 8},
    {"m": 2, "genus": 0, "degree": 8, "exceptional_mass": 8},
    {"m": 4, "genus": 0, "degree": 12, "exceptional_mass": 8},
    {"m": 8, "genus": 0, "degree": 10, "exceptional_mass": 8},
]


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_retained(path: pathlib.Path) -> dict:
    spec = importlib.util.spec_from_file_location("stage32_picard_retained", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained bundle: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    payload = mod.load()
    assert payload["canonical_sha256"] == RETAINED_BUNDLE_SHA256
    return payload


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
        is_exceptional = idx < EXCEPTIONAL_BASIS_COUNT
        upper = e - exceptional_used if is_exceptional else normal_mass - normal_used
        for value in range(upper + 1):
            nodes += 1
            if nodes > node_limit:
                exhausted = True
                return
            values.append(value)
            if oracle.feasible(values):
                if is_exceptional:
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
        "exceptional_basis_coordinate_count": EXCEPTIONAL_BASIS_COUNT,
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
    ap.add_argument("--retained", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--node-limit", type=int, default=250000)
    args = ap.parse_args()

    bundle = load_retained(args.retained)
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    t0 = time.perf_counter()
    oracle = PrefixMembershipOracle(transform, ASSIGNMENT_ORDER)
    oracle_seconds = time.perf_counter() - t0

    profiles = [run_probe(oracle, rep, args.node_limit) for rep in REPRESENTATIVES]
    payload = {
        "schema": SCHEMA,
        "engine": "LOCAL_OFFLINE_EXACT_RETAINED_BASIS_PAIRING_PREFIX_HNF_MEMBERSHIP_V1",
        "coordinate_model": "RETAINED_PRIMITIVE_BASIS_PAIRINGS_EXCEPTIONALS_FIRST",
        "retained_picard_bundle_sha256": RETAINED_BUNDLE_SHA256,
        "transform_certificate": transform.certificate,
        "oracle_certificate": oracle.certificate(),
        "oracle_build_seconds": round(oracle_seconds, 6),
        "exceptional_basis_coordinate_count": EXCEPTIONAL_BASIS_COUNT,
        "curve_basis_coordinate_count": 64 - EXCEPTIONAL_BASIS_COUNT,
        "aut_used_in_probe": False,
        "leaf_aut_canonicalization_regressed_in_this_probe": False,
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
        "next_engineering_gate": "OFFLINE_AUT_PERMUTATION_RETENTION_AND_PREFIX_CANONICAL_AUGMENTATION",
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "schema": SCHEMA,
                "m_classes": payload["representative_m_classes"],
                "nodes": {str(p["m"]): p["nodes_visited"] for p in profiles},
                "prunes": {str(p["m"]): p["membership_prunes"] for p in profiles},
                "transform_denominator": transform.den,
                "sha256": payload["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
