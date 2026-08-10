#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def crt2(a, m, b, n):
    assert gcd(m, n) == 1
    return (a + m * (((b-a) * pow(m, -1, n)) % n)) % (m*n)


def check_2x2_algebra():
    jmm,jmp,jpm,jpp = 5,13,17,29
    cells=(jmm,jmp,jpm,jpp)
    for i in range(4):
        for k in range(i): assert gcd(cells[i],cells[k])==1
    J=jmm*jmp*jpm*jpp
    JCm,JCp=jmm*jmp,jpm*jpp
    JLm,JLp=jmm*jpm,jmp*jpp
    assert JCm*JCp==J and JLm*JLp==J
    hm,hp=3,7
    Lm,Lp=JLm*hm,JLp*hp
    assert (Lp+Lm)%2==0 and (Lp-Lm)%2==0
    Az,Bz=(Lp+Lm)//2,(Lp-Lm)//2
    assert Az-Bz==Lm and Az+Bz==Lp
    M=1234567
    n0=crt2(M%JCm,JCm,(-M)%JCp,JCp)
    assert (n0-M)%JCm==0 and (n0+M)%JCp==0
    for h in (-3,-1,0,2,5):
        N=n0+J*h
        assert (N-M)%JCm==0 and (N+M)%JCp==0


def strip_ok(t,p):
    return F(3,16)<=t<=F(5,16) and F(1,8)<=p<=F(1,4) and 0<=t-p<=F(1,8) and t+p>=F(3,8)


def complete_bounds(t,p,r):
    chi=2*t+2*p-F(3,4)
    Es=max(2*t,1-2*t)
    Ek=3*t-F(1,4)
    Ex=3*p-F(1,8)-r
    Erc=2*p+F(1,2)-2*chi+6*r
    return chi,Es,Ek,Ex,Erc,min(Es,Ek,Ex,Erc)


def check_symbolic():
    t,p,r=F(7,24),F(1,4),F(1,24)
    chi,Es,Ek,Ex,Erc,E=complete_bounds(t,p,r)
    assert chi==F(1,3)
    assert Es==Ex==Erc==E==F(7,12)
    assert Ek==F(5,8)
    j=chi-3*r
    assert j==F(5,24)
    assert F(1,4)-j==F(1,24)
    assert F(19,32)-F(7,12)==F(1,96)
    assert F(47,80)-F(7,12)==F(1,240)
    assert F(9,16)<F(7,12)
    weighted=(6*Ex+Erc)/7
    closed=(16*p-4*t+F(5,4))/7
    assert weighted==closed==F(7,12)
    d=max(F(0),chi-F(1,4))
    eta=F(0)
    assert d==F(1,12)==2*r+eta
    EH=3*p-F(1,8)-3*eta
    assert EH==F(5,8)>F(7,12)


def check_grid():
    target=F(7,12); max_seen=F(-1); eq=set()
    for it in range(144,241):
        t=F(it,768)
        for ip in range(96,193):
            p=F(ip,768)
            if not strip_ok(t,p): continue
            chi=2*t+2*p-F(3,4)
            r0=max(F(0),(chi-F(1,4))/3)
            local=F(-1); args=[]
            for ir in range(0,385):
                r=F(ir,1536)
                if r<r0: continue
                *_,E=complete_bounds(t,p,r)
                if E>local: local,args=E,[r]
                elif E==local: args.append(r)
            if local>max_seen:
                max_seen=local; eq={(t,p,r) for r in args}
            elif local==max_seen:
                eq|={(t,p,r) for r in args}
    assert max_seen==target,(max_seen,eq)
    assert eq=={(F(7,24),F(1,4),F(1,24))},eq


def check_predecessors():
    cu=(ROOT/'stages/stage14/14-4cu/result.md').read_text()
    s33=(ROOT/'stages/stage14/14-s7-33/result.md').read_text()
    s34=(ROOT/'stages/stage14/14-s7-34/result.md').read_text()
    s27=(ROOT/'stages/stage14/14-s7-27/result.md').read_text()
    for tok in ['CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/32','JOINT_CORE_DIVIDES_ENDPOINT_LINEAR_PRODUCT=true','PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16']:
        assert tok in cu,tok
    for tok in ['COMMON_CORE_ORIENTATION_DOUBLE_CHARGE_FORBIDDEN=true','STRONG_CANONICAL_ST_SPLIT_UNIVERSALLY_VALID=false']:
        assert tok in s33,tok
    for tok in ['CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=47/80','XI_COMMON_ROOT_GCD_FOURTH_POWER_DIVIDES_QXI=true']:
        assert tok in s34,tok
    assert 'oddpart(c_x^- c_x^+) = oddpart(u_res)' in s27
    assert 'oddpart(c_k^- c_k^+) = oddpart(v_res)' in s27


def check_boundary():
    out=(ROOT/'stages/stage14/14-4cv/result.md').read_text()
    for tok in [
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12',
        'IMPROVEMENT_OVER_PREVIOUS_19_32=1/96',
        'IMPROVEMENT_OVER_MERGED_S7_34_47_80=1/240',
        'SEVEN_TWELFTHS_SATURATION_THETA=7/24',
        'SEVEN_TWELFTHS_SATURATION_JOINT_CORE_EXPONENT=5/24',
        'SEVEN_TWELFTHS_EXTRA_RESIDUAL_GCD_EXPONENT=1/24',
        'STRONG_CANONICAL_ST_SPLIT_USED=false',
        'COMMON_CORE_ORIENTATION_DOUBLE_CHARGED=false',
        'MAINLINE_H_NEEDED=false',
        'NEXT=Stage14-4cw']:
        assert tok in out,tok


def main():
    check_2x2_algebra(); check_symbolic(); check_grid(); check_predecessors(); check_boundary()
    print('Stage14-4cv audit: OK')
    print('CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12')
    print('UNIQUE_GRID_SATURATION=theta=7/24,phi=1/4,rho=1/24')
    print('S7_34_COMPATIBILITY=eta=0,G_extra_exponent=1/24')

if __name__=='__main__': main()
