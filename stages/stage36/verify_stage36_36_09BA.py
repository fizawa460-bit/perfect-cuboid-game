#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BA/ay-auxiliary-genusone-open-points-preflight.json'
SRC=ROOT/'stages/stage36/36-09BA/ay-genusone-trivialized-covering-source-lock.md'
AZ=ROOT/'stages/stage36/36-09AZ/boundary-survivor-open-refinement-preflight.json'
AY=ROOT/'stages/stage36/36-09AY/universal-boundary-tunnell-survivor-preflight.json'
AH=ROOT/'stages/stage36/36-09AH/common-uv-two-quadric-genusone-preflight.json'
AI=ROOT/'stages/stage36/36-09AI/j1728-congruent-number-jacobian-preflight.json'
AJ=ROOT/'stages/stage36/36-09AJ/congruent-number-full2-covering-class-preflight.json'
AN=ROOT/'stages/stage36/36-09AN/retained-open-tunnell-necessary-gate-preflight.json'
FULL2=ROOT/'stages/stage36/36-09AJ/full2-homogeneous-space-source-lock.md'
W03=ROOT/'docs/arsenal/cards/formal/S34-W03.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='b7a045b7c910a3e01d3826556cd71019af15418f'
AZ_HEAD='70d242588f4ae1b56dfc80e7c634e1f666ff57fd'
AZ_CI='34090057759/101641532269'
CERT_BLOB='2f31c89b2760f2270fa0ea21106ef97a3ec0840b'
SRC_BLOB='5af1fb1162662f8224b91c909e9ca6f946032675'
LOCKS={
 AZ:'0ad33f6d197525978f716a146bb128ac343c0710',
 AY:'add18004debf95a218a6393f6c2f18f2bd4f7e10',
 AH:'732431bef8dfafe25cbdeb005c4237d72a40ae4b',
 AI:'c5af6c4dde67532ea8d592e74aed187c72bbed4e',
 AJ:'27950f53a89e28d02d04f2c19628504561c206e7',
 AN:'76c55e89505b081c487749f4d7ab4d80e9d38a1f',
 FULL2:'cc16ef3a9ed5ca5d8924ddb9fd531197d68c2f0d',
 W03:'1d5275321f42768a6414d4610ac912c63be43f96',
}
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def v2(n):
    n=abs(n); k=0
    while n and n%2==0: n//=2; k+=1
    return k
def sf(n):
    n=abs(n); out=1; p=2
    while p*p<=n:
        parity=0
        while n%p==0: n//=p; parity^=1
        if parity: out*=p
        p+=1 if p==2 else 2
    if n>1: out*=n
    return out
def odd_sf(n):
    z=sf(n); return z//2 if z%2==0 else z
def check_ay_boundary(a,b):
    assert a>0 and b>0 and a!=b and math.gcd(a,b)==1
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b)
    assert P and M and D0
    h=math.gcd(abs(P),abs(M)); assert h==(2 if a%2 and b%2 else 1)
    u=abs(P)//h; v=abs(M)//h
    U=u*u; V=v*v
    assert U-V==8*D0//(h*h)
    C=odd_sf(D0); eta=1 if D0>0 else -1
    e=(1+v2(D0))&1; f=1
    r2=abs(U-V)//((2**e)*C); r=math.isqrt(r2); assert r*r==r2 and r>0
    s2=(U+V)//2; s=math.isqrt(s2); assert s*s==s2 and s>0
    assert U-V==eta*(2**e)*C*r*r
    assert U+V==2*s*s
    # AJ / AN raw full-2 covering constants for A=B=D=1.
    c=eta*(2**e)*C; d=2
    L=c*d; T=c*d
    D1=c*d; D2=c*c*d; D3=c*d*d
    assert D1*u*u-D2*r*r==T*v*v
    assert D1*u*u-D3*s*s==-T*v*v
    x=Fraction(D1*u*u,v*v)
    y=Fraction(L*L*u*r*s,v*v*v)
    assert y*y==x*(x-T)*(x+T)
    assert y!=0 and x not in (0,T,-T)
    # Boundary is excluded only by original Lminus condition, not by genus-one coordinates.
    assert M*M*U-P*P*V==0
    return C,eta,e,T,x,y

def main():
    assert blob(CERT)==CERT_BLOB and blob(SRC)==SRC_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h, (p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',AZ_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    assert c['batch_parent']['pr']==1686
    assert c['AY_branch']['smooth_genus_one'] is True and c['AY_branch']['full2_two_covering'] is True
    assert c['boundary_rational_point']['AN_image_y_nonzero'] is True
    q=c['positive_rank_and_infinitude']
    assert q['AN_torsion_group']=='Z/2 x Z/2'
    assert q['boundary_image_infinite_order'] is True
    assert q['rank_E_n_Q_at_least']==1 and q['C_AY_Q_infinite'] is True
    n=c['nonboundary_auxiliary_points']
    assert n['AZ_unique_positive_primitive_Lminus_boundary_coordinate'] is True
    assert n['boundary_Q_lifts_finite'] is True and n['there_exist_infinitely_many_C_AY_Q_points_with_Lminus_nonzero'] is True
    f=c['receiver_intersection_firewall']
    assert f['auxiliary_C_AY_open_point_implies_top_receiver'] is False
    assert f['receiver_intersection_classified'] is False
    assert f['S34_W03_applicability'].startswith('MATCHED')
    tested=0
    for a in range(1,31):
      for b in range(1,31):
        if a==b or math.gcd(a,b)!=1: continue
        P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b
        if P==0 or M==0: continue
        check_ay_boundary(a,b); tested+=1
    assert tested>500
    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V89_36_09BA_CANDIDATE'
    ba=st['authority_frontier']['36-09BA']
    assert ba['AY_AUXILIARY_OPEN_Q_POINTS_INFINITE'] is True
    assert ba['BOUNDARY_ONLY_AUXILIARY_CLOSURE_IMPOSSIBLE'] is True
    assert ba['AUXILIARY_OPEN_POINT_IS_RECEIVER'] is False
    assert ba['S34_W03_RECEIVER_INTERSECTION_SELECTED'] is True
    assert ba['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and ba['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BB' and st['current']['36_09BB_entry_allowed'] is True
    print(f'36-09BA verified on {tested} AY boundary specializations: exact full-2 map gives y!=0; audited torsion then makes the image infinite-order. A rationally trivialized genus-one covering has infinite Q-points, hence infinitely many are off the unique Lminus boundary. Auxiliary open points are not receiver points; S34-W03 joint intersection is next.')
if __name__=='__main__': main()
