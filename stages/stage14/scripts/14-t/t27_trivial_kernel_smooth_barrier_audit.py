#!/usr/bin/env python3
"""Stage14-t27: trivial-kernel target compression / ambient friability diagnostics."""

from array import array
from bisect import bisect_right
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
T21 = ROOT / 'stages/stage14/scripts/14-t/t21_direction_scale_reduction_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t27/trivial_kernel_smooth_barrier.json'
MAX_B = 2_000_000
CUTS = (1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000)
ETAS = ((1,10), (1,8), (1,6), (1,5), (1,4), (3,10))


def largest_prime_factor_table(n):
    """Return largest-prime-factor table as a compact unsigned-int array."""
    lpf = array('I', [0]) * (n + 1)
    for p in range(2, n + 1):
        if lpf[p] != 0:
            continue
        for m in range(p, n + 1, p):
            lpf[m] = p
    return lpf


def largest_odd_prime_factor(n, lpf):
    if n <= 1:
        return 1
    p = int(lpf[n])
    return 1 if p <= 2 else p


def eta_key(frac):
    a,b = frac
    return f'{a}/{b}'


def is_smooth_at(pmax, B, frac):
    a,b = frac
    # pmax <= B^(a/b), avoiding floating-point threshold errors.
    return pow(pmax, b) <= pow(B, a)


def actual_trivial_kernel_edges():
    """Regenerate actual raw-pair edges and extract alpha=beta=1 edges."""
    t21 = runpy.run_path(str(T21))
    direction_data = t21['direction_data']
    graph = runpy.run_path(str(GRAPH))
    keep, _ = graph['enumerate_multi'](MAX_B)

    edge_ds = []
    total_edges = 0
    triple_objects = 0
    sidespec = ((0,1,0), (0,2,1), (1,2,2))
    for (a,b,c,d), (mask, ds) in keep.items():
        sides = (a,b,c)
        if mask.bit_count() == 3:
            triple_objects += 1
        for i,j,shared_idx in sidespec:
            if not ((mask & (1 << i)) and (mask & (1 << j))):
                continue
            total_edges += 1
            s = sides[shared_idx]
            z = direction_data(d, s)
            if z['alpha'] == 1 and z['beta'] == 1:
                # kappa=alpha*beta=1, so this must be a triple edge.
                assert mask.bit_count() == 3
                edge_ds.append(d)

    edge_ds.sort()
    assert total_edges == 356
    assert triple_objects == 0
    assert edge_ds == []
    return {
        'raw_pair_edges_B2m': total_edges,
        'triple_objects_B2m': triple_objects,
        'alpha_beta_1_1_edges_B2m': len(edge_ds),
        'alpha_beta_1_1_edge_diagonals': edge_ds,
    }


def enumerate_candidate_directions(lpf):
    """Enumerate all primitive alpha=beta=1 reduced directions D<=MAX_B.

    For coprime u>r>0, h=1 for both odd and h=2 otherwise,
      D=h(r^2+u^2)/2, C=h(u^2-r^2)/2,
    and D^2-C^2=(hru)^2.
    """
    rows = []
    umax = isqrt(2 * MAX_B) + 2
    for u in range(2, umax + 1):
        uu = u*u
        for r in range(1, u):
            if gcd(r,u) != 1:
                continue
            h = 1 if (r & 1 and u & 1) else 2
            total = h * (r*r + uu)
            assert total % 2 == 0
            D = total // 2
            if D > MAX_B:
                continue
            diff = h * (uu - r*r)
            assert diff % 2 == 0
            C = diff // 2
            L = h*r*u
            assert gcd(D,C) == 1
            assert D*D - C*C == L*L
            assert D - C == h*r*r
            assert D + C == h*u*u

            pmax = max(
                largest_odd_prime_factor(r, lpf),
                largest_odd_prime_factor(u, lpf),
                largest_odd_prime_factor(C, lpf),
                largest_odd_prime_factor(D, lpf),
            )
            rows.append((D, pmax, r, u, C, h))

    rows.sort(key=lambda z: (z[0],z[2],z[3]))
    # Parametrization is injective in the ordered positive coprime pair (r,u).
    assert len({(z[0],z[4]) for z in rows}) == len(rows)
    return rows


def aggregate_range(candidates, lo, hi, B):
    n = max(0, hi-lo)
    out = {'candidate_directions': n}
    for frac in ETAS:
        sm = 0
        for idx in range(lo, hi):
            if is_smooth_at(candidates[idx][1], B, frac):
                sm += 1
        key = eta_key(frac)
        out[f'smooth_eta_{key}'] = sm
        out[f'large_eta_{key}'] = n-sm
    if n:
        pvals = sorted(candidates[idx][1] for idx in range(lo,hi))
        out['median_largest_odd_prime'] = pvals[n//2]
        out['max_largest_odd_prime'] = pvals[-1]
    else:
        out['median_largest_odd_prime'] = 1
        out['max_largest_odd_prime'] = 1
    return out


def main():
    actual = actual_trivial_kernel_edges()
    lpf = largest_prime_factor_table(MAX_B)
    candidates = enumerate_candidate_directions(lpf)
    Ds = [z[0] for z in candidates]

    rows = []
    for B in CUTS:
        hi = bisect_right(Ds, B)
        shell_lo = bisect_right(Ds, B//2)
        all_stats = aggregate_range(candidates, 0, hi, B)
        shell_stats = aggregate_range(candidates, shell_lo, hi, B)
        rows.append({
            'B': B,
            'actual_alpha_beta_1_1_edges': 0,
            'all_D_le_B': all_stats,
            'top_dyadic_shell_B_over_2_lt_D_le_B': shell_stats,
        })

    final = rows[-1]
    report = {
        'stage': '14-t27',
        'target_compression': {
            'trivial_kernel_partition': '(alpha,beta)=(1,1) only',
            'exact_edge_identity': 'N_{1,1}(B)=n_1(B)=3T(B)',
            'danger_direction': 'D=h(r^2+u^2)/2, C=h(u^2-r^2)/2, L=hru, C^2+L^2=D^2',
            'fixed_direction_transfer': 'N_{1,1}(B)<=B^o(1) A_{1,1}(B) by t22',
            'primary_sufficient_target': 'A_{1,1}(B)=O(B^(1/2-delta)) for some fixed delta>0',
            'full_rank_second_moment_required_for_primary_T_target': False,
        },
        'dyadic_split': {
            'largest_prime_statistic': 'P_*=largest odd prime dividing r*u*C*D',
            'large_branch': 'P_*>X^eta on X<D<=2X; canonical largest prime is routed by t26',
            'smooth_branch': 'P_*<=X^eta and the physical cover equation must still be imposed',
            'etas_audited': [eta_key(z) for z in ETAS],
            'large_branch_power_saving_proved': False,
            'joint_cover_conditioned_smooth_power_saving_proved': False,
        },
        'literature_boundary': {
            'Le_Boudec_2018': 'large-prime subset has positive proportion and supports complete 2-descent; it is not an exhaustion theorem for the complement',
            'BBDT_2012': 'degree-2 binary forms have order-R^2 many R^epsilon-friable values in the ambient box; one quadratic column cannot supply a power-saving large-prime exception bound by itself',
            'joint_four_column_active_friability_conclusion': 'not supplied by those results; physical-cover-conditioned counting remains necessary',
        },
        'finite_actual': actual,
        'finite_candidate_universe': {
            'max_B': MAX_B,
            'candidate_directions_D_le_B2m': final['all_D_le_B']['candidate_directions'],
            'candidate_directions_top_shell_B2m': final['top_dyadic_shell_B_over_2_lt_D_le_B']['candidate_directions'],
            'actual_active_alpha_beta_1_1_edges_B2m': 0,
        },
        'rows': rows,
        'decision': {
            'STAGE14_T27': 'COMPLETE_TRIVIAL_KERNEL_TARGET_COMPRESSION_AND_COVER_CONDITIONED_FRIABILITY_SPLIT',
            'TRIVIAL_KERNEL_PARTITION_ONLY_1_1': True,
            'N_11_EQUALS_3T': True,
            'DANGER_FIBER_PRIMITIVE_PYTHAGOREAN': True,
            'FIXED_DIRECTION_TRANSFER_TO_A11': True,
            'GLOBAL_SECOND_MOMENT_REQUIRED_FOR_PRIMARY_T_TARGET': False,
            'PRIMARY_SUFFICIENT_TARGET': 'A_11(B)=O(B^(1/2-delta))',
            'DYADIC_LARGE_SMOOTH_SPLIT_EXPLICIT': True,
            'ODD_LARGE_BRANCH_ROUTING_COMPLETE_FROM_T26': True,
            'LE_BOUDEC_POSITIVE_PROPORTION_LARGE_PRIME_SUBSET_NOT_EXHAUSTIVE': True,
            'ONE_QUADRATIC_COLUMN_SMOOTH_EXCEPTION_POWER_SAVING_AVAILABLE': False,
            'JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED': False,
            'ROUTED_LARGE_BRANCH_POWER_SAVING_PROVED': False,
            'A_11_POWER_SAVING_PROVED': False,
            'T_O_SQRT_B_PROVED': False,
            'PERFECT_CUBOID_NONEXISTENCE_PROVED': False,
            'NEXT': 'Stage14-t28 cover-conditioned (1,1) dyadic incidence count: canonical largest-prime routed branch plus physical smooth branch',
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report['finite_actual'], indent=2))
    print(json.dumps(report['finite_candidate_universe'], indent=2))
    print(json.dumps(final, indent=2))
    print(json.dumps(report['decision'], indent=2))


if __name__ == '__main__':
    main()
