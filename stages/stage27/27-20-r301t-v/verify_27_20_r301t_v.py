from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
S=ROOT/'stages'/'stage27'
t=(S/'27-20-r301t'/'result.md').read_text(); u=(S/'27-20-r301u'/'result.md').read_text(); v=(S/'27-20-r301v'/'result.md').read_text()
reg=json.loads((S/'27-20-r301t-v'/'batch-registry.json').read_text()); qs=json.loads((S/'27-20-r301q-s'/'batch-registry.json').read_text()); ctl=json.loads((S/'27-controller.json').read_text())
audit=(S/'27-20-r301t-v'/'audit.md').read_text()
assert 'STATUS=AUDITED_PASS_MERGED' in t and 'STAGE27_20_R301T_STATUS=AUDITED_PASS_MERGED' in t
assert 'STATUS=AUDITED_PASS_MERGED' in u and 'STAGE27_20_R301U_STATUS=AUDITED_PASS_MERGED' in u
assert 'STATUS=AUDITED_PASS_MERGED' in v and 'STAGE27_20_R301V_STATUS=AUDITED_PASS_MERGED' in v
assert 'Q1_TO_STAGE14_FACE_MOBIUS_ADAPTER_PROVED=true' in t
assert 'Q1_TO_ACTIVE_FACE_SUPPORT_INJECTION_PROVED=true' in t
assert 'Q1_EQUALS_ALL_STAGE14_ACTIVE_VERTICES_CLAIMED=false' in t
assert 'OFF_WALL_FIXED_DISTANCE_SUPPORT_SAVING_PROVED=true' in u
assert 'OFF_WALL_NONPROPORTIONAL_BOUND=B^(1/2-2eta+o(1))' in u
assert 'OFF_WALL_PROPORTIONAL_BOUND=B^(7/16+o(1))' in u
assert 'OFF_WALL_Q1_BOUND=B^(1/2-min(2eta,1/16)+o(1))' in u
assert 'OFF_WALL_J_BOUND=B^(1/2-min(2eta,1/16)+o(1))' in u
assert 'CRITICAL_THETA=1/4' in u
assert 'CRITICAL_PHI_RANGE=[1/8,1/4]' in v
assert 'CRITICAL_CHI_FORMULA=2phi-1/4' in v
assert 'CRITICAL_E_K_UPPER_BOUND=1/2' in v and 'CRITICAL_E_RRF_UPPER_BOUND=1/2' in v
assert 'CRITICAL_ACTUAL_SATURATION_PROVED=false' in v
assert 'CRITICAL_Q1_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false' in v
assert 'NEXT_DERIVED_ROUTE=27-20-r301w' in v
assert qs['status']=='AUDITED_PASS_MERGED' and qs['audit_status']=='PASS' and qs['advance_allowed'] is True
assert reg['status']=='AUDITED_PASS_MERGED' and reg['audit_status']=='PASS'
assert reg['merge_allowed'] is True and reg['advance_allowed'] is True and reg['fresh_reaudit_required'] is False
assert reg['final_audit_verdict']=='PASS' and reg['merged'] is True and reg['pr']==1052
assert reg['merge_commit']=='1d6524bf98138aaf76b038eb50fda02f9f4e5ee0'
assert reg['audit_record']=='stages/stage27/27-20-r301t-v/audit.md'
assert 'AUDIT_VERDICT=PASS' in audit and 'MERGE_ALLOWED=true' in audit
assert 'NEXT_DERIVED_ROUTE=27-20-r301w' in audit
assert ctl['checkpoint_status']['50']=='BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE'
assert ctl['state']['CURRENT_CHECKPOINT']==40 and ctl['state']['NEXT_CHECKPOINT']==40
assert ctl['stage20_r301_numbering_contract']['after_r301z']=='Stage27-20-r302-main-batch'
assert ctl['stage20_r301_numbering_contract']['r301aa_forbidden'] is True
print('Stage27-20-r301t-v audited closeout verifier: PASS')
