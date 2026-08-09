#!/usr/bin/env python3
"""Stage14-t20: raw-edge collision correction and coprime factor-kernel audit."""

from collections import Counter
from math import gcd
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t20/edge_collision_factorization.json'
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


def edge_records(a, b, c, d, mask):
    """Return one record for each unordered pair of integral faces.

    Face indices: 0=ab, 1=ac, 2=bc.
    Pair (0,1) shares a and misses bc; (0,2) shares b and misses ac;
    pair (1,2) shares c and misses ab.
    """
    sides = (a, b, c)
    face_values = (a*a+b*b, a*a+c*c, b*b+c*c)
    specs = ((0,1,0,2), (0,2,1,1), (1,2,2,0))
    out = []
    for i, j, shared_idx, missing_idx in specs:
        if not ((mask & (1 << i)) and (mask & (1 << j))):
            continue
        s = sides[shared_idx]
        missing_value = face_values[missing_idx]
        assert missing_value == d*d - s*s

        g = gcd(d, s)
        D, C = d // g, s // g
        assert gcd(D, C) == 1
        h = gcd(D - C, D + C)
        assert h in (1, 2)
        A = (D - C) // h
        B = (D + C) // h
        assert A > 0 and B > 0 and gcd(A, B) == 1
        assert missing_value == g*g*h*h*A*B

        alpha = squarefree_core(A)
        beta = squarefree_core(B)
        kappa = squarefree_core(missing_value)
        assert gcd(alpha, beta) == 1
        assert alpha * beta == kappa
        assert squarefree_core(A * B) == kappa

        # The missing face is a primitive sum of two squares after removing
        # the gcd of its two side lengths.  Its squarefree kernel therefore
        # has no prime 3 mod 4.
        if missing_idx == 0:
            u, v = a, b
        elif missing_idx == 1:
            u, v = a, c
        else:
            u, v = b, c
        g0 = gcd(u, v)
        U, V = u // g0, v // g0
        assert gcd(U, V) == 1
        assert squarefree_core(U*U + V*V) == kappa
        assert all(p == 2 or p % 4 == 1 for p in prime_support(kappa))

        out.append({
            'd': d,
            'shared_side': s,
            'kappa': kappa,
            'alpha': alpha,
            'beta': beta,
            'is_triple_edge': mask.bit_count() == 3,
        })
    return out


def main():
    mod = runpy.run_path(str(GRAPH))
    keep, _ = mod['enumerate_multi'](MAX_B)

    records = []
    triple_objects = 0
    for (a,b,c,d),(mask,ds) in keep.items():
        if mask.bit_count() == 3:
            triple_objects += 1
        recs = edge_records(a,b,c,d,mask)
        assert len(recs) == (3 if mask.bit_count() == 3 else 1)
        for r in recs:
            if r['is_triple_edge']:
                assert r['kappa'] == 1
            else:
                assert r['kappa'] != 1
        records.extend(recs)

    records.sort(key=lambda r:(r['d'],r['shared_side'],r['kappa'],r['alpha'],r['beta']))
    assert len(records) == 356
    assert triple_objects == 0

    rows = []
    for B in CUTS:
        z = [r for r in records if r['d'] <= B]
        cnt = Counter(r['kappa'] for r in z)
        split = Counter((r['alpha'], r['beta']) for r in z)
        Q_edge = sum(v*v for v in cnt.values())
        Q_split = sum(v*v for v in split.values())
        trivial_edges = cnt.get(1, 0)
        triple_edges = sum(r['is_triple_edge'] for r in z)
        assert len(z) == EXPECTED[B]
        assert trivial_edges == triple_edges
        assert triple_edges % 3 == 0
        assert len(cnt) == len(z)
        assert len(split) == len(z)
        assert Q_edge == len(z)
        assert Q_split == len(z)
        rows.append({
            'B': B,
            'raw_pair_edges': len(z),
            'triple_objects': triple_edges // 3,
            'trivial_class_edges': trivial_edges,
            'distinct_squareclasses': len(cnt),
            'collision_Q_edge': Q_edge,
            'distinct_split_partitions': len(split),
            'collision_Q_split': Q_split,
        })

    report = {
        'stage': '14-t20',
        'corrected_population': {
            'population': 'raw-pair edges: one edge per exactly-two object and three edges per triple object',
            'edge_identity': 'E(B)=N2(B)+3T(B)',
            'trivial_class_identity': 'n_1(B)=3T(B)',
            'collision_inequality': '9*T(B)^2 <= Q_edge(B)',
            'sufficient_target': 'Q_edge(B)=o(B) implies T(B)=o(sqrt(B))',
            't19_exactly_two_asymptotic_statement_superseded': True,
        },
        'factorization': {
            'definitions': 'g=gcd(d,s), D=d/g, C=s/g, h=gcd(D-C,D+C), A=(D-C)/h, B=(D+C)/h',
            'h_values': [1, 2],
            'coprime_AB': True,
            'missing_face_formula': 'm=g^2*h^2*A*B',
            'kernel_partition': 'A=alpha*r^2, B=beta*u^2, gcd(alpha,beta)=1, kappa=alpha*beta',
            'kernel_prime_support': 'only 2 and primes 1 mod 4',
            'partition_bound': 'n_k^2 <= 2^omega(k) * sum_{alpha*beta=k} N_{alpha,beta}^2',
            'global_reduction': 'Q_edge(B) <= B^o(1) Q_split(B)',
        },
        'finite': {
            'max_B': MAX_B,
            'raw_pair_edges_B2m': rows[-1]['raw_pair_edges'],
            'triple_objects_B2m': rows[-1]['triple_objects'],
            'trivial_class_edges_B2m': rows[-1]['trivial_class_edges'],
            'collision_Q_edge_B2m': rows[-1]['collision_Q_edge'],
            'collision_Q_split_B2m': rows[-1]['collision_Q_split'],
        },
        'rows': rows,
        'decision': {
            'STAGE14_T20': 'COMPLETE_RAW_EDGE_COLLISION_CORRECTION_AND_COPRIME_FACTOR_REDUCTION',
            'ASYMPTOTIC_COLLISION_POPULATION': 'RAW_PAIR_EDGES',
            'RAW_EDGE_IDENTITY': 'E(B)=N2(B)+3T(B)',
            'TRIVIAL_CLASS_EDGE_COUNT': '3T(B)',
            'NINE_T_SQUARED_LE_Q_EDGE': True,
            'Q_EDGE_O_B_SUFFICIENT_FOR_T_O_SQRT_B': True,
            'T19_EXACTLY_TWO_COLLISION_ASYMPTOTIC_STATEMENT_SUPERSEDED': True,
            'MISSING_FACE_CLASS_EQUALS_DIFFERENCE_OF_SQUARES_KERNEL': True,
            'COPRIME_FACTORIZATION_M_EQUALS_G2_H2_A_B': True,
            'H_IN_1_2': True,
            'KERNEL_EQUALS_ALPHA_BETA': True,
            'KERNEL_PRIME_SUPPORT_ONLY_2_OR_1MOD4': True,
            'PARTITION_RESOLVED_COLLISION_REDUCTION': True,
            'Q_EDGE_LE_B_O1_Q_SPLIT': True,
            'FINITE_Q_EDGE_EQUALS_Q_SPLIT_EQUALS_356_AT_B2M': True,
            'Q_SPLIT_POWER_SAVING_PROVED': False,
            'Q_EDGE_O_B_PROVED': False,
            'T_O_SQRT_B_PROVED': False,
            'PERFECT_CUBOID_NONEXISTENCE_PROVED': False,
            'NEXT': 'Stage14-t21 attack partition-resolved collision energy Q_split(B) using the raw-pair Pythagorean parametrization',
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report['finite'], indent=2))
    print(json.dumps(report['decision'], indent=2))


if __name__ == '__main__':
    main()
