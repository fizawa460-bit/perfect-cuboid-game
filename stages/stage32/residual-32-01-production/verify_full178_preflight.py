#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "full178-manifest.json"
PREFLIGHT = ROOT / "full178-production-preflight.json"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-")
    return int(g[1:]), int(d[1:])


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    expected_hash = manifest.pop("canonical_sha256_without_this_field")
    assert csha(manifest) == expected_hash
    manifest["canonical_sha256_without_this_field"] = expected_hash

    expected_rows = []
    for genus, lo, hi in ((0, 2, 176), (1, 4, 192)):
        for degree in range(lo, hi + 1, 2):
            if degree <= 6:
                continue
            expected_rows.append((genus, degree))
    assert len(expected_rows) == 178

    seen = []
    counts = {}
    strata = 0
    max_norm = (-1, None)
    for m_text, ids in manifest["m_class_rows"].items():
        m = int(m_text)
        counts[m_text] = len(ids)
        for row_id in ids:
            genus, degree = parse_row_id(row_id)
            r = math.gcd(degree, 16)
            assert m == 16 // r
            norm = m * m * (degree * degree + 16 * degree + (32 if genus == 0 else 0))
            assert norm % 16 == 0
            norm //= 16
            if norm > max_norm[0]:
                max_norm = (norm, row_id)
            emin = 8 if genus == 0 else 4
            emax = (19 * degree) // 5
            strata += max(0, emax - emin + 1)
            seen.append((genus, degree))

    assert sorted(seen) == expected_rows
    assert len(seen) == len(set(seen)) == 178
    assert counts == {"1": 23, "2": 23, "4": 44, "8": 88}
    assert strata == manifest["coarse_strata_count"] == 64111
    assert max_norm == (156560, "g1-d190")

    preflight = json.loads(PREFLIGHT.read_text())
    assert preflight["manifest_sha256"] == expected_hash
    assert preflight["residual_row_count"] == 178
    assert preflight["coarse_strata_count"] == 64111
    assert preflight["effective_heavy_concurrency"] == 8
    assert preflight["effective_heavy_concurrency"] <= 18
    assert preflight["projected_peak_artifact_mb"] < 500
    assert preflight["raw_evidence_persisted"] is False
    assert preflight["full_178_heavy_sweep_authorized"] is False
    assert preflight["heavy_compute_armed"] is False
    assert preflight["unknown_is_unsat"] is False
    assert preflight["B18_RELEASE_AUTHORIZED"] is False
    assert preflight["THEOREM_CREDIT"] is False
    assert preflight["RECEIVER_CREDIT"] is False

    print(json.dumps({
        "manifest_sha256": expected_hash,
        "rows": len(seen),
        "m_class_counts": counts,
        "coarse_strata_count": strata,
        "max_hperp_norm_bound": max_norm[0],
        "max_row": max_norm[1],
        "preflight_verdict": "PASS_COLD_PREFLIGHT_STATIC_CONTRACT",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
