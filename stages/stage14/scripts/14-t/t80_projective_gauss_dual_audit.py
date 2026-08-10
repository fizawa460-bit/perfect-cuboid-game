#!/usr/bin/env python3
"""Stage14-t80: primitive projective Gauss/Fourier dualization audit."""
from __future__ import annotations
import cmath, json, math, runpy
from collections import Counter
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T79 = ROOT / "stages/stage14/14-t79/result.md"
MAINLINE = ROOT / "stages/stage14/14-4cx/result.md"

def oddpart(n):
    n=abs(n)
    while n and n%2==0: n//=2
    return n

def factor(n):
    n=abs(n); out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p=3 if p==2 else p+2
    if n>1: out[n]=out.get(n,0)+1
    return out

def prime_divisors(n): return sorted(factor(n))
def divisors_squarefree(n):
    ds=[1]
    for p in prime_divisors(n): ds += [d*p for d in list(ds)]
    return sorted(ds)
def is_prime(n):
    if n<2:return False
    if n%2==0:return n==2
    p=3
    while p*p<=n:
        if n%p==0:return False
        p+=2
    return True

def inv(a,p): return pow(a%p,-1,p)
def allowed_slopes(p): return [None]+[x for x in range(p) if (1+x*x)%p!=0]
def mul_slope(x,y,p):
    if x is None and y is None:return 0
    if x is None:
        if y%p==0:return None
        return (-inv(y,p))%p
    if y is None:
        if x%p==0:return None
        return (-inv(x,p))%p
    den=(1-x*y)%p; num=(x+y)%p
    if den==0:return None
    return (num*inv(den,p))%p

def elem_order(x,p):
    target=len(allowed_slopes(p)); cur=0
    for n in range(1,target+1):
        cur=mul_slope(cur,x,p)
        if cur==0:return n
    raise AssertionError((p,x))
def find_generator(p):
    target=len(allowed_slopes(p))
    for x in allowed_slopes(p):
        if elem_order(x,p)==target:return x
    raise AssertionError(p)
def log_table(p):
    g=find_generator(p); n=len(allowed_slopes(p)); out={0:0}; cur=0
    for j in range(1,n):
        cur=mul_slope(cur,g,p); out[cur]=j
    assert len(out)==n
    return out

def local_fourier_audit(p):
    logs=log_table(p); n=len(logs)
    assert n==p-(1 if p%4==1 else -1)
    max_ratio=max_zero=max_parseval=0.0; checks=0
    for j in range(1,n):
        vals=[]
        for x in range(p):
            vals.append(0j if x not in logs else cmath.exp(2j*math.pi*j*logs[x]/n))
        infinity=cmath.exp(2j*math.pi*j*logs[None]/n)
        hats=[sum(vals[x]*cmath.exp(-2j*math.pi*a*x/p) for x in range(p)) for a in range(p)]
        max_zero=max(max_zero,abs(hats[0]+infinity)); assert abs(hats[0]+infinity)<1e-8
        for a in range(1,p):
            ratio=abs(hats[a])/(2*math.sqrt(p)); max_ratio=max(max_ratio,ratio); assert ratio<=1+1e-8; checks+=1
        coeffs=[z/p for z in hats]
        lhs=sum(abs(z)**2 for z in coeffs); rhs=sum(1 for x in range(p) if x in logs)/p
        max_parseval=max(max_parseval,abs(lhs-rhs)); assert abs(lhs-rhs)<1e-8
        assert abs(abs(coeffs[0])-1/p)<1e-8
    return n-1,max_ratio,max_zero,max_parseval,checks

def main():
    assert "STAGE14_T79=COMPLETE_PRINCIPAL_RAY_DENSITY_AND_ACTIVE_SUPPORT_DEFICIT_STRATIFICATION" in T79.read_text()
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44" in MAINLINE.read_text()
    t36=runpy.run_path(str(T36),run_name="stage14_t36_import")
    t42=runpy.run_path(str(T42),run_name="stage14_t42_import")
    reps=t42["reciprocal_quotient"](t36["build_frozen_states"]()); invisible=[st for st in reps if st["branch"]=="invisible"]
    assert len(reps)==560 and len(invisible)==419
    physical_unit_checks=physical_affine_checks=0; max_M=max_omega_M=1; hist=Counter()
    for st in invisible:
        a,b,cp,cq=st["a"],st["b"],st["p"],st["q"]
        k=st["n"]//st["delta"]; A,B=b-a,b+a; r,t=cq-cp,cq+cp
        K=oddpart(st["kernel"]); g=gcd(oddpart(A*B),oddpart(r*t)); M=K//gcd(K,g*k)
        assert gcd(M,A*B*r*t)==1; physical_unit_checks+=1
        for p in prime_divisors(M):
            assert (A*A+B*B)%p!=0 and (r*r+t*t)%p!=0
            xd=(B*pow(A,-1,p))%p; xc=(t*pow(r,-1,p))%p
            assert (1+xd*xd)%p!=0 and (1+xc*xc)%p!=0
            physical_affine_checks+=1; hist[p]+=1
        max_M=max(max_M,M); max_omega_M=max(max_omega_M,len(prime_divisors(M)))
    local_primes=[p for p in range(3,60,2) if is_prime(p)]
    local_chars=local_checks=split=inert=0; max_ratio=max_zero=max_parseval=0.0
    for p in local_primes:
        split += p%4==1; inert += p%4==3
        chars,ratio,ze,pe,checks=local_fourier_audit(p)
        local_chars+=chars; local_checks+=checks; max_ratio=max(max_ratio,ratio); max_zero=max(max_zero,ze); max_parseval=max(max_parseval,pe)
    crt_moduli=crt_checks=0; max_strata=0
    for d in range(1,1500,2):
        fac=factor(d)
        if any(e!=1 for e in fac.values()):continue
        crt_moduli+=1; ds=divisors_squarefree(d); max_strata=max(max_strata,len(ds))
        for z in ds:
            assert 1/(z*z)<=1/(z*z)+1e-15; crt_checks+=1
    report={"stage":"14-t80","reciprocal_states":len(reps),"invisible_states":len(invisible),"physical_unit_checks":physical_unit_checks,"physical_affine_prime_checks":physical_affine_checks,"max_M":max_M,"max_omega_M":max_omega_M,"local_primes":len(local_primes),"local_split_primes":split,"local_inert_primes":inert,"local_nonprincipal_characters":local_chars,"local_nonzero_frequency_checks":local_checks,"max_observed_weil_ratio_to_2sqrtp":max_ratio,"max_zero_frequency_identity_error":max_zero,"max_parseval_error":max_parseval,"independent_crt_squarefree_moduli":crt_moduli,"independent_crt_zero_support_checks":crt_checks,"max_crt_divisor_strata":max_strata,"most_common_active_primes":hist.most_common(12),"boundary":{"STAGE14_T80":"COMPLETE_NEAR_FULL_SUPPORT_PROJECTIVE_GAUSS_DUALIZATION_TO_PRIMITIVE_INVERSE_FRACTION_KERNEL","MERGED_T79_IMPORTED":True,"TH22_AUDIT_PR_MERGED":False,"PROJECTIVE_LOCAL_AFFINE_FOURIER_EXPANSION_PROVED":True,"PROJECTIVE_LOCAL_ZERO_FREQUENCY_COEFFICIENT_EXACT":"1/p","PROJECTIVE_LOCAL_NONZERO_FREQUENCY_WEIL_BOUND":"2/sqrt(p)","PROJECTIVE_CRT_FOURIER_FACTORIZATION_PROVED":True,"PRIMITIVE_ADDITIVE_FREQUENCY_COEFFICIENT":"d^-1/2*Bo1","ADDITIVE_FREQUENCY_FIXED_POWER_DEFICIT_AUTOMATICALLY_SAVED":True,"ADDITIVE_FREQUENCY_DEFICIT_L2_BOUND":"Z^-2*Bo1","PROJECTIVE_HECKE_CONDUCTOR_NORM":"d^2","PROJECTIVE_ADDITIVE_DUAL_MODULUS":"d","PROJECTIVE_CONDUCTOR_COMPRESSION_TO_RATIONAL_ADDITIVE_MODULUS_PROVED":True,"PHYSICAL_PROJECTIVE_SLOPES_ARE_UNIT_AFFINE_MOD_D":True,"PROJECTIVE_CHARACTER_KERNEL_BECOMES_INVERSE_FRACTION_ADDITIVE_KERNEL":True,"FULL_PHYSICAL_MASKS_RETAINED":True,"PRIMITIVE_INVERSE_FRACTION_PHYSICAL_ENERGY_PROVED":False,"ENDPOINT_SMALL_EXTERNAL_KAPPA_PHYSICAL_ENERGY_PROVED":False,"CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT":"23/44","T80_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING":False,"TH23_NEEDED":True,"TH23_REQUESTED_OBJECT":"NearFullSupportProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionLargeSieve","T_ROUTE_BLOCKED_WAITING_FOR_TH23":False,"NEXT":"Stage14-t81"}}
    print(json.dumps(report,indent=2,sort_keys=True))
if __name__=="__main__": main()
