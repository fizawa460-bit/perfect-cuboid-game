#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
from typing import Any

EXPECTED_CORE_SCHEMA = "STAGE32_PICARD_CORE_INDLIST_V1"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
CERT_SCHEMA = "STAGE32_INTERSECTION_CAP_CERTIFICATE_V1"


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_core(path: pathlib.Path) -> dict[str, Any]:
    core = json.loads(path.read_text(encoding="utf-8"))
    assert core["schema"] == EXPECTED_CORE_SCHEMA
    assert core["source"]["git_blob_sha1"] == EXPECTED_SOURCE_BLOB
    assert core["rank"] == 64 and core["known_class_count"] == 140
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(unsigned) == claimed
    return core


def verify_certificate(core: dict[str, Any], certificate: dict[str, Any]) -> dict[str, Any]:
    assert certificate["schema"] == CERT_SCHEMA
    assert certificate["source_core_canonical_sha256"] == core["canonical_sha256_without_this_field"]
    assert certificate["source_blob_sha1"] == core["source"]["git_blob_sha1"]
    unsigned = dict(certificate)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(unsigned) == claimed

    known = core["known_classes"]
    hyperplane = core["hyperplane"]
    rows = certificate["certificates"]
    assert len(rows) == 140
    seen: set[int] = set()
    max_denominator = 0
    max_coefficient = 0
    nonzero_terms = 0
    for row in rows:
        j1 = int(row["known_index_1based"])
        assert 1 <= j1 <= 140 and j1 not in seen
        seen.add(j1)
        multiplier = int(row["target_multiplier"])
        assert multiplier == (2 if j1 <= 92 else 4)
        denominator = int(row["denominator"])
        assert denominator > 0
        max_denominator = max(max_denominator, denominator)

        rhs = [multiplier * denominator * int(v) for v in known[j1 - 1]]
        used: set[int] = set()
        for index1, coefficient in row["combination"]:
            index1 = int(index1)
            coefficient = int(coefficient)
            assert 1 <= index1 <= 140 and index1 != j1 and index1 not in used
            assert coefficient >= 0
            used.add(index1)
            max_coefficient = max(max_coefficient, coefficient)
            nonzero_terms += int(coefficient != 0)
            source = known[index1 - 1]
            rhs = [rhs[k] + coefficient * int(source[k]) for k in range(64)]
        lhs = [denominator * int(v) for v in hyperplane]
        assert rhs == lhs

    assert seen == set(range(1, 141))
    return {
        "schema": "STAGE32_INTERSECTION_CAP_VERIFICATION_V1",
        "certificate_canonical_sha256": claimed,
        "verified_certificate_count": 140,
        "curve_cap": "K_i.x <= floor((H.x)/2), i=1..92",
        "exceptional_cap": "K_i.x <= floor((H.x)/4), i=93..140",
        "max_denominator": max_denominator,
        "max_sparse_coefficient": max_coefficient,
        "nonzero_combination_terms": nonzero_terms,
        "exact_integer_verification": True,
        "floating_point_theorem_credit": False,
        "receiver_credit": False,
    }


def load_and_verify(core_path: pathlib.Path, certificate_path: pathlib.Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    core = load_core(core_path)
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    summary = verify_certificate(core, certificate)
    return core, certificate, summary
