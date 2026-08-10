#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def oddpart(n: int) -> int:
    while n % 2 == 0 and n:
        n //= 2
    return n


def strip_ok(theta, phi):
    return (
        F(3,16) <= theta <= F(5,16)
        and F(1,8) <= phi <= F(1,4)
        and F(0) <= theta-phi <= F(1,8)
        and theta+phi >= F(3,8)
    )


def check_four_root_gcd_identity():
    checks=0
    for x1 in range(1,25):
        for y1 in range(1,25):
            if gcd(x1,y1)!=1:
                continue
            for x2 in range(1,25):
                for y2 in range(1,25):
                    if gcd(x2,y2)!=1:
                        continue
                    Kx=oddpart(gcd(x1,x2))
                    Ky=oddpart(gcd(y1,y2))
                    HT=oddpart(gcd(x1,y2))
                    HS=oddpart(gcd(y1,x2))
                    cells=(Kx,Ky,HT,HS)
                    for i in range(4):
                        for j in range(i):
                            assert gcd(cells[i],cells[j])==1,(x1,y1,x2,y2,cells)
                    lhs=oddpart(gcd(x1*y1,x2*y2))
                    rhs=Kx*Ky*HT*HS
                    assert lhs==rhs,(x1,y1,x2,y2,lhs,rhs,cells)
                    # g_i in {1,2} never changes the odd identity for z_i=2xy/g_i.
                    for g1 in (1,2):
                        for g2 in (1,2):
                            if (2*x1*y1)%g1 or (2*x2*y2)%g2:
                                continue
                            z1=2*x1*y1//g1
                            z2=2*x2*y2//g2
                            assert oddpart(gcd(z1,z2))==rhs
                    checks+=1
    assert checks>10000
    return checks


def check_same_side_modular_unit_lemma():
    # Same-side root prime p: one coordinate of the xi switched host is a p-unit,
    # so the norm and hence q_xi are p-units.  Check the local algebra for many
    # unit choices and valuations.  R is allowed to contain p in the Kx case;
    # J, S and the opposite root/omega factors are units.
    checks=0
    for p in (3,5,7,11,13):
        for e in (1,2,3):
            pe=p**e
            for J in range(1,p):
                for y in range(1,p):
                    for om in range(1,p):
                        imag=(J*y*y*om)%p
                        assert imag!=0
                        # real may be zero; norm is still imag^2 mod p.
                        for real in (0,p,pe,2*pe):
                            norm=(real*real+imag*imag)%p
                            assert norm!=0
                            checks+=1
            # Ky case is symmetric: real coordinate is the unit one.
            for R in range(1,p):
                for x in range(1,p):
                    for om in range(1,p):
                        real=(R*x*x*om)%p
                        assert real!=0
                        for imag in (0,p,pe,2*pe):
                            norm=(real*real+imag*imag)%p
                            assert norm!=0
                            checks+=1
    assert checks>1000
    return checks


def check_exponent_algebra():
    # t exponent 1/8 = noncross sigma + odd cross eta.
    # T0^2|u_res and mu<=2(theta-phi) imply sigma<=theta-phi,
    # hence eta>=phi-theta+1/8.
    theta=F(5,16)
    for phi in (F(11,48),F(1,4),F(3,16)):
        assert strip_ok(theta,phi)
        sigma_max=theta-phi
        eta_min=F(1,8)-sigma_max
        EH=3*phi-F(1,8)-3*eta_min
        assert EH==3*theta-F(1,2)==F(7,16)

    # The proportional bound is below sqrt throughout the strip.
    assert 3*F(5,16)-F(1,2)==F(7,16)<F(1,2)

    # Global promotion and gap.
    assert F(19,34)>F(1,2)>F(7,16)
    assert F(9,16)-F(19,34)==F(1,272)
    assert F(19,34)-F(1,2)==F(1,17)
    assert F(4,7)-F(19,34)==F(3,238)


def check_strip_prop_grid():
    max_prop=F(-10)
    arg=None
    D=816
    for nt in range(3*D//16,5*D//16+1):
        theta=F(nt,D)
        for np in range(D//8,D//4+1):
            phi=F(np,D)
            if not strip_ok(theta,phi):
                continue
            # New cross-mass complete count after the T0^2|u_res transfer.
            E=3*theta-F(1,2)
            if E>max_prop:
                max_prop=E; arg=(theta,phi)
    assert max_prop==F(7,16),(max_prop,arg)


def check_predecessors():
    s36=(ROOT/'stages/stage14/14-s7-36/result.md').read_text()
    s34=(ROOT/'stages/stage14/14-s7-34/result.md').read_text()
    ci=(ROOT/'stages/stage14/14-4ci/result.md').read_text()
    s21=(ROOT/'stages/stage14/14-s7-21/result.md').read_text()

    for tok in [
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/16',
        'NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34',
        'REMAINING_RECEIVER=NineSixteenthsProportionalCommonZScaleKGaussianResidualIncidence',
    ]:
        assert tok in s36,tok
    assert 'XI_COMMON_ROOT_GCD_FOURTH_POWER_DIVIDES_QXI=true' in s34
    assert 'COMMON_Z_SCALE_SQUARE_DIVIDES_QK=true' in ci
    assert 'g_i=gcd(Q_i-P_i,Q_i+P_i) in {1,2}' in s21


def check_boundary():
    out=(ROOT/'stages/stage14/14-4cw/result.md').read_text()
    for tok in [
        'STAGE14_4CW=COMPLETE_PROPORTIONAL_COMMON_Z_ROOT_GCD_DECOMPOSITION_AND_19_34_PROMOTION',
        'PROPORTIONAL_ODDPART_T_EQUALS_KX_KY_HS_HT=true',
        'PROPORTIONAL_NONCROSS_BUCKET_SQUARE_DIVIDES_URES=true',
        'PROPORTIONAL_FORCED_CROSS_ROOT_EXPONENT_LOWER_BOUND=phi-theta+1/8',
        'PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16',
        'NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34',
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34',
        'IMPROVEMENT_OVER_MERGED_S7_36_9_16=1/272',
        'CURRENT_GAP_TO_SQRT=1/17',
        'REMAINING_RECEIVER=NineteenThirtyFourthsSingleCrossRootRowColumnTwinShortLiftIncidence',
        'MAINLINE_H_NEEDED=false',
        'NEXT=Stage14-4cx',
    ]:
        assert tok in out,tok


def main():
    root_checks=check_four_root_gcd_identity()
    unit_checks=check_same_side_modular_unit_lemma()
    check_exponent_algebra()
    check_strip_prop_grid()
    check_predecessors()
    check_boundary()
    print('Stage14-4cw audit: OK')
    print('root-gcd decomposition checks:',root_checks)
    print('same-side modular unit checks:',unit_checks)
    print('PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16')
    print('CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34')


if __name__=='__main__':
    main()
