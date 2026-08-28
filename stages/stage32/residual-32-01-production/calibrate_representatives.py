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
from prefix_aut1536 import PrefixAut1536CanonicalAugmentation

SCHEMA = "STAGE32_RESIDUAL32_01_PREFIX_AUT1536_CALIBRATION_V3"
COORDINATE_MODEL = "DISCRIMINANT_ACTIVE_RAW_PAIRING_COORDINATES_HNF_SELECTED"
AUT_MODE = "EXACT_AUT1536_SELECTED64_BUDGET_CLASS_COMPATIBLE_PREFIX_STABILIZER_LEX_MIN"
EXCEPTIONAL_BASIS_COUNT = len(EXCEPTIONAL_BASIS_POSITIONS)
ASSIGNMENT_ORDER = [0, 1, 2, 3, 61, 4, 5, 6, 7, 8, 9]
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


def load_module_payload(path: pathlib.Path, module_name: str) -> dict:
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained payload: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def run_probe(
    oracle: PrefixMembershipOracle,
    aut: PrefixAut1536CanonicalAugmentation,
    rep: dict,
    node_limit: int,
) -> dict:
    e = int(rep["exceptional_mass"])
    d = int(rep["degree"])
    normal_mass = 19 * d - 5 * e
    values: list[int] = []
    nodes = 0
    membership_prunes = 0
    symmetry_prunes = 0
    terminal_prefixes = 0
    terminal_hash = hashlib.sha256()
    exhausted = False
    max_depth_reached = 0
    started = time.perf_counter()

    def dfs(depth: int, exceptional_used: int, normal_used: int) -> None:
        nonlocal nodes, membership_prunes, symmetry_prunes, terminal_prefixes, exhausted, max_depth_reached
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
            if not oracle.feasible(values):
                membership_prunes += 1
            elif not aut.canonical(values):
                symmetry_prunes += 1
            else:
                if is_exceptional:
                    dfs(depth + 1, exceptional_used + value, normal_used)
                else:
                    dfs(depth + 1, exceptional_used, normal_used + value)
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
        "symmetry_prunes": symmetry_prunes,
        "total_exact_prunes": membership_prunes + symmetry_prunes,
        "terminal_prefixes_before_stop": terminal_prefixes,
        "terminal_prefix_stream_sha256": terminal_hash.hexdigest(),
        "max_depth_reached": max_depth_reached,
        "node_budget_exhausted": exhausted,
        "probe_complete": not exhausted,
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "credit_scope": "PAIRING_LATTICE_AND_PREFIX_AUT_COST_PROFILE_ONLY",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=pathlib.Path, required=True)
    ap.add_argument("--marking", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--node-limit", type=int, default=250000)
    args = ap.parse_args()

    bundle = load_module_payload(args.retained, "stage32_picard_retained")
    assert bundle["canonical_sha256"] == RETAINED_BUNDLE_SHA256
    transform = RetainedBasisPairingTransform.from_bundle(bundle)

    oracle_started = time.perf_counter()
    oracle = PrefixMembershipOracle(transform, ASSIGNMENT_ORDER)
    oracle_seconds = time.perf_counter() - oracle_started

    marking = load_module_payload(args.marking, "stage32_marking_retained")
    aut_payload = marking["aut_action"]
    aut_started = time.perf_counter()
    aut = PrefixAut1536CanonicalAugmentation(
        aut_payload["permutations_1based"],
        transform.certificate["selected_known_indices_1based"],
        EXCEPTIONAL_BASIS_COUNT,
        ASSIGNMENT_ORDER,
        aut_payload["canonical_sha256_without_this_field"],
    )
    aut_seconds = time.perf_counter() - aut_started

    profiles = [run_probe(oracle, aut, rep, args.node_limit) for rep in REPRESENTATIVES]
    active_by_depth = [
        c["active_congruence_rows"] for c in oracle.certificate()["checks"]
    ]
    aut_certificate = aut.certificate()
    payload = {
        "schema": SCHEMA,
        "engine": "LOCAL_OFFLINE_EXACT_HNF_PLUS_PREFIX_AUT1536_CANONICAL_AUGMENTATION_V3",
        "coordinate_model": COORDINATE_MODEL,
        "assignment_order_source": "LOCKED_FROM_GENERATION6_DISCRIMINANT_ACTIVE_SELECTION",
        "assignment_order": ASSIGNMENT_ORDER,
        "active_congruence_rows_by_depth": active_by_depth,
        "first_active_depth": next((i + 1 for i, n in enumerate(active_by_depth) if n > 0), None),
        "retained_picard_bundle_sha256": RETAINED_BUNDLE_SHA256,
        "retained_marking_sha256": marking["canonical_sha256"],
        "retained_aut_action_sha256": marking["stage32_aut_action_sha256"],
        "transform_certificate": transform.certificate,
        "oracle_certificate": oracle.certificate(),
        "oracle_build_seconds": round(oracle_seconds, 6),
        "aut_mode": AUT_MODE,
        "aut_certificate": aut_certificate,
        "aut_build_seconds": round(aut_seconds, 6),
        "aut_used_in_probe": True,
        "prefix_aut_canonical_augmentation_implemented": True,
        "full_aut_group_order": aut.group_order,
        "selected_coordinate_compatible_subgroup_size": aut.compatible_subgroup_size,
        "exceptional_basis_coordinate_count": EXCEPTIONAL_BASIS_COUNT,
        "curve_basis_coordinate_count": 64 - EXCEPTIONAL_BASIS_COUNT,
        "representatives": profiles,
        "representative_m_classes": [1, 2, 4, 8],
        "full_178_row_sweep_authorized": False,
        "B18_RELEASE_AUTHORIZED": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2": "NOT_DISCHARGED",
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "next_engineering_gate": "PREFIX_AUT1536_REPRESENTATIVE_COST_RESULT_REVIEW",
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "schema": SCHEMA,
        "assignment_order": ASSIGNMENT_ORDER,
        "active_rows": active_by_depth,
        "full_aut_group_order": aut.group_order,
        "compatible_subgroup_size": aut.compatible_subgroup_size,
        "prefix_actions": [c["distinct_prefix_actions"] for c in aut_certificate["checks"]],
        "nodes": {str(p["m"]): p["nodes_visited"] for p in profiles},
        "membership_prunes": {str(p["m"]): p["membership_prunes"] for p in profiles},
        "symmetry_prunes": {str(p["m"]): p["symmetry_prunes"] for p in profiles},
        "terminals": {str(p["m"]): p["terminal_prefixes_before_stop"] for p in profiles},
        "oracle_build_seconds": payload["oracle_build_seconds"],
        "aut_build_seconds": payload["aut_build_seconds"],
        "sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
