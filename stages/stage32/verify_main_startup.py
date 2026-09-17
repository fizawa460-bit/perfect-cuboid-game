#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDIDATE = HERE / "management/grf04-quadratic-capacity/GRF04-V42-HPADJ20-LOW-D-FULL-QA-HYBRID-CANDIDATE.json"

def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def main() -> None:
    obj = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    print("V42_HYBRID_CANDIDATE_CANONICAL_DIAGNOSTIC=" + canonical(obj))
    print("V42_HYBRID_CANDIDATE_STORED_CANONICAL=" + str(obj.get("canonical_sha256_without_this_field")))
    runpy.run_path(
        str(HERE / "verify_main_startup_authority_v42_hpadj20_low_d_full_qa_hybrid_candidate.py"),
        run_name="__main__",
    )
    runpy.run_path(str(HERE / "verify_command_surface.py"), run_name="__main__")
    print("PASS: Stage32 MAIN V42 hybrid candidate is retained; hostile audit is the active stop gate")

if __name__ == "__main__":
    main()
