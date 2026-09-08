#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
REGISTRY_PATH = HERE / "CLAIM-REGISTRY.json"
SCHEMA_PATH = HERE / "CLAIM-REGISTRY.schema.json"
ADAPTER_PATH = HERE / "LANE-ADAPTERS.json"
FINAL_PATH = ROOT / "stages/stage32/FINAL-CHECK.json"

CLAIM_ID_RE = re.compile(r"^S32\.[A-Z0-9_]+(?:\.[A-Z0-9_]+)*\.V[1-9][0-9]*$")
SCOPE_KEY_RE = re.compile(r"^S32\.[A-Z0-9_]+(?:\.[A-Z0-9_]+)*$")
HEX40_RE = re.compile(r"^[0-9a-f]{40}$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
HEXHEAD_RE = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_STATUS = {"SCRATCH", "PROVISIONAL", "AUDITED", "DECLARED_GOAL", "SUPERSEDED", "REVOKED"}
ALLOWED_KIND = {"authority_snapshot", "mathematical_claim", "lane_contract", "adapter_contract"}
STRUCTURAL_CONTEXT_DECLARED_GOAL_KINDS = {"authority_snapshot", "lane_contract"}

EXPECTED_FINAL_MILESTONES = [
    {"slot": "32-01 numerical census", "required_claim_id": "S32.PROOF.NUMERICAL_CENSUS.V1", "required_authority_status": "AUDITED"},
    {"slot": "32-02 effectivity/carrier disposal", "required_claim_id": "S32.PROOF.EFFECTIVITY_DISPOSAL.V1", "required_authority_status": "AUDITED"},
    {"slot": "32-03 multibranch ledger", "required_claim_id": "S32.PROOF.MULTIBRANCH_LEDGER.V1", "required_authority_status": "AUDITED"},
    {"slot": "32-04 integrated synthesis", "required_claim_id": "S32.PROOF.INTEGRATED_SYNTHESIS.V1", "required_authority_status": "AUDITED"},
    {"slot": "32-05 hostile-audit release", "required_claim_id": "S32.PROOF.HOSTILE_AUDIT_RELEASE.V1", "required_authority_status": "AUDITED"},
    {"slot": "Stage32 closed", "required_claim_id": "S32.PROOF.STAGE32_CLOSED.V1", "required_authority_status": "AUDITED"},
]
EXPECTED_FINAL_ROOT_ID = "S32.PROOF.STAGE32_CLOSED.V1"
EXPECTED_FINAL_REQUIRED_PROVES = ["STAGE32_CLOSED=true"]
EXPECTED_FINAL_FORBIDDEN_PROVES = [
    "PERFECT_CUBOID_EXISTENCE_CLAIM=true",
    "PERFECT_CUBOID_NONEXISTENCE_CLAIM=true",
]
EXPECTED_FINAL_TRUE_FLAGS = {
    "hostile_audit_receipt_required",
    "all_transitive_mathematical_dependencies_must_be_audited",
    "source_locks_must_match_working_tree",
    "missing_reserved_claim_is_not_ready_not_success",
    "declared_goal_does_not_substitute_for_audited_final_claim",
    "required_milestones_must_be_transitive_dependencies_of_final_root",
}

CORE_KEYS = [
    "claim_id",
    "kind",
    "statement",
    "scope_key",
    "scope",
    "proves",
    "does_not_prove",
    "requires",
    "bridges",
    "source_locks",
    "replay_verifier",
]


class CheckError(RuntimeError):
    pass


def load_json(path: Path) -> object:
    if not path.exists():
        raise CheckError(f"missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise CheckError(f"invalid JSON {path.relative_to(ROOT)}: {exc}") from exc


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    prefix = f"blob {len(data)}\0".encode()
    return hashlib.sha1(prefix + data).hexdigest()


def claim_core_sha(claim: dict) -> str:
    return csha({key: claim[key] for key in CORE_KEYS if key in claim})


def validate_registry_shape(registry: dict) -> list[dict]:
    if registry.get("schema") != "STAGE32_CLAIM_REGISTRY_V1":
        raise CheckError("unexpected registry schema")
    if registry.get("stage") != 32:
        raise CheckError("registry stage must be 32")
    contract = registry.get("claim_id_contract", {})
    if contract.get("pattern") != r"^S32\.[A-Z0-9_]+(?:\.[A-Z0-9_]+)*\.V[1-9][0-9]*$":
        raise CheckError("claim ID pattern contract drift")
    statuses = registry.get("authority_status_contract", {}).get("allowed")
    if set(statuses or []) != ALLOWED_STATUS:
        raise CheckError("authority status contract drift")
    claims = registry.get("claims")
    if not isinstance(claims, list):
        raise CheckError("claims must be a list")
    return claims


def validate_final_contract(final: dict) -> None:
    if final.get("schema") != "STAGE32_FINAL_CHECK_V1":
        raise CheckError("unexpected FINAL-CHECK schema")
    if final.get("stage") != 32:
        raise CheckError("FINAL-CHECK stage must be 32")
    if final.get("mode") != "FAIL_CLOSED_FOR_STAGE32_CLOSURE":
        raise CheckError("FINAL-CHECK mode drift")
    if final.get("required_milestones") != EXPECTED_FINAL_MILESTONES:
        raise CheckError("FINAL-CHECK reserved milestone contract drift")
    contract = final.get("closure_contract")
    if not isinstance(contract, dict):
        raise CheckError("FINAL-CHECK closure_contract must be object")
    if contract.get("required_final_claim_id") != EXPECTED_FINAL_ROOT_ID:
        raise CheckError("FINAL-CHECK final root ID drift")
    if contract.get("required_proves_tokens") != EXPECTED_FINAL_REQUIRED_PROVES:
        raise CheckError("FINAL-CHECK required PROVES token contract drift")
    if contract.get("forbidden_proves_tokens") != EXPECTED_FINAL_FORBIDDEN_PROVES:
        raise CheckError("FINAL-CHECK forbidden PROVES token contract drift")
    for key in sorted(EXPECTED_FINAL_TRUE_FLAGS):
        if contract.get(key) is not True:
            raise CheckError(f"FINAL-CHECK safety flag must remain true: {key}")


def validate_bridge_shape(cid: str, bridge: object) -> None:
    if not isinstance(bridge, dict):
        raise CheckError(f"{cid}: adapter_contract requires bridges object")
    for key in ("from_scope_key", "to_scope_key"):
        value = bridge.get(key)
        if not isinstance(value, str) or not SCOPE_KEY_RE.fullmatch(value):
            raise CheckError(f"{cid}: bridges.{key} must be a valid scope_key")


def validate_claims(claims: list[dict]) -> dict[str, dict]:
    by_id: dict[str, dict] = {}
    for claim in claims:
        for key in ("claim_id","kind","statement","scope_key","scope","proves","does_not_prove","requires","claim_core_sha256","authority_status","source_locks","audit_receipt"):
            if key not in claim:
                raise CheckError(f"claim missing {key}: {claim.get('claim_id')}")
        cid = claim["claim_id"]
        if not isinstance(cid, str) or not CLAIM_ID_RE.fullmatch(cid):
            raise CheckError(f"invalid claim ID: {cid!r}")
        if cid in by_id:
            raise CheckError(f"duplicate claim ID: {cid}")
        if claim["kind"] not in ALLOWED_KIND:
            raise CheckError(f"{cid}: invalid kind {claim['kind']}")
        if claim["kind"] == "adapter_contract":
            validate_bridge_shape(cid, claim.get("bridges"))
        elif "bridges" in claim:
            raise CheckError(f"{cid}: only adapter_contract may declare bridges")
        if not isinstance(claim["scope_key"], str) or not SCOPE_KEY_RE.fullmatch(claim["scope_key"]):
            raise CheckError(f"{cid}: invalid scope_key")
        if not isinstance(claim["statement"], str) or not claim["statement"].strip():
            raise CheckError(f"{cid}: empty statement")
        if not isinstance(claim["scope"], dict):
            raise CheckError(f"{cid}: scope must be object")
        for key in ("proves", "does_not_prove", "requires", "source_locks"):
            if not isinstance(claim[key], list):
                raise CheckError(f"{cid}: {key} must be list")
        if not claim["proves"]:
            raise CheckError(f"{cid}: PROVES must be nonempty")
        if not claim["does_not_prove"]:
            raise CheckError(f"{cid}: DOES_NOT_PROVE must be nonempty")
        if len(set(claim["requires"])) != len(claim["requires"]):
            raise CheckError(f"{cid}: duplicate dependencies")
        status = claim["authority_status"]
        if status not in ALLOWED_STATUS:
            raise CheckError(f"{cid}: invalid authority status {status}")
        expected = claim_core_sha(claim)
        actual = claim["claim_core_sha256"]
        if not isinstance(actual, str) or not HEX64_RE.fullmatch(actual):
            raise CheckError(f"{cid}: invalid claim_core_sha256")
        if actual != expected:
            raise CheckError(f"{cid}: immutable claim core hash mismatch")
        receipt = claim["audit_receipt"]
        if status == "AUDITED":
            if not isinstance(receipt, dict) or receipt.get("status") != "PASS":
                raise CheckError(f"{cid}: AUDITED requires PASS audit receipt")
            if not isinstance(receipt.get("pr"), int):
                raise CheckError(f"{cid}: AUDITED receipt requires PR number")
            if not isinstance(receipt.get("review_id"), int):
                raise CheckError(f"{cid}: AUDITED receipt requires review_id")
            if not isinstance(receipt.get("exact_head"), str) or not HEXHEAD_RE.fullmatch(receipt["exact_head"]):
                raise CheckError(f"{cid}: AUDITED receipt requires 40-hex exact_head")
        elif isinstance(receipt, dict) and receipt.get("status") == "PASS":
            raise CheckError(f"{cid}: PASS receipt cannot coexist with non-AUDITED status")
        by_id[cid] = claim
    return by_id


def validate_dependencies(by_id: dict[str, dict]) -> None:
    for cid, claim in by_id.items():
        for dep_id in claim["requires"]:
            if dep_id not in by_id:
                raise CheckError(f"{cid}: dangling dependency {dep_id}")
            dep = by_id[dep_id]
            dep_status = dep["authority_status"]
            if dep_status == "REVOKED":
                raise CheckError(f"{cid}: dependency is REVOKED: {dep_id}")
            if claim["authority_status"] != "SCRATCH" and dep_status == "SCRATCH":
                raise CheckError(f"{cid}: non-SCRATCH claim depends on SCRATCH {dep_id}")
            if claim["authority_status"] == "PROVISIONAL" and dep_status not in {"AUDITED", "PROVISIONAL", "DECLARED_GOAL"}:
                raise CheckError(f"{cid}: illegal PROVISIONAL dependency status on {dep_id}")
            if claim["authority_status"] == "AUDITED":
                if dep_status == "AUDITED":
                    pass
                elif dep_status == "DECLARED_GOAL" and dep["kind"] in STRUCTURAL_CONTEXT_DECLARED_GOAL_KINDS:
                    pass
                elif dep_status == "DECLARED_GOAL" and dep["kind"] == "mathematical_claim":
                    raise CheckError(f"{cid}: AUDITED claim depends on unresolved mathematical DECLARED_GOAL {dep_id}")
                else:
                    raise CheckError(f"{cid}: AUDITED claim depends on non-audited proof input {dep_id}")
            if claim["kind"] == "mathematical_claim" and dep["kind"] == "mathematical_claim" and claim["scope_key"] != dep["scope_key"]:
                acceptable = []
                for adapter_id in claim["requires"]:
                    adapter = by_id.get(adapter_id)
                    if not adapter or adapter["kind"] != "adapter_contract":
                        continue
                    bridge = adapter["bridges"]
                    if bridge["from_scope_key"] != dep["scope_key"] or bridge["to_scope_key"] != claim["scope_key"]:
                        continue
                    if claim["authority_status"] == "AUDITED" and adapter["authority_status"] != "AUDITED":
                        continue
                    if claim["authority_status"] == "PROVISIONAL" and adapter["authority_status"] not in {"AUDITED", "PROVISIONAL"}:
                        continue
                    acceptable.append(adapter_id)
                if not acceptable:
                    raise CheckError(f"{cid}: cross-scope mathematical dependency {dep_id} requires explicit adapter_contract")

    color: dict[str, int] = {cid: 0 for cid in by_id}
    stack: list[str] = []
    def visit(cid: str) -> None:
        color[cid] = 1
        stack.append(cid)
        for dep in by_id[cid]["requires"]:
            if color[dep] == 1:
                raise CheckError("claim dependency cycle: " + " -> ".join(stack + [dep]))
            if color[dep] == 0:
                visit(dep)
        stack.pop()
        color[cid] = 2
    for cid in by_id:
        if color[cid] == 0:
            visit(cid)


def validate_replay_verifiers(by_id: dict[str, dict]) -> int:
    checked = 0
    for cid, claim in by_id.items():
        replay = claim.get("replay_verifier")
        if replay is None:
            continue
        if not isinstance(replay, str) or not replay:
            raise CheckError(f"{cid}: malformed replay_verifier")
        path = ROOT / replay
        if not path.exists() or not path.is_file():
            raise CheckError(f"{cid}: missing replay_verifier {replay}")
        checked += 1
    return checked


def validate_source_locks(by_id: dict[str, dict]) -> int:
    checked = 0
    for cid, claim in by_id.items():
        for lock in claim["source_locks"]:
            if not isinstance(lock, dict) or not isinstance(lock.get("path"), str):
                raise CheckError(f"{cid}: malformed source lock")
            path = ROOT / lock["path"]
            if not path.exists() or not path.is_file():
                raise CheckError(f"{cid}: missing source lock {lock['path']}")
            data = path.read_bytes()
            if "blob_sha1" in lock:
                expected = lock["blob_sha1"]
                if not isinstance(expected, str) or not HEX40_RE.fullmatch(expected):
                    raise CheckError(f"{cid}: malformed blob_sha1 for {lock['path']}")
                actual = git_blob_sha1(data)
                if actual != expected:
                    raise CheckError(f"{cid}: blob source-lock mismatch for {lock['path']}: {actual} != {expected}")
            if "canonical_sha256" in lock:
                expected = lock["canonical_sha256"]
                if not isinstance(expected, str) or not HEX64_RE.fullmatch(expected):
                    raise CheckError(f"{cid}: malformed canonical_sha256 for {lock['path']}")
                try:
                    obj = json.loads(data)
                except Exception as exc:
                    raise CheckError(f"{cid}: canonical lock requires JSON: {lock['path']}") from exc
                stored = obj.get("canonical_sha256_without_this_field")
                if stored != expected:
                    raise CheckError(f"{cid}: stored canonical digest mismatch for {lock['path']}: {stored} != {expected}")
                stripped = dict(obj)
                stripped.pop("canonical_sha256_without_this_field", None)
                actual = csha(stripped)
                if actual != expected:
                    raise CheckError(f"{cid}: recomputed canonical digest mismatch for {lock['path']}: {actual} != {expected}")
            checked += 1
    return checked


def validate_lane_adapters(by_id: dict[str, dict], adapters: dict) -> None:
    if adapters.get("schema") != "STAGE32_LANE_CLAIM_ADAPTERS_V1":
        raise CheckError("unexpected lane adapter schema")
    lanes = adapters.get("lanes")
    if not isinstance(lanes, list):
        raise CheckError("lane adapters must contain lanes list")
    expected = {"MAIN", "EX1", "EX2", "EX3", "EX4", "EX5", "EX6"}
    seen = set()
    for lane in lanes:
        name = lane.get("lane")
        if name in seen:
            raise CheckError(f"duplicate lane adapter: {name}")
        seen.add(name)
        state_path = lane.get("state_path")
        if not isinstance(state_path, str) or not (ROOT / state_path).is_file():
            raise CheckError(f"{name}: missing state_path")
        refs = lane.get("claim_refs")
        if not isinstance(refs, list) or not refs:
            raise CheckError(f"{name}: empty claim_refs")
        for cid in refs:
            if cid not in by_id:
                raise CheckError(f"{name}: adapter references unknown claim {cid}")
    if seen != expected:
        raise CheckError(f"lane adapter coverage mismatch: {sorted(seen)}")


def transitive_dependencies(by_id: dict[str, dict], root_id: str) -> set[str]:
    out: set[str] = set()
    todo = list(by_id[root_id]["requires"])
    while todo:
        cid = todo.pop()
        if cid in out:
            continue
        out.add(cid)
        todo.extend(by_id[cid]["requires"])
    return out


def run_final_check(by_id: dict[str, dict], final: dict) -> tuple[bool, list[str]]:
    validate_final_contract(final)
    milestones = final["required_milestones"]
    missing: list[str] = []
    milestone_ids: set[str] = set()
    for item in milestones:
        cid = item["required_claim_id"]
        wanted = item["required_authority_status"]
        milestone_ids.add(cid)
        if cid not in by_id:
            missing.append(f"{item['slot']}: missing {cid}")
            continue
        claim = by_id[cid]
        if claim["authority_status"] != wanted:
            missing.append(f"{item['slot']}: {cid} status {claim['authority_status']} != {wanted}")
    if missing:
        return False, missing
    contract = final["closure_contract"]
    root_id = contract["required_final_claim_id"]
    if root_id not in by_id:
        return False, [f"missing final claim {root_id}"]
    if root_id not in milestone_ids:
        return False, [f"final root is not a required milestone: {root_id}"]
    root = by_id[root_id]
    for token in contract["required_proves_tokens"]:
        if token not in root["proves"]:
            return False, [f"final claim missing required PROVES token: {token}"]
    for token in contract["forbidden_proves_tokens"]:
        if token in root["proves"]:
            return False, [f"final claim illegally PROVES: {token}"]
    if root["authority_status"] != "AUDITED":
        return False, [f"final claim is not AUDITED: {root_id}"]
    receipt = root["audit_receipt"]
    if not isinstance(receipt, dict) or receipt.get("status") != "PASS":
        return False, [f"final claim lacks PASS audit receipt: {root_id}"]
    deps = transitive_dependencies(by_id, root_id)
    required_ancestors = milestone_ids - {root_id}
    unreachable = sorted(required_ancestors - deps)
    if unreachable:
        return False, ["final claim dependency closure does not contain required milestones: " + ", ".join(unreachable)]
    bad = []
    for cid in sorted(deps):
        claim = by_id[cid]
        if claim["kind"] in {"mathematical_claim", "adapter_contract"} and claim["authority_status"] != "AUDITED":
            bad.append(f"{cid}={claim['authority_status']}")
    if bad:
        return False, ["non-audited transitive proof dependencies: " + ", ".join(bad)]
    return True, []


def synthetic_audited_claim(cid: str, requires: list[str] | None = None, proves: list[str] | None = None) -> dict:
    return {"claim_id":cid,"kind":"mathematical_claim","statement":"synthetic fail-close fixture","scope_key":"S32.TEST.FINAL","scope":{},"proves":proves or ["synthetic"],"does_not_prove":["production credit"],"requires":requires or [],"source_locks":[],"replay_verifier":None,"authority_status":"AUDITED","audit_receipt":{"status":"PASS","pr":1,"review_id":1,"exact_head":"0"*40}}


def synthetic_final_fixture() -> dict:
    return {"schema":"STAGE32_FINAL_CHECK_V1","stage":32,"mode":"FAIL_CLOSED_FOR_STAGE32_CLOSURE","required_milestones":copy.deepcopy(EXPECTED_FINAL_MILESTONES),"closure_contract":{"required_final_claim_id":EXPECTED_FINAL_ROOT_ID,"required_proves_tokens":copy.deepcopy(EXPECTED_FINAL_REQUIRED_PROVES),"forbidden_proves_tokens":copy.deepcopy(EXPECTED_FINAL_FORBIDDEN_PROVES),**{key:True for key in EXPECTED_FINAL_TRUE_FLAGS}}}


def run_fail_closed_self_test() -> dict:
    ids = [item["required_claim_id"] for item in EXPECTED_FINAL_MILESTONES]
    by_id = {cid: synthetic_audited_claim(cid) for cid in ids}
    root_id = EXPECTED_FINAL_ROOT_ID
    by_id[root_id]["proves"] = ["STAGE32_CLOSED=true"]
    final_fixture = synthetic_final_fixture()
    ok, reasons = run_final_check(by_id, final_fixture)
    if ok or not any("dependency closure" in reason for reason in reasons):
        raise CheckError("self-test: disconnected audited milestones did not fail closed")
    weakened_flag = copy.deepcopy(final_fixture)
    weakened_flag["closure_contract"]["required_milestones_must_be_transitive_dependencies_of_final_root"] = False
    try:
        validate_final_contract(weakened_flag)
    except CheckError as exc:
        if "safety flag must remain true" not in str(exc): raise
    else:
        raise CheckError("self-test: weakened FINAL-CHECK safety boolean was accepted")
    weakened_milestones = copy.deepcopy(final_fixture)
    weakened_milestones["required_milestones"].pop(0)
    try:
        validate_final_contract(weakened_milestones)
    except CheckError as exc:
        if "reserved milestone contract drift" not in str(exc): raise
    else:
        raise CheckError("self-test: removed reserved FINAL-CHECK milestone was accepted")
    unresolved_math = {"claim_id":"S32.TEST.UNRESOLVED_MATH.V1","kind":"mathematical_claim","statement":"synthetic unresolved mathematical goal","scope_key":"S32.TEST.AUTHORITY","scope":{},"proves":["synthetic unresolved goal"],"does_not_prove":["audited credit"],"requires":[],"source_locks":[],"replay_verifier":None,"authority_status":"DECLARED_GOAL","audit_receipt":None}
    unresolved_math["claim_core_sha256"] = claim_core_sha(unresolved_math)
    audited_child = {"claim_id":"S32.TEST.AUDITED_CHILD.V1","kind":"mathematical_claim","statement":"synthetic audited child","scope_key":"S32.TEST.AUTHORITY","scope":{},"proves":["synthetic audited result"],"does_not_prove":["production credit"],"requires":[unresolved_math["claim_id"]],"source_locks":[],"replay_verifier":None,"authority_status":"AUDITED","audit_receipt":{"status":"PASS","pr":1,"review_id":1,"exact_head":"0"*40}}
    audited_child["claim_core_sha256"] = claim_core_sha(audited_child)
    authority_fixture = validate_claims([unresolved_math, audited_child])
    try:
        validate_dependencies(authority_fixture)
    except CheckError as exc:
        if "unresolved mathematical DECLARED_GOAL" not in str(exc): raise
    else:
        raise CheckError("self-test: AUDITED claim consumed unresolved mathematical DECLARED_GOAL")
    adapter = {"claim_id":"S32.TEST.ADAPTER.V1","kind":"adapter_contract","statement":"synthetic bridge immutability fixture","scope_key":"S32.TEST.ADAPTER","scope":{},"proves":["synthetic adapter"],"does_not_prove":["production credit"],"requires":[],"bridges":{"from_scope_key":"S32.TEST.A","to_scope_key":"S32.TEST.B"},"source_locks":[],"replay_verifier":None,"authority_status":"DECLARED_GOAL","audit_receipt":None}
    adapter["claim_core_sha256"] = claim_core_sha(adapter)
    validate_claims([adapter])
    mutated = copy.deepcopy(adapter)
    mutated["bridges"]["from_scope_key"] = "S32.TEST.C"
    try:
        validate_claims([mutated])
    except CheckError as exc:
        if "immutable claim core hash mismatch" not in str(exc): raise
    else:
        raise CheckError("self-test: bridge mutation preserved immutable core hash")
    missing_bridge = copy.deepcopy(adapter)
    missing_bridge.pop("bridges")
    missing_bridge["claim_core_sha256"] = claim_core_sha(missing_bridge)
    try:
        validate_claims([missing_bridge])
    except CheckError as exc:
        if "requires bridges object" not in str(exc): raise
    else:
        raise CheckError("self-test: adapter without bridge shape was accepted")
    return {"verdict":"PASS_STAGE32_FAIL_CLOSED_SELF_TEST","disconnected_final_milestones_rejected":True,"production_final_safety_boolean_weakening_rejected":True,"production_final_milestone_removal_rejected":True,"audited_to_unresolved_mathematical_goal_rejected":True,"bridge_mutation_changes_core":True,"adapter_bridge_shape_required":True}


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--integrity", action="store_true", help="check registry/DAG/source-lock integrity (default)")
    mode.add_argument("--final", action="store_true", help="run fail-closed Stage32 FINAL-CHECK")
    mode.add_argument("--self-test-fail-closed", action="store_true", help="replay synthetic fail-close regression tests")
    args = parser.parse_args()
    try:
        if args.self_test_fail_closed:
            print(json.dumps(run_fail_closed_self_test(), sort_keys=True))
            return 0
        schema = load_json(SCHEMA_PATH)
        if schema.get("$id") != "STAGE32_CLAIM_REGISTRY_SCHEMA_V1":
            raise CheckError("claim registry schema file drift")
        registry = load_json(REGISTRY_PATH)
        adapters = load_json(ADAPTER_PATH)
        final = load_json(FINAL_PATH)
        validate_final_contract(final)
        claims = validate_registry_shape(registry)
        by_id = validate_claims(claims)
        validate_dependencies(by_id)
        replay_verifier_count = validate_replay_verifiers(by_id)
        source_lock_count = validate_source_locks(by_id)
        validate_lane_adapters(by_id, adapters)
        status_counts = Counter(c["authority_status"] for c in claims)
        base = {"verdict":"PASS_STAGE32_CLAIM_DAG_INTEGRITY","claim_count":len(claims),"source_locks_checked":source_lock_count,"replay_verifiers_checked":replay_verifier_count,"authority_status_counts":dict(sorted(status_counts.items())),"lanes":["MAIN","EX1","EX2","EX3","EX4","EX5","EX6"],"final_contract_locked":True}
        if args.final:
            ok, reasons = run_final_check(by_id, final)
            if not ok:
                print(json.dumps({**base,"verdict":"NOT_READY_STAGE32_FINAL_CHECK","final_ready":False,"reasons":reasons}, sort_keys=True))
                return 2
            print(json.dumps({**base,"verdict":"PASS_STAGE32_FINAL_CHECK","final_ready":True}, sort_keys=True))
            return 0
        print(json.dumps(base, sort_keys=True))
        return 0
    except CheckError as exc:
        print(json.dumps({"verdict":"FAIL_STAGE32_CLAIM_DAG_INTEGRITY","error":str(exc)}, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
