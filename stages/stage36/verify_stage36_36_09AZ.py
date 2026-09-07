#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09AZ/boundary-survivor-open-refinement-preflight.json'
AY=ROOT/'stages/stage36/36-09AY/universal-boundary-tunnell-survivor-preflight.json'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
AC=ROOT/'stages/stage36/36-09AC/same-x-separate-squareclass-double-cover-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='b7a045b7c910a3e01d3826556cd71019af15418f'
AUDITED_HEAD='c09f264e4becbc4c7f06145b32ce366b2d4d7a4f'
AUDIT_REVIEW=5128446584
AUDITED_CI='34087344920/101633809000'
CERT_BLOB='0ad33f6d197525978f716a146bb128ac343c0710'
AY_BLOB='add18004debf95a218a6393f6c2f18f2bd4f7e10'
AE_BLOB='ddae37dd35cd0e732cebadf9c17f3f3fa57930df'
AC_BLOB='3e95cc443bb9de9e0d2b14d6d9c32ea7c1953021'
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def check_boundary(a:int,b:int):
    P=a*a+2*a*b-b*b
    M=a*a-2*a*b-b*b
    assert P and M
    h=math.gcd(abs(P),abs(M))
    assert h==(2 if a%2 and b%2 else 1)
    P0=P//h; M0=M//h
    assert math.gcd(abs(P0),abs(M0))==1
    U0=P0*P0; V0=M0*M0
    assert math.gcd(U0,V0)==1
    assert M*M*U0-P*P*V0==0
    # Exhaustively verify uniqueness in a box; the exact proof is the coprime divisibility argument source-locked in CERT.
    lim=max(U0,V0)+40
    hits=[]
    for U in range(1,lim+1):
      for V in range(1,lim+1):
        if math.gcd(U,V)!=1: continue
        if M*M*U==P*P*V: hits.append((U,V))
    assert hits==[(U0,V0)]
    return P,M,h,U0,V0

def main():
    assert blob(CERT)==CERT_BLOB
    assert blob(AY)==AY_BLOB and blob(AE)==AE_BLOB and blob(AC)==AC_BLOB
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    p=c['audited_parent']
    assert p['pr']==1683 and p['hostile_audit_review']==AUDIT_REVIEW
    assert p['audited_exact_head']==AUDITED_HEAD and p['exact_head_ci']==AUDITED_CI and p['merged_main_sha']==BASE
    tested=0
    for a in range(1,13):
      for b in range(1,13):
        if a==b or math.gcd(a,b)!=1: continue
        P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b
        if P==0 or M==0: continue
        check_boundary(a,b); tested+=1
    assert tested>70
    o=c['correct_open_refinement']
    assert o['open_inequality']=='M^2*A*u^2-P^2*B*v^2 != 0'
    assert o['branch_label_deletion_valid'] is False
    t=c['tunnell_limit']
    assert t['constant_on_squareclass_tuple'] is True and t['detects_open_inequality'] is False
    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V88_36_09AZ_CANDIDATE'
    assert st['status']=='ACTIVE_BATCHING_SUBSTANTIVE_PR'
    hist=st['audited_history']['36-09AV-AY']
    assert hist['pr']==1683 and hist['hostile_audit_review']==AUDIT_REVIEW and hist['merged_main_sha']==BASE
    az=st['authority_frontier']['36-09AZ']
    assert az['UNIQUE_PRIMITIVE_LMINUS_BOUNDARY'] is True
    assert az['COORDINATE_LEVEL_OPEN_REFINEMENT'] is True
    assert az['BRANCH_LABEL_DELETION_VALID'] is False
    assert az['TUNNELL_DETECTS_OPEN_INEQUALITY'] is False
    assert az['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and az['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BA' and st['current']['36_09BA_entry_allowed'] is True
    assert st['claims']['receiver_emptiness_proved'] is False
    print(f'36-09AZ verified on {tested} primitive parameter diagnostics plus exact coprime-divisibility proof interface: Lminus=0 has one primitive positive coordinate; open refinement is coordinate-level and Tunnell cannot delete the whole AY squareclass tuple.')
if __name__=='__main__': main()
