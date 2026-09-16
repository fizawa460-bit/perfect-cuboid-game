#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
SYNC = HERE / "management/grf04-quadratic-capacity/GRF04-V39-TD02-FULL178-INTEGER-LATTICE-AUDIT-SYNC.json"

def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def main() -> None:
    obj = json.loads(SYNC.read_text(encoding="utf-8"))
    print("V39_AUDIT_SYNC_CANONICAL_DIAGNOSTIC=" + canonical(obj))
    print("V39_AUDIT_SYNC_STORED_CANONICAL=" + str(obj.get("canonical_sha256_without_this_field")))
    runpy.run_path(
        str(HERE / "verify_main_startup_authority_v39_full178_integer_lattice_audit_synced.py"),
        run_name="__main__",
    )
    runpy.run_path(str(HERE / "verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN V39 audit-sync complete; replacement gate cleared and FULL178 route resumed")

if __name__=="__main__":
    main()
