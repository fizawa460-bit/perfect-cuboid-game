#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
sys.path.insert(0, str(HERE))
from pairing_prefix_engine import close_permutation_group  # noqa: E402

AV = HERE / "diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py"
ZD = HERE / "diagnose_stage32_post1648aw_boundary_Z_hyperplane_blocks.py"
CELL = HERE / "diagnose_stage32_post1648aw_Z_Wpair_support_cells.py"


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def run_json(path: Path) -> dict:
    p = subprocess.run([sys.executable, "-B", str(path)], cwd=ROOT, check=True, capture_output=True, text=True)
    return json.loads(p.stdout)


def image(block: set[int], g: tuple[int, ...]) -> set[int]:
    return {g[i - 1] + 1 for i in block}


def compose(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a[b[i]] for i in range(len(a)))


def power(a: tuple[int, ...], n: int) -> tuple[int, ...]:
    r = tuple(range(len(a)))
    for _ in range(n):
        r = compose(a, r)
    return r


def block_perm(blocks: list[set[int]], g: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for b in blocks:
        ib = image(b, g)
        hits = [j for j, c in enumerate(blocks) if ib == c]
        if len(hits) != 1:
            raise ValueError(f"block image not unique: {hits}")
        out.append(hits[0])
    return tuple(out)


def subgroup_closure(gens: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    identity = tuple(range(len(gens[0])))
    out = {identity}
    changed = True
    while changed:
        changed = False
        for a in list(out):
            for b in gens:
                c = compose(a, b)
                if c not in out:
                    out.add(c)
                    changed = True
    return out


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_ay_marking")
    G = close_permutation_group(marking["aut_action"]["permutations_1based"])
    av = run_json(AV)
    zd = run_json(ZD)
    cell = run_json(CELL)
    if len(G) != 1536:
        raise ValueError(f"retained group order regression: {len(G)}")

    zparts = zd["retained"]["unordered_Z1_Z2_Z3_exact_partitions"]
    survivors = cell["support_design_survivors"]
    if len(zparts) != 1 or len(survivors) != 1:
        raise ValueError("unique coordinate design regression")
    zblocks = [set(b["exceptional_labels_1based"]) for b in zparts[0]["blocks"]]
    chosen = survivors[0]["candidate_indices_zero_based"]
    candidates = av["coordinate_W1_W2_W3_C_recovery"]["single_hyperplane_candidates"]
    wblocks = [set(candidates[i]["exceptional_labels_1based"]) for i in chosen]

    by_wp: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    kernel = []
    for g in G:
        wp = block_perm(wblocks, g)
        zp = block_perm(zblocks, g)
        by_wp[wp].append(g)
        if wp == (0, 1, 2, 3) and zp == (0, 1, 2):
            kernel.append(g)
    if len(by_wp) != 24 or {len(v) for v in by_wp.values()} != {64} or len(kernel) != 64:
        raise ValueError("quotient/kernel regression")

    identity = tuple(range(140))
    s1 = (1, 0, 2, 3)
    s2 = (0, 2, 1, 3)
    s3 = (0, 1, 3, 2)
    C1 = [g for g in by_wp[s1] if power(g, 2) == identity]
    C2 = [g for g in by_wp[s2] if power(g, 2) == identity]
    C3 = [g for g in by_wp[s3] if power(g, 2) == identity]
    if not C1 or not C2 or not C3:
        raise ValueError(f"missing involutive Coxeter lifts: {[len(C1),len(C2),len(C3)]}")

    solutions = []
    # Coxeter presentation of S4:
    # si^2=1, (s1 s2)^3=(s2 s3)^3=1, and s1 s3=s3 s1.
    for a in C1:
        commuting_c = [c for c in C3 if compose(a, c) == compose(c, a)]
        for c in commuting_c:
            for b in C2:
                if power(compose(a, b), 3) != identity:
                    continue
                if power(compose(b, c), 3) != identity:
                    continue
                L = subgroup_closure([a, b, c])
                if len(L) != 24:
                    continue
                if len(L.intersection(kernel)) != 1:
                    continue
                qimage = {block_perm(wblocks, x) for x in L}
                if len(qimage) != 24:
                    continue
                solutions.append((a, b, c, L))

    if not solutions:
        raise ValueError("no exact S4 complement found")
    solutions.sort(key=lambda x: (x[0], x[1], x[2]))
    a, b, c, L = solutions[0]

    # Exact internal semidirect-product checks.
    products = {compose(h, l) for h in kernel for l in L}
    products_rev = {compose(l, h) for h in kernel for l in L}
    if len(products) != 1536 or products != set(G) or products_rev != set(G):
        raise ValueError("H*L does not recover retained G")
    factor_pairs = {}
    for h in kernel:
        for l in L:
            g = compose(h, l)
            if g in factor_pairs:
                raise ValueError("H*L factorization not unique")
            factor_pairs[g] = (h, l)
    if len(factor_pairs) != 1536:
        raise ValueError("factorization cardinality regression")

    # The chosen complement must reproduce the exact standard S4 quotient.
    quotient_generator_perms = [block_perm(wblocks, x) for x in (a, b, c)]
    if quotient_generator_perms != [s1, s2, s3]:
        raise ValueError("chosen complement generator quotient regression")

    exceptional = list(range(93, 141))
    L_exceptional_orbits = []
    unseen = set(exceptional)
    while unseen:
        p = min(unseen)
        orb = {l[p - 1] + 1 for l in L}
        L_exceptional_orbits.append(sorted(orb))
        unseen -= orb
    L_exceptional_orbits.sort(key=lambda x: (len(x), x))

    print(json.dumps({
        "mode": "SCRATCH_POST1648AY_S4_COMPLEMENT_SPLITTING",
        "retained_group_order": len(G),
        "kernel_order": len(kernel),
        "quotient_order": len(by_wp),
        "coxeter_involutive_lift_candidate_counts": [len(C1), len(C2), len(C3)],
        "exact_S4_complement_solution_count": len(solutions),
        "chosen_complement_order": len(L),
        "chosen_complement_intersection_kernel_order": len(L.intersection(kernel)),
        "chosen_complement_WC_generator_permutations": [list(x) for x in quotient_generator_perms],
        "internal_semidirect_product_verified": True,
        "unique_H_times_S4_factorization_verified": True,
        "S4_complement_exceptional_orbit_sizes": sorted(len(x) for x in L_exceptional_orbits),
        "next_exact_route": "USE_THE_EXACT_C2_6_RT_S4_ISOMORPHISM_TO_RECOVER_A_SOURCE_NODE_STABILIZER_AND_SOLVE_THE_FULL_48_NODE_EQUIVARIANT_BIJECTION",
        "firewalls": {
            "scratch_only": True,
            "full_1536_source_to_retained_group_isomorphism_verified": False,
            "source_node_stabilizer_matched": False,
            "explicit_48_node_bijection_obtained": False,
            "v6_carrier_excluded": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False
        }
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
