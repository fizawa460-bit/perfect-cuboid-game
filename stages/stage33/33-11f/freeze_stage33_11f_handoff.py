#!/usr/bin/env python3
"""Freeze audited 33-11e, Stage33-10 receiver, and exact source actions."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
OUT = HERE / "stage33-11f-source-lock.json"
E_CERT = "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426"
BLOCK_CERT = "851628f8ec5613cbee0d0bdd02135a756d1dc48403b3bc79ec1e9a8bf6ce80a3"
PROFILE_CERT = "6856ec7defea97732ea443d351d9283ef19e386e13c4c8b90a0d1545bd135390"
RECEIVER_CERT = "4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f"
ACTION_NAMES = ["sign_a1", "sign_a2", "sign_a3", "sign_b1", "sign_b2", "sign_b3", "sign_c", "swap12", "swap13"]


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_checked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock mismatch: {path}")
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("remaining_block_certificate", type=Path, nargs="?")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not args.write:
        lock = json.loads(OUT.read_text(encoding="utf-8"))
        body = dict(lock)
        claimed = body.pop("canonical_sha256")
        if csha(body) != claimed:
            raise SystemExit("recorded 33-11f source lock hash mismatch")
        print("STAGE33_11F_SOURCE_LOCK=PASS")
        print("SOURCE_LOCK_SHA256=" + claimed)
        return
    if args.remaining_block_certificate is None:
        raise SystemExit("--write requires frozen remaining-block certificate")

    e = load_checked(S33 / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json", E_CERT)
    receiver = load_checked(S33 / "33-10" / "handoff.json", RECEIVER_CERT)
    blocks = load_checked(args.remaining_block_certificate, BLOCK_CERT)

    profile_path = S33 / "33-11" / "profile_stage33_11_equivariant_forced_zero_blocks.py"
    ns = {"__name__": "__main__", "__file__": str(profile_path)}
    exec(compile(profile_path.read_text(encoding="utf-8"), str(profile_path), "exec"), ns)
    profile = ns["cert"]
    actions = [[[int(x) & 1 for x in row] for row in matrix] for matrix in ns["source_actions"]]
    if profile["canonical_sha256"] != PROFILE_CERT or len(actions) != 9:
        raise SystemExit("source action/profile lock moved")
    if any(len(matrix) != 26 or any(len(row) != 26 for row in matrix) for matrix in actions):
        raise SystemExit("source action shape moved")

    lock = {
        "schema": "STAGE33_11F_AUDITED_HANDOFF_V1",
        "stage": "33-11f",
        "audited_stage33_11e": {
            "pr": 1457,
            "merged_commit": "26e28cc6",
            "audited_head": "433dc8f644ed173555c261fe1742e32851611ea9",
            "hostile_audit_verdict": "PASS_STAGE33_11E_PRIME_LEVEL_GALOIS_TRANSPORT",
            "certificate_sha256": E_CERT,
            "workflow_run": 33217020140,
            "repair_required": False,
            "advance_to_33_11f": True,
        },
        "stage33_10_absolute_receiver": {
            "handoff_sha256": RECEIVER_CERT,
            "status": receiver["status"],
            "exact_receiver": receiver["exact_receiver"],
            "exit_condition": receiver["exit_condition"],
        },
        "frozen_cyclic_partition": {
            "remaining_block_certificate_sha256": BLOCK_CERT,
            "equivariant_profile_sha256": PROFILE_CERT,
            "smallest_exact_directions_1based": [2, 3, 24, 25, 26],
            "remaining_block_records": blocks["remaining_block_records"],
        },
        "exact_source_actions": {
            "coefficient_field": "F2",
            "dimension": 26,
            "action_names": ACTION_NAMES,
            "matrices": actions,
            "matrices_sha256": csha(actions),
            "remote_cas_used": False,
            "smith_form_used_for_target": False,
        },
        "summary": {
            "generator_prime_level_zero_coverage": e["summary"]["working_generator_coverage"],
            "unresolved_prime_transports": e["summary"]["unresolved_prime_transports"],
            "named_source_directions": 26,
            "cyclic_source_submodules": profile["cyclic_source_submodules"]["distinct_named_cyclic_submodules"],
            "exact_audited_connecting_progress_at_entry": "0/26",
        },
        "firewalls": {
            "stage33_11_closed_exact": False,
            "stage33_12_released": False,
            "stage33_08_released": False,
            "stage33_07_closed": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
    }
    lock["canonical_sha256"] = csha(lock)
    OUT.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("STAGE33_11F_SOURCE_LOCK=PASS")
    print("SOURCE_LOCK_SHA256=" + lock["canonical_sha256"])


if __name__ == "__main__":
    main()
