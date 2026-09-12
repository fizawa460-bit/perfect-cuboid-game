#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mass7_mod2_obstruction as base

G1 = [101, 102, 103]
G2 = [97, 98, 99]
G3 = [93, 94, 95, 96]
FIXED = sorted(G1 + G2 + G3)
EXPECTED_GROUP_CELL_PAIRS = {
    "g1": [2, 3],
    "g2": [5, 4],
    "g3": [4, 5],
}


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def run() -> dict:
    _P, blocks = base.load_picard_interface()
    req(len(blocks) == 2 and all(len(pack) == 6 for pack in blocks), "two-pack fibre geometry drift")

    cell_pair = {}
    for label in range(93, 141):
        loc = []
        for p, pack in enumerate(blocks):
            hits = [k for k, cell in enumerate(pack) if label in cell]
            req(len(hits) == 1, f"exceptional label {label} incidence drift in pack {p}")
            loc.append(hits[0])
        cell_pair[label] = tuple(loc)

    groups = {"g1": G1, "g2": G2, "g3": G3}
    for name, labels in groups.items():
        expected = tuple(EXPECTED_GROUP_CELL_PAIRS[name])
        req(all(cell_pair[label] == expected for label in labels), f"{name} cell-pair geometry drift")

    fixed_cells = []
    empty_cells = []
    for p in range(2):
        occupied = sorted({cell_pair[label][p] for label in FIXED})
        empty = [k for k in range(6) if k not in occupied]
        fixed_cells.append(occupied)
        empty_cells.append(empty)
        req(len(empty) == 3, f"pack {p+1} must have exactly three fixed-empty cells")

    free = [label for label in range(93, 141) if label not in FIXED]
    free_g3_pair = [label for label in free if cell_pair[label] == tuple(EXPECTED_GROUP_CELL_PAIRS["g3"])]

    # Symbolic argument under d=e=8, fixed_mass>=7, g3=3:
    # 1. fixed_mass<=e=8, so residual exceptional mass r is 0 or 1.
    # 2. Each pack has three cells with zero fixed contribution. A residual of
    #    mass <=1 can affect at most one of them, leaving at least two zero cells.
    # 3. Fibre equalities 2*y_boundary+s[p,k]=n_p force all six s[p,k]
    #    in a pack to have the same parity. Since a zero cell remains, that
    #    common parity is even in both packs.
    # 4. g3=3 contributes an odd 3 to pack1 cell4 and pack2 cell5. To make both
    #    cells even, r must be 1 and its unique unit must lie in a free label
    #    whose cell pair is simultaneously (4,5).
    # 5. Source-locked incidence geometry has no such free label, contradiction.
    symbolic_contradiction = len(free_g3_pair) == 0
    req(symbolic_contradiction, f"free exceptional labels share g3 cell pair: {free_g3_pair}")

    out = {
        "schema": "STAGE32_CERTLIFT_G3_MASS7_SYMBOLIC_FIBRE_PARITY_LEMMA_V1",
        "stage": "32",
        "node": "CERTLIFT-03",
        "status": "PASS_SYMBOLIC_MASS7_G3_FIBRE_PARITY_LEMMA_D8_E8",
        "hypothesis": {
            "d": 8,
            "e": 8,
            "fixed_exceptional_labels": FIXED,
            "fixed_exceptional_mass_lower_bound": 7,
            "g3_labels": G3,
            "g3_sum": 3,
        },
        "source_locked_geometry": {
            "group_cell_pairs_pack1_pack2": EXPECTED_GROUP_CELL_PAIRS,
            "fixed_occupied_cells_by_pack": fixed_cells,
            "fixed_empty_cells_by_pack": empty_cells,
            "free_exceptional_count": len(free),
            "free_labels_with_g3_cell_pair_4_5": free_g3_pair,
            "all_exceptional_cell_pair_sha256": csha({str(k): list(v) for k, v in sorted(cell_pair.items())}),
        },
        "derivation": [
            "fixed_mass>=7 and total exceptional mass e=8 imply residual exceptional mass r<=1",
            "in each six-cell pack the ten fixed labels occupy exactly three cells, so at least two of the three fixed-empty cells remain zero after adding residual mass r<=1",
            "2*y_boundary+s[p,k]=n_p forces all six cell sums in each pack to share one parity; the surviving zero cell forces that parity to be even",
            "g3=3 is odd and contributes to pack1 cell4 and pack2 cell5, so both can be even only if the unique residual unit lies simultaneously in cell pair (4,5)",
            "no free exceptional label has cell pair (4,5), hence no integral exceptional/fibre completion exists"
        ],
        "dependencies": {
            "uses_picard64_column_image": False,
            "uses_hnf": False,
            "uses_solver": False,
            "uses_block_enumeration": False,
            "uses_nonnegativity_beyond_exceptional_mass": False,
            "uses_cross_pack_incidence_inequality": False,
            "uses_fixed_exceptional_mass_ge_7": True,
            "uses_source_locked_two_pack_incidence": True,
        },
        "interpretation": {
            "lemma": "At d=e=8 in the source-locked e8 two-pack interface, fixed_exceptional_mass>=7 and y93+y94+y95+y96=3 are incompatible with the exact fibre equalities.",
            "strictly_stronger_than_1852_block_replay": True,
            "cross_e_claim": False,
            "cross_d_claim": False,
            "next_gate": "Hostile-audit this symbolic derivation and build an exact adapter identifying how many current/remaining Stage32 states satisfy the lemma before any MAIN pruning credit."
        },
        "credit": {
            "certlift_symbolic_lemma_candidate": True,
            "stage32_main_pruning_credit": False,
            "full178_credit": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "stage32_closure_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    return out


def main() -> None:
    out = run()
    req(out["status"] == "PASS_SYMBOLIC_MASS7_G3_FIBRE_PARITY_LEMMA_D8_E8", "symbolic MASS7-g3 lemma failed")
    req(out["source_locked_geometry"]["free_labels_with_g3_cell_pair_4_5"] == [], "g3 cell-pair residual escape exists")
    print(json.dumps({
        "status": out["status"],
        "group_cell_pairs": out["source_locked_geometry"]["group_cell_pairs_pack1_pack2"],
        "empty_cells": out["source_locked_geometry"]["fixed_empty_cells_by_pack"],
        "free_g3_pair_labels": out["source_locked_geometry"]["free_labels_with_g3_cell_pair_4_5"],
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
