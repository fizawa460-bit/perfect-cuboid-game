#!/usr/bin/env python3
from __future__ import annotations

import math
from dataclasses import dataclass

from stage15_4_normal_form import normal_form
from stage15_6aa_core_adapter import classify_core, physical_exact_two
from stage15_6ab_core_charge import actual_outer_charge


@dataclass(frozen=True)
class BranchReport:
    params: tuple[int, int, int, int]
    k: int
    q: int
    R0: int
    S0: int
    V: int
    branch: str
    high_core_bound: int | None


def dyadic_base(x: int) -> int:
    if x <= 0:
        raise ValueError("positive dyadic coordinate required")
    return 1 << (x.bit_length() - 1)


def branch_report(m: int, n: int, r: int, s: int) -> BranchReport:
    if not physical_exact_two(m, n, r, s):
        raise ValueError("Stage15-6ac report expects an exactly-two survivor")
    split = classify_core(m, n, r, s)
    charge = actual_outer_charge(m, n, r, s)
    q = charge.q
    if q != split.k_S * split.k_O:
        raise AssertionError("6aa/6ab core disagreement")
    R0 = dyadic_base(r)
    S0 = dyadic_base(s)
    V = R0 * S0
    high = q * q >= V
    bound = None
    if high:
        # AR-009's explicit line bound is <= 1 + 6 V/q.
        # Under q^2 >= V this is <= 1 + 6 sqrt(V), rounded safely.
        bound = 1 + math.ceil(6 * V / q)
        if bound > 1 + 6 * math.ceil(math.sqrt(V)):
            raise AssertionError("high-core square-root collapse failed")
    return BranchReport(
        params=(m, n, r, s),
        k=split.k,
        q=q,
        R0=R0,
        S0=S0,
        V=V,
        branch="HIGH" if high else "LOW",
        high_core_bound=bound,
    )


def cross_gcd_report(m: int, n: int, r: int, s: int) -> dict:
    if math.gcd(m, n) != 1 or math.gcd(r, s) != 1:
        raise ValueError("primitive toric pairs required")
    h_alpha = math.gcd(m * r, n * s)
    h_beta = math.gcd(m * s, n * r)
    g_ms = math.gcd(m, s)
    g_nr = math.gcd(n, r)
    g_mr = math.gcd(m, r)
    g_ns = math.gcd(n, s)
    if h_alpha != g_ms * g_nr:
        raise AssertionError("h_alpha cross-gcd identity failed")
    if h_beta != g_mr * g_ns:
        raise AssertionError("h_beta cross-gcd identity failed")
    if math.gcd(g_ms, g_nr) != 1 or math.gcd(g_mr, g_ns) != 1:
        raise AssertionError("cross-gcd factors should be coprime")
    return {
        "h_alpha": h_alpha,
        "h_beta": h_beta,
        "gcd_m_s": g_ms,
        "gcd_n_r": g_nr,
        "gcd_m_r": g_mr,
        "gcd_n_s": g_ns,
    }


def gmul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c


def gdiv_exact(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int] | None:
    a, b = z
    c, d = w
    norm = c * c + d * d
    nr = a * c + b * d
    ni = b * c - a * d
    if nr % norm or ni % norm:
        return None
    return nr // norm, ni // norm


def gaussian_square_root(z: tuple[int, int]) -> tuple[int, int] | None:
    A, B = z
    norm = A * A + B * B
    t = math.isqrt(norm)
    if t * t != norm:
        return None
    if (t + A) % 2 or (t - A) % 2:
        return None
    a2 = (t + A) // 2
    b2 = (t - A) // 2
    if a2 < 0 or b2 < 0:
        return None
    a = math.isqrt(a2)
    b = math.isqrt(b2)
    if a * a != a2 or b * b != b2:
        return None
    for aa in ({a, -a} if a else {0}):
        for bb in ({b, -b} if b else {0}):
            if (aa * aa - bb * bb, 2 * aa * bb) == z:
                return aa, bb
    return None


def gaussian_core_representations(k: int) -> list[tuple[int, int]]:
    if k <= 0:
        raise ValueError("positive Gaussian core norm required")
    reps: set[tuple[int, int]] = set()
    for a in range(math.isqrt(k) + 1):
        b2 = k - a * a
        b = math.isqrt(b2)
        if b * b != b2:
            continue
        for aa in {a, -a}:
            for bb in {b, -b}:
                reps.add((aa, bb))
                reps.add((bb, aa))
    reps.discard((0, 0))
    return sorted(reps)


def find_gaussian_square_lift(
    z: tuple[int, int], k: int
) -> tuple[tuple[int, int], tuple[int, int]]:
    if math.gcd(abs(z[0]), abs(z[1])) != 1:
        raise ValueError("primitive Gaussian integer required")
    for core in gaussian_core_representations(k):
        quotient = gdiv_exact(z, core)
        if quotient is None:
            continue
        root = gaussian_square_root(quotient)
        if root is not None:
            if gmul(core, gmul(root, root)) != z:
                raise AssertionError("Gaussian square lift reconstruction failed")
            return core, root
    raise AssertionError(f"no Gaussian core-square lift found for z={z}, k={k}")


def low_core_lift_report(m: int, n: int, r: int, s: int) -> dict:
    br = branch_report(m, n, r, s)
    if br.branch != "LOW":
        raise ValueError("low-core lift requested on high-core witness")
    nf = normal_form(m, n, r, s)
    k = int(nf["k"])
    cross = cross_gcd_report(m, n, r, s)
    h_alpha = cross["h_alpha"]
    h_beta = cross["h_beta"]
    alpha0 = (m * r // h_alpha, n * s // h_alpha)
    beta0 = (m * s // h_beta, n * r // h_beta)
    if math.gcd(*alpha0) != 1 or math.gcd(*beta0) != 1:
        raise AssertionError("primitive Gaussian reduction failed")
    core_alpha, root_alpha = find_gaussian_square_lift(alpha0, k)
    core_beta, root_beta = find_gaussian_square_lift(beta0, k)
    return {
        "params": [m, n, r, s],
        "k": k,
        "q": br.q,
        "V": br.V,
        "h_alpha": h_alpha,
        "h_beta": h_beta,
        "alpha0": list(alpha0),
        "beta0": list(beta0),
        "Pi_alpha": list(core_alpha),
        "Pi_beta": list(core_beta),
        "z": list(root_alpha),
        "w": list(root_beta),
    }


def witness_report() -> dict[str, list[dict]]:
    high_witnesses = [
        (13, 1, 9, 1),
        (9, 1, 27, 14),
    ]
    low_witnesses = [
        (5, 3, 7, 4),
        (31, 7, 31, 23),
        (11, 1, 29, 22),
    ]
    high = []
    for params in high_witnesses:
        br = branch_report(*params)
        if br.branch != "HIGH":
            raise AssertionError(f"expected high-core witness: {params}")
        high.append(
            {
                "params": list(params),
                "k": br.k,
                "q": br.q,
                "V": br.V,
                "bound": br.high_core_bound,
            }
        )
    low = [low_core_lift_report(*params) for params in low_witnesses]
    return {"high": high, "low": low}


if __name__ == "__main__":
    report = witness_report()
    print("STAGE15_6AC_HIGH_LOW_CORE=PASS")
    for row in report["high"]:
        print(f"HIGH={row['params']} q={row['q']} V={row['V']} bound={row['bound']}")
    for row in report["low"]:
        print(
            f"LOW={row['params']} q={row['q']} V={row['V']} "
            f"hA={row['h_alpha']} hB={row['h_beta']}"
        )
