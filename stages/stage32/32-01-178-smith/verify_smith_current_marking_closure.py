#!/usr/bin/env python3
"""Exact preflight: close the *numerical marking* gate for current Smith reuse.

This does NOT lift a numerical Picard class to an actual carrier/common-cover/
H-equivariant cellular assembly. It only verifies that the retained current
X(8) boundary/exceptional geometry already supplies an audited marking in
which the three single-transposition pair-mass signatures are the three
marked cusp-pair directions.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

STAGE32 = Path(__file__).resolve().parents[1]
RESIDUAL = STAGE32 / "residual-32-01-production"
HERE = Path(__file__).resolve().parent

INCIDENCE_CANONICAL = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
WEIERSTRASS_CANONICAL = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
CZERO_CANONICAL = "96e9d9b78201e99d98b31b8ece51c3e6227a2637c35356f012d0049d589a0f42"
PAIR_IMAGE_CANONICAL = "8c5acfb7d058cfe8c4fdbd94c1eb889578c331b03f83150889303c6bcbbc1b23"
MARKING_AUDIT_HEAD = "a2cd62cdcf8331827eca94453482244a2fd8bf0d"
MARKING_AUDIT_REVIEW = 5083834097
LOCATOR_COMMIT = "66147254a7893b38a57a07d75576ac72dc178a37"
LOCATOR_PATH = "docs/evidence-locator/index.json"


def canonical_without_field(obj: dict) -> str:
    y = dict(obj)
    y.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(y, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def require_canonical(obj: dict, expected: str, name: str) -> None:
    got = obj.get("canonical_sha256_without_this_field")
    if got != expected:
        raise AssertionError(f"{name} declared canonical drift: {got} != {expected}")
    calc = canonical_without_field(obj)
    if calc != expected:
        raise AssertionError(f"{name} canonical replay drift: {calc} != {expected}")


def load_locator() -> dict:
    raw = subprocess.check_output(
        ["git", "show", f"{LOCATOR_COMMIT}:{LOCATOR_PATH}"], text=True
    )
    return json.loads(raw)


def pair_image(argv: list[str]) -> dict:
    if len(argv) > 1:
        return load(Path(argv[1]))
    out = subprocess.check_output(
        [sys.executable, str(HERE / "verify_smith_pair_mass_image_classifier.py")],
        text=True,
    )
    return json.loads(out)


def connected_components(edges: set[tuple[int, int]]) -> list[tuple[set[int], set[int]]]:
    adj: dict[tuple[str, int], set[tuple[str, int]]] = defaultdict(set)
    for a, b in edges:
        u, v = ("L", a), ("R", b)
        adj[u].add(v)
        adj[v].add(u)
    unseen = set(adj)
    comps = []
    while unseen:
        start = min(unseen)
        q = deque([start])
        seen = {start}
        unseen.remove(start)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    unseen.discard(v)
                    q.append(v)
        left = {x for s, x in seen if s == "L"}
        right = {x for s, x in seen if s == "R"}
        comps.append((left, right))
    return sorted(comps, key=lambda z: min(z[0]))


def main() -> None:
    inc = load(RESIDUAL / "post1473-x8-marked-exceptional-incidence.json")
    wei = load(RESIDUAL / "post1473-boundary-label-weierstrass-adapter.json")
    cz = load(RESIDUAL / "post1473-x8-marked-node-czero-partition.json")
    cls = pair_image(sys.argv)
    locator = load_locator()

    require_canonical(inc, INCIDENCE_CANONICAL, "incidence")
    require_canonical(wei, WEIERSTRASS_CANONICAL, "weierstrass_adapter")
    require_canonical(cz, CZERO_CANONICAL, "c_zero_partition")
    require_canonical(cls, PAIR_IMAGE_CANONICAL, "pair_image_classifier")

    assets = {a["asset_id"]: a for a in locator["assets"]}
    for aid, canon in [
        ("EVID-S32-BOUNDARY-LABEL-WEIERSTRASS-ADAPTER", WEIERSTRASS_CANONICAL),
        ("EVID-S32-X8-MARKED-NODE-CZERO-PARTITION", CZERO_CANONICAL),
    ]:
        auth = assets[aid]["current_authority_snapshot"]
        assert auth["status"] == "AUDITED_PASS"
        assert auth["canonical_sha256"] == canon
        assert auth["audit_pass_head_sha"] == MARKING_AUDIT_HEAD
        assert auth["audit_pass_review_id"] == MARKING_AUDIT_REVIEW

    rows = inc["rows"]
    assert len(rows) == 48
    labels = [r["exceptional_label"] for r in rows]
    assert sorted(labels) == list(range(93, 141))
    edges = {(r["first_factor_boundary_label"], r["second_factor_boundary_label"]) for r in rows}
    edge_counts = Counter((r["first_factor_boundary_label"], r["second_factor_boundary_label"]) for r in rows)
    assert len(edges) == 12 and set(edge_counts.values()) == {4}

    comps = connected_components(edges)
    assert len(comps) == 3
    assert all(len(left) == len(right) == 2 for left, right in comps)
    assert all({(a, b) for a in left for b in right} <= edges for left, right in comps)

    wmap = {int(k): int(v) for k, v in wei["boundary_label_to_weierstrass_id"].items()}
    component_weierstrass_pairs = []
    for left, right in comps:
        lw, rw = {wmap[x] for x in left}, {wmap[x] for x in right}
        assert lw == rw and len(lw) == 2
        component_weierstrass_pairs.append(tuple(sorted(lw)))
    component_weierstrass_pairs = sorted(component_weierstrass_pairs)
    expected_pairs = sorted([tuple(sorted(x)) for x in wei["cusp_pairs"].values()])
    assert component_weierstrass_pairs == expected_pairs == [(1, 6), (2, 4), (3, 5)]

    zero_pairs = {tuple(map(int, k.split(":"))) for k in cz["structure"]["c_zero_pairs"]}
    nonzero_pairs = {tuple(map(int, k.split(":"))) for k in cz["structure"]["c_nonzero_pairs"]}
    assert zero_pairs.isdisjoint(nonzero_pairs)
    assert zero_pairs | nonzero_pairs == edges
    for left, right in comps:
        block = {(a, b) for a in left for b in right}
        for matching in (zero_pairs & block, nonzero_pairs & block):
            assert len(matching) == 2
            assert {a for a, _ in matching} == left
            assert {b for _, b in matching} == right

    transpositions = sorted(
        tuple(sorted(rec["nontrivial_cycles"][0]))
        for rec in cls["linear_image"]["classified_signatures"]
        if rec["single_transposition"]
    )
    assert transpositions == expected_pairs
    assert cls["linear_image"]["single_transposition_signature_count"] == 3

    out = {
        "schema": "STAGE32_32_01_178_SMITH_CURRENT_NUMERICAL_MARKING_CLOSURE_V1",
        "source_locks": {
            "incidence_canonical": INCIDENCE_CANONICAL,
            "weierstrass_adapter_canonical": WEIERSTRASS_CANONICAL,
            "c_zero_partition_canonical": CZERO_CANONICAL,
            "pair_image_classifier_canonical": PAIR_IMAGE_CANONICAL,
            "marking_hostile_audit_review": MARKING_AUDIT_REVIEW,
            "marking_hostile_audit_head": MARKING_AUDIT_HEAD,
            "evidence_locator_commit": LOCATOR_COMMIT,
        },
        "exact_result": {
            "exceptional_rows": 48,
            "realized_boundary_pairs": 12,
            "nodes_per_realized_pair": 4,
            "incidence_components": 3,
            "component_type": "K2,2",
            "canonical_unordered_weierstrass_pairs": [list(x) for x in expected_pairs],
            "c_zero_matching_per_component": True,
            "c_nonzero_complementary_matching_per_component": True,
            "pair_mass_single_transpositions": [list(x) for x in transpositions],
            "single_transpositions_equal_marked_cusp_pairs": True,
            "current_numerical_marking_gate_closed": True,
        },
        "remaining_semantic_gate": {
            "current_carrier_common_cover_h_equivariant_assembly_lift": False,
            "pair_mass_parity_is_not_carrier_branch_location": True,
            "c_sign_is_not_product_cover_v4_without_adapter": True,
            "numerical_marking_closure_does_not_prove_actual_carrier": True,
        },
        "credit": {
            "main_pruning_credit": False,
            "full178_completion": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_claim": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical_without_field(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
