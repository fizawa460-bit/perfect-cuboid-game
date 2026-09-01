#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib

from compressed_terminal_family import build_exceptional_count_table

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
SCHEMA = "STAGE32_RESIDUAL32_01_COMPRESSED_FULL178_PREFIX_COUNT_CENSUS_V1"


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

    table = build_exceptional_count_table(729)
    stream_hash = hashlib.sha256()
    total_strata = 0
    total_terminals = 0
    max_stratum = None
    row_summaries = []

    for row_id in rows:
        genus, d = parse_row_id(row_id)
        emin = 8 if genus == 0 else 4
        emax = (19 * d) // 5
        assert emax <= table.max_e
        row_total = 0
        row_max = None
        for e in range(emin, emax + 1):
            normal_budget = 19 * d - 5 * e
            count = (normal_budget + 1) * table.count(e)
            rec = {"row_id": row_id, "e": e, "terminal_count": str(count)}
            stream_hash.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
            total_strata += 1
            total_terminals += count
            row_total += count
            if row_max is None or count > row_max[1]:
                row_max = (e, count)
            if max_stratum is None or count > max_stratum[2]:
                max_stratum = (row_id, e, count)
        assert row_max is not None
        row_summaries.append({
            "row_id": row_id,
            "degree": d,
            "emin": emin,
            "emax": emax,
            "stratum_count": emax - emin + 1,
            "terminal_count_total": str(row_total),
            "terminal_count_digits": len(str(row_total)),
            "peak_terminal_e": row_max[0],
            "peak_terminal_count": str(row_max[1]),
        })

    assert total_strata == int(manifest["coarse_strata_count"]) == 64111
    assert max_stratum is not None
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "SYMBOLIC_EXACT_COUNT_OF_CURRENT_PAIRING_PREFIX_TERMINAL_FAMILY",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "row_count": len(rows),
        "exact_coarse_e_strata": total_strata,
        "maximum_emax": 729,
        "terminal_count_total": str(total_terminals),
        "terminal_count_total_digits": len(str(total_terminals)),
        "max_single_stratum": {
            "row_id": max_stratum[0],
            "e": max_stratum[1],
            "terminal_count": str(max_stratum[2]),
        },
        "symbolic_stratum_count_stream_sha256": stream_hash.hexdigest(),
        "row_summaries": row_summaries,
        "semantics": {
            "count_is_exact_for_current_prefix_filters": True,
            "terminal_stream_materialized": False,
            "terminal_stream_sha256_replaced": False,
            "numerical_picard_leaf_checks_complete": False,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_COMPRESSED_FULL178_PREFIX_COUNT_CENSUS",
        "rows": len(rows),
        "strata": total_strata,
        "terminal_count_total": str(total_terminals),
        "terminal_count_total_digits": len(str(total_terminals)),
        "max_stratum_row": max_stratum[0],
        "max_stratum_e": max_stratum[1],
        "max_stratum_terminal_count": str(max_stratum[2]),
        "stream_sha256": stream_hash.hexdigest(),
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
