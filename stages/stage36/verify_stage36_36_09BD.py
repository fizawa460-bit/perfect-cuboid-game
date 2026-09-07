#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BD/exhaustive-view-audit-scaled-self-intersection.json'
BC=ROOT/'stages/stage36/36-09BC/boundary-neighborhood-open-local-no-loop-preflight.json'
CYCLE=ROOT/'docs/research-os/policies/cycle-exploration-safety-protocol.md'
W01=ROOT/'docs/arsenal/cards/formal/S31-W01.md'
W02=ROOT/'docs/arsenal/cards/formal/S34-W02.md'
W03=ROOT/'docs/arsenal/cards/formal/S34-W03.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='c52f88a671503ac9eb25c20186b4fb7729ba9112'
BC_HEAD='c8acd051f3d6b5537c9bd7220909b2f71306a870'
BC_CI='34094930848/101656307425'
CERT_BLOB='7bab7a7d0a8eba8ca9304abb862dbee784df030b'
LOCKS={BC:'317638c4d1a76f683c7af9bdb4e8285af35f4d05',CYCLE:'4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37',W01:'122a6c1c5c871c1c7b797017e854de8ec55e7c50',W02:'13d41be776fcd2edcd258f11bd28c5a6596de45b',W03:'1d5275321f42768a6414d4610ac912c63be43f96'}
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def main():
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BC_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    assert c['base_main_sha']==BASE
    assert c['audit_repair']['hostile_audit_review']==5128976664
    assert c['batch_parent']['36_09BC_exact_head']==BC_HEAD and c['batch_parent']['36_09BC_exact_head_ci']==BC_CI
    b=c['blind_rediscovery']; assert b['performed_before_arsenal_comparison'] is True
    lenses=b['lenses']; assert len(lenses)==10 and len({x['id'] for x in lenses})==10
    assert any(x['id']=='BLIND_FULL_CHARACTER_QUOTIENTS' and x['status']=='LIVE_SELECTED' for x in lenses)
    s=c['selection']; assert s['selected_next']=='36-09BE_FULL_MULTIQ_CHARACTER_QUOTIENT_INVENTORY_PREFLIGHT' and s['parallel_split'] is False
    e=c['cycle_exit']; assert e['CYCLE_EXHAUSTIVE_VIEW_AUDIT'] is True and e['CYCLE_BLIND_REDISCOVERY'] is True and e['CYCLE_SPLIT_TRIGGERED'] is False
    st=json.loads(STATE.read_text())
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    bd=st['authority_frontier']['36-09BD']
    assert bd['EXHAUSTIVE_VIEW_AUDIT_COMPLETE'] is True and bd['BLIND_REDISCOVERY_COMPLETE'] is True
    assert bd['SELECTED_FULL_CHARACTER_QUOTIENT_INVENTORY'] is True
    assert st['claims']['receiver_emptiness_proved'] is False
    print('36-09BD repaired provenance verified: breadth audit and blind rediscovery now lock the repaired BC exact-green parent.')
if __name__=='__main__': main()
