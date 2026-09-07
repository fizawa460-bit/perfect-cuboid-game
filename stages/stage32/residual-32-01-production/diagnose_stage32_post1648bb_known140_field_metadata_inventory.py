#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
BASE_PATH = ROOT / "stages" / "stage33" / "33-07" / "picard_base_rows_retained.py"
TOKENS = ("galois", "conjug", "complex", "field", "rational", "defined", "sqrt", "name", "label", "curve")


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def summarize(v: Any) -> Any:
    if isinstance(v, dict):
        return {"type": "dict", "len": len(v), "keys": sorted(map(str, v.keys()))[:80]}
    if isinstance(v, list):
        d = {"type": "list", "len": len(v)}
        if len(v) <= 20 and all(isinstance(x, (str, int, float, bool, type(None))) for x in v):
            d["value"] = v
        elif v:
            d["first_type"] = type(v[0]).__name__
            if isinstance(v[0], (list, tuple, dict)):
                d["first_summary"] = summarize(v[0])
        return d
    if isinstance(v, tuple):
        return summarize(list(v))
    if isinstance(v, (str, int, float, bool)) or v is None:
        s = v
        if isinstance(s, str) and len(s) > 300:
            s = s[:300] + "..."
        return {"type": type(v).__name__, "value": s}
    return {"type": type(v).__name__}


def main() -> None:
    bundle = load_retained(BASE_PATH, "s32_bb_base")
    hits = []
    text_hits = []

    def walk(v: Any, path: str, depth: int = 0) -> None:
        if depth > 7:
            return
        if isinstance(v, dict):
            for k, x in v.items():
                kp = f"{path}.{k}" if path else str(k)
                kl = str(k).lower()
                if any(tok in kl for tok in TOKENS):
                    hits.append({"path": kp, "summary": summarize(x)})
                walk(x, kp, depth + 1)
        elif isinstance(v, list):
            for i, x in enumerate(v[:250]):
                walk(x, f"{path}[{i}]", depth + 1)
        elif isinstance(v, str):
            vl = v.lower()
            if any(tok in vl for tok in ("q(i)", "sqrt", "galois", "conjug", "rational", "exceptional", "genus one", "conic")):
                text_hits.append({"path": path, "text": v[:400]})

    walk(bundle, "")
    print(json.dumps({
        "mode": "SCRATCH_POST1648BB_KNOWN140_FIELD_METADATA_INVENTORY",
        "top_level_keys": sorted(bundle.keys()),
        "keyword_path_hits": hits[:300],
        "text_hits": text_hits[:300],
        "counts": {"keyword_path_hits": len(hits), "text_hits": len(text_hits)},
        "firewalls": {
            "runner_side_import_only": True,
            "giant_retained_payload_whole_fetch_used": False,
            "repository_absence_claimed": False,
            "field_metadata_adapter_identified": False,
            "scratch_only": True
        }
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
