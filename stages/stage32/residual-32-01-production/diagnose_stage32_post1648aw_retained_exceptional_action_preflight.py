#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
sys.path.insert(0, str(HERE))
from pairing_prefix_engine import close_permutation_group  # noqa: E402


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def cycle_type(perm: tuple[int, ...], subset: list[int]) -> list[int]:
    S = set(subset)
    if {perm[i] for i in subset} != S:
        raise ValueError("generator does not preserve requested subset")
    unseen = set(subset)
    out = []
    while unseen:
        a = min(unseen)
        cur = a
        n = 0
        while cur in unseen:
            unseen.remove(cur)
            n += 1
            cur = perm[cur]
        out.append(n)
    return sorted(out)


def orbit_partition(subset: list[int], group: list[tuple[int, ...]]) -> list[list[int]]:
    S = set(subset)
    unseen = set(subset)
    out = []
    while unseen:
        a = min(unseen)
        orb = {g[a] for g in group}
        if not orb <= S:
            raise ValueError("orbit leaves subset")
        out.append(sorted(orb))
        unseen -= orb
    return sorted(out, key=lambda x: (len(x), x))


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_aw_marking")
    aut = marking["aut_action"]
    perms = [tuple(int(x) - 1 for x in p) for p in aut["permutations_1based"]]
    # close_permutation_group expects the retained 1-based form itself.
    group = close_permutation_group(aut["permutations_1based"])
    normal = list(range(92))
    exceptional = list(range(92, 140))
    out = {
        "mode": "SCRATCH_POST1648AW_RETAINED_EXCEPTIONAL_ACTION_PREFLIGHT",
        "marking_top_level_keys": sorted(marking.keys()),
        "aut_action_keys": sorted(aut.keys()),
        "stored_generator_count": len(perms),
        "permutation_degree": len(perms[0]) if perms else 0,
        "closed_group_order": len(group),
        "normal_orbits_1based": [[i + 1 for i in o] for o in orbit_partition(normal, group)],
        "exceptional_orbits_1based": [[i + 1 for i in o] for o in orbit_partition(exceptional, group)],
        "generator_cycle_types_on_exceptional": [cycle_type(p, exceptional) for p in perms],
        "generator_fixed_exceptional_counts": [sum(p[i] == i for i in exceptional) for p in perms],
        "generator_exceptional_images_first8_1based": [[p[i] + 1 for i in exceptional[:8]] for p in perms],
        "non_payload_aut_scalars": {
            k: v for k, v in aut.items()
            if k != "permutations_1based" and isinstance(v, (str, int, float, bool, type(None)))
        },
        "firewalls": {"scratch_only": True, "retained_payload_emitted": False, "semantic_node_matching_obtained": False},
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
