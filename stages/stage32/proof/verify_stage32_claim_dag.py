#!/usr/bin/env python3
from __future__ import annotations

import argparse
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
ALLOWED_STATUS = {"SCRATCH", "PROVISIONAL", "AUDITED", "DECLARED_GOAL", "SUPERSEDED", "REVOKED"}
ALLOWED_KIND = {"authority_snapshot", "mathematical_claim", "lane_contract", "adapter_contract"}
CORE_KEYS = [
    "claim_id",
    "kind",
    "statement",
    "scope_key",
    "scope",
    "proves",
    "does_not_prove",
    "requires",
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
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    prefix = f"blob {len(data)}\0".encode()
    return hashlib.sha1(prefix + data).hexdigest()


def claim_core_sha(claim: dict) -> str:
    return csha({key: claim[key] for key in CORE_KEYS})


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


def validate_claims(claims: list[dict]) -> dict[str, dict]:
    by_id: dict[str, dict] = {}
    for claim in claims:
        for key in (
            "claim_id",
            "kind",
            "statement",
            "scope_key",
            "scope",
            "proves",
            "does_not_prove",
            "requires",
            "claim_core_sha256",
            "authority_status",
            "source_locks",
            "audit_receipt",
        ):
            if key not in claim:
                raise CheckError(f"claim missing {key}: {claim.get('claim_id')}")
        cid = claim["claim_id"]
        if not isinstance(cid, str) or not CLAIM_ID_RE.fullmatch(cid):
            raise CheckError(f"invalid claim ID: {cid!r}")
        if cid in by_id:
            raise CheckError(f"duplicate claim ID: {cid}")
        if claim["kind"] not in ALLOWED_KIND:
            raise CheckError(f"{cid}: invalid kind {claim['kind']}")
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
            if not isinstance(receipt.get("exact_head"), str) or not HEX40_RE.fullmatch(receipt["exact_head"]):
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
            if dep["authority_status"] == "REVOKED":
                raise CheckError(f"{cid}: dependency is REVOKED: {dep_id}")
            if claim["authority_status"] != "SCRATCH" and dep["authority_status"] == "SCRATCH":
                raise CheckError(f"{cid}: non-SCRATCH claim depends on SCRATCH {dep_id}")
            if claim["authority_status"] == "PROVISIONAL" and dep["authority_status"] not in {
                "AUDITED",
                "PROVISIONAL",
                "DECLARED_GOAL",
            }:
                raise CheckError(f"{cid}: illegal PROVISIONAL dependency status on {dep_id}")
            if claim["authority_status"] == "AUDITED" and dep["authority_status"] not in {
                "AUDITED",
                "DECLARED_GOAL",
            }:
                raise CheckError(f"{cid}: AUDITED claim depends on non-audited proof input {dep_id}")

            # A mathematical dependency crossing scope must use an explicit adapter.
            if (
                claim["kind"] == "mathematical_claim"
                and dep["kind"] == "mathematical_claim"
                and claim["scope_key"] != dep["scope_key"]
            ):
                acceptable = []
                for adapter_id in claim["requires"]:
                    adapter = by_id.get(adapter_id)
                    if not adapter or adapter["kind"] != "adapter_contract":
                        continue
                    bridge = adapter.get("bridges")
                    if not isinstance(bridge, dict):
                        continue
                    if bridge.get("from_scope_key") != dep["scope_key"]:
                        continue
                    if bridge.get("to_scope_key") != claim["scope_key"]:
                        continue
                    if claim["authority_status"] == "AUDITED" and adapter["authority_status"] != "AUDITED":
                        continue
                    if claim["authority_status"] == "PROVISIONAL" and adapter["authority_status"] not in {
                        "AUDITED",
                        "PROVISIONAL",
                    }:
                        continue
                    acceptable.append(adapter_id)
                if not acceptable:
                    raise CheckError(
                        f"{cid}: cross-scope mathematical dependency {dep_id} requires explicit adapter_contract"
                    )

    color: dict[str, int] = {cid: 0 for cid in by_id}
    stack: list[str] = []

    def visit(cid: str) -> None:
        color[cid] = 1
        stack.append(cid)
        for dep in by_id[cid]["requires"]:
            if color[dep] == 1:
                cycle = " -> ".join(stack + [dep])
                raise CheckError(f"claim dependency cycle: {cycle}")
            if color[dep] == 0:
                visit(dep)
        stack.pop()
        color[cid] = 2

    for cid in by_id:
        if color[cid] == 0:
            visit(cid)


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
                    raise CheckError(
                        f"{cid}: blob source-lock mismatch for {lock['path']}: {actual} != {expected}"
                    )
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
                    raise CheckError(
                        f"{cid}: stored canonical digest mismatch for {lock['path']}: {stored} != {expected}"
                    )
                stripped = dict(obj)
                stripped.pop("canonical_sha256_without_this_field", None)
                actual = csha(stripped)
                if actual != expected:
                    raise CheckError(
                        f"{cid}: recomputed canonical digest mismatch for {lock['path']}: {actual} != {expected}"
                    )
            checked += 1
    return checked


def validate_lane_adapters(by_id: dict[str, dict], adapters: dict) -> None:
    if adapters.get("schema") != "STAGE32_LANE_CLAIM_ADAPTERS_V1":
        raise CheckError("unexpected lane adapter schema")
    lanes = adapters.get("lanes")
    if not isinstance(lanes, list):
        raise CheckError("lane adapters must contain lanes list")
    expected = {"MAIN", "EX1", "EX2", "EX3", "EX4", "EX5"}
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
    if final.get("schema") != "STAGE32_FINAL_CHECK_V1":
        raise CheckError("unexpected FINAL-CHECK schema")
    missing: list[str] = []
    milestones = final.get("required_milestones")
    if not isinstance(milestones, list) or not milestones:
        raise CheckError("FINAL-CHECK requires milestone list")
    for item in milestones:
        cid = item.get("required_claim_id")
        wanted = item.get("required_authority_status")
        if cid not in by_id:
            missing.append(f"{item.get('slot')}: missing {cid}")
            continue
        claim = by_id[cid]
        if claim["authority_status"] != wanted:
            missing.append(
                f"{item.get('slot')}: {cid} status {claim['authority_status']} != {wanted}"
            )
    if missing:
        return False, missing

    contract = final.get("closure_contract", {})
    root_id = contract.get("required_final_claim_id")
    if root_id not in by_id:
        return False, [f"missing final claim {root_id}"]
    root = by_id[root_id]
    for token in contract.get("required_proves_tokens", []):
        if token not in root["proves"]:
            return False, [f"final claim missing required PROVES token: {token}"]
    for token in contract.get("forbidden_proves_tokens", []):
        if token in root["proves"]:
            return False, [f"final claim illegally PROVES: {token}"]
    if root["authority_status"] != "AUDITED":
        return False, [f"final claim is not AUDITED: {root_id}"]
    receipt = root["audit_receipt"]
    if not isinstance(receipt, dict) or receipt.get("status") != "PASS":
        return False, [f"final claim lacks PASS audit receipt: {root_id}"]

    if contract.get("all_transitive_mathematical_dependencies_must_be_audited", True):
        bad = []
        for cid in sorted(transitive_dependencies(by_id, root_id)):
            claim = by_id[cid]
            if claim["kind"] in {"mathematical_claim", "adapter_contract"} and claim["authority_status"] != "AUDITED":
                bad.append(f"{cid}={claim['authority_status']}")
        if bad:
            return False, ["non-audited transitive proof dependencies: " + ", ".join(bad)]
    return True, []


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--integrity", action="store_true", help="check registry/DAG/source-lock integrity (default)")
    mode.add_argument("--final", action="store_true", help="run fail-closed Stage32 FINAL-CHECK")
    args = parser.parse_args()

    try:
        # Schema is retained as a contract artifact; manual stdlib validation avoids a new jsonschema dependency.
        schema = load_json(SCHEMA_PATH)
        if schema.get("$id") != "STAGE32_CLAIM_REGISTRY_SCHEMA_V1":
            raise CheckError("claim registry schema file drift")
        registry = load_json(REGISTRY_PATH)
        adapters = load_json(ADAPTER_PATH)
        final = load_json(FINAL_PATH)

        claims = validate_registry_shape(registry)
        by_id = validate_claims(claims)
        validate_dependencies(by_id)
        source_lock_count = validate_source_locks(by_id)
        validate_lane_adapters(by_id, adapters)

        status_counts = Counter(c["authority_status"] for c in claims)
        base = {
            "verdict": "PASS_STAGE32_CLAIM_DAG_INTEGRITY",
            "claim_count": len(claims),
            "source_locks_checked": source_lock_count,
            "authority_status_counts": dict(sorted(status_counts.items())),
            "lanes": ["MAIN", "EX1", "EX2", "EX3", "EX4", "EX5"],
        }

        if args.final:
            ok, reasons = run_final_check(by_id, final)
            if not ok:
                print(json.dumps({
                    **base,
                    "verdict": "NOT_READY_STAGE32_FINAL_CHECK",
                    "final_ready": False,
                    "reasons": reasons,
                }, sort_keys=True))
                return 2
            print(json.dumps({
                **base,
                "verdict": "PASS_STAGE32_FINAL_CHECK",
                "final_ready": True,
            }, sort_keys=True))
            return 0

        print(json.dumps(base, sort_keys=True))
        return 0
    except CheckError as exc:
        print(json.dumps({"verdict": "FAIL_STAGE32_CLAIM_DAG_INTEGRITY", "error": str(exc)}, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
