#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import time

from aut_equivariant_pairing_adapter import (
    AutEquivariantPrefixCanonicalAugmentation,
    EquivariantPrefixMembershipOracle,
    NORMAL_LABEL_MAX,
)
from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import RETAINED_BUNDLE_SHA256, RetainedBasisPairingTransform

SCHEMA = "STAGE32_RESIDUAL32_01_AUT_EQUIVARIANT_ALL140_CALIBRATION_V4"
COORDINATE_MODEL = "AUT_EQUIVARIANT_ALL140_KNOWN_CURVE_PAIRINGS_TO_PICARD64_HNF"
AUT_MODE = "EXACT_AUT1536_ALL140_GLOBAL_BUDGET_CLASS_PREFIX_STABILIZER_LEX_MIN"
SELECTED_ASSIGNMENT_ORDER = [0, 1, 2, 3, 61, 4, 5, 6, 7, 8, 9]
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
    oracle: EquivariantPrefixMembershipOracle,
    aut: AutEquivariantPrefixCanonicalAugmentation,
    known_labels_1based: list[int],
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
        if depth == len(known_labels_1based):
            terminal_prefixes += 1
            terminal_hash.update(json.dumps(values, separators=(",", ":")).encode() + b"\n")
            return
        label = known_labels_1based[depth]
        is_exceptional = label > NORMAL_LABEL_MAX
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
        "known_label_order_1based": known_labels_1based,
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
        "credit_scope": "ALL140_PAIRING_LATTICE_AND_PREFIX_AUT_COST_PROFILE_ONLY",
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
    selected_known = transform.certificate["selected_known_indices_1based"]
    known_labels = [selected_known[i] for i in SELECTED_ASSIGNMENT_ORDER]
    assert known_labels == [93, 94, 95, 96, 49, 97, 98, 99, 101, 102, 103]

    marking = load_module_payload(args.marking, "stage32_marking_retained")
    adapter_started = time.perf_counter()
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    adapter_seconds = time.perf_counter() - adapter_started

    oracle_started = time.perf_counter()
    oracle = EquivariantPrefixMembershipOracle(adapter, known_labels)
    oracle_seconds = time.perf_counter() - oracle_started

    aut_payload = marking["aut_action"]
    aut_started = time.perf_counter()
    aut = AutEquivariantPrefixCanonicalAugmentation(
        aut_payload["permutations_1based"],
        known_labels,
        aut_payload["canonical_sha256_without_this_field"],
    )
    aut_seconds = time.perf_counter() - aut_started

    profiles = [run_probe(oracle, aut, known_labels, rep, args.node_limit) for rep in REPRESENTATIVES]
    oracle_certificate = oracle.certificate()
    active_by_depth = [c["active_congruence_rows"] for c in oracle_certificate["checks"]]
    aut_certificate = aut.certificate()
    prefix_actions = [c["distinct_prefix_actions"] for c in aut_certificate["checks"]]
    gen6_regression = adapter.certificate["generation6_hnf_regression"]

    payload = {
        "schema": SCHEMA,
        "engine": "LOCAL_OFFLINE_EXACT_ALL140_PAIRING_IMAGE_HNF_PLUS_PREFIX_AUT1536_V4",
        "coordinate_model": COORDINATE_MODEL,
        "selected_assignment_order_source": "LOCKED_FROM_GENERATION6_DISCRIMINANT_ACTIVE_SELECTION",
        "selected_assignment_order": SELECTED_ASSIGNMENT_ORDER,
        "known_label_order_1based": known_labels,
        "gen6_depth5_active_known_label_1based": 49,
        "generation6_hnf_regression": gen6_regression,
        "saturated_picard64_integral_adapter_validated": adapter.certificate["saturated_picard64_integral_adapter_validated"],
        "active_congruence_rows_by_depth": active_by_depth,
        "first_active_depth": next((i + 1 for i, n in enumerate(active_by_depth) if n > 0), None),
        "retained_picard_bundle_sha256": RETAINED_BUNDLE_SHA256,
        "retained_marking_sha256": marking["canonical_sha256"],
        "retained_aut_action_sha256": marking["stage32_aut_action_sha256"],
        "selected64_transform_certificate": transform.certificate,
        "adapter_certificate": adapter.certificate,
        "adapter_build_seconds": round(adapter_seconds, 6),
        "oracle_certificate": oracle_certificate,
        "oracle_build_seconds": round(oracle_seconds, 6),
        "aut_mode": AUT_MODE,
        "aut_certificate": aut_certificate,
        "aut_build_seconds": round(aut_seconds, 6),
        "aut_used_in_probe": True,
        "prefix_aut_canonical_augmentation_implemented": True,
        "full_aut_group_order": aut.group_order,
        "global_budget_class_preserving_subgroup_size": aut.global_budget_subgroup_size,
        "distinct_prefix_actions_by_depth": prefix_actions,
        "selected64_setwise_preservation_required": False,
        "representatives": profiles,
        "representative_m_classes": [1, 2, 4, 8],
        "full_178_row_sweep_authorized": False,
        "B18_RELEASE_AUTHORIZED": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2": "NOT_DISCHARGED",
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "next_engineering_gate": "AUT_EQUIVARIANT_ALL140_REPRESENTATIVE_COST_RESULT_REVIEW",
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "schema": SCHEMA,
        "known_labels": known_labels,
        "adapter_paths": list(adapter.discovery_paths),
        "adapter_modes": list(adapter.discovery_modes),
        "saturated_adapter_validated": payload["saturated_picard64_integral_adapter_validated"],
        "gen6_hnf_exact": gen6_regression["exact_match"],
        "active_rows": active_by_depth,
        "full_aut_group_order": aut.group_order,
        "global_budget_subgroup_size": aut.global_budget_subgroup_size,
        "prefix_actions": prefix_actions,
        "nodes": {str(p["m"]): p["nodes_visited"] for p in profiles},
        "membership_prunes": {str(p["m"]): p["membership_prunes"] for p in profiles},
        "symmetry_prunes": {str(p["m"]): p["symmetry_prunes"] for p in profiles},
        "terminals": {str(p["m"]): p["terminal_prefixes_before_stop"] for p in profiles},
        "adapter_build_seconds": payload["adapter_build_seconds"],
        "oracle_build_seconds": payload["oracle_build_seconds"],
        "aut_build_seconds": payload["aut_build_seconds"],
        "sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
