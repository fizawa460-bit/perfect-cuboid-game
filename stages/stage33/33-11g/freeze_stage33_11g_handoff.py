#!/usr/bin/env python3
"""Freeze the merged and hostile-reaudited 33-11f handoff for 33-11g."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
OUT = HERE / "stage33-11g-source-lock.json"
D_SHA = "b45da57ac9b04b744dbdc44a69b80cc3acca42c30e62db6351903d6be3aafc4d"
E_SHA = "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426"
F_SHA = "c7ba9a5a4a9475830e62276292abcdb89deb729a6aecab2c0b6f48a71a65f6e4"
F_SOURCE_SHA = "3c493c5863a1506e48622ec9180119b6b80f5ee0642fe20515916749b3138957"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical source mismatch: {path}")
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not args.write:
        lock = json.loads(OUT.read_text(encoding="utf-8"))
        body = dict(lock)
        claimed = body.pop("canonical_sha256")
        if csha(body) != claimed:
            raise SystemExit("recorded 33-11g source lock hash mismatch")
        print("STAGE33_11G_SOURCE_LOCK=PASS")
        print("SOURCE_LOCK_SHA256=" + claimed)
        return

    d = load_checked(S33 / "33-11d" / "stage33-11d-prime-refinement-certificate.json", D_SHA)
    e = load_checked(S33 / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json", E_SHA)
    f = load_checked(S33 / "33-11f" / "stage33-11f-26-column-exact-closure-certificate.json", F_SHA)
    f_source = load_checked(S33 / "33-11f" / "stage33-11f-source-lock.json", F_SOURCE_SHA)
    controller = json.loads((S33 / "controller.json").read_text(encoding="utf-8"))
    s11 = next(x for x in controller["repair_children"] if x["id"] == "33-11")
    if controller["schema"] != "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V25_STAGE33_11F_MAIN_WRITEBACK":
        raise SystemExit("pre-exit controller schema moved")
    if s11["connecting_columns_exact_main"] != 26 or s11["connecting_columns_exact_audited"] != 0:
        raise SystemExit("pre-exit MAIN/audited boundary moved")

    lock = {
        "schema": "STAGE33_11G_AUDITED_HANDOFF_V1",
        "stage": "33-11g",
        "merged_stage33_11f": {
            "pr": 1458,
            "repaired_head": "70f2a7c1322cf727b5bd22bd9131bf599f886608",
            "merge_commit": "6bc8b41b4c927a89c34336edbd1002f0a301d0bf",
            "certificate_sha256": F_SHA,
            "source_lock_sha256": F_SOURCE_SHA,
            "authoritative_main_workflow_run": 33218516451,
            "controller_only_repair_runs": [33219673170, 33219673196, 33219673173],
        },
        "hostile_reaudit": {
            "review_id": 5055777323,
            "reviewed_head": "70f2a7c1322cf727b5bd22bd9131bf599f886608",
            "verdict": "PASS_STAGE33_11F_26_COLUMN_EXACT_CLOSURE",
            "submitted_at": "2026-08-28T23:15:37Z",
            "mathematical_counterexample_found": False,
            "controller_only_prior_failure_repaired": True,
        },
        "audited_prerequisites": {
            "stage33_11d": {
                "pr": 1455,
                "audited_head": "1e5612d92586f157acbd334506e99d2642a409f7",
                "certificate_sha256": d["canonical_sha256"],
                "verdict": "PASS_STAGE33_11D_CARRIER_PRIME_REFINEMENT",
            },
            "stage33_11e": {
                "pr": 1457,
                "audited_head": "433dc8f644ed173555c261fe1742e32851611ea9",
                "certificate_sha256": e["canonical_sha256"],
                "verdict": "PASS_STAGE33_11E_PRIME_LEVEL_GALOIS_TRANSPORT",
            },
        },
        "exact_inputs": {
            "carrier_prime_refinement": d["summary"],
            "prime_level_galois_transport": e["summary"],
            "main_26_column_closure": f["summary"],
            "source_action_names": f_source["exact_source_actions"]["action_names"],
            "source_action_matrices_sha256": f_source["exact_source_actions"]["matrices_sha256"],
            "stage33_10_absolute_receiver": f["absolute_receiver"],
        },
        "pre_exit_controller": {
            "schema": controller["schema"],
            "status": s11["status"],
            "exact_main": s11["connecting_columns_exact_main"],
            "exact_audited": s11["connecting_columns_exact_audited"],
            "audit_required": s11["audit_required"],
            "audit_passed": s11["audit_passed"],
            "unit_closed": s11["unit_closed"],
        },
        "firewalls_at_entry": {
            "stage33_12_released": False,
            "stage33_08_released": False,
            "stage33_07_closed": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
    }
    lock["canonical_sha256"] = csha(lock)
    OUT.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("STAGE33_11G_SOURCE_LOCK=PASS")
    print("SOURCE_LOCK_SHA256=" + lock["canonical_sha256"])


if __name__ == "__main__":
    main()
