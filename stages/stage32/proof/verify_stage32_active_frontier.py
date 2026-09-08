#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
BASE_VERIFIER_PATH = HERE / "verify_stage32_claim_dag.py"
BASE_REGISTRY_PATH = HERE / "CLAIM-REGISTRY.json"
ACTIVE_PATH = HERE / "ACTIVE-FRONTIER.json"
ADAPTER_PATH = HERE / "LANE-ADAPTERS.json"
SYNC_CONTRACT_REL = "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
SYNC_CONTRACT_PATH = ROOT / SYNC_CONTRACT_REL

REQUIRED_SYNC_TRIGGERS = {
    "RETAINED_CONSOLIDATION",
    "AUTHORITY_OR_AUDIT_TRANSITION",
    "EX_TO_MAIN_PROMOTION",
    "ACTIVE_FRONTIER_REMAP",
    "FINAL_MILESTONE_TRANSITION",
}
EXPECTED_AUDIT_TRANSITION_POLICY = {
    "pass_before_sync": "KEEP_PRE_SYNC_AUTHORITY_NO_UPGRADE",
    "fail_before_sync": "BLOCK_DOWNSTREAM_IMMEDIATELY",
    "revocation_before_sync": "BLOCK_DOWNSTREAM_IMMEDIATELY",
    "registry_authority_mutation": "AT_CLAIM_SYNC_WITH_EXACT_RECEIPT",
}
REQUIRED_ACTIVE_IDS = {
    "S32.O210.EXCLUSION.V1",
    "S32.Q602.SURVIVORS_73_97_235.V1",
    "S32.Q602.EXCLUSION.V1",
    "S32.FULL178.NUMERICAL_CENSUS.V1",
    "S32.GOAL.STAGE32_CLOSURE.V1",
}
ALLOWED_LANES = {"MAIN", "EX1", "EX2", "EX3", "EX4", "EX5", "EX6"}
ALLOWED_LANE_ROLES = {"OWNER", "ATTACKS", "CONSUMES"}
ALLOWED_FRONTIER_STATUS = {
    "AUDITED_TRUE", "OPEN_GOAL", "OPEN_BRANCH", "BLOCKED_OPEN_GOAL", "ACTIVE_INCOMPLETE"
}
INACTIVE_LANE_STATUSES = {
    "EX1": "COMPLETED_AUDITED_HANDOFF",
    "EX2": "DOMINATED_BY_AUDITED_V6_NONEXISTENCE",
    "EX6": "STOPPED_PENDING_NEW_ENDPOINT_INPUT",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_base_verifier():
    spec = importlib.util.spec_from_file_location("stage32_claim_base", BASE_VERIFIER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load base Stage32 claim verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_sync(adapters: dict) -> None:
    contract = adapters.get("contract", {})
    if contract.get("claim_sync_contract") != SYNC_CONTRACT_REL:
        raise RuntimeError("claim-sync contract path drift")
    if set(contract.get("claim_sync_triggers", [])) != REQUIRED_SYNC_TRIGGERS:
        raise RuntimeError("claim-sync trigger contract drift")
    if contract.get("audit_transition_policy") != EXPECTED_AUDIT_TRANSITION_POLICY:
        raise RuntimeError("audit transition policy drift")
    if contract.get("ordinary_startup_preloads_claim_dag") is not False:
        raise RuntimeError("ordinary startup must not preload claim DAG")
    if contract.get("scratch_only_sync_required") is not False:
        raise RuntimeError("scratch-only work must not require sync")
    text = SYNC_CONTRACT_PATH.read_text(encoding="utf-8")
    for trigger in REQUIRED_SYNC_TRIGGERS:
        if trigger not in text:
            raise RuntimeError(f"sync contract missing {trigger}")


def main() -> int:
    try:
        basev = load_base_verifier()
        base = load_json(BASE_REGISTRY_PATH)
        active = load_json(ACTIVE_PATH)
        adapters = load_json(ADAPTER_PATH)

        if active.get("schema") != "STAGE32_ACTIVE_FRONTIER_CLAIM_REGISTRY_V1":
            raise RuntimeError("active-frontier schema drift")
        if active.get("stage") != 32:
            raise RuntimeError("active-frontier stage drift")
        expected_core = [k for k in basev.CORE_KEYS if k != "bridges"]
        if active.get("claim_core_keys") != expected_core:
            raise RuntimeError("active core-key drift")
        if set(active.get("status_contract", {})) != ALLOWED_FRONTIER_STATUS:
            raise RuntimeError("frontier status-contract drift")

        base_claims = basev.validate_registry_shape(base)
        active_claims = active.get("claims")
        if not isinstance(active_claims, list):
            raise RuntimeError("active claims missing")
        active_ids = {c.get("claim_id") for c in active_claims}
        if active_ids != REQUIRED_ACTIVE_IDS or len(active_ids) != len(active_claims):
            raise RuntimeError(f"post1728 active ID drift: {sorted(active_ids)}")

        base_ids = {c.get("claim_id") for c in base_claims}
        if base_ids & active_ids:
            raise RuntimeError("active/base claim ID collision")

        combined = list(base_claims) + list(active_claims)
        by_id = basev.validate_claims(combined)
        basev.validate_dependencies(by_id)
        replay_count = basev.validate_replay_verifiers(by_id)
        source_count = basev.validate_source_locks(by_id)
        basev.validate_lane_adapters(by_id, adapters)
        validate_sync(adapters)

        lane_to_claims: dict[str, list[str]] = defaultdict(list)
        owner_claims: list[str] = []
        for claim in active_claims:
            cid = claim["claim_id"]
            fs = claim.get("frontier_status")
            if fs not in ALLOWED_FRONTIER_STATUS:
                raise RuntimeError(f"{cid}: bad frontier status")
            blockers = claim.get("blockers")
            if not isinstance(blockers, list):
                raise RuntimeError(f"{cid}: blockers missing")
            if claim["authority_status"] == "AUDITED":
                if fs != "AUDITED_TRUE" or blockers:
                    raise RuntimeError(f"{cid}: audited frontier shape invalid")
            elif not blockers:
                raise RuntimeError(f"{cid}: unresolved active claim requires blocker")
            links = claim.get("lane_links")
            if not isinstance(links, list) or not links:
                raise RuntimeError(f"{cid}: lane links missing")
            owners = 0
            for link in links:
                lane, role = link.get("lane"), link.get("role")
                if lane not in ALLOWED_LANES or role not in ALLOWED_LANE_ROLES:
                    raise RuntimeError(f"{cid}: invalid lane link")
                if lane == "MAIN" and role == "OWNER":
                    owners += 1
                    owner_claims.append(cid)
                if lane.startswith("EX") and role in {"ATTACKS", "CONSUMES"}:
                    lane_to_claims[lane].append(cid)
            if owners != 1:
                raise RuntimeError(f"{cid}: must have exactly one MAIN OWNER")

        lane_items = {x["lane"]: x for x in adapters.get("lanes", [])}
        if set(lane_items) != ALLOWED_LANES:
            raise RuntimeError("lane coverage drift")

        inactive = []
        for lane in sorted(ALLOWED_LANES):
            item = lane_items[lane]
            refs = item.get("active_frontier_refs")
            if not isinstance(refs, list) or len(refs) != len(set(refs)):
                raise RuntimeError(f"{lane}: malformed active refs")
            expected = set(owner_claims) if lane == "MAIN" else set(lane_to_claims[lane])
            if expected:
                if set(refs) != expected:
                    raise RuntimeError(f"{lane}: active refs disagree with frontier")
                if lane in INACTIVE_LANE_STATUSES:
                    raise RuntimeError(f"{lane}: inactive lane unexpectedly has active claims")
                continue

            if lane == "MAIN":
                raise RuntimeError("MAIN cannot have empty frontier")
            wanted = INACTIVE_LANE_STATUSES.get(lane)
            if wanted is None or item.get("lane_status") != wanted:
                raise RuntimeError(f"{lane}: empty frontier lacks exact inactive status")
            if item.get("promotion_blocked_without_active_claim") is not True or refs:
                raise RuntimeError(f"{lane}: inactive lane promotion gate invalid")

            state_rel = item.get("state_path")
            if not isinstance(state_rel, str):
                raise RuntimeError(f"{lane}: inactive lane state_path missing")
            lane_state = load_json(ROOT / state_rel)
            if lane_state.get("current", {}).get("status") != wanted:
                raise RuntimeError(
                    f"{lane}: lane adapter inactive status disagrees with ordinary MAIN-STATE"
                )
            inactive.append(lane)

        if inactive != ["EX1", "EX2", "EX6"]:
            raise RuntimeError(f"inactive-lane set drift: {inactive}")

        survivor = by_id["S32.Q602.SURVIVORS_73_97_235.V1"]
        if survivor["authority_status"] != "AUDITED":
            raise RuntimeError("Q602 survivor authority drift")
        if survivor["scope"].get("surviving_residues") != [73, 97, 235]:
            raise RuntimeError("Q602 survivor set drift")

        v6 = by_id["S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2"]
        if v6["authority_status"] != "AUDITED":
            raise RuntimeError("audited V6-negative authority missing")
        if v6["audit_receipt"].get("review_id") != 5147810198:
            raise RuntimeError("V6-negative audit receipt drift")

        print(json.dumps({
            "verdict": "PASS_STAGE32_POST1728_ACTIVE_FRONTIER_DAG",
            "active_claim_ids": sorted(active_ids),
            "inactive_lanes": inactive,
            "inactive_lane_states_verified": True,
            "v6_negative_consumed": True,
            "q602_excluded": False,
            "o210_excluded": False,
            "source_locks_checked": source_count,
            "replay_verifiers_checked": replay_count,
        }, sort_keys=True))
        return 0
    except Exception as exc:
        print(f"FAIL_STAGE32_POST1728_ACTIVE_FRONTIER_DAG: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
