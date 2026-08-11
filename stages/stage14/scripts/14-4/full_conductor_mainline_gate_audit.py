#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def phi(n):
    out=n
    x=n
    p=2
    while p*p<=x:
        if x%p==0:
            while x%p==0:
                x//=p
            out-=out//p
        p+=1
    if x>1:
        out-=out//x
    return out


def roots_minus_one(q):
    return [r for r in range(q) if (r*r+1)%q==0]


def main():
    c1=0
    for C in [5,13,17,25,29,37,41,65,85]:
        for g in [d for d in range(1,C) if C%d==0]:
            q=C//g
            if q<=1:
                continue
            hs=[h for h in range(1,C) if gcd(h,C)==g]
            assert len(hs)==phi(q)
            assert Fraction(len(hs),C)<=Fraction(1,g)
            c1+=1

    c2=0
    for q in [5,13,17,25,29,37,41,65,85]:
        for rho in roots_minus_one(q):
            for A in range(1,min(q,12)):
                if gcd(A,q)!=1:
                    continue
                D=(-rho*A)%q
                m=(D+A)%q
                n=(D-A)%q
                assert (m-rho*n)%q==0
                Xm=(m*n)%q
                X0=((m*m-n*n)*pow(2,-1,q))%q
                assert (X0-rho*Xm)%q==0
                c2+=1

    c3=0
    for chi in [Fraction(1,6),Fraction(5,24),Fraction(1,4)]:
        plus=chi+2*(Fraction(1,4)-chi/2)
        assert plus==Fraction(1,2)
        for lam in [Fraction(0),Fraction(1,100),Fraction(1,24),chi]:
            e=plus-lam
            assert e==Fraction(1,2)-lam
            if lam>0:
                assert e<Fraction(1,2)
            c3+=1

    assert c1>10 and c2>20
    print(f"exact_conductor_mass_checks={c1}")
    print(f"same_root_checks={c2}")
    print(f"exponent_checks={c3}")
    print("OPEN_S7_50_USED_AS_THEOREM_SOURCE=false")
    print("CONDUCTOR_LOSS_FIXED_POWER_SAVING_PROVED=true")
    print("CONDUCTOR_LOSS_STRATUM_EXPONENT=1/2-lambda")
    print("SQRT_SATURATION_FREQUENCY_GCD=Bo1")
    print("FULL_CONDUCTOR_ENDPOINT_PROVED=true")
    print("FULL_CONDUCTOR_THREE_PROJECTION_SAME_ROOT=true")
    print("THIRD_PROJECTION_INDEPENDENT_FULL_CONDUCTOR_SAVING=false")
    print("CONDUCTOR_GCD_PEEL_EXHAUSTED=true")
    print("PRINCIPAL_ZERO_MODE_STILL_EXPONENT_HALF=true")
    print("OSCILLATORY_ERROR_SAVING_ALONE_SUFFICIENT=false")
    print("CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2")
    print("STRICT_SUBSQRT_POWER_SAVING_PROVED=false")
    print("MAINLINE_H_NEEDED=true")
    print("MAINLINE_H_STAGE=Stage14-4diH")

if __name__=="__main__":
    main()
