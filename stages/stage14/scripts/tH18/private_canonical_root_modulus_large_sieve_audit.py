#!/usr/bin/env python3
"""Stage14-tH18: private canonical-prime opposite-sign root-modulus large-sieve audit."""

from __future__ import annotations

from collections import defaultdict
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
T67 = ROOT / "stages/stage14/14-t67/result.md"
RESULT = ROOT / "stages/stage14/14-tH18/result.md"
SUMMARY = ROOT / "stages/stage14/data/tH18/private_canonical_root_modulus_large_sieve_summary.json"


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def factor(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def lpf_odd(n: int) -> int:
    return max((p for p in factor(oddpart(n)) if p & 1), default=1)


def circular_numerator(r1: int, m1: int, r2: int, m2: int) -> int:
    den = m1 * m2
    d = abs(r1 * m2 - r2 * m1)
    d %= den
    return min(d, den - d)


def build_records():
    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560
    assert len(invisible) == 419

    records = []
    quartic_checks = 0
    crt_checks = 0
    for st in invisible:
        eps, ell, m, n, delta = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        k = n // delta
        h = eps * m // k
        H, D = oddpart(h), oddpart(delta)
        M = ell * H * D
        c = M // ell
        kappa = st["kernel"]

        assert h * k == eps * m
        assert gcd(h, delta) == 1
        assert 2 * c < ell
        assert lpf_odd(M) == ell
        assert factor(M).get(ell, 0) == 1

        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        A0 = b * b * p * p - a * a * q * q
        B0 = b * b * q * q - a * a * p * p
        s = Fraction(A0, B0)
        sq = s / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u * u == sq.numerator and v * v == sq.denominator
        assert gcd(u, v) == 1
        assert gcd(u, M) == 1
        rho = (v * pow(u, -1, M)) % M

        Amod = ell * H
        Dmod = D
        assert gcd(Amod, Dmod) == 1
        assert (rho * rho - kappa) % Amod == 0
        assert (rho * rho + kappa) % Dmod == 0
        assert gcd(rho, M) == 1
        assert (pow(rho, 4, M) - (kappa * kappa) % M) % M == 0
        quartic_checks += 1

        alpha = rho % Amod
        beta = rho % Dmod if Dmod > 1 else 0
        if Dmod > 1:
            invD = pow(Dmod, -1, Amod)
            invA = pow(Amod, -1, Dmod)
            reconstructed = (alpha * Dmod * invD + beta * Amod * invA) % M
            assert reconstructed == rho
        else:
            # CRT degenerates to the A-side only.
            reconstructed = alpha % M
            assert reconstructed == rho
        crt_checks += 1

        packet = (tuple(st["U"]), eps, k, h)
        records.append({
            "packet": packet,
            "kappa": kappa,
            "ell": ell,
            "H": H,
            "D": D,
            "M": M,
            "c": c,
            "rho": rho,
        })
    return reps, invisible, records, quartic_checks, crt_checks


def main() -> None:
    t66 = T66.read_text()
    t67 = T67.read_text()
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())

    assert "STAGE14_T66=COMPLETE_PRIMEWISE_CAYLEY_ALLOCATION_AND_OPPOSITE_SIGN_ROOT_LINE_REDUCTION" in t66
    assert "OPPOSITE_SIGN_QUADRATIC_ROOT_CONGRUENCES_PROVED=true" in t66
    assert "STAGE14_T67=COMPLETE_CANONICAL_ROOT_MODULUS_COLLAPSE_AND_PRIVATE_PRIME_REDUCTION" in t67
    assert "PRIVATE_CANONICAL_PRIME_PAIR_REDUCTION_PROVED=true" in t67

    reps, invisible, records, quartic_checks, crt_checks = build_records()

    groups = defaultdict(list)
    for rec in records:
        groups[(rec["packet"], rec["kappa"])].append(rec)

    private_pairs = 0
    determinant_checks = 0
    private_prime_nondiv_checks = 0
    min_scaled_gap = None
    min_gap_witness = None

    for vals in groups.values():
        for x, y in combinations(vals, 2):
            if x["M"] == y["M"] or x["ell"] == y["ell"]:
                continue
            lo, hi = (x, y) if x["ell"] < y["ell"] else (y, x)
            if hi["M"] % lo["ell"] == 0:
                # nested pair: t67 already closes it, and tH18 must not recharge it.
                continue
            assert lo["M"] % hi["ell"] != 0
            assert hi["M"] % lo["ell"] != 0
            private_pairs += 1

            g = gcd(lo["M"], hi["M"])
            assert g == gcd(lo["c"], hi["c"])
            num = circular_numerator(lo["rho"], lo["M"], hi["rho"], hi["M"])
            assert num > 0
            assert num % g == 0
            # Exact Farey-scale lower bound: num/(M1*M2) >= g/(M1*M2).
            assert num >= g
            determinant_checks += 1

            raw_det = lo["rho"] * hi["M"] - hi["rho"] * lo["M"]
            assert raw_det % lo["ell"] != 0
            assert raw_det % hi["ell"] != 0
            private_prime_nondiv_checks += 1

            gap = Fraction(num, lo["M"] * hi["M"])
            Q = max(lo["M"], hi["M"])
            scaled = gap * Q
            if min_scaled_gap is None or scaled < min_scaled_gap:
                min_scaled_gap = scaled
                min_gap_witness = {
                    "M1": lo["M"], "ell1": lo["ell"], "rho1": lo["rho"],
                    "M2": hi["M"], "ell2": hi["ell"], "rho2": hi["rho"],
                    "gap": str(gap), "Q_times_gap": str(scaled), "gcd": g,
                }

    assert private_pairs > 0

    # Exact synthetic close-pair guard inside the private opposite-sign model.
    syn = [
        {"ell": 229, "D": 65, "M": 14885, "rho": 2062},
        {"ell": 233, "D": 65, "M": 15145, "rho": 2098},
    ]
    for r in syn:
        assert r["M"] == r["ell"] * r["D"]
        assert 2 * r["D"] < r["ell"]
        assert (r["rho"] * r["rho"] - 1) % r["ell"] == 0
        assert (r["rho"] * r["rho"] + 1) % r["D"] == 0
        assert gcd(r["rho"], r["M"]) == 1
    assert syn[1]["M"] % syn[0]["ell"] != 0
    assert syn[0]["M"] % syn[1]["ell"] != 0
    syn_num = circular_numerator(syn[0]["rho"], syn[0]["M"], syn[1]["rho"], syn[1]["M"])
    syn_gap = Fraction(syn_num, syn[0]["M"] * syn[1]["M"])
    assert syn_gap == Fraction(4, 3468205)
    assert syn_gap < Fraction(1, max(syn[0]["M"], syn[1]["M"]))

    required = [
        "STAGE14_TH18=COMPLETE_PRIVATE_CANONICAL_ROOT_MODULUS_LARGE_SIEVE_APPLICABILITY_AUDIT",
        "T67_RADIAL_COLLAPSE_REOPENED=false",
        "T67_FIXED_M_REOPENED=false",
        "T67_SAME_ELL_REOPENED=false",
        "T67_NESTED_PAIR_REOPENED=false",
        "GLOBAL_BIQUADRATIC_ROOT_ENVELOPE_PROVED=true",
        "PRIVATE_PRIME_FORCES_ONE_OVER_Q_SPACING=false",
        "GENERIC_PRIVATE_ROOT_FRACTION_LARGE_SIEVE_PROVED=true",
        "GENERIC_LARGE_SIEVE_CLOSES_PRIVATE_RECEIVER=false",
        "OPPOSITE_SIGN_CRT_RECIPROCAL_PHASE_FACTORIZATION_PROVED=true",
        "FOUVRY_IWANIEC_DIRECT_IMPORT_VALID=false",
        "DFI_NGO_DIRECT_IMPORT_VALID=false",
        "ALGEBRAIC_NUMBER_FIELD_LARGE_SIEVE_DIRECT_IMPORT_VALID=false",
        "PRIVATE_RECIPROCAL_CROSS_TWIST_OPPOSITE_SIGN_ROOT_LARGE_SIEVE_PROVED=false",
        "PRIVATE_CANONICAL_PRIME_OPPOSITE_SIGN_ROOT_MODULUS_LARGE_SIEVE_PROVED=false",
        "E4_COEFFICIENT_ENERGY_USED=false",
        "MINIMAL_REMAINING_OBSTRUCTION=PrivateReciprocalCrossTwistOppositeSignRootLargeSieve",
    ]
    for token in required:
        assert token in result, token

    dec = summary["decision"]
    assert dec["STAGE14_TH18"] == "COMPLETE_PRIVATE_CANONICAL_ROOT_MODULUS_LARGE_SIEVE_APPLICABILITY_AUDIT"
    assert dec["GENERIC_PRIVATE_ROOT_FRACTION_LARGE_SIEVE_PROVED"] is True
    assert dec["GENERIC_LARGE_SIEVE_CLOSES_PRIVATE_RECEIVER"] is False
    assert dec["PRIVATE_RECIPROCAL_CROSS_TWIST_OPPOSITE_SIGN_ROOT_LARGE_SIEVE_PROVED"] is False
    assert dec["E4_COEFFICIENT_ENERGY_USED"] is False

    report = {
        "stage": "14-tH18",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "quartic_envelope_checks": quartic_checks,
        "crt_reconstruction_checks": crt_checks,
        "private_pairs": private_pairs,
        "private_determinant_checks": determinant_checks,
        "private_prime_nondivisibility_checks": private_prime_nondiv_checks,
        "minimum_frozen_Q_scaled_private_gap": str(min_scaled_gap),
        "minimum_frozen_gap_witness": min_gap_witness,
        "synthetic_close_pair": {
            "kappa": 1,
            "H": 1,
            "left": syn[0],
            "right": syn[1],
            "gap": str(syn_gap),
            "less_than_1_over_Q": True,
        },
        "boundary_locked": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
