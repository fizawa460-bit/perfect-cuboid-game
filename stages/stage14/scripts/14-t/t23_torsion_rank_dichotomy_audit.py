#!/usr/bin/env python3
"""Stage14-t23: torsion/positive-rank dichotomy on the t22 direction quotient."""

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
T21 = ROOT / 'stages/stage14/scripts/14-t/t21_direction_scale_reduction_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t23/torsion_rank_dichotomy.json'
MAX_B = 2_000_000
CUTS = (1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000)
EXPECTED = {1000:2,2000:5,5000:15,10000:25,20000:42,50000:62,100000:89,200000:116,500000:188,1000000:255,2000000:356}


def is_square_int(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r*r == n


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
    while p*p <= n:
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


def edge_records(a, b, c, d, mask, direction_data):
    sides = (a,b,c)
    specs = ((0,1,0), (0,2,1), (1,2,2))
    out = []
    for i,j,shared_idx in specs:
        if not ((mask & (1 << i)) and (mask & (1 << j))):
            continue
        s = sides[shared_idx]
        others = [sides[k] for k in range(3) if k != shared_idx]
        zdir = direction_data(d,s)
        g,D,C = zdir['g'],zdir['D'],zdir['C']
        K = D*D-C*C
        assert d == g*D and s == g*C and gcd(D,C) == 1

        orientation_checks = 0
        order8_hits = 0
        for xx,yy in (others, others[::-1]):
            hx = isqrt(s*s + xx*xx)
            hy = isqrt(s*s + yy*yy)
            assert hx*hx == s*s + xx*xx
            assert hy*hy == s*s + yy*yy
            X = Fraction(xx,g)
            Y = Fraction(yy,g)
            Q = Fraction(hy,g)
            assert Q*Q == D*D-X*X
            assert Y*Y == K-X*X

            # t22 quotient, shifted to the standard rational-4-torsion model:
            # E: y^2=z(z^2+A z+1), A=4(D/C)^2-2.
            U = Fraction(2*D,1) / (D-X)
            z = 1-U
            A = Fraction(4*D*D,C*C)-2
            assert z < -1
            q = (D+X)/Q
            assert z == -q*q

            R = Y*Q
            V = Fraction(2*D,1)*R/(D-X)**2
            yE = V/C
            assert yE*yE == z*(z*z+A*z+1)
            assert yE != 0

            # Built-in rational 4-torsion P4=(1,2D/C); duplication numerator is zero.
            s4 = Fraction(2*D,C)
            assert s4*s4 == A+2

            # Exact duplication formula:
            # x(2P)=(z^2-1)^2/[4z(z^2+Az+1)] = (C X/(QY))^2 >= 0.
            x2 = (z*z-1)**2 / (4*z*(z*z+A*z+1))
            assert x2 == (Fraction(C,1)*X/(Q*Y))**2
            assert x2 >= 0

            # Mazur + the 2-isogeny Kummer class leaves exact order 8 as the
            # only physical torsion possibility.  Then 2P is order 4; x(2P)
            # cannot be -1 because it is a square, so it must be +1.
            order8_necessary = (X*X == D*(D-C))
            assert (x2 == 1) == order8_necessary
            if order8_necessary:
                assert Q*Q == C*D
                assert Y*Y == C*(D-C)
                assert is_square_int(D) and is_square_int(C) and is_square_int(D-C)
                aa,bb,cc = isqrt(D),isqrt(C),isqrt(D-C)
                assert aa*aa == bb*bb+cc*cc and gcd(aa,gcd(bb,cc)) == 1
                order8_hits += 1
            orientation_checks += 1

        out.append({
            'd':d,'s':s,'g':g,'D':D,'C':C,
            'alpha':zdir['alpha'],'beta':zdir['beta'],
            'kappa':zdir['alpha']*zdir['beta'],
            'full_rational_2_torsion': is_square_int(K),
            'orientation_checks':orientation_checks,
            'physical_order8_necessary_hits':order8_hits,
            'positive_rank_certified_by_non_torsion_physical_point': order8_hits == 0,
            'is_triple_edge': mask.bit_count() == 3,
        })
    return out


def torsion_quartic_packet_identity(m,n):
    assert m > n > 0 and gcd(m,n) == 1 and (m-n) % 2 == 1
    a = m*m+n*n
    even = 2*m*n
    odd = m*m-n*n
    D = a*a

    C = even*even
    h = gcd(D-C,D+C)
    assert h == 1
    A = (D-C)//h
    B = (D+C)//h
    assert is_square_int(A) and squarefree_core(A) == 1
    assert B == m**4 + 6*m*m*n*n + n**4

    C = odd*odd
    h = gcd(D-C,D+C)
    assert h == 2
    A = (D-C)//h
    B = (D+C)//h
    assert squarefree_core(A) == 2
    assert B == m**4+n**4
    return 2


def main():
    t21 = runpy.run_path(str(T21))
    direction_data = t21['direction_data']
    graph = runpy.run_path(str(GRAPH))
    keep,_ = graph['enumerate_multi'](MAX_B)

    records=[]
    for (a,b,c,d),(mask,ds) in keep.items():
        records.extend(edge_records(a,b,c,d,mask,direction_data))
    records.sort(key=lambda r:(r['d'],r['s'],r['D'],r['C']))
    assert len(records)==356
    assert sum(r['orientation_checks'] for r in records)==712
    assert sum(r['physical_order8_necessary_hits'] for r in records)==0
    assert all(r['positive_rank_certified_by_non_torsion_physical_point'] for r in records)

    synthetic_packet_checks=0
    for m in range(2,40):
        for n in range(1,m):
            if gcd(m,n)==1 and (m-n)%2==1:
                synthetic_packet_checks += torsion_quartic_packet_identity(m,n)
    assert synthetic_packet_checks > 100

    rows=[]
    for B in CUTS:
        z=[r for r in records if r['d']<=B]
        assert len(z)==EXPECTED[B]
        parts=Counter((r['alpha'],r['beta']) for r in z)
        rank_parts=Counter((r['alpha'],r['beta']) for r in z if r['positive_rank_certified_by_non_torsion_physical_point'])
        torsion_possible=[r for r in z if r['physical_order8_necessary_hits']]
        q_active=sum(v*v for v in parts.values())
        q_rank=sum(v*v for v in rank_parts.values())
        assert not torsion_possible
        assert q_active==q_rank==len(z)
        rows.append({
            'B':B,
            'raw_pair_edges':len(z),
            'physical_quotient_positive_rank_certified_edges':len(z),
            'physical_order8_necessary_edges':0,
            'active_direction_partition_second_moment':q_active,
            'rank_active_partition_second_moment':q_rank,
        })

    final=rows[-1]
    report={
        'stage':'14-t23',
        'torsion_model':{
            'shifted_curve':'E_{D,C}: y^2=z(z^2+(4D^2/C^2-2)z+1)',
            'built_in_order_4_point':'P4=(1,2D/C), 2P4=(0,0)',
            'physical_kummer_class':'z=1-U=-(D+X)/(D-X)=-((D+X)/Q)^2, hence [z]=[-1]',
            'mazur_dichotomy':'with built-in Z/4, torsion is cyclic Z/4,Z/8,Z/12 when E[2](Q)=Z/2, or Z/2xZ/4,Z/2xZ/8 when full rational 2-torsion',
            'physical_torsion_reduction':'physical z<-1 and [z]=[-1] exclude all torsion possibilities except exact order 8',
        },
        'order8_reduction':{
            'duplication':'x(2P)=(z^2-1)^2/(4z(z^2+Az+1))=(C X/(QY))^2',
            'necessary_and_exact_target':'physical torsion => order 8 => x(2P)=1 => X^2=D(D-C)',
            'square_direction_consequence':'D=a^2, C=b^2, D-C=c^2 with primitive a^2=b^2+c^2',
            'global_first_moment_bound':'number of torsion-active reduced directions with D<=B is O(B^(1/2+o(1)))',
        },
        'torsion_quartic_packets':{
            'euclid_parameters':'a=m^2+n^2, legs 2mn and m^2-n^2, gcd(m,n)=1, opposite parity',
            'alpha_1_packet':'if C=(2mn)^2 then alpha=1 and beta=core(m^4+6m^2n^2+n^4)',
            'alpha_2_packet':'if C=(m^2-n^2)^2 then alpha=2 and beta=core(m^4+n^4)',
            'synthetic_identity_checks':synthetic_packet_checks,
            'polynomial_square_sieve_trigger':True,
        },
        'second_moment_split':{
            'definition':'A=A_rank+A_tor by split partition; Q_active<=2Q_rank+2Q_tor',
            'rank_branch':'every active direction carrying a physical point outside the order-8 locus has a non-torsion rational quotient point, hence positive Mordell-Weil rank',
            'torsion_branch':'supported on the two explicit quartic squarefree-kernel packets above; first moment O(B^(1/2+o(1))) but its partition second moment is not yet power-saved',
            'sufficient_next_target':'prove fixed power savings for both Q_rank(B) and Q_tor(B)',
        },
        'finite':{
            'max_B':MAX_B,
            'raw_pair_edges_B2m':final['raw_pair_edges'],
            'physical_quotient_checks_B2m':sum(r['orientation_checks'] for r in records),
            'physical_order8_necessary_edges_B2m':0,
            'physical_positive_rank_certified_edges_B2m':final['physical_quotient_positive_rank_certified_edges'],
            'rank_active_partition_second_moment_B2m':final['rank_active_partition_second_moment'],
        },
        'rows':rows,
        'decision':{
            'STAGE14_T23':'COMPLETE_TORSION_POSITIVE_RANK_DICHOTOMY_AND_ORDER8_PACKET_REDUCTION',
            'DIRECTION_QUOTIENT_HAS_RATIONAL_4_TORSION':True,
            'PHYSICAL_KUMMER_CLASS_MINUS_ONE':True,
            'PHYSICAL_TORSION_ONLY_POSSIBLE_ORDER8':True,
            'ORDER8_IMPLIES_D_C_DMINUSC_ALL_SQUARE':True,
            'TORSION_ACTIVE_DIRECTION_FIRST_MOMENT':'B^(1/2+o(1))',
            'TORSION_BRANCH_QUARTIC_PACKET_EXPLICIT':True,
            'FINITE_ORDER8_NECESSARY_HITS_B2M':0,
            'FINITE_ALL_ACTIVE_EDGES_CERTIFIED_POSITIVE_RANK_B2M':True,
            'ACTIVE_SECOND_MOMENT_SPLIT_RANK_PLUS_TORSION':True,
            'TORSION_SECOND_MOMENT_POWER_SAVING_PROVED':False,
            'RANK_ACTIVE_SECOND_MOMENT_POWER_SAVING_PROVED':False,
            'Q_ACTIVE_DIRECTION_POWER_SAVING_PROVED':False,
            'Q_SPLIT_POWER_SAVING_PROVED':False,
            'Q_EDGE_O_B_PROVED':False,
            'T_O_SQRT_B_PROVED':False,
            'PERFECT_CUBOID_NONEXISTENCE_PROVED':False,
            'NEXT':'Stage14-t24 attack the two second moments separately: quartic squarefree-kernel collisions on the order-8 torsion packet and positive-rank/small-point frequency on the remaining active direction family',
        },
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report['finite'],indent=2))
    print(json.dumps(report['decision'],indent=2))


if __name__=='__main__':
    main()
