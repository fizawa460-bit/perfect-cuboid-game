#!/usr/bin/env python3
from __future__ import annotations

import argparse
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
        v.validate_source_locks(by_id)
        if a.phase == "sources":
            print("PASS claim-DAG phase=source-locks")
            return 0
        v.validate_lane_adapters(by_id, adapters)
        print("PASS claim-DAG phase=lane-adapters")
        return 0
    except v.CheckError as exc:
        print(f"FAIL claim-DAG phase={a.phase}: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
