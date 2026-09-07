#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
BS=ROOT/'stages/stage36/36-09BS/fixed-p-outer-branch-full-cover-local-gate-adapter-preflight.json'
BSV=ROOT/'stages/stage36/verify_stage36_36_09BS.py'
AD=ROOT/'stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
BH=ROOT/'stages/stage36/36-09BH/bad-place-full-cover-valuation-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='eb11c6a7fef1d25d9188ecd1be6a856f109e7f39'
SYNC='451d2c2a36f953ad60e9731c0b7ca29717b05f3f'
BS_HEAD='14dc92d94dd81d01f0b84070070410ad4c3ecca9'
BS_CI='34114221064/101717172157'
CERT_BLOB='e58c417ddfa340d96b2ac1fbae9e7da7c5224d78'
LOCKS={
    BS:'273f3f33762861fe809929bd8e32dd5153c0a781',
    BSV:'0a1b1396f6f2ecbf3b19e417182d25b7c300acdf',
    AD:'9d0388845955efee71d1a761ae4ee943d8b565d5',
    BB:'e4b63fd500d05ff5dc704e0c08409edee5895053',
    BH:'76487371ed363868af18a9fa0f6f7e1367d28f27',
}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BS_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); bs=json.loads(BS.read_text()); ad=json.loads(AD.read_text()); bb=json.loads(BB.read_text()); bh=json.loads(BH.read_text())
    assert c['base_main_sha']==BASE
    fs=c['freshness_sync']
    assert fs['previous_base']=='727b3f34c4d850e868aff64483aeb99861b13c7c'
    assert fs['current_main']==BASE and fs['sync_merge_commit']==SYNC and fs['stage36_source_drift'] is False
    assert c['batch_parent']=={'pr':1693,'36_09BS_exact_head':BS_HEAD,'36_09BS_exact_head_ci':BS_CI}
    assert bs['route_result']['next_leaf']=='36-09BT_GENERAL_AW_SQUARECLASS_BRANCH_FULL_COVER_LOCAL_MODEL_PREFLIGHT'
    assert bs['adapter_audit']['directly_attach_BH_BO_gate_to_every_AW_branch'] is False

    rec=c['AD_squareclass_reconstruction']; model=c['general_t_line_four_square_model']; elim=c['general_BH_elimination']; ay=c['AY_specialization_check']; credit=c['credit_boundary']; rr=c['route_result']
    assert ad['coupled_squareclass_reconstruction']['U']=='delta_P*u^2'
    assert ad['coupled_squareclass_reconstruction']['V']=='delta_M*v^2'
    assert rec['U']=='A*u^2' and rec['V']=='B*v^2'
    assert rec['UminusV']=='kappa*r^2' and rec['UplusV']=='rho*s^2'
    assert rec['Lminus']=='M^2*U-P^2*V=kappa*A*B*c^2'
    assert rec['Lplus']=='M^2*U+P^2*V=rho*A*B*d^2'
    assert model['general_AW_branch_full_cover_local_model_obtained'] is True
    assert model['equations']==[
      'A-B*t^2=kappa*(r/u)^2','A+B*t^2=rho*(s/u)^2',
      'A-lambda^2*B*t^2=kappa*A*B*(c/(M*u))^2','A+lambda^2*B*t^2=rho*A*B*(d/(M*u))^2']
    assert model['normalized_square_root_version']==[
      'R^2=kappa*(A-B*t^2)','S^2=rho*(A+B*t^2)',
      'Zminus^2=kappa*A*B*(A-lambda^2*B*t^2)','Zplus^2=rho*A*B*(A+lambda^2*B*t^2)']

    ids=bh['branch_discriminant_support']['identities']
    assert 'P^2-M^2=8*D0' in ids and 'P^2+M^2=2*Q^2' in ids
    assert elim['minus']=='A*B*c^2=Q^2*r^2-(4*D0*rho/kappa)*s^2'
    assert elim['plus']=='A*B*d^2=Q^2*s^2-(4*D0*kappa/rho)*r^2'
    assert elim['seven_reservoir_upper_support_retained'] is True
    assert bh['branch_discriminant_support']['seven_pairwise_odd_disjoint_reservoirs']==['P','M','a','b','a-b','a+b','Q']

    assert ay['exact_specialization'] is True
    assert ay['BB_recovered']==bb['AY_genusone_ratio_model']['equations'] + bb['receiver_restricted_intersection']['normalized_extra_equations']
    assert ay['BH_elimination_recovered']==bh['full_cover_integral_squareclass_form']['difference_of_squares_forms']
    assert credit['population_adapter_gap_from_BS_resolved_at_equation_level'] is True
    assert credit['BH_BO_local_taxonomy_transfers_unchanged_to_general_branch'] is False
    assert credit['general_branch_bad_place_taxonomy_complete'] is False
    assert credit['whole_fixed_p_parameter_elimination_interface_complete'] is False
    assert rr['route_status']=='PASS_GENERAL_BRANCH_FULL_COVER_MODEL_OBTAINED_LOCAL_TAXONOMY_NEXT'
    assert rr['next_leaf']=='36-09BU_GENERAL_AW_BRANCH_BAD_PLACE_VALUATION_TAXONOMY_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V109_36_09BT_GENERAL_AW_FULL_COVER_MODEL'
    bt=st['authority_frontier']['36-09BT']
    assert bt['certificate_blob_sha']==CERT_BLOB
    assert bt['GENERAL_AW_BRANCH_FULL_COVER_LOCAL_MODEL_OBTAINED'] is True
    assert bt['SEVEN_RESERVOIR_ODD_SUPPORT_UPPER_BOUND'] is True
    assert bt['GENERAL_BRANCH_BAD_PLACE_TAXONOMY_COMPLETE'] is False
    assert bt['WHOLE_FIXED_P_PARAMETER_ELIMINATION_INTERFACE_COMPLETE'] is False
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    assert st['freshness']['stage36_source_drift'] is False and st['freshness']['sync_required_before_audit'] is False
    assert st['current']['unit']=='36-09BT'
    assert st['current']['next_exact_leaf']=='36-09BU_GENERAL_AW_BRANCH_BAD_PLACE_VALUATION_TAXONOMY_PREFLIGHT'
    assert st['current']['36_09BU_entry_allowed'] is True
    for k in ['finite_exhaustive_H1_twist_family','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09BT verified: general AW branch four-square/full-cover model and BH elimination are exact; AY specializes back to BB/BH. Only the equations transfer. General bad-place taxonomy is still open; BU selected.')

if __name__=='__main__': main()
