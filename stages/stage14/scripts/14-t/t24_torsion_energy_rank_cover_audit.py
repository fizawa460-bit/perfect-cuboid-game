#!/usr/bin/env python3
"""Stage14-t24: torsion packet energy / rank [-1] cover audit."""

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
T21 = ROOT / 'stages/stage14/scripts/14-t/t21_direction_scale_reduction_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t24/torsion_energy_rank_cover.json'
MAX_B = 2_000_000
CUTS = (1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000)
EXPECTED_RAW = {1000:2,2000:5,5000:15,10000:25,20000:42,50000:62,100000:89,200000:116,500000:188,1000000:255,2000000:356}


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


def quartic_invariants(A, beta):
    """Classical I,J for beta*(x^4+A*x^2*z^2+z^4)."""
    I = (A*A + 12) * beta * beta
    J = 2 * A * (36 - A*A) * beta**3
    return I, J


def packet_universe(B):
    """Potential order-8 Euclid directions before the physical completion gate."""
    amax = isqrt(B)
    rows = []
    mmax = isqrt(amax) + 1
    for m in range(2, mmax + 1):
        for n in range(1, m):
            if gcd(m,n) != 1 or (m-n) % 2 == 0:
                continue
            a = m*m + n*n
            D = a*a
            if D > B:
                continue
            fplus = m**4 + 6*m*m*n*n + n**4
            fminus = m**4 + n**4
            bplus = squarefree_core(fplus)
            bminus = squarefree_core(fminus)
            # Packet identity: F=beta*v^2.
            vp2 = fplus // bplus
            vm2 = fminus // bminus
            vp = isqrt(vp2)
            vm = isqrt(vm2)
            assert vp*vp == vp2 and vm*vm == vm2

            # Binary-quartic invariant/Jacobian check. J=0 in both families,
            # and the standard Jacobian is y^2=x^3-(I/3)x.
            Iplus,Jplus = quartic_invariants(6,bplus)
            Iminus,Jminus = quartic_invariants(0,bminus)
            assert Jplus == Jminus == 0
            assert Iplus // 3 == 16*bplus*bplus
            assert Iminus // 3 == 4*bminus*bminus
            # Explicit nonzero rational 2-torsion roots.
            assert (4*bplus)**2 == Iplus // 3
            assert (2*bminus)**2 == Iminus // 3

            rows.append({
                'm':m,'n':n,'D':D,
                'beta_plus':bplus,'beta_minus':bminus,
                'F_plus':fplus,'F_minus':fminus,
            })
    return rows


def actual_edge_records(a,b,c,d,mask,direction_data):
    sides=(a,b,c)
    specs=((0,1,0),(0,2,1),(1,2,2))
    out=[]
    for i,j,shared_idx in specs:
        if not ((mask & (1 << i)) and (mask & (1 << j))):
            continue
        s=sides[shared_idx]
        others=[sides[k] for k in range(3) if k != shared_idx]
        zdir=direction_data(d,s)
        g,D,C=zdir['g'],zdir['D'],zdir['C']
        alpha,beta,r,u,h=(zdir[k] for k in ('alpha','beta','r','u','h'))
        assert gcd(D,C)==1 and d==g*D and s==g*C
        assert D-C==h*alpha*r*r
        assert D+C==h*beta*u*u

        # Exact displayed discriminant squareclass identity.
        disc = 256 * C**8 * D**2 * (D*D-C*C)
        sq = 16*h*C**4*D*r*u
        assert disc == alpha*beta*sq*sq

        cover_checks=0
        for xx,yy in (others,others[::-1]):
            hx=isqrt(s*s+xx*xx)
            hy=isqrt(s*s+yy*yy)
            assert hx*hx==s*s+xx*xx
            assert hy*hy==s*s+yy*yy
            X=Fraction(xx,g)
            Y=Fraction(yy,g)
            Q=Fraction(hy,g)
            assert Q*Q==D*D-X*X
            assert Y*Y==D*D-C*C-X*X

            # t22/t23 shifted elliptic point.
            U=Fraction(2*D,1)/(D-X)
            z=1-U
            A=Fraction(4*D*D,C*C)-2
            p=D+X
            q=Q
            assert z == -(p/q)**2

            R=Y*Q
            V=Fraction(2*D,1)*R/(D-X)**2
            yE=V/C
            assert yE*yE == z*(z*z+A*z+1)

            # Exact [-1] 2-cover. omega = y*q^3/p.
            omega=yE*q**3/p
            rhs=-p**4 + A*p*p*q*q - q**4
            assert omega*omega == rhs
            cleared=(C*omega)**2
            cleared_rhs=(4*D*D-2*C*C)*p*p*q*q - C*C*(p**4+q**4)
            assert cleared == cleared_rhs
            assert cleared + C*C*(p*p+q*q)**2 == (2*D*p*q)**2

            # Frozen range contains no t23 order-8 necessary hit.
            assert X*X != D*(D-C)
            cover_checks += 1

        out.append({
            'd':d,'D':D,'C':C,'alpha':alpha,'beta':beta,
            'disc_squareclass_checked':True,
            'minus_one_cover_checks':cover_checks,
            'is_triple_edge':mask.bit_count()==3,
        })
    return out


def packet_stats(B):
    rows=packet_universe(B)
    cp=Counter(r['beta_plus'] for r in rows)
    cm=Counter(r['beta_minus'] for r in rows)
    return {
        'primitive_euclid_parameters':len(rows),
        'potential_oriented_torsion_directions':2*len(rows),
        'F_plus_packet_energy':sum(v*v for v in cp.values()),
        'F_minus_packet_energy':sum(v*v for v in cm.values()),
        'combined_packet_energy':sum(v*v for v in cp.values())+sum(v*v for v in cm.values()),
        'max_F_plus_kernel_multiplicity':max(cp.values(),default=0),
        'max_F_minus_kernel_multiplicity':max(cm.values(),default=0),
        'repeated_F_plus_kernels':sorted(k for k,v in cp.items() if v>1),
        'repeated_F_minus_kernels':sorted(k for k,v in cm.items() if v>1),
    }


def main():
    t21=runpy.run_path(str(T21))
    direction_data=t21['direction_data']
    graph=runpy.run_path(str(GRAPH))
    keep,_=graph['enumerate_multi'](MAX_B)

    actual=[]
    for (a,b,c,d),(mask,ds) in keep.items():
        actual.extend(actual_edge_records(a,b,c,d,mask,direction_data))
    actual.sort(key=lambda r:(r['d'],r['D'],r['C']))
    assert len(actual)==356
    assert not any(r['is_triple_edge'] for r in actual)
    assert sum(r['minus_one_cover_checks'] for r in actual)==712

    rows=[]
    for B in CUTS:
        z=[r for r in actual if r['d']<=B]
        assert len(z)==EXPECTED_RAW[B]
        ps=packet_stats(B)
        rows.append({
            'B':B,
            'actual_rank_active_raw_edges':len(z),
            'rank_discriminant_squareclass_checks':len(z),
            'rank_minus_one_cover_orientation_checks':sum(r['minus_one_cover_checks'] for r in z),
            **ps,
        })

    final=rows[-1]
    assert final['primitive_euclid_parameters']==225
    assert final['potential_oriented_torsion_directions']==450
    assert final['F_plus_packet_energy']==225
    assert final['F_minus_packet_energy']==229
    assert final['combined_packet_energy']==454
    assert final['max_F_plus_kernel_multiplicity']==1
    assert final['max_F_minus_kernel_multiplicity']==2
    assert final['repeated_F_plus_kernels']==[]
    assert final['repeated_F_minus_kernels']==[17,113]

    report={
        'stage':'14-t24',
        'torsion_energy_theorem':{
            'packet_curves':'C_{A,beta}: W^2=beta*(M^4+A M^2 N^2+N^4), A in {0,6}',
            'binary_quartic_invariants':'I=(A^2+12)beta^2, J=2A(36-A^2)beta^3; J=0 for A=0,6',
            'jacobian_minus':'Y^2=X^3-4 beta^2 X',
            'jacobian_plus':'Y^2=X^3-16 beta^2 X',
            'uniform_rational_2_torsion':True,
            'fixed_beta_packet_multiplicity':'B^o(1) by bounded-degree 2-cover plus Dujella uniform bounded-height theorem',
            'potential_packet_first_moment':'O(B^(1/2))',
            'torsion_second_moment':'O(B^(1/2+o(1)))',
        },
        'q8_transfer_audit':{
            'F_minus_discriminant':'2^8',
            'F_plus_discriminant':'2^14',
            'Pierce_Xu_quadratic_admissible_every_odd_prime':True,
            'square_sieve_needed_for_torsion_closure':False,
            'reason':'binary-quartic Jacobian route already gives fixed-kernel B^o(1) multiplicity',
        },
        'rank_cover_reduction':{
            'integral_curve':'E_{D,C}: Y^2=X(X^2+(4D^2-2C^2)X+C^4)',
            'displayed_discriminant':'Delta=256 C^8 D^2(D^2-C^2)=alpha beta (16 h C^4 D r u)^2',
            'displayed_discriminant_squareclass':'[Delta]=[alpha beta]',
            'physical_kummer_class':'[-1]',
            'minus_one_cover':'omega^2=-p^4+(4D^2/C^2-2)p^2q^2-q^4',
            'cleared_cover':'(C omega)^2=(4D^2-2C^2)p^2q^2-C^2(p^4+q^4)',
            'right_triangle_form':'(C omega)^2+C^2(p^2+q^2)^2=(2Dpq)^2',
            'moving_displayed_discriminant_factors_fixed_partition':['r','u','beta*u^2-alpha*r^2','beta*u^2+alpha*r^2'],
            'minimal_discriminant_or_conductor_claimed':False,
        },
        'finite':{
            'max_B':MAX_B,
            'actual_rank_active_raw_edges_B2m':final['actual_rank_active_raw_edges'],
            'rank_discriminant_squareclass_checks_B2m':final['rank_discriminant_squareclass_checks'],
            'rank_minus_one_cover_orientation_checks_B2m':final['rank_minus_one_cover_orientation_checks'],
            'potential_primitive_euclid_parameters_B2m':final['primitive_euclid_parameters'],
            'potential_oriented_torsion_directions_B2m':final['potential_oriented_torsion_directions'],
            'F_plus_packet_energy_B2m':final['F_plus_packet_energy'],
            'F_minus_packet_energy_B2m':final['F_minus_packet_energy'],
            'combined_potential_torsion_packet_energy_B2m':final['combined_packet_energy'],
            'max_F_plus_kernel_multiplicity_B2m':final['max_F_plus_kernel_multiplicity'],
            'max_F_minus_kernel_multiplicity_B2m':final['max_F_minus_kernel_multiplicity'],
            'repeated_F_minus_kernels_B2m':final['repeated_F_minus_kernels'],
            'actual_physical_torsion_active_directions_B2m':0,
        },
        'rows':rows,
        'decision':{
            'STAGE14_T24':'COMPLETE_TORSION_SECOND_MOMENT_AND_RANK_MINUS_ONE_COVER_REDUCTION',
            'TORSION_PACKET_BINARY_QUARTIC_2_COVER':True,
            'TORSION_PACKET_JACOBIAN_RATIONAL_2_TORSION':True,
            'FIXED_TORSION_KERNEL_MULTIPLICITY':'B^o(1)',
            'TORSION_SECOND_MOMENT':'O(B^(1/2+o(1)))',
            'TORSION_SECOND_MOMENT_POWER_SAVING_PROVED':True,
            'PIERCE_XU_ODD_PRIME_ADMISSIBILITY':True,
            'RANK_INTEGRAL_4_TORSION_MODEL_EXPLICIT':True,
            'RANK_DISPLAYED_DISCRIMINANT_SQUARECLASS':'alpha*beta',
            'RANK_PHYSICAL_MINUS_ONE_2_COVER_EXPLICIT':True,
            'Q_ACTIVE_REDUCED_TO_RANK_ENERGY':True,
            'RANK_ACTIVE_SECOND_MOMENT_POWER_SAVING_PROVED':False,
            'Q_ACTIVE_DIRECTION_POWER_SAVING_PROVED':False,
            'Q_SPLIT_POWER_SAVING_PROVED':False,
            'Q_EDGE_O_B_PROVED':False,
            'T_O_SQRT_B_PROVED':False,
            'PERFECT_CUBOID_NONEXISTENCE_PROVED':False,
            'NEXT':'Stage14-t25 rank-active Le-Boudec transfer test: minimal discriminant/local large-prime forcing on the explicit [-1] cover and same-partition collision pairs',
        },
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report['finite'],indent=2))
    print(json.dumps(report['decision'],indent=2))


if __name__=='__main__':
    main()
