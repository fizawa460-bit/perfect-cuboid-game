#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib

from direct_picard_slice_bridge import DirectPicardSliceBridge

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
SCHEMA = "STAGE32_RESIDUAL32_01_DIRECT_PICARD_D_E_A_SLICE_CENSUS_V1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def load_module_payload(path: pathlib.Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def feasible_a_count(bridge: DirectPicardSliceBridge, d: int, e: int, upper: int) -> tuple[int, list[int]]:
    q = int(bridge.target_image_modulus)
    if q == 1:
        return upper + 1, [0]
    residues = [a for a in range(q) if bridge.target_in_image(d, e, a)]
    count = 0
    for r in residues:
        if r <= upper:
            count += (upper - r) // q + 1
    return count, residues


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=pathlib.Path, required=True)
    ap.add_argument("--retained", type=pathlib.Path, required=True)
    ap.add_argument("--marking", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    assert csha(manifest) == claimed == EXPECTED_MANIFEST_SHA256

    bundle = load_module_payload(args.retained, "stage32_direct_slice_picard")
    marking = load_module_payload(args.marking, "stage32_direct_slice_marking")
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    assert len(rows) == 178 and len(set(rows)) == 178

    total_e_strata = 0
    total_slices = 0
    total_image_feasible = 0
    image_empty_e_strata = 0
    max_row = None
    max_e_stratum = None
    max_feasible_e_stratum = None
    row_summaries = []
    stream_hash = hashlib.sha256()

    for row_id in rows:
        genus, d = parse_row_id(row_id)
        emin = 8 if genus == 0 else 4
        emax = (19 * d) // 5
        row_slices = 0
        row_feasible = 0
        row_peak = None
        row_peak_feasible = None
        row_empty = 0
        for e in range(emin, emax + 1):
            normal_mass = 19 * d - 5 * e
            assert normal_mass >= 0
            slices = normal_mass + 1
            feasible, residues = feasible_a_count(bridge, d, e, normal_mass)
            if feasible == 0:
                row_empty += 1
                image_empty_e_strata += 1
            rec = {
                "row_id": row_id,
                "e": e,
                "normal_mass": normal_mass,
                "a_slice_count": slices,
                "image_feasible_a_slice_count": feasible,
                "image_feasible_a_residues_mod_q": residues,
            }
            stream_hash.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
            total_e_strata += 1
            total_slices += slices
            total_image_feasible += feasible
            row_slices += slices
            row_feasible += feasible
            if row_peak is None or slices > row_peak[1]:
                row_peak = (e, slices)
            if row_peak_feasible is None or feasible > row_peak_feasible[1]:
                row_peak_feasible = (e, feasible)
            if max_e_stratum is None or slices > max_e_stratum[2]:
                max_e_stratum = (row_id, e, slices)
            if max_feasible_e_stratum is None or feasible > max_feasible_e_stratum[2]:
                max_feasible_e_stratum = (row_id, e, feasible)
        assert row_peak is not None and row_peak_feasible is not None
        row_summaries.append({
            "row_id": row_id,
            "degree": d,
            "emin": emin,
            "emax": emax,
            "e_strata": emax - emin + 1,
            "direct_a_slices": row_slices,
            "image_feasible_a_slices": row_feasible,
            "image_empty_e_strata": row_empty,
            "peak_a_slice_e": row_peak[0],
            "peak_a_slice_count": row_peak[1],
            "peak_image_feasible_e": row_peak_feasible[0],
            "peak_image_feasible_count": row_peak_feasible[1],
        })
        if max_row is None or row_slices > max_row[2]:
            max_row = (row_id, d, row_slices, row_feasible)

    assert total_e_strata == int(manifest["coarse_strata_count"]) == 64111
    assert max_row is not None and max_e_stratum is not None and max_feasible_e_stratum is not None
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "EXACT_COUNT_OF_DIRECT_PICARD_D_E_A_PARTITION_AND_TARGET_IMAGE_GATE",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "bridge_certificate_sha256": bridge.certificate["canonical_sha256_without_this_field"],
        "target_image_index": bridge.certificate["target_image"]["image_index"],
        "target_image_modulus": bridge.target_image_modulus,
        "target_image_active_congruence_rows": bridge.certificate["target_image"]["active_congruence_rows"],
        "row_count": len(rows),
        "exact_coarse_e_strata": total_e_strata,
        "direct_picard_slice_count": total_slices,
        "image_feasible_direct_picard_slice_count": total_image_feasible,
        "image_empty_e_strata": image_empty_e_strata,
        "max_row": {
            "row_id": max_row[0],
            "degree": max_row[1],
            "slice_count": max_row[2],
            "image_feasible_slice_count": max_row[3],
        },
        "max_single_e_stratum": {"row_id": max_e_stratum[0], "e": max_e_stratum[1], "a_slice_count": max_e_stratum[2]},
        "max_image_feasible_single_e_stratum": {"row_id": max_feasible_e_stratum[0], "e": max_feasible_e_stratum[1], "a_slice_count": max_feasible_e_stratum[2]},
        "slice_stream_sha256": stream_hash.hexdigest(),
        "row_summaries": row_summaries,
        "semantics": {
            "slice_key": ["degree", "exceptional_total", "first_normal_half_total"],
            "a_range_exact_for_nonnegative_all140_candidates": "0..19*d-5*e",
            "image_gate_exactly_matches_historical_tar_in_Image_phi": True,
            "count_before_closevectors": True,
            "prefix_terminal_stream_materialized": False,
            "numerical_picard_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_DIRECT_PICARD_SLICE_CENSUS",
        "rows": len(rows),
        "e_strata": total_e_strata,
        "direct_picard_slices": total_slices,
        "image_feasible_direct_picard_slices": total_image_feasible,
        "image_empty_e_strata": image_empty_e_strata,
        "target_image_index": bridge.certificate["target_image"]["image_index"],
        "target_image_modulus": bridge.target_image_modulus,
        "max_row": payload["max_row"],
        "max_single_e_stratum": payload["max_single_e_stratum"],
        "max_image_feasible_single_e_stratum": payload["max_image_feasible_single_e_stratum"],
        "bridge_sha256": bridge.certificate["canonical_sha256_without_this_field"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
