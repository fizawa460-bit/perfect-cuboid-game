#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ST33 = ROOT / "stages" / "stage33" / "33-07"
MARKING_PATH = ST33 / "stage32_picard_marking_retained.py"


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def perm0(p1: list[int]) -> tuple[int, ...]:
    return tuple(int(x) - 1 for x in p1)


def compose(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    # a after b
    return tuple(a[b[i]] for i in range(len(a)))


def order(p: tuple[int, ...]) -> int:
    n = len(p)
    seen = [False] * n
    out = 1
    for i in range(n):
        if seen[i]:
            continue
        j = i
        k = 0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            k += 1
        if k:
            out = out * k // gcd(out, k)
    return out


def cycle_profile(p: tuple[int, ...]) -> dict[str, int]:
    n = len(p)
    seen = [False] * n
    prof: dict[str, int] = {}
    for i in range(n):
        if seen[i]:
            continue
        j = i
        k = 0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            k += 1
        prof[str(k)] = prof.get(str(k), 0) + 1
    return prof


def close(gens: list[tuple[int, ...]], cap: int = 200000) -> list[tuple[int, ...]]:
    if not gens:
        return []
    ident = tuple(range(len(gens[0])))
    group = {ident}
    frontier = [ident]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = compose(g, x)
            if y not in group:
                group.add(y)
                frontier.append(y)
                if len(group) > cap:
                    raise RuntimeError(f"group cap exceeded: {cap}")
    return sorted(group)


def bounded_meta(v: object) -> object:
    if v is None or isinstance(v, (bool, int, float)):
        return v
    if isinstance(v, str):
        return v if len(v) <= 240 else {"type": "str", "length": len(v), "prefix": v[:120]}
    if isinstance(v, list):
        if len(v) <= 16 and all(isinstance(x, (str, int, bool)) for x in v):
            return v
        return {"type": "list", "length": len(v), "item_types": sorted({type(x).__name__ for x in v})}
    if isinstance(v, dict):
        return {"type": "dict", "keys": sorted(map(str, v.keys())), "length": len(v)}
    return {"type": type(v).__name__}


def main() -> None:
    marking = load_retained(MARKING_PATH, "s32_aq_marking")
    aut = marking.get("aut_action")
    if not isinstance(aut, dict):
        raise ValueError("retained marking aut_action missing or non-dict")
    p_raw = aut.get("permutations_1based")
    if not isinstance(p_raw, list) or not p_raw:
        raise ValueError("aut_action.permutations_1based missing")
    gens = [perm0(p) for p in p_raw]
    n = len(gens[0])
    if any(len(g) != n for g in gens):
        raise ValueError("generator permutation lengths differ")
    group = close(gens)

    generator_summaries = [
        {
            "index_1based": i + 1,
            "order": order(g),
            "cycle_profile": cycle_profile(g),
        }
        for i, g in enumerate(gens)
    ]

    # Report only bounded metadata. The retained payload itself is never emitted.
    out = {
        "mode": "SCRATCH_POST1648AQ_RESIDUAL_G_ACTION_PREFLIGHT",
        "retained_marking_path": str(MARKING_PATH.relative_to(ROOT)),
        "top_level_keys": sorted(marking.keys()),
        "top_level_metadata": {k: bounded_meta(v) for k, v in marking.items() if k != "hperp_text"},
        "hperp_text_length": len(marking.get("hperp_text", "")),
        "aut_action_keys": sorted(aut.keys()),
        "aut_action_metadata": {k: bounded_meta(v) for k, v in aut.items() if k != "permutations_1based"},
        "permutation_degree": n,
        "stored_generator_count": len(gens),
        "stored_generator_summaries": generator_summaries,
        "closed_group_order": len(group),
        "closed_group_element_order_histogram": {},
        "firewalls": {
            "scratch_only": True,
            "retained_payload_emitted": False,
            "residual_G_semantic_identification_granted": False,
            "Q602_excluded": False,
            "O210_excluded": False,
        },
    }
    hist: dict[str, int] = {}
    for g in group:
        o = str(order(g))
        hist[o] = hist.get(o, 0) + 1
    out["closed_group_element_order_histogram"] = hist
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
