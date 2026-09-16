#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "management/grf04-quadratic-capacity/GRF04-V38-TD02-FULL178-INTEGER-LATTICE-MAIN-BOUND-REPLACEMENT.json"

def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def main() -> None:
    obj = json.loads(RECEIPT.read_text(encoding="utf-8"))
    print("V38_REPLACEMENT_CANONICAL_DIAGNOSTIC=" + canonical(obj))
    print("V38_REPLACEMENT_STORED_CANONICAL=" + str(obj.get("canonical_sha256_without_this_field")))
    runpy.run_path(str(HERE/"verify_main_startup_authority_v38_full178_integer_lattice_consumed.py"), run_name="__main__")
    runpy.run_path(str(HERE/"verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN V38 consumed the hostile-audited TD02 FULL178 bound; replacement reaudit is the current stop gate")

if __name__=="__main__":
    main()
