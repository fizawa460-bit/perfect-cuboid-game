#!/usr/bin/env python3
"""Verify V91C1F audited authority plus V91C1G V4-naturality candidate startup."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parents[1]; D=H/"33-12"; STATE=H/"MAIN-STATE.json"
AUTH=D/"e3-v91c1f-a2-02-source-bound-kummer-quotient-marking-obstruction.json"
CAND=D/"e3-v91c1g-a2-02-v4-naturality-fixed-subspace-preflight.json"
STATE_SHA="e708fec595ab7008fe18316742f2af11911e15dbd9cdb521a15d10e5eacf72ef"
AUTH_SHA="4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273"
CAND_SHA="2a176993614fac6f4b1555855794642702f3eeb055d710b8f04ac5097e9fb370"
NEXT="V91C1H_CONSTRUCT_SOURCE_BOUND_MARKED_BRAUER_FUNCTIONAL_OR_DIRECT_QUOTIENT_EVALUATION_FOR_A2_02_THEN_TEST_MASK20"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b); return o
s,a,c=load(STATE,STATE_SHA),load(AUTH,AUTH_SHA),load(CAND,CAND_SHA)
assert s["authority_sync"]["frontier_authority"]=="V91C1F_A2_02_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_TYPE_PROVENANCE_OBSTRUCTION"
assert s["authority_sync"]["branch_candidate_frontier"]=="V91C1G_A2_02_V4_NATURALITY_FIXED_SUBSPACE_PREFLIGHT"
ag=s["authority_audit_gate"]; assert ag["pr"]==1646 and ag["hostile_audit_review"]==5123592182 and ag["hostile_audit_verdict"]=="PASS" and ag["audit_pass_credit"] is True
cg=s["candidate_audit_gate"]; assert cg["pr"]==1649 and cg["candidate_certificate_sha256"]==CAND_SHA and cg["status"]=="PENDING_HOSTILE_AUDIT" and cg["hostile_audit_verdict"]=="NOT_RUN" and cg["audit_pass_credit"] is False
assert a["construction_result"]["exact_obstruction_materialized"] is True and a["construction_result"]["a2_02_marked_brauer_image_computed"] is False
assert c["proper14_fixed_subspace_test"]["joint_v4_fixed_dimension_f2"]==10 and c["proper14_fixed_subspace_test"]["mask20_joint_v4_fixed"] is True and c["proper14_fixed_subspace_test"]["v4_naturality_uniquely_identifies_mask20"] is False
r=c["construction_result"]; assert r["a2_02_marked_brauer_image_computed"] is False and r["a2_02_marked_brauer_image_equal_mask20"] is False and r["a2_02_claimed_e3_coefficient"] is False and r["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
cont=s["continuation_provenance"]; assert cont["v91c1c_pr"]==1620 and cont["hostile_audit_pass_claimed"] is False
assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False and s["firewalls"]["merge_allowed"] is False and s["stage33_progress"]=="6/11"
print(json.dumps({"success":True,"marker":"V102_V91C1G_V4_NATURALITY_CANDIDATE_STARTUP","state_sha256":STATE_SHA,"authority_sha256":AUTH_SHA,"candidate_sha256":CAND_SHA,"next_exact_leaf":NEXT},sort_keys=True))
