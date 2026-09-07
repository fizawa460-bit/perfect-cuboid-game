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


def source_signature(bits7: tuple[int, ...], source_supports: list[set[int]]) -> tuple[int, ...]:
    # A projective diagonal sign change fixes an entire sign-support cell
    # pointwise iff its signs are constant on the four nonzero coordinates.
    return tuple(int(len({bits7[i] for i in supp}) == 1) for supp in source_supports)


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_aw_sign_marking")
    G = close_permutation_group(marking["aut_action"]["permutations_1based"])
    av = run_json(AV)
    zd = run_json(ZD)
    cell = run_json(CELL)

    if len(G) != 1536:
        raise ValueError("retained group order regression")
    zparts = zd["retained"]["unordered_Z1_Z2_Z3_exact_partitions"]
    survivors = cell["support_design_survivors"]
    if len(zparts) != 1 or len(survivors) != 1:
        raise ValueError("unique coordinate design regression")

    zblocks = [set(b["exceptional_labels_1based"]) for b in zparts[0]["blocks"]]
    chosen = survivors[0]["candidate_indices_zero_based"]
    candidates = av["coordinate_W1_W2_W3_C_recovery"]["single_hyperplane_candidates"]
    wblocks = [set(candidates[i]["exceptional_labels_1based"]) for i in chosen]
    blocks = zblocks + wblocks
    H = [g for g in G if all(image(b, g) == b for b in blocks)]
    if len(H) != 64:
        raise ValueError(f"unique coordinate-block kernel order regression: {len(H)}")

    # Cell order is source-design order:
    # Z0:(W0,W3),(W1,W2); Z1:(W0,W2),(W1,W3); Z2:(W0,W1),(W2,W3).
    pairings = [[(0, 3), (1, 2)], [(0, 2), (1, 3)], [(0, 1), (2, 3)]]
    retained_cells: list[set[int]] = []
    source_supports: list[set[int]] = []
    cell_descriptors = []
    for zi, pairs in enumerate(pairings):
        for wi, wj in pairs:
            rc = zblocks[zi] & wblocks[wi] & wblocks[wj]
            if len(rc) != 8:
                raise ValueError(f"retained support cell size regression: Z{zi}, W{wi},W{wj}: {len(rc)}")
            retained_cells.append(rc)
            zero = {zi, 3 + wi, 3 + wj}
            source_supports.append(set(range(7)) - zero)
            cell_descriptors.append({
                "Z_index_zero_based": zi,
                "WC_pair_zero_based": [wi, wj],
                "retained_exceptional_labels_1based": sorted(rc),
                "source_zero_coordinate_indices": sorted(zero),
                "source_nonzero_coordinate_indices": sorted(set(range(7)) - zero),
            })

    def retained_signature(g: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(int(all(g[p - 1] + 1 == p for p in c)) for c in retained_cells)

    src_elements = []
    src_counter = Counter()
    src_by_sig: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for bits6 in itertools.product((0, 1), repeat=6):
        bits7 = tuple(bits6) + (0,)  # quotient by global sign: canonical representative
        sig = source_signature(bits7, source_supports)
        src_elements.append((bits7, sig))
        src_counter[sig] += 1
        src_by_sig.setdefault(sig, []).append(bits7)

    ret_counter = Counter(retained_signature(g) for g in H)
    if src_counter != ret_counter:
        raise ValueError(f"source/retained sign-kernel signature multiset mismatch: {src_counter} != {ret_counter}")

    # The seven projective single-coordinate sign flips have unique cell-fixing
    # signatures.  For coordinate 6 use the globally equivalent representative
    # that flips coordinates 0..5 and leaves coordinate 6 unchanged.
    coordinate_flips = []
    retained_flip_elements = []
    for k in range(7):
        if k < 6:
            bits7 = tuple(1 if i == k else 0 for i in range(6)) + (0,)
        else:
            bits7 = (1, 1, 1, 1, 1, 1, 0)
        sig = source_signature(bits7, source_supports)
        if src_counter[sig] != 1:
            raise ValueError(f"source coordinate-flip signature not unique: {k}, {sig}, {src_counter[sig]}")
        matches = [g for g in H if retained_signature(g) == sig]
        if len(matches) != 1:
            raise ValueError(f"retained coordinate-flip signature not unique: {k}, {sig}, {len(matches)}")
        g = matches[0]
        retained_flip_elements.append(g)
        coordinate_flips.append({
            "coordinate_index": k,
            "coordinate_family": "Z" if k < 3 else "WC",
            "pointwise_fixed_cell_mask": list(sig),
            "pointwise_fixed_cell_count": sum(sig),
            "retained_fixed_exceptional_count": sum(g[p - 1] + 1 == p for p in range(93, 141)),
        })

    identity = tuple(range(140))
    product_all = identity
    for g in retained_flip_elements:
        product_all = compose(g, product_all)
    if product_all != identity:
        raise ValueError("seven retained coordinate flips do not satisfy global-sign relation")

    generated = {identity}
    changed = True
    while changed:
        changed = False
        for a in list(generated):
            for b in retained_flip_elements:
                c = compose(a, b)
                if c not in generated:
                    generated.add(c)
                    changed = True
    if set(generated) != set(H):
        raise ValueError(f"seven coordinate flips fail to generate H: {len(generated)} != 64")

    # Verify the generator-wise map extends to an exact signature-preserving
    # C2^6 isomorphism by multiplying the first six source coordinate flips.
    mapped = {}
    for bits6 in itertools.product((0, 1), repeat=6):
        g = identity
        for k, bit in enumerate(bits6):
            if bit:
                g = compose(retained_flip_elements[k], g)
        bits7 = tuple(bits6) + (0,)
        ssig = source_signature(bits7, source_supports)
        rsig = retained_signature(g)
        if ssig != rsig:
            raise ValueError(f"signature transport regression for {bits6}: {ssig} != {rsig}")
        mapped[bits6] = g
    if len(set(mapped.values())) != 64 or set(mapped.values()) != set(H):
        raise ValueError("source C2^6 does not biject onto retained H")

    fixed_cell_count_hist = Counter(sum(sig) for sig in src_counter.elements())
    print(json.dumps({
        "mode": "SCRATCH_POST1648AW_SIGN_KERNEL_SIGNATURE",
        "unique_WC_cover_candidate_indices_zero_based": chosen,
        "support_cells": cell_descriptors,
        "source_projective_sign_group_order": 64,
        "retained_coordinate_block_kernel_order": len(H),
        "signature_multiset_exact_match": True,
        "fixed_cell_count_histogram": {str(k): v for k, v in sorted(fixed_cell_count_hist.items())},
        "coordinate_flip_recovery": coordinate_flips,
        "seven_flip_global_sign_relation_verified": True,
        "first_six_flips_generate_retained_kernel": True,
        "source_C2_6_to_retained_kernel_exact_isomorphism_verified": True,
        "retained_kernel_support_cell_orbit_sizes": [len({g[min(c) - 1] + 1 for g in H}) for c in retained_cells],
        "remaining_matching_ambiguity": "one basepoint choice in each of six 8-node support cells before using the order-24 outer action",
        "next_exact_route": "RECOVER_ORDER24_OUTER_ACTION_ON_FOUR_WC_BLOCKS_AND_THREE_Z_MATCHINGS_THEN_COUPLE_THE_SIX_BASEPOINT_CHOICES",
        "firewalls": {
            "scratch_only": True,
            "full_1536_node_action_adapter_credit": False,
            "sign_kernel_subaction_identified": True,
            "explicit_48_node_bijection_obtained": False,
            "v6_carrier_excluded": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False
        }
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
