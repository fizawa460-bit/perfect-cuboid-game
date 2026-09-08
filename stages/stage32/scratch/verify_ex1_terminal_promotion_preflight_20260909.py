#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

OUT=Path(__file__).with_name("ex1-terminal-promotion-preflight-20260909.json")
EXPECTED="a2a7f2351d170424ec818db3992a787280ca96fc7001fccec622b1de4651fefe"

def csha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

x=json.loads(OUT.read_text())
stored=x.pop("canonical_sha256_without_this_field")
assert stored==EXPECTED==csha(x)
assert x["snapshot"]["ex1_pr"]==1728
assert x["snapshot"]["ex1_head"]=="0ea608585ee1c747ee5737240671279f6f595612"
assert x["snapshot"]["ex1_authority"]=="RETAINED_PROVISIONAL_AUDIT_READY"
assert x["snapshot"]["ex1_audit_status"]=="PENDING_HOSTILE_AUDIT"
assert x["main_target_alignment"]["candidate_primary_target_claim"]=="S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1"
assert x["scope_firewalls"]["ex_to_main_promotion_performed"] is False
assert x["scope_firewalls"]["O210_excluded"] is False
assert x["scope_firewalls"]["Q602_excluded"] is False
assert x["stage32_after_hypothetical_v6_promotion"]["would_not_close_stage32"] is True
print(json.dumps({
  "verdict":"PASS_STAGE32_MAIN_SCRATCH_EX1_TERMINAL_PROMOTION_PREFLIGHT",
  "ex1_pr":1728,
  "audit_gate":"PENDING_HOSTILE_AUDIT",
  "primary_future_main_target":"S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1",
  "O210_promoted":False,
  "Q602_promoted":False,
  "stage32_closed":False,
  "canonical_sha256":EXPECTED
},sort_keys=True))
