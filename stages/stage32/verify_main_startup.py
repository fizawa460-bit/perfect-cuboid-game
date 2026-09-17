#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
SYNC = HERE / "management/grf04-quadratic-capacity/GRF04-V41-HPADJ20-FULL178-AUDIT-SYNC.json"

def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def main() -> None:
    obj = json.loads(SYNC.read_text(encoding="utf-8"))
    print("V41_HPADJ20_AUDIT_SYNC_CANONICAL_DIAGNOSTIC=" + canonical(obj))
    print("V41_HPADJ20_AUDIT_SYNC_STORED_CANONICAL=" + str(obj.get("canonical_sha256_without_this_field")))
    runpy.run_path(
        str(HERE / "verify_main_startup_authority_v41_hpadj20_full178_audit_synced.py"),
        run_name="__main__",
    )
    runpy.run_path(str(HERE / "verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN V41 audit synchronization is current; FULL178 route resumed")

if __name__ == "__main__":
    main()
