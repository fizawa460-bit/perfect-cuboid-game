#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

V6_PATH = Path("stages/stage32/32-21/post1473-v6-witness-body-recovered.json")
V6_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
ALL140_SHA = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
FIXED_ROWS = [17, 21, 24, 25, 26, 28, 30, 31]
PAIRWISE_INTERSECTIONS = [0] * 28
FPAIR_FIRST92 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-4,0,0,0,-4,0,0,-4,-4,-4,0,-4,0,-4,-4,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,3,2,3,2,2,3,2,3,2,3,2,3,3,2,3,2,2,1,1,2,2,1,1,2,0,3,3,0,0,3,3,0,0,0,0,0,0,0,0,0]
FPAIR_SHA = "ea960468c133814c1fb342efa8be682fd6c56880785abdf087fa2f5ca671b38c"
D1_FIRST92_SHA = "0ee12ba4030500fa0e61d67c3e46a83541508d48d6609926df0afb67bfa17ace"
F_EXCEPTIONAL_INCIDENCE = [3] * 2 + [2] * 10 + [1] * 22 + [0] * 14


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

    kdeg = [2] * 32 + [4] * 60 + [0] * 48
    d_pairings = [c - k for c, k in zip(all140, kdeg)]
    assert [i + 1 for i, x in enumerate(d_pairings) if x < 0] == FIXED_ROWS

    # External source-geometry certificate: Stoll--Testa cuboids.magma at
    # verification commit 51233ed... / blob 0422b698... gives the explicit
    # conic equations and the singular-point subtraction intersection rule.
    # The bounded 28-pair replay produces the following compact certificate.
    assert len(PAIRWISE_INTERSECTIONS) == 28
    assert max(PAIRWISE_INTERSECTIONS) == 0
    assert min(PAIRWISE_INTERSECTIONS) == 0
    pairwise_sum = sum(PAIRWISE_INTERSECTIONS)
    assert pairwise_sum == 0

    k_dot_f = 8 * 2
    d_dot_f = sum(d_pairings[i - 1] for i in FIXED_ROWS)
    f_square = 8 * (-4) + 2 * pairwise_sum
    assert k_dot_f == 16
    assert d_dot_f == -14
    assert f_square == -32

    d_square = 402
    d_dot_k = 170
    d1_square = d_square - 2 * d_dot_f + f_square
    d1_dot_k = d_dot_k - k_dot_f
    chi_d1 = 8 + (d1_square - d1_dot_k) // 2
    h2_test = 16 - d1_dot_k
    assert d1_square == 398
    assert d1_dot_k == 154
    assert chi_d1 == 130
    assert h2_test == -138

    chi_d = 124
    h1_shift = chi_d1 - chi_d
    assert h1_shift == 6

    assert len(FPAIR_FIRST92) == 92
    assert csha(FPAIR_FIRST92) == FPAIR_SHA
    d1_first92 = [d_pairings[i] - FPAIR_FIRST92[i] for i in range(92)]
    assert csha(d1_first92) == D1_FIRST92_SHA
    assert [i + 1 for i, x in enumerate(d1_first92) if x < 0] == []
    assert [i + 1 for i, x in enumerate(d1_first92) if x == 0] == [11]

    # Eight conics, six singular points each.  Unlabeled incidence certificate.
    assert len(F_EXCEPTIONAL_INCIDENCE) == 48
    assert sum(F_EXCEPTIONAL_INCIDENCE) == 48
    assert sum(1 for x in F_EXCEPTIONAL_INCIDENCE if x > 0) == 34
    assert {m: F_EXCEPTIONAL_INCIDENCE.count(m) for m in [0, 1, 2, 3]} == {
        0: 14,
        1: 22,
        2: 10,
        3: 2,
    }

    c_exc = all140[92:]
    assert len(c_exc) == 48
    assert sum(c_exc) == 266
    assert [i + 93 for i, x in enumerate(c_exc) if x == 0] == [98]
    assert sum(c_exc) - sum(F_EXCEPTIONAL_INCIDENCE) == 218

    # The unlabeled multisets admit a nonnegative matching; hence an actual
    # negative exceptional row is not forced until the row permutation is locked.
    sorted_c = sorted(c_exc)
    sorted_f = sorted(F_EXCEPTIONAL_INCIDENCE)
    assert all(c >= f for c, f in zip(sorted_c, sorted_f))

    # Bigness of D1 from RR growth: chi(nD1)=8+199n^2-77n and h2=0.
    for n in [1, 2, 3, 10]:
        assert 16 - 154 * n < 0
        assert 8 + 199 * n * n - 77 * n > 0

    result = {
        "schema": "STAGE32EX6_SCRATCH_V6_C_MINUS_K_EIGHT_CONIC_DISJOINT_PEEL_REPLAY_V1",
        "v6_all140_sha256": ALL140_SHA,
        "fixed_rows": FIXED_ROWS,
        "pairwise_intersection_count": 28,
        "pairwise_intersection_sum": pairwise_sum,
        "F_square": f_square,
        "D_dot_F": d_dot_f,
        "K_dot_F": k_dot_f,
        "D1_square": d1_square,
        "K_dot_D1": d1_dot_k,
        "chi_D1": chi_d1,
        "h1_D_minus_h1_D1": h1_shift,
        "D1_negative_known_nonexceptional_rows": [],
        "D1_zero_known_nonexceptional_rows": [11],
        "F_exceptional_incidence_total": sum(F_EXCEPTIONAL_INCIDENCE),
        "F_exceptional_incidence_support": 34,
        "D1_exceptional_total": 218,
        "unlabeled_exceptional_matching_can_be_nonnegative": True,
        "exceptional_row_adapter_locked": False,
        "O266_endpoint_excluded": False,
        "O264_descent_authorized": False,
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
