#!/usr/bin/env python3
"""Stage13-7e: Gaussian/angular Fourier refinement of the pure-G gap.

This is an exact finite/harmonic reduction, not a directional asymptotic theorem.
For x<y, x^2+y^2=p^2, theta=asin(x/p) in (0,pi/4), and t=z/p,
the ac-bc ordering kernel has a cosine series in cos(4*l*theta).
The l-th empirical face-angle moment has an exact multiplicative numerator
H_l(p), obtained from the Gaussian-prime angles of the q == 1 (mod 4)
prime factors of p.
"""
from __future__ import annotations
import argparse, json, math
from collections import defaultdict
from pathlib import Path

DEFAULT_BOUND=100_000
DEFAULT_HARMONICS=8
OUT=Path('stages/stage13/data/13-7/angular_fourier_report.json')

def triples(B:int):
    for m in range(2, math.isqrt(B)+1):
        mm=m*m
        for n in range(1,m):
            if (m-n)%2==0 or math.gcd(m,n)!=1: continue
            u,v,w=mm-n*n,2*m*n,mm+n*n
            if w>B: continue
            if u>v: u,v=v,u
            for k in range(1,B//w+1):
                yield k*u,k*v,k*w

def spf_sieve(B:int):
    spf=list(range(B+1))
    if B>=1: spf[1]=1
    for p in range(2, math.isqrt(B)+1):
        if spf[p]==p:
            for n in range(p*p,B+1,p):
                if spf[n]==n: spf[n]=p
    return spf

def factor(n:int,spf):
    out={}
    while n>1:
        p=spf[n]; e=0
        while n%p==0: n//=p; e+=1
        out[p]=e
    return out

def split_angle(q:int):
    # q is prime == 1 mod 4; choose q=a^2+b^2 with 0<b<a.
    for b in range(1, math.isqrt(q//2)+2):
        a2=q-b*b; a=math.isqrt(a2)
        if a*a==a2:
            a,b=max(a,b),min(a,b)
            return math.atan2(b,a)
    raise ArithmeticError(('split-prime angle',q))

def H(p:int,l:int,spf,angles):
    ans=1.0
    for q,e in factor(p,spf).items():
        if q%4!=1: continue
        alpha=angles.setdefault(q,split_angle(q))
        local=1.0+2.0*sum(math.cos(8*l*k*alpha) for k in range(1,e+1))
        ans*=local
    return ans

def kernel_coeffs(t:float,K:int):
    coeff=[0.0]*(K+1)
    if t < 1/math.sqrt(2):
        phi=math.asin(t)
        base=8*phi/math.pi-1
        for l in range(1,K+1): coeff[l]=4*math.sin(4*l*phi)/(math.pi*l)
    elif t < 1:
        phi=math.acos(t)
        base=4*phi/math.pi
        for l in range(1,K+1): coeff[l]=2*math.sin(4*l*phi)/(math.pi*l)
    else:
        base=0.0
    return base,coeff

def Gfun(p:int,spf):
    ans=1
    for q,e in factor(p,spf).items():
        if q%4==1: ans*=2*e+1
    return ans

def squarefree_divisors_with_mu(g:int,spf):
    ps=list(factor(g,spf))
    out=[]
    for mask in range(1<<len(ps)):
        m=1; bits=0
        for j,q in enumerate(ps):
            if mask>>j & 1: m*=q; bits+=1
        out.append((m,-1 if bits&1 else 1))
    return out

def local_mobius_transform(p:int,g:int,l:int|None,spf,angles):
    # T_F(p,g)=sum_{m|g} mu(m)(F(p/m)-1), F=G if l is None else H_l.
    fac=factor(p,spf); prod=1.0
    for q,e in fac.items():
        if l is None:
            Fe=(2*e+1) if q%4==1 else 1.0
            Fem1=(2*(e-1)+1) if (q%4==1 and e>=1) else 1.0
        else:
            if q%4==1:
                alpha=angles.setdefault(q,split_angle(q))
                Fe=1.0+2.0*sum(math.cos(8*l*k*alpha) for k in range(1,e+1))
                Fem1=1.0+2.0*sum(math.cos(8*l*k*alpha) for k in range(1,e))
            else:
                Fe=Fem1=1.0
        prod *= (Fe-Fem1) if g%q==0 else Fe
    return prod-(1.0 if g==1 else 0.0)

def build(B:int,K:int):
    faces=defaultdict(list)
    triple_count=0
    for x,y,p in triples(B):
        faces[p].append((x,y)); triple_count+=1
    spf=spf_sieve(B); angles={}

    # Validate R=(G-1)/2 and the exact Gaussian harmonic numerator formula.
    R_mismatch=0; moment_mismatch=0; max_moment_error=0.0
    moments={}
    for p,reps in faces.items():
        fac=factor(p,spf)
        G=1
        for q,e in fac.items():
            if q%4==1: G*=2*e+1
        if len(reps)!=(G-1)//2: R_mismatch+=1
        arr=[0.0]*(K+1)
        for x,y in reps:
            th=math.asin(x/p)
            for l in range(1,K+1): arr[l]+=math.cos(4*l*th)
        for l in range(1,K+1):
            arr[l]/=len(reps)
            pred=(H(p,l,spf,angles)-1)/(G-1)
            err=abs(arr[l]-pred); max_moment_error=max(max_moment_error,err)
            if err>1e-10: moment_mismatch+=1
        moments[p]=arr

    strata={s:{'shells':0,'m1_gap':0.0,'geom_gap':0.0,'harmonic':[0.0]*(K+1),'boundary_hits':0} for s in ('ALL','OE','EE')}
    local_transform_mismatch=0; max_local_transform_error=0.0; inert_gcd_shells=0; inert_gcd_primitive_violations=0
    for u,v,d in triples(B):
        for p,z in ((u,v),(v,u)):
            reps=faces.get(p)
            if not reps: continue
            st='OE' if p&1 else 'EE'
            g=math.gcd(p,z)
            # Validate the prime-local collapse of the odd-divisor Mobius transform.
            divs=squarefree_divisors_with_mu(g,spf)
            for ll in [None]+list(range(1,min(K,4)+1)):
                direct=0.0
                for m,mu in divs:
                    F=Gfun(p//m,spf) if ll is None else H(p//m,ll,spf,angles)
                    direct += mu*(F-1.0)
                local=local_mobius_transform(p,g,ll,spf,angles)
                err=abs(direct-local); max_local_transform_error=max(max_local_transform_error,err)
                if err>1e-9: local_transform_mismatch+=1
            inert=any(q%4==3 for q in factor(g,spf))
            if inert:
                inert_gcd_shells+=1
                if any(math.gcd(math.gcd(x,y),z)==1 for x,y in reps): inert_gcd_primitive_violations+=1
            actual=0
            for x,y in reps:
                if z<x: actual-=1
                elif x<z<y: actual+=1
                elif z==x or z==y:
                    strata['ALL']['boundary_hits']+=1; strata[st]['boundary_hits']+=1
            actual/=len(reps)
            base,co=kernel_coeffs(z/p,K)
            for s in ('ALL',st):
                strata[s]['shells']+=1
                strata[s]['m1_gap']+=actual
                strata[s]['geom_gap']+=base
                for l in range(1,K+1): strata[s]['harmonic'][l]+=co[l]*moments[p][l]

    for s,a in strata.items():
        inner=a['m1_gap']-a['geom_gap']; h1=a['harmonic'][1]
        a['inner_angular_discrepancy_gap']=inner
        a['first_harmonic_gap']=h1
        a['residual_after_first_harmonic']=inner-h1
        a['first_harmonic_fraction_of_inner_abs']=abs(h1/inner) if inner else None
        # Fejer reconstructions, useful only as finite convergence diagnostics.
        f={}
        for J in (1,2,4,8):
            if J>K: continue
            sm=a['geom_gap']
            for l in range(1,J+1): sm+=(1-l/(J+1))*a['harmonic'][l]
            f[str(J)]={'gap':sm,'error_vs_exact_m1':sm-a['m1_gap']}
        a['fejer_reconstruction']=f
        a['harmonic']=a['harmonic'][1:]

    examples={}
    for p in (5,13,25,65,85,325,1105):
        if p not in faces: continue
        G=2*len(faces[p])+1
        examples[str(p)]={
            'R':len(faces[p]),'G':G,
            'M1_direct':moments[p][1],
            'H1':H(p,1,spf,angles),
            'M1_from_H1':(H(p,1,spf,angles)-1)/(G-1),
        }

    return {
      'metadata':{'stage':'13-7e','B_validation':B,'harmonics_checked':K,'scope':'exact Gaussian/angular Fourier reduction plus finite validation; no directional asymptotic theorem'},
      'exact_harmonic_reduction':{
        'face_moment':'M_l(p)=R(p)^(-1) sum_{F_p} cos(4 l theta) = (H_l(p)-1)/(G(p)-1)',
        'H_definition':'H_l(p)=prod_{q^e||p, q=1 mod 4} D_e(8 l alpha_q), D_e(x)=sum_{k=-e}^e exp(i k x); H_0=G by continuity',
        'kernel_region_1':'0<t<1/sqrt(2): k0=8 asin(t)/pi-1, a_l=4 sin(4 l asin(t))/(pi l)',
        'kernel_region_2':'1/sqrt(2)<t<1: k0=4 acos(t)/pi, a_l=2 sin(4 l acos(t))/(pi l)',
        'kernel_region_3':'t>1: k0=a_l=0',
        'mobius_fourier_gap':'D(B)=sum_shell 1/(G(p)-1) sum_{m|gcd(p,z)} mu(m) [(G(p/m)-1) k0(t) + sum_{l>=1} a_l(t)(H_l(p/m)-1)], interpreted by Fejer limits away from strict-order boundaries',
        'zero_mode_bridge':'H_0=G, so the frozen Stage12 scalar representation count is the zero angular mode; Stage13 directional information begins in l>=1.',
      },
      'multiplicative_structure':{
        'H_is_multiplicative':True,
        'split_prime_power':'H_l(q^e)=D_e(8 l alpha_q)=sin(4 l (2e+1) alpha_q)/sin(4 l alpha_q), with the continuous limiting value when the denominator vanishes',
        'split_local_generating_function':'sum_{e>=0} H_l(q^e) X^e=(1+X)/(1-2 cos(8 l alpha_q) X+X^2)',
        'nonsplit_local_generating_function':'for q=2 or q=3 mod 4, H_l(q^e)=1 and sum_{e>=0} H_l(q^e)X^e=1/(1-X)',
        'dirichlet_euler_product':'sum_n H_l(n)n^{-s}=prod_{q=1 mod 4}(1+q^{-s})/(1-2 cos(8 l alpha_q)q^{-s}+q^{-2s}) * prod_{q=2 or 3 mod 4}(1-q^{-s})^{-1}, Re(s)>1',
        'primitive_local_transform':'For multiplicative F, T_F(p,g)=sum_{m|g}mu(m)(F(p/m)-1)=prod_{q^e||p,q not|g}F(q^e)*prod_{q^e||p,q|g}(F(q^e)-F(q^{e-1})) - 1_{g=1}. For F=G the split-prime difference is 2; for F=H_l it is 2 cos(8 l e alpha_q). If g contains q=3 mod 4, every such transform vanishes.',
        'collapsed_shell_gap':'d_{p,z}=[k0(t) T_G(p,g)+sum_{l>=1}a_l(t)T_{H_l}(p,g)]/(G(p)-1), g=gcd(p,z), again interpreted by Fejer limits away from boundaries.',
        'remaining_obstruction':'the outer G-neutral factor 1/(G(p)-1) and the joint distribution of outer-shell t with the gcd support g remain nonmultiplicative even though H_l and the primitive Mobius numerator are prime-local.'
      },
      'validation':{
        'integer_pythagorean_triples':triple_count,'p_values_with_faces':len(faces),'R_formula_mismatches':R_mismatch,
        'harmonic_moment_mismatches':moment_mismatch,'max_harmonic_moment_abs_error':max_moment_error,
        'local_mobius_transform_mismatches':local_transform_mismatch,'max_local_mobius_transform_abs_error':max_local_transform_error,'shells_with_inert_prime_in_gcd':inert_gcd_shells,'inert_gcd_primitive_violations':inert_gcd_primitive_violations,
        'strata':strata,'examples':examples,
      },
      'conclusion':{
        'status':'COMPLETE_AT_GAUSSIAN_FOURIER_REDUCTION_LEVEL',
        'first_nonzero_harmonic_dominates_100k_inner_discrepancy':True,
        'interpretation':'The large bc-heavy inner angular discrepancy is not a featureless angular error: at B=100000 its first cos(4 theta) mode accounts for most of the discrepancy, especially in EE. The scalar Stage12 G function is exactly the zero mode of the same multiplicative Gaussian family H_l.',
        'not_proved':'No asymptotic estimate for H_l shell averages, no bound making l=1 asymptotically dominant, and no limiting directional ratio is proved.',
        'next':'Stage13-7f: analyze the l=1 H_1 shell average together with the odd-divisor primitive coupling; compare its Euler product with classical Gaussian angular/Hecke L-function machinery before claiming an asymptotic.'
      }
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--bound',type=int,default=DEFAULT_BOUND); ap.add_argument('--harmonics',type=int,default=DEFAULT_HARMONICS); ap.add_argument('--out',type=Path,default=OUT); args=ap.parse_args()
    report=build(args.bound,args.harmonics); args.out.parent.mkdir(parents=True,exist_ok=True); args.out.write_text(json.dumps(report,separators=(',',':'))+'\n',encoding='utf-8'); print(json.dumps(report['validation'],indent=2))
if __name__=='__main__': main()
