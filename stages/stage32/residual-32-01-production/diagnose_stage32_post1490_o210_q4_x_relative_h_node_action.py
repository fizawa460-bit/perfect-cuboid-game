#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
INCIDENCE = HERE / "post1473-x8-marked-exceptional-incidence.json"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_INCIDENCE = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"


def csha(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    # one-based permutation composition p o q
    return tuple(p[q[i] - 1] for i in range(len(p)))


def main() -> None:
    marking = load_module(MARKING, "s32_post1490_relative_h_marking").load()
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise SystemExit("retained marking canonical moved")
    aut = marking.get("aut_action", {})
    perms = aut.get("permutations_1based", [])
    if len(perms) != 9:
        raise SystemExit(f"retained automorphism generator count moved: {len(perms)}")
    pp = [tuple(int(x) for x in p) for p in perms]
    ident = tuple(range(1, 141))
    if any(len(p) != 140 or tuple(sorted(p)) != ident for p in pp):
        raise SystemExit("retained automorphism permutation shape moved")

    raw = json.loads(INCIDENCE.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_INCIDENCE or csha(raw) != claimed:
        raise SystemExit("marked exceptional incidence canonical moved")
    rows = raw["rows"]
    pair_to_nodes: dict[str, list[int]] = {}
    for r in rows:
        key = f'{int(r["first_factor_boundary_label"])}:{int(r["second_factor_boundary_label"])}'
        pair_to_nodes.setdefault(key, []).append(int(r["exceptional_label"]))
    if len(pair_to_nodes) != 12 or any(len(v) != 4 for v in pair_to_nodes.values()):
        raise SystemExit("12 x 4 marked-node partition moved")

    # Upstream Stoll generator order: g7,g8,g9 are b1,b2,b3 sign flips.
    # From the theta transformation source lock on the first X(8) factor:
    # T=g9, T'=g7, R=g7*g8*g9, hence H=Gamma'[4]/Gamma[8] has
    # u=TT'=g7*g9, v=RT=g7*g8, uv=RT'=g8*g9.
    g7, g8, g9 = pp[6], pp[7], pp[8]
    deck = {
        "u": compose(g7, g9),
        "v": compose(g7, g8),
        "uv": compose(g8, g9),
    }
    if any(compose(p, p) != ident for p in deck.values()):
        raise SystemExit("candidate relative-H node action ceased to be involutive")
    if compose(deck["u"], deck["v"]) != deck["uv"] or compose(deck["v"], deck["u"]) != deck["uv"]:
        raise SystemExit("candidate relative-H node action ceased to form V4")

    boundary_labels = sorted({int(r["first_factor_boundary_label"]) for r in rows} | {int(r["second_factor_boundary_label"]) for r in rows})
    boundary_fixed = {name: all(p[j - 1] == j for j in boundary_labels) for name, p in deck.items()}
    if not all(boundary_fixed.values()):
        raise SystemExit(f"candidate H action moved a quotient boundary label: {boundary_fixed}")

    fiber_rows = []
    all_regular = True
    for pair in sorted(pair_to_nodes):
        nodes = sorted(pair_to_nodes[pair])
        node_set = set(nodes)
        local = {}
        for name, p in deck.items():
            image = [p[j - 1] for j in nodes]
            if set(image) != node_set:
                raise SystemExit(f"deck {name} moved node fiber {pair}: {nodes} -> {image}")
            if any(p[j - 1] == j for j in nodes):
                raise SystemExit(f"deck {name} fixed a node in fiber {pair}")
            local[name] = [[j, p[j - 1]] for j in nodes]
        orbit = {nodes[0], deck["u"][nodes[0] - 1], deck["v"][nodes[0] - 1], deck["uv"][nodes[0] - 1]}
        regular = orbit == node_set
        all_regular = all_regular and regular
        fiber_rows.append({"pair": pair, "nodes": nodes, "regular_H_torsor": regular, "deck_pairs": local})
    if not all_regular:
        raise SystemExit("at least one 4-node marked fiber is not a regular H torsor")

    exc = list(range(93, 141))
    out = {
        "status": "PASS_DIAGNOSTIC",
        "scope": "B-side automorphism permutations used only on the 48 singular-node labels; no Pic(B)->Pic(X) divisor-class identification",
        "source_locks": {
            "retained_marking_canonical_sha256": EXPECTED_MARKING,
            "marked_exceptional_incidence_canonical_sha256": EXPECTED_INCIDENCE,
            "stoll_generator_indices_1based": {"g7_b1_sign": 7, "g8_b2_sign": 8, "g9_b3_sign": 9},
            "modular_to_stoll": {"u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"},
        },
        "checks": {
            "candidate_actions_form_V4": True,
            "all_12_quotient_boundary_labels_fixed": True,
            "all_12_marked_four_node_fibers_invariant": True,
            "all_nonidentity_actions_fixed_point_free_on_48_nodes": all(all(p[j - 1] != j for j in exc) for p in deck.values()),
            "all_12_four_node_fibers_are_regular_H_torsors": all_regular,
        },
        "exceptional_permutations_1based": {name: [p[j - 1] for j in exc] for name, p in deck.items()},
        "fiber_rows": fiber_rows,
        "next": "Source-lock the X->B unique-point lift/equivariance and then the local branch multiplicity adapter before accumulating D.t(D).",
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
