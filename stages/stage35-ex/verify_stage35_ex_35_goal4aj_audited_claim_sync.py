#!/usr/bin/env python3
"""Verify V73 audited Goal4AJ claim synchronization without granting F_B/E1 credit.

When V74 is live, replay the immutable V73 state snapshot instead of requiring the
mutable live MAIN-STATE to remain V73. This keeps the historical Goal4AJ verifier
usable after the audited Goal4AK authority transition.
"""
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
LIVE_STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V73_SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V73-84a9906500e2.json'
SYNC=ROOT/'stages/stage35-ex/35ex-35/goal4aj-audited-claim-sync.json'
EQ=ROOT/'stages/stage35-ex/35ex-35/goal4aj-degree31-literal-numerator-divisor-equality.json'
DEN=ROOT/'stages/stage35-ex/35ex-35/goal4aj-degree31-denominator-source-lock.md'
QVERIFY=ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4aj_qcandidate_chunks.py'
EQVERIFY=ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4aj_literal_numerator_divisor_equality.py'
LEGACY=ROOT/'stages/stage35-ex/verify_stage35_ex_v73_legacy_replay.py'
V74LEGACY=ROOT/'stages/stage35-ex/verify_stage35_ex_v74_legacy_replay.py'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V72-e98b06455d34.json'
V73='STAGE35_EX_PESCH_E1_STATE_V73_GOAL4AJ_LITERAL_DEGREE31_SECTIONS_AUDITED_EXPLICIT_F_B_PENDING'
V74='STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED'
EXPECTED_SYNC_CANONICAL='3fc9114234e2dfe91b41fa3be43e40da7e32d8a60184ddaeb25034f905fc9cfc'
EXPECTED_NUM='358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb'
EXPECTED_DEN='28d738a7a23df1ace371cabe3a476c270a54c6b7798e8172bd7111b14e25fc29'
EXPECTED_EQ='7ef8ce746f44ed729a3c87d21d6b5be4e7e711a4af087233951dd4ee80a20da9'

live=json.loads(LIVE_STATE.read_text())
if live['schema']==V73:
    STATE=LIVE_STATE
    replay_mode='LIVE_V73'
elif live['schema']==V74:
    STATE=V73_SNAP
    replay_mode='V74_PERSISTED_V73'
else:
    raise AssertionError(('unsupported live schema',live.get('schema')))

EXPECTED_BLOBS={
 STATE:'9dfb9f44b1c84ae774f80ce5021193a5d6cd8807',
 SYNC:'498a1e7554a8016863a6518cde91edd591f20b38',
 EQ:'a60034bb2b2e3cbd16d96fa26b76eeaf1210900f',
 DEN:'95c0eef4a420234964217d3ceb41e57ea5e5b95d',
 QVERIFY:'d000c3e65ffcb3e00d2dee8b7161a9dd0b4e4716',
 EQVERIFY:'8a52d7f2c51dc69a9e6bf8a70864cf0f5afe66be',
 LEGACY:'35c48142c2bbee20087e38768c6a7dd5a422014e',
 SNAP:'0f1bad646ad2b9667431e18519bc5379b70a8631',
}

def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def canonical(obj:dict)->str:
    x=dict(obj); got=x.pop('canonical_sha256')
    calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert calc==got
    return got

def run(path:Path,*args:str,marker:str)->None:
    cp=subprocess.run([sys.executable,'-B',str(path),*args],text=True,capture_output=True,timeout=300)
    if cp.returncode!=0: raise SystemExit(cp.stdout+'\n'+cp.stderr)
    assert marker in cp.stdout,(path,marker,cp.stdout)

for p,h in EXPECTED_BLOBS.items(): assert blob(p)==h,(p,blob(p),h)

s=json.loads(STATE.read_text())
assert s['schema']==V73
assert s['status']=='ACTIVE_RESEARCH_AUDITED_INTERMEDIATE_NO_E1_CREDIT'
assert s['history_snapshot']['hostile_review_id']==5134464420
assert s['last_audited_authority']['hostile_review_id']==5140644783
assert s['last_audited_authority']['pr']==1698
assert s['last_audited_authority']['exact_head_sha']=='2f3ea24388e1557e8288064677c8daa2d2a77212'
assert s['last_audited_authority']['merge_sha']=='e98b06455d34bf2f346d297d9370e82fc2a71970'
assert s['current']['next']=='35EX-35_GOAL4AK_SECOND_CLASS_QI_CYCLIC_EXPLICIT_F_B_ASSEMBLY_PREFLIGHT'
assert s['claims']['goal4aj_executed'] is True
assert s['claims']['open_receiver_second_class_degree31_literal_sections_materialized'] is True
assert s['claims']['open_receiver_second_class_degree31_literal_numerator_materialized'] is True
assert s['claims']['open_receiver_second_class_degree31_literal_denominator_materialized'] is True
assert s['claims']['open_receiver_second_class_degree31_numerator_target_divisor_equality_proved'] is True
assert s['claims']['open_receiver_second_class_explicit_F_B_ready_for_assembly'] is True
assert s['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert s['claims']['open_receiver_local_evaluations_computed'] is False
assert s['claims']['brauer_manin_obstruction_obtained'] is False
assert s['claims']['E1_proved'] is False and s['claims']['stage35_closed'] is False
assert s['claims']['perfect_cuboid_existence_claim'] is False and s['claims']['perfect_cuboid_nonexistence_claim'] is False

c=json.loads(SYNC.read_text())
assert canonical(c)==EXPECTED_SYNC_CANONICAL
assert c['parent_goal4ai_audit']['hostile_review_id']==5134464420
assert c['goal4aj_audit']['hostile_review_id']==5140644783
assert c['goal4aj_audit']['hostile_audit_pass'] is True
assert c['literal_sections']['numerator_materialized'] is True
assert c['literal_sections']['numerator_sha256']==EXPECTED_NUM
assert c['literal_sections']['numerator_target_divisor_equality_proved'] is True
assert c['literal_sections']['numerator_equality_canonical_sha256']==EXPECTED_EQ
assert c['literal_sections']['denominator_materialized'] is True
assert c['literal_sections']['denominator_sha256']==EXPECTED_DEN
assert c['credit_firewall']['explicit_F_B_materialized'] is False
assert c['credit_firewall']['local_evaluations_computed'] is False
assert c['credit_firewall']['brauer_manin_obstruction_obtained'] is False
assert c['credit_firewall']['E1_proved'] is False

# Recheck permanent Q bytes and audited numerator divisor equality.
run(QVERIFY,marker='STAGE35_EX_GOAL4AJ_QCANDIDATE_CHUNKS=PASS')
run(EQVERIFY,marker='STAGE35_EX_GOAL4AJ_LITERAL_NUMERATOR_DIVISOR_EQUALITY=PASS')
# Recheck the previous live authority under immutable history. Under V74, use the
# V74 snapshot adapter so the subprocess does not read mutable V74 as if it were V73.
if replay_mode=='LIVE_V73':
    run(LEGACY,'35g4ai',marker='PASS V73_PERSISTED_V72_REPLAY_35g4ai')
else:
    run(V74LEGACY,'35g4ai',marker='PASS V74_PERSISTED_V73_REPLAY_35g4ai')

d=DEN.read_text()
assert 'q31_den = q19 * c * b1^11' in d
assert EXPECTED_DEN in d
assert 'term count: `1542`' in d
assert 'maximum absolute coefficient: `11188`' in d

print(f'PASS Stage35-EX V73 Goal4AJ claim sync replay mode={replay_mode}; explicit F_B/local/BM/E1 remain pending')
