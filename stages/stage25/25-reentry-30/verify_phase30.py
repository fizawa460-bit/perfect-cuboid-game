#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
def text(rel):
    p=ROOT/rel; assert p.exists(),rel; return p.read_text(encoding='utf-8')
def data(rel): return json.loads(text(rel))

reg=data('stages/stage25/25-reentry-30/mask-registry.json')
back=data('stages/stage25/25-reentry-30/backflow-proposals.json')
ctrl=data('stages/stage25/25-reentry-controller.json')
res=text('stages/stage25/25-reentry-30/result.md')
disc=text('stages/stage25/25-reentry-30/discovery-ledger.md')
weap=text('stages/stage25/25-reentry-30/weapon-delta.md')
st13=text('stages/stage13/final.md')
st17=text('stages/stage17/final.md')
st23_bundle=text('stages/stage23/23-70/self-contained-bundle.md')
st19=text('stages/stage19/post-stage25-50-supersession.md')
r008=text('stages/stage25/25-reentry-r008a/audit.md')

assert reg['task_id']=='Stage25-u23-r003a' and reg['phase']==30
assert reg['authorization']['r008a_pr']==1004
assert reg['authorization']['r008a_merge_commit']=='11075adf8e30c73e5058790ee6ed6e2a9b6c9e2b'
assert 'AUDIT_VERDICT=PASS' in r008
for marker in ('A_{ab,ac}=', 'A_{ab,bc}=', 'A_{ac,bc}=', 'A_3=', 'I_{ab}I_{ac}I_{bc}'):
    assert marker in st13,marker
assert 'N_1(B)\\sim\\frac{\\kappa}{24\\pi}B(\\log B)^3' in st17
assert 'CURRENT_LOWER=N2(B)>>B^(1/4)' in st19

m=reg['masks']
assert m['a']['identity']=='N2,a=A_ab,ac-A3'
assert m['b']['identity']=='N2,b=A_ab,bc-A3'
assert m['c']['identity']=='N2,c=A_ac,bc-A3'
assert reg['sum_identity']=='N2=A_ab,ac+A_ab,bc+A_ac,bc-3*A3'
assert len(reg['triple_free_contrasts'])==3
for ab in (0,1):
  for ac in (0,1):
    for bc in (0,1):
      a3=ab*ac*bc
      naa=ab*ac*(1-bc); nbb=ab*bc*(1-ac); ncc=ac*bc*(1-ab)
      assert ab*ac-a3==naa and ab*bc-a3==nbb and ac*bc-a3==ncc
      assert (ab*ac+ab*bc+ac*bc)-3*a3==naa+nbb+ncc
      assert ab*ac-ab*bc==naa-nbb
      assert ab*ac-ac*bc==naa-ncc
      assert ab*bc-ac*bc==nbb-ncc

assert 'The two strata are disjoint' in st23_bundle
assert 'not a literal survival probability' in st23_bundle
assert reg['directional_stage23']['ratio_semantics']=='MATCHED_ADJACENT_STRATUM_POPULATION_SIZE_RATIO_NOT_LITERAL_SURVIVAL'
assert reg['directional_stage23']['N2j_subset_of_N1'] is False
assert reg['directional_stage23']['N1_and_N2j_disjoint_exact_face_strata'] is True
assert reg['scope_firewall']['literal_subset_survival_interpretation'] is False
assert reg['scope_firewall']['A3_quarter_power_control_proved'] is False
assert reg['scope_firewall']['perfect_cuboid_existence_proved'] is False
assert reg['scope_firewall']['perfect_cuboid_nonexistence_proved'] is False
for marker in ('N2,a = A_ab,ac - A3','N2,b = A_ab,bc - A3','N2,c = A_ac,bc - A3','DIRECTIONAL_STAGE23_RATIO_LIMIT=0','PERFECT_CUBOID_CONCLUSION=NONE'):
    assert marker in res,marker
assert 'D30-03' in disc and 'A3' in disc and 'S25R-W30-02' in weap
assert back['queued_derived_routes']==['Stage25-um-r009a']
assert ctrl['phases']['20']['status']=='AUDITED_PASS_MERGED_BACKFLOW_AUDITED_PASS_MERGED'

closed = ctrl['status']=='CLOSED_AUDITED_PASS_MERGED_STAGE26_HANDOFF_READY'
assert ctrl['stage26_gate']['stage26_allowed'] is closed
if closed:
    assert ctrl['current_phase']==70
    assert ctrl['phase70_submission']['audit_status']=='PASS'
    assert ctrl['phase70_submission']['merge_commit']=='be5f7d8360b3bac2b9060cd88ede596a4fb218dc'
    assert ctrl['next_expected_command']=='Stage26-main-batch'

status=ctrl['status']; current=ctrl['current_phase']
if current==30:
    assert ctrl['phases']['40']['status'] in ('BLOCKED_UNTIL_PHASE30_BACKFLOW','BLOCKED_UNTIL_R009A_AUDIT_PASS_MERGE')
    assert ctrl['propagation_queue'][-1]['route_id']=='Stage25-um-r009a'
    if status=='PHASE30_SUBMITTED_PENDING_FRESH_AUDIT':
        assert reg['status']=='SUBMITTED_PENDING_FRESH_AUDIT'
        assert ctrl['phase30_submission']['audit_status']=='PENDING'
    elif status in ('PHASE30_AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW','PHASE30_BACKFLOW_AUDITED_PASS_AWAITING_MERGE'):
        assert ctrl['phase30_submission']['audit_status']=='PASS'
    else:
        raise AssertionError(status)
else:
    assert current in (40,50,60,70)
    p30=ctrl['phase30_submission']; r9=ctrl['r009a_submission']
    assert p30['audit_status']=='PASS'
    assert p30['pr']==1005 and p30['merge_commit']=='daf84757c185df6973936d2970a6307ab0bff62b'
    assert r9['audit_status']=='PASS' and r9['status']=='AUDITED_PASS_MERGED'
    assert r9['pr']==1006 and r9['merge_commit']=='4eb3349ee8ec02dcabb71bd1be3a48234356606b'
    assert not any(x['route_id']=='Stage25-um-r009a' and x['blocks_next_phase'] for x in ctrl['propagation_queue'])

print('STAGE25_REENTRY_PHASE30_MASK_TRUTH_TABLE=PASS')
print('STAGE25_REENTRY_PHASE30_SOURCE_BINDING=PASS')
print('STAGE25_REENTRY_PHASE30_ADJACENT_STRATUM_SEMANTICS=PASS')
print('STAGE25_REENTRY_PHASE30_DIRECTIONAL_NORMALIZATION=PASS')
print('STAGE25_REENTRY_PHASE30_BACKFLOW_QUEUE=PASS')
print('STAGE26_GATE=LIFECYCLE_VALID')
