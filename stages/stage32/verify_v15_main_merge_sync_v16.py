#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
RECEIPT = HERE / "management/post-cut195-replacement-head-hostile-pass-merge-sync-20260912.json"

AUDITED_HEAD = "fdc372e1666e1176d80953b6303b13b240da84c5"
AUDITED_TREE = "fccba090fb1330a0167dde476440254bda43db3f"
AUDIT_REVIEW = 5185987769
MERGE_COMMIT = "e4d3b8b83626526ffeccdbd9c956081735fe1a6e"
MERGE_TREE = "fccba090fb1330a0167dde476440254bda43db3f"
V15_STATE_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
V15_STATE_CANONICAL = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
V15_STARTUP_VERIFIER_BLOB = "fa620931aa0addc7d98cdf4208be2d9b4ee75c49"
V15_CROSS_LANE_VERIFIER_BLOB = "bcae62bcbdcaa08c389180babb9a623a4dd67bb6"
V16_STATE_BLOB = "514fd4d3e4ba8ab5e33b0ff9537350e82a123ce0"
V16_STATE_CANONICAL = "23918007afdf7b01c7736dfb938d3d51261d3f79939627df7737fa7de12ba882"
RECEIPT_BLOB = "a38be20bf4db3342eb0fcea91c6f8aed50b03b54"
RECEIPT_CANONICAL = "9c5ef3da7907eb37b36e30d2feb7d47194d8765f8fac4cf72b1f102159190f2c"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(isinstance(obj, dict), f"expected object: {path}")
    return obj

def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()

def replay(path: Path, cwd: Path, label: str) -> None:
    proc = subprocess.run([sys.executable, str(path)], cwd=cwd, text=True, capture_output=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise SystemExit(f"FAIL: {label}")
    print(proc.stdout, end="")

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-main-v15-root", type=Path, required=True)
    args = ap.parse_args()
    audited = args.audited_main_v15_root.resolve()

    req(git(audited, "rev-parse", "HEAD") == AUDITED_HEAD, "audited V15 exact head drift")
    req(git(audited, "rev-parse", "HEAD^{tree}") == AUDITED_TREE, "audited V15 tree drift")
    req(git(ROOT, "rev-parse", f"{MERGE_COMMIT}^{tree}") == MERGE_TREE, "merged main tree drift")
    req(AUDITED_TREE == MERGE_TREE, "audited V15 tree differs from squash-merge tree")
    subprocess.check_call(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", MERGE_COMMIT, "HEAD"])

    v15_state_path = audited / "stages/stage32/MAIN-STATE.json"
    v15_startup = audited / "stages/stage32/verify_main_startup_authority_v15.py"
    v15_cross = audited / "stages/stage32/proof/verify_cross_lane_demands.py"
    req(git_blob(v15_state_path) == V15_STATE_BLOB, "audited V15 MAIN state blob drift")
    req(git_blob(v15_startup) == V15_STARTUP_VERIFIER_BLOB, "audited V15 startup verifier blob drift")
    req(git_blob(v15_cross) == V15_CROSS_LANE_VERIFIER_BLOB, "audited V15 cross-lane verifier blob drift")
    old = load(v15_state_path)
    req(old["canonical_sha256_without_this_field"] == V15_STATE_CANONICAL, "audited V15 canonical field drift")
    req(canonical(old) == V15_STATE_CANONICAL, "audited V15 canonical drift")
    req(old["authority_sync"]["cut195_post_sync_reaudit_status"] == "PENDING",
        "audited V15 tree is not the pre-external-audit authority projection")

    replay(v15_startup, audited, "audited V15 startup authority replay failed")
    replay(v15_cross, audited, "audited V15 cross-lane replay failed")

    req(git_blob(STATE) == V16_STATE_BLOB, "current V16 MAIN state blob drift")
    current = load(STATE)
    req(current["canonical_sha256_without_this_field"] == V16_STATE_CANONICAL,
        "current V16 canonical field drift")
    req(canonical(current) == V16_STATE_CANONICAL, "current V16 canonical drift")

    req(git_blob(RECEIPT) == RECEIPT_BLOB, "V15 hostile-audit merge-sync receipt blob drift")
    receipt = load(RECEIPT)
    req(receipt["canonical_sha256_without_this_field"] == RECEIPT_CANONICAL,
        "merge-sync receipt canonical field drift")
    req(canonical(receipt) == RECEIPT_CANONICAL, "merge-sync receipt canonical drift")
    req(receipt["audited_boundary"]["exact_head"] == AUDITED_HEAD, "receipt audited head drift")
    req(receipt["audited_boundary"]["hostile_reaudit_review_id"] == AUDIT_REVIEW,
        "receipt hostile re-audit review drift")
    req(receipt["audited_boundary"]["hostile_reaudit_status"] == "PASS",
        "receipt hostile re-audit not PASS")
    req(receipt["merge_boundary"]["merge_commit"] == MERGE_COMMIT, "receipt merge commit drift")
    req(receipt["merge_boundary"]["audited_head_tree_equals_merge_commit_tree"] is True,
        "receipt tree-equivalence flag false")
    req(current["authority_sync"]["cut195_post_sync_reaudit_status"] == "PASS",
        "current authority did not consume V15 external audit")
    req(current["authority_sync"]["cut195_post_sync_reaudit_review_id"] == AUDIT_REVIEW,
        "current authority audit review drift")
    req(current["authority_sync"]["cut195_synchronized_head_hostile_audited"] is True,
        "current authority synchronized audit flag false")
    req(current["current_exact_frontier"]["full178_numerical_census_complete"] is False,
        "FULL178 incorrectly closed")
    req(current["current_exact_frontier"]["cut196_main_pruning_credit"] is False,
        "CUT196 gained unauthorized MAIN credit")
    req(current["firewalls"]["merge_authorized"] is False, "merge self-authorized")

    print("PASS_STAGE32_V15_HOSTILE_AUDIT_MERGE_SYNC_V16")
    print(f"audited_head={AUDITED_HEAD} audited_tree={AUDITED_TREE}")
    print(f"merge_commit={MERGE_COMMIT} merge_tree={MERGE_TREE}")
    print("tree_equivalent=true full178=ACTIVE_INCOMPLETE cut196_main_credit=false")

if __name__ == "__main__":
    main()
