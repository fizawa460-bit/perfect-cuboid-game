#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BV/fixed-p-q-reservoir-branch-filter-integration-preflight.json'
BU=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
AW=ROOT/'stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='eb11c6a7fef1d25d9188ecd1be6a856f109e7f39'
BU_HEAD='72252b9e891d7986813c9e81706958970a754331'
BU_CI='34120012847/101735669506'
CERT_BLOB='11b2b927f04c6a7ad151d2456fc79d27329b8dad'
LOCKS={BU:'a8f3fb880b83aac2240ce299fe8a8fa42e044093',BUV:'64b889c2dde22d021fb2933b976311d903f57dce',AW:'c1970a020803275ba87b249229e319367fa8f811'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def load_bu_verifier():
    spec=importlib.util.spec_from_file_location('stage36_bu_verifier',BUV)
    mod=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(mod); return mod

def main():
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BU_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bu=json.loads(BU.read_text()); aw=json.loads(AW.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1693,'36_09BU_exact_head':BU_HEAD,'36_09BU_exact_head_ci':BU_CI}
    assert bu['route_result']['next_leaf']=='36-09BV_FIXED_P_Q_RESERVOIR_BRANCH_FILTER_INTEGRATION_PREFLIGHT'
    enum=c['integrated_fixed_p_outer_enumerator']; rule=c['sound_fixed_p_exclusion_rule']; credit=c['credit_boundary']; rr=c['route_result']
    assert aw['fixed_p_outer_enumerator']['outer_superset'] is True
    assert aw['fixed_p_exclusion_rule']['unconditional'] is True
    assert bu['Q_reservoir_generalization']['branch_only_first_residue_row']=='Legendre(mu*A*B,q)=+1 for every odd q|Q'
    assert bu['Q_reservoir_generalization']['failure_consequence'].startswith('if the row fails')
    assert enum['finite_for_each_fixed_p'] is True
    assert enum['uniform_single_finite_Q_squareclass_family'] is False
    assert rule['unconditional'] is True and rule['converse'] is False
    assert rule['surviving_branch_implies_receiver'] is False

    mod=load_bu_verifier()
    b12=mod.ae_outer(1,2); b211=mod.ae_outer(2,11)
    d=c['exact_diagnostics']
    assert (len(b12),sum(x[-1] for x in b12))==(14,8)
    assert (len(b211),sum(x[-1] for x in b211))==(158,77)
    assert d['p_1_over_2']=={'AW_AE_local_outer_branches':14,'Q_admissible_outer_branches':8,'eliminated_branches':6,'fixed_p_excluded':False}
    assert d['p_2_over_11']=={'AW_AE_local_outer_branches':158,'Q_admissible_outer_branches':77,'eliminated_branches':81,'fixed_p_excluded':False}
    assert credit['new_exact_fixed_p_exclusion_interface'] is True
    assert credit['fixed_p_parameter_exclusion_obtained_in_certified_diagnostics'] is False
    assert credit['general_prime2_branch_taxonomy_complete'] is False
    assert rr['fixed_p_Q_filter_integration_complete'] is True
    assert rr['sound_zero_survivor_exclusion_rule'] is True
    assert rr['next_leaf']=='36-09BW_GENERAL_AW_BRANCH_PRIME2_TAXONOMY_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V111_36_09BV_FIXED_P_Q_FILTER_INTEGRATION'
    bv=st['authority_frontier']['36-09BV']
    assert bv['certificate_blob_sha']==CERT_BLOB
    assert bv['FIXED_P_Q_FILTER_INTEGRATION_COMPLETE'] is True
    assert bv['SOUND_ZERO_SURVIVOR_EXCLUSION_RULE'] is True
    assert bv['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09BW_GENERAL_AW_BRANCH_PRIME2_TAXONOMY_PREFLIGHT'
    assert st['current']['36_09BW_entry_allowed'] is True
    for k in ['finite_exhaustive_H1_twist_family','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09BV verified: AW exhaustive fixed-p outer branches are now filtered by the exact BU Q-reservoir row. Empty integrated family would soundly exclude that fixed p; current certified examples retain 8 and 77 branches. BW prime-2 generalization selected.')

if __name__=='__main__': main()
