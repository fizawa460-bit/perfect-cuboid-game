#!/usr/bin/env python3
from __future__ import annotations

import json, math, subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09AV/tunnell-actual-receiver-coordinate-specialization-preflight.json'
AU=ROOT/'stages/stage36/36-09AU/even-transposed-redei-stage36-equivalence-close-preflight.json'
AD=ROOT/'stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json'
AN=ROOT/'stages/stage36/36-09AN/retained-open-tunnell-necessary-gate-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='d43db1874b0e657143fa07b1a16eb87fc27e0238'
AUDITED_HEAD='9aa2e4c06240bbf1f6260dd2c11c3d622119f16f'
AUDIT_REVIEW=5128229756
AUDITED_CI='34085000175/101627220799'
CERT_BLOB='a64689ae6f8683c4d4b66e4f67a24f58624150f5'
AU_BLOB='ae4572d4131464a8aca83d39e2faefbd4ffec18e'
AD_BLOB='9d0388845955efee71d1a761ae4ee943d8b565d5'
AN_BLOB='76c55e89505b081c487749f4d7ab4d80e9d38a1f'

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
    x=sf(n)
    return x//2 if x%2==0 else x

def main():
    assert blob(CERT)==CERT_BLOB
    assert blob(AU)==AU_BLOB and blob(AD)==AD_BLOB and blob(AN)==AN_BLOB
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    assert c['audited_parent']['hostile_audit_review']==AUDIT_REVIEW
    assert c['audited_parent']['audited_exact_head']==AUDITED_HEAD
    assert c['audited_parent']['exact_head_ci']==AUDITED_CI
    assert c['audited_parent']['merged_main_sha']==BASE

    tested=0
    for U in range(1,45):
      for V in range(1,45):
        if U==V or math.gcd(U,V)!=1: continue
        if v2(U)%2 or v2(V)%2: continue
        A=odd_sf(U); B=odd_sf(V); C=odd_sf(U-V); D=odd_sf(U+V)
        g=(v2(U-V)+v2(U+V))&1
        N=(2**g)*A*B*C*D
        Q=abs(U*V*(U*U-V*V))
        assert N==sf(Q)
        W2=Q//N; W=math.isqrt(W2); assert W*W==W2
        if U>V:
            x=Fraction(N*U,V); y=Fraction(N*N*W,V*V)
        else:
            x=Fraction(N*V,U); y=Fraction(N*N*W,U*U)
        assert y*y==x*x*x-N*N*x
        assert x>N and y!=0
        tested+=1
    assert tested>200

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V84_36_09AV_CANDIDATE'
    assert st['status']=='ACTIVE_BATCHING_SUBSTANTIVE_PR'
    assert st['audited_history']['36-09AP-AU']['hostile_audit_review']==AUDIT_REVIEW
    av=st['authority_frontier']['36-09AV']
    assert av['ACTUAL_COORDINATE_TWIST_FORMULA']==True
    assert av['EXPLICIT_NON2TORSION_POINT']==True
    assert av['TUNNELL_NEW_FILTER_AFTER_ACTUAL_COORDINATE']==False
    assert av['TUNNELL_BRANCH_PREFILTER_BEFORE_REALIZATION']==True
    assert av['P_ONLY_TUNNELL_GATE']==False
    assert av['CANDIDATE_PARAMETER_SET_SHRUNK']==False
    assert av['RECEIVER_CLOSED']==False
    assert st['current']['unit']=='36-09AW'
    assert st['current']['36_09AW_entry_allowed']==True
    assert st['claims']['receiver_emptiness_proved']==False
    print(f'36-09AV verified on {tested} primitive U/V samples plus exact algebraic identities: N=sf(|UV(U^2-V^2)|), explicit non-2-torsion E_N(Q) point; Tunnell is automatic after actual coordinate realization and remains only a pre-realization branch sieve.')
if __name__=='__main__': main()
