#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
POLICY_REL = "docs/research-os/policies/hostile-audit-and-freshness.md"
POLICY = ROOT / POLICY_REL
AGENTS = ROOT / "AGENTS.md"
SYNC_REL = "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
SYNC = ROOT / SYNC_REL


class CheckError(RuntimeError):
    pass


def read_required(path: Path) -> str:
    if not path.is_file():
        raise CheckError(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text()


def require(text: str, marker: str, label: str) -> None:
    if marker not in text:
        raise CheckError(f"{label} missing required marker: {marker}")


def main() -> int:
    try:
        policy = read_required(POLICY)
        agents = read_required(AGENTS)
        sync = read_required(SYNC)

        for marker in [
            "HOSTILE AUDIT: PASS",
            "MERGE-READY FRESHNESS: PENDING — unrelated main drift",
            "behind > 0",
            "Hostile audit PASS is not merge authorization.",
            "Stage-local controller/state/audit contracts may impose additional checks",
            "HOSTILE AUDIT\n!= STAGE-LOCAL AUTHORITY / CLAIM SYNCHRONIZATION\n!= MERGE-READY FRESHNESS\n!= MERGE AUTHORIZATION",
            "This policy grants no mathematical theorem credit",
        ]:
            require(policy, marker, POLICY_REL)

        require(agents, POLICY_REL, "AGENTS.md")
        require(agents, "hostile audit", "AGENTS.md")
        require(agents, "freshness", "AGENTS.md")

        for marker in [
            POLICY_REL,
            "`HOSTILE AUDIT`",
            "`CLAIM-DAG SYNC`",
            "`MERGE-READY FRESHNESS`",
            "PASS cannot upgrade consumable authority before synchronization.",
            "A PASS receipt by itself does not silently mutate the claim registry",
            "downstream consumption of the affected claim is blocked immediately",
            "synchronization latency may delay an authority increase, but it may never delay an authority decrease",
            "`EX_TO_MAIN_PROMOTION`",
        ]:
            require(sync, marker, SYNC_REL)

        print(json.dumps({
            "verdict": "PASS_HOSTILE_AUDIT_FRESHNESS_POLICY_INTEGRITY",
            "common_policy": POLICY_REL,
            "agents_on_demand_reference": True,
            "stage32_claim_sync_reference": True,
            "hostile_audit_distinct_from_claim_sync": True,
            "hostile_audit_distinct_from_merge_ready_freshness": True,
            "pass_cannot_upgrade_consumable_authority_before_sync": True,
            "mathematical_credit_granted": False,
            "merge_authorized": False,
        }, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({
            "verdict": "FAIL_HOSTILE_AUDIT_FRESHNESS_POLICY_INTEGRITY",
            "error": str(exc),
        }, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
