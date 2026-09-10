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

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_HPERP_ADAPTER_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
CURRENT_EXCEPTIONAL_PREFIX = [93,94,95,96,97,98,99,101,102,103]
BOUNDARY_PACKS = [[33,36,37,40,41,44], [34,35,38,39,42,43]]
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


def isum_rows(M: Matrix, labels: list[int]) -> list[int]:
    return [sum(int(M[label-1, j]) for label in labels) for j in range(M.cols)]


def row_sum(M: Matrix, labels: list[int]) -> Matrix:
    out = Matrix.zeros(1, M.cols)
    for label in labels:
        out += M.row(label - 1)
    return out


def main() -> None:
    raw = (RESIDUAL / "hperp_integral_adapter.py").read_bytes()
    blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    if blob != EXPECTED_HPERP_ADAPTER_BLOB:
        raise ValueError(f"hperp adapter blob regression: {blob}")

    bundle = load_retained(RETAINED, "s32_smith_factor_bundle")
    marking = load_retained(MARKING, "s32_smith_factor_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = hia.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    # Recover the two current factor-fibre classes exactly as N352 does.
    fibre_classes = []
    fibre_blocks = []
    for pack in BOUNDARY_PACKS:
        rows = []
        block_labels = []
        seen = []
        for label in pack:
            inc = [j for j in range(93,141) if int(full[label-1,j-1]) == 1]
            if len(inc) != 8:
                raise ValueError(f"boundary incidence regression label={label}")
            F = 2 * coords.row(label-1) + row_sum(coords, inc)
            rows.append(F)
            block_labels.append(inc)
            seen.extend(inc)
        if sorted(seen) != list(range(93,141)):
            raise ValueError("factor fibre blocks do not partition all 48 exceptionals")
        if any(F != rows[0] for F in rows[1:]):
            raise ValueError("six special fibres are not linearly equivalent")
        fibre_classes.append(rows[0])
        fibre_blocks.append(block_labels)

    f1 = [int(v) for v in list(fibre_classes[0] * gram)]
    f2 = [int(v) for v in list(fibre_classes[1] * gram)]

    _, degree_col, _, _, _ = hia._parse_hperp(marking["hperp_text"])
    basis_labels = hia.RETAINED_BASIS_KNOWN_LABELS_1BASED
    degree = [int(degree_col[label-1,0]) for label in basis_labels]
    if [a+b for a,b in zip(f1,f2)] != degree:
        raise ValueError("exact factor-degree identity n1+n2=d regression")

    e_total = isum_rows(P, list(range(93,141)))
    row_by_label = {label: [int(P[label-1,j]) for j in range(64)] for label in range(1,141)}
    obs_named = [("degree", degree), ("exceptional_total", e_total), ("x4_label49", row_by_label[49])]
    obs_named += [(f"exceptional_label{label}", row_by_label[label]) for label in CURRENT_EXCEPTIONAL_PREFIX]
    obs_rows = [gf2_row(row) for _,row in obs_named]

    pair_rows = [gf2_row(isum_rows(P, PAIR_EXCEPTIONAL_LABELS[key])) for key in PAIR_KEYS]
    base_rank = gf2_rank(obs_rows)
    base_residual = gf2_rank(obs_rows + pair_rows) - base_rank

    f1_mod2 = gf2_row(f1)
    f2_mod2 = gf2_row(f2)
    f1_determined = gf2_rank(obs_rows + [f1_mod2]) == base_rank
    f2_determined = gf2_rank(obs_rows + [f2_mod2]) == base_rank
    obs_factor = obs_rows + [f1_mod2]
    factor_rank = gf2_rank(obs_factor)
    factor_residual = gf2_rank(obs_factor + pair_rows) - factor_rank

    # Verify every special-fibre block gives the same factor parity and identify
    # which two marked four-exceptional pair groups constitute it.
    pair_by_set = {frozenset(v): i for i,v in enumerate(PAIR_EXCEPTIONAL_LABELS.values())}
    factor_block_pair_indices = []
    for fi, blocks in enumerate(fibre_blocks):
        expected = f1_mod2 if fi == 0 else f2_mod2
        entries = []
        for inc in blocks:
            groups = [idx for s,idx in pair_by_set.items() if s.issubset(set(inc))]
            if len(groups) != 2:
                raise ValueError(f"special fibre does not split into two marked pair groups: {inc} -> {groups}")
            row = tuple(pair_rows[groups[0]][j] ^ pair_rows[groups[1]][j] for j in range(64))
            if row != expected:
                raise ValueError("special-fibre parity / pair-group parity regression")
            entries.append(groups)
        factor_block_pair_indices.append(entries)

    minimal_group_count = None
    minimal_group_subsets = []
    for k in range(13):
        for subset in itertools.combinations(range(12), k):
            rows = obs_factor + [pair_rows[i] for i in subset]
            if gf2_rank(rows + pair_rows) == gf2_rank(rows):
                minimal_group_count = k
                minimal_group_subsets.append(list(subset))
        if minimal_group_count is not None:
            break

    body = {
        "schema": "STAGE32_32_01_178_SMITH_CURRENT_FACTOR_DEGREE_PARITY_REDUCTION_V1",
        "status": "PROVISIONAL_EXACT_LINEAR_ALGEBRA_NO_MAIN_CREDIT",
        "source_locks": {
            "hperp_adapter_blob_sha1": blob,
            "retained_bundle_canonical": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical": EXPECTED_MARKING_CANONICAL,
            "n352_factor_fibre_reconstruction_replayed": True,
        },
        "factor_geometry": {
            "boundary_packs": BOUNDARY_PACKS,
            "fibre_blocks_exceptional_labels": fibre_blocks,
            "factor_block_pair_indices_0based": factor_block_pair_indices,
            "exact_n1_plus_n2_equals_degree": True,
            "mod2_f1_equals_f2_for_even_current_degree": True,
        },
        "current_observable_algebra": {
            "observable_names": [name for name,_ in obs_named],
            "base_mod2_rank": base_rank,
            "pair_mass_parity_map_rank": gf2_rank(pair_rows),
            "residual_pair_mass_rank_before_factor_parity": base_residual,
            "f1_parity_already_determined_by_current_prefix": f1_determined,
            "f2_parity_already_determined_by_current_prefix": f2_determined,
            "rank_after_adjoining_f1_parity": factor_rank,
            "residual_pair_mass_rank_after_factor_parity": factor_residual,
            "minimal_additional_true_pair_group_sums_after_factor_parity": minimal_group_count,
            "minimal_group_subsets_0based": minimal_group_subsets,
        },
        "interpretation": {
            "factor_parity_is_a_new_pair_mass_observable": not f1_determined,
            "factor_parity_reduces_pair_mass_gap": factor_residual < base_residual,
            "remaining_pair_mass_bits_after_factor_parity": factor_residual,
            "next_route": "If factor degree parity can be exposed from the current retained terminal/stratum state without new geometry, only the reported remaining true pair-group parity needs materialization before exact three-transposition census. Otherwise factor parity itself is one of the missing data bits.",
        },
        "credit": {
            "main_pruning_credit": False,
            "n350_producer_registration": False,
            "full178_completion": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "perfect_cuboid_claim": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    print(json.dumps(body, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
