#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, subprocess
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BW/general-aw-branch-prime2-taxonomy-preflight.json'
BV=ROOT/'stages/stage36/36-09BV/fixed-p-q-reservoir-branch-filter-integration-preflight.json'
BVV=ROOT/'stages/stage36/verify_stage36_36_09BV.py'
BU=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
BI=ROOT/'stages/stage36/36-09BI/prime2-full-cover-congruence-preflight.json'
BJ=ROOT/'stages/stage36/36-09BJ/prime2-equal-valuation-unit-branch-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e6fd1aec8391c2e9a82eab45c3498afcec99ad44'
PARENT='9bc6a455a3d9eacf54db5dbcd60ef3ce732c8b18'
PARENT_CI='34121263304/101739583607'
CERT_BLOB='d7feb3e6b86c5c93bae999f8836840e64fbd5fb5'
LOCKS={BV:'11b2b927f04c6a7ad151d2456fc79d27329b8dad',BVV:'345fdf7c8133883c3eb261e1313ee56a7b9d7f7f',BU:'a8f3fb880b83aac2240ce299fe8a8fa42e044093',BUV:'64b889c2dde22d021fb2933b976311d903f57dce',AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df',BI:'ba6a705ce61b14e640b2c400d42dded60097b406',BJ:'f9ef3dde7b756470f2fc882327a67d72db7902f1'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def v2int(n:int):
    assert n
    c=0
    while n%2==0: c+=1; n//=2
    return c,n%8
def q2square(x:Fraction):
    if x==0: return False
    vn,un=v2int(x.numerator); vd,ud=v2int(x.denominator)
    return (vn-vd)%2==0 and (un*pow(ud,-1,8))%8==1
def predict(a:int,g:int,mu0:int,x:Fraction,y:Fraction):
    X=v2int(x.numerator)[0]-v2int(x.denominator)[0]; Y=v2int(y.numerator)[0]-v2int(y.denominator)[0]
    E1=2*X; E2=g+2*Y
    if E1<E2:
        h=E2-E1
        if h>=3:return a%8==1
        if h==2:return False
        return a%8==7 and mu0%4==1
    if E1>E2:
        if g==1:return False
        h=E1-E2
        if h==2:return mu0%8==(3*a)%8
        return mu0%8==(-a)%8
    assert g==0
    w=(x/y)**2-mu0
    if w==0:return None
    vn,un=v2int(w.numerator); vd,ud=v2int(w.denominator)
    return (vn-vd)%2==0 and (un*pow(ud,-1,8))%8==a%8
def load_bu():
    spec=importlib.util.spec_from_file_location('stage36_bu_verifier',BUV)
    mod=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(mod); return mod

def main():
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bv=json.loads(BV.read_text()); ae=json.loads(AE.read_text()); bi=json.loads(BI.read_text()); bj=json.loads(BJ.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1693,'36_09BV_fresh_exact_head':PARENT,'36_09BV_fresh_exact_head_ci':PARENT_CI}
    assert bv['route_result']['next_leaf']=='36-09BW_GENERAL_AW_BRANCH_PRIME2_TAXONOMY_PREFLIGHT'
    assert ae['alpha_two_residue_input']['consequence'][2]=='A mod 8 is in {1,7}'
    assert ae['alpha_two_residue_input']['consequence'][3]=='B mod 8 is in {1,7}'
    for a0 in range(-15,16):
      for b0 in range(-15,16):
        if not a0 or not b0 or gcd(a0,b0)!=1 or a0 in (b0,-b0):continue
        Q=a0*a0+b0*b0; D0=a0*b0*(a0-b0)*(a0+b0); sigma=v2int(Q)[0]; delta=v2int(D0)[0]
        assert sigma in (0,1) and delta>=2*sigma+1
    for a in (1,7):
      for g in (0,1):
       for mu0 in (1,3,5,7):
        for X in range(5):
         for Y in range(5):
          for xu in (1,3,5,7):
           for yu in (1,3,5,7):
            x=Fraction(2**X*xu); y=Fraction(2**Y*yu); F=(x*x-2**g*mu0*y*y)/a; p=predict(a,g,mu0,x,y)
            assert (F==0 if p is None else p==q2square(F)),(a,g,mu0,X,Y,xu,yu,F,p,q2square(F) if F else None)
    n=c['notation']; src=c['primitive_source_Q2_cases']; rule=c['generic_two_term_Q2_square_rule']; filt=c['branch_only_prime2_filters']; ay=c['AY_specialization_check']; rr=c['route_result']
    assert n['primitive_parameter_bound']=='delta>=2*sigma+1'
    assert src['both_units_A_equal_B_mod8']['forced']=='f=1, s is a unit'
    assert src['both_units_A_not_equal_B_mod8']['forced']=='e=1, r is a unit'
    assert rule['tie_E1_equal_E2']['criterion']=='F is a Q2-square iff n is even and w0=a mod8'
    assert filt['AB_residue_filter']['point_independent'] is True
    assert filt['critical_deep_branch_filter']['critical_condition']=='delta=2*sigma+2-e, equivalently Delta_max=1'
    assert filt['critical_deep_branch_filter']['point_independent'] is True
    assert ay['exact_specialization'] is True
    assert bi['minus_root_valuation_gate']['h']=='Y-X=(delta+3-2*sigma-alpha)/2'
    assert bj['equality_branch_input']['minus_root_equivalence']=='the h=0 minus root exists over Q2 iff z^2-1 is a Q2-square'
    mod=load_bu()
    for a0,b0,expected in [(1,2,(14,8,6,4)),(2,11,(158,77,52,30))]:
        rows=mod.ae_outer(a0,b0); Q=a0*a0+b0*b0; D0=a0*b0*(a0-b0)*(a0+b0); sigma=v2int(Q)[0]; delta=v2int(D0)[0]
        qrows=[r for r in rows if r[-1]]; same=[r for r in qrows if r[0]%8==r[1]%8]; final=[r for r in same if not (r[6]==1 and delta==2*sigma+2-r[5])]
        assert (len(rows),len(qrows),len(same),len(final))==expected
    assert rr['general_prime2_branch_taxonomy_complete_at_valuation_unit_layer'] is True
    assert rr['new_AB_mod8_branch_filter'] is True and rr['new_critical_deep_branch_filter'] is True
    assert rr['next_leaf']=='36-09BX_FIXED_P_Q2_BRANCH_FILTER_INTEGRATION_PREFLIGHT'
    st=json.loads(STATE.read_text()); assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V112_36_09BW_GENERAL_Q2_TAXONOMY'
    bw=st['authority_frontier']['36-09BW']; assert bw['certificate_blob_sha']==CERT_BLOB and bw['GENERAL_PRIME2_BRANCH_TAXONOMY_COMPLETE'] is True and bw['AB_MOD8_BRANCH_FILTER'] is True and bw['CRITICAL_DEEP_BRANCH_FILTER'] is True
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    assert st['current']['next_exact_leaf']=='36-09BX_FIXED_P_Q2_BRANCH_FILTER_INTEGRATION_PREFLIGHT' and st['current']['36_09BX_entry_allowed'] is True
    for k in ['finite_exhaustive_H1_twist_family','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:assert st['claims'][k] is False
    print('36-09BW verified: general AW Q2 taxonomy exact; A=B mod8 and the critical deep-row filter are point-independent; diagnostics are 8->4 and 77->30. BX selected.')
if __name__=='__main__':main()
