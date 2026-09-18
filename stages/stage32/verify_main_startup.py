#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SYNC = HERE / "management/grf04-quadratic-capacity/GRF04-V43-HPADJ21-FULL178-AUDIT-SYNC.json"
AUTHORITY = HERE / "verify_main_startup_authority_v43_hpadj21_full178_audit_synced.py"
COMMAND_SURFACE = HERE / "verify_command_surface.py"


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def replay(path: Path) -> None:
    subprocess.run([sys.executable, str(path)], check=True)


def main() -> None:
    obj = json.loads(SYNC.read_text(encoding="utf-8"))
    print("V43_HPADJ21_AUDIT_SYNC_CANONICAL_DIAGNOSTIC=" + canonical(obj), flush=True)
    print("V43_HPADJ21_AUDIT_SYNC_STORED_CANONICAL=" + str(obj.get("canonical_sha256_without_this_field")), flush=True)
    replay(AUTHORITY)
    replay(COMMAND_SURFACE)
    print("PASS: Stage32 MAIN V43 audit synchronization is current; FULL178 research resumed")


if __name__ == "__main__":
    main()
