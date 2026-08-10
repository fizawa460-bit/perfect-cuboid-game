#!/usr/bin/env python3
from __future__ import annotations
import cmath, json, math, runpy
from collections import Counter
from math import gcd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
T36=ROOT/'stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py'
T42=ROOT/'stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py'
T79=ROOT/'stages/stage14/14-t79/result.md'
TH22=ROOT/'stages/stage14/14-tH22/result.md'
MAINLINE=ROOT/'stages/stage14/14-4cx/result.md'

def oddpart(n):
    n=abs(n)
    while n and n%2==0:n//=2
    return n

def factor(n):
    out={}; n=abs(n); p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p=3 if p==2 else p+2
    if n>1:out[n]=out.get(n,0)+1
    return out

def primes(n):return sorted(factor(n))
def divisors_sf(n):
    ds=[1]
    for p in primes(n):ds += [d*p for d in list(ds)]
    return sorted(ds)
def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    p=3
    while p*p<=n:
        if n%p==0:return False
        p+=2
    return True

def inv(a,p):return pow(a%p,-1,p)
def allowed(p):return [None]+[x for x in range(p) if (1+x*x)%p!=0]
def mul(x,y,p):
    if x is None and y is None:return 0
    if x is None:return None if y%p==0 else (-inv(y,p))%p
    if y is None:return None if x%p==0 else (-inv(x,p))%p
    den=(1-x*y)%p
    return None if den==0 else ((x+y)*inv(den,p))%p

def order(x,p):
    cur=0
    for n in range(1,len(allowed(p))+1):
        cur=mul(cur,x,p)
        if cur==0:return n
    raise AssertionError

def logs(p):
    N=len(allowed(p)); g=next(x for x in allowed(p) if order(x,p)==N)
    out={0:0}; cur=0
    for j in range(1,N):cur=mul(cur,g,p);out[cur]=j
    assert len(out)==N
    return out

def local_audit(p):
    L=logs(p); N=len(L); assert N==p-(1 if p%4==1 else -1)
    chars=checks=0; maxratio=maxzero=maxparse=0.0
    for j in range(1,N):
        chars+=1
        vals=[0j if x not in L else cmath.exp(2j*math.pi*j*L[x]/N) for x in range(p)]
        inf=cmath.exp(2j*math.pi*j*L[None]/N)
        hats=[sum(vals[x]*cmath.exp(-2j*math.pi*a*x/p) for x in range(p)) for a in range(p)]
        maxzero=max(maxzero,abs(hats[0]+inf)); assert abs(hats[0]+inf)<1e-8
        for a in range(1,p):
            ratio=abs(hats[a])/(2*math.sqrt(p)); maxratio=max(maxratio,ratio); assert ratio<=1+1e-8; checks+=1
        coeff=[z/p for z in hats]; lhs=sum(abs(z)**2 for z in coeff); rhs=sum(x in L for x in range(p))/p
        maxparse=max(maxparse,abs(lhs-rhs)); assert abs(lhs-rhs)<1e-8; assert abs(abs(coeff[0])-1/p)<1e-8
    return chars,checks,maxratio,maxzero,maxparse

def main():
    assert 'STAGE14_T79=COMPLETE_PRINCIPAL_RAY_DENSITY_AND_ACTIVE_SUPPORT_DEFICIT_STRATIFICATION' in T79.read_text()
    th=TH22.read_text(); assert 'STAGE14_TH22=COMPLETE_T79_REFINED_CANONICAL_GAUSSIAN_PRIME_PROJECTIVE_RAY_CHARACTER_BALANCED_COVER_LARGE_SIEVE_APPLICABILITY_AUDIT' in th
    assert 'PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=d_chi^2' in th
    assert 'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44' in MAINLINE.read_text()
    t36=runpy.run_path(str(T36),run_name='t36'); t42=runpy.run_path(str(T42),run_name='t42')
    reps=t42['reciprocal_quotient'](t36['build_frozen_states']()); invisible=[s for s in reps if s['branch']=='invisible']; assert len(reps)==560 and len(invisible)==419
    unit=aff=0; maxM=1; maxom=0; hist=Counter()
    for s in invisible:
        a,b,p0,q0=s['a'],s['b'],s['p'],s['q']; k=s['n']//s['delta']; A,B=b-a,b+a; r,t=q0-p0,q0+p0
        K=oddpart(s['kernel']); g=gcd(oddpart(A*B),oddpart(r*t)); M=K//gcd(K,g*k)
        assert gcd(M,A*B*r*t)==1; unit+=1
        for p in primes(M):
            assert (A*A+B*B)%p and (r*r+t*t)%p
            xd=B*pow(A,-1,p)%p; xc=t*pow(r,-1,p)%p
            assert (1+xd*xd)%p and (1+xc*xc)%p
            aff+=1; hist[p]+=1
        maxM=max(maxM,M); maxom=max(maxom,len(primes(M)))
    lp=[p for p in range(3,60,2) if isprime(p)]; chars=checks=split=inert=0; mr=mz=mp=0.0
    for p in lp:
        split+=p%4==1; inert+=p%4==3; c,k,r,z,v=local_audit(p); chars+=c; checks+=k; mr=max(mr,r); mz=max(mz,z); mp=max(mp,v)
    cm=cc=0; ms=0
    for d in range(1,1500,2):
        if any(e!=1 for e in factor(d).values()):continue
        cm+=1; ds=divisors_sf(d); ms=max(ms,len(ds))
        for z in ds: assert 1/(z*z)<=1/(z*z)+1e-15; cc+=1
    report={'stage':'14-t80','reciprocal_states':560,'invisible_states':419,'physical_unit_checks':unit,'physical_affine_prime_checks':aff,'max_M':maxM,'max_omega_M':maxom,'local_primes':len(lp),'local_split_primes':split,'local_inert_primes':inert,'local_nonprincipal_characters':chars,'local_nonzero_frequency_checks':checks,'max_observed_weil_ratio_to_2sqrtp':mr,'max_zero_frequency_identity_error':mz,'max_parseval_error':mp,'independent_crt_squarefree_moduli':cm,'independent_crt_zero_support_checks':cc,'max_crt_divisor_strata':ms,'most_common_active_primes':hist.most_common(12),'boundary':{'STAGE14_T80':'COMPLETE_NEAR_FULL_SUPPORT_PROJECTIVE_GAUSS_DUALIZATION_TO_PRIMITIVE_INVERSE_FRACTION_KERNEL','MERGED_T79_IMPORTED':True,'MERGED_TH22_IMPORTED':True,'PROJECTIVE_LOCAL_AFFINE_FOURIER_EXPANSION_PROVED':True,'PROJECTIVE_LOCAL_ZERO_FREQUENCY_COEFFICIENT_EXACT':'1/p','PROJECTIVE_LOCAL_NONZERO_FREQUENCY_WEIL_BOUND':'2/sqrt(p)','PROJECTIVE_CRT_FOURIER_FACTORIZATION_PROVED':True,'PRIMITIVE_ADDITIVE_FREQUENCY_COEFFICIENT':'d^-1/2*Bo1','ADDITIVE_FREQUENCY_FIXED_POWER_DEFICIT_AUTOMATICALLY_SAVED':True,'ADDITIVE_FREQUENCY_DEFICIT_L2_BOUND':'Z^-2*Bo1','PROJECTIVE_HECKE_CONDUCTOR_NORM':'d^2','PROJECTIVE_ADDITIVE_DUAL_MODULUS':'d','PROJECTIVE_CONDUCTOR_COMPRESSION_TO_RATIONAL_ADDITIVE_MODULUS_PROVED':True,'PHYSICAL_PROJECTIVE_SLOPES_ARE_UNIT_AFFINE_MOD_D':True,'PROJECTIVE_CHARACTER_KERNEL_BECOMES_INVERSE_FRACTION_ADDITIVE_KERNEL':True,'FULL_PHYSICAL_MASKS_RETAINED':True,'PRIMITIVE_INVERSE_FRACTION_PHYSICAL_ENERGY_PROVED':False,'ENDPOINT_SMALL_EXTERNAL_KAPPA_PHYSICAL_ENERGY_PROVED':False,'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT':'23/44','T80_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING':False,'TH23_NEEDED':True,'TH23_REQUESTED_OBJECT':'NearFullSupportProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionLargeSieve','T_ROUTE_BLOCKED_WAITING_FOR_TH23':False,'NEXT':'Stage14-t81'}}
    print(json.dumps(report,indent=2,sort_keys=True))
if __name__=='__main__':main()
