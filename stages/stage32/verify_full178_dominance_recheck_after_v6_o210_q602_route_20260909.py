#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage32/full178-dominance-recheck-after-v6-o210-q602-route-20260909.json'
ACTIVE=ROOT/'stages/stage32/proof/ACTIVE-FRONTIER.json'
EX5=ROOT/'stages/stage32-ex5/MAIN-STATE.json'
def main():
    x=json.loads(ART.read_text()); a=json.loads(ACTIVE.read_text()); e=json.loads(EX5.read_text())
    assert x['schema']=='STAGE32_FULL178_DOMINANCE_RECHECK_AFTER_V6_O210_Q602_ROUTE_V1'
    assert x['status']=='EXACT_SCOPE_RECHECK_FULL178_NOT_DOMINATED'
    claims={c['claim_id']:c for c in a['claims']}
    f=claims['S32.FULL178.NUMERICAL_CENSUS.V1']
    assert f['scope']==x['full178_scope']
    assert f['frontier_status']=='ACTIVE_INCOMPLETE'
    assert f['authority_status']=='DECLARED_GOAL'
    rc=e['receiver_contract']
    assert rc['unibranch_degree_row_count']==183
    assert rc['row_count']==185
    assert rc['status_counts']=={'CLOSED':5,'OPEN':180,'UNKNOWN':0,'CONDITIONAL':0,'OUT_OF_SCOPE':0}
    assert rc['V6_O210_Q602_treated_as_definition_of_all_receivers'] is False
    d=x['decision']
    assert d['full178_dominated_by_v6_o210_q602_nonexistence'] is False
    assert d['full178_remains_independent_main_closure_obligation'] is True
    assert d['ex5_remains_attack_lane'] is True
    assert all(v is False for v in x['firewalls'].values())
    print('PASS_STAGE32_FULL178_NOT_DOMINATED_BY_V6_O210_Q602_SCOPE')
if __name__=='__main__': main()
