#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CQ/bt-cartier-dual-local-condition-adapter-preflight.json'
CM=ROOT/'stages/stage36/36-09CM/bt-global-kummer-class-localization-adapter-preflight.json'
CO=ROOT/'stages/stage36/36-09CO/required-place-selection-rule-preflight.json'
CP=ROOT/'stages/stage36/36-09CP/fixed-dual-pairing-local-condition-system-preflight.json'
LIT=ROOT/'docs/arsenal/lit-wf02-global-h1-localization-reciprocity-contract.json'
BASE='0134d5f42df5aa290f5514cc48822e80a34d083c'
AUDITED_HEAD='e1c76660f08190709bff6ccf4336ac425020f156'
MERGED_PARENT='0afdbe5a0e4131e46b176800ca466795230d9702'
LOCKS={
    CERT:'c7042cc86ff94cf94db88c8cc65ce5b69441aabe',
    CM:'06c3e6d1fcc2453dc44b84d50896abdc6a1658d7',
    CO:'e41bfad47046ff47074285f2c6f719d9125b12a1',
    CP:'3ea852b149986c1ac0b3916005b605b138b21feb',
    LIT:'6fc62623ee59b4aaf1fc053ad42df2dcbba0855b',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def vp(q:Fraction,p:int)->int:
    n=abs(q.numerator); d=q.denominator; v=0
    while n and n%p==0: n//=p; v+=1
    while d%p==0: d//=p; v-=1
    return v

def unit_mod(q:Fraction,p:int,modulus:int)->int:
    v=vp(q,p)
    u=q/(Fraction(p,1)**v)
    return (u.numerator%modulus)*pow(u.denominator%modulus,-1,modulus)%modulus

def legendre_rational_unit(q:Fraction,p:int)->int:
    x=unit_mod(q,p,p)
    r=pow(x,(p-1)//2,p)
    assert r in (1,p-1)
    return 1 if r==1 else -1

def hilbert_odd(a:Fraction,b:Fraction,p:int)->int:
    aa=vp(a,p); bb=vp(b,p)
    s=-1 if ((aa&1)*(bb&1)*(((p-1)//2)&1))&1 else 1
    if bb&1: s*=legendre_rational_unit(a,p)
    if aa&1: s*=legendre_rational_unit(b,p)
    return s

def hilbert_2(a:Fraction,b:Fraction)->int:
    aa=vp(a,2); bb=vp(b,2)
    u=unit_mod(a,2,8); v=unit_mod(b,2,8)
    e=(((u-1)//2)*((v-1)//2) + aa*((v*v-1)//8) + bb*((u*u-1)//8))&1
    return -1 if e else 1

def hilbert_inf(a:Fraction,b:Fraction)->int:
    return -1 if a<0 and b<0 else 1

def prime_factors(n:int)->set[int]:
    n=abs(n); out:set[int]=set(); p=2
    while p*p<=n:
        while n%p==0:
            out.add(p); n//=p
        p=3 if p==2 else p+2
    if n>1: out.add(n)
    return out

def global_hilbert_product(a:Fraction,b:Fraction)->int:
    ps={2}
    for n in (a.numerator,a.denominator,b.numerator,b.denominator): ps|=prime_factors(n)
    z=hilbert_inf(a,b)
    for p in sorted(ps): z*=hilbert_2(a,b) if p==2 else hilbert_odd(a,b,p)
    return z

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',AUDITED_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',MERGED_PARENT,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cm=json.loads(CM.read_text()); co=json.loads(CO.read_text()); cp=json.loads(CP.read_text()); lit=json.loads(LIT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
        'audited_pr':1707,
        'hostile_audit_review':5137131273,
        'audited_exact_head':AUDITED_HEAD,
        'exact_head_ci':'34183931952/101928383350',
        'merged_main_sha':MERGED_PARENT,
    }
    assert cm['global_kummer_class']['module']=='K_BT=mu_2^3 over Q'
    assert cm['global_kummer_class']['class_name']=='Xi_BT'
    assert cp['adapter_result']['first_missing_obligation']=='BT_CARTIER_DUAL_CLASS_AND_LOCAL_CONDITION_ADAPTER'
    assert co['lit_wf02_consequence']['LIT_WF02_PASS_package_emitted'] is False

    left=c['fixed_left_class']; dual=c['cartier_dual_module']; fam=c['global_dual_h1_family']; pair=c['local_tate_pairing']; rec=c['global_reciprocity_boundary']; gap=c['geometric_adapter_gap']; rr=c['route_result']
    assert left['module']=='K_BT=mu_2^3' and left['class_name']=='Xi_BT'
    assert left['coordinates']==['[A*B]','[kappa*A]','[rho*A]']
    assert dual['identified_module']=='(Z/2Z)^3' and dual['rank']==3
    assert dual['abstract_dual_module_identification_complete'] is True
    assert dual['abstract_identification_alone_supplies_geometric_local_conditions'] is False
    assert fam['cohomology_group']=='H^1(Q,K_BT^D)'
    assert fam['arbitrary_global_Psi_is_geometry_bound_evaluation_class'] is False
    assert fam['arbitrary_global_Psi_is_poitou_tate_local_condition_system'] is False
    assert pair['coordinate_formula_multiplicative']=='<Xi_BT,Psi>_v=(A*B,u0)_v*(kappa*A,u1)_v*(rho*A,u2)_v'
    assert rec['global_global_pairing_total_can_be_nontrivial'] is False
    assert rec['choosing_a_global_dual_class_alone_can_supply_the_missing_obstruction'] is False
    assert rec['hilbert_product_formula_is_a_contradiction'] is False

    # Executable sanity check of the coordinatewise reciprocity identity over Q.
    samples=[
        (Fraction(-1),Fraction(2)),
        (Fraction(6),Fraction(35)),
        (Fraction(5,3),Fraction(-14,9)),
        (Fraction(-77,10),Fraction(33,14)),
        (Fraction(17,6),Fraction(85,22)),
    ]
    for a,b in samples: assert global_hilbert_product(a,b)==1,(a,b)
    triples=[samples[:3],samples[2:5]]
    for tri in triples:
        z=1
        for a,b in tri: z*=global_hilbert_product(a,b)
        assert z==1

    assert gap['source_bound_exact_sequence_or_connecting_map_defining_local_conditions'] is False
    assert gap['source_bound_local_point_to_H1_or_dual_evaluation_map'] is False
    assert gap['source_bound_orthogonal_local_condition_subgroups'] is False
    assert gap['arbitrary_dual_squareclasses_may_be_substituted_for_missing_geometry'] is False
    assert gap['first_missing_obligation']=='BT_GEOMETRIC_CONNECTING_MAP_OR_POINT_DEPENDENT_LOCAL_EVALUATION_ADAPTER'
    assert rr['route_status']=='FAIL_CLOSED_GLOBAL_DUAL_PAIRING_IS_RECIPROCITY_TAUTOLOGY_GEOMETRIC_LOCAL_CONDITION_ADAPTER_MISSING'
    assert rr['new_positive_obstruction'] is False
    assert rr['next_leaf']=='36-09CR_BT_GEOMETRIC_LOCAL_CONDITION_OR_ADELIC_EVALUATION_SOURCE_PREFLIGHT'

    assert 'calling the Hilbert product formula a contradiction' in lit['do_not_use_for']
    serre=[x for x in lit['literature'] if x['authors']=='Jean-Pierre Serre'][0]
    milne=[x for x in lit['literature'] if x['authors']=='J. S. Milne'][0]
    assert serre['theorem_identifier']=='Chapter III Theorems 2-4'
    assert 'product formula' in serre['conclusion_summary']
    assert 'product formula alone is not an obstruction' in serre['conditional_assumptions']
    assert milne['theorem_identifier']=='Theorem I.4.10'
    assert 'required localization maps and local conditions' in milne['exact_hypotheses_summary']

    for key,val in c['scope_firewalls'].items(): assert val is False,(key,val)
    print('36-09CQ verified: K_BT^D=(Z/2)^3 and the coordinate local Tate/Hilbert pairing are explicit, but pairing global Xi_BT with any global dual H1 class is reciprocity-trivial in total. Geometry-derived local conditions/evaluation remain missing; no LIT-WF02/PT/BM/receiver/endpoint credit.')

if __name__=='__main__': main()
