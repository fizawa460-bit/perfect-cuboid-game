#!/usr/bin/env python3
"""Verify provisional exact Goal4AL class-B evaluation on U(R)^+."""
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage35-ex/35ex-35/goal4al-positive-real-class-b-evaluation.json'
SOURCE=ROOT/'stages/stage35-ex/35ex-35/goal4al-real-component-local-evaluation-preflight-source-lock.md'
DIAG=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4al_real_component_eval.py'
LOADER=ROOT/'stages/stage35-ex/35ex-35/goal4ak_explicit_fb.py'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
EXPECTED_CANONICAL='cd0830cf69988b3745eeb0d4725761ffd997696fcf3cb7329727087c1c709d56'
EXPECTED_SOURCE_BLOB='126d421ad93bddb24468828137acd184fa8f8a59'
EXPECTED_DIAG_BLOB='3ebdf6262a297dfa9c81f818d6e1795015cd550a'
EXPECTED_LOADER_BLOB='3c5814fd98375f1eeeefd33f7fb99d9c888fbb9a'
V74='STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED'

def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def canonical(o:dict)->str:
    x=dict(o); got=x.pop('canonical_sha256'); calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest(); assert got==calc==EXPECTED_CANONICAL,(got,calc); return got
assert blob(SOURCE)==EXPECTED_SOURCE_BLOB
assert blob(DIAG)==EXPECTED_DIAG_BLOB
assert blob(LOADER)==EXPECTED_LOADER_BLOB
state=json.loads(STATE.read_text())
assert state['schema']==V74
assert state['claims']['open_receiver_second_class_explicit_F_B_computed'] is True
assert state['claims']['open_receiver_second_class_local_evaluation_released'] is True
assert state['claims']['open_receiver_local_evaluations_computed'] is False
assert state['claims']['brauer_manin_obstruction_obtained'] is False
assert state['claims']['E1_proved'] is False
assert state['claims']['stage35_closed'] is False
cert=json.loads(CERT.read_text()); canonical(cert)
assert cert['source_provenance']['exact_head_sha']=='0cc56b2f9021824f1a6047dfb3f4f1a6f8dd3d0e'
assert cert['source_provenance']['aggregate_run']==34237581156
assert cert['source_provenance']['current_job']==102101438782
assert cert['off_diagonal_exact_probes']['sample_count']==6
assert cert['off_diagonal_exact_probes']['regular_sample_count']==6
assert cert['result']['common_F_B_sign']==-1
assert cert['result']['class_B_positive_real_component_invariant']=='1/2'
assert all(r['regular_for_fixed_FB'] and r['F_B_sign']==-1 and r['class_B_real_invariant']=='1/2' for r in cert['off_diagonal_exact_probes']['samples'])
assert all(v is False for v in cert['credit_firewall'].values())
cp=subprocess.run([sys.executable,'-B',str(DIAG)],text=True,capture_output=True,timeout=120)
if cp.returncode!=0: raise SystemExit(cp.stdout+'\n'+cp.stderr)
prefix='GOAL4AL_REAL_EVAL_JSON='; line=next((ln for ln in cp.stdout.splitlines() if ln.startswith(prefix)),None); assert line is not None
live=json.loads(line[len(prefix):])
assert live['schema']=='STAGE35_EX_GOAL4AL_CLASS_B_POSITIVE_REAL_COMPONENT_DIAGNOSTIC_V2'
assert live['regular_sample_count']==6
assert live['common_F_B_sign_on_regular_samples']==-1
assert live['class_B_positive_real_component_invariant']=='1/2'
assert live['samples']==cert['off_diagonal_exact_probes']['samples']
assert live['credit_firewall']['brauer_manin_obstruction_obtained'] is False
assert live['credit_firewall']['E1_proved'] is False
assert live['credit_firewall']['stage35_closed'] is False
print('STAGE35_EX_GOAL4AL_POSITIVE_REAL_CLASS_B_EVALUATION=PASS')
print('class_B_positive_real_component_invariant=1/2')
print('canonical_sha256='+EXPECTED_CANONICAL)
