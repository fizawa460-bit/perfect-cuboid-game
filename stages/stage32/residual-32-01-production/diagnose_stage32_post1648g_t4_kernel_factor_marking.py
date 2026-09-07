#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
MARKING_FILE = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
SATAKE_FILE = HERE / "post1473-x8-satake-boundary-marking.json"
BOUNDARY_FILE = HERE / "post1473-boundary-label-weierstrass-adapter.json"

EXPECTED_SATAKE = "69a2a6d3cdf7b0d5c6162424a8102ec41cd09ac7e303469d30577d454363e31d"
EXPECTED_BOUNDARY = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
KNOWN_CURVE_COUNT = 140
KERNEL_WORDS = {
    "1": (),
    "g7": (7,),
    "g8": (8,),
    "g9": (9,),
    "g7*g8": (7,8),
    "g7*g9": (7,9),
    "g8*g9": (8,9),
    "g7*g8*g9": (7,8,9),
}
H_WORDS = {"1", "g7*g8", "g7*g9", "g8*g9"}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def canonical(doc: dict) -> str:
    body = dict(doc)
    field = "canonical_sha256_without_this_field" if "canonical_sha256_without_this_field" in body else "canonical_sha256"
    claimed = body.pop(field)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if claimed != got:
        raise SystemExit(f"canonical mismatch {claimed} != {got}")
    return got


def compose(p: list[int], q: list[int]) -> list[int]:
    return [q[p[j] - 1] for j in range(len(p))]


def main() -> None:
    satake = json.loads(SATAKE_FILE.read_text())
    boundary = json.loads(BOUNDARY_FILE.read_text())
    if satake.get("canonical_sha256") != EXPECTED_SATAKE:
        raise SystemExit("Satake marking canonical moved")
    if canonical(boundary) != EXPECTED_BOUNDARY:
        raise SystemExit("boundary adapter canonical moved")

    zset = set(satake["factor_marking"]["first_factor_cusp_z_fixed_curves"])
    wset = set(satake["factor_marking"]["second_factor_cusp_w_fixed_curves"])
    all_boundary = set(range(33,45))
    assert zset | wset == all_boundary and not (zset & wset)

    bmap = {int(k): int(v) for k,v in boundary["boundary_label_to_weierstrass_id"].items()}
    fibers = {i: sorted(k for k,v in bmap.items() if v == i) for i in range(1,7)}
    assert all(len(v) == 2 for v in fibers.values())
    assert all(len(set(v) & zset) == 1 and len(set(v) & wset) == 1 for v in fibers.values())

    marking_mod = load_module(MARKING_FILE, "stage32_post1648g_marking")
    marking = marking_mod.load()
    perms = [[int(x) for x in p] for p in marking["aut_action"]["permutations_1based"]]
    assert len(perms) == 9 and all(len(p) == KNOWN_CURVE_COUNT for p in perms)
    ident = list(range(1, KNOWN_CURVE_COUNT+1))

    def word(indices: tuple[int,...]) -> list[int]:
        out = ident
        for i in indices:
            out = compose(out, perms[i-1])
        return out

    rows = []
    for name, indices in KERNEL_WORDS.items():
        p = word(indices)
        image_boundary = {p[x-1] for x in all_boundary}
        preserves_boundary = image_boundary == all_boundary
        preserves_factor_sets = ({p[x-1] for x in zset} == zset and {p[x-1] for x in wset} == wset)
        swaps_factor_sets = ({p[x-1] for x in zset} == wset and {p[x-1] for x in wset} == zset)
        fixes_all_boundary_labels = all(p[x-1] == x for x in all_boundary)
        fiberwise = all({p[x-1] for x in labels} == set(labels) for labels in fibers.values())
        within_fiber_swap_count = sum(1 for labels in fibers.values() if all(p[x-1] != x for x in labels) and {p[x-1] for x in labels} == set(labels))
        rows.append({
            "word": name,
            "in_H": name in H_WORDS,
            "outside_H": name not in H_WORDS,
            "preserves_boundary_33_44": preserves_boundary,
            "preserves_z_w_factor_sets": preserves_factor_sets,
            "swaps_z_w_factor_sets": swaps_factor_sets,
            "fixes_all_12_boundary_labels": fixes_all_boundary_labels,
            "preserves_each_weierstrass_two_label_fiber": fiberwise,
            "within_fiber_swap_count": within_fiber_swap_count,
            "boundary_permutation": {str(x): p[x-1] for x in range(33,45)},
        })

    factor_preserving_outside = [r["word"] for r in rows if r["outside_H"] and r["preserves_z_w_factor_sets"]]
    label_fixing_outside = [r["word"] for r in rows if r["outside_H"] and r["fixes_all_12_boundary_labels"]]
    fiber_preserving_outside = [r["word"] for r in rows if r["outside_H"] and r["preserves_each_weierstrass_two_label_fiber"]]

    result = {
        "schema": "STAGE32_POST1648G_T4_KERNEL_FACTOR_MARKING_DIAGNOSTIC_V1",
        "source_locks": {
            "satake_marking": EXPECTED_SATAKE,
            "boundary_weierstrass_adapter": EXPECTED_BOUNDARY,
        },
        "kernel_order": 8,
        "retained_H_order": 4,
        "rows": rows,
        "candidate_filters": {
            "outside_H_count": 4,
            "outside_H_preserving_z_w_factor_sets": factor_preserving_outside,
            "outside_H_preserving_each_weierstrass_two_label_fiber": fiber_preserving_outside,
            "outside_H_fixing_all_12_boundary_labels": label_fixing_outside,
        },
        "decision_boundary": {
            "modular_T4_retained_member_identified": len(label_fixing_outside) == 1,
            "factor_marking_alone_identifies_T4": len(factor_preserving_outside) == 1,
            "source_binding_claimed": False,
            "survivors_current_credit": [73,97,235],
            "Q602_excluded": False,
            "O210_excluded": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
