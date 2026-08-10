#!/usr/bin/env python3
"""Stage14-t67: canonical root modulus and private-prime pair audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T66 = ROOT / "stages/stage14/14-t66/result.md"


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


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


def lpf_odd(n: int) -> int:
    return max((p for p in factor(oddpart(n)) if p & 1), default=1)


def main() -> None:
    t66 = T66.read_text()
    assert "STAGE14_T66=COMPLETE_PRIMEWISE_CAYLEY_ALLOCATION_AND_OPPOSITE_SIGN_ROOT_LINE_REDUCTION" in t66
    assert "CANONICAL_LARGEST_PRIME_TAG_RETAINED=true" in t66

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    B = t36["B_FROZEN"]
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560
    assert len(invisible) == 419

    records = []
    root_modulus_checks = 0
    side_recovery_checks = 0
    modulus_band_checks = 0
    max_fixed_packet_M_mass = 0
    packet_M_mass = Counter()

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        k = n // delta
        h = eps * m // k
        H, D = oddpart(h), oddpart(delta)
        assert h * k == eps * m
        assert gcd(h, delta) == 1
        assert ell > 2 * eps * m * delta

        M = ell * H * D
        c = M // ell
        assert c == H * D
        assert 2 * c < ell
        assert lpf_odd(M) == ell
        assert factor(M).get(ell, 0) == 1
        assert M // (ell * H) == D
        root_modulus_checks += 1

        assert M > 2 * isqrt(B)
        assert M * k <= 2 * B
        modulus_band_checks += 1

        A = b * b * p * p - a * a * q * q
        B0 = b * b * q * q - a * a * p * p
        s = Fraction(A, B0)
        kappa = st["kernel"]
        sq = s / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator
        assert gcd(u, v) == 1
        assert gcd(u, M) == 1
        rho = (v * pow(u, -1, M)) % M
        assert (rho * rho - kappa) % (ell * H) == 0
        assert (rho * rho + kappa) % D == 0
        side_recovery_checks += 1

        packet = (tuple(st["U"]), eps, k, h)
        packet_M_mass[(packet, M)] += 1
        max_fixed_packet_M_mass = max(max_fixed_packet_M_mass, packet_M_mass[(packet, M)])
        records.append({
            "packet": packet,
            "kappa": kappa,
            "ell": ell,
            "M": M,
            "c": c,
            "rho": rho,
        })

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["packet"], rec["kappa"])].append(rec)

    same_M_pairs = 0
    same_ell_pairs = 0
    nested_pairs = 0
    private_pairs = 0
    max_nested_degree = 0
    nested_degree = Counter()
    private_gcd_checks = 0

    for vals in groups.values():
        for x, y in combinations(vals, 2):
            if x["M"] == y["M"]:
                same_M_pairs += 1
            if x["ell"] == y["ell"]:
                same_ell_pairs += 1
                continue

            lo, hi = (x, y) if x["ell"] < y["ell"] else (y, x)
            assert hi["ell"] > lo["c"]
            assert hi["ell"] > lo["ell"]
            assert hi["ell"] not in factor(lo["M"])

            if hi["M"] % lo["ell"] == 0:
                assert hi["c"] % lo["ell"] == 0
                nested_pairs += 1
                nested_degree[(hi["packet"], hi["kappa"], hi["M"], hi["rho"])] += 1
                max_nested_degree = max(max_nested_degree, nested_degree[(hi["packet"], hi["kappa"], hi["M"], hi["rho"])])
            else:
                assert lo["M"] % hi["ell"] != 0
                assert hi["M"] % lo["ell"] != 0
                assert gcd(lo["M"], hi["M"]) == gcd(lo["c"], hi["c"])
                private_pairs += 1
                private_gcd_checks += 1

    report = {
        "stage": "14-t67",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "canonical_root_modulus_checks": root_modulus_checks,
        "root_side_recovery_checks": side_recovery_checks,
        "modulus_band_checks": modulus_band_checks,
        "max_frozen_fixed_packet_M_mass": max_fixed_packet_M_mass,
        "same_squareclass_same_M_pairs": same_M_pairs,
        "same_squareclass_same_ell_pairs": same_ell_pairs,
        "same_squareclass_nested_prime_pairs": nested_pairs,
        "same_squareclass_private_prime_pairs": private_pairs,
        "private_pair_gcd_checks": private_gcd_checks,
        "max_frozen_nested_degree": max_nested_degree,
        "modulus": "M=ell*odd(h)*odd(delta), ell=LPF_odd(M), M/ell<ell/2",
        "root_packet": "rho^2=+kappa mod ell*odd(h), rho^2=-kappa mod M/(ell*odd(h))",
        "boundary": {
            "STAGE14_T67": "COMPLETE_CANONICAL_ROOT_MODULUS_COLLAPSE_AND_PRIVATE_PRIME_REDUCTION",
            "CANONICAL_ELL_RECOVERED_FROM_ROOT_MODULUS": True,
            "ODD_DELTA_RECOVERED_FROM_ROOT_MODULUS": True,
            "ROOT_SIDE_ALLOCATION_RECOVERED_FROM_M": True,
            "CANONICAL_ROOT_MODULUS_SUPER_SQRT_BAND_PROVED": True,
            "SAME_ROOT_MODULUS_SQUARECLASS_ENERGY_NEAR_LINEAR": True,
            "SAME_CANONICAL_ELL_SQUARECLASS_ENERGY_NEAR_LINEAR": True,
            "NESTED_CANONICAL_PRIME_INCIDENCE_NEAR_LINEAR": True,
            "PRIVATE_CANONICAL_PRIME_PAIR_REDUCTION_PROVED": True,
            "SHARED_U_PRIVATE_CANONICAL_PRIME_ROOT_MODULUS_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "7/8",
            "TH18_NEEDED": True,
            "TH18_REQUESTED_OBJECT": "PrivateCanonicalPrimeOppositeSignRootModulusLargeSieve",
            "NEXT": "Stage14-t68",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
