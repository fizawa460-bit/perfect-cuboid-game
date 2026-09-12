#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

import mass7_mod2_obstruction as base
import mass7_scope_split as split


@dataclass(frozen=True)
class Atom:
    feature: str
    op: str
    value: int
    mask: int

    @property
    def text(self) -> str:
        return f"{self.feature}{self.op}{self.value}"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def feature_dict(sig: dict) -> dict[str, int]:
    fixed = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}
    groups = [int(v) for v in sig["n355_known_group_sums"]]
    out = {f"y{label}": value for label, value in sorted(fixed.items())}
    out.update({
        "fixed_mass": int(sig["fixed_exceptional_mass"]),
        "support": int(sig["known_exceptional_support"]),
        "g1": groups[0],
        "g2": groups[1],
        "g3": groups[2],
        "max_group": max(groups),
        "min_group": min(groups),
        "g2_minus_g3": groups[1] - groups[2],
        "g1_minus_g2": groups[0] - groups[1],
        "g1_minus_g3": groups[0] - groups[2],
        "x0_eq_x1": int(fixed[95] == fixed[99]),
        "pairlex_eq": int((fixed[97], fixed[94]) == (fixed[93], fixed[98])),
    })
    return out


def atom_mask(records: list[dict], feature: str, op: str, value: int) -> int:
    mask = 0
    for i, rec in enumerate(records):
        x = int(rec["features"][feature])
        ok = (x <= value) if op == "<=" else (x >= value) if op == ">=" else (x == value)
        if ok:
            mask |= 1 << i
    return mask


def candidate_row(text: str, mask: int, blocked_mask: int, survivor_mask: int, audited_mask: int) -> dict:
    blocked = (mask & blocked_mask).bit_count()
    survivors = (mask & survivor_mask).bit_count()
    audited = (mask & audited_mask).bit_count()
    return {
        "predicate": text,
        "selected_blocks": mask.bit_count(),
        "selected_mod2_obstructed": blocked,
        "selected_projection_survivors": survivors,
        "selected_audited_mass7": audited,
        "blocked_coverage_fraction": f"{blocked}/{blocked_mask.bit_count()}",
        "audited_coverage_fraction": f"{audited}/{audited_mask.bit_count()}",
    }


def run() -> dict:
    P, blocks = base.load_picard_interface()
    kernel = base.left_kernel_mod2(P)
    boundary_labels = sorted({b for pack in base.PACKS for b in pack})
    unknown_normal_labels = [
        label for label in range(1, base.NORMAL_COUNT + 1) if label not in boundary_labels
    ]
    masks = base.consistency_masks(kernel, unknown_normal_labels)
    idx = base.e8.indexer()
    current_main = list(map(int, base.e8.current_main_survivor_block_indices()))
    audited_blocks, _manifest = split.locked_audited_scope(current_main)
    audited_set = set(audited_blocks)

    records: list[dict] = []
    blocked_mask = 0
    survivor_mask = 0
    audited_mask = 0
    for block_index in current_main:
        sig = base.e8.block_signature(block_index, idx)
        if int(sig["fixed_exceptional_mass"]) < 7:
            continue
        blocked, witness, _attempts = base.block_mod2_obstructed(
            block_index, idx, blocks, kernel, masks
        )
        i = len(records)
        bit = 1 << i
        if blocked:
            blocked_mask |= bit
        else:
            survivor_mask |= bit
        if block_index in audited_set:
            audited_mask |= bit
        records.append({
            "block_index": block_index,
            "blocked": blocked,
            "features": feature_dict(sig),
            "witness_fibre_degrees": None if witness is None else witness.get("fibre_degrees"),
            "witness_residual_exceptional_label": None if witness is None else witness.get("residual_exceptional_label"),
        })

    req(len(records) == 5667, "MASS7 current-MAIN target-count drift")
    req(blocked_mask.bit_count() == 5392, "current-MAIN mod2 obstruction-count drift")
    req(survivor_mask.bit_count() == 275, "current-MAIN projection-survivor count drift")
    req(audited_mask.bit_count() == 1049, "audited MASS7 target-count drift")
    req((audited_mask & survivor_mask) == 0, "audited MASS7 projection survivor regression")

    features = sorted(records[0]["features"])
    atoms: list[Atom] = []
    all_mask = (1 << len(records)) - 1
    for feature in features:
        values = sorted({int(rec["features"][feature]) for rec in records})
        for value in values:
            for op in ("<=", ">=", "=="):
                mask = atom_mask(records, feature, op, value)
                if mask in (0, all_mask):
                    continue
                atoms.append(Atom(feature, op, value, mask))

    # Deduplicate logically identical masks while keeping a stable, shortest textual representative.
    by_mask: dict[int, Atom] = {}
    for atom in atoms:
        prev = by_mask.get(atom.mask)
        if prev is None or (len(atom.text), atom.text) < (len(prev.text), prev.text):
            by_mask[atom.mask] = atom
    atoms = sorted(by_mask.values(), key=lambda a: a.text)

    singles = []
    for atom in atoms:
        if atom.mask & survivor_mask:
            continue
        singles.append(candidate_row(atom.text, atom.mask, blocked_mask, survivor_mask, audited_mask))
    singles.sort(key=lambda r: (-r["selected_mod2_obstructed"], -r["selected_audited_mass7"], r["predicate"]))

    pairs = []
    for i, a in enumerate(atoms):
        for b in atoms[i + 1 :]:
            if a.feature == b.feature:
                continue
            mask = a.mask & b.mask
            if not mask or (mask & survivor_mask):
                continue
            row = candidate_row(f"({a.text}) & ({b.text})", mask, blocked_mask, survivor_mask, audited_mask)
            if row["selected_mod2_obstructed"] < 100:
                continue
            pairs.append(row)
    pairs.sort(key=lambda r: (-r["selected_mod2_obstructed"], -r["selected_audited_mass7"], r["predicate"]))

    survivor_signature_hist: dict[str, int] = {}
    for i, rec in enumerate(records):
        if not (survivor_mask >> i) & 1:
            continue
        f = rec["features"]
        key = json.dumps({
            "fixed_mass": f["fixed_mass"],
            "support": f["support"],
            "groups": [f["g1"], f["g2"], f["g3"]],
            "x0_eq_x1": f["x0_eq_x1"],
            "pairlex_eq": f["pairlex_eq"],
        }, sort_keys=True, separators=(",", ":"))
        survivor_signature_hist[key] = survivor_signature_hist.get(key, 0) + 1

    out = {
        "schema": "STAGE32_CERTLIFT_MASS7_FEATURE_DISCRIMINATOR_V1",
        "stage": "32",
        "node": "CERTLIFT-02",
        "status": "PASS_ZERO_FALSE_POSITIVE_FEATURE_SEARCH",
        "scope": {
            "current_main_mass7_targets": len(records),
            "mod2_obstructed": blocked_mask.bit_count(),
            "projection_survivors": survivor_mask.bit_count(),
            "audited_mass7_targets": audited_mask.bit_count(),
        },
        "features": features,
        "search": {
            "offset_or_block_index_used_as_feature": False,
            "atom_count_after_mask_dedup": len(atoms),
            "single_atom_zero_survivor_count": len(singles),
            "pair_zero_survivor_count_min100_coverage": len(pairs),
            "top_single_atoms": singles[:20],
            "top_two_atom_conjunctions": pairs[:20],
        },
        "survivor_signature_histogram": dict(sorted(survivor_signature_hist.items(), key=lambda kv: (-kv[1], kv[0]))),
        "interpretation": {
            "feature_search_is_symbolic_proof": False,
            "purpose": "choose a compact source-level hypothesis for the next exact symbolic derivation; every reported predicate has zero projected-mod2 survivors on the full current-MAIN MASS7 target population",
        },
        "credit": {
            "main_pruning": False,
            "theorem": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
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
        s = out["search"]
        print(json.dumps({
            "status": out["status"],
            "top_single": s["top_single_atoms"][:5],
            "top_pair": s["top_two_atom_conjunctions"][:5],
            "survivor_signature_histogram": out["survivor_signature_histogram"],
            "canonical": out["canonical_sha256_without_this_field"],
        }, sort_keys=True))
    elif not args.output:
        print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
