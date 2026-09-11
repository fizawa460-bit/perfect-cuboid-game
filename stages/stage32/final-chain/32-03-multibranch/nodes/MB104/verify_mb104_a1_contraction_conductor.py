#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"

LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/A1-CONTRACTION-CONDUCTOR-SOURCE-NOTE.md": "060a1c989c4fcadbb595add7250189e0b7834ab4",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/A1-CONTRACTION-CONDUCTOR.json": "fda08685a63caab19851d0d6e5bac353092c888e",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/KNOWN-CURVE-CONE-WALL.json": "61e516f2cb231ad61d16eb097395ec69e409c943",
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def f(m: int) -> int:
    return (m * m) // 4


def balanced(M: int, n: int = 48) -> int:
    q, r = divmod(M, n)
    return (n - r) * f(q) + r * f(q + 1)


def main() -> None:
    for rel, expected in LOCKS.items():
        got = git_blob_sha(ROOT / rel)
        assert got == expected, (rel, got, expected)

    cert = json.loads((NODE / "A1-CONTRACTION-CONDUCTOR.json").read_text())
    wall = json.loads((NODE / "KNOWN-CURVE-CONE-WALL.json").read_text())

    assert cert["schema"] == "STAGE32_MB104_A1_CONTRACTION_CONDUCTOR_V1"
    assert cert["a1_lattice"]["exceptional_square"] == -2
    assert cert["a1_lattice"]["crepant"] is True
    assert cert["a1_lattice"]["local_class_group"] == "Z/2"
    assert cert["exact_contraction_formula"]["single_node"] == "p_a(C)-p_a(D)=floor(M^2/4)"
    assert cert["exact_contraction_formula"]["lambda_dependent"] is False
    assert cert["population_wide_consequences"]["finite_degree_window_proved"] is False

    # A1 parity replay from chi(E/2)=1/4.
    for M in range(0, 1001):
        blache_quarters = 0 if M % 2 == 0 else 1
        # 4 * (M^2/4 - A_X) = M^2 - 4*A_X.
        jump4 = M * M - blache_quarters
        assert jump4 % 4 == 0
        assert jump4 // 4 == f(M)

    # Discrete convexity and the exact 48-bin balanced minimum.
    for m in range(0, 1000):
        assert f(m + 1) - f(m) == (m + 1) // 2

    # Exhaustive dynamic-programming check for modest total masses.  This is an
    # arithmetic replay of the balancing lemma, not a geometric finite search.
    INF = 10**18
    dp = [0] + [INF] * 160
    for bins in range(1, 49):
        ndp = [INF] * 161
        for total in range(161):
            if dp[total] == INF:
                continue
            for x in range(161 - total):
                v = dp[total] + f(x)
                if v < ndp[total + x]:
                    ndp[total + x] = v
        dp = ndp
    for M in range(161):
        assert dp[M] == balanced(M)
        assert dp[M] >= M * M / 192 - 12

    # The retained effective divisor-class ray survives the new correction.
    assert wall["symmetric_scaling_ray"]["class"] == "D_k=6*k*H-k*E_total, E_total=sum_i E_i"
    for k in range(1, 1001):
        Mvec = [2 * k] * 48
        assert sum(Mvec) == 96 * k
        assert sum(f(x) for x in Mvec) == 48 * k * k

    fw = cert["credit_firewall"]
    assert fw["mb104_complete"] is False
    assert fw["finite_degree_window_proved"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["receiver_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 A1 contraction-conductor verifier PASS")
    print("single-node jump=floor(M^2/4); 48-node balanced minimum replayed")
    print("quadratic conductor debt retained; finite degree window remains OPEN")


if __name__ == "__main__":
    main()
