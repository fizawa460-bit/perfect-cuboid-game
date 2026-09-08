#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
BASE_VERIFIER_PATH = HERE / "verify_stage32_claim_dag.py"
BASE_REGISTRY_PATH = HERE / "CLAIM-REGISTRY.json"
ACTIVE_PATH = HERE / "ACTIVE-FRONTIER.json"
ADAPTER_PATH = HERE / "LANE-ADAPTERS.json"
SYNC_CONTRACT_REL = "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md"
SYNC_CONTRACT_PATH = ROOT / SYNC_CONTRACT_REL
SYNC_TRIGGER_MARKER = "Claim-DAG synchronization trigger"
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
STOPPED_LANE_STATUS = "STOPPED_PENDING_NEW_ENDPOINT_INPUT"

REQUIRED_ACTIVE_IDS = {
    "S32.V6.ACTUAL_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1",
    "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1",
    "S32.V6.SURFACE_NODE_MULTIBRANCH.V3",
    "S32.V6.SMOOTH_AMBIENT_LOCUS_CURVE_SINGULARITY.V2",
    "S32.O210.EXCLUSION.V2",
    "S32.Q602.SURVIVORS_73_97_235.V1",
    "S32.Q602.EXCLUSION.V1",
    "S32.J2.DELTA0INF_ABSOLUTE_W_LINE_MARKING.V1",
    "S32.V6.MEMBER_LEVEL_Q602_LOCAL_IDENTITY.V3",
    "S32.FULL178.NUMERICAL_CENSUS.V1",
    "S32.GOAL.STAGE32_CLOSURE.V1",
}
ALLOWED_LANES = {"MAIN", "EX1", "EX2", "EX3", "EX4", "EX5", "EX6"}
ALLOWED_LANE_ROLES = {"OWNER", "ATTACKS", "CONSUMES"}
ALLOWED_FRONTIER_STATUS = {"AUDITED_TRUE", "OPEN_GOAL", "OPEN_BRANCH", "BLOCKED_OPEN_GOAL", "ACTIVE_INCOMPLETE"}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise RuntimeError(f"invalid JSON {path.relative_to(ROOT)}: {exc}") from exc


def load_base_verifier():
    spec = importlib.util.spec_from_file_location("stage32_claim_base", BASE_VERIFIER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load base Stage32 claim verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def downstream_consumption_allowed_before_sync(pre_sync_authority: str, audit_transition: str) -> bool:
    """Fail-close authority use while an audit transition is known but not yet synchronized."""
    transition = audit_transition.upper()
    if transition in {"FAIL", "REVOCATION", "REVOKED"}:
        return False
    if transition == "PASS":
        return pre_sync_authority == "AUDITED"
    raise RuntimeError(f"unknown audit transition {audit_transition!r}")


def self_test_audit_transition_fail_closed() -> None:
    if downstream_consumption_allowed_before_sync("AUDITED", "FAIL"):
        raise RuntimeError("synthetic regression: known FAIL left old AUDITED claim consumable")
    if downstream_consumption_allowed_before_sync("AUDITED", "REVOCATION"):
        raise RuntimeError("synthetic regression: known revocation left old AUDITED claim consumable")
    if downstream_consumption_allowed_before_sync("PROVISIONAL", "PASS"):
        raise RuntimeError("synthetic regression: PASS upgraded PROVISIONAL authority before sync")
    if not downstream_consumption_allowed_before_sync("AUDITED", "PASS"):
        raise RuntimeError("synthetic regression: PASS incorrectly revoked existing AUDITED authority")


def validate_claim_sync_contract(adapters: dict) -> None:
    contract = adapters.get("contract")
    if not isinstance(contract, dict):
        raise RuntimeError("LANE-ADAPTERS contract missing")
    if contract.get("claim_sync_contract") != SYNC_CONTRACT_REL:
        raise RuntimeError("claim-sync contract path drift")
    if contract.get("ordinary_startup_preloads_claim_dag") is not False:
        raise RuntimeError("ordinary startup must not preload claim DAG")
    if contract.get("scratch_only_sync_required") is not False:
        raise RuntimeError("scratch-only work must not require claim-DAG synchronization")
    triggers = contract.get("claim_sync_triggers")
    if not isinstance(triggers, list) or set(triggers) != REQUIRED_SYNC_TRIGGERS or len(triggers) != len(REQUIRED_SYNC_TRIGGERS):
        raise RuntimeError("claim-sync trigger contract drift")
    if contract.get("audit_transition_policy") != EXPECTED_AUDIT_TRANSITION_POLICY:
        raise RuntimeError("claim-sync audit transition policy drift")
    if not SYNC_CONTRACT_PATH.is_file():
        raise RuntimeError("claim-sync contract file missing")
    sync_text = SYNC_CONTRACT_PATH.read_text()
    for trigger in sorted(REQUIRED_SYNC_TRIGGERS):
        if trigger not in sync_text:
            raise RuntimeError(f"claim-sync contract missing trigger {trigger}")
    if "Scratch-only work does not trigger claim-DAG writes." not in sync_text:
        raise RuntimeError("claim-sync scratch firewall text missing")
    required_audit_text = [
        "downstream consumption of the affected claim is blocked immediately",
        "synchronization latency may delay an authority increase, but it may never delay an authority decrease",
        "PASS receipt by itself does not silently mutate the claim registry",
    ]
    for marker in required_audit_text:
        if marker not in sync_text:
            raise RuntimeError(f"claim-sync audit fail-close text missing: {marker}")
    self_test_audit_transition_fail_closed()

    lanes = adapters.get("lanes")
    if not isinstance(lanes, list):
        raise RuntimeError("lane adapters must be a list")
    lane_names = [item.get("lane") for item in lanes if isinstance(item, dict)]
    if set(lane_names) != ALLOWED_LANES or len(lane_names) != len(ALLOWED_LANES):
        raise RuntimeError("mapped lane coverage drift")
    for item in lanes:
        if not isinstance(item, dict):
            raise RuntimeError("malformed lane adapter")
        lane = item.get("lane")
        startup_rel = item.get("startup_path")
        if lane not in ALLOWED_LANES:
            raise RuntimeError(f"unknown mapped lane {lane!r}")
        if not isinstance(startup_rel, str) or not startup_rel:
            raise RuntimeError(f"{lane}: startup_path missing from lane adapter")
        startup_path = ROOT / startup_rel
        if not startup_path.is_file():
            raise RuntimeError(f"{lane}: startup_path does not exist: {startup_rel}")
        startup_text = startup_path.read_text()
        if SYNC_TRIGGER_MARKER not in startup_text:
            raise RuntimeError(f"{lane}: startup missing claim-sync trigger section")
        if SYNC_CONTRACT_REL not in startup_text:
            raise RuntimeError(f"{lane}: startup does not point to claim-sync contract")
        for trigger in sorted(REQUIRED_SYNC_TRIGGERS):
            if trigger not in startup_text:
                raise RuntimeError(f"{lane}: startup missing claim-sync trigger {trigger}")
        if "Scratch-only diagnostics do not trigger claim-DAG writes." not in startup_text:
            raise RuntimeError(f"{lane}: startup missing scratch-only sync firewall")


def main() -> int:
    try:
        basev = load_base_verifier()
        base = load_json(BASE_REGISTRY_PATH)
        active = load_json(ACTIVE_PATH)
        adapters = load_json(ADAPTER_PATH)

        if active.get("schema") != "STAGE32_ACTIVE_FRONTIER_CLAIM_REGISTRY_V1":
            raise RuntimeError("unexpected active-frontier schema")
        if active.get("stage") != 32:
            raise RuntimeError("active-frontier stage must be 32")
        if active.get("base_registry") != "stages/stage32/proof/CLAIM-REGISTRY.json":
            raise RuntimeError("active-frontier base registry drift")
        if active.get("inherits_claim_schema") != "stages/stage32/proof/CLAIM-REGISTRY.schema.json":
            raise RuntimeError("active-frontier schema inheritance drift")
        expected_active_core_keys = [key for key in basev.CORE_KEYS if key != "bridges"]
        if active.get("claim_core_keys") != expected_active_core_keys:
            raise RuntimeError("active-frontier immutable non-adapter claim core drift")
        status_contract = active.get("status_contract")
        if not isinstance(status_contract, dict) or set(status_contract) != ALLOWED_FRONTIER_STATUS:
            raise RuntimeError("active-frontier status contract drift")

        base_claims = basev.validate_registry_shape(base)
        active_claims = active.get("claims")
        if not isinstance(active_claims, list):
            raise RuntimeError("active-frontier claims must be a list")
        if any(c.get("kind") == "adapter_contract" for c in active_claims):
            raise RuntimeError("adapter_contract must live in base registry so bridges remain immutable")

        base_ids = {c.get("claim_id") for c in base_claims}
        active_ids = {c.get("claim_id") for c in active_claims}
        if len(active_ids) != len(active_claims):
            raise RuntimeError("duplicate active-frontier claim ID")
        if active_ids != REQUIRED_ACTIVE_IDS:
            missing = sorted(REQUIRED_ACTIVE_IDS - active_ids)
            extra = sorted(active_ids - REQUIRED_ACTIVE_IDS)
            raise RuntimeError(f"active-frontier ID coverage drift: missing={missing} extra={extra}")
        overlap = sorted(base_ids & active_ids)
        if overlap:
            raise RuntimeError(f"active-frontier IDs collide with base registry: {overlap}")

        combined_claims = list(base_claims) + list(active_claims)
        by_id = basev.validate_claims(combined_claims)
        basev.validate_dependencies(by_id)
        replay_count = basev.validate_replay_verifiers(by_id)
        source_lock_count = basev.validate_source_locks(by_id)
        basev.validate_lane_adapters(by_id, adapters)
        validate_claim_sync_contract(adapters)

        lane_to_claims: dict[str, list[str]] = defaultdict(list)
        owner_claims: list[str] = []
        for claim in active_claims:
            cid = claim["claim_id"]
            frontier_status = claim.get("frontier_status")
            if frontier_status not in ALLOWED_FRONTIER_STATUS:
                raise RuntimeError(f"{cid}: invalid frontier_status {frontier_status!r}")
            blockers = claim.get("blockers")
            if not isinstance(blockers, list):
                raise RuntimeError(f"{cid}: blockers must be a list")
            if claim["authority_status"] != "AUDITED" and not blockers:
                raise RuntimeError(f"{cid}: non-audited active goal requires explicit blockers")
            if claim["authority_status"] == "AUDITED" and frontier_status != "AUDITED_TRUE":
                raise RuntimeError(f"{cid}: AUDITED active claim must use AUDITED_TRUE frontier status")
            if frontier_status == "AUDITED_TRUE" and claim["authority_status"] != "AUDITED":
                raise RuntimeError(f"{cid}: AUDITED_TRUE cannot coexist with non-AUDITED authority")
            links = claim.get("lane_links")
            if not isinstance(links, list) or not links:
                raise RuntimeError(f"{cid}: lane_links must be nonempty")
            owners = 0
            for link in links:
                if not isinstance(link, dict):
                    raise RuntimeError(f"{cid}: malformed lane link")
                lane = link.get("lane")
                role = link.get("role")
                if lane not in ALLOWED_LANES or role not in ALLOWED_LANE_ROLES:
                    raise RuntimeError(f"{cid}: invalid lane link {link}")
                if lane == "MAIN" and role == "OWNER":
                    owners += 1
                    owner_claims.append(cid)
                if lane.startswith("EX") and role in {"ATTACKS", "CONSUMES"}:
                    lane_to_claims[lane].append(cid)
            if owners != 1:
                raise RuntimeError(f"{cid}: active frontier node requires exactly one MAIN OWNER link")

        adapter_by_lane = {item.get("lane"): item for item in adapters.get("lanes", [])}
        stopped_lanes: list[str] = []
        for lane in sorted(ALLOWED_LANES):
            item = adapter_by_lane.get(lane)
            if not isinstance(item, dict):
                raise RuntimeError(f"{lane}: missing lane adapter")
            refs = item.get("active_frontier_refs")
            if not isinstance(refs, list):
                raise RuntimeError(f"{lane}: active_frontier_refs must be a list")
            if len(refs) != len(set(refs)):
                raise RuntimeError(f"{lane}: duplicate active_frontier_refs")
            unknown = sorted(set(refs) - active_ids)
            if unknown:
                raise RuntimeError(f"{lane}: unknown active frontier refs {unknown}")
            expected = set(owner_claims) if lane == "MAIN" else set(lane_to_claims[lane])

            if lane != "MAIN" and not expected:
                if item.get("lane_status") != STOPPED_LANE_STATUS:
                    raise RuntimeError(f"{lane}: empty active frontier is allowed only for an explicitly stopped lane")
                if item.get("promotion_blocked_without_active_claim") is not True:
                    raise RuntimeError(f"{lane}: stopped lane must block promotion without an active claim")
                if refs:
                    raise RuntimeError(f"{lane}: stopped lane without active attack must have empty active_frontier_refs")
                state_rel = item.get("state_path")
                if not isinstance(state_rel, str) or not state_rel:
                    raise RuntimeError(f"{lane}: stopped lane state_path missing")
                state = load_json(ROOT / state_rel)
                if state.get("current", {}).get("status") != STOPPED_LANE_STATUS:
                    raise RuntimeError(f"{lane}: lane adapter stop status disagrees with MAIN-STATE")
                if state.get("credit", {}).get("stage32_main_credit") is not False:
                    raise RuntimeError(f"{lane}: stopped lane cannot carry Stage32 MAIN credit")
                stopped_lanes.append(lane)
                continue

            if lane != "MAIN" and not expected:
                raise RuntimeError(f"{lane}: not connected to any active frontier claim")
            if set(refs) != expected:
                raise RuntimeError(
                    f"{lane}: LANE-ADAPTERS active refs disagree with claim lane_links; "
                    f"missing={sorted(expected-set(refs))} extra={sorted(set(refs)-expected)}"
                )

        if stopped_lanes != ["EX6"]:
            raise RuntimeError(f"unexpected stopped-lane set: {stopped_lanes}")

        survivor = by_id["S32.Q602.SURVIVORS_73_97_235.V1"]
        if survivor["authority_status"] != "AUDITED" or survivor["scope"].get("surviving_residues") != [73, 97, 235]:
            raise RuntimeError("audited Q602 survivor frontier drift")

        status_counts = Counter(c["authority_status"] for c in active_claims)
        frontier_status_counts = Counter(c["frontier_status"] for c in active_claims)
        print(json.dumps({
            "verdict": "PASS_STAGE32_ACTIVE_FRONTIER_DAG",
            "active_claim_count": len(active_claims),
            "active_claim_ids": sorted(active_ids),
            "active_authority_status_counts": dict(sorted(status_counts.items())),
            "active_frontier_status_counts": dict(sorted(frontier_status_counts.items())),
            "ex_lane_targets": {k: sorted(v) for k, v in sorted(lane_to_claims.items())},
            "stopped_lanes_without_active_claim": stopped_lanes,
            "combined_claim_count": len(combined_claims),
            "source_locks_checked": source_lock_count,
            "replay_verifiers_checked": replay_count,
            "claim_sync_contract": SYNC_CONTRACT_REL,
            "claim_sync_triggers": sorted(REQUIRED_SYNC_TRIGGERS),
            "audit_transition_policy": EXPECTED_AUDIT_TRANSITION_POLICY,
            "audit_transition_fail_closed_regression": True,
            "ordinary_startup_preloads_claim_dag": False,
            "scratch_only_sync_required": False,
            "historical_bulk_migration": False,
            "hostile_audit_credit_self_assigned": False,
        }, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"verdict":"FAIL_STAGE32_ACTIVE_FRONTIER_DAG","error":str(exc)}, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())