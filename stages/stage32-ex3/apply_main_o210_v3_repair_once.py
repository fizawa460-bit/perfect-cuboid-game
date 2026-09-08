#!/usr/bin/env python3
from __future__ import annotations
import copy, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
REG=ROOT/'stages/stage32/proof/CLAIM-REGISTRY.json'
ACTIVE=ROOT/'stages/stage32/proof/ACTIVE-FRONTIER.json'
LANES=ROOT/'stages/stage32/proof/LANE-ADAPTERS.json'
AV=ROOT/'stages/stage32/proof/verify_stage32_active_frontier.py'
STATE=ROOT/'stages/stage32-ex3/MAIN-STATE.json'
REPLAY=ROOT/'.github/workflows/stage32ex3-ex3-09-retained-exact-replay.yml'
ART=ROOT/'stages/stage32-ex3/main-o210-exclusion-v3-candidate.json'
VER=ROOT/'stages/stage32-ex3/verify_main_o210_exclusion_v3_candidate.py'

V2='S32.O210.EXCLUSION.V2'
V3='S32.O210.EXCLUSION.V3'
CTX='S32.MAIN.CURRENT_TARGET_CONTEXT.V1'
EX3='S32.EX3.O210_COVER_GEOMETRY_EXCLUSION_TERMINAL.V1'
AD='S32.ADAPTER.EX3_O210_TO_MAIN_O210.V3'
V2_CORE='178c0a8a381abacbfb5662f44f2faab2f2f6076f4be653172f7e586f77476746'
FAIL_REVIEW=5144919736
FAIL_HEAD='81ec62fc8413840fcb18936b9244e32b171c90b1'
FIXED={'row_id':'g1-d186','picard_class':'V6','O':210,'qprime':4,'target':'population_wide_exclusion'}
CORE_KEYS=['claim_id','kind','statement','scope_key','scope','proves','does_not_prove','requires','source_locks','replay_verifier']
def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

reg=json.loads(REG.read_text())
reg_by={c['claim_id']:c for c in reg['claims']}
assert V2 not in reg_by and V3 not in reg_by
assert reg_by[EX3]['authority_status']=='AUDITED' and reg_by[EX3]['audit_receipt']['review_id']==5141988194
assert reg_by[AD]['authority_status']=='AUDITED' and reg_by[AD]['audit_receipt']['review_id']==5143014619

active=json.loads(ACTIVE.read_text()); active_before=copy.deepcopy(active)
idx=next(i for i,c in enumerate(active['claims']) if c['claim_id']==V2)
old=copy.deepcopy(active['claims'][idx])
assert old['authority_status']=='PROVISIONAL' and old['audit_receipt'] is None
assert old['claim_core_sha256']==V2_CORE
assert old['scope']==FIXED and old['requires']==[CTX,EX3,AD]

historical={k:v for k,v in old.items() if k not in {'frontier_status','blockers','lane_links'}}
historical['authority_status']='SUPERSEDED'
historical['audit_receipt']=None
assert historical['claim_core_sha256']==csha({k:historical[k] for k in CORE_KEYS})==V2_CORE
reg['claims'].append(historical)

new={
  'claim_id':V3,
  'kind':'mathematical_claim',
  'statement':'Under the exact g1-d186, V6, qprime=4 Stage32 target semantics, the full O=210 carrier/cover population is excluded by the population-wide Stage32EX3 terminal exclusion transported through the exact EX3-to-MAIN population-identity adapter V3.',
  'scope_key':'S32.O210.COVER',
  'scope':FIXED,
  'proves':['O210 is excluded for the exact registered Stage32 target population.'],
  'does_not_prove':['It does not exclude Q602 or alter the audited survivor set [73,97,235].','It does not assert any result outside the exact registered O210 target population.','It does not prove Stage32 closure or any Perfect Cuboid endpoint.'],
  'requires':[CTX,EX3,AD],
  'source_locks':copy.deepcopy(old['source_locks']),
  'replay_verifier':'stages/stage32-ex3/verify_main_o210_exclusion_v3_candidate.py',
  'authority_status':'PROVISIONAL',
  'audit_receipt':None,
  'frontier_status':'ACTIVE_INCOMPLETE',
  'blockers':['Hostile audit of the explicit MAIN O210 V3 claim has not yet been performed.'],
  'lane_links':copy.deepcopy(old['lane_links'])
}
new['claim_core_sha256']=csha({k:new[k] for k in CORE_KEYS})
CORE=new['claim_core_sha256']
assert 'PROVISIONAL' not in new['statement']
assert all('PROVISIONAL' not in x and 'AUDITED' not in x and 'hostile-audit' not in x.lower() for x in new['proves']+new['does_not_prove'])
active['claims'][idx]=new
before_by={c['claim_id']:c for c in active_before['claims']}; after_by={c['claim_id']:c for c in active['claims']}
for cid,obj in before_by.items():
    if cid!=V2: assert after_by[cid]==obj, cid
ACTIVE.write_text(json.dumps(active,separators=(',',':'))+'\n')
REG.write_text(json.dumps(reg,separators=(',',':'))+'\n')

lanes=json.loads(LANES.read_text()); lanes_before=copy.deepcopy(lanes); touched=[]
for lane in lanes['lanes']:
    refs=lane.get('active_frontier_refs',[])
    if V2 in refs:
        assert lane['lane'] in {'MAIN','EX3'}
        lane['active_frontier_refs']=[V3 if x==V2 else x for x in refs]
        touched.append(lane['lane'])
assert sorted(touched)==['EX3','MAIN']
ex3lane=next(x for x in lanes['lanes'] if x['lane']=='EX3')
ex3lane['notes']=('EX3 terminal O210 exclusion and drift-robust adapter V3 are AUDITED. MAIN O210 claim V2 failed hostile audit only because its immutable core mixed authority-state language into DOES_NOT_PROVE (review 5144919736); V2 is historical SUPERSEDED provenance. Active MAIN O210 routing now uses authority-neutral S32.O210.EXCLUSION.V3 as PROVISIONAL pending narrow hostile re-audit. No MAIN O210 credit exists before PASS receipt synchronization.')
before={x['lane']:x for x in lanes_before['lanes']}; after={x['lane']:x for x in lanes['lanes']}
for lane,obj in before.items():
    if lane not in {'MAIN','EX3'}: assert after[lane]==obj, lane
LANES.write_text(json.dumps(lanes,indent=2)+'\n')

av=AV.read_text()
assert av.count('"S32.O210.EXCLUSION.V2"')==1
AV.write_text(av.replace('"S32.O210.EXCLUSION.V2"','"S32.O210.EXCLUSION.V3"'))

art={
  'schema':'STAGE32_MAIN_O210_EXCLUSION_V3_CANDIDATE_V1',
  'status':'RETAINED_PROVISIONAL_MAIN_O210_EXCLUSION_V3_NARROW_REAUDIT_PENDING',
  'role':'MAIN_ACTIVE_FRONTIER_MATHEMATICAL_CLAIM_CANDIDATE_AUTHORITY_NEUTRAL_CORE',
  'target':{'row_id':'g1-d186','picard_class':'V6','O':210,'qprime':4,'Q':602,'surviving_marked_residues':[73,97,235],'population_scope':'population_wide_exclusion'},
  'claim_binding':{'claim_id':V3,'claim_core_sha256':CORE,'immutable_statement_proves_does_not_prove_authority_state_neutral':True},
  'proof_binding':{
    'target_context_claim_id':CTX,'target_context_core_sha256':'cb3aa4b36332cda9d960103972e7235d3cf7b1bc41fcefc99f19a050a7ab2f14',
    'ex3_terminal_claim_id':EX3,'ex3_terminal_core_sha256':'78399b9797723b4134198b2f4b2dc3ed3024897b7ad128d1f0621e1e85cf8102','ex3_terminal_audit_receipt':{'status':'PASS','pr':1714,'review_id':5141988194,'exact_head':'8da8d4cd932c5c9b82dfd0c304638e866c656069'},
    'promotion_adapter_claim_id':AD,'promotion_adapter_core_sha256':'55505658e272ec7d60372f2d67cb93c9c007d782145f18d5ef9d2c1146582c88','promotion_adapter_audit_receipt':{'status':'PASS','pr':1714,'review_id':5143014619,'exact_head':'280595ed892ae2ef70e049a3f722ea024452e206'}
  },
  'derivation':{'ex3_terminal_excludes_every_hypothetical_fixed_target_carrier':True,'audited_v3_identifies_ex3_population_with_main_o210_population':True,'therefore_main_o210_population_exclusion_is_supported':True,'no_additional_finite_search_or_monodromy_restriction_used':True,'q602_survivors_are_obstruction_evidence_not_population_filter':True},
  'v2_audit_history':{'result':'FAIL_CLAIM_VERSIONING_ONLY','review_id':FAIL_REVIEW,'exact_head':FAIL_HEAD,'mathematical_dependency_chain':'PASS','repair':'new authority-state-neutral V3 core; V2 immutable core not mutated'},
  'source_locks':{
    'ex3_terminal_artifact':{'path':'stages/stage32-ex3/ex3-09-o210-cover-geometry-exclusion-candidate.json','blob_sha1':'0114531c52730730e9a35ad1c8d8aea21eed03e9','canonical_sha256':'9244f82daef79306abe99d8a3ccee111c80c4c057f1b5f7df3bafd5500d8ca21'},
    'v3_adapter_artifact':{'path':'stages/stage32-ex3/ex3-10-main-o210-promotion-adapter-candidate-v3.json','blob_sha1':'dd548d20e4f9bd007395606a5450d1ffc964cde9','canonical_sha256':'63dc72b89f59709fcce13cbc4e9c777819a419f7b6213a6ccd2c7c5977fce37c'}
  },
  'credit_ceiling':{'main_o210_claim_candidate_retained':True,'main_o210_claim_hostile_audited':False,'main_o210_excluded':False,'q602_excluded':False,'stage32_main_credit':False,'o212_plus_advance_allowed':False,'stage32_closed':False,'endpoint_credit':False}
}
art['canonical_sha256_without_this_field']=csha(art)
ART.write_text(json.dumps(art,indent=2)+'\n')
ART_CANON=art['canonical_sha256_without_this_field']

verifier=f'''#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'stages/stage32-ex3/main-o210-exclusion-v3-candidate.json'
REG = ROOT / 'stages/stage32/proof/CLAIM-REGISTRY.json'
ACTIVE = ROOT / 'stages/stage32/proof/ACTIVE-FRONTIER.json'
STATE = ROOT / 'stages/stage32-ex3/MAIN-STATE.json'
CID='{V3}'
OLD='{V2}'
CTX='{CTX}'
EX3='{EX3}'
AD='{AD}'
CORE='{CORE}'
ART_CANON='{ART_CANON}'
CORE_KEYS={CORE_KEYS!r}
FIXED={FIXED!r}
def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def bsha(data:bytes): return hashlib.sha1(f"blob {{len(data)}}\\0".encode()+data).hexdigest()
def canonical(path:Path):
    obj=json.loads(path.read_text()); stored=obj['canonical_sha256_without_this_field']; stripped=dict(obj); stripped.pop('canonical_sha256_without_this_field',None); assert csha(stripped)==stored; return stored
a=json.loads(ART.read_text())
assert a['schema']=='STAGE32_MAIN_O210_EXCLUSION_V3_CANDIDATE_V1'
assert canonical(ART)==ART_CANON
assert a['claim_binding']=={{'claim_id':CID,'claim_core_sha256':CORE,'immutable_statement_proves_does_not_prove_authority_state_neutral':True}}
assert a['v2_audit_history']['review_id']==5144919736 and a['v2_audit_history']['result']=='FAIL_CLAIM_VERSIONING_ONLY'
for name,lock in a['source_locks'].items():
    p=ROOT/lock['path']; data=p.read_bytes(); assert bsha(data)==lock['blob_sha1'], name
    if 'canonical_sha256' in lock: assert canonical(p)==lock['canonical_sha256'], name
reg=json.loads(REG.read_text()); by={{c['claim_id']:c for c in reg['claims']}}
assert by[CTX]['claim_core_sha256']==a['proof_binding']['target_context_core_sha256']
assert by[EX3]['authority_status']=='AUDITED' and by[EX3]['audit_receipt']==a['proof_binding']['ex3_terminal_audit_receipt']
assert by[AD]['authority_status']=='AUDITED' and by[AD]['audit_receipt']==a['proof_binding']['promotion_adapter_audit_receipt']
assert by[OLD]['authority_status']=='SUPERSEDED' and by[OLD]['audit_receipt'] is None
assert by[OLD]['claim_core_sha256']=='{V2_CORE}'
active=json.loads(ACTIVE.read_text()); claims={{c['claim_id']:c for c in active['claims']}}
assert OLD not in claims and CID in claims
c=claims[CID]
assert c['kind']=='mathematical_claim' and c['scope_key']=='S32.O210.COVER' and c['scope']==FIXED
assert c['requires']==[CTX,EX3,AD]
assert c['lane_links']==[{{'lane':'MAIN','role':'OWNER'}},{{'lane':'EX3','role':'ATTACKS'}}]
assert c['replay_verifier']=='stages/stage32-ex3/verify_main_o210_exclusion_v3_candidate.py'
assert c['claim_core_sha256']==CORE==csha({{k:c[k] for k in CORE_KEYS}})
assert 'PROVISIONAL' not in c['statement']
assert all('PROVISIONAL' not in x and 'AUDITED' not in x and 'hostile-audit' not in x.lower() for x in c['proves']+c['does_not_prove'])
assert c['authority_status'] in {{'PROVISIONAL','AUDITED'}}
if c['authority_status']=='PROVISIONAL':
    assert c['audit_receipt'] is None and c['frontier_status']=='ACTIVE_INCOMPLETE'
    assert c['blockers']==['Hostile audit of the explicit MAIN O210 V3 claim has not yet been performed.']
else:
    assert c['audit_receipt']['status']=='PASS' and c['frontier_status']=='AUDITED_TRUE' and c['blockers']==[]
for lock in c['source_locks']:
    assert lock['path'] not in {{'stages/stage32/MAIN-STATE.json','stages/stage32/proof/ACTIVE-FRONTIER.json','stages/stage32-ex3/MAIN-STATE.json'}}
state=json.loads(STATE.read_text())
assert state['candidate_frontier']['main_o210_active_claim_id']==CID
assert state['candidate_frontier']['main_o210_v3_core_sha256']==CORE
if c['authority_status']=='PROVISIONAL':
    assert state['credit']['O210_excluded'] is False and state['credit']['stage32_main_credit'] is False
    assert state['firewalls']['O210_excluded'] is False and state['firewalls']['O212_plus_advance_allowed'] is False
print('PASS Stage32 MAIN O210 exclusion V3 authority-neutral candidate')
print(json.dumps({{'claim_id':CID,'claim_core_sha256':CORE,'authority':c['authority_status'],'frontier_status':c['frontier_status']}},sort_keys=True))
'''
VER.write_text(verifier)

state=json.loads(STATE.read_text())
assert state['candidate_frontier']['main_o210_active_claim_id']==V2
assert state['credit']['O210_excluded'] is False and state['credit']['stage32_main_credit'] is False
state['schema']='STAGE32EX3_MAIN_COMPACT_STATE_V1_MAIN_O210_V3_AUTHORITY_NEUTRAL_NARROW_REAUDIT_PENDING'
state['current'].update({'status':'MAIN_O210_V3_PROVISIONAL_ACTIVE_NARROW_REAUDIT_PENDING','subroute':'MAIN_O210_V3_NARROW_HOSTILE_REAUDIT_HANDOFF','objective':'Narrow hostile re-audit of authority-state-neutral S32.O210.EXCLUSION.V3; mathematical dependencies were PASS in V2 audit, but no MAIN credit exists before V3 PASS receipt synchronization.','next_route_on_success':'MAIN_O210_V3_PASS_RECEIPT_SYNC_THEN_AUTHORITY_TRANSITION','next_route_on_block':'REPAIR_MAIN_O210_V3_WITH_AUDITED_EX3_V3_PRESERVED','stop_semantics':'V3_PROVISIONAL_ONLY_O210_EXCLUDED_FALSE_NO_O212_ADVANCE_NO_MERGE'})
cf=state['candidate_frontier']; cf.update({'main_o210_active_claim_id':V3,'main_o210_v3_core_sha256':CORE,'main_o210_v3_registered_provisional':True,'main_o210_v3_hostile_audited':False,'main_o210_v2_superseded_after_hostile_audit_fail':True,'main_o210_v2_fail_review_id':FAIL_REVIEW,'main_o210_v2_fail_exact_head':FAIL_HEAD})
if 'main_o210_v2' in state:
    state['main_o210_v2'].update({'status':'HOSTILE_AUDIT_FAIL_CLAIM_VERSIONING_ONLY_SUPERSEDED','hostile_audit_result':'FAIL','hostile_audit_review_id':FAIL_REVIEW,'hostile_audited_exact_head':FAIL_HEAD,'main_O210_promotion_complete':False,'credit_ceiling':'HISTORICAL_PROVISIONAL_FAILED_VERSION_NO_MAIN_CREDIT'})
state['main_o210_v3']={'status':'RETAINED_PROVISIONAL_ACTIVE_AUTHORITY_NEUTRAL_CLAIM_NARROW_REAUDIT_PENDING','claim_id':V3,'claim_core_sha256':CORE,'requires':[CTX,EX3,AD],'hostile_audit_required':True,'hostile_audit_result':None,'main_O210_promotion_complete':False,'credit_ceiling':'PROVISIONAL_MAIN_O210_ACTIVE_CLAIM_ONLY_NO_O210_EXCLUSION_CREDIT'}
mg=state['management']; mg.update({'claim_sync_trigger':'ACTIVE_FRONTIER_REMAP','claim_sync_status':'COMPLETE_MAIN_O210_V3_AUTHORITY_NEUTRAL_PROVISIONAL_REMAP_NARROW_REAUDIT_PENDING_NO_MAIN_CREDIT','active_frontier_remap_claim_id':V3,'active_frontier_remap_authority':'PROVISIONAL','main_o210_v3_hostile_audit_required':True,'main_o210_v2_hostile_audit_result':'FAIL_CLAIM_VERSIONING_ONLY','main_o210_v2_hostile_audit_review_id':FAIL_REVIEW})
for p in ['stages/stage32-ex3/main-o210-exclusion-v3-candidate.json','stages/stage32-ex3/verify_main_o210_exclusion_v3_candidate.py']:
    if p not in state['current_leaf_working_set']: state['current_leaf_working_set'].append(p)
for key in ['stage32_main_credit','Q602_excluded','O210_excluded','receiver_credit','theorem_credit','endpoint_credit']: assert state['credit'][key] is False
for key in ['stage32_main_credit','Q602_excluded','O210_excluded','O212_plus_advance_allowed','stage32_closed']: assert state['firewalls'][key] is False
STATE.write_text(json.dumps(state,indent=2)+'\n')

replay=REPLAY.read_text()
replay=replay.replace('MAIN O210 V2 audit handoff','MAIN O210 V3 narrow re-audit handoff')
replay=replay.replace('MAIN O210 V2 candidate','MAIN O210 V3 authority-neutral candidate')
assert replay.count('python stages/stage32-ex3/verify_main_o210_exclusion_v2_candidate.py')==1
replay=replay.replace('python stages/stage32-ex3/verify_main_o210_exclusion_v2_candidate.py','python stages/stage32-ex3/verify_main_o210_exclusion_v3_candidate.py')
REPLAY.write_text(replay)

print('MAIN_O210_V3_CORE',CORE)
print('MAIN_O210_V3_ARTIFACT_CANON',ART_CANON)
print('V2_FAIL_REVIEW',FAIL_REVIEW)
