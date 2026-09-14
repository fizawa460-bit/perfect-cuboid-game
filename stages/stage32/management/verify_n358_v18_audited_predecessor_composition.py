#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INNER = ROOT / "stages/stage32/management/verify_n358_v18_current_authority_composition.py"
SNAPSHOT = ROOT / "stages/stage32/management/MAIN-STATE-V18-N358-PRECONSUMPTION.json"

AUDITED_V18_HEAD = "152e8f92346c038aed5628d7d70063cc5c8cd9d4"
AUDITED_V18_STATE_BLOB = "48a3b18671ddd85a8b0916a8be1d9f611c38b534"
AUDITED_V18_STATE_CANONICAL = "8590ba2d6a8d9e5250f5849a5052a3abeef43884eee2e237d5372dd61f841bef"
INNER_VERIFIER_BLOB = "e441287905c35284fd33e7ede7956d3db1c4aa80"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load_locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(git_blob(path) == blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can, f"stored canonical drift {path}")
    req(canonical(obj) == can, f"canonical drift {path}")
    return obj


def exact_head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-main-v18-root", type=Path, required=True)
    ap.add_argument("--audited-n358-root", type=Path, required=True)
    args = ap.parse_args()

    v18_root = args.audited_main_v18_root.resolve()
    n358_root = args.audited_n358_root.resolve()

    req(exact_head(v18_root) == AUDITED_V18_HEAD, "audited MAIN V18 exact head drift")
    audited_state_path = v18_root / "stages/stage32/MAIN-STATE.json"
    audited_state = load_locked(audited_state_path, AUDITED_V18_STATE_BLOB, AUDITED_V18_STATE_CANONICAL)
    retained_state = load_locked(SNAPSHOT, AUDITED_V18_STATE_BLOB, AUDITED_V18_STATE_CANONICAL)
    req(retained_state == audited_state, "retained V18 snapshot differs from hostile-audited exact-head MAIN-STATE.json")

    req(git_blob(INNER) == INNER_VERIFIER_BLOB, "inner N358/V18 composition verifier blob drift")
    subprocess.run([
        sys.executable,
        str(INNER),
        "--audited-n358-root",
        str(n358_root),
    ], check=True)

    print(json.dumps({
        "verdict": "PASS_N358_V18_DIRECT_AUDITED_PREDECESSOR_IDENTITY_AND_COMPOSITION",
        "audited_main_v18_exact_head": AUDITED_V18_HEAD,
        "audited_main_v18_state_blob": AUDITED_V18_STATE_BLOB,
        "audited_main_v18_state_canonical": AUDITED_V18_STATE_CANONICAL,
        "retained_snapshot_byte_identical": True,
        "inner_composition_verifier_blob": INNER_VERIFIER_BLOB,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
