from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
S=ROOT/'stages'/'stage27'
t=(S/'27-20-r301t'/'result.md').read_text(); u=(S/'27-20-r301u'/'result.md').read_text(); v=(S/'27-20-r301v'/'result.md').read_text()
reg=json.loads((S/'27-20-r301t-v'/'batch-registry.json').read_text()); qs=json.loads((S/'27-20-r301q-s'/'batch-registry.json').read_text()); ctl=json.loads((S/'27-controller.json').read_text())
assert 'Q1_TO_STAGE14_FACE_MOBIUS_ADAPTER_PROVED=true' in t
assert 'Q1_TO_ACTIVE_FACE_SUPPORT_INJECTION_PROVED=true' in t
assert 'Q1_EQUALS_ALL_STAGE14_ACTIVE_VERTICES_CLAIMED=false' in t
assert 'OFF_WALL_FIXED_DISTANCE_SUPPORT_SAVING_PROVED=true' in u
assert 'OFF_WALL_Q1_BOUND=B^(1/2-2eta+o(1))' in u
assert 'CRITICAL_THETA=1/4' in u
assert 'CRITICAL_PHI_RANGE=[1/8,1/4]' in v
assert 'CRITICAL_CHI_FORMULA=2phi-1/4' in v
assert 'CRITICAL_E_K=1/2' in v and 'CRITICAL_E_RRF=1/2' in v
assert 'CRITICAL_Q1_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false' in v
assert 'NEXT_DERIVED_ROUTE=27-20-r301w' in v
assert qs['status']=='AUDITED_PASS_MERGED' and qs['audit_status']=='PASS' and qs['advance_allowed'] is True
assert reg['status']=='BATCH_SUBMITTED_PENDING_FRESH_AUDIT' and reg['audit_status']=='PENDING'
assert reg['merge_allowed'] is False and reg['advance_allowed'] is False and reg['fresh_reaudit_required'] is True
for name in ('Stage27-20-r301t','Stage27-20-r301u','Stage27-20-r301v'):
    e=ctl['derived_routes'][name]
    assert e['status']=='BATCH_SUBMITTED_PENDING_FRESH_AUDIT' and e['audit_status']=='PENDING'
    assert e['merge_allowed'] is False and e['advance_allowed'] is False
assert ctl['derived_routes']['Stage27-20-r301v']['next_derived_route']=='27-20-r301w'
assert ctl['checkpoint_status']['50']=='BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE'
assert ctl['state']['CURRENT_CHECKPOINT']==40 and ctl['state']['NEXT_CHECKPOINT']==40
assert ctl['state']['MAIN_STATUS']=='UPPER_REENTRY_STAGE27_19_R402C_F_BATCH_SUBMITTED_PENDING_FRESH_AUDIT'
assert ctl['stage20_r301_numbering_contract']['after_r301z']=='Stage27-20-r302-main-batch'
assert ctl['stage20_r301_numbering_contract']['r301aa_forbidden'] is True
print('Stage27-20-r301t-v verifier: PASS')
