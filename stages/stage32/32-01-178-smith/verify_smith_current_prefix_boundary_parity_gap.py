#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
sys.path.insert(0, str(RESIDUAL))

import hperp_integral_adapter as hia
from pairing_prefix_engine import INDLIST

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_HPERP_ADAPTER_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"

CURRENT_EXCEPTIONAL_PREFIX = [93,94,95,96,97,98,99,101,102,103]
BOUNDARY_LABELS = list(range(33,45))
# Ordered pair masses used by the hostile-audited old V6 Weierstrass parity/transvection adapter.
PAIR_LABELS = [
    (43,41),(42,44),(39,37),(38,40),(35,33),(34,36),
    (35,36),(34,33),(38,37),(39,40),(43,44),(42,41),
]
OLD_V6_PAIR_MASSES = [5,5,21,25,24,18,19,35,28,34,32,20]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained payload: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    payload = mod.load()
    if not isinstance(payload, dict):
        raise ValueError(f"retained payload is not dict: {path}")
    return payload


def gf2_row(values) -> tuple[int, ...]:
    return tuple(int(v) & 1 for v in values)


def gf2_rank(rows) -> int:
    a = [list(gf2_row(r)) for r in rows if any(int(v) & 1 for v in r)]
    if not a:
        return 0
    n = len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                a[i] = [x ^ y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def row_add(*rows) -> tuple[int, ...]:
    out = [0] * len(rows[0])
    for row in rows:
        for i, v in enumerate(row):
            out[i] ^= int(v) & 1
    return tuple(out)


def isum_rows(P: Matrix, labels: list[int]) -> list[int]:
    return [sum(int(P[label-1, j]) for label in labels) for j in range(P.cols)]


def main() -> None:
    # Fail closed on the compact adapter itself; do not read the retained denylist payloads in this script body.
    adapter_path = RESIDUAL / "hperp_integral_adapter.py"
    raw = adapter_path.read_bytes()
    blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    if blob != EXPECTED_HPERP_ADAPTER_BLOB:
        raise ValueError(f"hperp adapter blob regression: {blob}")

    bundle = load_retained(RETAINED, "s32_smith_bundle")
    marking = load_retained(MARKING, "s32_smith_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = hia.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    if P.shape != (140,64):
        raise ValueError("all140 pairing shape regression")

    # Recover the canonical-degree functional in the same retained Picard basis.
    _, degree_col, _, _, _ = hia._parse_hperp(marking["hperp_text"])
    basis_labels = hia.RETAINED_BASIS_KNOWN_LABELS_1BASED
    degree = [int(degree_col[label-1,0]) for label in basis_labels]
    e_total = isum_rows(P, list(range(93,141)))
    normal_total = isum_rows(P, list(range(1,93)))
    if normal_total != [19*degree[j] - 5*e_total[j] for j in range(64)]:
        raise ValueError("normal-total identity regression")

    row_by_label = {label: [int(P[label-1,j]) for j in range(64)] for label in range(1,141)}
    obs_named = [("degree", degree), ("exceptional_total", e_total), ("x4_label49", row_by_label[49])]
    obs_named += [(f"exceptional_label{label}", row_by_label[label]) for label in CURRENT_EXCEPTIONAL_PREFIX]
    obs_rows = [gf2_row(row) for _, row in obs_named]
    obs_rank = gf2_rank(obs_rows)

    target_rows = [row_add(gf2_row(row_by_label[a]), gf2_row(row_by_label[b])) for a,b in PAIR_LABELS]
    target_rank = gf2_rank(target_rows)
    joint_rank = gf2_rank(obs_rows + target_rows)
    residual_rank = joint_rank - obs_rank

    individually_determined = []
    for i, row in enumerate(target_rows):
        if gf2_rank(obs_rows + [row]) == obs_rank:
            individually_determined.append(i)

    direct_selected_boundary = [label for label in BOUNDARY_LABELS if label in INDLIST]
    direct_rows = [gf2_row(row_by_label[label]) for label in direct_selected_boundary]
    residual_after_direct_selected = gf2_rank(obs_rows + direct_rows + target_rows) - gf2_rank(obs_rows + direct_rows)

    # Exact minimal boundary-observable augmentation: among the twelve actual boundary pairings,
    # find the smallest subset whose parities make all twelve pair-mass parities determined.
    minimal_size = None
    minimal_subsets = []
    for k in range(len(BOUNDARY_LABELS) + 1):
        for subset in itertools.combinations(BOUNDARY_LABELS, k):
            rows = obs_rows + [gf2_row(row_by_label[label]) for label in subset]
            if gf2_rank(rows + target_rows) == gf2_rank(rows):
                minimal_size = k
                minimal_subsets.append(list(subset))
        if minimal_size is not None:
            break

    old_signature = [m & 1 for m in OLD_V6_PAIR_MASSES]
    expected_old_signature = [1,1,1,1,0,0,1,1,0,0,0,0]
    if old_signature != expected_old_signature:
        raise ValueError("old V6 parity signature regression")

    body = {
        "schema": "STAGE32_32_01_178_SMITH_CURRENT_PREFIX_BOUNDARY_PARITY_GAP_V1",
        "source_locks": {
            "hperp_adapter_blob_sha1": blob,
            "retained_bundle_canonical": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical": EXPECTED_MARKING_CANONICAL,
            "old_weierstrass_transvection_artifact_canonical": "83fd16fdaac674a3f63b4b2dac498136f1bc584c9e06d89f1aa1a7bdc4c30386",
            "old_smith_hostile_review": 5147627146,
        },
        "current_observables": {
            "names": [name for name,_ in obs_named],
            "mod2_rank": obs_rank,
            "n355_group_sums_add_no_new_linear_information": True,
            "normal_total_exactly_19d_minus_5e": True,
        },
        "old_transvection_boundary_parity_map": {
            "boundary_labels": BOUNDARY_LABELS,
            "ordered_pair_labels": [list(x) for x in PAIR_LABELS],
            "pair_parity_map_rank": target_rank,
            "joint_rank_with_current_observables": joint_rank,
            "residual_pair_parity_rank_beyond_current_observables": residual_rank,
            "individually_determined_pair_indices_0based": individually_determined,
            "old_v6_pair_masses": OLD_V6_PAIR_MASSES,
            "old_v6_pair_parity_signature": old_signature,
        },
        "prefix_extension": {
            "selected64_boundary_labels_already_coordinate_rows": direct_selected_boundary,
            "residual_rank_after_exposing_all_direct_selected_boundary_labels": residual_after_direct_selected,
            "minimal_actual_boundary_pairing_count_to_determine_all_pair_parities": minimal_size,
            "minimal_subset_count": len(minimal_subsets),
            "minimal_subsets_first20": minimal_subsets[:20],
        },
        "interpretation": {
            "current_prefix_already_determines_old_transvection_parities": residual_rank == 0,
            "direct_current_to_smith_adapter_established": False,
            "why_not": "The hostile-audited Smith obstruction still requires the fixed X(8)/V4 common-cover semantics. This computation only measures how much of the old boundary-parity observable is missing from the current Picard/N355 prefix.",
            "next_route": "If the residual rank is small, extend the exact pairing prefix by the certified minimal boundary observables, reconstruct the branch-permutation/transvection predicate stratumwise, and only then test a source-compatible Smith obstruction on the corresponding common-cover subpopulation.",
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
    body["canonical_sha256_without_this_field"] = csha(body)
    print(json.dumps(body, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
