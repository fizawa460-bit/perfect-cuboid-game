#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

V6_PATH = Path("stages/stage32/32-21/post1473-v6-witness-body-recovered.json")
V6_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
ALL140_SHA = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
NEGATIVE_ROWS = [17, 21, 24, 25, 26, 28, 30, 31]
R2_ROWS = [17, 21, 24, 25, 30, 31]
R1_ROWS = [26, 28]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def main() -> None:
    raw = V6_PATH.read_bytes()
    assert git_blob_sha1(raw) == V6_BLOB
    obj = json.loads(raw)
    assert obj["canonical_sha256_without_this_field"] == V6_CANONICAL
    witness = obj["witness"]
    assert witness["self_intersection"] == 758
    assert obj["target"]["d"] == 186
    assert obj["target"]["e"] == 266

    all140 = [int(x) for x in witness["all140_pairings"]]
    assert len(all140) == 140
    assert csha(all140) == ALL140_SHA
    assert witness["all140_pairings_sha256"] == ALL140_SHA

    # Source-locked order from Stoll--Testa verification blob 0422...:
    # 32 conics, 12+48 genus-one curves, 48 exceptional curves.
    # Adjunction gives canonical degrees 2,4,0 respectively.
    kdeg = [2] * 32 + [4] * 60 + [0] * 48
    d_pairings = [c - k for c, k in zip(all140, kdeg)]

    neg = [i + 1 for i, x in enumerate(d_pairings) if x < 0]
    assert neg == NEGATIVE_ROWS
    assert [(i, all140[i - 1], d_pairings[i - 1]) for i in R2_ROWS] == [
        (17, 0, -2),
        (21, 0, -2),
        (24, 0, -2),
        (25, 0, -2),
        (30, 0, -2),
        (31, 0, -2),
    ]
    assert [(i, all140[i - 1], d_pairings[i - 1]) for i in R1_ROWS] == [
        (26, 1, -1),
        (28, 1, -1),
    ]
    assert d_pairings[10] == 0  # conic row 11
    assert min(d_pairings[32:92]) == 7
    assert min(d_pairings[92:]) == 0
    assert [i + 93 for i, x in enumerate(d_pairings[92:]) if x == 0] == [98]

    # F = sum of the eight forced conics.  Pairwise intersections contribute
    # I >= 0, so the cohomology jump is at least its I=0 value.
    k_dot_f = 8 * 2
    d_dot_f = 6 * (-2) + 2 * (-1)
    f_square_constant = 8 * (-4)  # F^2 = -32 + 2I
    assert k_dot_f == 16
    assert d_dot_f == -14
    assert f_square_constant == -32

    # K.(2K-C+F) = 2K^2-K.C+K.F = -138 < 0, so h2(D-F)=0.
    h2_test_k_degree = 2 * 16 - 186 + k_dot_f
    assert h2_test_k_degree == -138

    # chi(D-F)-chi(D) = -D.F + (F^2+K.F)/2 = 6+I.
    chi_jump_at_i0 = -d_dot_f + (f_square_constant + k_dot_f) // 2
    assert chi_jump_at_i0 == 6

    result = {
        "schema": "STAGE32EX6_SCRATCH_V6_EIGHT_CONIC_FIXED_PART_REPLAY_V1",
        "v6_all140_sha256": ALL140_SHA,
        "negative_rows": neg,
        "r2_rows": R2_ROWS,
        "r1_rows": R1_ROWS,
        "min_genus1_D_intersection": min(d_pairings[32:92]),
        "zero_exceptional_rows": [i + 93 for i, x in enumerate(d_pairings[92:]) if x == 0],
        "fixed_sum_K_degree": k_dot_f,
        "fixed_sum_D_intersection": d_dot_f,
        "h2_D_minus_F_exclusion_K_degree": h2_test_k_degree,
        "h1_D_lower_bound": chi_jump_at_i0,
        "C_minus_K_nef": False,
        "direct_H1_D_zero_route": False,
        "O266_endpoint_excluded": False,
        "O264_descent_authorized": False,
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
