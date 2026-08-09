#!/usr/bin/env python3
"""Stage14-4al: collective rank-jump / first-small-point audit.

This script turns the post-4ak main-track question into an exact activation
measure on primitive oriented Pythagorean first-face bases.

For a base F=(S,X,H), let mu(F) be its first physical Stage14 height d, with
mu(F)=infinity when no physical partner exists.  Then

    V(B) = #{F : mu(F) <= B}.

The ambient base population is

    A(B) = #{primitive oriented Pythagorean F : H <= B}.

Elementary Euclid-parameter counting gives A(B) ~ B/pi, so any eventual
V(B) ~ c*sqrt(B) law is equivalent to activation density
V(B)/A(B) ~ pi*c/sqrt(B).  This script does not assume that asymptotic; it
checks the exact finite activation ledger and decomposes the 490 active bases
using the Stage14-s4a arithmetic census.
"""
from __future__ import annotations

from collections import Counter
from math import gcd, log, pi, sqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
S4A = ROOT / 'stages/stage14/scripts/14-s4a/active_fingerprint_census.py'
FULL = ROOT / 'stages/stage14/data/14-s4a/active_fingerprint_census.json'
OUT = ROOT / 'stages/stage14/data/14-4/collective_first_hit_audit.json'

CUTS = (1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000)
MAX_B = max(CUTS)


def primitive_oriented_base_count(B: int) -> int:
    """Count oriented primitive Pythagorean faces with hypotenuse <= B.

    A primitive Euclid pair m>n, gcd(m,n)=1, m-n odd gives one primitive
    triangle and two oriented choices for the distinguished leg.
    """
    triples = 0
    m = 2
    while m*m + 1 <= B:
        for n in range(1, m):
            if ((m-n) & 1) == 0 or gcd(m, n) != 1:
                continue
            if m*m + n*n <= B:
                triples += 1
        m += 1
    return 2 * triples


def qtile(xs, p):
    ys = sorted(xs)
    if not ys:
        return None
    i = int(round(p * (len(ys)-1)))
    return ys[i]


def finite_profile(rows, graph_rows):
    grow = {r['B']: r for r in graph_rows}
    out = []
    for B in CUTS:
        active = [r for r in rows if r['mu'] <= B]
        A = primitive_oriented_base_count(B)
        V = len(active)
        assert V == grow[B]['active_oriented_face_vertices'], (B, V, grow[B])
        exact_rank = Counter()
        root = Counter()
        for r in active:
            rk = str(r['rank_lower']) if r['rank_lower'] == r['rank_upper'] else f"{r['rank_lower']}..{r['rank_upper']}"
            exact_rank[rk] += 1
            root[str(r['root_number'])] += 1
        ratios = [r['mu']/r['face'][2] for r in active]
        alphas = [log(r['mu'])/log(r['face'][2]) for r in active]
        hr = [r['canonical_over_log_mu'] for r in active]
        rho = V/A if A else 0.0
        out.append({
            'B': B,
            'eligible_oriented_primitive_bases_A': A,
            'A_over_B': A/B,
            'active_vertices_V': V,
            'V_over_sqrtB': V/sqrt(B),
            'activation_density_V_over_A': rho,
            'activation_density_times_sqrtB': rho*sqrt(B),
            'exact_or_interval_rank_histogram': dict(sorted(exact_rank.items())),
            'root_number_histogram': dict(sorted(root.items())),
            'mu_over_H': {
                'min': min(ratios) if ratios else None,
                'q25': qtile(ratios, .25),
                'median': qtile(ratios, .50),
                'q75': qtile(ratios, .75),
                'max': max(ratios) if ratios else None,
            },
            'log_mu_over_log_H': {
                'q25': qtile(alphas, .25),
                'median': qtile(alphas, .50),
                'q75': qtile(alphas, .75),
            },
            'canonical_height_over_log_mu': {
                'q25': qtile(hr, .25),
                'median': qtile(hr, .50),
                'q75': qtile(hr, .75),
            },
        })
    return out


def slope(y2, y1, b2=2_000_000, b1=200_000):
    return log(y2/y1) / log(b2/b1)


def main():
    # Regenerate the full exact s4a active census, including PARI rank/height data.
    s4a = runpy.run_path(str(S4A))
    s4a['main']()
    census = json.load(open(FULL))
    rows = census['rows']
    assert len(rows) == 490

    graph_mod = runpy.run_path(str(GRAPH))
    keep, _ = graph_mod['enumerate_multi'](MAX_B)
    graph_rows = [graph_mod['graph_row'](B, keep) for B in CUTS]
    profile = finite_profile(rows, graph_rows)

    p200 = next(r for r in profile if r['B'] == 200_000)
    p2m = profile[-1]
    late = [r for r in profile if r['B'] >= 200_000]
    scaled = [r['activation_density_times_sqrtB'] for r in late]
    scaled_mean = sum(scaled)/len(scaled)
    scaled_cv = (sum((x-scaled_mean)**2 for x in scaled)/len(scaled))**0.5/scaled_mean

    # Contribution growth by the two dominant exact-rank strata.
    def rank_count(pr, key):
        return pr['exact_or_interval_rank_histogram'].get(key, 0)
    rank1_200, rank1_2m = rank_count(p200, '1'), rank_count(p2m, '1')
    rank2_200, rank2_2m = rank_count(p200, '2'), rank_count(p2m, '2')

    result = {
        'metadata': {
            'stage': '14-4al',
            'max_B': MAX_B,
            'active_vertices_at_max': len(rows),
            'definition': 'mu(F)=first physical Stage14 space-diagonal height for primitive oriented Pythagorean first-face base F; infinity if no physical hit',
        },
        'exact_identity': 'V(B)=#{primitive oriented Pythagorean F : mu(F)<=B}',
        'ambient_base_asymptotic': {
            'statement': 'A(B)=B/pi+O(sqrt(B) log B) by Euclid parameters, coprimality and opposite parity',
            'consequence': 'V(B)~c*sqrt(B) iff V(B)/A(B)~pi*c/sqrt(B), whenever either asymptotic exists',
        },
        'profile': profile,
        'late_diagnostics': {
            'A_effective_exponent_200k_to_2m': slope(p2m['eligible_oriented_primitive_bases_A'], p200['eligible_oriented_primitive_bases_A']),
            'V_effective_exponent_200k_to_2m': slope(p2m['active_vertices_V'], p200['active_vertices_V']),
            'activation_density_effective_exponent_200k_to_2m': slope(p2m['activation_density_V_over_A'], p200['activation_density_V_over_A']),
            'activation_density_times_sqrtB_mean_200k_to_2m': scaled_mean,
            'activation_density_times_sqrtB_cv_200k_to_2m': scaled_cv,
            'rank1_exact_effective_exponent_200k_to_2m': slope(rank1_2m, rank1_200) if rank1_200 and rank1_2m else None,
            'rank2_exact_effective_exponent_200k_to_2m': slope(rank2_2m, rank2_200) if rank2_200 and rank2_2m else None,
            'B2m': p2m,
        },
        'cross_track_inputs': {
            's3': 'physical hit implies a non-torsion elliptic point in a logarithmic canonical-height window; positive rank alone is insufficient',
            's4a': 'all 490 active vertices have exact first-hit arithmetic fingerprints; 483/490 exact Kummer square-class triples are distinct',
            's4b': '393 coarse signatures among 490 vertices, largest cluster 4; moving bad-prime/small-point data remain dispersed',
            '4ak': 'all fixed physical M-degree-4 rational-bisection mechanisms are eliminated',
        },
        'decision': {
            'STAGE14_4AL': 'COMPLETE_COLLECTIVE_ACTIVATION_MEASURE_AND_FINITE_FIRST_HIT_PROFILE',
            'COLLECTIVE_FIRST_HIT_IDENTITY_LOCKED': True,
            'ORIENTED_PRIMITIVE_PYTHAGOREAN_BASE_ASYMPTOTIC_LINEAR': True,
            'SQRTB_EQUIVALENT_TO_INVERSE_SQRT_ACTIVATION_DENSITY': True,
            'FIXED_CURVE_MECHANISM_REOPENED': False,
            'POSITIVE_RANK_DENSITY_PROVED': False,
            'UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED': False,
            'ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED': False,
            'TRUE_GROWTH_ORDER_IDENTIFIED': False,
            'NEXT': 'Stage14-4am isolate a uniform arithmetic lower-tail statement for mu(F), separating positive-rank frequency from first-small-point frequency',
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['late_diagnostics'], indent=2))
    print(json.dumps(result['decision'], indent=2))


if __name__ == '__main__':
    main()
