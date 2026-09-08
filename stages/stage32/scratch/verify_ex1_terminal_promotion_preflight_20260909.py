#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

OUT=Path(__file__).with_name("ex1-terminal-promotion-preflight-20260909.json")
EXPECTED="c9a972757f7a2def4dd45bca2bd9cf37755fe481613c6b99a85667674e2bfa29"

def csha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

x=json.loads(OUT.read_text())
stored=x.pop("canonical_sha256_without_this_field")
assert stored==EXPECTED==csha(x)
assert x["snapshot"]["ex1_pr"]==1728
assert x["snapshot"]["ex1_head"]=="0ea608585ee1c747ee5737240671279f6f595612"
assert x["snapshot"]["ex1_hostile_audit_result"]=="FAIL"
assert x["snapshot"]["ex1_hostile_audit_review_id"]==5147121377
assert len(x["audit_fail"]["blockers"])==3
assert x["audit_fail"]["freshness"]=="CLEAR"
assert x["audit_fail"]["strongest_supported_audited_credit"]=="S32.EX1.CANDIDATE_THROUGH_05H.V2_INTERMEDIATE_CEILING_ONLY"
assert x["main_target_alignment"]["candidate_primary_target_claim"]=="S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1"
assert x["scope_firewalls"]["failed_terminal_claim_may_satisfy_main_dependency"] is False
assert x["scope_firewalls"]["ex_to_main_promotion_performed"] is False
assert x["scope_firewalls"]["O210_excluded"] is False
assert x["scope_firewalls"]["Q602_excluded"] is False
assert x["stage32_after_hypothetical_v6_promotion"]["would_not_close_stage32"] is True
print(json.dumps({
  "verdict":"PASS_STAGE32_MAIN_SCRATCH_EX1_TERMINAL_PROMOTION_BLOCKED_BY_AUDIT_FAIL",
  "ex1_pr":1728,
  "audit_result":"FAIL",
  "audit_review_id":5147121377,
  "blocker_count":3,
  "strongest_audited_credit":"S32.EX1.CANDIDATE_THROUGH_05H.V2",
  "primary_future_main_target":"S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1",
  "O210_promoted":False,
  "Q602_promoted":False,
  "stage32_closed":False,
  "canonical_sha256":EXPECTED
},sort_keys=True))
