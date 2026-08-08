#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

OUT = Path('stages/stage14/data/14-e7/secondary_crossover_audit.json')
CUTOFFS = [
    2000, 3000, 5000, 7500, 10000, 15000, 20000, 30000,
    50000, 75000, 100000, 150000, 200000, 300000, 500000,
    750000, 1000000,
]

# Stage14-e6 rigorous interval for the proved leading coefficient C_E.
C5_LO = 1.47953102009666e-6
C5_HI = 1.47956061101297e-6
C5 = 0.5 * (C5_LO + C5_HI)

LOCKED_E2 = {
    2000: 4812,
    10000: 41666,
    50000: 331731,
    200000: 1896505,
    1000000: 13817725,
}


def is_square(n: int) -> bool:
    r = math.isqrt(n)
    return r * r == n


def pythagorean_neighbors(hyp_limit: int):
    nbr = defaultdict(set)
    m = 2
    while m * m + 1 <= hyp_limit:
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a, b, h = m * m - n * n, 2 * m * n, m * m + n * n
            if h > hyp_limit:
                continue
            for k in range(1, hyp_limit // h + 1):
                A, C = k * a, k * b
                nbr[A].add(C)
                nbr[C].add(A)
        m += 1
    return nbr


def census(B: int):
    nbr = pythagorean_neighbors(B)
    B2 = B * B
    raw_total = 0
    exact_total = 0
    bricks = set()
    for e, others in nbr.items():
        vals = sorted(others)
        for i, x in enumerate(vals):
            ex = e * e + x * x
            if ex >= B2:
                continue
            ymax = math.isqrt(B2 - ex)
            for y in vals[i + 1:]:
                if y > ymax:
                    break
                if math.gcd(math.gcd(e, x), y) != 1:
                    continue
                raw_total += 1
                if is_square(x * x + y * y):
                    bricks.add(tuple(sorted((e, x, y))))
                else:
                    exact_total += 1
    assert raw_total - exact_total == 3 * len(bricks)
    return raw_total, exact_total, len(bricks)


def fit_c4_c3(rows, min_B: int):
    # Fit R3(B)-c5*L^2 = c4*L+c3 by ordinary least squares.
    pts = [r for r in rows if r['B'] >= min_B]
    xs = [r['logB'] for r in pts]
    ys = [r['R3'] - C5 * r['logB'] ** 2 for r in pts]
    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    den = n * sxx - sx * sx
    c4 = (n * sxy - sx * sy) / den
    c3 = (sy - c4 * sx) / n
    rel = []
    for r in pts:
        L = r['logB']
        pred = C5 * L * L + c4 * L + c3
        rel.append((pred - r['R3']) / r['R3'])
    disc = c4 * c4 + 4.0 * C5 * c3
    L_cross = (-c4 + math.sqrt(disc)) / (2.0 * C5)
    return {
        'min_B': min_B,
        'points': n,
        'effective_c4': c4,
        'effective_c3': c3,
        'rms_relative_error': math.sqrt(sum(x*x for x in rel) / n),
        'max_abs_relative_error': max(abs(x) for x in rel),
        'diagnostic_balance_logB': L_cross,
        'diagnostic_balance_log10B': L_cross / math.log(10.0),
    }


def main():
    rows = []
    for B in CUTOFFS:
        raw, exact, bricks = census(B)
        if B in LOCKED_E2:
            assert exact == LOCKED_E2[B]
        L = math.log(B)
        lead_lo = C5_LO * B * L**5
        lead_hi = C5_HI * B * L**5
        rows.append({
            'B': B,
            'E2': exact,
            'raw_total': raw,
            'euler_bricks': bricks,
            'logB': L,
            'R3': exact / (B * L**3),
            'R5': exact / (B * L**5),
            'proved_log5_main_share_lower': lead_lo / exact,
            'proved_log5_main_share_upper': lead_hi / exact,
        })

    fits = [fit_c4_c3(rows, m) for m in (2000, 20000, 100000, 200000)]
    final = rows[-1]

    # The finite effective coefficients drift materially as the window moves.
    c4s = [f['effective_c4'] for f in fits]
    c3s = [f['effective_c3'] for f in fits]
    c4_drift = max(c4s) - min(c4s)
    c3_drift = max(c3s) - min(c3s)

    report = {
        'metadata': {
            'stage': '14-e7',
            'track': 'secondary asymptotic boundary and finite crossover',
            'height': 'physical Euclidean D_R',
            'max_B': CUTOFFS[-1],
            'number_of_cutoffs': len(CUTOFFS),
        },
        'theorem_input': {
            'c5_lower': C5_LO,
            'c5_upper': C5_HI,
            'c5_midpoint_used_only_for_finite_regression': C5,
            'pole_order': 6,
            'formal_polynomial_degree': 5,
        },
        'dense_exact_census': rows,
        'anchored_three_term_diagnostics': fits,
        'finite_crossover_summary': {
            'R3_at_1e6': final['R3'],
            'proved_c5_log2_contribution_to_R3_at_1e6': C5 * final['logB']**2,
            'proved_log5_main_share_at_1e6_lower': final['proved_log5_main_share_lower'],
            'proved_log5_main_share_at_1e6_upper': final['proved_log5_main_share_upper'],
            'remaining_fraction_at_1e6_lower': 1.0 - final['proved_log5_main_share_upper'],
            'remaining_fraction_at_1e6_upper': 1.0 - final['proved_log5_main_share_lower'],
            'effective_c4_window_drift': c4_drift,
            'effective_c3_window_drift': c3_drift,
            'interpretation': 'The proved log^5 leading term is only about 5.39% of the exact count at B=10^6; the finite range is dominated by lower-order/pre-asymptotic mass. Fitted c4,c3 drift with the window and are not theorem coefficients.',
        },
        'analytic_boundary': {
            'batyrev_tschinkel_sixfold_pole_and_leading_term': True,
            'formal_laurent_to_polynomial_dictionary_recorded': True,
            'physical_metric_left_half_plane_continuation_verified': False,
            'physical_metric_vertical_growth_verified': False,
            'full_secondary_polynomial_proved': False,
            'finite_effective_coefficients_are_laurent_coefficients': False,
        },
        'status': {
            'STAGE14_E7': 'COMPLETE_FINITE_CROSSOVER_AND_SECONDARY_BOUNDARY',
            'FINITE_CROSSOVER_DIAGNOSIS_COMPLETE': True,
            'FULL_SECONDARY_ASYMPTOTIC_PROVED': False,
            'E6_LEADING_CONSTANT_UNCHANGED': True,
            'NEXT_E_SUPPLEMENT': 'Stage14-e8 quantitative Euler-brick thin-set count',
        },
        'pass': True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(report['status'], indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
