#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

LOCKS = {
    "td02_bounded_source": (
        "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_bounded.py",
        "8dc7b6255b31a79aa7f51141f1ac5a5b8137efc0",
    ),
    "td01_audited_envelope": (
        "stages/stage32/32-01-178/topdown-01/EXACT-X4-ENVELOPE-BOUND.json",
        "51271c11078459ad9171138c4fb6121d7a665c39",
    ),
}

HMAX = 96
EXPECTED_FIXED_T_STATES = 912_673
EXPECTED_BOUNDED_STATES = 18_785
EXPECTED_BOUNDED_STRICT = 18_626
EXPECTED_BOUNDED_EQUAL = 159
EXPECTED_MAX_GAP = Fraction(5120, 23)
EXPECTED_MAX_GAP_WITNESS = (0, 0, -32)


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def checked_raw(rel: str, expected: str) -> bytes:
    path = ROOT / rel
    req(path.is_file(), f"missing source {rel}")
    raw = path.read_bytes()
    req(git_blob(raw) == expected, f"source drift {rel}")
    return raw


def qmin2(total: int) -> int:
    # Exact minimum of x^2+y^2 over nonnegative integer x+y=total.
    return (total * total + (total & 1)) // 2


def qmin3(total: int) -> int:
    # Exact minimum of x^2+y^2+z^2 over nonnegative integer x+y+z=total.
    q, r = divmod(total, 3)
    return r * (q + 1) ** 2 + (3 - r) * q * q


def qbc_integer_lower(b: int, c: int, t: int, u: int) -> int:
    # u=x1+x9, t=x0+x1+x6+x9.
    # At fixed (b,c,t,u), the three two-variable splits are independent after
    # dropping canonical restrictions, so qmin2 is an exact relaxed minimum.
    return (
        qmin2(u)
        + (b - u) ** 2
        + qmin2(t - u)
        + qmin2(c - t + u)
    )


def feasible_u_interval(b: int, c: int, t: int) -> tuple[int, int]:
    return max(0, t - c), min(b, t)


def fast_u_candidates(b: int, c: int, t: int) -> tuple[int, ...]:
    # For fixed t, the real qBC relaxation has center
    # u0=(2b+2t-c)/5 and curvature (5/2)(u-u0)^2.
    # The integer correction from the three qmin2 terms is in [0,3/2].
    # Hence, inside the feasible interval, no integer beyond floor/ceil(u0)
    # can beat both nearest integers; outside, the integer boundary is exact.
    lo, hi = feasible_u_interval(b, c, t)
    req(lo <= hi, f"empty u interval {(b,c,t)}")
    num = 2 * b + 2 * t - c
    floor_u0 = num // 5
    ceil_u0 = -((-num) // 5)
    return tuple(sorted({max(lo, min(hi, floor_u0)), max(lo, min(hi, ceil_u0))}))


def fixed_t_min_fast(b: int, c: int, t: int) -> int:
    return min(qbc_integer_lower(b, c, t, u) for u in fast_u_candidates(b, c, t))


def fixed_t_min_brute(b: int, c: int, t: int) -> int:
    lo, hi = feasible_u_interval(b, c, t)
    return min(qbc_integer_lower(b, c, t, u) for u in range(lo, hi + 1))


def integer_bc_grf_min(b: int, c: int, D: int) -> int:
    # Exact minimum of the integer-relaxed BC contribution to
    # 6*q + (D-t)^2 after only canonical restrictions are dropped.
    return min(
        6 * fixed_t_min_fast(b, c, t) + (D - t) ** 2
        for t in range(b + c + 1)
    )


def real_bc_grf_min(b: int, c: int, D: int) -> Fraction:
    return Fraction(
        3 * (
            6 * D * D
            - 8 * D * b
            - 6 * D * c
            + 18 * b * b
            + 4 * b * c
            + 13 * c * c
        ),
        23,
    )


def real_bc_objective(b: int, c: int, D: int, u: Fraction, t: Fraction) -> Fraction:
    qbc = (
        u * u / 2
        + (b - u) ** 2
        + (t - u) ** 2 / 2
        + (c - t + u) ** 2 / 2
    )
    return 6 * qbc + (D - t) ** 2


def main() -> None:
    raws = {name: checked_raw(rel, sha) for name, (rel, sha) in LOCKS.items()}
    td01 = json.loads(raws["td01_audited_envelope"])
    deriv = td01["exact_envelope_derivation"]
    req(deriv["hpadj08_replay_domain_exact_cardinality"] == 47_589_703_313_957_134_107_892, "TD01 replay domain")
    req(deriv["hpadj08_exact_square_survivor_envelope"] == 6_703_403_803_993_209_250_491, "TD01 envelope")

    # Exact pair-split identity over the entire production sum range.
    for s in range(2 * HMAX + 1):
        brute = min(x * x + (s - x) ** 2 for x in range(s + 1))
        req(brute == qmin2(s), f"qmin2 mismatch {s}")

    # Exact A-group three-square minimum over production a<=96.
    for a in range(HMAX + 1):
        brute = min(
            x * x + y * y + (a - x - y) ** 2
            for x in range(a + 1)
            for y in range(a - x + 1)
        )
        req(brute == qmin3(a), f"qmin3 mismatch {a}")
        correction = 0 if a % 3 == 0 else 4
        req(6 * qmin3(a) == 2 * a * a + correction, f"qmin3 correction {a}")

    # Production-wide verification of the O(1)-candidate u minimizer.
    fixed_t_states = 0
    for b in range(HMAX + 1):
        for c in range(HMAX + 1):
            for t in range(b + c + 1):
                req(fixed_t_min_fast(b, c, t) == fixed_t_min_brute(b, c, t), f"fast-u mismatch {(b,c,t)}")
                fixed_t_states += 1
    req(fixed_t_states == EXPECTED_FIXED_T_STATES, f"fixed-t state count {fixed_t_states}")

    # Independent bounded comparison against the MAIN real quadratic minimum.
    strict = equal = 0
    max_gap = Fraction(-1, 1)
    max_witness = None
    bounded_states = 0
    for b in range(17):
        for c in range(17):
            for D in range(-32, 33):
                ustar = Fraction(2 * D + 14 * b - c, 23)
                tstar = Fraction(5 * D + 12 * b + 9 * c, 23)
                real_min = real_bc_grf_min(b, c, D)
                req(real_bc_objective(b, c, D, ustar, tstar) == real_min, f"real minimizer identity {(b,c,D)}")
                integer_min = integer_bc_grf_min(b, c, D)
                gap = Fraction(integer_min, 1) - real_min
                req(gap >= 0, f"integer relaxation weakened {(b,c,D,gap)}")
                if gap > 0:
                    strict += 1
                else:
                    equal += 1
                if gap > max_gap:
                    max_gap = gap
                    max_witness = (b, c, D)
                bounded_states += 1

    req(bounded_states == EXPECTED_BOUNDED_STATES, f"bounded states {bounded_states}")
    req(strict == EXPECTED_BOUNDED_STRICT, f"strict count {strict}")
    req(equal == EXPECTED_BOUNDED_EQUAL, f"equal count {equal}")
    req(max_gap == EXPECTED_MAX_GAP, f"max gap {max_gap}")
    req(max_witness == EXPECTED_MAX_GAP_WITNESS, f"max witness {max_witness}")

    print(json.dumps({
        "production_fixed_t_states_verified": fixed_t_states,
        "bounded_bcD_states": bounded_states,
        "bounded_strict_integer_gain_states": strict,
        "bounded_equal_states": equal,
        "bounded_max_gap": f"{max_gap.numerator}/{max_gap.denominator}",
        "bounded_max_gap_witness": list(max_witness),
        "main_q_quadratic_candidate_external_reference": {
            "pr": 1808,
            "exact_head": "6489e1fb9f35b8ecdc19c982301a816d956711e9",
            "candidate_blob_sha1": "1d669114e930951b9d5f9f82a6abb2b59cd43884",
            "candidate_upper_bound": 195_603_649_074_545_538_415,
            "authority_or_credit_inherited": False
        }
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
