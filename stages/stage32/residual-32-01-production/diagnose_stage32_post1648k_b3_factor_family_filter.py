#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
E_PATH = HERE / "diagnose_stage32_post1648e_b3_boundary_weierstrass_filter.py"
POST1550 = HERE / "post1550-b3-v4-torsor-normalizer.json"
POST1563 = HERE / "post1563-ambient-symmetry-exhaustion-batch.json"
BOUNDARY = HERE / "post1473-boundary-label-weierstrass-adapter.json"
SATAKE = HERE / "post1473-x8-satake-boundary-marking.json"
POST1648J = HERE / "post1648j-cecotti-trace-orientation-correction.json"

EXPECTED_POST1550 = "1225ca34034f1f1dacb2f3e1f46e7f3d15a6008a5e6b03960109f7bc992b5e95"
EXPECTED_POST1563 = "9dbf0bcb144824a14497b663da2200f94d7250bfc755a37d1d65ca0b565fbb2e"
EXPECTED_BOUNDARY = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
EXPECTED_SATAKE = "69a2a6d3cdf7b0d5c6162424a8102ec41cd09ac7e303469d30577d454363e31d"
EXPECTED_J = "3f6fd55ced259c6f28949df61865e22d43a669a50bdaf2adf5ddcd88411a48ec"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


E = load_module(E_PATH, "stage32_post1648k_base_e")


def canonical(doc: dict) -> str:
    body = dict(doc)
    field = "canonical_sha256_without_this_field" if "canonical_sha256_without_this_field" in body else "canonical_sha256"
    claimed = body.pop(field)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def inverse_map(p: dict[int, int]) -> dict[int, int]:
    return {v: k for k, v in p.items()}


post1550 = json.loads(POST1550.read_text())
post1563 = json.loads(POST1563.read_text())
boundary = json.loads(BOUNDARY.read_text())
satake = json.loads(SATAKE.read_text())
j = json.loads(POST1648J.read_text())
assert canonical(post1550) == EXPECTED_POST1550
assert canonical(post1563) == EXPECTED_POST1563
assert canonical(boundary) == EXPECTED_BOUNDARY
assert canonical(satake) == EXPECTED_SATAKE
assert canonical(j) == EXPECTED_J

normalizer = post1550["torsor_normalizer"]
assert normalizer["same_lift_on_both_factors_normalizes_H_diag"] is True
assert normalizer["diagonal_b3_lift_to_X_exists"] is True
assert normalizer["covers"] == "b3 x b3 on C0 x C0"
route = post1563["routes"]["C_principal_b3_membership"]
assert route["beta_B_exists_as_box_automorphism"] is True
assert route["beta_B_in_retained_stoll_group"] is True

factor = satake["factor_marking"]
first = set(factor["first_factor_cusp_z_fixed_curves"])
second = set(factor["second_factor_cusp_w_fixed_curves"])
assert len(first) == len(second) == 6 and first.isdisjoint(second)
assert first | second == set(range(33, 45))

boundary_map = {int(k): int(v) for k, v in boundary["boundary_label_to_weierstrass_id"].items()}
fibers = {i: set() for i in range(1, 7)}
for label, wid in boundary_map.items():
    fibers[wid].add(label)
pair_sets = {
    "Z1": frozenset(boundary["cusp_pairs"]["Z1"]),
    "Z2": frozenset(boundary["cusp_pairs"]["Z2"]),
    "Z3": frozenset(boundary["cusp_pairs"]["Z3"]),
}


def pair_action(wperm: dict[int, int]) -> dict[str, str]:
    out = {}
    for pname, pset in pair_sets.items():
        image = frozenset(wperm[x] for x in pset)
        target = next((q for q, qset in pair_sets.items() if qset == image), None)
        if target is None:
            raise AssertionError
        out[pname] = target
    return out


cecotti_phi6 = {1: 2, 2: 5, 3: 6, 4: 3, 5: 1, 6: 4}
cecotti_phi6_inv = inverse_map(cecotti_phi6)
assert j["ordered_generator_pair_enumeration"]["cecotti_B7_B8_trace_orbit"] == "+r"
assert j["correction_to_post1648b"]["compatible_orientation_orbit"] == "inner conjugates of (S,T^-1)"

marking_mod = E.load_module(E.MARKING_FILE, "stage32_post1648k_marking")
marking = marking_mod.load()
perms = [[int(x) for x in p] for p in marking["aut_action"]["permutations_1based"]]
group = E.close_group([(f"g{i}", perms[i - 1]) for i in range(1, 10)])
assert len(group) == 1536
identity = list(range(1, 141))


def word(indices):
    out = identity
    for i in indices:
        out = E.compose(out, perms[i - 1])
    return out


h_perms = {
    "id": identity,
    "u": word((7, 9)),
    "v": word((7, 8)),
    "uv": word((8, 9)),
}
h_lookup = {tuple(p): name for name, p in h_perms.items()}

records = []
for p_tuple, word_name in group.items():
    p = list(p_tuple)
    if p == identity or E.power(p, 3) != identity:
        continue
    pinv = E.inverse(p)
    induced_h = {}
    ok = True
    for hname, h in h_perms.items():
        conj = E.compose(E.compose(pinv, h), p)
        cname = h_lookup.get(tuple(conj))
        if cname is None:
            ok = False
            break
        induced_h[hname] = cname
    if not ok or not all(induced_h[name] != name for name in ("u", "v", "uv")):
        continue
    if {p[label - 1] for label in range(33, 45)} != set(range(33, 45)):
        continue
    wid_perm = {}
    for wid, labels in fibers.items():
        image_wids = {boundary_map[p[label - 1]] for label in labels}
        if len(image_wids) != 1:
            break
        wid_perm[wid] = next(iter(image_wids))
    if len(wid_perm) != 6 or set(wid_perm.values()) != set(range(1, 7)):
        continue
    try:
        paction = pair_action(wid_perm)
    except AssertionError:
        continue
    if not all(paction[name] != name for name in ("Z1", "Z2", "Z3")):
        continue

    image_first = {p[x - 1] for x in first}
    image_second = {p[x - 1] for x in second}
    family_action = (
        "PRESERVE_EACH_FACTOR"
        if image_first == first and image_second == second
        else "SWAP_FACTORS"
        if image_first == second and image_second == first
        else "MIXED"
    )
    records.append({
        "word": word_name,
        "label1_image": p[0],
        "weierstrass_permutation": wid_perm,
        "pair_permutation": paction,
        "factor_family_action": family_action,
    })

assert len(records) == 32
from collections import Counter
all_family = Counter(r["factor_family_action"] for r in records)
inv_records = [r for r in records if r["weierstrass_permutation"] == cecotti_phi6_inv]
assert len(inv_records) == 4
inv_family = Counter(r["factor_family_action"] for r in inv_records)
preserve_records = [r for r in records if r["factor_family_action"] == "PRESERVE_EACH_FACTOR"]
inv_preserve = [r for r in inv_records if r["factor_family_action"] == "PRESERVE_EACH_FACTOR"]

result = {
    "schema": "STAGE32_POST1648K_B3_FACTOR_FAMILY_FILTER_DIAGNOSTIC_V1",
    "source_locks": {
        "post1550": EXPECTED_POST1550,
        "post1563": EXPECTED_POST1563,
        "boundary_weierstrass": EXPECTED_BOUNDARY,
        "satake_factor_marking": EXPECTED_SATAKE,
        "post1648J": EXPECTED_J,
    },
    "semantic_requirement": "beta_B comes from the same b3 lift on both X(8) factors, so it preserves the first-factor and second-factor Satake boundary families separately",
    "counts": {
        "pre_factor_candidate_count": len(records),
        "all_factor_family_actions": dict(sorted(all_family.items())),
        "factor_preserving_candidate_count": len(preserve_records),
        "factor_preserving_label1_images": sorted({r["label1_image"] for r in preserve_records}),
        "trace_oriented_phi6_inverse_candidate_count": len(inv_records),
        "trace_oriented_phi6_inverse_family_actions": dict(sorted(inv_family.items())),
        "trace_oriented_phi6_inverse_factor_preserving_count": len(inv_preserve),
        "trace_oriented_phi6_inverse_factor_preserving_label1_images": sorted({r["label1_image"] for r in inv_preserve}),
    },
    "trace_oriented_phi6_inverse_candidates": inv_records,
    "decision_boundary": {
        "factor_family_requirement_is_source_bound": True,
        "cecotti_inner_conjugating_element_source_bound": False,
        "principal_b3_member_identified": len(preserve_records) == 1,
        "absolute_delta0inf_retained_W_line_identified": False,
        "survivors_current_credit": [73,97,235],
        "Q602_excluded": False,
        "O210_excluded": False,
    },
}
print(json.dumps(result, sort_keys=True, separators=(",", ":")))
