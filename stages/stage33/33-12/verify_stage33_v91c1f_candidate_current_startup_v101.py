#!/usr/bin/env python3
"""Verify V91C1E authority plus V91C1F type/provenance obstruction candidate startup."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parents[1]; D=H/"33-12"; STATE=H/"MAIN-STATE.json"; AUTH=D/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json"; CAND=D/"e3-v91c1f-a2-02-source-bound-kummer-quotient-marking-obstruction.json"
STATE_SHA="9eab75f049be7fffd40ed99d497f746fa28f1b6b100c00d730877d330d95c64b"; AUTH_SHA="5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f"; CAND_SHA="4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273"; NEXT="V91C1G_CONSTRUCT_SOURCE_SPECIFIC_A2_02_BRAUER_IMAGE_WITNESS_OR_GEOMETRIC_QUOTIENT_ADAPTER_THEN_TEST_MASK20"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b); return o
s,a,c=load(STATE,STATE_SHA),load(AUTH,AUTH_SHA),load(CAND,CAND_SHA)
assert s["authority_sync"]["frontier_authority"]=="V91C1E_A2_02_MARKED_BRAUER_IMAGE_ADAPTER_PREFLIGHT"
assert s["authority_sync"]["branch_candidate_frontier"]=="V91C1F_A2_02_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_TYPE_PROVENANCE_OBSTRUCTION"
ag=s["authority_audit_gate"]; assert ag["pr"]==1639 and ag["hostile_audit_review"]==5123392163 and ag["hostile_audit_verdict"]=="PASS" and ag["audit_pass_credit"] is True
cg=s["candidate_audit_gate"]; assert cg["pr"]==1646 and cg["candidate_certificate_sha256"]==CAND_SHA and cg["status"]=="PENDING_HOSTILE_AUDIT" and cg["hostile_audit_verdict"]=="NOT_RUN" and cg["audit_pass_credit"] is False
assert a["type_safe_adapter_audit"]["literal_h2_seed_to_marked_proper14_quotient_map_materialized_by_locked_assets"] is False
assert c["construction_result"]["exact_obstruction_materialized"] is True and c["construction_result"]["source_bound_kummer_quotient_marking_materialized"] is False
assert c["construction_result"]["a2_02_marked_brauer_image_computed"] is False and c["construction_result"]["a2_02_marked_brauer_image_equal_mask20"] is False and c["construction_result"]["a2_02_claimed_e3_coefficient"] is False and c["construction_result"]["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
assert c["v25_method_decomposition"]["method_pattern_reusable"] is True and c["v25_method_decomposition"]["j2_marking_data_reusable_by_relabelling"] is False
cont=s["continuation_provenance"]; assert cont["v91c1c_pr"]==1620 and cont["hostile_audit_pass_claimed"] is False
assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False and s["firewalls"]["merge_allowed"] is False and s["stage33_progress"]=="6/11"
print(json.dumps({"success":True,"marker":"V101_V91C1F_OBSTRUCTION_CANDIDATE_STARTUP","state_sha256":STATE_SHA,"authority_sha256":AUTH_SHA,"candidate_sha256":CAND_SHA,"next_exact_leaf":NEXT},sort_keys=True))
