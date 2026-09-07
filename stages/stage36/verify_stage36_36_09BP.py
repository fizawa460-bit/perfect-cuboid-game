#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BP/full-cover-global-descent-router-preflight.json'
BO=ROOT/'stages/stage36/36-09BO/q-reservoir-full-qq-cancellation-preflight.json'
BOV=ROOT/'stages/stage36/verify_stage36_36_09BO.py'
DISC=ROOT/'docs/research-os/policies/repository-asset-discovery.md'
FW=ROOT/'docs/research-os/policies/research-credit-and-promotion-firewalls.md'
CARD=ROOT/'docs/arsenal/cards/formal/S34-W01.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='727b3f34c4d850e868aff64483aeb99861b13c7c'
AUDITED_HEAD='40210e1f9225c792eca479f3f56bed73f550e024'
CERT_BLOB='fa29295bcc1072c9ed9608bc79be82993b2b657c'
LOCKS={
 BO:'138749fde9766cd217fcb4622ccdebcb45730c2e',
 BOV:'42dcbb35b29ddacd78fa8ce0430098c4c98124a3',
 DISC:'bf001d4ff4375281a901d52c147c35c28643b8a3',
 FW:'7a3de0b2692afe4fb25b6825b31bd0384a118a41',
 CARD:'01a8e90e34b4aa46edbfa825803d488e5230e9d0',
}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bo=json.loads(BO.read_text()); card=CARD.read_text(); fw=FW.read_text()
    assert c['base_main_sha']==BASE
    ap=c['audited_parent']
    assert ap['pr']==1691 and ap['failed_audit_review']==5130678946 and ap['hostile_reaudit_review']==5130920000
    assert ap['audited_exact_head']==AUDITED_HEAD
    assert ap['exact_head_ci']=='34111088276/101707255576'
    assert ap['merged_main_sha']==BASE
    assert ap['accepted_aggregate']=='NO_PARAMETER_SHRINK_ESTABLISHED_AT_CURRENT_CHECKPOINT'
    assert bo['route_result']['route_status']=='NO_PARAMETER_SHRINK_ESTABLISHED_AT_CURRENT_CHECKPOINT'
    assert bo['route_result']['local_parameter_elimination_route_exhausted'] is False

    w=c['selected_weapon']; h=c['stage36_hypothesis_audit']; gap=c['exact_gap']; rr=c['route_result']
    assert w['id']=='S34-W01' and w['maturity']=='FORMAL' and w['role']=='SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT'
    assert '| Role | `SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT` |' in card
    assert 'proof that every receiver point enters one enumerated squareclass branch' in card
    assert 'finite exhaustive branch family representing the receiver' in card
    assert 'finite over-cover != receiver closure' in card
    assert 'A bounded result is authoritative only on its certified bounded domain' in fw
    assert h['every_receiver_point_enters_one_enumerated_squareclass_branch']=='NOT_ESTABLISHED'
    assert h['uniform_finite_squareclass_family_over_all_parameters']=='NOT_ESTABLISHED'
    assert h['full_S34_W01_applicability_proved'] is False
    assert gap['uniform_symbolic_branch_types_may_be_finite'] is True
    assert gap['fixed_finite_Q_squareclass_twist_family_follows_automatically'] is False
    assert rr['route_status']=='PASS_ROUTER_MATCH_ONLY_EXHAUSTIVE_BRANCH_ADAPTER_REQUIRED'
    assert rr['S34_W01_shape_match'] is True
    assert rr['finite_exhaustive_squareclass_branch_family_obtained'] is False
    assert rr['finite_exhaustive_H1_twist_family_obtained'] is False
    assert rr['candidate_parameter_set_shrunk'] is False and rr['receiver_closed'] is False
    assert rr['next_leaf']=='36-09BQ_RELATIVE_FACTOR_SQUARECLASS_BRANCH_EXHAUSTIVENESS_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V105_36_09BP_GLOBAL_DESCENT_ROUTER'
    hist=st['audited_history']['36-09BH-BO']
    assert hist['status']=='AUDITED_MERGED_AUTHORITY'
    assert hist['hostile_reaudit_review']==5130920000
    assert hist['audited_exact_head']==AUDITED_HEAD
    assert hist['merged_main_sha']==BASE
    bp=st['authority_frontier']['36-09BP']
    assert bp['certificate_blob_sha']==CERT_BLOB
    assert bp['S34_W01_SHAPE_MATCH'] is True
    assert bp['EXHAUSTIVE_BRANCH_ADAPTER_MISSING'] is True
    assert bp['FINITE_EXHAUSTIVE_SQUARECLASS_FAMILY'] is False
    assert bp['FINITE_EXHAUSTIVE_H1_TWIST_FAMILY'] is False
    assert bp['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bp['RECEIVER_CLOSED'] is False
    assert st['freshness']['current_main']==BASE and st['base_main_sha']==BASE
    assert st['promotion_gates']['36_09BO_hostile_reaudit_passed'] is True
    assert st['promotion_gates']['36_09BO_merged'] is True
    assert st['current']['unit']=='36-09BP'
    assert st['current']['next_exact_leaf']=='36-09BQ_RELATIVE_FACTOR_SQUARECLASS_BRANCH_EXHAUSTIVENESS_PREFLIGHT'
    assert st['current']['36_09BQ_entry_allowed'] is True
    assert st['cycle_ledger']['B4_BAD_PRIME_LOCAL']=='LIVE_PARAMETER_ELIMINATION_UNTESTED_UNIFORMLY_RETAINS_RECEIVER_POINT_GATES'
    for key in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BP verified: #1691 re-audit PASS/merge promoted; S34-W01 is the formal shape match, but its every-receiver-point exhaustive branch adapter is not yet proved. BQ selected; no finite twist family or closure credit.')

if __name__=='__main__': main()
