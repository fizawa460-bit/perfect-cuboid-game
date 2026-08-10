#!/usr/bin/env python3
"""Stage14-t74: canonical host / short angular cofactor audit."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T73 = ROOT / "stages/stage14/14-t73/result.md"
S734 = ROOT / "stages/stage14/14-s7-34/result.md"
B_FROZEN = 10_000


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def v2(n: int) -> int:
    n = abs(n)
    e = 0
    while n and n % 2 == 0:
        n //= 2
        e += 1
    return e


def factor(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n: int) -> list[int]:
    out = [1]
    for p, e in factor(n).items():
        base = list(out)
        pe = 1
        for _ in range(e):
            pe *= p
            out += [d * pe for d in base]
    return sorted(out)


def gaussian_unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def reconstruct_candidates(*, a: int, b: int, ell: int, m: int, eps: int,
                           k: int, h: int, c: int) -> set[tuple[int, int, int]]:
    """Finite shadow of fixed-(direction,ell,c) divisor reconstruction."""
    H = oddpart(h)
    if c % H:
        return set()
    RV = c // H
    Dpi_odd = oddpart(b * b - a * a)
    ans: set[tuple[int, int, int]] = set()

    for g0 in divisors(Dpi_odd):
        odd_DV = g0 * RV
        if gcd(Dpi_odd, odd_DV) != g0:
            continue
        for e in range((2 * B_FROZEN).bit_length() + 1):
            DV = odd_DV << e
            if DV <= 0 or DV > 2 * B_FROZEN:
                continue
            for r in divisors(DV):
                t = DV // r
                if r >= t:
                    continue
                if gcd(r, t) not in (1, 2):
                    continue
                if (r + t) & 1:
                    continue
                p = (t - r) // 2
                q = (t + r) // 2
                if p <= 0 or gcd(p, q) != 1:
                    continue
                n = p * p + q * q
                if n % k:
                    continue
                delta = n // k
                if eps * ell * m * delta > 2 * B_FROZEN:
                    continue
                if not (a * q < b * p and a * p < b * q):
                    continue
                if gcd(oddpart(b * b - a * a), oddpart(q * q - p * p)) != g0:
                    continue
                ans.add((p, q, delta))
    return ans


def main() -> None:
    assert "STAGE14_T73=COMPLETE_KAPPA_ONE_LINEAR_FACTORIZATION_FIXED_TAG_CONDITIONING_AND_UNIFORM_FIXED_NORM_FIBER_REDUCTION" in T73.read_text()
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=47/80" in S734.read_text()

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560 and len(invisible) == 419

    canonical_host_checks = ell_free_balance_checks = 0
    short_hyperbola_checks = short_factor_checks = 0
    reconstruction_checks = 0
    records = []
    c_hist = Counter()
    g_hist = Counter()
    max_candidates = 0
    cache: dict[tuple, set[tuple[int, int, int]]] = {}

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        kappa = st["kernel"]
        k = n // delta
        h = eps * m // k
        assert h * k == eps * m

        s0 = Fraction(b * b * p * p - a * a * q * q,
                      b * b * q * q - a * a * p * p)
        sq = s0 / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator and gcd(u, v) == 1

        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        G = gcd(raw_plus, raw_minus)
        Pplus, Pminus = raw_plus // G, raw_minus // G
        assert gcd(Pplus, Pminus) == 1 and Pplus > Pminus > 0

        assert Pminus % ell == 0
        assert factor(Pminus).get(ell, 0) == 1
        assert gcd(ell, kappa * u * v) == 1
        rho = (v * pow(u, -1, ell)) % ell
        assert (rho * rho - kappa) % ell == 0
        assert rho != (-rho) % ell
        canonical_host_checks += 1

        Q = Pminus // ell
        Dpi = b * b - a * a
        DV = q * q - p * p
        assert Dpi > 0 and DV > 0
        H = oddpart(h)
        D = oddpart(delta)
        g = gcd(oddpart(Dpi), oddpart(DV))
        Rpi = oddpart(Dpi) // g
        RV = oddpart(DV) // g
        c = oddpart(Q)

        assert oddpart(Pplus) == D * Rpi
        assert oddpart(Pminus) == ell * H * RV
        assert c == H * RV
        assert gcd(oddpart(Pplus), c) == 1

        assert ell * h * DV * Pplus == eps * delta * Dpi * Pminus
        assert h * DV * Pplus == eps * delta * Dpi * Q
        ell_free_balance_checks += 1

        assert eps * ell * m * delta <= 2 * B_FROZEN
        assert ell * ell > 4 * B_FROZEN
        assert c < eps * m * delta
        assert 2 * c < ell
        assert ell * c < 2 * B_FROZEN
        assert c * c < B_FROZEN
        assert g * c < H * k * delta
        assert ell * g * c < 2 * B_FROZEN
        short_hyperbola_checks += 1

        r, t = q - p, q + p
        assert 0 < r < t
        assert gcd(r, t) in (1, 2)
        assert r * t == DV
        assert r * r + t * t == 2 * n == 2 * k * delta
        assert t * t < 2 * n < ell
        assert h * ell * (r * r + t * t) <= 4 * B_FROZEN
        assert oddpart(r * t) == g * c // H
        short_factor_checks += 1

        beta = gcd(kappa, v)
        packet = (gaussian_unit_key(st["U"]), eps, k, h)
        records.append({
            "packet": packet,
            "kappa": kappa,
            "beta": beta,
            "ell": ell,
            "c": c,
            "g": g,
            "v2_DV": v2(DV),
        })
        c_hist[c] += 1
        g_hist[g] += 1

        key = (a, b, ell, m, eps, k, h, c)
        if key not in cache:
            cache[key] = reconstruct_candidates(a=a, b=b, ell=ell, m=m,
                                                eps=eps, k=k, h=h, c=c)
        candidates = cache[key]
        assert (p, q, delta) in candidates
        max_candidates = max(max_candidates, len(candidates))
        reconstruction_checks += 1

    by_ell_c = Counter((rec["packet"], rec["ell"], rec["c"]) for rec in records)
    by_tagged = Counter(
        (rec["packet"], rec["kappa"], rec["beta"], rec["ell"], rec["c"])
        for rec in records
    )

    report = {
        "stage": "14-t74",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "canonical_host_checks": canonical_host_checks,
        "ell_free_balance_checks": ell_free_balance_checks,
        "short_hyperbola_checks": short_hyperbola_checks,
        "short_factor_ellipse_checks": short_factor_checks,
        "reconstruction_checks": reconstruction_checks,
        "max_frozen_reconstruction_candidates_per_direction_ell_c": max_candidates,
        "max_frozen_packet_ell_c_multiplicity": max(by_ell_c.values(), default=0),
        "max_frozen_tagged_packet_ell_c_multiplicity": max(by_tagged.values(), default=0),
        "most_common_c": c_hist.most_common(12),
        "most_common_g": g_hist.most_common(12),
        "max_v2_DV": max((rec["v2_DV"] for rec in records), default=0),
        "boundary": {
            "STAGE14_T74": "COMPLETE_CANONICAL_HOST_ELL_FREE_COFACTOR_BALANCE_AND_SHORT_ANGULAR_COVER_REDUCTION",
            "MERGED_T73_IMPORTED": True,
            "MERGED_S7_34_GLOBAL_47_80_LEDGER_IMPORTED": True,
            "CANONICAL_ELL_TWO_ROOT_HOST_ORIENTATIONS_PROVED": True,
            "CANONICAL_ELL_HOST_ORIENTATION_COST": "O1",
            "CANONICAL_ELL_CANCELS_EXACTLY_FROM_CAYLEY_BALANCE": True,
            "ELL_FREE_RESIDUAL_COFACTOR_BALANCE_PROVED": True,
            "ODD_PMINUS_OVER_ELL_EQUALS_H_TIMES_RV": True,
            "SHARP_ELL_C_HYPERBOLA_PROVED": True,
            "SHARP_ELL_G_C_HYPERBOLA_PROVED": True,
            "CANONICAL_ODD_COFACTOR_LT_SQRT_B": True,
            "COVER_DEFICIT_LINEAR_FACTORIZATION_RESTORED": True,
            "COVER_LINEAR_FACTORS_LT_SQRT_ELL": True,
            "SHORT_COVER_ELLIPSE_PROVED": True,
            "FIXED_PACKET_ELL_C_PHYSICAL_FIBER": "Bo1",
            "FIXED_TAGGED_PACKET_ELL_C_PHYSICAL_FIBER": "Bo1",
            "MOVING_NORM_VALUE_PARAMETER_REDUCED_TO_ELL_C": True,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "47/80",
            "T74_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING": False,
            "TH20_NEEDED": True,
            "TH20_PRE_T74_TARGET_MINIMAL": False,
            "TH20_REQUESTED_OBJECT": "SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve",
            "T_ROUTE_BLOCKED_WAITING_FOR_TH20": False,
            "NEXT": "Stage14-t75",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
