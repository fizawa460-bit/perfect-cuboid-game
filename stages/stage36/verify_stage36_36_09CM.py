#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CM/bt-global-kummer-class-localization-adapter-preflight.json'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
CK=ROOT/'stages/stage36/36-09CK/good-prime-and-real-place-local-integration-preflight.json'
CKV=ROOT/'stages/stage36/verify_stage36_36_09CK.py'
LIT=ROOT/'docs/arsenal/lit-wf02-global-h1-localization-reciprocity-contract.json'
H04=ROOT/'stages/stage36/36-04/h-torsor-lift-class.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='3cbdaf46e74f458681041322f574365e0003d818'
PROMOTION='288fbeb4dce1043b7980dc0ebebaded544e28bac'
PROMOTION_CI='34176513379/101906884400'
CERT_BLOB='06c3e6d1fcc2453dc44b84d50896abdc6a1658d7'
LOCKS={
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
    AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
    CK:'909dcb4985414fc3085818ad818f7601830dc7f6',
    CKV:'d7541d86948d98a629f503443a82d52ab1c95908',
    LIT:'6fc62623ee59b4aaf1fc053ad42df2dcbba0855b',
    H04:'a06e201a9b554da71c5e75d8f8541e7284f8d020',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def load(p:Path,n:str):
    s=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m

def is_square_fraction(x:Fraction)->bool:
    return x>0 and isqrt(x.numerator)**2==x.numerator and isqrt(x.denominator)**2==x.denominator

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMOTION,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); bt=json.loads(BT.read_text()); ae=json.loads(AE.read_text()); ck=json.loads(CK.read_text()); lit=json.loads(LIT.read_text()); h04=json.loads(H04.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1707,'promotion_head':PROMOTION,'promotion_ci':PROMOTION_CI,'consumed_pr':1705,'hostile_audit_review':5136295432}
    assert bt['general_t_line_four_square_model']['general_AW_branch_full_cover_local_model_obtained'] is True
    assert ae['squareclass_variables']['properties'][-1]=='gcd(C,D)=1'
    assert ck['good_prime_model']['target_characters']==['d','k','r','k*d','r*d']
    assert lit['current_stage36_applicability_status']=='FAIL_CLOSED_MISSING_GLOBAL_CLASS_AND_LOCALIZATION_ADAPTER_EVIDENCE'
    assert h04['pointwise_class']['definition'].startswith('delta_H(P)')

    g=c['global_kummer_class']; ca=c['exact_BT_cover_adapter']; la=c['localization_adapter']; os=c['old_six_selected_prime_rewrite']; qr=c['Q_reservoir_rewrite']; ar=c['adapter_result']
    assert g['module']=='K_BT=mu_2^3 over Q'
    assert g['three_coordinates']==['xi0=[A*B]','xi1=[kappa*A]','xi2=[rho*A]']
    assert g['global_Kummer_class_constructed_for_each_fixed_BT_branch'] is True
    assert ca['equivalent_to_BT_normalized_four_square_model_on_retained_open'] is True
    assert la['CK_good_prime_target_vector_matches_exactly'] is True
    assert la['ramified_places_are_not_encoded_by_naive_Legendre_of_a_q_divisible_coordinate'] is True
    assert os['exactly_rewrites_AE_selected_prime_rows_in_local_squareclasses_using_loc_q_Xi_BT_and_fixed_classes_minus1_and_2'] is True
    assert qr['global_squareclass_identity']=='[mu]=[D0*kappa*rho]'
    assert ar['BT_global_Kummer_class_adapter_complete'] is True
    assert ar['BT_dynamic_localization_system_adapter_complete_at_squareclass_cover_level'] is True
    assert ar['old_S36_PW04_pointwise_36_04_class_identified_with_Xi_BT'] is False
    assert ar['old_S36_PW07_dynamic_matrix_adapter_declared_complete'] is False
    assert ar['LIT_WF02_applicability_PASS'] is False

    bu=load(BUV,'cm_bu')
    panels=[(1,2),(2,11),(3,4),(1,8)]
    checked_rows=0; checked_q=0
    for a,b in panels:
        P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b); Q=a*a+b*b
        assert gcd(a,b)==1 and P and M and D0
        assert P*P-M*M==8*D0 and P*P+M*M==2*Q*Q
        for row in bu.ae_outer(a,b):
            A,B,C,D,eta,e,f,mu,qok=row
            kappa=eta*(2**e)*C; rho=(2**f)*D
            xi0=A*B; xi1=kappa*A; xi2=rho*A
            # The two dependent root coefficients differ from xi0*xi1 and xi0*xi2 by A^2.
            assert is_square_fraction(Fraction(xi0*xi1,kappa*B))
            assert is_square_fraction(Fraction(xi0*xi2,rho*B))
            # Exact BT -> five-root change of variables over rational test t values.
            L=Fraction(P*P,M*M)
            for t in [Fraction(1,3),Fraction(2,5),Fraction(3,7)]:
                y=Fraction(B,A)*t*t
                assert Fraction(B*B)*t*t == Fraction(A*B)*y
                assert Fraction(kappa)*(A-B*t*t) == Fraction(kappa*A)*(1-y)
                assert Fraction(rho)*(A+B*t*t) == Fraction(rho*A)*(1+y)
                lhs_minus=Fraction(kappa*A*B)*(A-L*B*t*t)/Fraction(A*A)
                lhs_plus=Fraction(rho*A*B)*(A+L*B*t*t)/Fraction(A*A)
                assert lhs_minus == Fraction(kappa*B)*(1-L*y)
                assert lhs_plus == Fraction(rho*B)*(1+L*y)
            # Selected-prime AE row representatives are monomials in loc(Xi_BT), [-1], [2].
            assert is_square_fraction(Fraction((-1)*xi0*xi1,-kappa*B))
            assert is_square_fraction(Fraction(xi0*xi2,rho*B))
            assert is_square_fraction(Fraction(2*xi2,(2**(1-f))*A*D))
            assert is_square_fraction(Fraction(2*xi1,eta*(2**(1-e))*A*C))
            # BU normalization gives one exact global squareclass identity for mu.
            assert is_square_fraction(Fraction(D0*kappa*rho,mu))
            assert is_square_fraction(Fraction(D0*xi0*xi1*xi2,mu*A*B))
            # At q|Q the Xi coefficients are q-adic units, D0 is a square, and BU row is d*k*r.
            for q in bu.primes(Q):
                if q==2: continue
                assert (A*B*C*D)%q != 0
                assert bu.legendre(-1,q)==1
                assert bu.legendre(D0,q)==1
                d=bu.legendre(xi0,q); k=bu.legendre(xi1,q); r=bu.legendre(xi2,q)
                assert bu.legendre(mu*A*B,q)==d*k*r
                assert qok == (d*k*r==1)
                checked_q+=1
            # At ordinary unramified odd places the five-root character vector is exactly d,k,r,dk,dr.
            for q in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]:
                if (2*A*B*C*D)%q==0: continue
                d=bu.legendre(xi0,q); k=bu.legendre(xi1,q); r=bu.legendre(xi2,q)
                chars=[bu.legendre(z,q) for z in [A*B,kappa*A,rho*A,kappa*B,rho*B]]
                assert chars==[d,k,r,d*k,d*r],(a,b,row,q,chars,d,k,r)
            checked_rows+=1
    assert checked_rows>100 and checked_q>0

    fw=c['scope_firewalls']
    for key in ['Xi_BT_equals_36_04_delta_H','BT_Kummer_class_is_original_H_torsor_class','character_rewrite_alone_is_LIT_WF02_PASS','localization_class_implies_local_point','everywhere_local_means_global','Hilbert_product_formula_is_a_contradiction','Selmer_membership_obtained','Poitou_Tate_obstruction_obtained','Brauer_Manin_obstruction_obtained','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[key] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V136_36_09CM_BT_GLOBAL_KUMMER_LOCALIZATION_ADAPTER'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    cm=st['authority_frontier']['36-09CM']
    assert cm['certificate_blob_sha']==CERT_BLOB
    assert cm['BT_GLOBAL_KUMMER_CLASS_ADAPTER_COMPLETE'] is True
    assert cm['BT_DYNAMIC_LOCALIZATION_SYSTEM_ADAPTER_COMPLETE_AT_SQUARECLASS_COVER_LEVEL'] is True
    assert cm['LIT_WF02_APPLICABILITY_PASS'] is False
    assert st['current']['next_exact_leaf']=='36-09CN_BT_KUMMER_IMMUTABLE_LOCALIZATION_PACKAGE_PREFLIGHT'
    assert st['current']['36_09CN_entry_allowed'] is True
    for key in ['new_global_obstruction_obtained','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed']:
        assert st['promotion_gates'][key] is False
    print(f'36-09CM verified: fixed BT branch gives Xi_BT in H1(Q,mu2^3); five-root coefficients and local character rows are localizations of the same global branch class. rows={checked_rows}, Q-prime checks={checked_q}. LIT-WF02 PASS and global obstruction remain false; CN selected.')

if __name__=='__main__': main()
