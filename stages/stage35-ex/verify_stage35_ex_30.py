#!/usr/bin/env python3
"""Verify Stage35-EX 35EX-30 exact endpoint-gauge return and credit firewall."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
BREADTH=ROOT/'stages/stage35-ex/35ex-29/post-reciprocal-common-factor-breadth-audit.json'
DOC=ROOT/'stages/stage35-ex/35ex-30/endpoint-gauge-return-firewall.md'
CERT=ROOT/'stages/stage35-ex/35ex-30/endpoint-gauge-return-certificate.json'

SCHEMA='STAGE35_EX_PESCH_E1_STATE_V29_POST_35EX30_ENDPOINT_GAUGE_RETURN_FIREWALL'
MAIN='38434ea3c4124efd1cc04a228e85b2fd207f2c14'
AUDITED_HEAD='21ce592d3f30fd10b421ed0d3be68a702c26c65a'
REVIEW_NODE='PRR_kwDOTr52Y88AAAABMS3Ipg'

def git_blob_sha(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

state=json.loads(STATE.read_text())
breadth=json.loads(BREADTH.read_text())
cert=json.loads(CERT.read_text())
doc=DOC.read_text()

assert state['schema']==SCHEMA and state['stage']=='35-EX' and state['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha']==MAIN
hs=state['history_snapshot']
assert hs['commit_sha']==MAIN
assert hs['schema']=='STAGE35_EX_PESCH_E1_STATE_V28_POST_35EX29_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION'
assert hs['history_dropped'] is False
assert hs['historical_replay_verifier']=='stages/stage35-ex/verify_stage35_ex_v29_legacy_replay.py'
parent=state['parent_authority']
assert parent['unit']=='35EX-29'
assert parent['status']=='AUDITED_EXACT_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_NO_CREDIT'
assert parent['hostile_audit_verdict']=='PASS' and parent['pass_source']=='HOSTILE_AUDIT_REVIEW_ON_PR1579'
assert parent['hostile_audit_review_node_id']==REVIEW_NODE
assert parent['audited_head_sha']==AUDITED_HEAD
assert parent['exact_head_ci_run']==33946860829 and parent['exact_head_ci_job']==101254427135
assert parent['merged_main_sha']==MAIN and parent['audited_theorem_credit'] is False

delta=state['completed_units_delta']
assert delta['35EX-28B']['status']=='AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert delta['35EX-28B']['hostile_audit_review_node_id']==REVIEW_NODE
assert delta['35EX-29']['status']=='AUDITED_EXACT_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_NO_CREDIT'
assert delta['35EX-29']['audited_head_sha']==AUDITED_HEAD
assert delta['35EX-29B']['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert delta['35EX-29B']['selected_candidate']=='E1-PRIMITIVE-SOURCE-MARKING-ON-COMPRESSED-CUBOID-GAUGE'
assert delta['35EX-30']['status']=='PROVISIONAL_EXACT_ENDPOINT_GAUGE_RETURN_FIREWALL_NO_CREDIT'
assert delta['35EX-30']['symmetric_three_square_receiver_iff'] is True
assert delta['35EX-30']['endpoint_surface_new_theorem_credit'] is False
assert delta['35EX-30']['primitive_source_population_reverse_adapter_proved'] is False

cur=state['current']
assert cur['unit']=='35EX-30_ENDPOINT_GAUGE_RETURN_FIREWALL'
assert cur['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert cur['next_if_audited_pass']=='35EX-31_PRIMITIVE_SOURCE_MARKING_ON_COMPRESSED_CUBOID_GAUGE'
ledger=state['candidate_ledger_after_35ex29_breadth_audit']
assert ledger['selected_live']=='E1-PRIMITIVE-SOURCE-MARKING-ON-COMPRESSED-CUBOID-GAUGE'
assert 'E1-RATIO-DISCRIMINANT-QUARTIC-QUOTIENT' in ledger['untested']
assert ledger['fresh_breadth_audit_required_before_selected_35EX31'] is False

assert breadth['schema']=='STAGE35_EX_29B_POST_RECIPROCAL_COMMON_FACTOR_FRESH_BREADTH_AUDIT_V1'
assert breadth['protocol']['fresh_exhaustive_view_audit'] is True
assert breadth['protocol']['blind_rediscovery'] is True
assert breadth['protocol']['blind_generation_performed_before_arsenal_comparison'] is True
assert breadth['protocol']['historical_comparison_performed_after_blind_generation'] is True
assert breadth['selection']['selected_candidate']=='E1-PRIMITIVE-SOURCE-MARKING-ON-COMPRESSED-CUBOID-GAUGE'
assert breadth['selection']['selected_next_unit']=='35EX-31_PRIMITIVE_SOURCE_MARKING_ON_COMPRESSED_CUBOID_GAUGE'
assert breadth['arsenal_comparison']['S34-W03']['blob_sha']=='1d5275321f42768a6414d4610ac912c63be43f96'
assert breadth['claims']['endpoint_surface_new_credit'] is False
assert breadth['claims']['E1_proved'] is False

assert cert['schema']=='STAGE35_EX_30_ENDPOINT_GAUGE_RETURN_CERTIFICATE_V1'
assert cert['authority']['audited_exact_head_sha']==AUDITED_HEAD
assert cert['authority']['hostile_audit_review_node_id']==REVIEW_NODE
assert cert['authority']['merged_main_sha']==MAIN
for key in ('stage35_ex_29_doc','stage35_ex_21_doc','arsenal_S34_W03','cycle_policy'):
    lock=cert['source_locks'][key]
    p=ROOT/lock['path']
    assert git_blob_sha(p)==lock['blob_sha'], (key,git_blob_sha(p),lock['blob_sha'])
assert cert['symmetric_receiver']['R1_R2_iff_on_retained_positive_open'] is True
assert cert['cuboid_gauge']['matches_stage35_ex_21_endpoint_scale_surface'] is True
assert cert['cuboid_gauge']['endpoint_surface_new_theorem_credit'] is False
assert cert['firewall']['primitive_source_population_reverse_adapter_proved'] is False

# Exact symbolic algebra from 35EX-29 receiver to the symmetric square package.
A,s=sp.symbols('A s', positive=True, nonzero=True)
c=(A**2+1)/(2*A)
W=sp.factor((c*s-1)/(s-c))
assert sp.factor(W*(s-c)-(c*s-1))==0
assert sp.factor(s+W-(s**2-1)/(s-c))==0
assert sp.factor(W-A-((A**2-1)/(2*A))*(A-s)/(s-c))==0

T2=sp.factor(2*(s+W))
P2=sp.factor((c+1)*(s+W))
Q2=sp.factor((c-1)*(s+W))
assert sp.factor(P2-(s+1)*(W+1))==0
assert sp.factor(Q2-(s-1)*(W-1))==0
assert sp.factor(P2-Q2-T2)==0
assert sp.factor(s*W+1-c*(s+W))==0

# Reconstruct c and A from P,Q,t square package.
P,Q,T=sp.symbols('P Q T', nonzero=True)
Arec=sp.factor((P+Q)/(P-Q))
crec=sp.factor((Arec**2+1)/(2*Arec))
assert sp.factor(crec-(P**2+Q**2)/(P**2-Q**2))==0
S,Wv=sp.symbols('S Wv', positive=True)
P2sw=(S+1)*(Wv+1)
Q2sw=(S-1)*(Wv-1)
T2sw=2*(S+Wv)
assert sp.factor(P2sw-Q2sw-T2sw)==0
assert sp.factor((P2sw+Q2sw)/T2sw-(S*Wv+1)/(S+Wv))==0

# Exact rational perfect-cuboid gauge identities.
b,w=sp.symbols('b w', positive=True)
sbw=b**2
Wbw=w**2
e1=w-b
e2=w+b
Qsq=(sbw-1)*(Wbw-1)
tsq=2*(sbw+Wbw)
Psq=(sbw+1)*(Wbw+1)
assert sp.factor(e1**2+e2**2-tsq)==0
assert sp.factor(e1**2+Qsq-(b*w-1)**2)==0
assert sp.factor(e2**2+Qsq-(b*w+1)**2)==0
assert sp.factor(e1**2+e2**2+Qsq-Psq)==0

required_doc=[
    'SYMMETRIC_THREE_SQUARE_RECEIVER_IFF=true',
    'R1_R2_TO_RATIONAL_CUBOID_GAUGE_FORWARD_EXACT=true',
    'NORMALIZED_CUBOID_SURFACE_SPC_MATCH_35EX21=true',
    'ENDPOINT_SURFACE_NEW_THEOREM_CREDIT=false',
    'PRIMITIVE_SOURCE_POPULATION_REVERSE_ADAPTER_PROVED=false',
    'E1_PROVED=false',
    'PERFECT_CUBOID_NONEXISTENCE_CLAIM=false',
    'NEXT_IF_HOSTILE_PASS=35EX-31_PRIMITIVE_SOURCE_MARKING_ON_COMPRESSED_CUBOID_GAUGE',
]
for token in required_doc:
    assert token in doc, token

claims=state['claims']
for key in ('new_theorem_credit','endpoint_surface_new_theorem_credit','primitive_source_population_reverse_adapter_proved','global_surface_rational_points_classified','brauer_obstruction_proved','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
    assert claims[key] is False, key

print('PASS STAGE35_EX_30_ENDPOINT_GAUGE_RETURN_FIREWALL')
