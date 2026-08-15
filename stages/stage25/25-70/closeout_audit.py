#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]

def text(rel):
    p = root / rel
    assert p.exists(), f"missing {rel}"
    return p.read_text(encoding="utf-8")

def data(rel):
    return json.loads(text(rel))

r = text("stages/stage25/25-70/result.md")
f = text("stages/stage25/final.md")
m = text("stages/stage25/manifest-r01.md")
a = text("docs/stage25-arsenal-promotion.md")
l = text("stages/stage25/25-70/aggressive-search-ledger.md")
c70 = data("stages/stage25/25-70/controller.json")
c60 = data("stages/stage25/25-60/checkpoint60-deep-stop-controller.json")
reentry = data("stages/stage25/25-reentry-controller.json")

# checkpoint60 authorization
assert c60["checkpoint60_deep_stop_rule_satisfied"] is True
assert c60["checkpoint60_closed"] is True
assert c60["stage70_allowed"] is True
assert c60["audit_status"] == "PASS"
assert c60["next_checkpoint"] == 70

# theorem stack markers
for s in (r, f):
    assert "M_1(B)" in s or "M1(B)" in s
    assert "B^{1/4}" in s or "B^(1/4)" in s
    assert "B^{1/2+\\varepsilon}" in s or "B^(1/2+epsilon)" in s
    assert "THIN_BUT_POSITIVE_POWER_INFINITE" in s
    assert "TRUE_TARGET_EXPONENT_IDENTIFIED=false" in s
    assert "PERFECT_CUBOID_CONCLUSION=NONE" in s

# ratio exponents and causal sign
assert "B^{-7/4}" in r
assert "B^{-3/2+\\varepsilon}" in r
assert "POSITIVE_DIVERGENT" in r
assert "B^{1/4}(\\log B)^{-7}" in r

# route registry boundary
for marker in (
    "R501=PROVED_AUDITED_THETA_B_QUARTER",
    "R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS",
    "R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS",
    "R506=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_PREVIOUS_MATH_ACCEPTED",
):
    assert marker in r or marker in m
assert "EXTERNAL_THEOREM_GATE" in r and "R504" in r and "R505" in r

# required Stage70 materializations
assert c70["self_contained_bundle_materialized"] is True
assert c70["arsenal_promotion_materialized"] is True
assert c70["aggressive_search_ledger_materialized"] is True
assert "SELF_CONTAINED_BUNDLE_MATERIALIZED=true" in m
assert "ARSENAL_PROMOTION_MATERIALIZED=true" in m
assert "AGGRESSIVE_SEARCH_LEDGER_MATERIALIZED=true" in m
assert "S25-W01" in a and "S25-W04" in a
assert "CLOSEOUT_SUBMISSION_JUSTIFIED=true" in l

# backflow must be current without fabricating a new theorem delta
assert c70["backflow_status"] == "PASS_NO_DELTA_AFTER_CHECKPOINT50"
assert c70["global_stage25_lower_changed_after_checkpoint50"] is False
assert "BACKFLOW_STATUS=PASS_NO_DELTA_AFTER_CHECKPOINT50" in r

# submission must not self-audit or unlock reentry
assert c70["audit_status"] == "PENDING"
assert c70["advance_allowed"] is False
assert c70["merge_allowed"] is False
assert c70["stage25_reentry_unlocked"] is False
assert c70["close_stage_after_audit_pass"] is True
assert reentry["status"] == "BLOCKED_UNTIL_STAGE25_AUDITED_CLOSEOUT"
assert reentry["starts_after"]["stage25_checkpoint"] == 70
assert reentry["starts_after"]["audit_verdict"] == "PASS"
assert reentry["starts_after"]["closeout_merged"] is True
assert reentry["stage26_gate"]["stage26_allowed"] is False

print("STAGE25_70_CLOSEOUT_CONTRACT=PASS")
print("CHECKPOINT60_DEEP_STOP_DEPENDENCY=PASS")
print("FINAL_THEOREM_STACK_BINDING=PASS")
print("ROUTE_REGISTRY_BOUNDARY=PASS")
print("BACKFLOW_NO_DELTA_BINDING=PASS")
print("REENTRY_BYPASS_FIREWALL=PASS")
