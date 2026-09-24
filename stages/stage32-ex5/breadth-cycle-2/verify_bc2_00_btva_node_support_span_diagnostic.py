#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
LIVE_STATE = ROOT / "stages" / "stage32-ex5" / "MAIN-STATE.json"
FROZEN_V4_VERIFIER = HERE / "verify_bc2_00_btva_node_support_span_diagnostic_v4.py"
HISTORICAL_V4_STATE = HERE / "archive" / "MAIN-STATE-v4-c5b22dbf.json"
HISTORICAL_V4_STATE_BLOB = "94bf17df76a06132b8a85c735ac644269126966f"


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(f"FAIL: {message}")


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    state = json.loads(LIVE_STATE.read_text(encoding="utf-8"))
    req(state["stage"] == "32EX5", "live EX5 stage drift")
    bootstrap = state["bootstrap"]
    req(bootstrap["latest_merged_pr"] == 1765,
        "latest merged EX5 PR provenance drift")
    req(bootstrap["merge_authorized"] is False,
        "historical merge authorization leaked forward")
    req(state["authority"]["state_itself_grants_mathematical_credit"] is False,
        "live EX5 state unexpectedly grants mathematical credit")
    req(state["frontier"]["FULL178_complete"] is False,
        "historical BC2 progress promoted to EX5 FULL178 credit")
    req(state["credit"]["stage32_main_credit"] is False,
        "historical BC2 progress promoted to Stage32 MAIN credit")
    req(HISTORICAL_V4_STATE.is_file() and
        git_blob_sha(HISTORICAL_V4_STATE) == HISTORICAL_V4_STATE_BLOB,
        "historical V4 compatibility state drift")

    # Preserve the exact original BC2-00 mathematical/source-lock verifier.
    # It was written against the V4 startup projection.  Replaying it against
    # a mutated current state is incorrect once EX5 legitimately advances.
    # Feed it the source-locked historical V4 projection instead; live-state
    # checks above are limited to provenance and credit firewalls.
    spec = importlib.util.spec_from_file_location("bc2_00_v4_frozen", FROZEN_V4_VERIFIER)
    req(spec is not None and spec.loader is not None, "cannot load frozen BC2-00 verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    historical_v4 = HISTORICAL_V4_STATE.read_text(encoding="utf-8")

    class StateCompatProxy:
        def read_text(self, *args, **kwargs):
            return historical_v4

    module.MAIN_STATE = StateCompatProxy()
    module.main()
    print("PASS BC2-00 historical replay against source-locked EX5 V4 projection")


if __name__ == "__main__":
    main()
