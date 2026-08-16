#!/usr/bin/env python3
from __future__ import annotations

import hashlib
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


registry = data("stages/stage25/25-reentry-10/interface-registry.json")
backflow = data("stages/stage25/25-reentry-10/backflow-proposals.json")
reentry = data("stages/stage25/25-reentry-controller.json")
result = text("stages/stage25/25-reentry-10/result.md")
discovery = text("stages/stage25/25-reentry-10/discovery-ledger.md")
weapons = text("stages/stage25/25-reentry-10/weapon-delta.md")
status_doc = text("docs/00_CURRENT_RESEARCH_STATUS.md")
audit = text("stages/stage25/25-reentry-10/audit.md")

# Immutable phase10 artifact contract.
assert registry["task_id"] == "Stage25-um-r001a"
assert registry["phase"] == 10
assert registry["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
assert registry["merge_evidence"]["stage25_closeout_pr_1000"] == reentry["unlock_evidence"]["closeout_merge_commit"]
assert registry["merge_evidence"]["stage25_reentry_unlock_pr_1001"] == "549b080aaa614eaf4de8603dc453dc4ce5ec2d19"
assert reentry["stage26_gate"]["stage26_allowed"] is False

# Lifecycle-aware phase10 state: submission is historical after audit+merge.
p10 = reentry["phase10_submission"]
assert p10["task_id"] == "Stage25-um-r001a"
if reentry["current_phase"] == 10:
    assert reentry["status"] in (
        "PHASE10_SUBMITTED_PENDING_FRESH_AUDIT",
        "PHASE10_AUDITED_PASS_AWAITING_MERGE",
    )
    if p10["audit_status"] == "PENDING":
        assert p10["advance_allowed"] is False
        assert p10["merge_allowed"] is False
    else:
        assert p10["audit_status"] == "PASS"
else:
    assert reentry["current_phase"] in (20, 30, 40, 50, 60, 70)
    assert reentry["phases"]["10"]["status"] == "AUDITED_PASS_MERGED"
    assert p10["status"] == "AUDITED_PASS_MERGED"
    assert p10["audit_status"] == "PASS"
    assert p10["pr"] == 1002
    assert p10["merge_commit"] == "5cb7dc8792faf575c1e21fce8166f094af6d7b14"
    assert "AUDIT_VERDICT=PASS" in audit
    assert "PR=1002" in audit
    assert "STAGE25_REENTRY_PHASE10_STATUS=AUDITED_PASS_MERGED" in status_doc

# Every baseline controller was audited at checkpoint70; historical submission
# strings are not allowed to override the phase10 normalized interface registry.
controller_paths = {
    "Stage16": "stages/stage16/16-controller.json",
    "Stage16S": "stages/stage16s/16s-controller.json",
    "Stage17": "stages/stage17/17-controller.json",
    "Stage18": "stages/stage18/18-controller.json",
    "Stage19": "stages/stage19/19-controller.json",
    "Stage20": "stages/stage20/20-controller.json",
    "Stage21": "stages/stage21/21-controller.json",
    "Stage22": "stages/stage22/22-controller.json",
    "Stage23": "stages/stage23/23-controller.json",
    "Stage24": "stages/stage24/24-controller.json",
    "Stage25": "stages/stage25/25-controller.json",
}
for stage, path in controller_paths.items():
    controller = data(path)
    last = controller.get("last_audit") or controller.get("historical_last_audit", {})
    assert last.get("verdict") == "PASS", (stage, last)
    if "checkpoint_status" in controller:
        assert "PASS" in controller["checkpoint_status"]["70"], stage
    else:
        assert controller.get("current_checkpoint") == 70, stage

assert data("stages/stage25/25-controller.json")["status"] == "CLOSED"
assert "AUDIT_VERDICT=PASS" in text("stages/stage25/25-70/audit.md")

# Strongest interfaces and post-Stage25 supersession frozen by phase10.
pop = registry["population_interfaces"]
assert pop["Stage16"]["strongest_audited_interface"].startswith("M1(B)~3/")
assert "(log(B))^3" in pop["Stage17"]["strongest_audited_interface"]
assert "(log(B))^5" in pop["Stage18"]["strongest_audited_interface"]
assert pop["Stage19"]["strongest_audited_interface"] == "B^(1/4)<<N2(B)<<_epsilon B^(1/2+epsilon)"
assert pop["Stage20"]["strongest_audited_interface"] == "B^(1/6)<<M3(B)<<B*(log(B))^(5-1/50)"
assert "N_2(B)\\gg B^{1/4}" in text("stages/stage19/post-stage25-50-supersession.md")
assert "N_2(B)\\gg B^{1/4}" in text("stages/stage23/post-stage25-r01/result.md")
assert "N_2(B)\\gg B^{1/4}" in text("stages/stage24/post-stage25-r01/result.md")

# Exponent/log algebra.
M1 = (Fraction(2), Fraction(1))
N1 = (Fraction(1), Fraction(3))
M2 = (Fraction(1), Fraction(5))
N2_lo = (Fraction(1, 4), Fraction(0))
N2_hi = (Fraction(1, 2), Fraction(0))

def quotient(a, b):
    return (a[0] - b[0], a[1] - b[1])

assert quotient(N1, M1) == (Fraction(-1), Fraction(2))
assert quotient(M2, M1) == (Fraction(-1), Fraction(4))
assert quotient(N2_lo, N1) == (Fraction(-3, 4), Fraction(-3))
assert quotient(N2_hi, N1) == (Fraction(-1, 2), Fraction(-3))
assert quotient(N2_lo, M2) == (Fraction(-3, 4), Fraction(-5))
assert quotient(N2_hi, M2) == (Fraction(-1, 2), Fraction(-5))
assert quotient(N2_lo, M1) == (Fraction(-7, 4), Fraction(-1))
assert quotient(N2_hi, M1) == (Fraction(-3, 2), Fraction(-1))
cross = (N2_lo[0] + M1[0] - M2[0] - N1[0], N2_lo[1] + M1[1] - M2[1] - N1[1])
assert cross == (Fraction(1, 4), Fraction(-7))

# Receiver mutations remain the audited phase10 set and are non-theorem-changing.
mutations = registry["receiver_mutations"]
assert set(mutations) == {"R10-M01", "R10-M02", "R10-M03"}
assert all(not item["theorem_changed"] for item in mutations.values())
assert mutations["R10-M02"]["population_match"] == "EXACT"
assert mutations["R10-M03"]["population_match"] == "ADAPTER_REQUIRED_IN_PHASE60"
assert "FRESH_COMPATIBLE_RECEIVER_MUTATION=R10-M01,R10-M02,R10-M03" in result
assert "NEW_MATHEMATICAL_WEAPON_PROVED=false" in weapons

# Complete sharded attack ledger and curated terminal-route review stay bound.
manifest = data("docs/stage14-15-bound-attack-ledger/manifest.json")
assert manifest["total_records"] == 824
records = 0
for part in manifest["parts"]:
    raw = (ROOT / part["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == part["sha256"]
    rows = [line for line in raw.decode("utf-8").splitlines() if line]
    assert len(rows) == part["records"]
    records += len(rows)
assert records == 824
queue = data("docs/stage14-15-bound-deep-review-queue.json")
assert [item["id"] for item in queue["clusters"]] == [f"Q{i:02d}" for i in range(1, 12)]
for attack in (
    "S1415-ATTACK-0217", "S1415-ATTACK-0224", "S1415-ATTACK-0261",
    "S1415-ATTACK-0748", "S1415-ATTACK-0794", "S1415-ATTACK-0818",
    "S1415-ATTACK-0819", "S1415-ATTACK-0820",
):
    assert attack in discovery
assert "P3_EXHAUSTED_INTERNAL" in discovery
assert "DISCOVERY_LEDGER_STATUS=COMPLETE" in discovery
assert "STRONGEST_KNOWN_CHECK=PASS" in discovery

# Phase10 backflow itself was metadata-only; later phases may have their own queue.
assert len(backflow["proposals"]) == 2
assert {p["action"] for p in backflow["proposals"]} == {"APPLY_NOW"}
assert all(not p["theorem_changing"] for p in backflow["proposals"])
assert backflow["derived_routes_opened"] == []
assert backflow["queued_propagation_proposals"] == []
assert backflow["live_derived_routes"] == []
assert backflow["stage26_allowed"] is False

assert "PERFECT_CUBOID_CONCLUSION=NONE" in result
assert registry["scope_firewall"]["perfect_cuboid_existence_proved"] is False
assert registry["scope_firewall"]["perfect_cuboid_nonexistence_proved"] is False

print("STAGE25_REENTRY_PHASE10_AUTHORIZATION=PASS")
print("STAGE25_REENTRY_PHASE10_INTERFACE_FREEZE=PASS")
print("STAGE25_REENTRY_PHASE10_EXPONENT_ALGEBRA=PASS")
print("STAGE25_REENTRY_PHASE10_RECEIVER_MUTATIONS=PASS")
print("STAGE25_REENTRY_PHASE10_REUSE_PREFLIGHT=PASS")
print("STAGE25_REENTRY_PHASE10_HISTORICAL_BACKFLOW=PASS")
print(f"STAGE25_REENTRY_PHASE10_LIFECYCLE_CURRENT_PHASE={reentry['current_phase']}")
print("STAGE26_GATE=BLOCKED_VALID")
