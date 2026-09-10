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
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
sys.path.insert(0, str(RESIDUAL))

import hperp_integral_adapter as hia
from pairing_prefix_engine import INDLIST

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_HPERP_ADAPTER_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
EXPECTED_INCIDENCE_CANONICAL = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
EXPECTED_TRANSVECTION_CANONICAL = "83fd16fdaac674a3f63b4b2dac498136f1bc584c9e06d89f1aa1a7bdc4c30386"

CURRENT_EXCEPTIONAL_PREFIX = [93,94,95,96,97,98,99,101,102,103]
PAIR_KEYS = [
    "43:41","42:44","39:37","38:40","35:33","34:36",
    "35:36","34:33","38:37","39:40","43:44","42:41",
]
PAIR_EXCEPTIONAL_LABELS = {
    "43:41":[93,94,95,96],
    "42:44":[97,98,99,100],
    "39:37":[101,102,103,104],
    "38:40":[105,106,107,108],
    "35:33":[109,110,111,112],
    "34:36":[113,114,115,116],
    "35:36":[117,118,123,124],
    "34:33":[119,120,121,122],
    "38:37":[125,126,131,132],
    "39:40":[127,128,129,130],
    "43:44":[133,134,139,140],
    "42:41":[135,136,137,138],
}
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
    return rank


def isum_rows(P: Matrix, labels: list[int]) -> list[int]:
    return [sum(int(P[label-1, j]) for label in labels) for j in range(P.cols)]


def main() -> None:
    adapter_path = RESIDUAL / "hperp_integral_adapter.py"
    raw = adapter_path.read_bytes()
    blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    if blob != EXPECTED_HPERP_ADAPTER_BLOB:
        raise ValueError(f"hperp adapter blob regression: {blob}")

    incidence = json.loads((RESIDUAL / "post1473-x8-marked-exceptional-incidence.json").read_text())
    inc_claimed = incidence.pop("canonical_sha256_without_this_field")
    if csha(incidence) != inc_claimed or inc_claimed != EXPECTED_INCIDENCE_CANONICAL:
        raise ValueError("incidence canonical regression")
    incidence["canonical_sha256_without_this_field"] = inc_claimed
    derived = {key: [] for key in PAIR_KEYS}
    for row in incidence["rows"]:
        key = f"{row['first_factor_boundary_label']}:{row['second_factor_boundary_label']}"
        derived[key].append(int(row["exceptional_label"]))
    if {k: sorted(v) for k,v in derived.items()} != {k: sorted(v) for k,v in PAIR_EXCEPTIONAL_LABELS.items()}:
        raise ValueError("pair-to-exceptional incidence regression")

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

    _, degree_col, _, _, _ = hia._parse_hperp(marking["hperp_text"])
    basis_labels = hia.RETAINED_BASIS_KNOWN_LABELS_1BASED
    degree = [int(degree_col[label-1,0]) for label in basis_labels]
    e_total = isum_rows(P, list(range(93,141)))
    row_by_label = {label: [int(P[label-1,j]) for j in range(64)] for label in range(1,141)}

    obs_named = [("degree", degree), ("exceptional_total", e_total), ("x4_label49", row_by_label[49])]
    obs_named += [(f"exceptional_label{label}", row_by_label[label]) for label in CURRENT_EXCEPTIONAL_PREFIX]
    obs_rows = [gf2_row(row) for _, row in obs_named]
    obs_rank = gf2_rank(obs_rows)

    pair_rows = [gf2_row(isum_rows(P, PAIR_EXCEPTIONAL_LABELS[key])) for key in PAIR_KEYS]
    pair_rank = gf2_rank(pair_rows)
    joint_rank = gf2_rank(obs_rows + pair_rows)
    residual_rank = joint_rank - obs_rank
    individually_determined = [i for i,row in enumerate(pair_rows) if gf2_rank(obs_rows+[row]) == obs_rank]

    # Pair masses partition all 48 exceptional labels, so their parity sum must equal e mod 2.
    pair_sum = [sum(row[j] for row in pair_rows) & 1 for j in range(64)]
    if pair_sum != list(gf2_row(e_total)):
        raise ValueError("pair-mass partition/e-total parity regression")

    # N355 can expose arbitrary exceptional group sums directly. Find the smallest subset of the
    # twelve true M_p group sums whose parity, together with the current prefix, determines all twelve.
    minimal_group_count = None
    minimal_group_subsets = []
    for k in range(13):
        for subset in itertools.combinations(range(12), k):
            rows = obs_rows + [pair_rows[i] for i in subset]
            if gf2_rank(rows + pair_rows) == gf2_rank(rows):
                minimal_group_count = k
                minimal_group_subsets.append(list(subset))
        if minimal_group_count is not None:
            break

    selected_exceptional = [label for label in INDLIST if 93 <= label <= 140]
    selected_rows = [gf2_row(row_by_label[label]) for label in selected_exceptional]
    residual_after_selected = gf2_rank(obs_rows + selected_rows + pair_rows) - gf2_rank(obs_rows + selected_rows)

    old_signature = [m & 1 for m in OLD_V6_PAIR_MASSES]
    if old_signature != [1,1,1,1,0,0,1,1,0,0,0,0]:
        raise ValueError("old V6 parity signature regression")

    body = {
        "schema": "STAGE32_32_01_178_SMITH_CURRENT_PREFIX_EXCEPTIONAL_PAIR_MASS_PARITY_GAP_V2",
        "supersedes": {
            "invalid_model": "V1 treated M_p as a sum of two boundary-curve pairings; that model is false and grants no credit.",
            "repair": "M_p is the sum of exceptional contact masses over the four marked exceptional curves incident to the ordered cusp pair."
        },
        "source_locks": {
            "hperp_adapter_blob_sha1": blob,
            "retained_bundle_canonical": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical": EXPECTED_MARKING_CANONICAL,
            "marked_exceptional_incidence_canonical": EXPECTED_INCIDENCE_CANONICAL,
            "old_weierstrass_transvection_artifact_canonical": EXPECTED_TRANSVECTION_CANONICAL,
            "old_smith_hostile_review": 5147627146
        },
        "pair_mass_semantics": {
            "ordered_pairs": PAIR_KEYS,
            "exceptional_label_groups": [PAIR_EXCEPTIONAL_LABELS[k] for k in PAIR_KEYS],
            "each_group_size": 4,
            "groups_partition_93_through_140": sorted(sum((PAIR_EXCEPTIONAL_LABELS[k] for k in PAIR_KEYS), [])) == list(range(93,141)),
            "old_v6_pair_masses": OLD_V6_PAIR_MASSES,
            "old_v6_pair_parity_signature": old_signature
        },
        "current_observables": {
            "names": [name for name,_ in obs_named],
            "mod2_rank": obs_rank
        },
        "exact_gap": {
            "pair_mass_parity_map_rank": pair_rank,
            "joint_rank_with_current_observables": joint_rank,
            "residual_pair_mass_parity_rank_beyond_current_observables": residual_rank,
            "individually_determined_pair_indices_0based": individually_determined,
            "pair_parity_xor_equals_exceptional_total_parity": True,
            "minimal_additional_true_pair_group_sums_to_determine_all_pair_parities": minimal_group_count,
            "minimal_group_subset_count": len(minimal_group_subsets),
            "minimal_group_subsets_0based_first30": minimal_group_subsets[:30]
        },
        "selected64_comparison": {
            "selected_exceptional_labels": selected_exceptional,
            "residual_pair_mass_rank_after_current_plus_all_selected_exceptional_labels": residual_after_selected
        },
        "interpretation": {
            "current_prefix_already_determines_old_transvection_pair_parities": residual_rank == 0,
            "direct_current_to_smith_adapter_established": False,
            "next_route": "Use the exact residual rank and N355-style exceptional group sums to expose only the missing true M_p parities; then reconstruct the Weierstrass parity action. Common-cover/X(8)-V4 hypotheses still require a separate semantic adapter before any MAIN pruning credit."
        },
        "credit": {
            "main_pruning_credit": False,
            "full178_completion": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_claim": False,
            "merge_authorized": False
        }
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    print(json.dumps(body, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
