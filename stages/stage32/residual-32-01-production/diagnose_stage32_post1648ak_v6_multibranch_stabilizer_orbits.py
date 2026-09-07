#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STAGE33_07 = ROOT / "stages" / "stage33" / "33-07"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def compose_perm(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def close_permutation_group(permutations_1based: list[list[int]]) -> list[tuple[int, ...]]:
    gens = [tuple(int(v) - 1 for v in p) for p in permutations_1based]
    n = len(gens[0])
    if not all(len(g) == n and sorted(g) == list(range(n)) for g in gens):
        raise ValueError("invalid retained permutation generator")
    identity = tuple(range(n))
    seen = {identity}
    queue = [identity]
    while queue:
        cur = queue.pop()
        for gen in gens:
            nxt = compose_perm(gen, cur)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return sorted(seen)


def permute_pairings(pairings: tuple[int, ...], permutation: tuple[int, ...]) -> tuple[int, ...]:
    inv = [0] * len(permutation)
    for i, j in enumerate(permutation):
        inv[j] = i
    return tuple(pairings[inv[j]] for j in range(len(permutation)))


def orbit_partition(indices: set[int], group: list[tuple[int, ...]]) -> list[list[int]]:
    out = []
    unseen = set(indices)
    while unseen:
        seed = min(unseen)
        orb = {g[seed] for g in group}
        if not orb <= indices:
            raise ValueError("orbit leaves requested index population")
        out.append(sorted(orb))
        unseen -= orb
    return sorted(out, key=lambda x: (len(x), x))


def exact_r_dp(masses: list[int], need: int) -> dict[int, int]:
    inf = 10**9
    dp = {(0, 0): 0}
    for m in masses:
        if m == 0:
            opts = [(0, 0, 0)]
        elif m == 1:
            opts = [(0, 0, 1), (0, 1, 1)]
        else:
            opts = [(0, 0, 1)]
            for t in range(m + 1):
                b = m if t == m else max(2, t + 1)
                opts.append((1, t, b))
        nxt = {}
        for (r0, t0), b0 in dp.items():
            for dr, dt, db in opts:
                key = (r0 + dr, min(need, t0 + dt))
                val = b0 + db
                if val < nxt.get(key, inf):
                    nxt[key] = val
        dp = nxt
    return {r: b for (r, t), b in dp.items() if t == need}


def main() -> None:
    marking = load_retained(STAGE33_07 / "stage32_picard_marking_retained.py", "s32_ak_marking")
    gens = marking["aut_action"]["permutations_1based"]
    group = close_permutation_group(gens)
    if len(group) != 1536:
        raise ValueError(f"Aut group order moved: {len(group)}")

    v6 = json.loads(V6.read_text())
    pairings = tuple(int(x) for x in v6["witness"]["all140_pairings"])
    if len(pairings) != 140:
        raise ValueError("V6 all140 width moved")
    masses = list(pairings[92:])
    if sum(masses) != 266 or sum(x > 0 for x in masses) != 47:
        raise ValueError("V6 exceptional vector moved")

    normal_orbits = orbit_partition(set(range(92)), group)
    exceptional_orbits = orbit_partition(set(range(92, 140)), group)

    stabilizer = [g for g in group if permute_pairings(pairings, g) == pairings]
    if not stabilizer:
        raise ValueError("V6 stabilizer unexpectedly empty")
    for g in stabilizer:
        if any(g[92 + i] < 92 for i in range(48)):
            raise ValueError("V6 stabilizer mixes exceptional and normal curves")

    units = [i for i, m in enumerate(masses) if m == 1]
    nonunit = [i for i, m in enumerate(masses) if m > 1]
    need = 47
    triples = []
    for comb in combinations(nonunit, 3):
        capacity = len(units) + sum(masses[i] for i in comb)
        if capacity >= need:
            triples.append(tuple(sorted(comb)))
    if len(triples) != 65:
        raise ValueError(f"exactly-three candidate count moved: {len(triples)}")

    candidate_set = set(triples)

    def image_triple(tri: tuple[int, int, int], g: tuple[int, ...]) -> tuple[int, int, int]:
        out = tuple(sorted(g[92 + i] - 92 for i in tri))
        if out not in candidate_set:
            raise ValueError("stabilizer does not preserve exactly-three candidate set")
        return out

    unseen = set(triples)
    triple_orbits = []
    while unseen:
        seed = min(unseen)
        orb = {image_triple(seed, g) for g in stabilizer}
        triple_orbits.append(sorted(orb))
        unseen -= orb
    triple_orbits.sort(key=lambda orb: (orb[0], len(orb)))

    rdp = exact_r_dp(masses, need)
    pareto = [
        {
            "multibranch_node_count": r,
            "minimum_total_normalization_preimages": rdp[r],
            "minimum_branch_excess_over_47_met_nodes": rdp[r] - 47,
        }
        for r in sorted(rdp)
    ]

    result = {
        "full_aut_group_order": len(group),
        "v6_stabilizer_order": len(stabilizer),
        "normal_curve_aut_orbits": [
            {"size": len(o), "known140_labels_1based": [i + 1 for i in o]}
            for o in normal_orbits
        ],
        "exceptional_curve_aut_orbit_sizes": [len(o) for o in exceptional_orbits],
        "exactly_three_multibranch_candidate_count": len(triples),
        "exactly_three_candidate_orbit_count_under_v6_stabilizer": len(triple_orbits),
        "exactly_three_orbit_representatives": [
            {
                "exceptional_labels_1based": [i + 1 for i in orb[0]],
                "masses": [masses[i] for i in orb[0]],
                "capacity_with_nine_unit_nodes": len(units) + sum(masses[i] for i in orb[0]),
                "orbit_size": len(orb),
            }
            for orb in triple_orbits
        ],
        "r_conditioned_branch_pareto": pareto,
        "firewalls": {
            "scratch_only": True,
            "does_not_identify_boundary_orbit_without_source_family_adapter": True,
            "does_not_materialize_carrier": True,
            "does_not_exclude_Q602_or_O210": True,
        },
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
