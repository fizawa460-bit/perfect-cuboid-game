#!/usr/bin/env python3
from __future__ import annotations

import math
from dataclasses import dataclass

from stage15_4_normal_form import normal_form, prime_factors, recover_toric_params
from stage15_6aa_core_adapter import classify_core, physical_exact_two


@dataclass(frozen=True)
class OuterCharge:
    m: int
    n: int
    H_plus: int
    H_minus: int
    candidate_count: int
    actual_k_S: int
    actual_k_O: int
    q: int


def allowed_odd_primes(n: int) -> tuple[int, ...]:
    return tuple(p for p in prime_factors(abs(n)) if p % 4 == 1)


def squarefree_divisor_count_1mod4(n: int) -> int:
    return 1 << len(allowed_odd_primes(n))


def candidate_core_count(m: int, n: int) -> int:
    if not (m > n > 0 and math.gcd(m, n) == 1):
        raise ValueError("primitive positive outer pair required")
    hp = m * m + n * n
    hm = m * m - n * n
    return squarefree_divisor_count_1mod4(hp) * squarefree_divisor_count_1mod4(hm)


def actual_outer_charge(m: int, n: int, r: int, s: int) -> OuterCharge:
    split = classify_core(m, n, r, s)
    hp = m * m + n * n
    hm = m * m - n * n
    if hp % split.k_S or hm % split.k_O:
        raise AssertionError("actual channel core is not an outer divisor label")
    if math.gcd(hp, hm) not in (1, 2):
        raise AssertionError("odd outer hosts are not coprime")
    count = candidate_core_count(m, n)
    if count < 1:
        raise AssertionError("empty candidate core set")
    return OuterCharge(
        m=m,
        n=n,
        H_plus=hp,
        H_minus=hm,
        candidate_count=count,
        actual_k_S=split.k_S,
        actual_k_O=split.k_O,
        q=split.k_S * split.k_O,
    )


def physical_parameter_bound_report(m: int, n: int, r: int, s: int) -> dict:
    nf = normal_form(m, n, r, s)
    e, x, y, u, v = map(int, nf["physical"])
    R2 = int(nf["physical_R2"])
    B = math.isqrt(R2)
    if B * B < R2:
        B += 1
    recovered = recover_toric_params(e, x, y, u, v)
    if recovered != (m, n, r, s):
        raise AssertionError("physical inverse did not recover toric parameters")
    if max(e, x, y, u, v) > B:
        raise AssertionError("physical coordinate exceeded geometric height")
    if not (m <= 2 * B and n <= B and r <= 2 * B and s <= B):
        raise AssertionError("physical inverse parameter bound failed")
    hp = m * m + n * n
    hm = m * m - n * n
    if hp > 5 * B * B or hm >= 4 * B * B:
        raise AssertionError("outer host polynomial bound failed")
    return {
        "params": [m, n, r, s],
        "physical": [e, x, y, u, v],
        "B": B,
        "m_le_2B": m <= 2 * B,
        "n_le_B": n <= B,
        "r_le_2B": r <= 2 * B,
        "s_le_B": s <= B,
        "H_plus": hp,
        "H_minus": hm,
    }


def mixed_root_line_report(m: int, n: int, r: int, s: int) -> dict:
    charge = actual_outer_charge(m, n, r, s)
    q = charge.q
    if q == 1:
        rho = 0
        roots_upper_bound = 1
    else:
        if math.gcd(s, q) != 1 or math.gcd(r, q) != 1:
            raise AssertionError("inner pair is not a unit modulo actual odd core")
        rho = (r * pow(s, -1, q)) % q
        if charge.actual_k_S > 1 and (rho * rho - 1) % charge.actual_k_S:
            raise AssertionError("S-channel diagonal root condition failed")
        if charge.actual_k_O > 1 and (rho * rho + 1) % charge.actual_k_O:
            raise AssertionError("O-channel Gaussian root condition failed")
        roots_upper_bound = 1 << len(prime_factors(q))
    return {
        "params": [m, n, r, s],
        "k_S": charge.actual_k_S,
        "k_O": charge.actual_k_O,
        "q": q,
        "rho": rho,
        "root_orientation_upper_bound": roots_upper_bound,
        "candidate_core_count": charge.candidate_count,
    }


def witness_report() -> list[dict]:
    witnesses = [
        (13, 1, 9, 1),
        (13, 4, 13, 1),
        (9, 1, 27, 14),
    ]
    out = []
    for params in witnesses:
        if not physical_exact_two(*params):
            raise AssertionError(f"witness is not exactly-two: {params}")
        charge = actual_outer_charge(*params)
        row = physical_parameter_bound_report(*params)
        row.update(mixed_root_line_report(*params))
        row.update(
            {
                "actual_k_S": charge.actual_k_S,
                "actual_k_O": charge.actual_k_O,
                "candidate_count": charge.candidate_count,
            }
        )
        out.append(row)
    return out


def scan_small_outer_pairs(limit: int = 40) -> dict[str, int]:
    pairs = 0
    max_candidates = 0
    max_pair = (0, 0)
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1:
                continue
            pairs += 1
            c = candidate_core_count(m, n)
            if c > max_candidates:
                max_candidates = c
                max_pair = (m, n)
    return {
        "primitive_outer_pairs": pairs,
        "max_candidate_core_count": max_candidates,
        "max_pair_m": max_pair[0],
        "max_pair_n": max_pair[1],
    }


if __name__ == "__main__":
    print("STAGE15_6AB_CORE_CHARGE=PASS")
    print(scan_small_outer_pairs())
    for row in witness_report():
        print(
            f"WITNESS={row['params']} q={row['q']} candidates={row['candidate_count']} "
            f"rho={row['rho']}"
        )
