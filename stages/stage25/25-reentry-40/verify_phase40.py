#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[3]
def text(rel):
    p=ROOT/rel; assert p.exists(), rel; return p.read_text(encoding="utf-8")
def data(rel): return json.loads(text(rel))

result=text("stages/stage25/25-reentry-40/result.md")
registry=data("stages/stage25/25-reentry-40/mechanism-registry.json")
backflow=data("stages/stage25/25-reentry-40/backflow-proposals.json")
controller=data("stages/stage25/25-reentry-controller.json")
stage22=text("stages/stage22/22-70/result.md")
stage24=text("stages/stage24/final.md")
stage20=text("stages/stage20/final.md")
r009audit=text("stages/stage25/25-reentry-r009a/audit.md")

# Immutable mathematical authorization.
assert "AUDIT_VERDICT=PASS" in r009audit
assert registry["authorization"]["r009a_pr"]==1006
assert registry["authorization"]["r009a_merge_commit"]=="4eb3349ee8ec02dcabb71bd1be3a48234356606b"

# Exact truth table.
for ia in (0,1):
    for ib in (0,1):
        for ic in (0,1):
            faces=ia+ib+ic
            triple=int(faces==3)
            pa,pb,pc=ia*ib,ia*ic,ib*ic
            m2a=int(faces==2 and ia and ib)
            m2b=int(faces==2 and ia and ic)
            m2c=int(faces==2 and ib and ic)
            assert pa==m2a+triple
            assert pb==m2b+triple
            assert pc==m2c+triple

# Frozen asymptotic interfaces.
assert "SOURCE_ASYMPTOTIC=M1(B) ~ 3/(4*pi^2) B^2 log B" in stage22
assert "DIRECTIONAL_THEOREM=M2,j(B)~C_j B(log B)^5 for j=a,b,c with C_j>0" in stage24
assert "M_3(B)\\ll_\\eta B(\\log B)^{5-\\eta}" in stage20
assert "eta<1/46" in stage20

M2j=(Fraction(1),Fraction(5)); M1=(Fraction(2),Fraction(1)); M3upper=(Fraction(1),Fraction(5))
assert (M2j[0]-M1[0],M2j[1]-M1[1])==(Fraction(-1),Fraction(4))
assert M3upper[0]-M2j[0]==0
assert "M3(B)/M2,j(B) <<_{j,eta} (log B)^(-eta) -> 0" in result
assert "M2,j(B)/P_j(B) = 1-O_{j,eta}((log B)^(-eta)) -> 1" in result
assert "M2,j(B)/M1(B) ~ (4*pi^2*C_j/3) (log B)^4/B -> 0" in result
assert "C_M2=C_a+C_b+C_c" in result

for marker in (
    "FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false",
    "FINE_MECHANISM_OPEN=true",
    "TRUE_M3_EXPONENT_IDENTIFIED=false",
    "PERFECT_CUBOID_CONCLUSION=NONE",
    "FINITE_DATA_USED_AS_PROOF=false",
): assert marker in result, marker

# Immutable submission proposal plus lifecycle-aware controller checks.
assert backflow["status"]=="QUEUED_PENDING_PARENT_AUDIT"
assert backflow["queued_derived_routes"]==["Stage25-um-r010a"]
assert backflow["proposals"][0]["affected_stages"]==[18,20,22]
assert controller["phases"]["40"]["task_id"]=="Stage25-u22-r004a"
assert controller["stage26_gate"]["stage26_allowed"] is False

if controller["current_phase"]==40:
    if controller["status"]=="PHASE40_SUBMITTED_PENDING_FRESH_AUDIT":
        p40=controller["phase40_submission"]
        assert p40["audit_status"]=="PENDING"
        assert p40["advance_allowed"] is False
        assert p40["merge_allowed"] is False
        assert controller["phases"]["50"]["status"]=="BLOCKED_UNTIL_PHASE40_BACKFLOW"
        assert controller["next_expected_command"]=="Stage25-reentry-audit"
    else:
        assert controller["status"].startswith("PHASE40_")
else:
    # Post-phase40 lifecycle: the theorem remains immutable and both parent and backflow must be audited+merged.
    assert controller["current_phase"]>=50
    p40=controller["phase40_submission"]
    assert p40["audit_status"]=="PASS"
    assert p40["stronger_result_proved"] is True
    assert p40["pr"]==1007
    assert p40["merge_commit"]=="eebe4cd59caef804be76508f3773f2af6c7d47f2"
    assert controller["phases"]["40"]["status"]=="AUDITED_PASS_MERGED_BACKFLOW_AUDITED_PASS_MERGED"
    r10=controller["r010a_submission"]
    assert r10["audit_status"]=="PASS"
    assert r10["status"]=="AUDITED_PASS_MERGED"
    assert r10["pr"]==1008
    assert r10["merge_commit"]=="9d2e767697a33195e756af6b366cb6f0548494d3"
    q=[x for x in controller["propagation_queue"] if x["route_id"]=="Stage25-um-r010a"]
    assert len(q)==1
    assert q[0]["status"]=="AUDITED_PASS_MERGED"
    assert q[0]["blocks_next_phase"] is False

print("STAGE25_REENTRY_PHASE40_AUTHORIZATION=PASS")
print("STAGE25_REENTRY_PHASE40_EXACT_MASK=PASS")
print("STAGE25_REENTRY_PHASE40_DIRECTIONAL_ASYMPTOTICS=PASS")
print("STAGE25_REENTRY_PHASE40_STAGE20_RECEIVER=PASS")
print("STAGE25_REENTRY_PHASE40_FINE_MECHANISM_FIREWALL=PASS")
print("STAGE25_REENTRY_PHASE40_LIFECYCLE=PASS")
print("STAGE26_GATE=BLOCKED_VALID")
