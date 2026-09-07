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
BASE='fe7ef406a9987981fe5f79267f3f8a39f37a61e4'
BC_HEAD='5b15b0f9c7316cac76adf7b391fa2e873c8370d5'
BC_CI='34092194009/101647855514'
CERT_BLOB='5ee300e3a6765368c22aaf942180bb0a15aacf29'
LOCKS={BC:'f4223afb733ed3be112816f789d1d4ae10845249',CYCLE:'4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37',W01:'122a6c1c5c871c1c7b797017e854de8ec55e7c50',W02:'13d41be776fcd2edcd258f11bd28c5a6596de45b',W03:'1d5275321f42768a6414d4610ac912c63be43f96'}
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def main():
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BC_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']['36_09BC_exact_head']==BC_HEAD and c['batch_parent']['36_09BC_exact_head_ci']==BC_CI
    b=c['blind_rediscovery']
    assert b['performed_before_arsenal_comparison'] is True
    lenses=b['lenses']; assert len(lenses)==10
    ids={x['id'] for x in lenses}; assert len(ids)==10
    assert any(x['id']=='BLIND_FULL_CHARACTER_QUOTIENTS' and x['status']=='LIVE_SELECTED' for x in lenses)
    s=c['selection']; assert s['selected_next']=='36-09BE_FULL_MULTIQ_CHARACTER_QUOTIENT_INVENTORY_PREFLIGHT' and s['parallel_split'] is False
    e=c['cycle_exit']
    assert e['CYCLE_EXHAUSTIVE_VIEW_AUDIT'] is True and e['CYCLE_BLIND_REDISCOVERY'] is True and e['CYCLE_SPLIT_TRIGGERED'] is False
    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V92_36_09BD_CANDIDATE'
    bd=st['authority_frontier']['36-09BD']
    assert bd['EXHAUSTIVE_VIEW_AUDIT_COMPLETE'] is True and bd['BLIND_REDISCOVERY_COMPLETE'] is True
    assert bd['SELECTED_FULL_CHARACTER_QUOTIENT_INVENTORY'] is True
    assert st['current']['unit']=='36-09BE' and st['current']['36_09BE_entry_allowed'] is True
    assert st['claims']['receiver_emptiness_proved'] is False
    print('36-09BD verified: blind + exhaustive-view audit complete, 10 candidate lenses preserved/classified, full multiquadratic character-quotient inventory selected without parallel split.')
if __name__=='__main__': main()
