#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
DOC=ROOT/'stages/stage35-ex/35ex-28/full-rational-source-kummer-completion.md'
CERT=ROOT/'stages/stage35-ex/35ex-28/full-rational-source-kummer-certificate.json'
AUDIT=ROOT/'stages/stage35-ex/35ex-27/post-rational-source-kummer-breadth-audit.json'
S31=ROOT/'docs/arsenal/cards/formal/S31-W01.md'
S34=ROOT/'docs/arsenal/cards/formal/S34-W03.md'
V27='STAGE35_EX_PESCH_E1_STATE_V27_POST_35EX28_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION'
CURRENT_MAIN='dc5898281a7ccea25d8ee0c1ae9953a18941ec08'

def blob(path):
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

state=json.loads(STATE.read_text())
cert=json.loads(CERT.read_text())
audit=json.loads(AUDIT.read_text())
doc=DOC.read_text()
assert state['schema']==V27 and state['stage']=='35-EX' and state['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha']==CURRENT_MAIN
parent=state['parent_authority']
assert parent['unit']=='35EX-27' and parent['status']=='AUDITED_EXACT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_NO_CREDIT'
assert parent['hostile_audit_verdict']=='PASS' and parent['pass_source']=='USER_CONFIRMED_HOSTILE_PASS'
assert parent['audited_head_sha']=='dc1930632304d2c47e5583e4d8cb324cbbd73e15'
assert parent['exact_head_ci_run']==33929237884 and parent['exact_head_ci_job']==101204270892
assert parent['merged_main_sha']=='ee3e7aafd1742c5d96e2871f117412ef0823d57e' and parent['audited_theorem_credit'] is False
u27=state['completed_units']['35EX-27']; u27b=state['completed_units']['35EX-27B']; u28=state['completed_units']['35EX-28']
assert u27['status']=='AUDITED_EXACT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_NO_CREDIT' and u27['audited_theorem_credit'] is False
assert u27b['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT' and u27b['selected_candidate']=='E1-FULL-RATIONAL-SOURCE-KUMMER-COMPLETION'
assert u28['status']=='PROVISIONAL_EXACT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_NO_CREDIT' and u28['audited_theorem_credit'] is False
assert state['current']['unit']=='35EX-28_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_OR_JOINT_LOCAL_FIREWALL'
assert state['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False

assert audit['schema']=='STAGE35_EX_27B_POST_RATIONAL_SOURCE_KUMMER_FRESH_BREADTH_AUDIT_V1'
assert audit['protocol']['blind_generation_performed_before_arsenal_comparison'] is True
assert audit['selection']['selected_candidate']=='E1-FULL-RATIONAL-SOURCE-KUMMER-COMPLETION'
assert audit['selection']['selected_next_unit']=='35EX-28_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_OR_JOINT_LOCAL_FIREWALL'
assert cert['schema']=='STAGE35_EX_28_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_CERTIFICATE_V1'
assert cert['quotient_base_completion']['K4_iff_quotient_base_square'] is True
assert cert['quotient_base_completion']['full_rational_source_K1_K4_exact'] is True
assert cert['second_fixed_A_genus_one']['generic_smooth_on_retained_open'] is True
assert cert['second_fixed_A_genus_one']['absolute_invariant_nonconstant'] is True
assert blob(AUDIT)==cert['fresh_breadth_audit']['blob_sha']
assert blob(S31)==cert['arsenal']['S31_W01']['blob_sha']
assert blob(S34)==cert['arsenal']['S34_W03']['blob_sha']
assert cert['arsenal']['S34_W02_unlocked'] is False

# K1 factorization and K4 quotient-base completion.
A,beta=sp.symbols('A beta', nonzero=True)
u=sp.factor(2*A*(beta**2-1)/(beta*(A**2-1)))
uplus=sp.factor(2*(A+beta)*(A*beta-1)/(beta*(A**2-1)))
assert sp.factor(u+2-uplus)==0
raw=sp.factor(4*A*(beta**2-1)*(A+beta)*(A*beta-1)/(beta**2*(A**2-1)**2))
assert sp.factor(u*(u+2)-raw)==0
t=sp.factor((A*beta+1)/(A+beta))
k4=sp.factor((beta**2-1)*(A**2*beta**2-1))
reduced=sp.factor(4*A*k4/(t*beta**2*(A**2-1)**2))
assert sp.factor(raw-reduced)==0

# Exact positive-chamber algebra behind ORD.
assert sp.factor(t-1-(A-1)*(beta-1)/(A+beta))==0
assert sp.factor(A-t-(A**2-1)/(A+beta))==0
mid=(A**2+1)/(2*A)
assert sp.factor(t-mid-(A**2-1)*(beta-A)/(2*A*(A+beta)))==0

# K4 fixed-A quartic invariants and nonisotriviality.
I=sp.factor(A**4+14*A**2+1)
J=sp.factor(2*(A**2+1)*(A**4-34*A**2+1))
disccombo=sp.factor(4*I**3-J**2)
assert sp.factor(disccombo-432*A**2*(A-1)**4*(A+1)**4)==0
ratio=sp.factor(J**2/I**3)
assert sp.factor(sp.diff(ratio,A)) != 0

for marker in (
    'QUOTIENT_BASE_SQUARE_INTERNALIZED=true',
    'K4_EXACT=true',
    'K4_IFF_QUOTIENT_BASE_SQUARE=true',
    'FULL_RATIONAL_SOURCE_KUMMER_SYSTEM_K1_K4=true',
    'POSITIVE_CHAMBER_ORDER_EXACT=true',
    'SECOND_FIXED_A_GENUS_ONE_QUARTIC_EXACT=true',
    'SECOND_FIXED_A_GENUS_ONE_NONISOTRIVIAL=true',
    'PAIRED_GENUS_ONE_ISOGENY_PROVED=false',
    'JOINT_LOCAL_OBSTRUCTION_PROVED=false',
    'RECEIVER_INTERSECTION_CLOSED=false',
    'E1_PROVED=false',
    'STAGE35_CLOSED=false'):
    assert marker in doc
for key in ('new_theorem_credit','paired_genus_one_isogeny_proved','joint_local_obstruction_proved','receiver_intersection_closed','uniform_receiver_emptiness','uniform_full_MW_group','new_Brauer_obstruction','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim','audited_theorem_credit'):
    assert cert['claims'][key] is False
print('PASS STAGE35_EX_28_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION')
