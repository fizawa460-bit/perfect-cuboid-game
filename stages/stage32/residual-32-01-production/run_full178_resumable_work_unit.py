#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib

from aut_equivariant_pairing_adapter import (
    AutEquivariantPrefixCanonicalAugmentation,
    EquivariantPrefixMembershipOracle,
)
from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import RETAINED_BUNDLE_SHA256
from resumable_prefix_engine import run_resumable_dfs
from run_full178_prefix_work_unit import (
    KNOWN_LABEL_ORDER,
    csha,
    load_module_payload,
    manifest_rows,
    next_upper,
    normalize_unit,
    parse_row_id,
)

SCHEMA = "STAGE32_RESIDUAL32_01_FULL178_RESUMABLE_WORK_UNIT_V1"
CURSOR_KIND = "RESUMABLE_CURSOR"
EMPTY_CHAIN_SHA256 = hashlib.sha256().hexdigest()


def chain_step(previous: str, segment: dict) -> str:
    payload = (previous + "\n" + csha(segment)).encode()
    return hashlib.sha256(payload).hexdigest()


def normalize_cursor(
    source_unit: dict,
    *,
    e_current: int,
    continuation: dict | None,
    segment_chain_sha256: str,
    segment_count: int,
    terminal_count_accumulated: int,
    nodes_accumulated: int,
) -> dict:
    source = normalize_unit(source_unit)
    base = {
        "kind": CURSOR_KIND,
        "row_id": source["row_id"],
        "source_unit": source,
        "e_current": int(e_current),
        "continuation": continuation,
        "segment_chain_sha256": str(segment_chain_sha256),
        "segment_count": int(segment_count),
        "terminal_count_accumulated": int(terminal_count_accumulated),
        "nodes_accumulated": int(nodes_accumulated),
    }
    base["work_unit_id"] = "wu-r-" + csha(base)[:18]
    return base


def decode_input(raw: dict, *, emin: int) -> dict:
    if raw.get("kind") != CURSOR_KIND:
        source = normalize_unit(raw)
        if source["kind"] == "ROW_TAIL":
            e_current = max(emin, int(source["e_start"]))
        else:
            e_current = int(source["e"])
        return normalize_cursor(
            source,
            e_current=e_current,
            continuation=None,
            segment_chain_sha256=EMPTY_CHAIN_SHA256,
            segment_count=0,
            terminal_count_accumulated=0,
            nodes_accumulated=0,
        )

    source = normalize_unit(raw["source_unit"])
    assert raw["row_id"] == source["row_id"]
    rebuilt = normalize_cursor(
        source,
        e_current=int(raw["e_current"]),
        continuation=raw.get("continuation"),
        segment_chain_sha256=str(raw["segment_chain_sha256"]),
        segment_count=int(raw["segment_count"]),
        terminal_count_accumulated=int(raw["terminal_count_accumulated"]),
        nodes_accumulated=int(raw["nodes_accumulated"]),
    )
    assert raw["work_unit_id"] == rebuilt["work_unit_id"]
    return rebuilt


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=pathlib.Path, required=True)
    ap.add_argument("--marking", type=pathlib.Path, required=True)
    ap.add_argument("--work-unit-json", required=True)
    ap.add_argument("--node-limit", type=int, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    rows = manifest_rows()
    raw = json.loads(args.work_unit_json)
    raw_row_id = raw["row_id"]
    if raw_row_id not in rows:
        raise ValueError(f"row not in audited residual manifest: {raw_row_id}")
    genus, degree = parse_row_id(raw_row_id)
    m = 16 // math.gcd(degree, 16)
    assert rows[raw_row_id] == m
    emin = 8 if genus == 0 else 4
    emax = (19 * degree) // 5
    unit = decode_input(raw, emin=emin)
    source = unit["source_unit"]
    row_id = unit["row_id"]

    bundle = load_module_payload(args.retained, "stage32_picard_retained_resumable")
    assert bundle["canonical_sha256"] == RETAINED_BUNDLE_SHA256
    marking = load_module_payload(args.marking, "stage32_marking_retained_resumable")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    oracle = EquivariantPrefixMembershipOracle(adapter, KNOWN_LABEL_ORDER)
    aut = AutEquivariantPrefixCanonicalAugmentation(
        marking["aut_action"]["permutations_1based"],
        KNOWN_LABEL_ORDER,
        marking["aut_action"]["canonical_sha256_without_this_field"],
    )

    remaining = int(args.node_limit)
    if remaining < 0:
        raise ValueError("node limit must be nonnegative")
    e_current = int(unit["e_current"])
    continuation = unit.get("continuation")
    chain = str(unit["segment_chain_sha256"])
    segment_count = int(unit["segment_count"])
    terminal_acc = int(unit["terminal_count_accumulated"])
    nodes_acc = int(unit["nodes_accumulated"])
    completed: list[dict] = []
    telemetry: list[dict] = []
    unresolved: list[dict] = []

    if source["kind"] == "STRATUM_PARTITION":
        e_last = e_current
    else:
        e_last = emax

    while e_current <= e_last:
        if source["kind"] == "STRATUM_PARTITION":
            assert e_current == int(source["e"])
            fixed_prefix = list(source["prefix"])
            root_lo = int(source["next_min"])
            root_hi = int(source["next_max"])
            partition = source
        else:
            fixed_prefix = []
            root_lo = 0
            root_hi = e_current
            partition = normalize_unit(
                {
                    "kind": "STRATUM_PARTITION",
                    "row_id": row_id,
                    "e": e_current,
                    "prefix": [],
                    "next_min": 0,
                    "next_max": e_current,
                }
            )

        if continuation is None and fixed_prefix and (
            not oracle.feasible(fixed_prefix) or not aut.canonical(fixed_prefix)
        ):
            segment = {
                "e": e_current,
                "nodes": 0,
                "membership_prunes": 0,
                "symmetry_prunes": 0,
                "terminal_count": 0,
                "terminal_stream_sha256": hashlib.sha256().hexdigest(),
                "complete": True,
                "empty_by_prefix_filter": True,
            }
            telemetry.append(segment)
            chain = chain_step(chain, segment)
            segment_count += 1
        else:
            out = run_resumable_dfs(
                labels=KNOWN_LABEL_ORDER,
                fixed_prefix=fixed_prefix,
                root_lo=root_lo,
                root_hi=root_hi,
                node_limit=remaining,
                upper_for_prefix=lambda p, e=e_current: next_upper(KNOWN_LABEL_ORDER, p, e, degree),
                feasible=oracle.feasible,
                canonical=aut.canonical,
                continuation=continuation,
                capture_terminals=False,
            )
            segment = {
                "e": e_current,
                "nodes": out.nodes,
                "membership_prunes": out.membership_prunes,
                "symmetry_prunes": out.symmetry_prunes,
                "terminal_count": out.terminal_count,
                "terminal_stream_sha256": out.terminal_stream_sha256,
                "complete": out.complete,
                "empty_by_prefix_filter": False,
            }
            telemetry.append(segment)
            remaining -= out.nodes
            nodes_acc += out.nodes
            terminal_acc += out.terminal_count
            chain = chain_step(chain, segment)
            segment_count += 1
            continuation = out.continuation

            if not out.complete:
                unresolved.append(
                    normalize_cursor(
                        source,
                        e_current=e_current,
                        continuation=continuation,
                        segment_chain_sha256=chain,
                        segment_count=segment_count,
                        terminal_count_accumulated=terminal_acc,
                        nodes_accumulated=nodes_acc,
                    )
                )
                break

        completed.append(
            {
                "e": e_current,
                "partition": partition,
                "terminal_count_across_segments": terminal_acc,
                "segment_count": segment_count,
                "segment_chain_sha256": chain,
                "nodes_across_segments": nodes_acc,
            }
        )
        continuation = None
        chain = EMPTY_CHAIN_SHA256
        segment_count = 0
        terminal_acc = 0
        nodes_acc = 0

        if source["kind"] == "STRATUM_PARTITION":
            break
        e_current += 1
        if e_current <= e_last and remaining == 0:
            unresolved.append(
                normalize_cursor(
                    source,
                    e_current=e_current,
                    continuation=None,
                    segment_chain_sha256=EMPTY_CHAIN_SHA256,
                    segment_count=0,
                    terminal_count_accumulated=0,
                    nodes_accumulated=0,
                )
            )
            break

    nodes_this_call = sum(int(t["nodes"]) for t in telemetry)
    assert 0 <= nodes_this_call <= args.node_limit
    assert len(unresolved) <= 1

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "phase": "FULL178_EXACT_PAIRING_PREFIX_RESUMABLE_PROBE",
        "prefix_stage_only": True,
        "row_id": row_id,
        "genus": genus,
        "degree": degree,
        "m": m,
        "exceptional_mass_range": [emin, emax],
        "input_work_unit": unit,
        "node_limit": args.node_limit,
        "nodes_used": nodes_this_call,
        "completed_prefix_partitions": completed,
        "unresolved_exact_child_work_units": unresolved,
        "telemetry": telemetry,
        "unknown_count": len(unresolved),
        "max_unresolved_children_per_input": 1,
        "reproduction_factor_structural_upper_bound": 1.0,
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
    print(json.dumps({
        "row_id": row_id,
        "nodes_used": nodes_this_call,
        "completed": len(completed),
        "unresolved": len(unresolved),
        "structural_reproduction_upper_bound": 1.0,
        "sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
