#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

AUDIT_HEAD = "b28adadc95776762754e1415a0ecab0da1d4cd8e"
ARCHIVE_HEAD = "ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11"

AUDIT_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-Z33-SPAN5-HYPERPLANE-CONTACT-EQUALITY-20260919.md":
        "65656518d30f69ab3a4a892c8d4ae1d5ed72670e",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_z33_span5_hyperplane_contact.py":
        "7ba0b4eb4fffda7fe1b88b958d952276c8af271b",
    "stages/stage32/final-chain/32-03-multibranch/STATE.json":
        "7fa7b24fc8e28727ff2c63d893128b9cf2099ba5",
}

ARCHIVE_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-FINITE-REDUCTION.md":
        "08eee3d3492db710c7161fdf17ce1eca35e50413",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-FINITE-REDUCTION-CERTIFICATE.json":
        "b6035b2e525a08ab0fc028e1e1f81519548e1a5b",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-AUT-ORBIT-CLASSIFICATION.md":
        "c3bcc580b5bd43b7805c7227c7420445f14c4b8c",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-AUT-ORBIT-CERTIFICATE.json":
        "3bc4453affce96e87a60864c99f745bb4c28c794",
}


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit("FAIL: " + msg)


def git_head(root: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
    ).strip()


def blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def check_root(root: Path, expected_head: str, locks: dict[str, str], label: str) -> None:
    req(root.is_dir(), f"{label} root missing")
    req(git_head(root) == expected_head, f"{label} HEAD mismatch")
    for rel, expected in locks.items():
        p = root / rel
        req(p.is_file(), f"{label} missing {rel}")
        req(blob_sha1(p) == expected, f"{label} blob mismatch {rel}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit-root", required=True)
    ap.add_argument("--archive-root", required=True)
    args = ap.parse_args()

    check_root(Path(args.audit_root), AUDIT_HEAD, AUDIT_LOCKS, "audited predecessor")
    check_root(Path(args.archive_root), ARCHIVE_HEAD, ARCHIVE_LOCKS, "historical archive")

    here = Path(__file__).resolve().parents[2]
    state_path = here / "STATE.json"
    req(state_path.is_file(), "current compact STATE missing")
    state = json.loads(state_path.read_text())
    rb = state.get("restart_boundary", {})
    req(rb.get("audited_predecessor_head") == AUDIT_HEAD, "STATE predecessor head")
    req(rb.get("historical_archive_head") == ARCHIVE_HEAD, "STATE archive head")
    req(state.get("current_node") == "MB104", "current node")
    active_leaf = state.get("next_obligation", {}).get("active_leaf")
    req(isinstance(active_leaf, str) and active_leaf.startswith("MB104-"),
        "active leaf must remain inside MB104")

    for k, v in state["credit_firewall"].items():
        req(v is False, "credit firewall " + k)

    print("PASS: compact MB104 restart boundary")
    print("audited predecessor:", AUDIT_HEAD)
    print("historical archive:", ARCHIVE_HEAD)
    print("active leaf:", active_leaf)
    print("credit: zero")


if __name__ == "__main__":
    main()
