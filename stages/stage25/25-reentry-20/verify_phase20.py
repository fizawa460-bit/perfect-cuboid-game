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


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def poly_scale(a, s):
    return [v * s for v in a]


def poly_mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def poly_pow(a, n):
    out = [Fraction(1)]
    for _ in range(n): out = poly_mul(out, a)
    return out


def poly_eval(a, x):
    out = Fraction(0)
    for c in reversed(a): out = out * x + c
    return out


registry = data("stages/stage25/25-reentry-20/directional-registry.json")
backflow = data("stages/stage25/25-reentry-20/backflow-proposals.json")
reentry = data("stages/stage25/25-reentry-controller.json")
result = text("stages/stage25/25-reentry-20/result.md")
proof = text("stages/stage25/25-reentry-20/directional-quarter-power.md")
discovery = text("stages/stage25/25-reentry-20/discovery-ledger.md")
weapons = text("stages/stage25/25-reentry-20/weapon-delta.md")
status_doc = text("docs/00_CURRENT_RESEARCH_STATUS.md")
r501 = text("stages/stage25/25-50/r501-parametric-positive-power.md")
r502 = text("stages/stage25/25-60/r502-primitive-height-no-upgrade.md")
r502_audit = text("stages/stage25/25-60/audit-recheck.md")
stage24 = text("stages/stage24/final.md")
phase10_audit = text("stages/stage25/25-reentry-10/audit.md")

# Authorization and lifecycle. Phase20 artifacts remain immutable after audit;
# the controller may subsequently be in the authorized r008a backflow lane.
assert registry["task_id"] == "Stage25-u24-r002a"
assert registry["phase"] == 20
assert registry["authorization"]["phase10_pr"] == 1002
assert registry["authorization"]["phase10_merge_commit"] == "5cb7dc8792faf575c1e21fce8166f094af6d7b14"
assert "AUDIT_VERDICT=PASS" in phase10_audit
assert reentry["current_phase"] == 20
assert reentry["phases"]["10"]["status"] == "AUDITED_PASS_MERGED"
assert reentry["stage26_gate"]["stage26_allowed"] is False

lifecycle = reentry["status"]
assert lifecycle in (
    "PHASE20_SUBMITTED_PENDING_FRESH_AUDIT",
    "PHASE20_AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW",
    "PHASE20_BACKFLOW_SUBMITTED_PENDING_FRESH_AUDIT",
    "PHASE20_BACKFLOW_AUDITED_PASS_AWAITING_MERGE",
)
if lifecycle == "PHASE20_SUBMITTED_PENDING_FRESH_AUDIT":
    assert reentry["phases"]["20"]["status"] == "SUBMITTED_PENDING_AUDIT"
    assert reentry["phase20_submission"]["audit_status"] == "PENDING"
    assert reentry["phase20_submission"]["advance_allowed"] is False
    assert reentry["phase20_submission"]["merge_allowed"] is False
    assert reentry["next_expected_command"] == "Stage25-reentry-audit"
elif lifecycle == "PHASE20_AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW":
    p20 = reentry["phase20_submission"]
    assert reentry["phases"]["20"]["status"] == "AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW"
    assert p20["audit_status"] == "PASS"
    assert p20["advance_allowed"] is True
    assert p20["merge_allowed"] is True
    assert p20["stronger_result_proved"] is True
    assert p20["new_reusable_weapon_proved"] is True
    assert p20["audit_record"] == "stages/stage25/25-reentry-20/audit.md"
    assert "AUDIT_VERDICT=PASS" in text(p20["audit_record"])
    assert reentry["phases"]["30"]["status"] == "BLOCKED_UNTIL_PHASE20_BACKFLOW"
    assert reentry["next_expected_command"] == "merge PR #1003; then Stage25-reentry-main-batch"
else:
    p20 = reentry["phase20_submission"]
    assert p20["audit_status"] == "PASS"
    assert p20["stronger_result_proved"] is True
    assert p20["new_reusable_weapon_proved"] is True
    assert p20["pr"] == 1003
    assert p20["merge_commit"] == "1d88e8e3254a383620e221df8a1a1039ebeabcd4"
    assert reentry["phases"]["20"]["status"] in (
        "AUDITED_PASS_MERGED_BACKFLOW_PENDING_AUDIT",
        "AUDITED_PASS_MERGED_BACKFLOW_AUDITED_PASS_AWAITING_MERGE",
    )
    r8 = reentry["r008a_submission"]
    assert r8["route_id"] == "Stage25-um-r008a"
    assert r8["parent_pr"] == 1003
    assert r8["parent_merge_commit"] == p20["merge_commit"]
    assert reentry["phases"]["30"]["status"] == "BLOCKED_UNTIL_R008A_AUDIT_PASS_MERGE"
    if lifecycle == "PHASE20_BACKFLOW_SUBMITTED_PENDING_FRESH_AUDIT":
        assert r8["audit_status"] == "PENDING"
        assert r8["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
        assert reentry["next_expected_command"] == "Stage25-reentry-audit"
    else:
        assert r8["audit_status"] == "PASS"
        assert r8["status"] == "AUDITED_PASS_AWAITING_MERGE"

# Exact R501 factor identities for the new a-cone.
t = [Fraction(0), Fraction(1)]
one = [Fraction(1)]
t2 = poly_pow(t, 2)
t4 = poly_pow(t, 4)
A = poly_scale(poly_mul(t2, poly_add(t4, [Fraction(-9)])), Fraction(16))
f = poly_add(t4, poly_add(poly_scale(t2, Fraction(-10)), [Fraction(9)]))
g = poly_add(t4, poly_add(poly_scale(t2, Fraction(2)), [Fraction(9)]))
B = poly_mul(f, g)
C = poly_scale(poly_mul(poly_mul(t, poly_add(t2, [Fraction(3)])), f), Fraction(4))
Q1 = [Fraction(9), Fraction(-12), Fraction(2), Fraction(-4), Fraction(1)]
Q2 = [Fraction(9), Fraction(12), Fraction(-10), Fraction(-4), Fraction(1)]
prod = one
for root in (3, 1, -1, -3):
    prod = poly_mul(prod, [Fraction(-root), Fraction(1)])
assert poly_add(B, poly_scale(C, -1)) == poly_mul(prod, Q1)
assert poly_add(A, poly_scale(C, -1)) == poly_scale(poly_mul(poly_mul(t, poly_add(t2, [Fraction(3)])), Q2), -4)

# Interval sign certificate.
x0 = Fraction(9, 2)
assert poly_eval(Q1, x0) == Fraction(657, 16)
q1prime = [Fraction(-12), Fraction(4), Fraction(-12), Fraction(4)]
q1fact = poly_scale(poly_mul([Fraction(-3), Fraction(1)], poly_add(t2, [Fraction(1)])), 4)
assert q1prime == q1fact
H = [Fraction(3), Fraction(-5), Fraction(-3), Fraction(1)]
q2prime = [Fraction(12), Fraction(-20), Fraction(-12), Fraction(4)]
assert q2prime == poly_scale(H, 4)
assert poly_eval(H, x0) == Fraction(87, 8) > 0
Hprime = [Fraction(-5), Fraction(-6), Fraction(3)]
assert poly_eval(Hprime, x0) == Fraction(115, 4) > 0
assert poly_eval(Q2, Fraction(5)) == Fraction(-56) < 0

# Existing family premises remain bound to audited sources.
for marker in (
    r"A^2+C^2=D_{AC}^2",
    r"B^2+C^2=D_{BC}^2",
    r"N_2(B)\gg B^{1/4}",
    "PARAMETER_FIBER_BOUND=8",
    "THIRD_FACE_EXCEPTION_CURVE_GENUS=7",
):
    assert marker in r501, marker
assert "0<A<B<C" in r502
assert "R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))" in r502
assert "R502_EXACT_FAMILY_GROWTH_ACCEPTED=Theta(B^(1/4))" in r502_audit

# Directional denominator and upper interfaces are audited Stage24 inputs.
assert "DIRECTIONAL_THEOREM=M2,j(B)~C_j B(log B)^5 for j=a,b,c with C_j>0" in stage24
assert r"N_{2,j}(B)" in stage24 and r"M_{2,j}(B)" in stage24

# Registry binds exactly three canonical shared-edge directions.
dirs = registry["directional_families"]
assert set(dirs) == {"a", "b", "c"}
assert dirs["a"]["canonical_shared_edge"] == "a"
assert dirs["b"]["canonical_shared_edge"] == "b"
assert dirs["c"]["canonical_shared_edge"] == "c"
assert dirs["a"]["cone"] == "9/2<t<5"
assert dirs["a"]["status"] == "NEW_CONE_CANDIDATE_PENDING_AUDIT"
assert dirs["c"]["exact_family_growth"] == "Theta(B^(1/4))"
assert registry["global_surface"]["global_exponent_upgraded"] is False
assert registry["scope_firewall"]["true_N2_exponent_identified"] is False

# The original backflow proposal is an immutable parent-submission artifact.
assert backflow["status"] == "QUEUED_PENDING_PARENT_AUDIT"
assert len(backflow["proposals"]) == 1
p = backflow["proposals"][0]
assert p["theorem_changing"] is True
assert p["action"] == "QUEUE_DERIVED_ROUTE"
assert p["derived_route"] == "Stage25-um-r008a"
assert p["affected_stages"] == [19, 23, 24]
assert backflow["derived_routes_opened"] == []
assert backflow["queued_derived_routes"] == ["Stage25-um-r008a"]
assert reentry["derived_route_policy"]["next_route_serial"] == 9
assert reentry["propagation_queue"][0]["route_id"] == "Stage25-um-r008a"
if lifecycle == "PHASE20_SUBMITTED_PENDING_FRESH_AUDIT":
    assert reentry["propagation_queue"][0]["status"] == "QUEUED_UNTIL_PHASE20_AUDIT_PASS"
elif lifecycle == "PHASE20_AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW":
    assert reentry["propagation_queue"][0]["status"] == "AUTHORIZED_BY_PHASE20_AUDIT_AWAITING_PARENT_MERGE"
else:
    assert reentry["propagation_queue"][0]["status"] in (
        "SUBMITTED_PENDING_FRESH_AUDIT",
        "AUDITED_PASS_AWAITING_MERGE",
    )

# Required theorem/non-theorem boundaries.
for marker in (
    "ALL_SHARED_EDGE_DIRECTIONS_POSITIVE_POWER=true",
    "GLOBAL_N2_EXPONENT_UPGRADED=false",
    "TRUE_N2_EXPONENT_IDENTIFIED=false",
    "MOVING_FAMILY_UNIFORMITY_PROVED=false",
    "FINITE_DATA_USED_AS_PROOF=false",
    "PERFECT_CUBOID_CONCLUSION=NONE",
):
    assert marker in proof, marker
assert "D20-05" in discovery and "AR-035" in discovery
assert "AR-023/024" in discovery
assert "S25R-W20-01" in weapons and "S25R-W20-02" in weapons
assert "NEW_REUSABLE_WEAPON_PROVED=false" in weapons

for marker in (
    "STAGE25_REENTRY_CURRENT_PHASE=20",
    "STAGE25_REENTRY_ROUTE_R008A=Stage25-um-r008a",
    "STAGE26_ALLOWED=false",
):
    assert marker in status_doc, marker
assert "AUDIT_STATUS=PENDING" in result
assert "ADVANCE_ALLOWED=false" in result
assert "MERGE_ALLOWED=false" in result

print("STAGE25_REENTRY_PHASE20_AUTHORIZATION=PASS")
print("STAGE25_REENTRY_PHASE20_R501_A_CONE_ALGEBRA=PASS")
print("STAGE25_REENTRY_PHASE20_R501_R502_SOURCE_BINDING=PASS")
print("STAGE25_REENTRY_PHASE20_DIRECTIONAL_ADAPTER=PASS")
print("STAGE25_REENTRY_PHASE20_BACKFLOW_QUEUE=PASS")
print("STAGE25_REENTRY_PHASE20_SCOPE_FIREWALL=PASS")
print(f"STAGE25_REENTRY_PHASE20_LIFECYCLE={lifecycle}")
print("STAGE26_GATE=BLOCKED_VALID")
