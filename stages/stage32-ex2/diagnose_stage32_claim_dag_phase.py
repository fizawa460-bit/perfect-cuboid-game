#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROOF = ROOT / "stages/stage32/proof"
sys.path.insert(0, str(PROOF))
import verify_stage32_claim_dag_impl as v  # noqa: E402


def load_base():
    schema = v.load_json(v.SCHEMA_PATH)
    if schema.get("$id") != "STAGE32_CLAIM_REGISTRY_SCHEMA_V1":
        raise v.CheckError("claim registry schema file drift")
    registry = v.load_json(v.REGISTRY_PATH)
    adapters = v.load_json(v.ADAPTER_PATH)
    final = v.load_json(v.FINAL_PATH)
    v.validate_final_contract(final)
    claims = v.validate_registry_shape(registry)
    return claims, adapters


def diagnose_sources(by_id: dict[str, dict], adapters: dict) -> int:
    mismatches: list[dict] = []
    reverse: dict[str, list[str]] = {cid: [] for cid in by_id}
    for cid, claim in by_id.items():
        for dep in claim["requires"]:
            reverse.setdefault(dep, []).append(cid)
    lane_refs: dict[str, list[str]] = {cid: [] for cid in by_id}
    for lane in adapters.get("lanes", []):
        for cid in lane.get("claim_refs", []):
            lane_refs.setdefault(cid, []).append(str(lane.get("lane")))

    for cid, claim in by_id.items():
        for lock in claim["source_locks"]:
            path = ROOT / lock["path"]
            reason = None
            actual_blob = None
            if not path.is_file():
                reason = "missing"
            else:
                data = path.read_bytes()
                actual_blob = v.git_blob_sha1(data)
                expected_blob = lock.get("blob_sha1")
                if expected_blob is not None and actual_blob != expected_blob:
                    reason = "blob_mismatch"
                elif "canonical_sha256" in lock:
                    try:
                        obj = json.loads(data)
                    except Exception:
                        reason = "canonical_non_json"
                    else:
                        expected = lock["canonical_sha256"]
                        stored = obj.get("canonical_sha256_without_this_field")
                        stripped = dict(obj)
                        stripped.pop("canonical_sha256_without_this_field", None)
                        actual_canon = v.csha(stripped)
                        if stored != expected or actual_canon != expected:
                            reason = "canonical_mismatch"
            if reason:
                mismatches.append({
                    "claim_id": cid,
                    "authority_status": claim["authority_status"],
                    "kind": claim["kind"],
                    "path": lock["path"],
                    "reason": reason,
                    "expected_blob": lock.get("blob_sha1"),
                    "actual_blob": actual_blob,
                    "direct_dependents": sorted(reverse.get(cid, [])),
                    "lane_refs": sorted(lane_refs.get(cid, [])),
                })

    if mismatches:
        print("SOURCE_LOCK_MISMATCHES=" + json.dumps(mismatches, sort_keys=True))
        raise v.CheckError(f"source-lock mismatch count={len(mismatches)}")
    v.validate_source_locks(by_id)
    print("PASS claim-DAG phase=source-locks")
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("phase", choices=["shape", "claims", "dependencies", "replay", "sources", "lanes"])
    a = p.parse_args()
    try:
        claims, adapters = load_base()
        if a.phase == "shape":
            print("PASS claim-DAG phase=shape-final-contract")
            return 0
        by_id = v.validate_claims(claims)
        if a.phase == "claims":
            print("PASS claim-DAG phase=claim-core")
            return 0
        v.validate_dependencies(by_id)
        if a.phase == "dependencies":
            print("PASS claim-DAG phase=dependencies")
            return 0
        v.validate_replay_verifiers(by_id)
        if a.phase == "replay":
            print("PASS claim-DAG phase=replay-paths")
            return 0
        if a.phase == "sources":
            return diagnose_sources(by_id, adapters)
        v.validate_source_locks(by_id)
        v.validate_lane_adapters(by_id, adapters)
        print("PASS claim-DAG phase=lane-adapters")
        return 0
    except v.CheckError as exc:
        print(f"FAIL claim-DAG phase={a.phase}: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
