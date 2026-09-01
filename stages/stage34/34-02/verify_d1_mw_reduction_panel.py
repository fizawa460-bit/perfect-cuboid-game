#!/usr/bin/env python3
"""Exact Stage34-02 D1 Mordell-Weil reduction panel.

For each audited Paper-C fiber and p in {107,109,113,127}, define

  rho_p : Z^r x Z/4 x Z/2 -> E_q(F_p)

using the exact audited free basis and torsion generators

  R=(q,q(q+1)),  ord(R)=4,  2R=(0,0),
  S=(-1,0),       ord(S)=2.

The d=1,2 split-cover condition is tested on the reduction of the resulting
point.  For rank one the four prime conditions are combined by generalized CRT
on the free coefficient while preserving the same rational torsion labels.
For rank two the per-prime coefficient maps are committed by canonical hashes;
no global closure is inferred from finite residue survival.
"""

from fractions import Fraction
from math import gcd, isqrt, lcm
import hashlib
import json

PANEL = [107,109,113,127]

FIBERS = {
    "20/21": {"a":20,"b":21,"basis":[("-45/49","10/343")]},
    "80/39": {"a":80,"b":39,"basis":[("-160/39","1760/1521")]},
    "24/7": {"a":24,"b":7,"basis":[("-75/7","510/49")]},
    "84/13": {"a":84,"b":13,"basis":[("17787/169","216678/169")]},
    "48/55": {"a":48,"b":55,"basis":[("-24/25","24/275")]},
    "20/99": {"a":20,"b":99,"basis":[("-20/27","980/2673")]},
    "60/11": {"a":60,"b":11,"basis":[("-180/11","7020/121"),("-300/11","5100/121")]},
}

EXPECTED_RANK1 = {
 "20/21":{"1":[2464,144,"cb1538a5386fe9d58ef830b5b776ccbf02f67c7600747f6e6fd58bef6933ee52"],"2":[2464,48,"98354cfd88e88d6cf7751e139df8c945b05d696456bd1f76a43da4bd0af6f0ce"]},
 "80/39":{"1":[1680,16,"8d418433176de4d4151ba0ca3f3850ddd9c321474db557a0d360151441321c9e"],"2":[1680,144,"aeebbe5a6016fd8c9c0d568af7ca436ffcf198e0759f20ea9effe465c8f1bbfc"]},
 "24/7":{"1":[3120,200,"ef6e62e52fe86ad6b6e35276cf1361734325fbe9907acacb8f3dbd5ce1b648cb"],"2":[3120,72,"706c1e4a309907ec6cc2d53bbd033bbf94c887faa16ee21c05c5636b26ea5f90"]},
 "84/13":{"1":[420,8,"ae144f7b97cc2432212b47ac664af960dcb142b6f653ab8dc63f1f000afafdc5"],"2":[420,136,"b13932534ffc524ae8952e240729f46f9de7e1a423f8ef547c2afe104877c74e"]},
 "48/55":{"1":[16320,480,"e94fac6d56ea2c1442ac97b0628e8d165262459ffb826fc602c9494388273a94"],"2":[16320,1248,"436c2fd19a2cedf59e6ac751333d0456cb4a1fb85e291ac9c2dabb045f95b48e"]},
 "20/99":{"1":[672,48,"aacac47b6aab316bb254bffab1182612dddf7baae96228d28939d54ffbdba759"],"2":[672,8,"ad7483de084c064f404945fcc316013c5863736db7a80aad661e782622df23b1"]}
}

EXPECTED_RANK2 = {
 "107":{"1":[60,12,1728,"38bb4858c1072bf50a167aad4e611862005fb3cbde96cdbf18a8fff67f928aff"],"2":[60,12,960,"7ecad53237ddef80205b9904f0bfe4fe8d5ce60f94cfbdf2f65baae8588f6f6f"]},
 "109":{"1":[28,28,448,"8b909aa2d5dc41fece3f3fd9cc1773648010ef30855bf3034c72567f873fed5b"],"2":[28,28,448,"d0016d3c39ff3368246d82af81e72d550dcbe592d5f0e2728a85dc36248e466e"]},
 "113":{"1":[56,8,1280,"f8cf424b90b3822c90a501b4440b68e9f437e79a64406fa69a0271746ea68ec7"],"2":[56,8,1280,"f8cf424b90b3822c90a501b4440b68e9f437e79a64406fa69a0271746ea68ec7"]},
 "127":{"1":[64,64,10240,"2ce0206bd6020da4749f2c603216ebe136f3b54a4c468a5294a0b2d1aae7ac5c"],"2":[64,64,10240,"2ce0206bd6020da4749f2c603216ebe136f3b54a4c468a5294a0b2d1aae7ac5c"]}
}


def inv(a,p): return pow(a%p,-1,p)
def red(s,p):
    f=Fraction(s)
    return f.numerator%p*inv(f.denominator,p)%p

def neg(P,p): return None if P is None else (P[0],(-P[1])%p)

def add(P,Q,a2,a4,p):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and (y1+y2)%p==0: return None
    if P==Q:
        if y1%p==0: return None
        m=(3*x1*x1+2*a2*x1+a4)*inv(2*y1,p)%p
    else:
        m=(y2-y1)*inv(x2-x1,p)%p
    x3=(m*m-a2-x1-x2)%p
    y3=(-y1+m*(x1-x3))%p
    return (x3,y3)

def mul(P,n,a2,a4,p):
    if n<0: return mul(neg(P,p),-n,a2,a4,p)
    R=None; Q=P
    while n:
        if n&1: R=add(R,Q,a2,a4,p)
        Q=add(Q,Q,a2,a4,p); n//=2
    return R

def order(P,a2,a4,p):
    if P is None: return 1
    R=None
    for n in range(1,p+2+2*isqrt(p)+20):
        R=add(R,P,a2,a4,p)
        if R is None: return n
    raise RuntimeError("order not found")

def square(v,p):
    v%=p
    return v==0 or pow(v,(p-1)//2,p)==1

def torsion(r,s,R,S,a2,a4,p):
    return add(mul(R,r,a2,a4,p),mul(S,s,a2,a4,p),a2,a4,p)

def canonical_hash(rows):
    rows=sorted([list(x) for x in rows])
    return hashlib.sha256(json.dumps(rows,separators=(",",":")).encode()).hexdigest()

def allowed_point(Q,a,b,q,d,p):
    dinv=inv(d,p)
    if Q is None:
        A=b*b%p
        B=b*b*(a*a+b*b)%p
    else:
        x,_=Q
        A=(x*x+q*q)%p
        B=((1+q*q)*x*x+4*q*q*x+q*q*(1+q*q))%p
    return square(A*dinv,p) and square(B*dinv,p)

def crt(a,m,b,n):
    g=gcd(m,n)
    if (b-a)%g: return None
    mm=m//g; nn=n//g
    t=((b-a)//g*inv(mm,nn))%nn
    return (a+m*t)%lcm(m,n), lcm(m,n)

def setup(name,p):
    f=FIBERS[name]; a=f["a"]; b=f["b"]
    assert (2*a*b*(a*a-b*b)*(a*a+b*b))%p != 0
    q=a%p*inv(b,p)%p
    a2=(1+q*q)%p; a4=q*q%p
    basis=[(red(x,p),red(y,p)) for x,y in f["basis"]]
    R=(q,q*(q+1)%p); S=(-1%p,0)
    assert order(R,a2,a4,p)==4 and mul(R,2,a2,a4,p)==(0,0)
    assert order(S,a2,a4,p)==2
    tors={torsion(r,s,R,S,a2,a4,p) for r in range(4) for s in range(2)}
    assert len(tors)==8
    return a,b,q,a2,a4,basis,R,S

# Rank-one exact four-prime CRT panels.
for name in [x for x in FIBERS if x!="60/11"]:
    for d in (1,2):
        states=None; M=1
        for p in PANEL:
            a,b,q,a2,a4,basis,R,S=setup(name,p)
            P=basis[0]; m=order(P,a2,a4,p)
            local=set()
            for n in range(m):
                nP=mul(P,n,a2,a4,p)
                for r in range(4):
                    for s in range(2):
                        Q=add(nP,torsion(r,s,R,S,a2,a4,p),a2,a4,p)
                        if allowed_point(Q,a,b,q,d,p): local.add((n,r,s))
            if states is None:
                states=local; M=m
            else:
                new=set()
                for n0,r,s in states:
                    for n1,r1,s1 in local:
                        if (r,s)!=(r1,s1): continue
                        c=crt(n0,M,n1,m)
                        if c is not None: new.add((c[0],r,s))
                states=new; M=lcm(M,m)
        exp=EXPECTED_RANK1[name][str(d)]
        got=[M,len(states),canonical_hash(states)]
        assert got==exp, (name,d,got,exp)
        print(f"PASS rank1 {name} d={d}: modulus={M} states={len(states)} sha={got[2]}")

# Rank-two exact per-prime maps.  We commit the full coefficient-residue sets by hash.
name="60/11"
for p in PANEL:
    a,b,q,a2,a4,basis,R,S=setup(name,p)
    G1,G2=basis; m1=order(G1,a2,a4,p); m2=order(G2,a2,a4,p)
    M1=[mul(G1,i,a2,a4,p) for i in range(m1)]
    M2=[mul(G2,j,a2,a4,p) for j in range(m2)]
    for d in (1,2):
        local=set()
        for i in range(m1):
            for j in range(m2):
                Q0=add(M1[i],M2[j],a2,a4,p)
                for r in range(4):
                    for s in range(2):
                        Q=add(Q0,torsion(r,s,R,S,a2,a4,p),a2,a4,p)
                        if allowed_point(Q,a,b,q,d,p): local.add((i,j,r,s))
        exp=EXPECTED_RANK2[str(p)][str(d)]
        got=[m1,m2,len(local),canonical_hash(local)]
        assert got==exp, (p,d,got,exp)
        print(f"PASS rank2 p={p} d={d}: mods=({m1},{m2}) states={len(local)} sha={got[3]}")

print("PASS exact D1 MW reduction panel; finite residue survival remains and grants no global closure")
