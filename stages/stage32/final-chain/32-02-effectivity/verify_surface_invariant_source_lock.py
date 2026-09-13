#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
LOCK = HERE / "SURFACE-INVARIANT-SOURCE-LOCK.json"


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(f"FAIL: {message}")


def canonical_without_self(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def main() -> None:
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    req(lock["schema"] == "STAGE32_FINAL_CHAIN_32_02_SURFACE_INVARIANT_SOURCE_LOCK_V1", "source-lock schema drift")
    req(canonical_without_self(lock) == lock["canonical_sha256_without_this_field"], "source-lock canonical drift")

    s29 = lock["stage29_source"]
    s29_path = REPO / s29["path"]
    req(blob(s29_path) == s29["blob_sha"], "Stage29 source-lock blob drift")
    source = s29_path.read_text(encoding="utf-8")
    req(s29["source_audit"] == "PASS", "Stage29 source audit is not PASS")
    for token in s29["required_statements"]:
        req(token in source, f"Stage29 source-lock statement missing: {token}")

    hist = lock["historical_rr"]
    hist_path = REPO / hist["path"]
    req(blob(hist_path) == hist["blob_sha"], "historical RR blob drift")
    hist_rr = json.loads(hist_path.read_text(encoding="utf-8"))
    req(canonical_without_self(hist_rr) == hist["canonical_sha256_without_this_field"], "historical RR canonical drift")
    req(hist_rr["source_locks"]["source_lock_audit"] == hist["source_lock_audit"] == "PASS", "historical RR source audit drift")
    req(hist_rr["source_locks"]["testa_stoll_stage29_source_lock"] == s29["path"], "historical RR Stage29 source path drift")

    expected_invariants = {
        "K_big": True,
        "K_nef": True,
        "K_square": 16,
        "chi_O": 8,
        "p_g": 7,
        "q": 0,
    }
    req(hist_rr["source_locks"]["surface_invariants"] == expected_invariants, "historical RR surface invariants drift")
    retained = lock["surface_invariants"]
    req(retained["K_square"] == 16, "K^2 drift")
    req(retained["p_g"] == 7 and retained["q"] == 0, "p_g/q drift")
    req(retained["chi_O"] == 1 - retained["q"] + retained["p_g"] == 8, "chi(O) derivation drift")
    req(retained["K_big"] is True and retained["K_nef"] is True, "big/nef source lock drift")

    audit = lock["historical_fresh_audit"]
    audit_path = REPO / audit["path"]
    req(blob(audit_path) == audit["blob_sha"], "historical fresh-audit blob drift")
    audit_text = audit_path.read_text(encoding="utf-8")
    for token in audit["required_degree_bridge"]:
        req(token in audit_text, f"historical K.C bridge missing: {token}")

    n348 = lock["retired_n348_replay"]
    n348_path = REPO / n348["path"]
    req(blob(n348_path) == n348["blob_sha"], "retired N348 verifier blob drift")
    n348_text = n348_path.read_text(encoding="utf-8")
    for token in (
        'SOURCE_LOCK = ROOT / "stages/stage29/29-02a/source-lock.md"',
        '"K^2=16"',
        '"p_g=7"',
        '"q=0"',
        '"canonical divisor big and nef"',
        'if hist_rr["source_locks"]["surface_invariants"] != {',
        'degree = int(picard["target"]["degree"])',
        '"K_dot_C": degree',
        'K_K_minus_C = K2 - degree',
    ):
        req(token in n348_text, f"retired N348 retained source-lock replay drift: {token}")

    applicability = lock["applicability"]
    req(applicability["stage32_target_degree_semantics"] == "degree=K.C", "Stage32 target-degree semantics drift")
    req(applicability["source_lock_is_global_surface_data"] is True, "surface data not marked global")
    req(applicability["does_not_depend_on_full178_completion"] is True, "source-lock incorrectly tied to FULL178 completion")

    fw = lock["credit_firewall"]
    req(fw["surface_invariant_source_lock_complete"] is True, "source-lock completion flag missing")
    for key in (
        "effectivity_final_execution_released",
        "full178_rows_effectivity_classified",
        "integral_irreducible_low_genus_carrier_proved",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "merge_authorized",
    ):
        req(fw[key] is False, f"source-lock leaked credit: {key}")

    print("PASS: Stage32 final-chain 32-02 surface invariant source lock")
    print("K^2=16; p_g=7; q=0; chi(O)=8; K big and nef")
    print("Stage32 target degree semantics: degree=K.C")
    print("credit: source-lock only; no survivor/effectivity-final/carrier/receiver/theorem/endpoint credit")


if __name__ == "__main__":
    main()
