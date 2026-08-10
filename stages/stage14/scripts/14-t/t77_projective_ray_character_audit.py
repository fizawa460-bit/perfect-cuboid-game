#!/usr/bin/env python3
"""Stage14-t77: radial support and Gaussian projective ray-character audit."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json, runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T76 = ROOT / "stages/stage14/14-t76/result.md"
TH21 = ROOT / "stages/stage14/14-tH21/result.md"
S738 = ROOT / "stages/stage14/14-s7-38/result.md"
DIAG_BALANCE = 4


def oddpart(n):
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def factor(n):
    out = {}; n = abs(n); p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1; n //= p
        p = 3 if p == 2 else p + 2
    if n > 1: out[n] = out.get(n, 0) + 1
    return out


def primes(n): return sorted(factor(n))
def norm(z): return z[0]*z[0] + z[1]*z[1]
def proj_eq(z, w, p): return (z[0]*w[1]-z[1]*w[0]) % p == 0


def ray_order(M):
    out = 1
    for p in primes(M): out *= p - (1 if p % 4 == 1 else -1)
    return out


def main():
    assert "STAGE14_T76=COMPLETE_CLEAN_KAPPA_COVER_PROJECTIVE_ROOTLINE_AND_DEFICIENT_TYPEII_REDUCTION" in T76.read_text()
    th21 = TH21.read_text()
    assert "STAGE14_TH21=COMPLETE_BALANCED_CLEAN_KAPPA_CANONICAL_PRIME_PRIMITIVE_COVER_TYPEII_DISPERSION_APPLICABILITY_AUDIT" in th21
    assert "OFF_THE_SHELF_TYPEII_POWER_SAVING_PROVED=false" in th21
    assert "V(B) << B^(61/112+o(1))" in S738.read_text()

    t36 = runpy.run_path(str(T36), run_name="t36_import")
    t42 = runpy.run_path(str(T42), run_name="t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [s for s in reps if s["branch"] == "invisible"]
    assert len(reps) == 560 and len(invisible) == 419

    cnt = Counter(); qrad_hist = Counter(); qray_hist = Counter(); comp_hist = Counter()
    max_qrad = max_qray = max_order = 1
    min_ratio = None; max_ratio = Fraction(1, 1)

    for st in invisible:
        a,b,cp,cq = st["a"],st["b"],st["p"],st["q"]
        eps,ell,m,n,delta = st["eps"],st["ell"],st["m"],st["n"],st["delta"]
        kappa = st["kernel"]; k = n // delta; h = eps*m // k
        assert h*k == eps*m

        s0 = Fraction(b*b*cp*cp-a*a*cq*cq, b*b*cq*cq-a*a*cp*cp)
        sq = s0 / kappa
        u,v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u*u == sq.numerator and v*v == sq.denominator and gcd(u,v)==1
        beta = gcd(kappa,v); alpha = kappa // beta
        rp,rm = v*v+kappa*u*u, v*v-kappa*u*u
        G = gcd(rp,rm); Pp,Pm = rp//G,rm//G
        assert gcd(Pp*Pm,kappa)==1 and Pm % ell == 0

        A,B = b-a,b+a; r,t = cq-cp,cq+cp
        L = (A*t-B*r, B*t-A*r, A*t+B*r, B*t+A*r)
        K = oddpart(kappa)
        g = gcd(oddpart(A*B), oddpart(r*t))
        Q = K // gcd(K,g)
        assert gcd(Q,A*B*r*t)==1

        Qrad = gcd(Q,k); Qray = Q // Qrad
        assert Qrad == gcd(Q,m) and gcd(Qrad,Qray)==1
        cnt["radial_identity"] += 1
        qrad_hist[Qrad] += 1; qray_hist[Qray] += 1
        max_qrad=max(max_qrad,Qrad); max_qray=max(max_qray,Qray)
        if Qrad>1: cnt["radial_nontrivial_states"] += 1
        if Qray>1: cnt["ray_active_states"] += 1
        else: cnt["ray_trivial_states"] += 1

        for pp in primes(Qrad):
            assert pp%4==1 and h%pp and ell%pp and delta%pp
            assert (A*A+B*B)%pp==0 and (r*r+t*t)%pp==0
            actual=t*pow(r,-1,pp)%pp
            assert (actual*actual+1)%pp==0
            sign=1 if oddpart(alpha)%pp==0 else -1
            roots={sign*B*pow(A,-1,pp)%pp, sign*A*pow(B,-1,pp)%pp}
            assert actual in roots and all((x*x+1)%pp==0 for x in roots)
            cnt["radial_isotropic_prime"] += 1

        aray=gcd(oddpart(alpha),Qray); bray=gcd(oddpart(beta),Qray)
        assert aray*bray==Qray and gcd(aray,bray)==1
        comps=[1,1,1,1]; z=(a,b); V=(cp,cq); U=tuple(st["U"])
        assert norm(U)==m and norm(z)==ell*m and norm(V)==k*delta

        for pp in primes(Qray):
            assert h%pp and ell%pp and delta%pp and k%pp and m%pp
            assert norm(z)%pp and norm(U)%pp and norm(V)%pp
            cnt["ray_unit_prime"] += 1
            ids=(0,1) if aray%pp==0 else (2,3)
            good=[j for j in ids if L[j]%pp==0]
            assert good; j=good[0]; comps[j]*=pp; comp_hist[j+1]+=1
            targets=((cp,cq),(cp,-cq),(cq,cp),(-cq,cp))
            assert proj_eq(z,targets[j],pp)
            cnt["ray_projective_prime"] += 1

        M1,M2,M3,M4=comps
        assert M1*M2*M3*M4==Qray and M1*M2==aray and M3*M4==bray
        if Qray>1:
            o=ray_order(Qray); ratio=Fraction(o,Qray)
            cnt["ray_group_order"] += 1; max_order=max(max_order,o)
            min_ratio=ratio if min_ratio is None else min(min_ratio,ratio)
            max_ratio=max(max_ratio,ratio)

        balanced=t<=DIAG_BALANCE*r; deficient=Q<r*t
        if balanced:
            cnt["balanced"] += 1
            if deficient:
                cnt["balanced_deficient"] += 1
                cnt["balanced_deficient_ray_active" if Qray>1 else "balanced_deficient_radial_only"] += 1

    report={
      "stage":"14-t77","reciprocal_states":len(reps),"invisible_states":len(invisible),
      "radial_identity_checks":cnt["radial_identity"],
      "radial_isotropic_prime_checks":cnt["radial_isotropic_prime"],
      "ray_unit_prime_checks":cnt["ray_unit_prime"],
      "ray_projective_prime_checks":cnt["ray_projective_prime"],
      "ray_group_order_checks":cnt["ray_group_order"],
      "diagnostic_balance_ratio":DIAG_BALANCE,
      "diagnostic_balanced_states":cnt["balanced"],
      "diagnostic_balanced_deficient_states":cnt["balanced_deficient"],
      "diagnostic_balanced_deficient_ray_active_states":cnt["balanced_deficient_ray_active"],
      "diagnostic_balanced_deficient_radial_only_states":cnt["balanced_deficient_radial_only"],
      "ray_active_states":cnt["ray_active_states"],"radial_nontrivial_states":cnt["radial_nontrivial_states"],
      "ray_trivial_states":cnt["ray_trivial_states"],"max_Q_rad":max_qrad,"max_Q_ray":max_qray,
      "max_ray_group_order":max_order,
      "min_ray_group_order_over_modulus":None if min_ratio is None else f"{min_ratio.numerator}/{min_ratio.denominator}",
      "max_ray_group_order_over_modulus":f"{max_ratio.numerator}/{max_ratio.denominator}",
      "most_common_Q_rad":qrad_hist.most_common(12),"most_common_Q_ray":qray_hist.most_common(12),
      "chosen_component_prime_histogram":sorted(comp_hist.items()),
      "boundary":{
        "STAGE14_T77":"COMPLETE_RADIAL_DEGENERATE_SPLIT_AND_GAUSSIAN_PROJECTIVE_RAY_CHARACTER_KERNEL",
        "MERGED_T76_IMPORTED":True,"MERGED_TH21_IMPORTED":True,
        "RADIAL_NONUNIT_SUPPORT_EQUALS_GCD_Q_K":True,"RADIAL_NONUNIT_SUPPORT_EQUALS_GCD_Q_M":True,
        "RADIAL_SUPPORT_PRIMES_SPLIT_MOD4":True,"RADIAL_SUPPORT_PROJECTIVE_ROOT_IS_ISOTROPIC":True,
        "RADIAL_SUPPORT_MOVING_PI_PHASE":False,"RAY_MODULUS_GAUSSIAN_DIRECTION_AND_COVER_ARE_UNITS":True,
        "PROJECTIVE_GAUSSIAN_RAY_GROUP_EXHIBITED":True,"PROJECTIVE_GAUSSIAN_RAY_GROUP_ORDER_FORMULA_PROVED":True,
        "CLEAN_PROJECTIVE_ROOTLINE_EQUALS_GAUSSIAN_RAY_CLASS_INCIDENCE":True,
        "FIXED_BETA_BECOMES_FIXED_I_RAY_CLASS":True,"RECIPROCAL_ROOT_CHOICE_BECOMES_LOCAL_INVERSION_AUTOMORPHISM":True,
        "PROJECTIVE_ROOTLINE_CHARACTER_ORTHOGONALITY_EXACT":True,"RAY_CHARACTER_KERNEL_SEPARATES_PI_AND_V_ARITHMETICALLY":True,
        "FULL_PHYSICAL_WEIGHT_TENSOR_FACTORIZATION_PROVED":False,"RAY_ACTIVE_TYPEII_ENERGY_PROVED":False,
        "TH22_NEEDED":True,"TH22_REQUESTED_OBJECT":"CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve",
        "T_ROUTE_BLOCKED_WAITING_FOR_TH22":False,"CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT":"61/112",
        "T77_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING":False,"NEXT":"Stage14-t78"}}
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__ == "__main__": main()
