#!/usr/bin/env python3
from __future__ import annotations
import itertools, json, subprocess
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BG/full-character-ay-pullback-collapse-preflight.json'
BF=ROOT/'stages/stage36/36-09BF/weight2-elliptic-quotient-pullback-collapse-preflight.json'
BFV=ROOT/'stages/stage36/verify_stage36_36_09BF.py'
BE=ROOT/'stages/stage36/36-09BE/full-multiquadratic-character-quotient-inventory-preflight.json'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='386b6a52d7bfec2e8903412c7ca56976b46c288b'
BF_HEAD='2079662f682f2a2b49009da169bc66176df8e893'
BF_CI='34097188205/101663334365'
CERT_BLOB='a47f1354f74f2ed5412fe5d58daeb657d47fef66'
LOCKS={BF:'da1f71559c8a6a56391c13dcb848aafdf3317ed7',BFV:'8bfd6716b8cee141a7400f41d48f5b16802e1c76',BE:'f30724ca63b30b4b960e31f7d8266a4a99884016',BB:'e4b63fd500d05ff5dc704e0c08409edee5895053'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def projection(mask:int): return ((mask>>2)&1,(mask>>3)&1)
def label(p): return {(0,0):'AUTOMATIC',(1,0):'F3',(0,1):'F4',(1,1):'F3F4'}[p]

def subset_key(indices): return ''.join(str(i+1) for i in indices)

def main():
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BF_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']['36_09BF_exact_head']==BF_HEAD
    assert c['batch_parent']['36_09BF_exact_head_ci']==BF_CI

    counts=Counter(); by_weight=defaultdict(dict); total=0
    for w in range(1,5):
        for S in itertools.combinations(range(4),w):
            mask=sum(1<<i for i in S)
            lab=label(projection(mask))
            counts[lab]+=1; total+=1
            by_weight[w][subset_key(S)]=lab
    assert total==15
    assert counts==Counter({'F3':4,'F4':4,'F3F4':4,'AUTOMATIC':3})
    recorded=c['all_character_projection_counts']
    assert recorded=={'AUTOMATIC_00':3,'F3_10':4,'F4_01':4,'F3F4_11':4,'total':15}
    assert by_weight[1]==c['weight_projection_table']['weight1']
    assert by_weight[2]==c['weight_projection_table']['weight2']
    assert by_weight[3]==c['weight_projection_table']['weight3']
    assert by_weight[4]==c['weight_projection_table']['weight4']

    rc=c['receiver_consequence']
    assert rc['new_character_predicate_beyond_BB'] is False
    assert rc['all_character_predicate_route_adds_candidate_shrink'] is False
    assert rc['independent_square_predicates_from_all_characters']==['f3 is a Q-square','f4 is a Q-square']
    scope=c['important_scope_distinction']
    assert scope['full_cover_information_retained'] is True
    assert 'arithmetic models' in scope['still_live']
    cyc=c['cycle_result']
    assert cyc['route_status']=='BLOCKED_NO_NEW_INFORMATION_AS_NEW_PREDICATE_ROUTE'
    assert cyc['selected_next']=='36-09BH_BAD_PLACE_FULL_COVER_VALUATION_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V95_36_09BG_AUDIT_CHECKPOINT'
    bg=st['authority_frontier']['36-09BG']
    assert bg['ALL_15_CHARACTER_PULLBACK_COLLAPSE_COMPLETE'] is True
    assert bg['NEW_CHARACTER_PREDICATE_BEYOND_BB'] is False
    assert bg['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bg['RECEIVER_CLOSED'] is False
    assert st['cycle_ledger']['B4_FULL_CHARACTER_QUOTIENTS']=='BLOCKED_NO_NEW_INFORMATION_AS_NEW_PREDICATE_ROUTE'
    assert st['cycle_ledger']['B4_BAD_PRIME_LOCAL']=='LIVE_SELECTED'
    assert st['current']['unit']=='36-09BG-AUDIT-CHECKPOINT'
    assert st['current']['hostile_audit_checkpoint_reached'] is True
    assert st['current']['36_09BH_entry_allowed'] is False
    assert st['claims']['receiver_emptiness_proved'] is False
    print('36-09BG verified: all 15 nontrivial character square predicates project on AY to 3 automatic + 4 f3 + 4 f4 + 4 f3f4; no new independent predicate exists beyond BB. Character-predicate route is blocked; bad-place full-cover valuation is selected but locked pending audit.')

if __name__=='__main__': main()
