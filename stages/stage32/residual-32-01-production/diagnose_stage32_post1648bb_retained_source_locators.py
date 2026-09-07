#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ST33 = ROOT / "stages" / "stage33" / "33-07"


def load(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def safe(v):
    if isinstance(v, (str, int, float, bool)) or v is None:
        return v
    if isinstance(v, list) and len(v) <= 20 and all(isinstance(x, (str,int,float,bool,type(None))) for x in v):
        return v
    if isinstance(v, dict):
        out = {}
        for k, x in v.items():
            if isinstance(x, (str,int,float,bool)) or x is None:
                out[str(k)] = x
            elif isinstance(x, list) and len(x) <= 20 and all(isinstance(y, (str,int,float,bool,type(None))) for y in x):
                out[str(k)] = x
        return out
    return {"type": type(v).__name__, "len": len(v) if hasattr(v, '__len__') else None}


def main() -> None:
    marking = load(ST33 / "stage32_picard_marking_retained.py", "s32_bb_marking_locator")
    base = load(ST33 / "picard_base_rows_retained.py", "s32_bb_base_locator")
    print(json.dumps({
        "mode": "SCRATCH_POST1648BB_RETAINED_SOURCE_LOCATORS",
        "marking": {
            "schema": marking.get("schema"),
            "source_artifact": safe(marking.get("source_artifact")),
            "stage32_aut_action_sha256": marking.get("stage32_aut_action_sha256"),
            "stage32_picard_core_sha256": marking.get("stage32_picard_core_sha256"),
        },
        "base": {
            "schema": base.get("schema"),
            "source_artifact": safe(base.get("source_artifact")),
            "top_level_keys": sorted(base.keys()),
        },
        "firewalls": {
            "runner_side_import_only": True,
            "giant_retained_payload_whole_fetch_used": False,
            "scratch_only": True
        }
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
