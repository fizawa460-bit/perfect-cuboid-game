#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "management/grf04-quadratic-capacity/GRF04-V42-HPADJ21-FULL178-MAIN-BOUND-REPLACEMENT.json"
AUTHORITY = HERE / "verify_main_startup_authority_v42_hpadj21_full178_bound_consumed.py"
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
    obj = json.loads(RECEIPT.read_text(encoding="utf-8"))
    print("V42_HPADJ21_REPLACEMENT_CANONICAL_DIAGNOSTIC=" + canonical(obj), flush=True)
    print("V42_HPADJ21_REPLACEMENT_STORED_CANONICAL=" + str(obj.get("canonical_sha256_without_this_field")), flush=True)
    replay(AUTHORITY)
    replay(COMMAND_SURFACE)
    print("PASS: Stage32 MAIN V42 HPADJ21 replacement projection is current; hostile reaudit required")


if __name__ == "__main__":
    main()
