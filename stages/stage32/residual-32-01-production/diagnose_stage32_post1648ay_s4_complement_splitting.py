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

    # Exhaust ALL involutive lifts of the three standard adjacent
    # transpositions. Any S4 complement L -> G/H=S4 would map the standard
    # Coxeter generators to a triple in these three finite sets satisfying
    # the S4 Coxeter presentation.
    C1 = [g for g in by_wp[s1] if power(g, 2) == identity]
    C2 = [g for g in by_wp[s2] if power(g, 2) == identity]
    C3 = [g for g in by_wp[s3] if power(g, 2) == identity]
    if not C1 or not C2 or not C3:
        raise ValueError(f"missing involutive Coxeter lifts: {[len(C1),len(C2),len(C3)]}")

    total_triples = len(C1) * len(C2) * len(C3)
    commuting_outer_pairs = 0
    s12_braid_pairs = 0
    s23_braid_pairs = 0
    after_commuting_and_s12 = 0
    after_commuting_and_s23 = 0
    full_coxeter_triples = []

    # Coxeter presentation of S4:
    # s_i^2=1, (s1 s2)^3=(s2 s3)^3=1, s1 s3=s3 s1.
    for a in C1:
        for c in C3:
            commute = compose(a, c) == compose(c, a)
            if commute:
                commuting_outer_pairs += 1
            for b in C2:
                braid12 = power(compose(a, b), 3) == identity
                braid23 = power(compose(b, c), 3) == identity
                if c == C3[0] and braid12:
                    # Count each (a,b) once, independent of c.
                    s12_braid_pairs += 1
                if a == C1[0] and braid23:
                    # Count each (b,c) once, independent of a.
                    s23_braid_pairs += 1
                if commute and braid12:
                    after_commuting_and_s12 += 1
                if commute and braid23:
                    after_commuting_and_s23 += 1
                if commute and braid12 and braid23:
                    full_coxeter_triples.append((a, b, c))

    # Completeness: a splitting section S4 -> G sends the three standard
    # transpositions to involutive lifts in C1,C2,C3 satisfying exactly the
    # tested Coxeter relations. Thus zero full triples proves no complement.
    split = bool(full_coxeter_triples)
    if split:
        raise ValueError(f"unexpected S4 complement witness count: {len(full_coxeter_triples)}")

    print(json.dumps({
        "mode": "SCRATCH_POST1648AY_S4_EXTENSION_NONSPLITTING",
        "retained_group_order": len(G),
        "kernel_order": len(kernel),
        "quotient_order": len(by_wp),
        "quotient_identification": "FULL_S4_ON_FOUR_RECOVERED_WC_BLOCKS",
        "standard_adjacent_transpositions_zero_based": [list(s1), list(s2), list(s3)],
        "coxeter_involutive_lift_candidate_counts": [len(C1), len(C2), len(C3)],
        "coxeter_candidate_triple_count": total_triples,
        "commuting_s1_s3_lift_pair_count": commuting_outer_pairs,
        "s1_s2_order3_lift_pair_count": s12_braid_pairs,
        "s2_s3_order3_lift_pair_count": s23_braid_pairs,
        "triples_passing_commuting_and_s1s2_order3": after_commuting_and_s12,
        "triples_passing_commuting_and_s2s3_order3": after_commuting_and_s23,
        "full_coxeter_triple_count": 0,
        "extension_split": False,
        "exact_completeness_argument": "Any complement S4->G projecting isomorphically to the fixed quotient sends the three standard adjacent transpositions to involutive lifts in the three exhaustively enumerated cosets. Those lifts must satisfy (s1s2)^3=(s2s3)^3=1 and s1s3=s3s1. Exhaustive finite enumeration finds zero such triples.",
        "bounded_negative": "NO_S4_COMPLEMENT_IN_THE_RETAINED_1536_EXTENSION_OVER_THE_EXACT_WC_BLOCK_QUOTIENT",
        "interpretation": "The retained group is an exact non-split extension 1->C2^6->G->S4->1 for this recovered coordinate-block quotient; do not model G as C2^6 semidirect S4.",
        "next_exact_route": "SOURCE_LOCK_THE_EXPLICIT_PROJECTIVE_MONOMIAL_AUTOMORPHISM_LIFTS_AND_MATCH_THE_NONSPLIT_EXTENSION_COCYCLE_BEFORE_SOLVING_THE_FULL_48_NODE_EQUIVARIANT_BIJECTION",
        "firewalls": {
            "scratch_only": True,
            "non_split_claim_scope_is_retained_fixed_quotient_only": True,
            "full_1536_source_to_retained_group_isomorphism_verified": False,
            "source_extension_cocycle_matched": False,
            "explicit_48_node_bijection_obtained": False,
            "v6_carrier_excluded": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False
        }
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
