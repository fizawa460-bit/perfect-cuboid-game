#!/usr/bin/env python3
"""Network-free structural, blob, and primary-status verifier."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INDEX = HERE / "index.json"


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", "--", str(path)], cwd=ROOT, text=True).strip()


def main() -> int:
    data = json.loads(INDEX.read_text())
    errors = []
    allowed = set(data["authority_classes"])
    ids = [asset["asset_id"] for asset in data["assets"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate asset_id")

    for asset in data["assets"]:
        if asset["authority"] not in allowed:
            errors.append(f"{asset['asset_id']}: invalid authority")
        if not asset.get("limitations"):
            errors.append(f"{asset['asset_id']}: limitations required")
        primary = None
        for file in asset["files"]:
            path = ROOT / file["path"]
            if not path.is_file():
                errors.append(f"{asset['asset_id']}: missing {file['path']}")
                continue
            actual = git_blob(path)
            if actual != file["blob_sha1"]:
                errors.append(f"{asset['asset_id']}: blob mismatch {file['path']} expected={file['blob_sha1']} actual={actual}")
            if file["role"] == "primary":
                if primary is not None:
                    errors.append(f"{asset['asset_id']}: multiple primary files")
                primary = path
        if primary is None:
            errors.append(f"{asset['asset_id']}: primary file required")
        elif primary.suffix == ".json":
            primary_data = json.loads(primary.read_text())
            if primary_data.get("status") != asset["status"]:
                errors.append(f"{asset['asset_id']}: primary status mismatch")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PROOF_REPLAY_COMPLETE: {len(data['assets'])} positive assets; IDs, paths, blobs, authority classes, limitations, and primary statuses verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
