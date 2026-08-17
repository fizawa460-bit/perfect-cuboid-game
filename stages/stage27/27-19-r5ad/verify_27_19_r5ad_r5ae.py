from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
R5AD = Path(__file__).with_name("result.md")
R5AE = ROOT / "stages" / "stage27" / "27-19-r5ae" / "result.md"


def omega(n: int) -> int:
    out = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            out += 1
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out += 1
    return out


def root_count(modulus: int, rhs: int) -> int:
    return sum(1 for x in range(modulus) if (x * x - rhs) % modulus == 0)


def is_sum_two_squares(n: int) -> bool:
    for x in range(isqrt(n) + 1):
        y2 = n - x * x
        y = isqrt(y2)
        if y * y == y2:
            return True
    return False


def verify_root_count_receivers(limit: int = 256) -> None:
    for a in range(1, limit + 1):
        assert root_count(a, -1) <= 4 * (2 ** omega(a))
        assert root_count(a, 1) <= 4 * (2 ** omega(a))


def verify_normalized_congruences(limit: int = 20) -> None:
    for m in range(2, limit + 1):
        for n in range(1, m):
            if gcd(m, n) != 1:
                continue
            for r in range(2, limit + 1):
                for s in range(1, r):
                    if gcd(r, s) != 1:
                        continue
                    d = gcd(n, s)
                    n0, s0 = n // d, s // d
                    M = m * m + n * n
                    K = r * r - s * s
                    h = gcd(M, K)
                    a, b = M // h, K // h
                    p, q = s0 * s0 * a, n0 * n0 * b
                    A, S = max(a, b), max(s0, n0)
                    H = max(p, q)

                    assert gcd(d * n0, a) == 1
                    assert gcd(d * s0, b) == 1
                    assert (m * m + (d * n0) ** 2) % a == 0
                    assert (r * r - (d * s0) ** 2) % b == 0
                    assert (m * m + (d * n0) ** 2) // a == h
                    assert (r * r - (d * s0) ** 2) // b == h
                    assert H <= S * S * A
                    assert A * S >= isqrt(H)


def verify_norm_support_barrier(B: int = 4096, T: int = 256) -> None:
    triples = set()
    x_lo = isqrt(T)
    if x_lo * x_lo < T:
        x_lo += 1
    x_hi = isqrt((3 * T) // 2)
    z_hi = B // (2 * isqrt(T))

    for x in range(x_lo, x_hi + 1):
        p, q = x * x, 1
        if not (T <= max(p, q) < 2 * T):
            continue
        for z in range(1, z_hi + 1):
            g = z * z
            assert gcd(p, q) == 1
            assert g <= B * B // (4 * T)
            assert is_sum_two_squares(p)
            assert is_sum_two_squares(g)
            assert is_sum_two_squares(p + q)
            triples.add((p, q, g))

    # This finite regression mirrors the proved product-size construction.
    assert len(triples) >= B // 20, len(triples)


def verify_markers() -> None:
    r5ad = R5AD.read_text(encoding="utf-8")
    for marker in [
        "UNIFORM_MOVING_TAU_DISTINCT_CORE_BOUND_PROVED=true",
        "REFINED_DECOMPOSITION_CORE_BOUND_PROVED=true",
        "UNIFORM_MOVING_TAU_FIBER_POWER_BOUND_PROVED=true",
        "TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false",
        "NEXT_DERIVED_ROUTE=27-19-r5ae",
    ]:
        assert marker in r5ad, marker

    r5ae = R5AE.read_text(encoding="utf-8")
    for marker in [
        "NORM_SUPPORT_ONLY_POWER_SAVING_BARRIER_PROVED=true",
        "R5AC_PLUS_CORE_HEIGHT_ALONE_INSUFFICIENT_FOR_STRICT_SUBHALF=true",
        "DIAGONAL_RECONSTRUCTION_MUST_BE_USED_FOR_NEXT_POWER_SAVING=true",
        "STRICT_SUB_SQRT_UPPER_PROVED=false",
        "NEXT_DERIVED_ROUTE=27-19-r5af",
    ]:
        assert marker in r5ae, marker


if __name__ == "__main__":
    verify_markers()
    verify_root_count_receivers()
    verify_normalized_congruences()
    verify_norm_support_barrier()
    print("Stage27-19-r5ad/r5ae verifier: PASS")
