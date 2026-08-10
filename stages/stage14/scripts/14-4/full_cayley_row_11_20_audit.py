#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def crt2(a, m, b, n):
    assert gcd(m,n)==1
    return (a + m*(((b-a)*pow(m,-1,n))%n))%(m*n)


def strip_ok(theta,phi):
    return (
        F(3,16)<=theta<=F(5,16)
        and F(1,8)<=phi<=F(1,4)
        and 0<=theta-phi<=F(1,8)
        and theta+phi>=F(3,8)
    )


def check_nested_row_column_crt():
    # J carries both row/column signs; extra Cayley-row factors live outside J.
    Jmm,Jmp,Jpm,Jpp=5,13,17,29
    extra_m,extra_p=37,41
    vals=(Jmm,Jmp,Jpm,Jpp,extra_m,extra_p)
    for i in range(len(vals)):
        for k in range(i):
            assert gcd(vals[i],vals[k])==1
    J=Jmm*Jmp*Jpm*Jpp
    JLm,JLp=Jmm*Jpm,Jmp*Jpp
    JCm,JCp=Jmm*Jmp,Jpm*Jpp
    Cm=JCm*extra_m
    Cp=JCp*extra_p
    Cc=Cm*Cp
    assert Cc%J==0 and Cc>J

    hm,hp=3,7
    Lm,Lp=JLm*hm,JLp*hp
    assert Lm%JLm==0 and Lp%JLp==0
    Az=(Lp+Lm)//2
    Bz=(Lp-Lm)//2
    assert 2*Az==Lp+Lm and 2*Bz==Lp-Lm

    # Column fixes endpoint values and therefore M; full row then fixes N modulo Cc.
    M=123456789
    N0=crt2(M%Cm,Cm,(-M)%Cp,Cp)
    assert (N0-M)%Cm==0
    assert (N0+M)%Cp==0
    assert 0<=N0<Cc
    # Restricting the row to J would leave a weaker residue class.
    NJ=crt2(M%JCm,JCm,(-M)%JCp,JCp)
    assert (N0-NJ)%J==0


def case_bounds(theta,phi):
    # Full-Cayley-row weighted bounds after eliminating a.
    GA=(12*phi-6*theta+F(5,2))/7  # row lift zero, 4:3
    GB=(4*phi-4*theta+F(7,4))/3   # row lift positive, 2:1
    Es=max(2*theta,1-2*theta)
    Ek=3*theta-F(1,4)
    return Es,Ek,GA,GB,min(Es,Ek,max(GA,GB))


def check_whole_strip():
    D=1360  # divisible by 16, 40 and 4
    target=F(11,20)
    best=F(-10)
    eq=set()
    for nt in range(3*D//16,5*D//16+1):
        theta=F(nt,D)
        for np in range(D//8,D//4+1):
            phi=F(np,D)
            if not strip_ok(theta,phi):
                continue
            *_,E=case_bounds(theta,phi)
            if E>best:
                best=E; eq={(theta,phi)}
            elif E==best:
                eq.add((theta,phi))
    assert best==target,(best,eq)
    assert eq=={(F(11,40),F(1,4))},eq


def check_equality_profile():
    theta=F(11,40); phi=F(1,4)
    chi=2*theta+2*phi-F(3,4)
    d=chi-F(1,4)
    a=F(1,40); b=F(0)
    rho=2*a
    j=chi-4*a-2*b
    cy=chi-2*a-2*b
    col=F(1,4)-j
    row=max(F(0),F(1,4)-cy)
    EH=3*phi-F(1,8)-3*a-3*b
    EFR=2*phi+col+row
    Es=2*theta
    Ek=3*theta-F(1,4)
    GA=(12*phi-6*theta+F(5,2))/7
    GB=(4*phi-4*theta+F(7,4))/3

    assert chi==F(3,10)
    assert d==F(1,20)
    assert rho==F(1,20)
    assert j==F(1,5)
    assert cy==F(1,4)
    assert col==F(1,20)
    assert row==0
    assert EH==EFR==Es==GA==GB==F(11,20)
    assert Ek==F(23,40)
    assert F(19,34)-F(11,20)==F(3,340)
    assert F(11,20)-F(1,2)==F(1,20)
    assert F(13,24)<F(11,20)


def check_predecessors():
    x11=(ROOT/'stages/stage14/14-X11/result.md').read_text()
    s36=(ROOT/'stages/stage14/14-s7-36/result.md').read_text()
    s35=(ROOT/'stages/stage14/14-s7-35/result.md').read_text()
    cv=(ROOT/'stages/stage14/14-4cv/result.md').read_text()
    cu=(ROOT/'stages/stage14/14-4cu/result.md').read_text()

    for tok in [
        'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34',
        'PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=13/24',
    ]:
        assert tok in x11,tok
    assert 'NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34' in s36
    assert 'XI_EXTRA_GCD_DIVIDES_ENDPOINT_OMEGA_PRODUCT=true' in s35
    assert 'E_RC <= 2phi+1/2-2j' in cv
    assert 'C/C_Cayley | B^o(1)*H^2' in cu


def check_boundary():
    out=(ROOT/'stages/stage14/14-4cw/result.md').read_text()
    for tok in [
        'STAGE14_4CW=COMPLETE_FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_RECONSTRUCTION_AND_11_20_PROMOTION',
        'FULL_CAYLEY_GOOD_CORE_ROW_REUSED_AFTER_COLUMN_M_RECONSTRUCTION=true',
        'FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false',
        'NONPROPORTIONAL_CASE_A_WEIGHTED_COMBINATION=4:3',
        'NONPROPORTIONAL_CASE_B_WEIGHTED_COMBINATION=2:1',
        'NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=11/20',
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20',
        'IMPROVEMENT_OVER_MERGED_X11_19_34=3/340',
        'ELEVEN_TWENTIETHS_FULL_ROW_N_LIFT_EXPONENT=0',
        'REMAINING_RECEIVER=ElevenTwentiethsFullCayleyRowUniqueNLinearShortCofactorIncidence',
        'MAINLINE_H_NEEDED=false',
        'NEXT=Stage14-4cx',
    ]:
        assert tok in out,tok


def main():
    check_nested_row_column_crt()
    check_whole_strip()
    check_equality_profile()
    check_predecessors()
    check_boundary()
    print('Stage14-4cw audit: OK')
    print('CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20')
    print('UNIQUE_SATURATION=theta=11/40,phi=1/4')
    print('FULL_ROW_N_LIFT_EXPONENT=0')


if __name__=='__main__':
    main()
