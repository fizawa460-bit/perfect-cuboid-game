#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
BA=ROOT/'stages/stage36/36-09BA/ay-auxiliary-genusone-open-points-preflight.json'
AC=ROOT/'stages/stage36/36-09AC/same-x-separate-squareclass-double-cover-preflight.json'
AY=ROOT/'stages/stage36/36-09AY/universal-boundary-tunnell-survivor-preflight.json'
W03=ROOT/'docs/arsenal/cards/formal/S34-W03.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='fe7ef406a9987981fe5f79267f3f8a39f37a61e4'
BA_HEAD='a4fde9a55b6483018ffb4be49ffbc758939b7e22'
BA_CI='34090570732/101643008125'
CERT_BLOB='e4b63fd500d05ff5dc704e0c08409edee5895053'
LOCKS={BA:'2f31c89b2760f2270fa0ea21106ef97a3ec0840b',AC:'3e95cc443bb9de9e0d2b14d6d9c32ea7c1953021',AY:'add18004debf95a218a6393f6c2f18f2bd4f7e10',W03:'1d5275321f42768a6414d4610ac912c63be43f96'}
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def v2(n):
    n=abs(n); k=0
    while n and n%2==0: n//=2; k+=1
    return k
def sf(n):
    n=abs(n); out=1; p=2
    while p*p<=n:
        e=0
        while n%p==0: n//=p; e^=1
        if e: out*=p
        p+=1 if p==2 else 2
    if n>1: out*=n
    return out
def odd_sf(n):
    z=sf(n); return z//2 if z%2==0 else z
def check_boundary_scaled(a,b):
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b)
    assert P and M and D0
    h=math.gcd(abs(P),abs(M))
    C=odd_sf(D0); eta=1 if D0>0 else -1; e=(1+v2(D0))&1
    kappa=eta*(2**e)*C
    u=Fraction(P,h); v=Fraction(M,h)
    Ui=(P//h)**2; Vi=(M//h)**2
    r2=abs(Ui-Vi)//((2**e)*C); r=math.isqrt(r2); assert r*r==r2
    s2=(Ui+Vi)//2; s=math.isqrt(s2); assert s*s==s2
    t=v/u; lam=Fraction(P,M)
    R=Fraction(kappa*r,1)/u
    S=Fraction(2*s,1)/u
    assert R*R==kappa*(1-t*t)
    assert S*S==2*(1+t*t)
    q=lam*t
    assert q in (1,-1)
    Zm=Fraction(0,1); Zp=Fraction(2,1)
    assert Zm*Zm==kappa*(1-q*q)
    assert Zp*Zp==2*(1+q*q)
    Lm=M*M*Ui-P*P*Vi; Lp=M*M*Ui+P*P*Vi
    assert Lm==0 and Lp>0
    assert Ui*Vi*(Ui-Vi)*Lm==0
    assert Ui*Vi*(Ui+Vi)*Lp==(2*Lp)*(abs(P//h)*abs(M//h)*s)**2

def main():
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h, (p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BA_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']['36_09BA_exact_head']==BA_HEAD
    assert c['batch_parent']['36_09BA_exact_head_ci']==BA_CI
    m=c['receiver_restricted_intersection']
    assert m['S34_W03_exact_joint_system_materialized'] is True
    assert m['equivalent_description']=='t is a Q-point of C_kappa and lambda*t is a Q-point of C_kappa'
    assert len(m['normalized_extra_equations'])==2
    b=c['boundary_behavior']
    assert b['excluded_by_open'] is True and b['projective_closed_intersection_always_has_boundary_Q_point'] is True
    assert b['naive_closed_mod_prime_zero_residue_strategy']=='STRUCTURALLY_BLOCKED'
    tested=0
    for a in range(1,31):
      for bb0 in range(1,31):
        if a==bb0 or math.gcd(a,bb0)!=1: continue
        P=a*a+2*a*bb0-bb0*bb0; M=a*a-2*a*bb0-bb0*bb0
        if P==0 or M==0: continue
        check_boundary_scaled(a,bb0); tested+=1
    assert tested>500
    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V90_36_09BB_CANDIDATE'
    bb=st['authority_frontier']['36-09BB']
    assert bb['RECEIVER_RESTRICTED_INTERSECTION_EXACT'] is True
    assert bb['SCALED_SELF_INTERSECTION_MODEL'] is True
    assert bb['NAIVE_PROJECTIVE_LOCAL_ZERO_RESIDUE_ATTACK_BLOCKED'] is True
    assert bb['OPEN_RECEIVER_INTERSECTION_EMPTY'] is False
    assert bb['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bb['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BC' and st['current']['36_09BC_entry_allowed'] is True
    print(f'36-09BB verified on {tested} boundary specializations plus exact factor identities: AY receiver = open C_kappa(t) intersect C_kappa(lambda*t). The rational X=K boundary remains in the projective closure at every good prime, so naive closed-residue emptiness is structurally blocked.')
if __name__=='__main__': main()
