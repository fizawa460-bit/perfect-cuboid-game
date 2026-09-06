#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
MARKING_FILE = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
BOUNDARY_FILE = HERE / "post1473-boundary-label-weierstrass-adapter.json"
H_ASSET_FILE = HERE / "post1532-full-stoll-h-orbit-symmetry-negative.json"

EXPECTED_BOUNDARY = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
EXPECTED_H = "6067bf47c856561917de355c0bb734580846f06fd3beaa81f43297721ca241aa"
EXPECTED_H_WORDS = {"id": "1", "u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"}
KNOWN_CURVE_COUNT = 140
EXPECTED_GROUP_ORDER = 1536


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


def close_group(generators: list[tuple[str, list[int]]]) -> dict[tuple[int, ...], str]:
    identity = tuple(range(1, KNOWN_CURVE_COUNT + 1))
    seen: dict[tuple[int, ...], str] = {identity: "1"}
    queue = deque([identity])
    while queue:
        p = queue.popleft()
        prefix = seen[p]
        for name, gp in generators:
            q = tuple(compose(list(p), gp))
            if q in seen:
                continue
            seen[q] = name if prefix == "1" else prefix + "*" + name
            queue.append(q)
    return seen


def main() -> None:
    boundary = json.loads(BOUNDARY_FILE.read_text())
    h_asset = json.loads(H_ASSET_FILE.read_text())
    assert canonical(boundary) == EXPECTED_BOUNDARY
    assert canonical(h_asset) == EXPECTED_H
    assert h_asset["finite_result"]["h_deck_words"] == EXPECTED_H_WORDS

    boundary_map = {int(k): int(v) for k, v in boundary["boundary_label_to_weierstrass_id"].items()}
    labels = set(range(33, 45))
    assert set(boundary_map) == labels
    fibers = {wid: {label for label, x in boundary_map.items() if x == wid} for wid in range(1, 7)}
    assert all(len(fiber) == 2 for fiber in fibers.values())

    marking_mod = load_module(MARKING_FILE, "stage32_post1648f_marking")
    marking = marking_mod.load()
    perms = [[int(x) for x in p] for p in marking["aut_action"]["permutations_1based"]]
    assert len(perms) == 9 and all(len(p) == KNOWN_CURVE_COUNT for p in perms)
    group = close_group([(f"g{i}", perms[i - 1]) for i in range(1, 10)])
    assert len(group) == EXPECTED_GROUP_ORDER

    identity = list(range(1, KNOWN_CURVE_COUNT + 1))

    def word(indices: tuple[int, ...]) -> list[int]:
        out = identity
        for i in indices:
            out = compose(out, perms[i - 1])
        return out

    h_perms = {
        "id": identity,
        "u": word((7, 9)),
        "v": word((7, 8)),
        "uv": word((8, 9)),
    }
    h_set = {tuple(p) for p in h_perms.values()}
    assert len(h_set) == 4

    boundary_setwise = []
    quotient_well_defined = []
    quotient_kernel = []
    quotient_actions: dict[tuple[int, ...], list[tuple[int, ...]]] = {}

    for p_tuple, word_name in group.items():
        p = list(p_tuple)
        if {p[label - 1] for label in labels} != labels:
            continue
        boundary_setwise.append((p_tuple, word_name))

        wid_perm = {}
        ok = True
        for wid, fiber in fibers.items():
            images = {boundary_map[p[label - 1]] for label in fiber}
            if len(images) != 1:
                ok = False
                break
            wid_perm[wid] = next(iter(images))
        if not ok or set(wid_perm.values()) != set(range(1, 7)):
            continue
        quotient_well_defined.append((p_tuple, word_name, wid_perm))
        action = tuple(wid_perm[i] for i in range(1, 7))
        quotient_actions.setdefault(action, []).append(p_tuple)
        if action == (1, 2, 3, 4, 5, 6):
            quotient_kernel.append((p_tuple, word_name))

    kernel_set = {p for p, _ in quotient_kernel}
    all_fiber_sizes = sorted({len(v) for v in quotient_actions.values()})
    action_count = len(quotient_actions)

    result = {
        "schema": "STAGE32_POST1648F_WEIERSTRASS_QUOTIENT_KERNEL_DIAGNOSTIC_V1",
        "source_locks": {
            "boundary_weierstrass_adapter": EXPECTED_BOUNDARY,
            "retained_H": EXPECTED_H,
        },
        "finite_counts": {
            "stoll_group_order": len(group),
            "boundary_33_44_setwise_stabilizer_order": len(boundary_setwise),
            "well_defined_six_weierstrass_quotient_action_domain_order": len(quotient_well_defined),
            "distinct_six_weierstrass_quotient_actions": action_count,
            "quotient_action_fiber_sizes": all_fiber_sizes,
            "quotient_kernel_order": len(quotient_kernel),
            "retained_H_order": len(h_set),
            "quotient_kernel_equals_retained_H": kernel_set == h_set,
            "quotient_kernel_words": sorted(word for _, word in quotient_kernel),
        },
        "exact_consequence": {
            "same_sixpoint_action_iff_same_H_coset_on_well_defined_domain": kernel_set == h_set and all_fiber_sizes == [4],
            "post1648e_each_four_candidate_sixpoint_pattern_is_one_H_coset": kernel_set == h_set and all_fiber_sizes == [4],
            "H_lift_ambiguity_size": 4,
            "absolute_W_line_identified": False,
            "survivors_current_credit": [73, 97, 235],
            "Q602_excluded": False,
            "O210_excluded": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
