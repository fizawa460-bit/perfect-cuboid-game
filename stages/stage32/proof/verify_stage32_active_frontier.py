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

REQUIRED_ACTIVE_IDS = {
    "S32.V6.ACTUAL_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1",
    "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1",
    "S32.V6.SURFACE_NODE_MULTIBRANCH.V1",
    "S32.V6.SMOOTH_AMBIENT_LOCUS_CURVE_SINGULARITY.V1",
    "S32.O210.EXCLUSION.V1",
    "S32.Q602.SURVIVORS_73_97_235.V1",
    "S32.Q602.EXCLUSION.V1",
    "S32.J2.DELTA0INF_ABSOLUTE_W_LINE_MARKING.V1",
    "S32.V6.MEMBER_LEVEL_Q602_LOCAL_IDENTITY.V1",
    "S32.FULL178.NUMERICAL_CENSUS.V1",
    "S32.GOAL.STAGE32_CLOSURE.V1",
}
ALLOWED_LANES = {"MAIN", "EX1", "EX2", "EX3", "EX4", "EX5"}
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
        if active.get("claim_core_keys") != basev.CORE_KEYS:
            raise RuntimeError("active-frontier immutable claim core drift")
        status_contract = active.get("status_contract")
        if not isinstance(status_contract, dict) or set(status_contract) != ALLOWED_FRONTIER_STATUS:
            raise RuntimeError("active-frontier status contract drift")

        base_claims = basev.validate_registry_shape(base)
        active_claims = active.get("claims")
        if not isinstance(active_claims, list):
            raise RuntimeError("active-frontier claims must be a list")

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

        for lane in sorted(ALLOWED_LANES - {"MAIN"}):
            if not lane_to_claims.get(lane):
                raise RuntimeError(f"{lane}: not connected to any active frontier claim")

        adapter_by_lane = {item.get("lane"): item for item in adapters.get("lanes", [])}
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
            if set(refs) != expected:
                raise RuntimeError(
                    f"{lane}: LANE-ADAPTERS active refs disagree with claim lane_links; "
                    f"missing={sorted(expected-set(refs))} extra={sorted(set(refs)-expected)}"
                )

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
            "combined_claim_count": len(combined_claims),
            "source_locks_checked": source_lock_count,
            "replay_verifiers_checked": replay_count,
            "historical_bulk_migration": False,
            "hostile_audit_credit_self_assigned": False,
        }, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"verdict":"FAIL_STAGE32_ACTIVE_FRONTIER_DAG","error":str(exc)}, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
