#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
DOC=ROOT/'stages/stage35-ex/35ex-27/rational-source-lift-kummer-normal-form.md'
CERT=ROOT/'stages/stage35-ex/35ex-27/rational-source-lift-kummer-certificate.json'
AUDIT=ROOT/'stages/stage35-ex/35ex-26/post-base-involution-breadth-audit.json'
S31=ROOT/'docs/arsenal/cards/formal/S31-W01.md'
S34=ROOT/'docs/arsenal/cards/formal/S34-W03.md'
V26='STAGE35_EX_PESCH_E1_STATE_V26_POST_35EX27_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM'
CURRENT_MAIN='09d42186c06cd906042f2ca3f16a9deaf4f1b4a3'

def blob(path):
    data=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

state=json.loads(STATE.read_text()); cert=json.loads(CERT.read_text()); audit=json.loads(AUDIT.read_text()); doc=DOC.read_text()
assert state['schema']==V26 and state['stage']=='35-EX' and state['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha']==CURRENT_MAIN
parent=state['parent_authority']
assert parent['unit']=='35EX-26' and parent['status']=='AUDITED_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT'
assert parent['pass_source']=='USER_CONFIRMED_HOSTILE_PASS'
assert parent['audited_head_sha']=='d836c743628b47d62e4db18c344981be8fe839f4'
assert parent['exact_head_ci_run']==33926330680 and parent['exact_head_ci_job']==101195546705
assert parent['merged_main_sha']=='74144644975d7800c6c5b529c5d8789f70366c2e' and parent['audited_theorem_credit'] is False
u26=state['completed_units']['35EX-26']; u26b=state['completed_units']['35EX-26B']; u27=state['completed_units']['35EX-27']
assert u26['status']=='AUDITED_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT' and u26['audited_theorem_credit'] is False
assert u26b['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT' and u26b['selected_candidate']=='E1-RATIONAL-SOURCE-LIFT-KUMMER-NORMAL-FORM'
assert u27['status']=='PROVISIONAL_EXACT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_NO_CREDIT' and u27['audited_theorem_credit'] is False
assert state['current']['unit']=='35EX-27_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_OR_DESCENDED_OVERCOVER_FIREWALL'
assert state['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False

assert audit['schema']=='STAGE35_EX_26B_POST_BASE_INVOLUTION_FRESH_BREADTH_AUDIT_V1'
assert audit['protocol']['blind_generation_performed_before_arsenal_comparison'] is True
assert audit['selection']['selected_candidate']=='E1-RATIONAL-SOURCE-LIFT-KUMMER-NORMAL-FORM'
assert audit['selection']['selected_next_unit']=='35EX-27_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_OR_DESCENDED_OVERCOVER_FIREWALL'
assert cert['schema']=='STAGE35_EX_27_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_CERTIFICATE_V1'
assert cert['rational_source_lift']['rational_source_lift_iff'] is True
assert cert['kummer_coordinates']['exact'] is True
assert cert['fixed_alpha_genus_one']['generic_smooth_on_retained_open'] is True
assert cert['fixed_alpha_genus_one']['absolute_invariant_nonconstant'] is True
assert blob(S31)==cert['arsenal']['S31_W01']['blob_sha'] and blob(S34)==cert['arsenal']['S34_W03']['blob_sha']
assert cert['arsenal']['S34_W02_unlocked'] is False

# Rational source lift converse.
u,h,k=sp.symbols('u h k', nonzero=True)
x=(u+k)/2
p=h*x/(x+1)
inv=sp.factor(x*(u-k)/2-1).subs(k**2,u**2-4)
assert sp.factor(inv)==0
pnum=sp.expand(sp.together(p**2-(1+x**2)).as_numer_denom()[0]).subs(h**2,u*(u+2))
krel=sp.Poly(k**2-(u**2-4),k)
assert sp.factor(sp.rem(sp.Poly(sp.expand(pnum),k),krel).as_expr())==0

# K1, K2 and K3 exact algebra.
A,beta=sp.symbols('A beta', nonzero=True)
uAB=sp.factor(2*A*(beta**2-1)/(beta*(A**2-1)))
b2=sp.factor((A*beta+1)/(A+beta))
q4_from_hyperbola=sp.factor((uAB/2*(A+1/A)+beta+1/beta)/(uAB+2))
assert sp.factor(q4_from_hyperbola-b2)==0
k2=sp.factor(uAB**2-4)
square_prefactor=sp.factor(4*b2*(A+beta)**2/(beta**2*(A**2-1)**2))
assert sp.factor(k2/square_prefactor-(beta-A)*(A*beta-1))==0

# Eliminate beta through t=b^2 and recover fixed-A quartic.
t=sp.symbols('t', nonzero=True)
betat=sp.factor((1-A*t)/(t-A))
quart=sp.factor((betat-A)*(A*betat-1)*(t-A)**2)
expected=sp.factor((A**2+1-2*A*t)*(2*A-(A**2+1)*t))
assert sp.factor(quart-expected)==0

# Binary quartic invariants and generic smoothness/nonisotriviality.
C=A**2+1; D=2*A; aa=C*D; cc=-(C**2+D**2); ee=C*D
I=sp.factor(12*aa*ee+cc**2)
J=sp.factor(72*aa*cc*ee-2*cc**3)
disccombo=sp.factor(4*I**3-J**2)
assert I==A**8+60*A**6+134*A**4+60*A**2+1
assert sp.factor(disccombo-1728*A**2*(A-1)**8*(A+1)**8*(A**2+1)**2)==0
ratio=sp.factor(J**2/I**3)
assert sp.factor(sp.diff(ratio,A)) != 0

for marker in (
 'RATIONAL_SOURCE_LIFT_DISCRIMINANT_REQUIRED=true',
 'RATIONAL_SOURCE_LIFT_IFF_H_AND_K_SQUARES=true',
 'DESCENDED_KUMMER_NORMAL_FORM_EXACT=true',
 'Q4_MOBIUS_SQUARE_EXACT=true',
 'SOURCE_LIFT_SECOND_KUMMER_SQUARE_EXACT=true',
 'FIXED_ALPHA_GENUS_ONE_QUARTIC_EXACT=true',
 'FIXED_ALPHA_FAMILY_NONISOTRIVIAL=true',
 'RECEIVER_INTERSECTION_CLOSED=false',
 'E1_PROVED=false',
 'STAGE35_CLOSED=false'):
    assert marker in doc
for key in ('new_theorem_credit','uniform_receiver_emptiness','uniform_full_MW_group','new_Brauer_obstruction','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim','audited_theorem_credit'):
    assert cert['claims'][key] is False
print('PASS STAGE35_EX_27_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM')
