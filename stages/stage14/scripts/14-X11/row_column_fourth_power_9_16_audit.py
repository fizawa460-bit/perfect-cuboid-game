#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations
from math import gcd

TARGET=F(9,16)
NONPROP=F(19,34)
ENTERING=F(4,7)


def chi(theta,phi):
    return 2*theta+2*phi-F(3,4)


def e_s(theta):
    return max(2*theta,1-2*theta)


def e_k(theta):
    return 3*theta-F(1,4)


def e_np_weight(theta,phi):
    return (18*phi-12*theta+5)/11


def admissible(theta,phi):
    return (
        F(3,16)<=theta<=F(5,16)
        and F(1,8)<=phi<=F(1,4)
        and 0<=theta-phi<=F(1,8)
        and theta+phi>=F(3,8)
    )


def crt_pair(a,m,b,n):
    assert gcd(m,n)==1
    k=((b-a)*pow(m,-1,n))%n
    return (a+m*k)%(m*n)

assert ENTERING-TARGET == F(1,112)
assert TARGET-F(1,2) == F(1,16)
assert NONPROP < TARGET

# Nonproportional equality profile.
th=F(19,68)
ph=F(1,4)
a=F(3,136)
b=F(0)
rho=2*a
ch=chi(th,ph)
j=F(15,68)
short=F(1,34)
EH=3*ph-F(1,8)-3*(a+b)
ERC=2*ph+F(1,2)-2*ch+8*a+4*b
assert ch==F(21,68)
assert rho==F(3,68)
assert j==ch-4*a-2*b
assert F(1,4)-j==short
assert EH==ERC==NONPROP
assert 2*th==NONPROP

# Exact 8:3 cancellation identity.
weighted_checks=0
for ai in range(0,9):
    for bi in range(0,ai+1):
        aa=F(ai,256)
        bb=F(bi,256)
        theta=F(9,32)
        phi=F(1,4)
        c=chi(theta,phi)
        eh=3*phi-F(1,8)-3*(aa+bb)
        erc=2*phi+F(1,2)-2*c+8*aa+4*bb
        lhs=(8*eh+3*erc)/11
        rhs=(18*phi-12*theta+5)/11-F(12,11)*bb
        assert lhs==rhs
        assert lhs<=(18*phi-12*theta+5)/11
        weighted_checks+=1

# Whole-strip exact rational mesh for nonproportional envelope.
mesh=[]
for ti in range(int(F(3,16)*816),int(F(5,16)*816)+1):
    theta=F(ti,816)
    for pi in range(int(F(1,8)*816),int(F(1,4)*816)+1):
        phi=F(pi,816)
        if not admissible(theta,phi):
            continue
        val=min(e_s(theta),e_k(theta),e_np_weight(theta,phi))
        assert val<=NONPROP
        mesh.append((val,theta,phi))
worst=max(v for v,_,_ in mesh)
sat=[(t,p) for v,t,p in mesh if v==NONPROP]
assert worst==NONPROP
assert sat==[(F(19,68),F(1,4))]

# Proportional branch and localization.
assert 3*F(5,16)-F(3,8)==TARGET
phi0=F(47,192)
a0=F(1,64)
b0=F(0)
ch0=chi(F(5,16),phi0)
j0=F(29,96)
EH0=3*phi0-F(1,8)-3*(a0+b0)
Erow0=F(1,2)+4*a0+2*b0
assert j0==ch0-4*a0-2*b0
assert EH0==Erow0==TARGET
assert (12*phi0+1)/7==TARGET

prop_weight_checks=0
for pi in range(44,49):
    phi=F(pi,192)
    for ai in range(0,9):
        for bi in range(0,ai+1):
            aa=F(ai,256)
            bb=F(bi,256)
            eh=3*phi-F(1,8)-3*(aa+bb)
            erow=F(1,2)+4*aa+2*bb
            lhs=(4*eh+3*erow)/7
            rhs=(12*phi+1)/7-F(6,7)*bb
            assert lhs==rhs
            assert lhs<=(12*phi+1)/7
            prop_weight_checks+=1

assert (12*F(47,192)+1)/7==TARGET
assert (12*F(11,48)+1)/7<TARGET

# Synthetic 2x2 row/column / CRT algebra guard.
primes=(3,5,7,11)
crt_checks=0
for cells in permutations(primes):
    jmm,jmp,jpm,jpp=cells
    JCm=jmm*jmp
    JCp=jpm*jpp
    JLm=jmm*jpm
    JLp=jmp*jpp
    J=JCm*JCp
    assert J==JLm*JLp
    assert gcd(JCm,JCp)==1
    assert gcd(JLm,JLp)==1
    for hm,hp in [(-3,2),(-1,4),(1,2),(3,4)]:
        Lm=JLm*hm
        Lp=JLp*hp
        assert abs(hm*hp)==abs(Lm*Lp)//J
        M=17
        N0=crt_pair(M%JCm,JCm,(-M)%JCp,JCp)
        assert (N0-M)%JCm==0
        assert (N0+M)%JCp==0
        for hN in range(-2,3):
            N=N0+J*hN
            assert (N-M)%JCm==0
            assert (N+M)%JCp==0
            crt_checks+=1

print('Stage14-X11 fourth-power row/column 9/16 audit: PASS')
print(f'nonproportional mesh points checked: {len(mesh)}')
print(f'8:3 cancellation checks: {weighted_checks}')
print(f'proportional 4:3 localization checks: {prop_weight_checks}')
print(f'synthetic row/column CRT checks: {crt_checks}')
print('entering merged exponent: 4/7')
print('nonproportional exponent: 19/34')
print('proportional exponent: 9/16')
print('current whole-family exponent: 9/16')
print('improvement over 4/7: 1/112')
print('gap to sqrt scale: 1/16')
print('nonproportional equality: theta=19/68, phi=1/4, j=15/68')
print('potential proportional saturation: theta=5/16, 47/192<=phi<=1/4, L_-=0')
print('X11 auxiliary H needed: false')
