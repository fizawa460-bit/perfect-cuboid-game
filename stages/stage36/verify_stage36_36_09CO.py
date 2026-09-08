#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CO/required-place-selection-rule-preflight.json'
CN=ROOT/'stages/stage36/36-09CN/bt-kummer-immutable-localization-package-preflight.json'
CNV=ROOT/'stages/stage36/verify_stage36_36_09CN.py'
CM=ROOT/'stages/stage36/36-09CM/bt-global-kummer-class-localization-adapter-preflight.json'
LIT=ROOT/'docs/arsenal/lit-wf02-global-h1-localization-reciprocity-contract.json'
LITV=ROOT/'docs/arsenal/verify_lit_wf02_global_h1_localization_reciprocity.py'
BASE='8143dbaabb0cf164e65091dd315996f7eac68cf8'
CN_HEAD='6b31ca804744c4d8726d3d74861faadee78e0d64'
CN_CI='34180629566/101918846959'
LOCKS={
    CERT:'e41bfad47046ff47074285f2c6f719d9125b12a1',
    CN:'e6b38b0bd621434a5cfa365ee1077241e1beb9bc',
    CNV:'1f0d20f3c02586c3689fbf1da57ddee39e9f6430',
    CM:'06c3e6d1fcc2453dc44b84d50896abdc6a1658d7',
    LIT:'6fc62623ee59b4aaf1fc053ad42df2dcbba0855b',
    LITV:'ee066a55f95184916c02dc1f1bbd9f07d1840dc8',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def vp_int(n:int,p:int)->int:
    n=abs(n); e=0
    while n and n%p==0:
        n//=p; e+=1
    return e

def vp(x:Fraction,p:int)->int:
    return vp_int(x.numerator,p)-vp_int(x.denominator,p)

def odd_prime_support(x:Fraction)->set[int]:
    n=abs(x.numerator*x.denominator)
    out=set(); q=3
    while q*q<=n:
        if n%q==0:
            if vp(x,q)%2: out.add(q)
            while n%q==0: n//=q
        q+=2
    if n>1 and n%2:
        if vp(x,n)%2: out.add(n)
    return out

def legendre_unit(x:Fraction,p:int)->int:
    e=vp(x,p)
    if e>=0:
        y=x/Fraction(p**e,1)
    else:
        y=x*Fraction(p**(-e),1)
    num=y.numerator%p; den=y.denominator%p
    u=(num*pow(den,-1,p))%p
    assert u
    z=pow(u,(p-1)//2,p)
    return -1 if z==p-1 else 1

def hilbert_odd(a:Fraction,b:Fraction,p:int)->int:
    assert p%2==1
    alpha=vp(a,p); beta=vp(b,p)
    sign=-1 if ((alpha*beta*((p-1)//2))%2) else 1
    if beta%2: sign*=legendre_unit(a,p)
    if alpha%2: sign*=legendre_unit(b,p)
    return sign

def required_places(alpha:list[Fraction],beta:list[Fraction])->set[str]:
    odd=set()
    for x in alpha+beta: odd |= odd_prime_support(x)
    return {'infinity','2',*[str(q) for q in sorted(odd)]}

def primes_upto(n:int)->list[int]:
    out=[]
    for x in range(3,n+1,2):
        if all(x%d for d in range(3,int(x**0.5)+1,2)):
            out.append(x)
    return out

def main()->None:
    for p,h in LOCKS.items():
        assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CN_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cn=json.loads(CN.read_text()); cm=json.loads(CM.read_text()); lit=json.loads(LIT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1707,'36_09CN_exact_green_head':CN_HEAD,'36_09CN_exact_head_ci':CN_CI}
    assert cn['route_result']['next_leaf']=='36-09CO_REQUIRED_PLACE_SELECTION_RULE_PREFLIGHT'
    assert cm['global_kummer_class']['three_coordinates']==['xi0=[A*B]','xi1=[kappa*A]','xi2=[rho*A]']
    assert cm['localization_adapter']['same_global_branch_class_used_at_all_places'] is True

    r=c['serre_hilbert_required_place_rule']
    assert r['required_place_set']=='S_Hilb={infinity,2} union {odd q : some v_q(alpha_i) or v_q(beta_j) is odd}'
    assert r['finite_inventory_after_both_sides_fixed'] is True
    assert r['rule_is_theorem_specific_not_receiver_bad_place_taxonomy'] is True

    # Executable check of the odd-prime Hilbert support lemma used by CO.
    panels=[
        ([Fraction(1),Fraction(-1),Fraction(1)],[Fraction(2),Fraction(3),Fraction(5)]),
        ([Fraction(6),Fraction(-10),Fraction(14)],[Fraction(15),Fraction(-21)]),
        ([Fraction(3,5),Fraction(-7,11)],[Fraction(13,3),Fraction(-5,17)]),
    ]
    checked=0
    for alpha,beta in panels:
        S=required_places(alpha,beta)
        assert '2' in S and 'infinity' in S
        for q in primes_upto(199):
            if str(q) in S: continue
            for a in alpha:
                for b in beta:
                    assert hilbert_odd(a,b,q)==1,(a,b,q,S)
                    checked+=1
    assert checked>100

    serre=[x for x in lit['literature'] if x['authors']=='Jean-Pierre Serre'][0]
    milne=[x for x in lit['literature'] if x['authors']=='J. S. Milne'][0]
    assert 'fixed squareclass/quadratic-form data' in serre['exact_hypotheses_summary']
    assert 'fixed global class system' in serre['conditional_assumptions']
    assert 'one fixed finite global Galois module' in milne['exact_hypotheses_summary']
    assert 'local conditions' in milne['exact_hypotheses_summary']
    assert 'genuine fixed global module/class and exact localizations' in milne['conditional_assumptions']

    s=c['stage36_instantiation_check']; lc=c['lit_wf02_consequence']; rr=c['route_result']; fw=c['scope_firewalls']
    assert s['left_class_and_localization_adapter_available'] is True
    assert s['fixed_dual_or_evaluation_squareclass_family_available'] is False
    assert s['serre_pairing_place_inventory_instantiated'] is False
    assert s['milne_fixed_local_condition_system_available'] is False
    assert s['milne_poitou_tate_place_inventory_instantiated'] is False
    assert lc['required_place_selection_rule_available_conditionally'] is True
    assert lc['independent_stage36_required_place_inventory_complete'] is False
    assert lc['LIT_WF02_PASS_package_emitted'] is False
    assert lc['first_missing_obligation']=='FIXED_DUAL_PAIRING_OR_LOCAL_CONDITION_SYSTEM'
    assert rr['route_status']=='PASS_CONDITIONAL_REQUIRED_PLACE_RULE_FAIL_CLOSED_AT_DUAL_LOCAL_CONDITION_INPUT'
    assert rr['next_leaf']=='36-09CP_FIXED_DUAL_PAIRING_OR_LOCAL_CONDITION_SYSTEM_PREFLIGHT'
    assert rr['36_09CP_entry_allowed_after_exact_green_CO'] is True
    for key,val in fw.items():
        assert val is False,(key,val)
    print(f'36-09CO verified: conditional finite Serre/Hilbert required-place rule is exact (diagnostic pair checks={checked}); Stage36 application remains fail-closed because no fixed dual/evaluation family or Milne local-condition system is bound. CP selected; no obstruction or receiver credit.')

if __name__=='__main__': main()
