#!/usr/bin/env python3
"""Stage14-t21: partition-resolved direction/scale counting reduction audit."""

from collections import Counter
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t21/direction_scale_reduction.json'
MAX_B = 2_000_000
CUTS = (1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000)
EXPECTED = {1000:2,2000:5,5000:15,10000:25,20000:42,50000:62,100000:89,200000:116,500000:188,1000000:255,2000000:356}


def squarefree_core(n):
    assert n > 0
    out = 1
    e = 0
    while n % 2 == 0:
        n //= 2
        e ^= 1
    if e:
        out *= 2
    p = 3
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 2
    if n > 1:
        out *= n
    return out


def prime_support(n):
    assert n > 0
    out = []
    if n % 2 == 0:
        out.append(2)
        while n % 2 == 0:
            n //= 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        out.append(n)
    return out


def tau_square(n):
    """tau(n^2) from the factorization of n."""
    assert n > 0
    ans = 1
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    if e:
        ans *= 2 * e + 1
    p = 3
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            ans *= 2 * e + 1
        p += 2
    if n > 1:
        ans *= 3
    return ans


def exact_sqrt(n):
    r = isqrt(n)
    assert r * r == n
    return r


def direction_data(d, s):
    g = gcd(d, s)
    D, C = d // g, s // g
    assert gcd(D, C) == 1
    h = gcd(D - C, D + C)
    assert h in (1, 2)
    A = (D - C) // h
    B = (D + C) // h
    assert A > 0 and B > A and gcd(A, B) == 1
    alpha = squarefree_core(A)
    beta = squarefree_core(B)
    r = exact_sqrt(A // alpha)
    u = exact_sqrt(B // beta)
    a = alpha * r * r
    b = beta * u * u
    assert a == A and b == B and gcd(a, b) == 1
    expected_h = 1 if (a % 2 == 1 and b % 2 == 1) else 2
    assert h == expected_h
    assert D == h * (a + b) // 2
    assert C == h * (b - a) // 2
    assert gcd(D, C) == 1
    assert D * D - C * C == h * h * alpha * beta * r * r * u * u
    return {
        'g': g, 'D': D, 'C': C, 'h': h,
        'alpha': alpha, 'beta': beta, 'r': r, 'u': u,
    }


def edge_records(a, b, c, d, mask):
    sides = (a, b, c)
    face_values = (a*a+b*b, a*a+c*c, b*b+c*c)
    specs = ((0,1,0,2), (0,2,1,1), (1,2,2,0))
    out = []
    for i, j, shared_idx, missing_idx in specs:
        if not ((mask & (1 << i)) and (mask & (1 << j))):
            continue
        s = sides[shared_idx]
        others = [sides[k] for k in range(3) if k != shared_idx]
        x, y = others
        assert x*x + y*y == face_values[missing_idx]
        assert d*d - s*s == x*x + y*y
        assert gcd(s, gcd(x, y)) == 1

        z = direction_data(d, s)
        g = z['g']

        # New t21 primitive scale restriction.
        assert g % 2 == 1
        assert all(p % 4 == 1 for p in prime_support(g))

        # The actual two integral faces are among the divisor-pair completions
        # of H^2-X^2=s^2.  tau(s^2)^2 is therefore a uniform soft envelope
        # for the ordered pair of face completions at fixed (d,s).
        hx = isqrt(s*s + x*x)
        hy = isqrt(s*s + y*y)
        assert hx*hx == s*s + x*x
        assert hy*hy == s*s + y*y
        t2 = tau_square(s)
        assert t2 >= 1

        out.append({
            'd': d,
            's': s,
            'g': g,
            'D': z['D'],
            'C': z['C'],
            'h': z['h'],
            'alpha': z['alpha'],
            'beta': z['beta'],
            'r': z['r'],
            'u': z['u'],
            'tau_s_squared': t2,
            'is_triple_edge': mask.bit_count() == 3,
        })
    return out


def synthetic_round_trip():
    """Check the converse direction map on small admissible tuples."""
    checked = 0
    squarefree = [1, 2, 5, 10, 13, 17, 26, 29, 37, 41, 53, 58, 65]
    for alpha in squarefree:
        if squarefree_core(alpha) != alpha:
            continue
        for beta in squarefree:
            if squarefree_core(beta) != beta or gcd(alpha, beta) != 1:
                continue
            for r in range(1, 7):
                for u in range(1, 7):
                    a = alpha * r * r
                    b = beta * u * u
                    if b <= a or gcd(a, b) != 1:
                        continue
                    h = 1 if (a % 2 and b % 2) else 2
                    D = h * (a + b) // 2
                    C = h * (b - a) // 2
                    assert D > C > 0 and gcd(D, C) == 1
                    assert gcd(D-C, D+C) == h
                    z = direction_data(D, C)
                    assert (z['alpha'],z['beta'],z['r'],z['u'],z['h']) == (alpha,beta,r,u,h)
                    checked += 1
    assert checked > 100
    return checked


def main():
    mod = runpy.run_path(str(GRAPH))
    keep, _ = mod['enumerate_multi'](MAX_B)

    records = []
    for (a,b,c,d),(mask,ds) in keep.items():
        records.extend(edge_records(a,b,c,d,mask))
    records.sort(key=lambda r:(r['d'],r['s'],r['D'],r['C']))
    assert len(records) == 356
    assert sum(r['is_triple_edge'] for r in records) == 0

    round_trip_checks = synthetic_round_trip()

    rows = []
    for B in CUTS:
        z = [r for r in records if r['d'] <= B]
        assert len(z) == EXPECTED[B]
        dirs = Counter((r['D'],r['C']) for r in z)
        parts = Counter((r['alpha'],r['beta']) for r in z)
        kappas = Counter(r['alpha'] * r['beta'] for r in z)
        assert max(dirs.values(), default=0) == 1
        assert max(parts.values(), default=0) == 1
        assert max(kappas.values(), default=0) == 1
        rows.append({
            'B': B,
            'raw_pair_edges': len(z),
            'h_1_edges': sum(r['h'] == 1 for r in z),
            'h_2_edges': sum(r['h'] == 2 for r in z),
            'g_1_edges': sum(r['g'] == 1 for r in z),
            'nontrivial_g_edges': sum(r['g'] > 1 for r in z),
            'distinct_reduced_directions': len(dirs),
            'distinct_split_partitions': len(parts),
            'max_g': max((r['g'] for r in z), default=0),
            'max_tau_s_squared': max((r['tau_s_squared'] for r in z), default=0),
        })

    g_hist = Counter(r['g'] for r in records)
    final = rows[-1]
    report = {
        'stage': '14-t21',
        'direction_parametrization': {
            'formula': 'a=alpha*r^2, b=beta*u^2, h=1 iff a,b odd else 2; D=h(a+b)/2, C=h(b-a)/2',
            'coprime_condition': 'gcd(a,b)=1 and b>a',
            'bijection_checked_on_all_frozen_edges': True,
            'synthetic_round_trip_checks': round_trip_checks,
        },
        'scale_restriction': {
            'statement': 'for a primitive raw edge, every prime divisor of g=gcd(d,s) is 1 mod 4; in particular g is odd',
            'observed_g_histogram_B2m': {str(k): g_hist[k] for k in sorted(g_hist)},
        },
        'fiber_majorant': {
            'fixed_direction_scale_face_bound': '#ordered face completions <= tau(s^2)^2 = B^o(1)',
            'direction_scale_sum': 'N_{alpha,beta}(B) <= B^o(1) sum_{r,u admissible} floor(B/D_{alpha,beta}(r,u))',
            'coarse_bound': 'N_{alpha,beta}(B) << B^(1+o(1))/sqrt(alpha*beta)',
            'coarse_bound_closes_Q_split': False,
        },
        'finite': {
            'max_B': MAX_B,
            'raw_pair_edges_B2m': final['raw_pair_edges'],
            'h_1_edges_B2m': final['h_1_edges'],
            'h_2_edges_B2m': final['h_2_edges'],
            'g_1_edges_B2m': final['g_1_edges'],
            'nontrivial_g_edges_B2m': final['nontrivial_g_edges'],
            'observed_g_values_B2m': sorted(g_hist),
            'max_g_B2m': final['max_g'],
            'max_r_B2m': max(r['r'] for r in records),
            'max_u_B2m': max(r['u'] for r in records),
            'distinct_reduced_directions_B2m': final['distinct_reduced_directions'],
            'distinct_split_partitions_B2m': final['distinct_split_partitions'],
            'max_tau_s_squared_B2m': final['max_tau_s_squared'],
        },
        'rows': rows,
        'decision': {
            'STAGE14_T21': 'COMPLETE_PARTITION_DIRECTION_SCALE_REDUCTION',
            'FIXED_PARTITION_DIRECTION_PARAMETRIZATION_BIJECTIVE': True,
            'H_PARITY_RULE_EXACT': True,
            'SCALE_PRIME_SUPPORT_ONLY_1MOD4': True,
            'FIXED_DIRECTION_SCALE_FACE_MULTIPLICITY': 'B^o(1)',
            'N_ALPHA_BETA_DIRECTION_SCALE_MAJORANT': True,
            'N_ALPHA_BETA_COARSE_BOUND': 'B^(1+o(1))/sqrt(alpha*beta)',
            'COARSE_BOUND_SUFFICIENT_FOR_Q_SPLIT_POWER_SAVING': False,
            'SIMULTANEOUS_FACE_COMPLETION_CORRELATION_REQUIRED': True,
            'Q_SPLIT_POWER_SAVING_PROVED': False,
            'Q_EDGE_O_B_PROVED': False,
            'T_O_SQRT_B_PROVED': False,
            'PERFECT_CUBOID_NONEXISTENCE_PROVED': False,
            'NEXT': 'Stage14-t22 analyze simultaneous face-completion counts M_{D,C}(G) / extract a power-saving average over generalized-Pell directions',
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report['finite'], indent=2))
    print(json.dumps(report['decision'], indent=2))


if __name__ == '__main__':
    main()
