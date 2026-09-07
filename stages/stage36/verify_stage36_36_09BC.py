#!/usr/bin/env python3
from __future__ import annotations
import itertools, json, math, subprocess
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BC/boundary-neighborhood-open-local-no-loop-preflight.json'
SRC=ROOT/'stages/stage36/36-09BC/boundary-neighborhood-local-and-elliptic-quotient-source-lock.md'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
BBV=ROOT/'stages/stage36/verify_stage36_36_09BB.py'
AA=ROOT/'stages/stage36/36-09AA/receiver-coupled-same-x-twist-intersection-preflight.json'
AC=ROOT/'stages/stage36/36-09AC/same-x-separate-squareclass-double-cover-preflight.json'
CYCLE=ROOT/'docs/research-os/policies/cycle-exploration-safety-protocol.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='c52f88a671503ac9eb25c20186b4fb7729ba9112'
BB_HEAD='72441c82f2c146c63ebde6459b18789e33c6dddb'
BB_CI='34091603898'
CERT_BLOB='317638c4d1a76f683c7af9bdb4e8285af35f4d05'
SRC_BLOB='fccb0742e5e765243201a59c27d1b76a9d5e8f58'
LOCKS={BB:'e4b63fd500d05ff5dc704e0c08409edee5895053',BBV:'a3591e34aaaafcac0efb540d92622fe83136dc18',AA:'be447726a97158849c67ed6d57d6d3c35d6ba20f',AC:'3e95cc443bb9de9e0d2b14d6d9c32ea7c1953021',CYCLE:'4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37'}
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

def det4(m):
    total=Fraction(0,1)
    for perm in itertools.permutations(range(4)):
        inv=sum(1 for i in range(4) for j in range(i+1,4) if perm[i]>perm[j])
        term=Fraction(-1 if inv%2 else 1,1)
        for i in range(4): term*=m[i][perm[i]]
        total+=term
    return total

def boundary_data(a:int,b:int):
    assert a>0 and b>0 and a!=b and math.gcd(a,b)==1
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b)
    assert P and M and D0
    h=math.gcd(abs(P),abs(M))
    u=Fraction(P,h); v=Fraction(M,h)
    C=odd_sf(D0); eta=1 if D0>0 else -1; e=(1+v2(D0))&1
    kappa=Fraction(eta*(2**e)*C,1); lam=Fraction(P,M); t=Fraction(M,P)
    Ui=(P//h)**2; Vi=(M//h)**2
    r2=abs(Ui-Vi)//((2**e)*C); r=math.isqrt(r2); assert r*r==r2 and r>0
    s2=(Ui+Vi)//2; s=math.isqrt(s2); assert s*s==s2 and s>0
    R=kappa*r/u; S=Fraction(2*s,1)/u
    assert R*R==kappa*(1-t*t)
    assert S*S==2*(1+t*t)
    assert lam*t==1
    Zp=Fraction(2,1)
    J=[
      [2*R, 0, 2*kappa*t, 0],
      [0, 2*S, -4*t, 0],
      [0, 0, 2*kappa*lam*lam*t, 0],
      [0, 0, -4*lam*lam*t, 2*Zp],
    ]
    det=det4(J)
    expected=32*R*S*kappa*lam
    assert det==expected
    assert det/(R*S*kappa*lam)==32
    return kappa,lam,t,R,S,det

def quotient_identity(kappa:Fraction,lam:Fraction,t:Fraction):
    assert kappa and lam and t
    R2=kappa*(1-t*t)
    Zm2=kappa*(1-lam*lam*t*t)
    S2=2*(1+t*t)
    Zp2=2*(1+lam*lam*t*t)
    X=1/(t*t)
    Wm2=R2*Zm2/(kappa*kappa*t**6)
    Wp2=S2*Zp2/(4*t**6)
    assert Wm2==X*(X-1)*(X-lam*lam)
    assert Wp2==X*(X+1)*(X+lam*lam)

def main():
    assert blob(CERT)==CERT_BLOB and blob(SRC)==SRC_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BB_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    assert c['base_main_sha']==BASE
    assert c['audit_repair']['hostile_audit_review']==5128976664
    assert c['batch_parent']['36_09BB_exact_head']==BB_HEAD
    assert c['batch_parent']['36_09BB_exact_head_ci']==BB_CI
    g=c['good_prime_local_analysis']
    assert g['jacobian_minor_diagonal_factors']==['2*R0','2*S0','2*kappa*lambda','4']
    assert g['jacobian_minor_determinant']=='32*R0*S0*kappa*lambda'
    assert g['jacobian_minor_recomputed_by_verifier'] is True
    assert g['punctured_Qell_points_arbitrarily_close_to_boundary'] is True
    assert g['generic_good_prime_boundary_neighborhood_obstruction'] is False
    e=c['elliptic_quotient']
    assert e['new_filter_credit'] is False and e['cycle_status']=='DOMINATED_BY_AUDITED_SAME_X_RECEIVER'
    tested=0
    for a in range(1,35):
      for b in range(1,35):
        if a==b or math.gcd(a,b)!=1: continue
        P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b
        if P==0 or M==0: continue
        kappa,lam,t,R,S,det=boundary_data(a,b)
        quotient_identity(kappa,lam,Fraction(2,3) if lam*Fraction(2,3) not in (1,-1) else Fraction(3,4))
        tested+=1
    assert tested>650
    cp=c['cycle_protocol']
    assert cp['EXHAUSTIVE_VIEW_AUDIT_TRIGGERED'] is True and cp['BLIND_REDISCOVERY_REQUIRED'] is True
    st=json.loads(STATE.read_text())
    assert st['base_main_sha']==BASE
    assert st['freshness']['current_main']==BASE
    bc=st['authority_frontier']['36-09BC']
    assert bc['GOOD_PRIME_PUNCTURED_BOUNDARY_LOCAL_NONEMPTY'] is True
    assert bc['ELLIPTIC_QUOTIENT_NEW_FILTER'] is False
    assert bc['EXHAUSTIVE_VIEW_AUDIT_TRIGGERED'] is True
    assert bc['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bc['RECEIVER_CLOSED'] is False
    assert st['claims']['receiver_emptiness_proved'] is False
    print(f'36-09BC repaired and verified on {tested} retained parameter diagnostics: exact 4x4 Jacobian determinant recomputes to 32*R0*S0*kappa*lambda; good-prime punctured boundary local nonemptiness and no-loop quotient conclusions remain unchanged.')
if __name__=='__main__': main()
