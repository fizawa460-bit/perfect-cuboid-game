#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

E7_PATH = Path('stages/stage14/data/14-e7/secondary_crossover_audit.json')
OUT = Path('stages/stage14/data/14-e8/euler_brick_thin_count_audit.json')
REPORT_CUTOFFS = {2000, 10000, 50000, 200000, 1000000}


def pythagorean_triple_count(B: int) -> int:
    """Number of positive unordered integer Pythagorean triples x<y, z<=B."""
    total = 0
    m = 2
    while m * m + 1 <= B:
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            h = m * m + n * n
            if h <= B:
                total += B // h
        m += 1
    return total


def max_tau_square(N: int) -> tuple[int, int]:
    """Return max_{n<=N} tau(n^2) and the first n attaining it."""
    spf = list(range(N + 1))
    if N >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(N) + 1):
        if spf[p] != p:
            continue
        for k in range(p * p, N + 1, p):
            if spf[k] == k:
                spf[k] = p

    best = 1
    arg = 1
    for n in range(2, N + 1):
        x = n
        t = 1
        while x > 1:
            p = spf[x]
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            t *= 2 * a + 1
        if t > best:
            best = t
            arg = n
    return best, arg


def loglog_fit(rows: list[dict], min_B: int) -> dict:
    pts = [(math.log(r['B']), math.log(r['euler_bricks'])) for r in rows if r['B'] >= min_B]
    xs = [x for x, _ in pts]
    ys = [y for _, y in pts]
    n = len(pts)
    xm = sum(xs) / n
    ym = sum(ys) / n
    den = sum((x - xm) ** 2 for x in xs)
    slope = sum((x - xm) * (y - ym) for x, y in pts) / den
    intercept = ym - slope * xm
    return {
        'min_B': min_B,
        'points': n,
        'effective_power_exponent': slope,
        'effective_prefactor': math.exp(intercept),
        'classification': 'finite_diagnostic_only',
    }


def main() -> None:
    e7 = json.loads(E7_PATH.read_text())
    dense = e7['dense_exact_census']

    # Frozen e7 exact census: every primitive Euler brick contributes exactly
    # three raw shared-edge incidences.
    for row in dense:
        assert row['raw_total'] - row['E2'] == 3 * row['euler_bricks']

    cutoffs = [r['B'] for r in dense]
    pyth_counts = {B: pythagorean_triple_count(B) for B in cutoffs}

    all_rows = []
    for r in dense:
        B = r['B']
        bricks = r['euler_bricks']
        raw = r['raw_total']
        incidence = 3 * bricks
        all_rows.append({
            'B': B,
            'euler_bricks': bricks,
            'third_face_square_incidences': incidence,
            'raw_ambient_incidences': raw,
            'third_face_square_incidence_fraction': incidence / raw,
            'bricks_over_sqrt_B': bricks / math.sqrt(B),
            'bricks_over_B': bricks / B,
            'pythagorean_triples_hyp_le_B': pyth_counts[B],
            'bricks_over_pythagorean_projection_pool': bricks / pyth_counts[B],
        })

    max_B = cutoffs[-1]
    tau_max, tau_arg = max_tau_square(max_B)
    finite_divisor_envelope = pyth_counts[max_B] * tau_max / 2
    fits = [loglog_fit(all_rows, b) for b in (2000, 10000, 50000, 100000, 200000)]
    rows = [r for r in all_rows if r['B'] in REPORT_CUTOFFS]

    report = {
        'metadata': {
            'stage': '14-e8',
            'height': 'D_R=sqrt(a^2+b^2+c^2)<=B',
            'population': 'primitive unordered Euler bricks',
            'max_B': max_B,
            'number_of_cutoffs': len(dense),
            'source_number_of_cutoffs': len(dense),
            'number_of_reported_cutoffs': len(rows),
        },
        'geometry': {
            'projective_model': [
                'U^2=E^2+X^2',
                'V^2=E^2+Y^2',
                'Z^2=X^2+Y^2',
            ],
            'ambient_projective_space': 'P^5',
            'complete_intersection_type': '(2,2,2)',
            'physical_positive_locus_smooth': True,
            'double_cover_branch_class': '-2K_Y',
            'minimal_resolution_type': 'K3',
            'height_comparison': 'H_max <= D_R <= sqrt(3)*H_max on physical points',
        },
        'unconditional_quantitative_envelope': {
            'projection': 'choose the two largest edges; they form an integer Pythagorean triple with hypotenuse <=B',
            'projection_pool_order': 'O(B log B)',
            'fixed_leg_completion': '(h-e)(h+e)=x^2 gives at most tau(x^2) candidates',
            'max_divisor_order': 'max_{n<=B} tau(n^2)=exp(O(log B/log log B))',
            'theorem': 'R_EB(B) << B log B * exp(O(log B/log log B)) = B^(1+o(1))',
            'epsilon_form': 'for every epsilon>0, R_EB(B)=O_epsilon(B^(1+epsilon))',
            'relative_log_saving_vs_B_log5_proved': False,
            'fixed_power_saving_B_1_minus_delta_proved': False,
            'independent_of_e4_thin_set_theorem': True,
        },
        'finite_divisor_envelope_at_max_B': {
            'B': max_B,
            'pythagorean_projection_pool': pyth_counts[max_B],
            'max_tau_n_square': tau_max,
            'first_argmax_n': tau_arg,
            'pool_times_half_max_tau': finite_divisor_envelope,
            'note': 'intentionally crude finite realization of the theorem envelope; not a prediction',
        },
        'dense_exact_census': rows,
        'finite_power_fits': fits,
        'finite_summary': {
            'B': max_B,
            'euler_bricks': all_rows[-1]['euler_bricks'],
            'bricks_over_sqrt_B': all_rows[-1]['bricks_over_sqrt_B'],
            'third_face_square_incidence_fraction': all_rows[-1]['third_face_square_incidence_fraction'],
            'global_2k_to_1m_effective_power_exponent': fits[0]['effective_power_exponent'],
            'interpretation': 'sqrt(B)-scale remains a finite candidate only; fitted exponents drift and no power-law asymptotic is claimed',
        },
        'theorem_boundary': {
            'e4_zero_density_retained': 'R_EB(B)=o(B(log B)^5)',
            'e8_independent_envelope': 'R_EB(B)=B^(1+o(1))',
            'quantitative_relative_saving_beyond_e4_proved': False,
            'sqrt_B_upper_bound_proved': False,
            'sqrt_B_asymptotic_proved': False,
            'reason': 'general rational-point counting on this K3 and uniform control of accumulating curves are not supplied by the current inputs',
        },
        'status': {
            'STAGE14_E8': 'COMPLETE_K3_AND_SUBPOWER_MULTIPLICITY_ENVELOPE',
            'EULER_BRICK_K3_MODEL_LOCKED': True,
            'EULER_BRICK_POWER_EXPONENT_UPPER_ENVELOPE': '1+o(1)',
            'QUANTITATIVE_RELATIVE_SAVING_PROVED': False,
            'SQRT_B_FINITE_CANDIDATE_ONLY': True,
            'NEXT_E_SUPPLEMENT': 'Stage14-e9 gcd/lcm and local-statistics decomposition',
        },
        'pass': True,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, sort_keys=True, separators=(',', ':')) + '\n')
    print(json.dumps(report['status'], indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
