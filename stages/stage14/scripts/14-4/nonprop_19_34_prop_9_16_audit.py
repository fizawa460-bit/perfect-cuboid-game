#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def strip_ok(theta, phi):
    return (
        F(3,16) <= theta <= F(5,16)
        and F(1,8) <= phi <= F(1,4)
        and F(0) <= theta-phi <= F(1,8)
        and theta+phi >= F(3,8)
    )


def check_symbolic_nonprop_equality():
    theta=F(19,68)
    phi=F(1,4)
    chi=2*theta+2*phi-F(3,4)
    a=F(3,136)
    b=F(0)
    rho=2*a
    j=chi-4*a-2*b

    EH=3*phi-F(1,8)-3*(a+b)
    ERC=2*phi+F(1,2)-2*j
    Es=2*theta
    Ek=3*theta-F(1,4)
    weighted=(8*EH+3*ERC)/11

    assert strip_ok(theta,phi)
    assert chi==F(21,68)
    assert rho==F(3,68)
    assert j==F(15,68)
    assert F(1,4)-j==F(1,34)
    assert EH==ERC==Es==weighted==F(19,34)
    assert Ek==F(10,17)
    assert F(19,34) < F(9,16) < F(4,7)
    assert F(4,7)-F(9,16)==F(1,112)
    assert F(7,12)-F(9,16)==F(1,48)


def check_weighted_identity():
    # 8 E_H + 3 E_RC cancels the selected cross-root exponent a.
    # Coefficients before division by 11:
    # E_H  = 3phi-1/8-3a-3b
    # E_RC = 2phi+1/2-2chi+8a+4b
    assert 8*(-3)+3*8 == 0
    assert 8*(-3)+3*4 == -12
    assert 8*3+3*2 == 30
    assert 8*F(-1,8)+3*F(1,2) == F(1,2)
    # After chi=2theta+2phi-3/4:
    # 30phi+1/2-6chi = 18phi-12theta+5.
    theta=F(7,24); phi=F(1,4)
    chi=2*theta+2*phi-F(3,4)
    lhs=30*phi+F(1,2)-6*chi
    rhs=18*phi-12*theta+5
    assert lhs==rhs


def nonprop_closed(theta,phi):
    Es=max(2*theta,1-2*theta)
    Ek=3*theta-F(1,4)
    Ew=(18*phi-12*theta+5)/11
    return min(Es,Ek,Ew)


def check_nonprop_strip_grid():
    target=F(19,34)
    max_seen=F(-10)
    equality=set()
    D=3264  # divisible by 68, 48, 16, 4
    t0=int(F(3,16)*D); t1=int(F(5,16)*D)
    p0=int(F(1,8)*D); p1=int(F(1,4)*D)
    for it in range(t0,t1+1):
        theta=F(it,D)
        for ip in range(p0,p1+1):
            phi=F(ip,D)
            if not strip_ok(theta,phi):
                continue
            E=nonprop_closed(theta,phi)
            if E>max_seen:
                max_seen=E
                equality={(theta,phi)}
            elif E==max_seen:
                equality.add((theta,phi))
    assert max_seen==target,(max_seen,equality)
    assert equality=={(F(19,68),F(1,4))},equality


def check_piecewise_proof():
    # theta <= 1/4: k one-host count <=1/2.
    assert 3*F(1,4)-F(1,4)==F(1,2)<F(19,34)
    # 1/4 <= theta <=19/68: s count =2theta.
    assert 2*F(19,68)==F(19,34)
    # theta >=19/68: weighted bound at phi=1/4 decreases in theta.
    edge=(18*F(1,4)-12*F(19,68)+5)/11
    assert edge==F(19,34)


def check_proportional_barrier():
    # Merged 4cu proportional count: E_prop<=3theta-3/8.
    assert 3*F(5,16)-F(3,8)==F(9,16)
    assert 3*F(3,16)-F(3,8)==F(3,16)
    # Independent xi one-host count forces phi>=11/48 to reach 9/16.
    phi0=F(11,48)
    assert 3*phi0-F(1,8)==F(9,16)
    assert phi0>=F(3,16) and phi0<=F(1,4)


def check_predecessors():
    cv=(ROOT/'stages/stage14/14-4cv/result.md').read_text()
    s35=(ROOT/'stages/stage14/14-s7-35/result.md').read_text()
    cu=(ROOT/'stages/stage14/14-4cu/result.md').read_text()

    for tok in [
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12',
        'REMAINING_RECEIVER=SevenTwelfthsExtraResidualGcdRowColumnTwinShortCofactorIncidence',
    ]:
        assert tok in cv,tok
    for tok in [
        'STAGE14_S7_35=COMPLETE_EXTRA_XI_RESIDUAL_GCD_COLLAPSE_AND_4_7_PROMOTION',
        'XI_EXTRA_GCD_DIVIDES_ENDPOINT_OMEGA_PRODUCT=true',
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=4/7',
    ]:
        assert tok in s35,tok
    for tok in [
        'PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16',
        'JOINT_CORE_DIVIDES_ENDPOINT_LINEAR_PRODUCT=true',
    ]:
        assert tok in cu,tok


def check_boundary():
    out=(ROOT/'stages/stage14/14-4cw/result.md').read_text()
    for tok in [
        'STAGE14_4CW=COMPLETE_S7_35_ROW_COLUMN_COUPLING_NONPROPORTIONAL_19_34_AND_9_16_PROMOTION',
        'NONPROPORTIONAL_WEIGHTED_COMPLETE_COUNT_COMBINATION=8:3',
        'NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34',
        'PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16',
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/16',
        'IMPROVEMENT_OVER_MERGED_S7_35_4_7=1/112',
        'NINE_SIXTEENTHS_SATURATION_PHI_LOWER=11/48',
        'NINE_SIXTEENTHS_REQUIRES_L_MINUS_ZERO=true',
        'REMAINING_RECEIVER=NineSixteenthsProportionalEndpointScaleKResidualGaussianGcdIncidence',
        'MAINLINE_H_NEEDED=false',
        'NEXT=Stage14-4cx',
    ]:
        assert tok in out,tok


def main():
    check_symbolic_nonprop_equality()
    check_weighted_identity()
    check_nonprop_strip_grid()
    check_piecewise_proof()
    check_proportional_barrier()
    check_predecessors()
    check_boundary()
    print('Stage14-4cw audit: OK')
    print('NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34')
    print('PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16')
    print('CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/16')


if __name__=='__main__':
    main()
