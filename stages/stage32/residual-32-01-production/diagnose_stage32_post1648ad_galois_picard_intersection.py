#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
STAGE33_07 = ROOT / "stage33" / "33-07"
sys.path.insert(0, str(STAGE33_07))

from picard_base_rows_retained import load as load_picard  # noqa: E402

V6 = ROOT / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
OUT = Path("/tmp/stage32-post1648ad-galois-picard-intersection-diagnostic.json")
EXPECTED_V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_RETAINED_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
RANK = 64


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mm(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    BT = list(zip(*B))
    return [[sum(int(a) * int(b) for a, b in zip(row, col)) for col in BT] for row in A]


def mv(A: list[list[int]], x: list[int]) -> list[int]:
    return [sum(int(a) * int(b) for a, b in zip(row, x)) for row in A]


def transpose(A: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*A)]


def dot(x: list[int], G: list[list[int]], y: list[int]) -> int:
    Gy = mv(G, y)
    return sum(int(a) * int(b) for a, b in zip(x, Gy))


def main() -> None:
    v6 = json.loads(V6.read_text(encoding="utf-8"))
    body = dict(v6)
    claimed = body.pop("canonical_sha256_without_this_field")
    assert claimed == EXPECTED_V6_CANONICAL == csha(body)
    x = [int(v) for v in v6["witness"]["picard_coordinates"]]
    assert len(x) == RANK
    assert v6["witness"]["self_intersection"] == 758

    retained = load_picard()
    assert retained["canonical_sha256"] == EXPECTED_RETAINED_CANONICAL
    assert retained["upstream_git_blob_sha1"] == EXPECTED_SOURCE_BLOB
    G = [[int(v) for v in row] for row in retained["picard_gram_64x64"]]
    A = [[int(v) for v in row] for row in retained["picard_action_cc_64x64"]]
    assert len(G) == len(A) == RANK
    assert all(len(row) == RANK for row in G + A)
    AT = transpose(A)
    I = [[int(i == j) for j in range(RANK)] for i in range(RANK)]
    assert mm(A, A) == I
    assert mm(mm(A, G), AT) == G

    # retained action is on the ordered Picard basis (row convention), hence
    # divisor coordinate columns transform by A^T.
    sx = mv(AT, x)
    ssx = mv(AT, sx)
    assert ssx == x
    d2 = dot(x, G, x)
    sd2 = dot(sx, G, sx)
    cross = dot(x, G, sx)
    assert d2 == sd2 == 758

    diff = [a - b for a, b in zip(x, sx)]
    summ = [a + b for a, b in zip(x, sx)]
    result = {
        "schema": "STAGE32_POST1648AD_GALOIS_PICARD_INTERSECTION_DIAGNOSTIC_V1",
        "retained_picard_bundle_canonical_sha256": retained["canonical_sha256"],
        "retained_upstream_git_blob_sha1": retained["upstream_git_blob_sha1"],
        "basis": "historical retained Magma Basis(Pic), row-action convention",
        "D_self_intersection": d2,
        "sigma_D_self_intersection": sd2,
        "D_dot_sigma_D": cross,
        "D_plus_sigma_D_square": dot(summ, G, summ),
        "D_minus_sigma_D_square": dot(diff, G, diff),
        "sigma_D_equals_D": sx == x,
        "sigma_D_picard_coordinates": sx,
        "involution_exact": ssx == x,
        "gram_isometry_exact": True,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
