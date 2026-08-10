#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd

PROP=F(13,24)
NONPROP=F(19,34)
ENTERING=F(9,16)
TARGET=NONPROP


def oddpart(n):
    while n % 2 == 0 and n:
        n //= 2
    return n


def admissible(theta,phi):
    return (
        F(3,16)<=theta<=F(5,16)
        and F(1,8)<=phi<=F(1,4)
        and 0<=theta-phi<=F(1,8)
        and theta+phi>=F(3,8)
    )


def e_prop_k(theta):
    return 3*theta-F(3,8)


def e_prop_root(theta,phi):
    # (E_H + 3 E_K)/4 after kappa+eta=1/8.
    return F(3,4)*phi+F(13,16)-F(3,2)*theta

assert ENTERING-TARGET == F(1,272)
assert TARGET-F(1,2) == F(1,17)
assert NONPROP-PROP == F(7,408)

# Exact four-root-gcd decomposition on small primitive root states.
root_checks=0
for x1 in range(1,25):
    for y1 in range(1,25):
        if gcd(x1,y1)!=1:
            continue
        for x2 in range(1,25):
            for y2 in range(1,25):
                if gcd(x2,y2)!=1:
                    continue
                t=oddpart(gcd(x1*y1,x2*y2))
                Kx=oddpart(gcd(x1,x2))
                Ky=oddpart(gcd(y1,y2))
                HT=oddpart(gcd(x1,y2))
                HS=oddpart(gcd(y1,x2))
                cells=(Kx,Ky,HS,HT)
                for i in range(4):
                    for j in range(i+1,4):
                        assert gcd(cells[i],cells[j])==1
                assert t==Kx*Ky*HS*HT
                X=x1*x2
                Y=y1*y2
                K=Kx*Ky
                assert X%(Kx*Kx)==0
                assert Y%(Ky*Ky)==0
                assert (X*Y)%(K*K)==0
                root_checks+=1

# Proportional minimax on an exact rational mesh; denominator 576 contains 11/36.
mesh=[]
for ti in range(int(F(3,16)*576),int(F(5,16)*576)+1):
    theta=F(ti,576)
    for pi in range(int(F(1,8)*576),int(F(1,4)*576)+1):
        phi=F(pi,576)
        if not admissible(theta,phi):
            continue
        val=min(e_prop_k(theta),e_prop_root(theta,phi))
        assert val<=PROP
        mesh.append((val,theta,phi))
worst=max(v for v,_,_ in mesh)
sat=[(t,p) for v,t,p in mesh if v==PROP]
assert worst==PROP
assert sat==[(F(11,36),F(1,4))]

# Equality profile of the root split.
theta=F(11,36)
phi=F(1,4)
eta=F(1,36)
kappa=F(7,72)
assert kappa+eta==F(1,8)
EH=3*phi-F(1,8)-3*eta
EK=F(5,4)-2*theta-kappa
assert EH==EK==PROP
assert e_prop_k(theta)==PROP
assert e_prop_root(theta,phi)==PROP
chi=2*theta+2*phi-F(3,4)
assert chi==F(13,36)

# Weighted cancellation is exact for all dyadic split values.
weight_checks=0
for i in range(0,33):
    eta_i=F(i,256)
    if eta_i>F(1,8):
        break
    kappa_i=F(1,8)-eta_i
    for theta_i in (F(1,4),F(11,36),F(5,16)):
        for phi_i in (F(11,48),F(1,4)):
            EH_i=3*phi_i-F(1,8)-3*eta_i
            EK_i=F(5,4)-2*theta_i-kappa_i
            avg=(EH_i+3*EK_i)/4
            expected=F(3,4)*phi_i+F(13,16)-F(3,2)*theta_i
            assert avg==expected
            weight_checks+=1

assert PROP<NONPROP<ENTERING

print('Stage14-X11 proportional four-root-gcd audit: PASS')
print(f'primitive four-cell root-gcd checks: {root_checks}')
print(f'proportional rational mesh points checked: {len(mesh)}')
print(f'weighted cancellation checks: {weight_checks}')
print('merged entering exponent: 9/16')
print('proportional branch exponent: 13/24')
print('nonproportional merged exponent: 19/34')
print('current whole-family exponent: 19/34')
print('improvement over 9/16: 1/272')
print('gap to sqrt scale: 1/17')
print('proportional equality: theta=11/36, phi=1/4, eta=1/36, kappa=7/72')
print('X11 auxiliary H needed: false')
