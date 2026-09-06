#!/usr/bin/env python3
"""Verify current Stage33 startup projection after V91C1H promotion."""
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
S=HERE.parent/"MAIN-STATE.json"
C=HERE/"e3-v91c1t-a2-02-swap23-pic2-adapter-preflight.json"
STATE_SHA="263bfb052deb8c59b7ed93fc7790ce45533334c3e81743fa772906021b52bea1"
CAND_SHA="6c064cf02fb7a0908242317bf7ac1b20b0586751b78e07b26d6c7889060ffdfa"

def csha(o):
 return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def load(path, expected):
 o=json.loads(path.read_text(encoding="utf-8")); b=dict(o); h=b.pop("canonical_sha256")
 assert h==expected==csha(b),path
 return o

s=load(S,STATE_SHA); c=load(C,CAND_SHA)
assert s["authority_audit_gate"]["authority"]=="V91C1H_A2_02_STAGE33_07_LOCALIZATION_QUOTIENT_PREFLIGHT"
assert s["authority_audit_gate"]["hostile_audit_review"]==5124792802
assert s["authority_audit_gate"]["merge_commit"]=="7a608ee2511192af8e293d88f8a7117aa5ad19d9"
assert s["candidate_audit_gate"]["candidate"]=="V91C1T_A2_02_SWAP23_PIC2_ADAPTER_PREFLIGHT"
assert s["candidate_audit_gate"]["pr"]==1661
assert s["candidate_audit_gate"]["status"]=="PENDING_HOSTILE_AUDIT"
assert s["execution_gate"]["advance_allowed"] is False
assert s["firewalls"]["merge_allowed"] is False
assert c["exact_consequence"]["pic2_cech_difference_class_computed"] is False
assert c["anti_inference"]["j2_pic2_machinery_relabelled_as_a2_02"] is False
print(json.dumps({"success":True,"marker":"V104_STAGE33_V91C1H_AUTHORITY_V91C1T_CANDIDATE_STARTUP","state_sha256":STATE_SHA,"candidate_sha256":CAND_SHA,"pr":1661,"stage33_progress":"6/11"},sort_keys=True))
