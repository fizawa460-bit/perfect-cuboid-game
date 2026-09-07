#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE_PATH = ROOT / "stages" / "stage33" / "33-07" / "picard_base_rows_retained.py"


def load(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    d = load(BASE_PATH, "s32_be_base")
    keys = [
        "schema",
        "source_head_sha",
        "source_run_id",
        "upstream_git_blob_sha1",
        "artifact_canonical_sha256",
        "canonical_sha256",
    ]
    out = {k: d.get(k) for k in keys}
    print(json.dumps({
        "mode": "SCRATCH_POST1648BE_PICARD_ACTION_SOURCE_LOCATORS",
        "locators": out,
        "has_picard_action_cc": "picard_action_cc_64x64" in d,
        "has_picard_action_ct": "picard_action_ct_64x64" in d,
        "firewalls": {
            "runner_side_import_only": True,
            "giant_retained_payload_whole_fetch_used": False,
            "cc_semantics_identified": False,
            "ct_semantics_identified": False,
            "scratch_only": True,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
