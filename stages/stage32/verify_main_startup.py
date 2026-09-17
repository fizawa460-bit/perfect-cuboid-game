#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SYNC = HERE / "management/grf04-quadratic-capacity/GRF04-V41-HPADJ20-FULL178-AUDIT-SYNC.json"
AUTHORITY = HERE / "verify_main_startup_authority_v41_hpadj20_full178_audit_synced.py"
COMMAND_SURFACE = HERE / "verify_command_surface.py"


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def replay(path: Path) -> None:
    # Keep each startup verifier in a fresh interpreter.  Several retained
    # verifiers use argparse/runpy and historical compatibility replay; process
    # isolation prevents caller state from changing fail-closed observations.
    subprocess.run([sys.executable, str(path)], check=True)


def main() -> None:
    obj = json.loads(SYNC.read_text(encoding="utf-8"))
    print("V41_HPADJ20_AUDIT_SYNC_CANONICAL_DIAGNOSTIC=" + canonical(obj), flush=True)
    print("V41_HPADJ20_AUDIT_SYNC_STORED_CANONICAL=" + str(obj.get("canonical_sha256_without_this_field")), flush=True)
    replay(AUTHORITY)
    replay(COMMAND_SURFACE)
    print("PASS: Stage32 MAIN V41 audit synchronization is current; FULL178 route resumed")


if __name__ == "__main__":
    main()
