#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BUNDLE = ROOT / "stages/stage32/scratch/q602-o210-versioned-claim-bundle-20260909.json"
PREFLIGHT = ROOT / "stages/stage32/scratch/q602-o210-forgetful-adapter-preflight-20260909.json"
ORIGIN = ROOT / "stages/stage32/scratch/q602-o210-forgetful-adapter-post1500-origin-addendum-20260909.json"
ACTIVE = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"

CORE_KEYS = [
    "claim_id", "kind", "statement", "scope_key", "scope", "proves",
    "does_not_prove", "requires", "bridges", "source_locks", "replay_verifier",
]
EXPECTED_BUNDLE_CANONICAL = "9ce14c2d619685ab9c22a83ccd36cc1b085bf1579132df7b0c0b2b4b1122ba07"
EXPECTED_ADAPTER_CORE = "ed1ea5441a3b0bb876a3a8b93f272e2a16d693f1b44f0f050c13af1625c1e028"
EXPECTED_Q602_V2_CORE = "f27890319709b9ee24a71e744990c9c5fb36d746cacb7bd8ee11a905bfc9750e"
EXPECTED_O210_V3_CORE = "7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canonical_without_field(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    return csha(x)


def claim_core(claim: dict) -> str:
    return csha({k: claim[k] for k in CORE_KEYS if k in claim})


def check_lock(lock: dict) -> None:
    path = ROOT / lock["path"]
    data = path.read_bytes()
    assert blob_sha1(data) == lock["blob_sha1"], lock["path"]
    if "canonical_sha256" in lock:
        obj = json.loads(data)
        assert obj["canonical_sha256_without_this_field"] == lock["canonical_sha256"]
        assert canonical_without_field(obj) == lock["canonical_sha256"]


def main() -> None:
    b = json.loads(BUNDLE.read_text())
    assert b["schema"] == "STAGE32_Q602_O210_VERSIONED_CLAIM_BUNDLE_V1"
    assert canonical_without_field(b) == b["canonical_sha256_without_this_field"] == EXPECTED_BUNDLE_CANONICAL
    assert b["claim_core_keys"] == CORE_KEYS
    assert b["fixed_target"] == {
        "row_id": "g1-d186", "picard_class": "V6", "d": 186, "e": 266,
        "genus": 1, "O": 210, "qprime": 4, "Q": 602,
        "formal_survivors": [73, 97, 235],
    }

    p = json.loads(PREFLIGHT.read_text())
    o = json.loads(ORIGIN.read_text())
    assert canonical_without_field(p) == "bfd17b6b41e32ab9ce729c2fb735477beb3e70061576433a16d1d0ad30edce69"
    assert canonical_without_field(o) == "7399302b10711a77a656f54bf34e2305d5358ea0eb2c29370c77c7f49d6fcf6e"
    assert p["decision"]["result"] == "TYPED_FORGETFUL_ADAPTER_IS_SOURCE_SUPPORTED_AS_SCRATCH_PREFLIGHT"
    assert o["exact_semantic_anchor"]["Q"] == 602
    assert "Q(T)=602" in o["exact_semantic_anchor"]["required_new_input"]

    adapter = b["adapter_claim"]
    q602 = b["q602_exclusion_claim"]
    assert adapter["claim_id"] == "S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1"
    assert q602["claim_id"] == "S32.Q602.EXCLUSION.V2"
    assert adapter["authority_status"] == q602["authority_status"] == "PROVISIONAL"
    assert adapter["audit_receipt"]["status"] == q602["audit_receipt"]["status"] == "NOT_AUDITED"
    assert claim_core(adapter) == adapter["claim_core_sha256"] == EXPECTED_ADAPTER_CORE
    assert claim_core(q602) == q602["claim_core_sha256"] == EXPECTED_Q602_V2_CORE
    assert adapter["bridges"]["from_scope_key"] == "S32.Q602.ADMISSIBLE_CONFIGURATION"
    assert adapter["bridges"]["to_scope_key"] == "S32.O210.COVER"
    assert "S32.O210.EXCLUSION.V3" in q602["requires"]
    assert adapter["claim_id"] in q602["requires"]
    assert b["prerequisite_authority"]["o210_claim_core_sha256"] == EXPECTED_O210_V3_CORE

    for lock in adapter["source_locks"]:
        check_lock(lock)
    for lock in q602["source_locks"]:
        check_lock(lock)

    active = json.loads(ACTIVE.read_text())
    active_ids = {c["claim_id"] for c in active["claims"]}
    support_ids = {c["claim_id"] for c in active["supporting_claims"]}
    assert "S32.Q602.EXCLUSION.V1" in active_ids
    assert "S32.Q602.EXCLUSION.V2" not in active_ids
    assert adapter["claim_id"] not in active_ids | support_ids
    assert b["versioning"]["q602_v1_mutation_forbidden"] is True
    assert all(v is False for v in b["authority_firewalls"].values())

    print("PASS_STAGE32_SCRATCH_Q602_O210_VERSIONED_CLAIM_BUNDLE")
    print("bundle_canonical=" + EXPECTED_BUNDLE_CANONICAL)
    print("adapter_core=" + EXPECTED_ADAPTER_CORE)
    print("q602_v2_core=" + EXPECTED_Q602_V2_CORE)
    print("authority_change=false")


if __name__ == "__main__":
    main()
