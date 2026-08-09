#!/usr/bin/env python3
"""Stage14-t22: fixed-direction simultaneous completion / elliptic quotient audit."""

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt, lcm
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
T21 = ROOT / 'stages/stage14/scripts/14-t/t21_direction_scale_reduction_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t22/uniform_direction_quotient.json'
MAX_B = 2_000_000
CUTS = (1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000)
EXPECTED = {1000:2,2000:5,5000:15,10000:25,20000:42,50000:62,100000:89,200000:116,500000:188,1000000:255,2000000:356}


def qheight(q):
    q = Fraction(q)
    return max(abs(q.numerator), q.denominator)


def edge_records(a, b, c, d, mask, direction_data):
    sides = (a, b, c)
    specs = ((0,1,0), (0,2,1), (1,2,2))
    out = []
    for i, j, shared_idx in specs:
        if not ((mask & (1 << i)) and (mask & (1 << j))):
            continue
        s = sides[shared_idx]
        others = [sides[k] for k in range(3) if k != shared_idx]
        x, y = others
        z = direction_data(d, s)
        g, D, C = z['g'], z['D'], z['C']
        assert d == g * D and s == g * C
        assert gcd(C, D) == 1 and D > C > 0
        assert gcd(s, gcd(x, y)) == 1

        hx = isqrt(s*s + x*x)
        hy = isqrt(s*s + y*y)
        assert hx*hx == s*s + x*x
        assert hy*hy == s*s + y*y
        K = D*D - C*C
        assert x*x + y*y == g*g*K

        X = Fraction(x, g)
        Y = Fraction(y, g)
        P = Fraction(hx, g)
        Q = Fraction(hy, g)
        assert P*P == C*C + X*X
        assert Q*Q == C*C + Y*Y
        assert X*X + Y*Y == K

        # Primitive normalization makes g the exact common denominator of X,Y.
        canonical_g = lcm(X.denominator, Y.denominator)
        assert canonical_g == g

        quotient_checks = 0
        for xx, yy, hh in ((x, y, hy), (y, x, hx)):
            Xq = Fraction(xx, g)
            Yq = Fraction(yy, g)
            Hq = Fraction(hh, g)
            R = Yq * Hq
            assert R*R == (K - Xq*Xq) * (D*D - Xq*Xq)

            # Birational cubic model: U=2D/(D-X), V=2D R/(D-X)^2.
            assert Xq < D
            den = D - Xq
            U = Fraction(2*D, 1) / den
            V = Fraction(2*D, 1) * R / (den*den)
            rhs = (U - 1) * (-C*C*U*U + 4*D*D*U - 4*D*D)
            assert V*V == rhs

            # Exact polynomial physical-height transfer.
            assert qheight(U) <= 2*d
            assert qheight(V) <= 2*d*d*d
            quotient_checks += 1

        # Smooth cubic: U=1 is a simple rational root; the other quadratic
        # has discriminant 16 D^2(D^2-C^2)>0 and does not vanish at U=1.
        assert -C*C != 0
        assert 16*D*D*K > 0

        out.append({
            'd': d, 's': s, 'g': g, 'D': D, 'C': C,
            'alpha': z['alpha'], 'beta': z['beta'],
            'canonical_scale_checked': True,
            'quotient_checks': quotient_checks,
            'is_triple_edge': mask.bit_count() == 3,
        })
    return out


def main():
    t21 = runpy.run_path(str(T21))
    direction_data = t21['direction_data']
    graph = runpy.run_path(str(GRAPH))
    keep, _ = graph['enumerate_multi'](MAX_B)

    records = []
    for (a,b,c,d),(mask,ds) in keep.items():
        records.extend(edge_records(a,b,c,d,mask,direction_data))
    records.sort(key=lambda r:(r['d'],r['s'],r['D'],r['C']))
    assert len(records) == 356
    assert sum(r['is_triple_edge'] for r in records) == 0
    assert sum(r['quotient_checks'] for r in records) == 712

    rows = []
    for B in CUTS:
        z = [r for r in records if r['d'] <= B]
        assert len(z) == EXPECTED[B]
        direction_counts = Counter((r['D'],r['C']) for r in z)
        part_active_dirs = Counter((r['alpha'],r['beta']) for r in z)
        q_active = sum(v*v for v in part_active_dirs.values())
        assert max(direction_counts.values(), default=0) == 1
        assert max(part_active_dirs.values(), default=0) == 1
        assert q_active == len(z)
        rows.append({
            'B': B,
            'raw_pair_edges': len(z),
            'active_reduced_directions': len(direction_counts),
            'max_edges_per_reduced_direction': max(direction_counts.values(), default=0),
            'active_direction_partition_second_moment': q_active,
        })

    final = rows[-1]
    report = {
        'stage': '14-t22',
        'normalized_completion_curve': {
            'curve': 'P^2=C^2+X^2; Q^2=C^2+Y^2; X^2+Y^2=D^2-C^2',
            'elliptic_quotient_quartic': 'R^2=(D^2-C^2-X^2)(D^2-X^2), R=YQ',
            'birational_cubic': 'V^2=(U-1)(-C^2 U^2+4D^2 U-4D^2), U=2D/(D-X), V=2DR/(D-X)^2',
            'quotient_degree_upper_bound': 4,
            'rational_exact_2_torsion': '(U,V)=(1,0)',
            'smooth_for_every_reduced_direction_D_gt_C_gt_0': True,
        },
        'height_and_scale': {
            'canonical_primitive_scale': 'g=lcm(den(X),den(Y))',
            'canonical_scale_verified_on_all_frozen_edges': True,
            'quotient_U_height_bound': 'H(U)<=2d',
            'quotient_V_height_bound': 'H(V)<=2d^3',
            'dujella_reference': 'Marta Dujella, arXiv:2312.03655, uniform exp(C log H/log log H) bound for elliptic curves with rational prime-order torsion',
            'uniform_fixed_direction_total_edge_bound': '(DG)^o(1) for g<=G, hence B^o(1) under d=gD<=B',
        },
        'active_direction_reduction': {
            'definition': 'A_{alpha,beta}(B)=number of generalized-Pell reduced directions in partition (alpha,beta) that have at least one physical simultaneous completion with d<=B',
            'fixed_partition_bound': 'N_{alpha,beta}(B) <= B^o(1) A_{alpha,beta}(B)',
            'second_moment_reduction': 'Q_split(B) <= B^o(1) Q_active_dir(B), Q_active_dir=sum A_{alpha,beta}(B)^2',
            'sufficient_target': 'Q_active_dir(B)=O(B^(1-delta)) for some delta>0 implies T(B)=o(sqrt(B))',
        },
        'finite': {
            'max_B': MAX_B,
            'raw_pair_edges_B2m': final['raw_pair_edges'],
            'canonical_scale_identity_checks_B2m': len(records),
            'elliptic_quotient_identity_checks_B2m': sum(r['quotient_checks'] for r in records),
            'smooth_cubic_checks_B2m': len(records),
            'active_reduced_directions_B2m': final['active_reduced_directions'],
            'max_edges_per_reduced_direction_B2m': final['max_edges_per_reduced_direction'],
            'active_direction_partition_second_moment_B2m': final['active_direction_partition_second_moment'],
        },
        'rows': rows,
        'decision': {
            'STAGE14_T22': 'COMPLETE_UNIFORM_FIXED_DIRECTION_ELLIPTIC_QUOTIENT_BOUND',
            'SIMULTANEOUS_COMPLETION_NORMALIZED_CURVE_EXPLICIT': True,
            'ELLIPTIC_QUOTIENT_EXPLICIT': True,
            'ELLIPTIC_QUOTIENT_RATIONAL_2_TORSION': True,
            'PRIMITIVE_SCALE_IS_CANONICAL_DENOMINATOR': True,
            'PHYSICAL_TO_QUOTIENT_HEIGHT_POLYNOMIAL': True,
            'DUJELLA_UNIFORM_BOUND_APPLIES': True,
            'FIXED_DIRECTION_ALL_SCALE_MULTIPLICITY': 'B^o(1)',
            'N_ALPHA_BETA_LE_B_O1_ACTIVE_DIRECTIONS': True,
            'Q_SPLIT_LE_B_O1_Q_ACTIVE_DIRECTION': True,
            'ACTIVE_DIRECTION_SECOND_MOMENT_POWER_SAVING_PROVED': False,
            'Q_SPLIT_POWER_SAVING_PROVED': False,
            'Q_EDGE_O_B_PROVED': False,
            'T_O_SQRT_B_PROVED': False,
            'PERFECT_CUBOID_NONEXISTENCE_PROVED': False,
            'NEXT': 'Stage14-t23 attack the active generalized-Pell direction second moment; classify torsion/positive-rank activation and seek a power-saving family count',
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report['finite'], indent=2))
    print(json.dumps(report['decision'], indent=2))


if __name__ == '__main__':
    main()
