#!/usr/bin/env python3
"""Stage14-t26: complete odd-prime Gaussian/dual routing audit."""

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
T21 = ROOT / 'stages/stage14/scripts/14-t/t21_direction_scale_reduction_audit.py'
OUT = ROOT / 'stages/stage14/data/14-t26/complete_large_prime_routing.json'
MAX_B = 2_000_000
CUTS = (1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000)
EXPECTED = {1000:2,2000:5,5000:15,10000:25,20000:42,50000:62,100000:89,200000:116,500000:188,1000000:255,2000000:356}


def factorint(n):
    n = abs(int(n)); out = {}
    while n and n % 2 == 0:
        out[2] = out.get(2,0)+1; n //= 2
    p = 3
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p,0)+1; n //= p
        p += 2
    if n > 1: out[n] = out.get(n,0)+1
    return out


def vp(n,p):
    n=abs(int(n)); e=0
    while n and n%p==0:
        e+=1; n//=p
    return e


def sqrt_minus_one_mod_prime(p):
    assert p % 4 == 1
    g = 2
    while pow(g,(p-1)//2,p) != p-1:
        g += 1
    r = pow(g,(p-1)//4,p)
    assert (r*r+1) % p == 0
    return r


def sqrt_minus_one_mod_prime_power(p,k):
    assert k >= 1 and p % 4 == 1
    r = sqrt_minus_one_mod_prime(p)
    mod = p
    for _ in range(1,k):
        c = (r*r+1)//mod
        t = (-c * pow(2*r,-1,p)) % p
        r += t*mod
        mod *= p
        assert (r*r+1) % mod == 0
    return r % mod


def edge_records(a,b,c,d,mask,direction_data):
    sides=(a,b,c); specs=((0,1,0),(0,2,1),(1,2,2)); out=[]
    for i,j,shared_idx in specs:
        if not ((mask & (1<<i)) and (mask & (1<<j))):
            continue
        s=sides[shared_idx]
        others=[sides[k] for k in range(3) if k != shared_idx]
        z=direction_data(d,s)
        g,D,C=(z[k] for k in ('g','D','C'))
        alpha,beta,r,u,h=(z[k] for k in ('alpha','beta','r','u','h'))
        K=D*D-C*C
        assert gcd(D,C)==1 and d==g*D and s==g*C
        assert D-C==h*alpha*r*r and D+C==h*beta*u*u

        route = Counter()
        orient_checks=0
        dual_checks=0
        for xx,yy in (others,others[::-1]):
            hy=isqrt(s*s+yy*yy); assert hy*hy==s*s+yy*yy
            rat=Fraction(d+xx,hy)
            p,q=rat.numerator,rat.denominator
            assert p>q>0 and gcd(p,q)==1
            S=p*p+q*q; T=p*p-q*q
            rhs=(4*D*D-2*C*C)*p*p*q*q-C*C*(p**4+q**4)
            W=isqrt(rhs); assert W*W==rhs
            assert W*W+C*C*S*S==(2*D*p*q)**2
            assert W*W+C*C*T*T==4*K*p*p*q*q

            # Dual 2-isogeny image: E' has full rational 2-torsion.
            xp=Fraction(W*W,p*p*q*q)
            assert xp == Fraction(W,p*q)**2
            assert xp-4*D*D == -Fraction(C*S,p*q)**2
            assert xp-4*K == -Fraction(C*T,p*q)**2
            dual_checks += 1

            # D-column: all odd primes are split by t25. Route to S or a
            # Gaussian linear congruence modulo the full D^2 contribution.
            for ell,eD in factorint(D).items():
                if ell==2: continue
                assert ell%4==1
                if S%ell==0:
                    route['D_to_S'] += 1
                else:
                    k=2*eD; mod=ell**k
                    rho=sqrt_minus_one_mod_prime_power(ell,k)
                    f1=(W-rho*C*S) % mod; f2=(W+rho*C*S) % mod
                    assert (f1==0) ^ (f2==0)
                    route['D_to_Gaussian'] += 1

            # r/u columns.  Inert primes use t25 valuation forcing; split
            # primes route to T or one Gaussian sign with the moving 2f power.
            for ell,f in factorint(r*u).items():
                if ell==2: continue
                if ell%4==3:
                    forced=ell**f
                    assert W%forced==0 and T%forced==0
                    route['RU_3mod4_to_T'] += 1
                else:
                    if T%ell==0:
                        route['RU_1mod4_to_T'] += 1
                    else:
                        k=2*f; mod=ell**k
                        rho=sqrt_minus_one_mod_prime_power(ell,k)
                        f1=(W-rho*C*T) % mod; f2=(W+rho*C*T) % mod
                        assert (f1==0) ^ (f2==0)
                        route['RU_1mod4_to_Gaussian'] += 1

            # C-column: dual/integer factorization.
            Lm=2*D*p*q-W; Lp=2*D*p*q+W
            assert Lm*Lp==C*C*S*S
            for ell,eC in factorint(C).items():
                if ell==2: continue
                if (p*q)%ell==0:
                    route['C_to_pq'] += 1
                else:
                    assert not (Lm%ell==0 and Lp%ell==0)
                    need=2*eC
                    okm=vp(Lm,ell)>=need; okp=vp(Lp,ell)>=need
                    assert okm ^ okp
                    route['C_to_dual_linear'] += 1
            orient_checks += 1

        out.append({
            'd':d,'D':D,'C':C,'alpha':alpha,'beta':beta,'r':r,'u':u,
            'orientation_checks':orient_checks,'dual_descent_checks':dual_checks,
            'route_counts':dict(route),'is_triple_edge':mask.bit_count()==3,
        })
    return out


def main():
    t21=runpy.run_path(str(T21)); direction_data=t21['direction_data']
    graph=runpy.run_path(str(GRAPH)); keep,_=graph['enumerate_multi'](MAX_B)
    rec=[]
    for (a,b,c,d),(mask,ds) in keep.items():
        rec.extend(edge_records(a,b,c,d,mask,direction_data))
    rec.sort(key=lambda x:(x['d'],x['D'],x['C']))
    assert len(rec)==356 and not any(x['is_triple_edge'] for x in rec)
    assert sum(x['orientation_checks'] for x in rec)==712
    assert sum(x['dual_descent_checks'] for x in rec)==712

    rows=[]
    for B in CUTS:
        z=[x for x in rec if x['d']<=B]; assert len(z)==EXPECTED[B]
        c=Counter()
        for x in z: c.update(x['route_counts'])
        rows.append({'B':B,'rank_active_raw_edges':len(z),'orientation_checks':sum(x['orientation_checks'] for x in z),'dual_descent_checks':sum(x['dual_descent_checks'] for x in z),'route_counts':dict(sorted(c.items()))})
    final=rows[-1]
    report={
        'stage':'14-t26',
        'dual_descent':{
            'dual_curve':'E_prime: y^2=x(x-4D^2)(x-4(D^2-C^2))',
            'physical_x_prime':'x_prime=(W/(pq))^2',
            'physical_differences':['x_prime-4D^2=-(C(p^2+q^2)/(pq))^2','x_prime-4(D^2-C^2)=-(C(p^2-q^2)/(pq))^2'],
            'physical_signature':'[1,-1,-1]',
        },
        'routing_theorem':{
            'D_column':'odd ell|D is 1 mod 4; either ell|S or ell^(2v_D) divides W +/- rho*C*S',
            'RU_3mod4':'ell^v_ru divides W and T',
            'RU_1mod4':'either ell|T or ell^(2v_ru) divides W +/- rho*C*T',
            'C_column':'either ell|pq or ell^(2v_C) divides 2D*pq +/- W',
            'state_loss':'at most 2^omega from sign allocations, hence B^o(1)',
            'prime_2':'not routed in t26',
        },
        'finite':{'max_B':MAX_B,**{k:v for k,v in final.items() if k!='B'}},
        'rows':rows,
        'decision':{
            'STAGE14_T26':'COMPLETE_ODD_PRIME_GAUSSIAN_AND_DUAL_ROUTING',
            'DUAL_CURVE_FULL_RATIONAL_2_TORSION':True,
            'PHYSICAL_DUAL_DESCENT_SIGNATURE':'1,-1,-1',
            'D_COLUMN_ODD_PRIME_ROUTING_COMPLETE':True,
            'RU_COLUMN_ODD_PRIME_ROUTING_COMPLETE':True,
            'C_COLUMN_ODD_PRIME_ROUTING_COMPLETE':True,
            'ODD_LARGE_PRIME_LOCAL_ROUTING_COMPLETE':True,
            'GAUSSIAN_STATE_LOSS':'B^o(1)',
            'LARGE_PRIME_AVAILABILITY_POWER_SAVING_PROVED':False,
            'ROUTED_PAIR_INCIDENCE_POWER_SAVING_PROVED':False,
            'RANK_ACTIVE_SECOND_MOMENT_POWER_SAVING_PROVED':False,
            'Q_ACTIVE_DIRECTION_POWER_SAVING_PROVED':False,
            'Q_EDGE_O_B_PROVED':False,
            'T_O_SQRT_B_PROVED':False,
            'NEXT':'Stage14-t27 large-prime availability / smooth-exception split and routed same-partition pair-incidence count',
        },
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report['finite'],indent=2))
    print(json.dumps(report['decision'],indent=2))

if __name__=='__main__': main()
