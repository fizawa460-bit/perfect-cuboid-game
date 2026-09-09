#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROOF = ROOT / "stages/stage32/proof"
BUNDLE = ROOT / "stages/stage32/q602-claim-dag-variance-repair-preflight-20260909.json"
OLD_BUNDLE = ROOT / "stages/stage32/scratch/q602-o210-versioned-claim-bundle-20260909.json"
ACTIVE = PROOF / "ACTIVE-FRONTIER.json"
BASE = PROOF / "CLAIM-REGISTRY.json"
BASE_VERIFIER = PROOF / "verify_stage32_claim_dag.py"
STATE = ROOT / "stages/stage32/MAIN-STATE.json"

BUNDLE_CANON = "1ed236ef01fbe739282c10a259dd7b000975cd7a32e475e7a9c8c10bb76c9b38"
OLD_ADAPTER_CORE = "ed1ea5441a3b0bb876a3a8b93f272e2a16d693f1b44f0f050c13af1625c1e028"
OLD_Q602_V2_CORE = "f27890319709b9ee24a71e744990c9c5fb36d746cacb7bd8ee11a905bfc9750e"
NEW_ADAPTER_CORE = "4dd78ed5a1917d7c953fee95bb52f1d1429e239ca90d3bf8dae26461e0611de8"
NEW_Q602_V3_CORE = "c85a76ac1ed07deec1d65269451452d33b63c3a5221134ee687e282951823067"
AUDIT = {"status":"PASS","pr":1730,"review_id":5149322780,"exact_head":"1689ed2bdfa149b5e462ce0182e7a7e7c31ee62c"}

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def load_basev():
    spec = importlib.util.spec_from_file_location("stage32_claim_base_wrapper", BASE_VERIFIER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load claim verifier")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def main() -> None:
    basev = load_basev()
    b = load(BUNDLE)
    old = load(OLD_BUNDLE)
    active = load(ACTIVE)
    state = load(STATE)
    base = load(BASE)

    stripped = dict(b)
    stored = stripped.pop("canonical_sha256_without_this_field")
    assert stored == BUNDLE_CANON
    assert basev.csha(stripped) == BUNDLE_CANON

    assert b["diagnosis"]["audited_object_level_adapter_core_sha256"] == OLD_ADAPTER_CORE
    assert b["diagnosis"]["audited_q602_v2_core_sha256"] == OLD_Q602_V2_CORE
    assert b["diagnosis"]["audit_receipt"] == AUDIT

    new = {c["claim_id"]: c for c in b["new_claims"]}
    nad = new["S32.ADAPTER.O210_EMPTY_TO_Q602_REALIZATION_EMPTY.V1"]
    nv3 = new["S32.Q602.EXCLUSION.V3"]
    assert nad["claim_core_sha256"] == NEW_ADAPTER_CORE
    assert nv3["claim_core_sha256"] == NEW_Q602_V3_CORE
    assert basev.claim_core_sha(nad) == NEW_ADAPTER_CORE
    assert basev.claim_core_sha(nv3) == NEW_Q602_V3_CORE
    assert nad["bridges"]["from_scope_key"] == "S32.O210.COVER"
    assert nad["bridges"]["to_scope_key"] == "S32.Q602.ARITHMETIC"
    assert nad["scope"]["object_map_direction"] == "S32.Q602.ADMISSIBLE_CONFIGURATION -> S32.O210.COVER"
    assert nad["scope"]["claim_credit_direction"] == "S32.O210.COVER -> S32.Q602.ARITHMETIC"

    old_ad = dict(old["adapter_claim"])
    assert old_ad["claim_core_sha256"] == OLD_ADAPTER_CORE
    assert old_ad["bridges"]["from_scope_key"] == "S32.Q602.ADMISSIBLE_CONFIGURATION"
    assert old_ad["bridges"]["to_scope_key"] == "S32.O210.COVER"
    old_ad["authority_status"] = "AUDITED"
    old_ad["audit_receipt"] = dict(AUDIT)
    assert basev.claim_core_sha(old_ad) == OLD_ADAPTER_CORE

    old_v2 = dict(old["q602_exclusion_claim"])
    assert old_v2["claim_core_sha256"] == OLD_Q602_V2_CORE
    old_v2["authority_status"] = "AUDITED"
    old_v2["audit_receipt"] = dict(AUDIT)
    assert basev.claim_core_sha(old_v2) == OLD_Q602_V2_CORE

    base_claims = basev.validate_registry_shape(base)
    current_support = list(active["supporting_claims"])
    current_active = list(active["claims"])
    qv1 = [c for c in current_active if c["claim_id"] == "S32.Q602.EXCLUSION.V1"]
    assert len(qv1) == 1
    assert qv1[0]["authority_status"] == "DECLARED_GOAL"
    assert state["current_exact_frontier"]["o210_excluded"] is True
    assert state["current_exact_frontier"]["q602_excluded"] is False
    assert state["firewalls"]["Q602_excluded"] is False
    assert state["firewalls"]["O212_plus_advance_allowed"] is False

    old_candidate = (
        list(base_claims)
        + current_support
        + [old_ad]
        + [c for c in current_active if c["claim_id"] != "S32.Q602.EXCLUSION.V1"]
        + [old_v2]
    )
    old_by = basev.validate_claims(old_candidate)
    failed_closed = False
    try:
        basev.validate_dependencies(old_by)
    except Exception as exc:
        text = str(exc)
        assert "cross-scope mathematical dependency" in text
        failed_closed = True
    assert failed_closed

    repaired_candidate = (
        list(base_claims)
        + current_support
        + [old_ad, nad]
        + [c for c in current_active if c["claim_id"] != "S32.Q602.EXCLUSION.V1"]
        + [nv3]
    )
    repaired_by = basev.validate_claims(repaired_candidate)
    basev.validate_dependencies(repaired_by)
    basev.validate_replay_verifiers(repaired_by)
    basev.validate_source_locks(repaired_by)

    assert b["authority_firewalls"] == {
        "new_adapter_audited": False,
        "q602_v3_audited": False,
        "claim_sync_done": False,
        "q602_excluded": False,
        "o212_plus_advance_allowed": False,
        "full178_complete": False,
        "stage32_closed": False,
        "endpoint_credit": False,
        "merge_authorized": False,
    }

    print("PASS_STAGE32_Q602_CLAIM_DAG_VARIANCE_REPAIR_PREFLIGHT")
    print("old_q602_v2_direct_sync_fail_closed=true")
    print("new_adapter_core=" + NEW_ADAPTER_CORE)
    print("new_q602_v3_core=" + NEW_Q602_V3_CORE)
    print(json.dumps({
        "Q602_excluded": False,
        "O212_plus_advance_allowed": False,
        "FULL178_complete": False,
        "Stage32_closed": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
