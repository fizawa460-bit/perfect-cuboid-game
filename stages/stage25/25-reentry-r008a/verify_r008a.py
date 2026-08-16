#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def text(rel: str) -> str:
    p = ROOT / rel
    assert p.exists(), f"missing {rel}"
    return p.read_text(encoding="utf-8")


def data(rel: str):
    return json.loads(text(rel))


registry = data("stages/stage25/25-reentry-r008a/backflow-registry.json")
result = text("stages/stage25/25-reentry-r008a/result.md")
controller = data("stages/stage25/25-reentry-controller.json")
audit20 = text("stages/stage25/25-reentry-20/audit.md")
stage19 = text("stages/stage19/post-stage25-50-supersession.md")
stage23 = text("stages/stage23/post-stage25-r01/result.md")
stage24 = text("stages/stage24/post-stage25-r01/result.md")
stage24_final = text("stages/stage24/final.md")
status_doc = text("docs/00_CURRENT_RESEARCH_STATUS.md")

# Parent authorization is immutable.
assert registry["route_id"] == "Stage25-um-r008a"
assert registry["parent_task"] == "Stage25-u24-r002a"
assert registry["source"]["pr"] == 1003
assert registry["source"]["merge_commit"] == "1d88e8e3254a383620e221df8a1a1039ebeabcd4"
assert registry["source"]["accepted_theorem"] == "N2,j(B)>>_j B^(1/4) for j=a,b,c"
assert "AUDIT_VERDICT=PASS" in audit20
assert "N2,j(B) >>_j B^(1/4)" in audit20

# Receiver species and exact shared-edge map.
receivers = registry["receivers"]
assert set(receivers) == {"Stage19", "Stage23", "Stage24"}
assert receivers["Stage19"]["population_match"] == "EXACT"
assert receivers["Stage23"]["population_match"] == "ONE_SIDED_INCIDENCE_EMBEDDING"
assert receivers["Stage24"]["population_match"] == "EXACT_DIRECTIONAL_STAGE18_TO_STAGE19"
assert receivers["Stage23"]["shared_edge_to_pair"] == {
    "a": "ab,ac",
    "b": "ab,bc",
    "c": "ac,bc",
}

# Exponent/log algebra for directional Stage24 survival and ambient interaction.
N2j = (Fraction(1, 4), Fraction(0))
M2j = (Fraction(1), Fraction(5))
S0 = (Fraction(-1), Fraction(0))
survival = (N2j[0] - M2j[0], N2j[1] - M2j[1])
interaction = (survival[0] - S0[0], survival[1] - S0[1])
assert survival == (Fraction(-3, 4), Fraction(-5))
assert interaction == (Fraction(1, 4), Fraction(-5))
assert "DIRECTIONAL_THEOREM=M2,j(B)~C_j B(log B)^5 for j=a,b,c with C_j>0" in stage24_final

# Stage19 current directional receiver.
for marker in (
    "N2,a(B)>>B^(1/4)",
    "N2,b(B)>>B^(1/4)",
    "N2,c(B)>>B^(1/4)",
    "ALL_DIRECTIONAL_QUARTER_POWER_LOWER_PROVED=true",
):
    assert marker in stage19, marker
assert "GLOBAL_N2_EXPONENT_UPGRADED=false" in stage19

# Stage23 all three raw pair-overlap receivers.
for marker in (
    "A_ab,ac(B)>>B^(1/4)",
    "A_ab,bc(B)>>B^(1/4)",
    "A_ac,bc(B)>>B^(1/4)",
    "ALL_PAIR_OVERLAP_QUARTER_POWER_LOWER_PROVED=true",
):
    assert marker in stage23, marker
assert "RAW_OVERLAP_IS_OBJECTWISE_SURVIVAL=false" in stage23

# Stage24 directional survival and J2 receivers.
for marker in (
    "N2,j/M2,j>>_j B^(-3/4)(log B)^(-5) for j=a,b,c",
    "J2,j>>_j B^(1/4)(log B)^(-5)->infinity for j=a,b,c",
    "ALL_DIRECTIONAL_SURVIVAL_LOWER_SYNCED=true",
    "ALL_DIRECTIONAL_J2_POSITIVE_DIVERGENT=true",
):
    assert marker in stage24, marker
assert "GLOBAL_N2_EXPONENT_UPGRADED=false" in stage24

# No forbidden upgrade/accounting mutation.
assert registry["accounting"]["parent_theorem_reproved"] is False
assert registry["accounting"]["new_global_N2_exponent"] is False
assert registry["accounting"]["double_charge"] is False
assert registry["accounting"]["finite_data_promoted"] is False
assert registry["accounting"]["raw_overlap_reinterpreted_as_survival_probability"] is False
assert registry["gates"]["stage26_allowed"] is False
assert registry["gates"]["true_N2_exponent_identified"] is False

# Lifecycle. The route may later be audited/merged, but phase30 cannot bypass it.
r8 = controller["r008a_submission"]
assert r8["route_id"] == "Stage25-um-r008a"
assert r8["parent_pr"] == 1003
assert r8["parent_merge_commit"] == registry["source"]["merge_commit"]
assert controller["stage26_gate"]["stage26_allowed"] is False

if controller["current_phase"] == 20:
    assert controller["status"] in (
        "PHASE20_BACKFLOW_SUBMITTED_PENDING_FRESH_AUDIT",
        "PHASE20_BACKFLOW_AUDITED_PASS_AWAITING_MERGE",
    )
    queued = [x for x in controller["propagation_queue"] if x["route_id"] == "Stage25-um-r008a"]
    assert len(queued) == 1
    assert queued[0]["blocks_next_phase"] is True
    assert controller["phases"]["30"]["status"] == "BLOCKED_UNTIL_R008A_AUDIT_PASS_MERGE"
    if r8["audit_status"] == "PENDING":
        assert r8["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
        assert r8["advance_allowed"] is False
        assert r8["merge_allowed"] is False
        assert controller["next_expected_command"] == "Stage25-reentry-audit"
    else:
        assert r8["audit_status"] == "PASS"
        assert r8["status"] == "AUDITED_PASS_AWAITING_MERGE"
        assert r8["advance_allowed"] is True
        assert r8["merge_allowed"] is True
else:
    assert controller["current_phase"] in (30, 40, 50, 60, 70)
    assert r8["status"] == "AUDITED_PASS_MERGED"
    assert r8["audit_status"] == "PASS"
    assert r8["merge_commit"]
    assert not any(x["route_id"] == "Stage25-um-r008a" and x["blocks_next_phase"] for x in controller["propagation_queue"])

for marker in (
    "STAGE25_REENTRY_ROUTE_R008A=Stage25-um-r008a",
    "STAGE25_REENTRY_PHASE30_ALLOWED=false",
    "STAGE26_ALLOWED=false",
):
    assert marker in status_doc, marker

for marker in (
    "GLOBAL_N2_EXPONENT_UPGRADED=false",
    "TRUE_N2_EXPONENT_IDENTIFIED=false",
    "FINITE_DATA_USED_AS_PROOF=false",
    "PERFECT_CUBOID_CONCLUSION=NONE",
):
    assert marker in result, marker

print("STAGE25_REENTRY_R008A_PARENT_AUTHORIZATION=PASS")
print("STAGE25_REENTRY_R008A_STAGE19_DIRECTIONAL_SYNC=PASS")
print("STAGE25_REENTRY_R008A_STAGE23_PAIR_OVERLAP_SYNC=PASS")
print("STAGE25_REENTRY_R008A_STAGE24_DIRECTIONAL_SYNC=PASS")
print("STAGE25_REENTRY_R008A_EXPONENT_ALGEBRA=PASS")
print("STAGE25_REENTRY_R008A_ACCOUNTING_FIREWALL=PASS")
print("STAGE25_REENTRY_R008A_LIFECYCLE=PASS")
print("STAGE26_GATE=BLOCKED_VALID")
