#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
SCHEMA = "STAGE32_RESIDUAL32_01_DIRECT_PICARD_D_E_A_SLICE_CENSUS_V1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    assert csha(manifest) == claimed == EXPECTED_MANIFEST_SHA256

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    assert len(rows) == 178 and len(set(rows)) == 178

    total_e_strata = 0
    total_slices = 0
    max_row = None
    max_e_stratum = None
    row_summaries = []
    stream_hash = hashlib.sha256()

    for row_id in rows:
        genus, d = parse_row_id(row_id)
        emin = 8 if genus == 0 else 4
        emax = (19 * d) // 5
        row_slices = 0
        row_peak = None
        for e in range(emin, emax + 1):
            normal_mass = 19 * d - 5 * e
            assert normal_mass >= 0
            slices = normal_mass + 1
            rec = {
                "row_id": row_id,
                "e": e,
                "normal_mass": normal_mass,
                "a_slice_count": slices,
            }
            stream_hash.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
            total_e_strata += 1
            total_slices += slices
            row_slices += slices
            if row_peak is None or slices > row_peak[1]:
                row_peak = (e, slices)
            if max_e_stratum is None or slices > max_e_stratum[2]:
                max_e_stratum = (row_id, e, slices)
        assert row_peak is not None
        row_summaries.append({
            "row_id": row_id,
            "degree": d,
            "emin": emin,
            "emax": emax,
            "e_strata": emax - emin + 1,
            "direct_a_slices": row_slices,
            "peak_a_slice_e": row_peak[0],
            "peak_a_slice_count": row_peak[1],
        })
        if max_row is None or row_slices > max_row[2]:
            max_row = (row_id, d, row_slices)

    assert total_e_strata == int(manifest["coarse_strata_count"]) == 64111
    assert max_row is not None and max_e_stratum is not None
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "EXACT_COUNT_OF_DIRECT_PICARD_D_E_A_PARTITION_BEFORE_LATTICE_IMAGE_PRUNING",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "row_count": len(rows),
        "exact_coarse_e_strata": total_e_strata,
        "direct_picard_slice_count": total_slices,
        "max_row": {"row_id": max_row[0], "degree": max_row[1], "slice_count": max_row[2]},
        "max_single_e_stratum": {"row_id": max_e_stratum[0], "e": max_e_stratum[1], "a_slice_count": max_e_stratum[2]},
        "slice_stream_sha256": stream_hash.hexdigest(),
        "row_summaries": row_summaries,
        "semantics": {
            "slice_key": ["degree", "exceptional_total", "first_normal_half_total"],
            "a_range_exact_for_nonnegative_all140_candidates": "0..19*d-5*e",
            "count_before_target_image_feasibility": True,
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
        "max_row": payload["max_row"],
        "max_single_e_stratum": payload["max_single_e_stratum"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
