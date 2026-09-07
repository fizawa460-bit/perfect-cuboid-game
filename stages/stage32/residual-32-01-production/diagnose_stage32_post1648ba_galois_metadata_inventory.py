#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
MARKING_PATH = ROOT / "stages" / "stage33" / "33-07" / "stage32_picard_marking_retained.py"

TOKENS = ("galois", "conjug", "complex", "field", "rational", "defined_over", "froben", "gal_")


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def summarize(v: Any) -> Any:
    if isinstance(v, dict):
        return {"type": "dict", "len": len(v), "keys": sorted(map(str, v.keys()))[:40]}
    if isinstance(v, list):
        out = {"type": "list", "len": len(v)}
        if len(v) <= 12 and all(isinstance(x, (str, int, float, bool, type(None))) for x in v):
            out["value"] = v
        elif v:
            out["first_type"] = type(v[0]).__name__
            if isinstance(v[0], list):
                out["first_len"] = len(v[0])
        return out
    if isinstance(v, tuple):
        return summarize(list(v))
    if isinstance(v, (str, int, float, bool)) or v is None:
        s = v
        if isinstance(s, str) and len(s) > 240:
            s = s[:240] + "..."
        return {"type": type(v).__name__, "value": s}
    return {"type": type(v).__name__}


def looks_like_perm(v: Any, n: int) -> bool:
    return isinstance(v, list) and len(v) == n and all(isinstance(x, int) for x in v) and set(v) in (set(range(n)), set(range(1, n + 1)))


def main() -> None:
    marking = load_retained(MARKING_PATH, "s32_ba_marking")
    hits = []
    perm_hits = []
    text_hits = []

    def walk(v: Any, path: str, depth: int = 0) -> None:
        if depth > 8:
            return
        if isinstance(v, dict):
            for k, x in v.items():
                kp = f"{path}.{k}" if path else str(k)
                kl = str(k).lower()
                if any(tok in kl for tok in TOKENS):
                    hits.append({"path": kp, "summary": summarize(x)})
                walk(x, kp, depth + 1)
        elif isinstance(v, list):
            if looks_like_perm(v, 140):
                perm_hits.append({"path": path, "length": 140, "fixed_count": sum((x == i) or (x == i + 1) for i, x in enumerate(v))})
            elif v and all(isinstance(x, list) for x in v):
                for i, x in enumerate(v[:64]):
                    if looks_like_perm(x, 140):
                        perm_hits.append({"path": f"{path}[{i}]", "length": 140, "fixed_count": sum((y == j) or (y == j + 1) for j, y in enumerate(x))})
            for i, x in enumerate(v[:200]):
                walk(x, f"{path}[{i}]", depth + 1)
        elif isinstance(v, str):
            vl = v.lower()
            if any(tok in vl for tok in ("galois", "conjug", "q(i)", "sqrt", "rational")):
                text_hits.append({"path": path, "text": v[:300]})

    walk(marking, "")
    # Remove the known geometric automorphism permutations from the generic permutation inventory.
    filtered_perm_hits = [x for x in perm_hits if not x["path"].startswith("aut_action.permutations_1based")]

    print(json.dumps({
        "mode": "SCRATCH_POST1648BA_GALOIS_METADATA_INVENTORY",
        "retained_marking_top_level_keys": sorted(marking.keys()),
        "keyword_path_hits": hits[:200],
        "non_autaction_140_permutation_hits": filtered_perm_hits[:200],
        "text_hits": text_hits[:200],
        "counts": {
            "keyword_path_hits": len(hits),
            "non_autaction_140_permutation_hits": len(filtered_perm_hits),
            "text_hits": len(text_hits),
        },
        "firewalls": {
            "runner_side_import_only": True,
            "giant_retained_payload_whole_fetch_used": False,
            "repository_absence_claimed": False,
            "galois_action_identified": False,
            "scratch_only": True,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
