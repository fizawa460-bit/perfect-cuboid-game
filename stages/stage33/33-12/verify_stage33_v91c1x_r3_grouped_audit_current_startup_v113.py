#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
STATE_SHA='bf00eda9927064a14562a91df106af999b292d42f6c2d5305225d8a6542a9528'
R3_SHA='e631d91eaa40a9f73b33e53ceff25745824f8ad6380d88d956424e29e9bd040e'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
    o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o

s=load(S33/'MAIN-STATE.json',STATE_SHA)
r3=load(HERE/'e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json',R3_SHA)
assert s['candidate_audit_gate']['candidate']=='V91C1X_R3_COVER_INDEXED_A2_02_REPRESENTATIVE_BOUNDED_PREFLIGHT'
assert s['candidate_audit_gate']['status']=='PENDING_GROUPED_HOSTILE_AUDIT_R1_R2_R3'
assert s['authority_audit_gate']['authority']=='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'
assert s['authority_audit_gate']['hostile_audit_verdict']=='PASS'
assert s['execution_gate']['advance_allowed'] is False
assert s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1678_GROUPED_V91C1X_R1_R2_R3_EXACT_HEAD'
assert s['stage33_progress']=='6/11'
assert r3['audit_checkpoint']['mathematically_substantial_checkpoint'] is True
assert r3['exact_bounded_consequence']['repository_wide_absence_claim'] is False
assert r3['exact_bounded_consequence']['route_mathematically_impossible'] is False
subprocess.run([sys.executable,str(S33/'sync_main_state.py'),'--check'],check=True)
print(json.dumps({'success':True,'marker':'V113_R3_GROUPED_AUDIT_CURRENT_STARTUP','state_sha256':STATE_SHA,'candidate_sha256':R3_SHA,'advance_allowed':False,'stage33_progress':'6/11'},sort_keys=True))
