#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
def text(rel):
    p=ROOT/rel; assert p.exists(),rel; return p.read_text(encoding='utf-8')
def data(rel): return json.loads(text(rel))

reg=data('stages/stage25/25-reentry-r008a/backflow-registry.json')
ctrl=data('stages/stage25/25-reentry-controller.json')
st19=text('stages/stage19/post-stage25-50-supersession.md')
st23=text('stages/stage23/post-stage25-r01/result.md')
st24=text('stages/stage24/post-stage25-r01/result.md')
st24f=text('stages/stage24/final.md')
a20=text('stages/stage25/25-reentry-20/audit.md')
a8=text('stages/stage25/25-reentry-r008a/audit.md')
res=text('stages/stage25/25-reentry-r008a/result.md')

assert reg['route_id']=='Stage25-um-r008a'
assert reg['parent_task']=='Stage25-u24-r002a'
assert reg['source']['pr']==1003
assert reg['source']['merge_commit']=='1d88e8e3254a383620e221df8a1a1039ebeabcd4'
assert reg['source']['accepted_theorem']=='N2,j(B)>>_j B^(1/4) for j=a,b,c'
assert 'AUDIT_VERDICT=PASS' in a20 and 'AUDIT_VERDICT=PASS' in a8

r=reg['receivers']; assert set(r)=={'Stage19','Stage23','Stage24'}
assert r['Stage19']['population_match']=='EXACT'
assert r['Stage23']['population_match']=='ONE_SIDED_INCIDENCE_EMBEDDING'
assert r['Stage24']['population_match']=='EXACT_DIRECTIONAL_STAGE18_TO_STAGE19'
assert r['Stage23']['shared_edge_to_pair']=={'a':'ab,ac','b':'ab,bc','c':'ac,bc'}

N=(Fraction(1,4),0); M=(Fraction(1),5); S=(Fraction(-1),0)
surv=(N[0]-M[0],N[1]-M[1]); inter=(surv[0]-S[0],surv[1]-S[1])
assert surv==(Fraction(-3,4),-5) and inter==(Fraction(1,4),-5)
assert 'DIRECTIONAL_THEOREM=M2,j(B)~C_j B(log B)^5 for j=a,b,c with C_j>0' in st24f
for marker in ('N2,a(B)>>B^(1/4)','N2,b(B)>>B^(1/4)','N2,c(B)>>B^(1/4)','ALL_DIRECTIONAL_QUARTER_POWER_LOWER_PROVED=true'):
    assert marker in st19,marker
for marker in ('A_ab,ac(B)>>B^(1/4)','A_ab,bc(B)>>B^(1/4)','A_ac,bc(B)>>B^(1/4)','ALL_PAIR_OVERLAP_QUARTER_POWER_LOWER_PROVED=true'):
    assert marker in st23,marker
for marker in ('N2,j/M2,j>>_j B^(-3/4)(log B)^(-5) for j=a,b,c','J2,j>>_j B^(1/4)(log B)^(-5)->infinity for j=a,b,c','ALL_DIRECTIONAL_SURVIVAL_LOWER_SYNCED=true','ALL_DIRECTIONAL_J2_POSITIVE_DIVERGENT=true'):
    assert marker in st24,marker

assert reg['accounting']['parent_theorem_reproved'] is False
assert reg['accounting']['new_global_N2_exponent'] is False
assert reg['accounting']['double_charge'] is False
assert reg['accounting']['finite_data_promoted'] is False
assert reg['accounting']['raw_overlap_reinterpreted_as_survival_probability'] is False
assert reg['gates']['stage26_allowed'] is False  # historical r008a snapshot

r8=ctrl['r008a_submission']
assert r8['route_id']=='Stage25-um-r008a' and r8['parent_pr']==1003
closed=ctrl['status']=='CLOSED_AUDITED_PASS_MERGED_STAGE26_HANDOFF_READY'
assert ctrl['stage26_gate']['stage26_allowed'] is closed
if closed:
    assert ctrl['current_phase']==70
    assert ctrl['phase70_submission']['audit_status']=='PASS'
    assert ctrl['phase70_submission']['merge_commit']=='be5f7d8360b3bac2b9060cd88ede596a4fb218dc'
    assert ctrl['next_expected_command']=='Stage26-main-batch'
if ctrl['current_phase']==20:
    assert r8['status'] in ('SUBMITTED_PENDING_FRESH_AUDIT','AUDITED_PASS_AWAITING_MERGE')
else:
    assert ctrl['current_phase'] in (30,40,50,60,70)
    assert r8['status']=='AUDITED_PASS_MERGED' and r8['audit_status']=='PASS'
    assert r8['merge_commit']=='11075adf8e30c73e5058790ee6ed6e2a9b6c9e2b'
    assert not any(x['route_id']=='Stage25-um-r008a' and x['blocks_next_phase'] for x in ctrl['propagation_queue'])

for marker in ('GLOBAL_N2_EXPONENT_UPGRADED=false','TRUE_N2_EXPONENT_IDENTIFIED=false','FINITE_DATA_USED_AS_PROOF=false','PERFECT_CUBOID_CONCLUSION=NONE'):
    assert marker in res,marker

print('STAGE25_REENTRY_R008A_PARENT_AUTHORIZATION=PASS')
print('STAGE25_REENTRY_R008A_STAGE19_DIRECTIONAL_SYNC=PASS')
print('STAGE25_REENTRY_R008A_STAGE23_PAIR_OVERLAP_SYNC=PASS')
print('STAGE25_REENTRY_R008A_STAGE24_DIRECTIONAL_SYNC=PASS')
print('STAGE25_REENTRY_R008A_POST_MERGE_LIFECYCLE=PASS')
print('STAGE26_GATE=LIFECYCLE_VALID')
