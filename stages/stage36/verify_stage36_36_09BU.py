#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
BTV=ROOT/'stages/stage36/verify_stage36_36_09BT.py'
AD=ROOT/'stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json'
AW=ROOT/'stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json'
BM=ROOT/'stages/stage36/36-09BM/old-six-full-cover-degenerate-cancellation-residue-preflight.json'
BN=ROOT/'stages/stage36/36-09BN/old-six-tie-normalized-unit-residue-preflight.json'
BO=ROOT/'stages/stage36/36-09BO/q-reservoir-full-qq-cancellation-preflight.json'
LIT=ROOT/'docs/arsenal/cards/workflows/LIT-WF02.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='eb11c6a7fef1d25d9188ecd1be6a856f109e7f39'
BT_HEAD='53c8d2fecff7e63ddfaef76de4387365f0ed2e28'
BT_CI='34119039258/101732546834'
CERT_BLOB='a8f3fb880b83aac2240ce299fe8a8fa42e044093'
LOCKS={BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',BTV:'3b9a1c2ceba0ed4091bc373ebf3d4a76025feec3',AD:'9d0388845955efee71d1a761ae4ee943d8b565d5',AW:'c1970a020803275ba87b249229e319367fa8f811',BM:'4fae43a7ebc9022acb4283a40f6eb95cb88d2aa5',BN:'c64ad051bb1466aa05dfb0cf638b9e7759766ed9',BO:'138749fde9766cd217fcb4622ccdebcb45730c2e',LIT:'a1e3e922ce3b2e26bfc5897fb1c1e2e82e3d6105'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def vq(n,q):
    n=abs(n); c=0
    while n and n%q==0: c+=1; n//=q
    return c
def primes(n):
    n=abs(n); out=[]
    if n%2==0:
        out.append(2)
        while n%2==0:n//=2
    d=3
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=2
    if n>1: out.append(n)
    return out
def odd_sf(n):
    out=1
    for q in primes(n):
        if q!=2 and vq(n,q)%2: out*=q
    return out
def legendre(a,q):
    a%=q
    if a==0:return 0
    x=pow(a,(q-1)//2,q)
    return 1 if x==1 else -1
def jacobi_sf(a,d):
    if d==1:return 1
    z=1
    for q in primes(d):
        if q==2:continue
        t=legendre(a,q)
        if t==0:return 0
        z*=t
    return z
def subset_products(ps):
    out=[1]
    for q in ps: out += [x*q for x in list(out)]
    return out
def is_square_fraction(x:Fraction):
    return x>0 and isqrt(x.numerator)**2==x.numerator and isqrt(x.denominator)**2==x.denominator

def ae_outer(a,b):
    assert gcd(a,b)==1
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b); Q=a*a+b*b
    assert P and M and D0
    pP=[q for q in primes(P) if q!=2]; pM=[q for q in primes(M) if q!=2]; pD=[q for q in primes(D0) if q!=2]
    assert all(legendre(2,q)==1 for q in pP+pM)
    rows=[]
    for A in subset_products(pP):
      for B in subset_products(pM):
       for ass in product((0,1,2),repeat=len(pD)):
        C=D=1
        for q,s in zip(pD,ass):
            if s==1:C*=q
            elif s==2:D*=q
        for eta in (-1,1):
         for e in (0,1):
          for f in (0,1):
            if A%8==B%8 and (e,f)==(1,0): continue
            if A%8!=B%8 and (e,f)==(0,1): continue
            tests=[jacobi_sf(-eta*(2**e)*B*C,A),jacobi_sf((2**f)*B*D,A),jacobi_sf(eta*(2**e)*A*C,B),jacobi_sf((2**f)*A*D,B),jacobi_sf(A*B,C),jacobi_sf((2**(1-f))*A*D,C),jacobi_sf(-A*B,D),jacobi_sf(eta*(2**(1-e))*A*C,D)]
            if tests!=[1]*8: continue
            delta=vq(D0,2); H=odd_sf(D0*C*D); g=(delta+e+f)%2
            mu=eta*(1 if D0>0 else -1)*(2**g)*H
            kappa=eta*(2**e)*C; rho=(2**f)*D
            tm2=Fraction(4*D0*rho,kappa*mu); tp2=Fraction(4*D0*kappa,rho*mu)
            assert is_square_fraction(tm2) and is_square_fraction(tp2)
            qok=all(legendre(mu*A*B,q)==1 for q in primes(Q) if q!=2)
            rows.append((A,B,C,D,eta,e,f,mu,qok))
    return rows

def main():
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BT_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bt=json.loads(BT.read_text()); aw=json.loads(AW.read_text()); bm=json.loads(BM.read_text()); bn=json.loads(BN.read_text()); bo=json.loads(BO.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1693,'36_09BT_exact_head':BT_HEAD,'36_09BT_exact_head_ci':BT_CI}
    assert bt['route_result']['next_leaf']=='36-09BU_GENERAL_AW_BRANCH_BAD_PLACE_VALUATION_TAXONOMY_PREFLIGHT'
    n=c['residual_squareclass_normalization']; g=c['generalized_norm_equations']; old=c['old_six_universal_odd_q_taxonomy']; qr=c['Q_reservoir_generalization']; rr=c['route_result']
    assert n['mu']=='eta*sign(D0)*2^g*H'
    assert n['Tminus_Tplus_rational_nonzero'] is True
    assert g['minus']=='A*B*c^2=(Q*r)^2-mu*(Tminus*s)^2'
    assert g['plus']=='A*B*d^2=(Q*s)^2-mu*(Tplus*r)^2'
    assert old['minus_term_valuations']==['2*R','hmu+2*Lminus+2*S']
    assert old['plus_term_valuations']==['2*S','hmu+2*Lplus+2*R']
    assert old['tie_possible_only_if']=='hmu=0'
    assert 'n mod 2 must equal hAB' in old['tie_square_criterion']
    assert bm['universal_nontie_rule']['post_leading_data_hensel_obstruction'] is False
    assert bn['universal_tie_reduction']['tie_square_equivalence']=='the tied full-cover radicand is a Q_q-square iff z^2-1 is a Q_q-square'
    assert qr['branch_only_first_residue_row']=='Legendre(mu*A*B,q)=+1 for every odd q|Q'
    assert qr['failure_consequence'].startswith('if the row fails')
    assert bo['Q_reservoir_setup']['minus_one_square'] is True
    assert qr['AY_reason_old_row_was_automatic']=='AY has A=B=mu=1'
    assert 'FAIL_CLOSED_MISSING_GLOBAL_CLASS_AND_LOCALIZATION_ADAPTER_EVIDENCE' in LIT.read_text()

    b12=ae_outer(1,2); b211=ae_outer(2,11)
    assert len(b12)==aw['diagnostics']['p_1_over_2']['AE_local_outer_branches']==14
    assert sum(x[-1] for x in b12)==8
    assert len(b211)==aw['diagnostics']['p_2_over_11']['AE_local_outer_branches']==158
    assert sum(x[-1] for x in b211)==77
    bykey={(x[0],x[1],x[2],x[3],x[4],x[5],x[6]):x for x in b12}
    assert bykey[(1,1,1,1,-1,0,1)][7:]==(3,False)
    assert bykey[(1,1,1,1,-1,0,0)][7:]==(6,True)
    d=c['exact_fixed_p_diagnostics']
    assert d['p_1_over_2']['AW_AE_local_outer_branches']==14 and d['p_1_over_2']['after_Q_reservoir_branch_row']==8
    assert d['p_2_over_11']['AW_AE_local_outer_branches']==158 and d['p_2_over_11']['after_Q_reservoir_branch_row']==77
    assert rr['general_old_six_odd_square_taxonomy_complete'] is True
    assert rr['general_Q_reservoir_odd_square_taxonomy_complete'] is True
    assert rr['new_Q_reservoir_branch_only_filter'] is True
    assert rr['general_prime2_branch_taxonomy_complete'] is False
    assert rr['next_leaf']=='36-09BV_FIXED_P_Q_RESERVOIR_BRANCH_FILTER_INTEGRATION_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V110_36_09BU_GENERAL_ODD_BAD_PLACE_TAXONOMY'
    bu=st['authority_frontier']['36-09BU']
    assert bu['certificate_blob_sha']==CERT_BLOB
    assert bu['GENERAL_ODD_BAD_PLACE_TAXONOMY_COMPLETE'] is True
    assert bu['NEW_Q_RESERVOIR_BRANCH_ONLY_FILTER'] is True
    assert bu['GENERAL_PRIME2_BRANCH_TAXONOMY_COMPLETE'] is False
    assert st['current']['next_exact_leaf']=='36-09BV_FIXED_P_Q_RESERVOIR_BRANCH_FILTER_INTEGRATION_PREFLIGHT'
    assert st['current']['36_09BV_entry_allowed'] is True
    for k in ['finite_exhaustive_H1_twist_family','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09BU verified: general odd bad-place square taxonomy is exact. A new branch-only Q-reservoir row Legendre(mu*A*B,q)=+1 prunes AW branches (14->8 at p=1/2, 158->77 at p=2/11) but gives no parameter or global-H1 credit. BV selected.')

if __name__=='__main__': main()
