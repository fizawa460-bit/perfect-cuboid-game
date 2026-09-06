#!/usr/bin/env python3
"""V100: current Stage33 startup projection after V91C1E promotion and V91C1F-S1 candidate."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parents[1]; S=H/"MAIN-STATE.json"; D=Path(__file__).resolve().parent; C=D/"e3-v91c1f-s1-a2-02-source-bound-kummer-quotient-marking-contract.json"
STATE_SHA="c105bed2d0dc24822eac019463a82f3baad42bdbd4cf7cef6e806296c3bbf949"; CERT_SHA="3f9bee9108bbf93b304c6d0fdae4235717c3fe919647c882fcc4ef5e822d3c93"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b),p; return o
s=load(S,STATE_SHA); c=load(C,CERT_SHA)
assert s["role"]=="ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE"
assert s["authority_sync"]["frontier_authority"]=="V91C1E_A2_02_MARKED_BRAUER_IMAGE_ADAPTER_PREFLIGHT"
assert s["candidate_audit_gate"]["pr"]==1645 and s["candidate_audit_gate"]["hostile_audit_verdict"]=="NOT_RUN"
assert s["execution_gate"]["advance_allowed"] is False and s["firewalls"]["merge_allowed"] is False
assert s["stage33_progress"]=="6/11" and S.stat().st_size<9800
assert c["required_source_bound_marking_witness"]["materialized"] is False
assert c["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False
print(json.dumps({"success":True,"marker":"V100_CURRENT_STARTUP_V91C1F_S1_PENDING_HOSTILE_AUDIT","state_sha256":STATE_SHA,"certificate_sha256":CERT_SHA},sort_keys=True))
