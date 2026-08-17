from collections import defaultdict
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = Path(__file__).with_name("result.md")
CONTRACT = Path(__file__).with_name("route-contract.json")


def square_divisor_count(n: int) -> int:
    return sum(1 for d in range(1, isqrt(n) + 1) if n % (d * d) == 0)


def canonical_data(m: int, n: int, r: int, s: int):
    A = s * s * (m * m + n * n)
    D = n * n * (r * r - s * s)
    g = gcd(A, D)
    p, q = A // g, D // g

    d = gcd(n, s)
    n0, s0 = n // d, s // d
    M = m * m + n * n
    K = r * r - s * s
    h = gcd(M, K)
    a, b = M // h, K // h
    return A, D, p, q, g, d, n0, s0, M, K, h, a, b


def verify_exact_factorization(limit: int = 18) -> None:
    fibers = defaultdict(list)

    for m in range(2, limit + 1):
        for n in range(1, m):
            if gcd(m, n) != 1:
                continue
            for r in range(2, limit + 1):
                for s in range(1, r):
                    if gcd(r, s) != 1:
                        continue

                    A, D, p, q, g, d, n0, s0, M, K, h, a, b = canonical_data(m, n, r, s)

                    assert g == d * d * h
                    assert p == s0 * s0 * a
                    assert q == n0 * n0 * b
                    assert gcd(p, q) == 1
                    assert gcd(s0, n0) == 1
                    assert gcd(s0, b) == 1
                    assert gcd(n0, a) == 1
                    assert gcd(a, b) == 1
                    assert m * m == a * h - d * d * n0 * n0
                    assert r * r == b * h + d * d * s0 * s0
                    assert p % (s0 * s0) == 0
                    assert q % (n0 * n0) == 0
                    assert g % (d * d) == 0

                    fibers[(p, q, g)].append((m, n, r, s))

    for (p, q, g), reps in fibers.items():
        receiver_bound = (
            square_divisor_count(p)
            * square_divisor_count(q)
            * square_divisor_count(g)
        )
        assert len(reps) <= receiver_bound, ((p, q, g), len(reps), receiver_bound)


def verify_contract_text() -> None:
    text = RESULT.read_text(encoding="utf-8")
    required = [
        "TASK_ID=Stage27-19-r5aa",
        "ROUTE_KIND=UPPER_REENTRY_PARALLEL",
        "TAU_CORE_GCD_SQUARE_FACTORIZATION_PROVED=true",
        "TAU_CORE_GCD_FACTORIZATION=g=d^2*h",
        "FIXED_TAU_G_CORE_MULTIPLICITY_UNIFORM_SUBPOWER_PROVED=true",
        "JOINT_TAU_G_SUPPORT_REDUCTION=N_T<=B^o(1)*K_T",
        "SAME_CORE_COLLISION_SUBPOWER_OVERHEAD_PROVED=true",
        "JOINT_SUPPORT_STRICT_SUBHALF_PROVED=false",
        "STRICT_SUB_SQRT_UPPER_PROVED=false",
        "NEXT_DERIVED_ROUTE=27-19-r5ab",
    ]
    for marker in required:
        assert marker in text, marker

    import json

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    assert contract["task_id"] == "Stage27-19-r5aa"
    assert contract["parallel_lane"] is True
    assert contract["proved"]["fixed_tau_g_core_multiplicity_uniform_subpower"] is True
    assert contract["not_proved"]["strict_sub_sqrt_upper"] is True


if __name__ == "__main__":
    verify_contract_text()
    verify_exact_factorization()
    print("Stage27-19-r5aa verifier: PASS")
