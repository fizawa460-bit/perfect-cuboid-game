#!/usr/bin/env python3
"""Verify Stage35-EX 35EX-31 primitive-source marking and endpoint-equivalence firewall."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
DOC=ROOT/'stages/stage35-ex/35ex-31/primitive-source-marking-endpoint-equivalence.md'
CERT=ROOT/'stages/stage35-ex/35ex-31/primitive-source-marking-certificate.json'

SCHEMA='STAGE35_EX_PESCH_E1_STATE_V30_POST_35EX31_PRIMITIVE_SOURCE_MARKING_ENDPOINT_EQUIVALENCE'
BASE_MAIN='32d35dd4372ceab3d67704290d48f6b6df8912bb'
HISTORY_MAIN='3d63864b0a10a53549f64a9e0dc3acf6f59ef9c0'
AUDITED_HEAD='00d6199c0df611b0606b15b8a46897629363cb10'
REVIEW_NODE='PRR_kwDOTr52Y88AAAABMS_hqA'

def git_blob_sha(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

state=json.loads(STATE.read_text())
cert=json.loads(CERT.read_text())
doc=DOC.read_text()

assert state['schema']==SCHEMA and state['stage']=='35-EX' and state['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha']==BASE_MAIN
hs=state['history_snapshot']
assert hs['commit_sha']==HISTORY_MAIN
assert hs['schema']=='STAGE35_EX_PESCH_E1_STATE_V29_POST_35EX30_ENDPOINT_GAUGE_RETURN_FIREWALL'
assert hs['role']=='IMMUTABLE_COMPLETE_V29_HISTORY_AND_AUTHORITY_SNAPSHOT'
assert hs['history_dropped'] is False
assert hs['historical_replay_verifier']=='stages/stage35-ex/verify_stage35_ex_v30_legacy_replay.py'

parent=state['parent_authority']
assert parent['unit']=='35EX-30'
assert parent['status']=='AUDITED_EXACT_ENDPOINT_GAUGE_RETURN_FIREWALL_NO_CREDIT'
assert parent['hostile_audit_verdict']=='PASS'
assert parent['pass_source']=='HOSTILE_AUDIT_REVIEW_ON_PR1581'
assert parent['hostile_audit_review_node_id']==REVIEW_NODE
assert parent['audited_head_sha']==AUDITED_HEAD
assert parent['exact_head_ci_run']==33950151293 and parent['exact_head_ci_job']==101263267837
assert parent['merged_main_sha']==HISTORY_MAIN
assert parent['audited_theorem_credit'] is False

delta=state['completed_units_delta']
assert delta['35EX-29B']['status']=='AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert delta['35EX-30']['status']=='AUDITED_EXACT_ENDPOINT_GAUGE_RETURN_FIREWALL_NO_CREDIT'
assert delta['35EX-30']['hostile_audit_review_node_id']==REVIEW_NODE
u31=delta['35EX-31']
assert u31['status']=='PROVISIONAL_EXACT_PRIMITIVE_SOURCE_REVERSE_ADAPTER_ENDPOINT_EQUIVALENCE_NO_CREDIT'
assert u31['artifact']==str(DOC.relative_to(ROOT))
assert u31['certificate']==str(CERT.relative_to(ROOT))
assert u31['verifier']=='stages/stage35-ex/verify_stage35_ex_31.py'
assert u31['source_to_35ex30_branchwise_label_map_exact'] is True
assert u31['primitive_source_reverse_adapter_provisional'] is True
assert u31['source_marking_reduces_unlabeled_endpoint_population'] is False
assert u31['E1_counterexample_rational_PC_population_equivalence_provisional'] is True
assert u31['audited_theorem_credit'] is False

cur=state['current']
assert cur['unit']=='35EX-31_PRIMITIVE_SOURCE_MARKING_ENDPOINT_EQUIVALENCE_OR_ENDPOINT_SCALE_BLOCKER'
assert cur['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert cur['candidate']=='E1-PRIMITIVE-SOURCE-MARKING-ON-COMPRESSED-CUBOID-GAUGE'
assert cur['next_if_audited_pass']=='FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION'

assert cert['schema']=='STAGE35_EX_31_PRIMITIVE_SOURCE_MARKING_ENDPOINT_EQUIVALENCE_CERTIFICATE_V1'
assert cert['authority']['audited_exact_head_sha']==AUDITED_HEAD
assert cert['authority']['hostile_audit_review_node_id']==REVIEW_NODE
assert cert['authority']['merged_main_sha']==HISTORY_MAIN
for key in (
    'stage35_ex_02_gcd_parity','stage35_ex_19_source_normalization',
    'stage35_ex_21_endpoint_surface','stage35_ex_26_source_quotient',
    'stage35_ex_27_rational_lift','stage35_ex_30_endpoint_gauge',
    'arsenal_S30_WF03','arsenal_S34_W03',
):
    lock=cert['source_locks'][key]
    p=ROOT/lock['path']
    assert git_blob_sha(p)==lock['blob_sha'], (key,git_blob_sha(p),lock['blob_sha'])
assert cert['reverse_adapter']['marked_endpoint_to_two_primitive_euclid_triples'] is True
assert cert['reverse_adapter']['marked_endpoint_to_master_hit'] is True
assert cert['reverse_adapter']['marked_endpoint_to_E1_counterexample'] is True
assert cert['endpoint_population']['unique_minimum_v2_edge'] is True
assert cert['endpoint_population']['source_marking_reduces_unlabeled_endpoint_population'] is False
assert cert['cycle']['fresh_breadth_audit_required_after_hostile_pass'] is True

# Source endpoint algebra.
x,y,d1,d2,d3,d4=sp.symbols('x y d1 d2 d3 d4', nonzero=True)

def reduce_source_squares(expr):
    num=sp.fraction(sp.together(expr))[0]
    out=sp.expand(num)
    # Repeat because one replacement can expose another square.
    for _ in range(3):
        out=sp.expand(out.subs(d1**2,1+x**2))
        out=sp.expand(out.subs(d2**2,1+y**2))
        out=sp.expand(out.subs(d3**2,x**2+y**2))
        out=sp.expand(out.subs(d4**2,1+x**2+y**2))
    return sp.factor(out)

alpha=(d4+y)/d1
alpha_inv=(d4-y)/d1
assert reduce_source_squares(alpha*alpha_inv-1)==0

c_alpha=(alpha**2+alpha_inv**2)/2
c_source=(d2**2+d3**2)/d1**2
assert reduce_source_squares(c_alpha-c_source)==0

R=d2+d3
b=R/(x+1)
s=b**2
W_candidate=(R/(x-1))**2
assert reduce_source_squares(W_candidate*(s-c_source)-(c_source*s-1))==0

# Branch A: x>1, omega=R/(x-1), the 35EX-30 gauge is source-labelled.
omega_A=R/(x-1)
e1A=sp.factor(omega_A-b)
e2A=sp.factor(omega_A+b)
assert reduce_source_squares(e2A-x*e1A)==0
assert reduce_source_squares(b*omega_A-1-d2*e1A)==0
assert reduce_source_squares(b*omega_A+1-d3*e1A)==0

# Branch B: 0<x<1, the first two endpoint edges are swapped and scaled by x.
omega_B=R/(1-x)
e1B=sp.factor(omega_B-b)
e2B=sp.factor(omega_B+b)
assert reduce_source_squares(e2B-e1B/x)==0
assert reduce_source_squares(b*omega_B-1-d3*e1B/x)==0
assert reduce_source_squares(b*omega_B+1-d2*e1B/x)==0

# The full S_PC equations are preserved under the Branch-B edge swap/rescaling.
X=1/x
Y=y/x
D1=d1/x
D2=d3/x
D3=d2/x
D4=d4/x
assert reduce_source_squares(D1**2-(1+X**2))==0
assert reduce_source_squares(D2**2-(1+Y**2))==0
assert reduce_source_squares(D3**2-(X**2+Y**2))==0
assert reduce_source_squares(D4**2-(1+X**2+Y**2))==0

# The 2-adic equal-valuation obstruction is the elementary mod-4 square fact.
square_residues_mod4={i*i % 4 for i in range(4)}
assert square_residues_mod4=={0,1}
assert (1+1) % 4 == 2 and 2 not in square_residues_mod4

required_doc=[
    'SOURCE_TO_35EX30_BRANCHWISE_LABEL_MAP_EXACT=true',
    'SOURCE_RECIPROCAL_BRANCH_RECOVERED_BY_V2=true',
    'PROVISIONAL_PRIMITIVE_SOURCE_REVERSE_ADAPTER=true',
    'CANONICAL_GCD_CHANNELS_RECONSTRUCTED_FROM_ENDPOINT=true',
    'UNIQUE_MINIMUM_V2_EDGE_FOR_RATIONAL_CUBOID=true',
    'SOURCE_MARKING_REDUCES_UNLABELED_ENDPOINT_POPULATION=false',
    'PROVISIONAL_E1_COUNTEREXAMPLE_RATIONAL_PC_POPULATION_EQUIVALENCE=true',
    'AUDITED_ADAPTER_CREDIT=false',
    'E1_PROVED=false',
    'PERFECT_CUBOID_NONEXISTENCE_CLAIM=false',
    'FRESH_BREADTH_AUDIT_REQUIRED_AFTER_HOSTILE_PASS=true',
]
for token in required_doc:
    assert token in doc, token

claims=state['claims']
for key in (
    'new_theorem_credit','audited_primitive_source_population_reverse_adapter',
    'audited_E1_endpoint_population_equivalence','E1_proved','R29_PESCH_E1_closed',
    'R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed',
    'perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim',
):
    assert claims[key] is False, key

print('PASS STAGE35_EX_31_PRIMITIVE_SOURCE_MARKING_ENDPOINT_EQUIVALENCE')
