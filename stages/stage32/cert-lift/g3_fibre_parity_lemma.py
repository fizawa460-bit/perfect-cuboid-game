#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mass7_mod2_obstruction as base

EXCEPTIONAL_LABELS = list(range(93, 141))
G3_LABELS = [93, 94, 95, 96]


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def bits(labels) -> int:
    out = 0
    for label in labels:
        label = int(label)
        req(93 <= label <= 140, f"nonexceptional label in parity functional: {label}")
        out ^= 1 << (label - 93)
    return out


def labels_from_bits(v: int) -> list[int]:
    return [label for label in EXCEPTIONAL_LABELS if (v >> (label - 93)) & 1]


def span_representation(vectors: list[int], target: int) -> int | None:
    # Echelon basis keyed by the highest set bit, retaining provenance in the
    # original constraint list. If target reduces to zero, provenance is an
    # exact XOR representation of target by those constraints.
    basis: dict[int, tuple[int, int]] = {}
    for i, original in enumerate(vectors):
        v = int(original)
        provenance = 1 << i
        while v:
            p = v.bit_length() - 1
            if p not in basis:
                basis[p] = (v, provenance)
                break
            bv, bp = basis[p]
            v ^= bv
            provenance ^= bp

    v = int(target)
    provenance = 0
    while v:
        p = v.bit_length() - 1
        row = basis.get(p)
        if row is None:
            return None
        bv, bp = row
        v ^= bv
        provenance ^= bp
    return provenance


def run() -> dict:
    _P, factor_blocks = base.load_picard_interface()
    req(len(factor_blocks) == 2 and all(len(pack) == 6 for pack in factor_blocks), "fibre block shape drift")
    for pack in factor_blocks:
        flat = sorted(label for cell in pack for label in cell)
        req(flat == EXCEPTIONAL_LABELS, "exceptional fibre partition drift")
        req(all(len(cell) == 8 for cell in pack), "fibre cell width drift")

    constraints = []
    # Exact fibre equations are 2*y_boundary + s_{p,k} = n_p. Modulo 2,
    # every incidence sum inside one pack equals n_p. Hence cell k and cell 0
    # have equal parity for k=1..5.
    for p in range(2):
        for k in range(1, 6):
            vector = bits(factor_blocks[p][0]) ^ bits(factor_blocks[p][k])
            constraints.append({
                "id": f"PACK{p+1}_CELL0_EQ_CELL{k}",
                "vector": vector,
                "rhs_d_coefficient": 0,
                "meaning": f"s[{p+1},0]+s[{p+1},{k}]=0 mod2",
            })
    # n1+n2=d, so modulo 2 the reference cell parities differ by d.
    constraints.append({
        "id": "PACK1_CELL0_PLUS_PACK2_CELL0_EQ_D",
        "vector": bits(factor_blocks[0][0]) ^ bits(factor_blocks[1][0]),
        "rhs_d_coefficient": 1,
        "meaning": "s[1,0]+s[2,0]=d mod2",
    })

    vectors = [int(row["vector"]) for row in constraints]
    target = bits(G3_LABELS)
    provenance = span_representation(vectors, target)
    in_span = provenance is not None

    selected_indices = [] if provenance is None else [
        i for i in range(len(constraints)) if (provenance >> i) & 1
    ]
    replay = 0
    rhs_d_coefficient = 0
    for i in selected_indices:
        replay ^= vectors[i]
        rhs_d_coefficient ^= int(constraints[i]["rhs_d_coefficient"])
    if in_span:
        req(replay == target, "g3 parity relation provenance replay failed")

    cell_map = {}
    for label in range(93, 141):
        locations = []
        for p, pack in enumerate(factor_blocks):
            hits = [k for k, cell in enumerate(pack) if label in cell]
            req(len(hits) == 1, f"label {label} fibre-cell incidence drift in pack {p}")
            locations.append(hits[0])
        cell_map[str(label)] = locations

    relation = (
        f"sum(y93,y94,y95,y96) == {rhs_d_coefficient}*d (mod 2)"
        if in_span else None
    )
    d8_forced_parity = (rhs_d_coefficient * 8) & 1 if in_span else None
    d8_g3_3_contradiction = bool(in_span and d8_forced_parity != (3 & 1))

    out = {
        "schema": "STAGE32_CERTLIFT_G3_FIBRE_PARITY_LEMMA_V1",
        "stage": "32",
        "node": "CERTLIFT-03",
        "status": (
            "PASS_SYMBOLIC_G3_FIBRE_PARITY_CONTRADICTION_D8"
            if d8_g3_3_contradiction
            else "NO_SYMBOLIC_G3_PARITY_CONTRADICTION"
        ),
        "geometry": {
            "exceptional_labels": [93, 140],
            "pack_count": 2,
            "cells_per_pack": 6,
            "labels_per_cell": 8,
            "g3_labels": G3_LABELS,
            "g3_label_cell_map_pack1_pack2": {str(k): cell_map[str(k)] for k in G3_LABELS},
            "all_fixed_terminal_label_cell_map_pack1_pack2": {
                str(k): cell_map[str(k)] for k in [93,94,95,96,97,98,99,101,102,103]
            },
        },
        "derivation": {
            "input_equations": "2*y_boundary[p,k] + s[p,k] = n_p for p=1,2 and k=0..5; n1+n2=d",
            "mod2_pack_consequence": "within each pack all six s[p,k] have parity n_p",
            "cross_pack_consequence": "s[1,0]+s[2,0]=d mod2",
            "constraint_count": len(constraints),
            "constraint_rank_representation_found": in_span,
            "g3_functional_labels": G3_LABELS,
            "g3_functional_sha256": csha(G3_LABELS),
            "selected_constraint_indices": selected_indices,
            "selected_constraint_ids": [constraints[i]["id"] for i in selected_indices],
            "rhs_d_coefficient": rhs_d_coefficient if in_span else None,
            "symbolic_relation": relation,
            "d8_forced_g3_parity": d8_forced_parity,
            "g3_equals_3_parity": 1,
            "d8_g3_equals_3_contradiction": d8_g3_3_contradiction,
        },
        "constraints": [
            {
                "id": row["id"],
                "labels": labels_from_bits(int(row["vector"])),
                "rhs_d_coefficient": row["rhs_d_coefficient"],
                "meaning": row["meaning"],
            }
            for row in constraints
        ],
        "interpretation": {
            "uses_picard64_column_image": False,
            "uses_hnf": False,
            "uses_solver": False,
            "uses_block_enumeration": False,
            "uses_fixed_exceptional_mass_ge_7": False,
            "stronger_than_finite_g3_mass7_candidate": d8_g3_3_contradiction,
            "lemma_scope": "For the source-locked two-pack fibre incidence geometry, any integral completion satisfying the fibre equalities obeys the displayed parity relation. At d=8 this rules out g3=3 before Picard/HNF constraints.",
            "cross_e_statement": "The parity relation itself contains no e; no population/pruning credit is claimed outside an exact adapter because g3/interface semantics must be transported separately."
        },
        "credit": {
            "certlift_symbolic_lemma_candidate": d8_g3_3_contradiction,
            "stage32_main_pruning_credit": False,
            "theorem_credit": False,
            "stage32_closure_credit": False,
            "merge_authorized": False
        }
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args()
    out = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    if args.self_check:
        d = out["derivation"]
        req(out["status"] == "PASS_SYMBOLIC_G3_FIBRE_PARITY_CONTRADICTION_D8", "symbolic g3 fibre parity lemma not established")
        req(d["constraint_rank_representation_found"] is True, "g3 functional absent from fibre parity row span")
        req(d["d8_g3_equals_3_contradiction"] is True, "d=8 does not contradict g3=3")
        req(out["interpretation"]["uses_picard64_column_image"] is False, "symbolic fibre lemma unexpectedly depends on Picard64")
        req(out["interpretation"]["uses_hnf"] is False, "symbolic fibre lemma unexpectedly depends on HNF")
        req(out["interpretation"]["uses_solver"] is False, "symbolic fibre lemma unexpectedly depends on solver")
        req(out["interpretation"]["uses_block_enumeration"] is False, "symbolic fibre lemma unexpectedly depends on block enumeration")
        req(out["interpretation"]["uses_fixed_exceptional_mass_ge_7"] is False, "symbolic fibre lemma unexpectedly depends on MASS7")
        print(json.dumps({
            "status": out["status"],
            "symbolic_relation": d["symbolic_relation"],
            "selected_constraint_ids": d["selected_constraint_ids"],
            "rhs_d_coefficient": d["rhs_d_coefficient"],
            "g3_cell_map": out["geometry"]["g3_label_cell_map_pack1_pack2"],
            "uses_mass7": out["interpretation"]["uses_fixed_exceptional_mass_ge_7"],
            "canonical": out["canonical_sha256_without_this_field"],
        }, sort_keys=True))
    elif not args.output:
        print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
