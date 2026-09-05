#!/usr/bin/env python3
"""Verify Stage35-EX 35EX-29 reciprocal common-factor Kummer compression."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
BREADTH=ROOT/'stages/stage35-ex/35ex-28/post-full-rational-source-kummer-breadth-audit.json'
DOC=ROOT/'stages/stage35-ex/35ex-29/reciprocal-common-factor-kummer-compression.md'
CERT=ROOT/'stages/stage35-ex/35ex-29/reciprocal-common-factor-kummer-certificate.json'

SCHEMA='STAGE35_EX_PESCH_E1_STATE_V28_POST_35EX29_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION'
MAIN='5fa33e600b81fc34f4be9b22761c8079b31d7806'
AUDITED_HEAD='908047d41b3f856cb5e6083793fb4815666b64b3'
MERGED_MAIN='0ebf2cfec83a39b016f61b996a0dd533d242de87'
REVIEW_NODE='PRR_kwDOTr52Y88AAAABMR185Q'

def git_blob_sha(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

state=json.loads(STATE.read_text())
breadth=json.loads(BREADTH.read_text())
cert=json.loads(CERT.read_text())
doc=DOC.read_text()

assert state['schema']==SCHEMA
assert state['stage']=='35-EX' and state['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha']==MAIN
parent=state['parent_authority']
assert parent['unit']=='35EX-28'
assert parent['status']=='AUDITED_EXACT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_NO_CREDIT'
assert parent['hostile_audit_verdict']=='PASS'
assert parent['hostile_audit_review_node_id']==REVIEW_NODE
assert parent['audited_head_sha']==AUDITED_HEAD
assert parent['exact_head_ci_run']==33932898366
assert parent['exact_head_ci_job']==101215004429
assert parent['merged_main_sha']==MERGED_MAIN
assert parent['audited_theorem_credit'] is False

u27b=state['completed_units']['35EX-27B']
assert u27b['status']=='AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert u27b['hostile_audit_verdict']=='PASS'
assert u27b['audited_head_sha']==AUDITED_HEAD
u28=state['completed_units']['35EX-28']
assert u28['status']=='AUDITED_EXACT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_NO_CREDIT'
assert u28['hostile_audit_verdict']=='PASS'
assert u28['audited_head_sha']==AUDITED_HEAD
assert u28['exact_head_ci_run']==33932898366 and u28['exact_head_ci_job']==101215004429
assert u28['merged_main_sha']==MERGED_MAIN
u28b=state['completed_units']['35EX-28B']
assert u28b['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert u28b['artifact']==str(BREADTH.relative_to(ROOT))
u29=state['completed_units']['35EX-29']
assert u29['status']=='PROVISIONAL_EXACT_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_NO_CREDIT'
assert u29['artifact']==str(DOC.relative_to(ROOT))
assert u29['certificate']==str(CERT.relative_to(ROOT))
assert u29['verifier']=='stages/stage35-ex/verify_stage35_ex_29.py'
assert u29['full_K1_K4_to_R1_R2_receiver_iff'] is True
assert u29['reciprocal_physical_chamber_preserved'] is False
assert u29['audited_theorem_credit'] is False

cur=state['current']
assert cur['unit']=='35EX-29_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_OR_JOINT_LOCAL_FIREWALL'
assert cur['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert cur['candidate']=='E1-RECIPROCAL-COMMON-FACTOR-KUMMER-COMPRESSION'
assert cur['next_if_audited_pass']=='FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION'
assert state['resolved_investigations']['CURRENT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION']['status']=='AUDITED_PASS_EXACT_K1_K4_COMPLETION_NO_CLOSURE'
assert state['resolved_investigations']['CURRENT_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION']['status']=='PROVISIONAL_PASS_EXACT_R1_R2_COMPRESSION_PENDING_HOSTILE_AUDIT'

assert breadth['schema']=='STAGE35_EX_28B_POST_FULL_RATIONAL_SOURCE_KUMMER_FRESH_BREADTH_AUDIT_V1'
assert breadth['protocol']['fresh_exhaustive_view_audit'] is True
assert breadth['protocol']['blind_rediscovery'] is True
assert breadth['protocol']['blind_generation_performed_before_arsenal_comparison'] is True
assert breadth['selection']['selected_candidate']=='E1-RECIPROCAL-COMMON-FACTOR-KUMMER-COMPRESSION'
assert breadth['selection']['selected_next_unit']=='35EX-29_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_OR_JOINT_LOCAL_FIREWALL'
assert 'E1-DESCENDED-RECEIVER-JOINT-LOCAL-CLASSIFICATION' in breadth['preserved_untested_candidates']
assert breadth['historical_comparison']['E1-K1-K4-CHARACTER-QUOTIENT-RECOMPOSITION'].startswith('EQUIVALENT_')
assert breadth['arsenal_comparison']['S34-W03']['blob_sha']=='1d5275321f42768a6414d4610ac912c63be43f96'
assert breadth['claims']['E1_proved'] is False

assert cert['schema']=='STAGE35_EX_29_RECIPROCAL_COMMON_FACTOR_KUMMER_CERTIFICATE_V1'
assert cert['authority']['audited_exact_head_sha']==AUDITED_HEAD
assert cert['authority']['merged_main_sha']==MERGED_MAIN
for key in ('stage35_ex_28_doc','stage35_ex_28_certificate','arsenal_S34_W03'):
    lock=cert['source_locks'][key]
    p=ROOT/lock['path']
    assert git_blob_sha(p)==lock['blob_sha'], (key, git_blob_sha(p), lock['blob_sha'])
assert cert['compressed_receiver']['full_K1_K4_iff'] is True
assert cert['reciprocal_symmetry']['physical_positive_chamber_preserved'] is False
assert cert['historical_firewall']['genus5_character_decomposition_new_credit'] is False
assert cert['historical_firewall']['five_elliptic_isogeny_new_credit'] is False

# Exact symbolic algebra.
A,s=sp.symbols('A s', nonzero=True)
c=(A**2+1)/(2*A)
beta=(A*s-1)/(A-s)

# K2 inverse and K1 deterministic reconstruction.
assert sp.factor((A*beta+1)/(A+beta)-s)==0
u=2*A*(beta**2-1)/(beta*(A**2-1))
u_new=2*A*(s**2-1)/((A-s)*(A*s-1))
assert sp.factor(u-u_new)==0

# K3 exact rational-square scaling.
k3=sp.factor((beta-A)*(A*beta-1))
r1=(s-c)*(c*s-1)
assert sp.factor(k3-(2*A/(A-s))**2*r1)==0

# K4 exact scaling after alpha^2=A and b^2=s.
k4=sp.factor((beta**2-1)*(A**2*beta**2-1))
r2=2*(c*s-1)*(s**2-1)
# lambda^2 * (A-s)^4/[A*s*(A^2-1)^2] = R2.
assert sp.factor(k4*(A-s)**4/(A*s*(A**2-1)**2)-r2)==0

# Shared factor gives the implied third character exactly.
r3=2*(s-c)*(s**2-1)
assert sp.factor(r1*r2/(c*s-1)**2-r3)==0

# Reciprocal action: R1 is preserved up to s^-2, R2 maps to R3 up to s^-3.
r1_inv=sp.factor(r1.subs(s,1/s))
r2_inv=sp.factor(r2.subs(s,1/s))
assert sp.factor(r1_inv-r1/s**2)==0
assert sp.factor(r2_inv-r3/s**3)==0

# Positive-order identities inherited from 35EX-28.
assert sp.factor(c-1-(A-1)**2/(2*A))==0
assert sp.factor(A-c-(A**2-1)/(2*A))==0

required_doc=[
    'r^2 = (s-c)*(c*s-1)',
    'ell^2 = 2*(c*s-1)*(s^2-1)',
    'rho^2 = 2*(s-c)*(s^2-1)',
    'GENUS5_FIVE_ELLIPTIC_NEW_CREDIT=false',
    'RECIPROCAL_PHYSICAL_CHAMBER_PRESERVED=false',
    'JOINT_LOCAL_OBSTRUCTION_PROVED=false',
    'E1_PROVED=false',
]
for token in required_doc:
    assert token in doc, token

claims=state['claims']
assert claims['new_theorem_credit'] is False
assert claims['E1_proved'] is False
assert claims['R29_PESCH_E1_closed'] is False
assert claims['stage35_closed'] is False
assert claims['perfect_cuboid_existence_claim'] is False
assert claims['perfect_cuboid_nonexistence_claim'] is False

print('PASS STAGE35_EX_29_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION')
