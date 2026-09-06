#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parents[1]; D=H/'33-12'; STATE=H/'MAIN-STATE.json'; AUTH=D/'e3-v91c1g-a2-02-v4-naturality-fixed-subspace-preflight.json'; CAND=D/'e3-v91c1h-a2-02-stage33-07-localization-quotient-preflight.json'
STATE_SHA='30914ca4245ade106985f44d9c64cc79ffd9bc6c4cf04ba6ad3eff4bbf45518d'; AUTH_SHA='2a176993614fac6f4b1555855794642702f3eeb055d710b8f04ac5097e9fb370'; CAND_SHA='d05672463ce6340773b6a4394851398360cf58b03f544ea4c00ff0d345089be2'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
s=load(STATE,STATE_SHA); a=load(AUTH,AUTH_SHA); c=load(CAND,CAND_SHA)
assert s['authority_sync']['frontier_authority']=='V91C1G_A2_02_V4_NATURALITY_FIXED_SUBSPACE_PREFLIGHT'
assert s['authority_audit_gate']['pr']==1649 and s['authority_audit_gate']['hostile_audit_review']==5123633478 and s['authority_audit_gate']['hostile_audit_verdict']=='PASS'
assert s['authority_audit_gate']['merge_commit']=='43f3f3b135a2f5664cb8cc736d6db0b37d7b79da'
assert s['candidate_audit_gate']['pr']==1653 and s['candidate_audit_gate']['candidate_certificate_sha256']==CAND_SHA and s['candidate_audit_gate']['status']=='PENDING_HOSTILE_AUDIT'
assert a['proper14_fixed_subspace_test']['joint_v4_fixed_dimension_f2']==10 and c['stage33_07_route_audit']['route_supplies_source_specific_marked_proper14_coordinate_for_A2_02'] is False
assert s['current_exact_frontier']['a2_02_marked_brauer_image_computed'] is False and s['current_exact_frontier']['a2_02_claimed_e3_coefficient'] is False and s['current_exact_frontier']['e3_kummer_column_materialized'] is False
assert s['continuation_provenance']['v91c1c_pr']==1620 and s['continuation_provenance']['hostile_audit_pass_claimed'] is False
assert s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False and s['stage33_progress']=='6/11'
print(json.dumps({'success':True,'marker':'V103_V91C1H_LOCALIZATION_PREFLIGHT_CANDIDATE_STARTUP','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'next_exact_leaf':s['current']['next_exact_leaf']},sort_keys=True))
