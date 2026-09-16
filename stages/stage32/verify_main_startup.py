#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROUTING = HERE / "management/grf04-quadratic-capacity/GRF04-V37-FULL178-INTEGER-LATTICE-ROUTING.json"

def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def main() -> None:
    obj = json.loads(ROUTING.read_text(encoding="utf-8"))
    print("V37_ROUTING_CANONICAL_DIAGNOSTIC=" + canonical(obj))
    print("V37_ROUTING_STORED_CANONICAL=" + str(obj.get("canonical_sha256_without_this_field")))
    runpy.run_path(str(HERE/"verify_main_startup_authority_v37_full178_integer_lattice_routed.py"), run_name="__main__")
    runpy.run_path(str(HERE/"verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN V37 authority unchanged; live specialist observations refreshed and 178 handoff awaits MAIN MIN-composition decision")

if __name__=="__main__":
    main()
