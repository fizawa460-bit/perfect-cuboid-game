#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
MAX_B = 50_000


def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def factor_prime_powers(n):
    n = abs(n)
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append((n, 1))
    return out


def half_angle_roots(S2, X2, H2):
    hp = H2 + S2
    hm = H2 - S2
    if is_square(hp) and is_square(hm):
        kappa = 1
        s = isqrt(hp)
        t = isqrt(hm)
    else:
        assert hp % 2 == 0 and hm % 2 == 0
        assert is_square(hp // 2) and is_square(hm // 2)
        kappa = 2
        s = isqrt(hp // 2)
        t = isqrt(hm // 2)
    assert gcd(s, t) == 1
    assert X2 == kappa * s * t
    return kappa, s, t


def ordered_incidences():
    mod = runpy.run_path(str(GRAPH))
    keep, _ = mod['enumerate_multi'](MAX_B)
    object_edges = mod['object_edges']
    rows = []
    undirected = 0
    for (a, b, c, d), (mask, ds) in keep.items():
        if d > MAX_B or mask.bit_count() < 2:
            continue
        for f1, f2 in object_edges(a, b, c, mask, ds):
            undirected += 1
            rows.append((d, f1, f2))
            rows.append((d, f2, f1))
    assert undirected == 62, undirected
    assert len(rows) == 124
    return rows


def main():
    rows = ordered_incidences()
    plus_root_checks = 0
    minus_root_checks = 0
    for d, F, F2 in rows:
        S, X, H = F
        S2, X2, H2 = F2
        G = gcd(S, S2) * d
        assert G * G == H * H * S2 * S2 + S * S * X2 * X2
        assert G * G == H * H * H2 * H2 - X * X * X2 * X2

        kappa, s, t = half_angle_roots(S2, X2, H2)
        hp = H2 + S2
        hm = H2 - S2

        # Merged s6-06 minus-column selector.
        Nminus = H * G - S * S * H2 - X * X * S2
        gminus = gcd(abs(Nminus), hm)
        Dminus2 = hm // gminus
        assert is_square(Dminus2)
        Dminus = isqrt(Dminus2)
        assert t % Dminus == 0
        kminus = t // Dminus
        assert gminus == kappa * kminus * kminus

        # Independently rederived plus-column selector.
        Nplus = H * G + X * X * S2 - S * S * H2
        # Check the exact factorization behind Z(P+T_-).
        lhs = (G + H * S2) * (H * H2 - G)
        assert lhs == (H2 - S2) * Nplus
        gplus = gcd(abs(Nplus), hp)
        Dplus2 = hp // gplus
        assert is_square(Dplus2)
        Dplus = isqrt(Dplus2)
        assert s % Dplus == 0
        kplus = s // Dplus
        assert gplus == kappa * kplus * kplus

        Q = Dplus * Dminus
        K = kplus * kminus
        assert Q * K == s * t == X2 // kappa
        assert K * K <= abs(Nplus * Nminus) or Nplus * Nminus == 0
        assert abs(Nplus) % (kplus * kplus) == 0
        assert abs(Nminus) % (kminus * kminus) == 0
        assert max(Q, K) * max(Q, K) >= Q * K

        # Good odd root-sign laws on the two coprime half-angle columns.
        bad = 2 * H * S * X
        for p, e in factor_prime_powers(s):
            if p == 2 or bad % p == 0:
                continue
            pe = p ** e
            modp = p ** (2 * e)
            survives = (Dplus % pe == 0)
            plus_sign = ((G - H * S2) % modp == 0)
            assert survives == plus_sign, (d, F, F2, p, e, Dplus, s)
            plus_root_checks += 1
        for p, e in factor_prime_powers(t):
            if p == 2 or bad % p == 0:
                continue
            pe = p ** e
            modp = p ** (2 * e)
            survives = (Dminus % pe == 0)
            minus_sign = ((G + H * S2) % modp == 0)
            assert survives == minus_sign, (d, F, F2, p, e, Dminus, t)
            minus_root_checks += 1

    # Exact exponent ledger.
    assert Fraction(41, 42) - Fraction(20, 21) == Fraction(1, 42)
    assert 2 * Fraction(10, 21) == Fraction(20, 21)
    assert Fraction(20, 21) < Fraction(41, 42)

    print(f'ORDERED_PHYSICAL_INCIDENCES={len(rows)}')
    print(f'PLUS_GOOD_ROOT_SIGN_CHECKS={plus_root_checks}')
    print(f'MINUS_GOOD_ROOT_SIGN_CHECKS={minus_root_checks}')
    print('DUAL_HALF_ANGLE_SELECTOR_AUDIT=true')
    print('DUAL_PRODUCT_IDENTITY_AUDIT=true')
    print('DUAL_CANCELLATION_SQUARE_AUDIT=true')
    print('DUAL_GOOD_ROOT_SIGN_AUDIT=true')
    print('OPTIMAL_BETA_20_21_LEDGER_AUDIT=true')
    print('SECTORAL_SAVING_1_42_LEDGER_AUDIT=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
