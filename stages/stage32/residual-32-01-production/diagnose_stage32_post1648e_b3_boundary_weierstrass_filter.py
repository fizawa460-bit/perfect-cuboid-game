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
POST1550_FILE = HERE / "post1550-b3-v4-torsor-normalizer.json"
POST1563_FILE = HERE / "post1563-ambient-symmetry-exhaustion-batch.json"
H_ASSET_FILE = HERE / "post1532-full-stoll-h-orbit-symmetry-negative.json"
BOUNDARY_FILE = HERE / "post1473-boundary-label-weierstrass-adapter.json"
POST1648B_FILE = HERE / "post1648b-cecotti-generator-pair-absolute-marking-preflight.json"

EXPECTED_POST1550 = "1225ca34034f1f1dacb2f3e1f46e7f3d15a6008a5e6b03960109f7bc992b5e95"
EXPECTED_POST1563 = "9dbf0bcb144824a14497b663da2200f94d7250bfc755a37d1d65ca0b565fbb2e"
EXPECTED_H = "6067bf47c856561917de355c0bb734580846f06fd3beaa81f43297721ca241aa"
EXPECTED_BOUNDARY = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
EXPECTED_POST1648B = "b0737602656ff5de3c98ba98cc862ec7b29599255c8da621099c2a63a69e503b"
EXPECTED_GROUP_ORDER = 1536
KNOWN_CURVE_COUNT = 140
EXPECTED_H_WORDS = {"id": "1", "u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"}


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


def power(p: list[int], n: int) -> list[int]:
    out = list(range(1, len(p) + 1))
    for _ in range(n):
        out = compose(out, p)
    return out


def inverse(p: list[int]) -> list[int]:
    out = [0] * len(p)
    for i, image in enumerate(p, start=1):
        out[image - 1] = i
    return out


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


def inverse_map(p: dict[int, int]) -> dict[int, int]:
    return {v: k for k, v in p.items()}


def main() -> None:
    post1550 = json.loads(POST1550_FILE.read_text())
    post1563 = json.loads(POST1563_FILE.read_text())
    h_asset = json.loads(H_ASSET_FILE.read_text())
    boundary = json.loads(BOUNDARY_FILE.read_text())
    post1648b = json.loads(POST1648B_FILE.read_text())
    if canonical(post1550) != EXPECTED_POST1550:
        raise SystemExit("post1550 moved")
    if canonical(post1563) != EXPECTED_POST1563:
        raise SystemExit("post1563 moved")
    if canonical(h_asset) != EXPECTED_H:
        raise SystemExit("H asset moved")
    if canonical(boundary) != EXPECTED_BOUNDARY:
        raise SystemExit("boundary adapter moved")
    if canonical(post1648b) != EXPECTED_POST1648B:
        raise SystemExit("post1648B moved")

    principal = post1550["principal_b3"]
    assert principal["restriction_order"] == 3
    assert principal["W_invariant"] is True
    assert principal["restriction_to_W"] == [[1, 1], [1, 0]]
    route_c = post1563["routes"]["C_principal_b3_membership"]
    assert route_c["beta_B_in_retained_stoll_group"] is True
    assert route_c["beta_B_in_H"] is False
    assert route_c["principal_b3_order"] == 3
    assert post1563["firewalls"]["explicit_beta_B_stoll_word_claimed"] is False
    assert h_asset["finite_result"]["h_deck_words"] == EXPECTED_H_WORDS
    assert post1648b["curve_pair_action"]["phi6_x_map"] == "i*(x-1)/(x+1)"

    boundary_map = {int(k): int(v) for k, v in boundary["boundary_label_to_weierstrass_id"].items()}
    expected_labels = set(range(33, 45))
    assert set(boundary_map) == expected_labels
    fibers: dict[int, set[int]] = {i: set() for i in range(1, 7)}
    for label, wid in boundary_map.items():
        fibers[wid].add(label)
    assert all(len(v) == 2 for v in fibers.values())
    pair_sets = {
        "Z1": frozenset(boundary["cusp_pairs"]["Z1"]),
        "Z2": frozenset(boundary["cusp_pairs"]["Z2"]),
        "Z3": frozenset(boundary["cusp_pairs"]["Z3"]),
    }

    # Exact evaluation of Cecotti's phi6(x)=i(x-1)/(x+1) in the audited
    # Weierstrass-id normalization 1=+1,6=-1,3=+i,5=-i,2=0,4=infinity.
    cecotti_phi6 = {1: 2, 2: 5, 3: 6, 4: 3, 5: 1, 6: 4}
    cecotti_phi6_inv = inverse_map(cecotti_phi6)
    assert cecotti_phi6_inv == {1: 5, 2: 1, 3: 4, 4: 6, 5: 2, 6: 3}

    def pair_action(wperm: dict[int, int]) -> dict[str, str]:
        out = {}
        for pname, pset in pair_sets.items():
            image = frozenset(wperm[x] for x in pset)
            target_name = next((qname for qname, qset in pair_sets.items() if qset == image), None)
            if target_name is None:
                raise AssertionError("not pair preserving")
            out[pname] = target_name
        return out

    assert pair_action(cecotti_phi6) == post1648b["curve_pair_action"]["phi6_pair_permutation"]

    marking_mod = load_module(MARKING_FILE, "stage32_post1648e_marking")
    marking = marking_mod.load()
    aut = marking["aut_action"]
    assert aut["schema"] == "STAGE32_AUT_PERM_SOURCELOCK_V1"
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
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
    h_lookup = {tuple(p): name for name, p in h_perms.items()}
    assert len(h_lookup) == 4

    records = []
    order3_count = 0
    h_cycle_count = 0
    boundary_preserving_count = 0
    quotient_well_defined_count = 0
    pair_partition_preserving_count = 0
    pair_cycling_count = 0

    for p_tuple, word_name in group.items():
        p = list(p_tuple)
        if p == identity or power(p, 3) != identity:
            continue
        order3_count += 1

        pinv = inverse(p)
        induced_h = {}
        ok_h = True
        for hname, h in h_perms.items():
            conj = compose(compose(pinv, h), p)
            cname = h_lookup.get(tuple(conj))
            if cname is None:
                ok_h = False
                break
            induced_h[hname] = cname
        if not ok_h or not all(induced_h[name] != name for name in ("u", "v", "uv")):
            continue
        h_cycle_count += 1

        if {p[label - 1] for label in expected_labels} != expected_labels:
            continue
        boundary_preserving_count += 1

        wid_perm: dict[int, int] = {}
        well_defined = True
        for wid, labels in fibers.items():
            image_wids = {boundary_map[p[label - 1]] for label in labels}
            if len(image_wids) != 1:
                well_defined = False
                break
            wid_perm[wid] = next(iter(image_wids))
        if not well_defined or set(wid_perm.values()) != set(range(1, 7)):
            continue
        quotient_well_defined_count += 1

        try:
            pair_perm = pair_action(wid_perm)
        except AssertionError:
            continue
        pair_partition_preserving_count += 1

        cycles_pairs = all(pair_perm[name] != name for name in ("Z1", "Z2", "Z3"))
        if not cycles_pairs:
            continue
        pair_cycling_count += 1
        records.append({
            "word": word_name,
            "label1_image": p[0],
            "H_conjugation": induced_h,
            "weierstrass_permutation": wid_perm,
            "pair_permutation": pair_perm,
        })

    pair_patterns: dict[str, int] = {}
    point_patterns: dict[str, int] = {}
    point_pattern_label1_images: dict[str, set[int]] = {}
    label1_images = sorted({r["label1_image"] for r in records})
    phi6_records = []
    phi6_inv_records = []
    for r in records:
        pk = json.dumps(r["pair_permutation"], sort_keys=True, separators=(",", ":"))
        wk = json.dumps(r["weierstrass_permutation"], sort_keys=True, separators=(",", ":"))
        pair_patterns[pk] = pair_patterns.get(pk, 0) + 1
        point_patterns[wk] = point_patterns.get(wk, 0) + 1
        point_pattern_label1_images.setdefault(wk, set()).add(r["label1_image"])
        if r["weierstrass_permutation"] == cecotti_phi6:
            phi6_records.append(r)
        if r["weierstrass_permutation"] == cecotti_phi6_inv:
            phi6_inv_records.append(r)

    point_pattern_multiplicities = sorted(point_patterns.values())
    point_pattern_image_cardinalities = sorted(len(v) for v in point_pattern_label1_images.values())
    phi6_label1_images = sorted({r["label1_image"] for r in phi6_records})
    phi6_inv_label1_images = sorted({r["label1_image"] for r in phi6_inv_records})

    result = {
        "schema": "STAGE32_POST1648E_B3_BOUNDARY_WEIERSTRASS_FILTER_DIAGNOSTIC_V2",
        "source_locks": {
            "post1550": EXPECTED_POST1550,
            "post1563": EXPECTED_POST1563,
            "retained_H": EXPECTED_H,
            "boundary_weierstrass_adapter": EXPECTED_BOUNDARY,
            "post1648b_cecotti_generator_preflight": EXPECTED_POST1648B,
        },
        "finite_counts": {
            "stoll_group_order": len(group),
            "order3_count": order3_count,
            "H_cycling_count": h_cycle_count,
            "boundary_33_44_setwise_preserving_count": boundary_preserving_count,
            "six_weierstrass_quotient_well_defined_count": quotient_well_defined_count,
            "Z1_Z2_Z3_partition_preserving_count": pair_partition_preserving_count,
            "Z1_Z2_Z3_cycling_count": pair_cycling_count,
            "candidate_count": len(records),
            "label1_image_set": label1_images,
            "label1_image_cardinality": len(label1_images),
            "distinct_pair_cycle_patterns": pair_patterns,
            "distinct_sixpoint_permutations": len(point_patterns),
            "sixpoint_pattern_multiplicities": point_pattern_multiplicities,
            "sixpoint_pattern_label1_image_cardinalities": point_pattern_image_cardinalities,
        },
        "cecotti_phi6_conditional_cosets": {
            "phi6_weierstrass_permutation": cecotti_phi6,
            "phi6_candidate_count": len(phi6_records),
            "phi6_label1_image_set": phi6_label1_images,
            "phi6_inverse_weierstrass_permutation": cecotti_phi6_inv,
            "phi6_inverse_candidate_count": len(phi6_inv_records),
            "phi6_inverse_label1_image_set": phi6_inv_label1_images,
            "conditional_only_no_principal_b3_phi6_binding_claimed": True,
        },
        "sample_candidates": records[:24],
        "decision_boundary": {
            "principal_b3_member_identified": len(records) == 1,
            "principal_b3_label1_image_identified": len(label1_images) == 1,
            "boundary_geometry_prunes_order3_candidates": len(records) < h_cycle_count,
            "cecotti_phi6_binding_source_locked": False,
            "residue_specific_commutator_obtained": False,
            "survivors_current_credit": [73, 97, 235],
            "Q602_excluded": False,
            "O210_excluded": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
