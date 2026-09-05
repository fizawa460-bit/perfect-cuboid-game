#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_HPERP_TEXT_SHA256 = "af373f16d6ab2bb8aed6ca09e0a15c8b28d565cbec6f242a8b76c590df81bb4f"
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
PICARD_RANK = 64


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def row_mask(matrix, i: int) -> int:
    out = 0
    for j in range(matrix.cols):
        if int(matrix[i, j]) & 1:
            out |= 1 << j
    return out


def triangular_basis(rows: list[int]) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for value in rows:
        x = value
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return pivots


def reduce_by_basis(value: int, pivots: dict[int, int]) -> int:
    x = value
    while x:
        p = x.bit_length() - 1
        if p not in pivots:
            return x
        x ^= pivots[p]
    return 0


def dot2(a: int, b: int) -> int:
    return (a & b).bit_count() & 1


def solve_separator(equations: list[int], rhs: list[int]) -> int:
    if len(equations) != len(rhs):
        raise ValueError("equation/rhs length mismatch")
    rows = [int(a) | ((int(b) & 1) << PICARD_RANK) for a, b in zip(equations, rhs)]
    pivot_rows: list[tuple[int, int]] = []
    r = 0
    for c in range(PICARD_RANK):
        pivot = next((i for i in range(r, len(rows)) if (rows[i] >> c) & 1), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1):
                rows[i] ^= rows[r]
        pivot_rows.append((r, c))
        r += 1
        if r == len(rows):
            break
    mask = (1 << PICARD_RANK) - 1
    for row in rows:
        if (row & mask) == 0 and ((row >> PICARD_RANK) & 1):
            raise ValueError("separator system inconsistent")
    solution = 0
    for row_index, col in pivot_rows:
        if (rows[row_index] >> PICARD_RANK) & 1:
            solution |= 1 << col
    return solution


def main() -> None:
    hperp = load_module(HERE / "hperp_integral_adapter.py", "stage32_hperp_nonexceptional_preflight")
    bundle_mod = load_module(
        ROOT / "stages/stage33/33-07/picard_base_rows_retained.py",
        "stage32_hperp_bundle_preflight",
    )
    marking_mod = load_module(
        ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py",
        "stage32_hperp_marking_preflight",
    )
    bundle = bundle_mod.load()
    marking = marking_mod.load()
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise SystemExit("retained Picard bundle canonical moved")
    if bundle.get("upstream_git_blob_sha1") != EXPECTED_UPSTREAM_BLOB:
        raise SystemExit("retained Picard upstream blob moved")

    adapter = hperp.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    cert = adapter.certificate
    if cert["hperp"]["hperp_text_sha256"] != EXPECTED_HPERP_TEXT_SHA256:
        raise SystemExit("retained Hperp text hash moved")
    if cert["known_curve_count"] != NORMAL_COUNT + EXCEPTIONAL_COUNT:
        raise SystemExit("known curve count moved")
    if cert["picard_rank"] != PICARD_RANK:
        raise SystemExit("Picard rank moved")
    if cert["normal_curve_self_intersection"] != -4 or cert["exceptional_curve_self_intersection"] != -2:
        raise SystemExit("known-curve geometry partition moved")
    if not cert["selected64_change_of_basis_unimodular"]:
        raise SystemExit("selected64 geometric basis ceased to be unimodular")

    coords = adapter.class_coordinates_in_retained_basis
    if coords.shape != (140, 64):
        raise SystemExit(f"all140 coordinate shape moved: {coords.shape}")
    normal_rows = [row_mask(coords, i) for i in range(NORMAL_COUNT)]
    exceptional_rows = [row_mask(coords, i) for i in range(NORMAL_COUNT, NORMAL_COUNT + EXCEPTIONAL_COUNT)]
    exceptional_basis = triangular_basis(exceptional_rows)
    all_basis = triangular_basis(exceptional_rows + normal_rows)
    normal_basis = triangular_basis(normal_rows)

    escaping = [i for i, row in enumerate(normal_rows) if reduce_by_basis(row, exceptional_basis) != 0]
    if not escaping:
        result = {
            "verdict": "NO_NONEXCEPTIONAL_NORMAL_CURVE_FOUND",
            "exceptional_rank_F2": len(exceptional_basis),
            "normal_rank_F2": len(normal_basis),
            "all140_rank_F2": len(all_basis),
            "escaping_normal_count": 0,
            "adapter_canonical_sha256": cert["canonical_sha256_without_this_field"],
        }
        print(json.dumps(result, sort_keys=True))
        return

    first = escaping[0]
    target = normal_rows[first]
    separator = solve_separator(exceptional_rows + [target], [0] * EXCEPTIONAL_COUNT + [1])
    if any(dot2(separator, row) for row in exceptional_rows):
        raise SystemExit("separator does not annihilate exceptional span")
    if dot2(separator, target) != 1:
        raise SystemExit("separator does not detect chosen normal curve")

    selected64 = [int(v) for v in cert["selected64_known_labels_1based"]]
    selected_normal = [label for label in selected64 if label <= NORMAL_COUNT]
    result = {
        "verdict": "PASS_SOURCE_BOUND_NONEXCEPTIONAL_NORMAL_CURVE_MOD2",
        "geometry_model": "Hperp all140: labels 1..92 normal (-4), 93..140 exceptional (-2)",
        "exceptional_rank_F2": len(exceptional_basis),
        "normal_rank_F2": len(normal_basis),
        "all140_rank_F2": len(all_basis),
        "quotient_dimension_lower_bound_from_all140": len(all_basis) - len(exceptional_basis),
        "escaping_normal_count": len(escaping),
        "escaping_normal_labels_1based": [i + 1 for i in escaping],
        "first_escaping_normal_label_1based": first + 1,
        "first_escaping_is_in_selected64_geometric_basis": (first + 1) in selected64,
        "selected64_normal_label_count": len(selected_normal),
        "separator_support_retained_picard_coordinates_1based": [j + 1 for j in range(PICARD_RANK) if (separator >> j) & 1],
        "separator_annihilates_all_48_exceptionals": True,
        "separator_detects_first_escaping_normal": True,
        "adapter_canonical_sha256": cert["canonical_sha256_without_this_field"],
        "hperp_text_sha256": cert["hperp"]["hperp_text_sha256"],
        "all140_retained_coordinates_sha256": cert["all140_retained_coordinates_sha256"],
        "selected64_change_of_basis_sha256": cert["selected64_change_of_basis_sha256"],
        "credit": {
            "source_bound_actual_known_curve_nonexceptional_mod2_class": True,
            "q602_residue_specific_commutator": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
