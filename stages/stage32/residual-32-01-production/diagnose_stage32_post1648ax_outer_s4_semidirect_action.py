#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import itertools
import json
import subprocess
import sys
from collections import Counter
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


def inverse(g: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(g)
    for i, j in enumerate(g):
        out[j] = i
    return tuple(out)


def block_perm(blocks: list[set[int]], g: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for b in blocks:
        ib = image(b, g)
        hits = [j for j, c in enumerate(blocks) if ib == c]
        if len(hits) != 1:
            raise ValueError(f"block image not unique: {hits}")
        out.append(hits[0])
    return tuple(out)


def source_signature(bits7: tuple[int, ...], source_supports: list[set[int]]) -> tuple[int, ...]:
    return tuple(int(len({bits7[i] for i in supp}) == 1) for supp in source_supports)


def canon_projective_bits(bits7: list[int]) -> tuple[int, ...]:
    if bits7[6]:
        bits7 = [b ^ 1 for b in bits7]
    return tuple(bits7[:6])


def transport_bits(bits6: tuple[int, ...], coord_perm7: tuple[int, ...]) -> tuple[int, ...]:
    old = list(bits6) + [0]
    new = [0] * 7
    for i, bit in enumerate(old):
        new[coord_perm7[i]] = bit
    return canon_projective_bits(new)


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_ax_marking")
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
    blocks = zblocks + wblocks

    # Source matching convention forced by the six exact node support cells.
    matchings = [
        frozenset((frozenset((0, 3)), frozenset((1, 2)))),
        frozenset((frozenset((0, 2)), frozenset((1, 3)))),
        frozenset((frozenset((0, 1)), frozenset((2, 3)))),
    ]
    matching_index = {m: i for i, m in enumerate(matchings)}
    wc_pairs = [(0, 3), (1, 2), (0, 2), (1, 3), (0, 1), (2, 3)]
    cell_z = [0, 0, 1, 1, 2, 2]

    records = []
    quotient_pairs = set()
    quotient_w = set()
    kernel = []
    cell_perm_records = set()
    for g in G:
        zp = block_perm(zblocks, g)
        wp = block_perm(wblocks, g)
        quotient_pairs.add((wp, zp))
        quotient_w.add(wp)
        if wp == tuple(range(4)) and zp == tuple(range(3)):
            kernel.append(g)

        induced_z = []
        for m in matchings:
            moved = frozenset(
                frozenset((wp[a], wp[b])) for a, b in (tuple(sorted(p)) for p in m)
            )
            induced_z.append(matching_index[moved])
        induced_z = tuple(induced_z)
        if induced_z != zp:
            raise ValueError(f"S4 perfect-matching action mismatch: wp={wp}, zp={zp}, induced={induced_z}")

        cp = []
        for k, (a, b) in enumerate(wc_pairs):
            pair = tuple(sorted((wp[a], wp[b])))
            hits = [j for j, q in enumerate(wc_pairs) if tuple(sorted(q)) == pair]
            if len(hits) != 1:
                raise ValueError("cell pair image ambiguity")
            j = hits[0]
            if zp[cell_z[k]] != cell_z[j]:
                raise ValueError("retained/source six-cell action mismatch")
            cp.append(j)
        cell_perm_records.add(tuple(cp))
        records.append((g, wp, zp, tuple(cp)))

    all_s4 = set(itertools.permutations(range(4)))
    if quotient_w != all_s4:
        raise ValueError(f"W/C quotient is not full S4: {len(quotient_w)}")
    if len(quotient_pairs) != 24 or len(kernel) != 64:
        raise ValueError(f"quotient/kernel order regression: quotient={len(quotient_pairs)}, kernel={len(kernel)}")
    if len(cell_perm_records) != 24:
        raise ValueError(f"six-cell quotient action not faithful S4: {len(cell_perm_records)}")

    H = kernel
    retained_cells = []
    source_supports = []
    for zi, pairset in enumerate([[(0, 3), (1, 2)], [(0, 2), (1, 3)], [(0, 1), (2, 3)]]):
        for wi, wj in pairset:
            rc = zblocks[zi] & wblocks[wi] & wblocks[wj]
            if len(rc) != 8:
                raise ValueError("support cell size regression")
            retained_cells.append(rc)
            zero = {zi, 3 + wi, 3 + wj}
            source_supports.append(set(range(7)) - zero)

    def retained_signature(h: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(int(all(h[p - 1] + 1 == p for p in c)) for c in retained_cells)

    src_counter = Counter()
    for bits6 in itertools.product((0, 1), repeat=6):
        src_counter[source_signature(tuple(bits6) + (0,), source_supports)] += 1
    ret_counter = Counter(retained_signature(h) for h in H)
    if src_counter != ret_counter:
        raise ValueError("kernel signature multiset regression")

    retained_flips = []
    for k in range(7):
        bits7 = (tuple(1 if i == k else 0 for i in range(6)) + (0,)) if k < 6 else (1, 1, 1, 1, 1, 1, 0)
        sig = source_signature(bits7, source_supports)
        hits = [h for h in H if retained_signature(h) == sig]
        if len(hits) != 1:
            raise ValueError(f"coordinate flip recovery regression at {k}: {len(hits)}")
        retained_flips.append(hits[0])

    identity = tuple(range(140))
    bits_to_h = {}
    h_to_bits = {}
    for bits6 in itertools.product((0, 1), repeat=6):
        h = identity
        for k, bit in enumerate(bits6):
            if bit:
                h = compose(retained_flips[k], h)
        bits_to_h[bits6] = h
        h_to_bits[h] = bits6
    if set(h_to_bits) != set(H) or len(h_to_bits) != 64:
        raise ValueError("kernel C2^6 recovery regression")

    # Verify the entire 24-action on H agrees with permutation of the seven
    # source coordinates, modulo global projective sign.
    conjugation_checks = 0
    quotient_lift_hist = Counter()
    for g, wp, zp, cp in records:
        quotient_lift_hist[wp] += 1
        coord_perm7 = tuple(zp) + tuple(3 + j for j in wp)
        ig = inverse(g)
        for k in range(6):
            bits = tuple(1 if i == k else 0 for i in range(6))
            expected = transport_bits(bits, coord_perm7)
            actual_h = compose(g, compose(retained_flips[k], ig))
            if actual_h not in h_to_bits:
                raise ValueError("kernel not normal under retained G")
            actual = h_to_bits[actual_h]
            if actual != expected:
                raise ValueError(
                    f"semidirect conjugation mismatch wp={wp}, zp={zp}, basis={k}, expected={expected}, actual={actual}"
                )
            conjugation_checks += 1

    if set(quotient_lift_hist.values()) != {64} or len(quotient_lift_hist) != 24:
        raise ValueError(f"quotient coset size regression: {quotient_lift_hist}")

    print(json.dumps({
        "mode": "SCRATCH_POST1648AX_OUTER_S4_SEMIDIRECT_ACTION",
        "retained_group_order": len(G),
        "kernel_order": len(H),
        "quotient_order": len(quotient_pairs),
        "unique_WC_cover_candidate_indices_zero_based": chosen,
        "W_C_block_action_is_full_S4": True,
        "Z_block_action_is_exact_induced_action_on_three_perfect_matchings_of_K4": True,
        "six_support_cell_action_is_exact_natural_S4_action_on_two_subsets_of_four_WC_coordinates": True,
        "quotient_coset_size": 64,
        "quotient_coset_count": 24,
        "source_C2_6_kernel_recovered": True,
        "semidirect_conjugation_matches_seven_coordinate_permutation_mod_global_sign": True,
        "conjugation_basis_checks": conjugation_checks,
        "next_exact_route": "TEST_SPLITTING_BY_RECOVERING_AN_S4_COMPLEMENT_AND_THEN_SOLVE_ONE_BASEPOINT_ORBIT_FOR_A_FULL_48_NODE_EQUIVARIANT_BIJECTION",
        "firewalls": {
            "scratch_only": True,
            "extension_splitting_verified": False,
            "full_1536_source_to_retained_group_isomorphism_verified": False,
            "explicit_48_node_bijection_obtained": False,
            "v6_carrier_excluded": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False
        }
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
