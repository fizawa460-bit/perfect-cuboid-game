#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

import sympy
from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
STATE = HERE / "STATE.json"
N374_STATE = HERE.parent / "N374/STATE.json"
N374_RESULT = HERE.parent / "N374/RESULT.json"
FAMILY = ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py"
INDEXER = ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py"
HPERP = ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"

STATE_BLOB = "05c9453b9a4970d02ff44eb5c254eab9c5f57d31"
STATE_CANON = "a1e5bda4004ea599e7a9e27f90e7749deb3bf3c3742667fdebf94324b3989b8a"
N374_STATE_BLOB = "a0122c46ec8c72a87f5a510b8faf83205cce44fa"
N374_RESULT_BLOB = "4e6fde243d1ea4695f7472ce3444df2b0e3b002c"
FAMILY_BLOB = "90ff82ed312dcc0cb32cf207935945f550e29170"
INDEXER_BLOB = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"
HPERP_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
CUT196_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"

D = 8
E = 8
BLOCK_WIDTH = 113
RAW_BLOCK_COUNT = 11318
RAW_TERMINAL_COUNT = 1278934
SURVIVOR_BLOCK_COUNT = 7596
SURVIVOR_TERMINAL_COUNT = 858348
TARGET_POS = (2, 3, 7)
TARGET_LABELS = (103, 102, 101)
ASSIGNMENT_ORDER = (95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96)


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return csha(q)


def checked_json(path: Path, expected_blob: str, expected_canon: str | None = None) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
        req(canonical(obj) == expected_canon, f"canonical drift: {path}")
    return obj


def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def apply_terminal_perm(values: tuple[int, ...], perm: tuple[int, int, int]) -> tuple[int, ...]:
    out = list(values)
    for i, pos in enumerate(TARGET_POS):
        out[pos] = values[TARGET_POS[perm[i]]]
    return tuple(int(v) for v in out)


def row_permuted_matrix(P: Matrix, perm: tuple[int, int, int]) -> Matrix:
    source_for_new = {TARGET_LABELS[i]: TARGET_LABELS[perm[i]] for i in range(3)}
    rows = []
    for label in range(1, 141):
        source = source_for_new.get(label, label)
        rows.append([int(P[source - 1, j]) for j in range(P.cols)])
    return Matrix(rows)


def flatten_ints(value) -> set[int]:
    out: set[int] = set()
    if isinstance(value, int):
        out.add(int(value))
    elif isinstance(value, (list, tuple)):
        for item in value:
            out.update(flatten_ints(item))
    return out


def compose(p: tuple[int, int, int], q: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(p[q[i]] for i in range(3))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    checked_json(STATE, STATE_BLOB, STATE_CANON)
    checked_json(N374_STATE, N374_STATE_BLOB)
    n374 = checked_json(N374_RESULT, N374_RESULT_BLOB)
    req(n374["decision"]["next_exact_unit"] == "SOURCE_LOCKED_NUMERICAL_LEAF_INVARIANCE_SIGNATURE_PROTOTYPE", "N374 next unit drift")
    req(blob(FAMILY) == FAMILY_BLOB, "compressed terminal family blob drift")
    req(blob(INDEXER) == INDEXER_BLOB, "compressed terminal indexer blob drift")
    req(blob(HPERP) == HPERP_BLOB, "Hperp adapter blob drift")
    req(exact_head(args.cut196_root.resolve()) == CUT196_HEAD, "CUT196 exact head drift")

    family = load_module(FAMILY, "n375_family")
    cut196_path = args.cut196_root.resolve() / "stages/stage32/full178-cut/cut196_e8_common_adapter_wave4.py"
    cut196 = load_module(cut196_path, "n375_cut196")
    cut196.preflight()
    core = cut196.core
    P, blocks, g = core.load_picard_interface()
    idx = core.e8.indexer()

    req((idx.d, idx.e) == (D, E), "e8 indexer stratum drift")
    req(idx.exceptional_count == RAW_BLOCK_COUNT, "raw e8 block count drift")
    req(idx.terminal_count == RAW_TERMINAL_COUNT, "raw e8 terminal count drift")
    req(idx.normal_budget + 1 == BLOCK_WIDTH, "e8 block width drift")
    req(tuple(core.e8.ASSIGNMENT_ORDER) == ASSIGNMENT_ORDER, "assignment order drift")

    survivor_blocks = tuple(int(v) for v in core.e8.current_main_survivor_block_indices())
    req(len(survivor_blocks) == SURVIVOR_BLOCK_COUNT, "current-MAIN e8 survivor block count drift")
    req(len(set(survivor_blocks)) == SURVIVOR_BLOCK_COUNT, "current-MAIN e8 survivor block stream is not unique")
    req(all(0 <= block < RAW_BLOCK_COUNT for block in survivor_blocks), "current-MAIN e8 survivor block outside raw indexer")
    req(BLOCK_WIDTH * len(survivor_blocks) == SURVIVOR_TERMINAL_COUNT, "current-MAIN e8 survivor terminal count drift")

    special_positions = {0, 1, 4, 5, 6, 8, 9, 10}
    req(set(TARGET_POS).isdisjoint(special_positions), "candidate positions touch non-symmetric terminal predicate coordinates")
    req(set(TARGET_LABELS) == {ASSIGNMENT_ORDER[i] for i in TARGET_POS}, "candidate label/position map drift")
    req(all(label > 92 for label in TARGET_LABELS), "candidate labels are not exceptional")
    normal_structure_labels = flatten_ints(core.PACKS) | flatten_ints(blocks)
    req(set(TARGET_LABELS).isdisjoint(normal_structure_labels), "candidate exceptional labels enter fibre/cross-factor normal structures")

    selected_labels = [int(v) for v in g.selected_labels]
    req(len(selected_labels) == 64 and len(set(selected_labels)) == 64, "selected64 label set drift")
    Psel = P.extract([label - 1 for label in selected_labels], list(range(64)))
    req(Psel.det() != 0, "selected64 pairing matrix singular")
    Psel_inv = Psel.inv()

    hperp = load_module(HPERP, "n375_hperp")
    bundle = core.e8.d18.load_retained(core.e8.d18.RETAINED, "n375_bundle")
    marking = core.e8.d18.load_retained(core.e8.d18.MARKING, "n375_marking")
    G = Matrix(bundle["picard_gram_64x64"])
    _q, known_degree, _linear, _caps, hmeta = hperp._parse_hperp(marking["hperp_text"])
    basis_labels = [int(v) for v in hperp.RETAINED_BASIS_KNOWN_LABELS_1BASED]
    degree_row = Matrix([[int(known_degree[v - 1]) for v in basis_labels]])
    req(G.shape == (64, 64) and degree_row.shape == (1, 64), "retained Picard metric/degree shape drift")

    perms = [tuple(int(v) for v in p) for p in itertools.permutations(range(3))]
    identity = (0, 1, 2)
    results = []
    valid: list[tuple[int, int, int]] = []

    all_blocks = set(survivor_blocks)
    base_cache = {
        block: tuple(int(v) for v in idx.unrank(block * BLOCK_WIDTH))
        for block in survivor_blocks
    }
    req(
        all(base[4] == 0 and family.terminal_predicate(base, e=E, d=D) for base in base_cache.values()),
        "canonical current-MAIN e8 survivor block bases drift",
    )

    for perm in perms:
        Pperm = row_permuted_matrix(P, perm)
        Pperm_sel = Pperm.extract([label - 1 for label in selected_labels], list(range(64)))
        Tq = Psel_inv * Pperm_sel
        integral = all(sympy.denom(v) == 1 for v in Tq)
        unimodular = False
        full_pairing_equivariance = False
        gram_isometry = False
        degree_preserved = False
        det = None
        if integral:
            T = Matrix([[int(Tq[i, j]) for j in range(64)] for i in range(64)])
            det = int(T.det())
            unimodular = abs(det) == 1
            full_pairing_equivariance = P * T == Pperm
            gram_isometry = T.T * G * T == G
            degree_preserved = degree_row * T == degree_row

        mapped_blocks: list[int] = []
        terminal_family_closed = True
        for _block, base in base_cache.items():
            moved = apply_terminal_perm(base, perm)
            if not family.terminal_predicate(moved, e=E, d=D):
                terminal_family_closed = False
                break
            rank = int(idx.rank(moved))
            if rank % BLOCK_WIDTH != 0:
                terminal_family_closed = False
                break
            mapped_blocks.append(rank // BLOCK_WIDTH)
        block_bijection = (
            terminal_family_closed
            and len(mapped_blocks) == SURVIVOR_BLOCK_COUNT
            and set(mapped_blocks) == all_blocks
        )

        leaf_action = all([
            integral,
            unimodular,
            full_pairing_equivariance,
            gram_isometry,
            degree_preserved,
            block_bijection,
        ])
        if leaf_action:
            valid.append(perm)
        results.append({
            "perm_new_from_old_indices": list(perm),
            "pairing_label_action": {
                str(TARGET_LABELS[i]): int(TARGET_LABELS[perm[i]]) for i in range(3)
            },
            "current_main_survivor_block_bijection": block_bijection,
            "picard_coordinate_transform_integral": integral,
            "picard_coordinate_transform_determinant": det,
            "picard_coordinate_transform_unimodular": unimodular,
            "all140_pairing_equivariance": full_pairing_equivariance,
            "gram_isometry": gram_isometry,
            "degree_preserved": degree_preserved,
            "numerical_leaf_action_valid": leaf_action,
        })

    req(identity in valid, "identity permutation failed exact probe")
    valid_set = set(valid)
    subgroup_closed = all(compose(p, q) in valid_set for p in valid for q in valid)
    req(subgroup_closed, "valid numerical-leaf actions are not closed under composition")

    canonical_blocks: dict[int, set[int]] = {}
    for block, base in base_cache.items():
        orbit = set()
        for perm in valid:
            moved = apply_terminal_perm(base, perm)
            rank = int(idx.rank(moved))
            orbit.add(rank // BLOCK_WIDTH)
        req(orbit <= all_blocks, "valid action left current-MAIN e8 survivor family")
        rep = min(orbit)
        canonical_blocks.setdefault(rep, set()).update(orbit)

    covered = set().union(*canonical_blocks.values()) if canonical_blocks else set()
    req(covered == all_blocks, "block orbit quotient does not cover current-MAIN e8 survivor family")
    orbit_sizes = Counter(len(v) for v in canonical_blocks.values())
    block_orbit_count = len(canonical_blocks)
    terminal_orbit_count = block_orbit_count * BLOCK_WIDTH
    strict_reduction = terminal_orbit_count < SURVIVOR_TERMINAL_COUNT
    reduction_ratio = [SURVIVOR_TERMINAL_COUNT, terminal_orbit_count]

    status = (
        "NONTRIVIAL_E8_NUMERICAL_LEAF_SYMMETRY_CANDIDATE"
        if len(valid) > 1 and strict_reduction
        else "IDENTITY_ONLY_E8_NUMERICAL_LEAF_SYMMETRY"
    )

    out = {
        "schema": "STAGE32_32_01_178_N375_E8_S3_NUMERICAL_LEAF_SYMMETRY_RESULT_V1",
        "status": status,
        "scope": {
            "row_id": "g1-d008",
            "d": D,
            "e": E,
            "raw_e8_terminal_count": RAW_TERMINAL_COUNT,
            "raw_e8_block_count": RAW_BLOCK_COUNT,
            "current_main_survivor_terminal_count": SURVIVOR_TERMINAL_COUNT,
            "current_main_survivor_block_count": SURVIVOR_BLOCK_COUNT,
            "block_width": BLOCK_WIDTH,
            "full178_global_scope": False,
            "effectivity_or_lift_invariance_proved": False,
        },
        "candidate": {
            "coordinate_positions": list(TARGET_POS),
            "pairing_labels": list(TARGET_LABELS),
            "ambient_group": "S3",
            "ambient_group_order": 6,
            "permutation_results": results,
        },
        "retained_action": {
            "valid_permutations_new_from_old_indices": [list(p) for p in valid],
            "group_order": len(valid),
            "subgroup_closed": subgroup_closed,
            "block_orbit_count": block_orbit_count,
            "terminal_orbit_count": terminal_orbit_count,
            "block_orbit_size_histogram": {str(k): int(v) for k, v in sorted(orbit_sizes.items())},
            "strict_terminal_orbit_reduction": strict_reduction,
            "terminal_to_orbit_count_ratio": reduction_ratio,
        },
        "proof_surface": {
            "terminal_predicate_symmetry_exact_by_coordinate_support": True,
            "candidate_labels_disjoint_from_fibre_and_cross_factor_normal_structures": True,
            "picard_integral_unimodular_action_checked": True,
            "all140_pairing_equivariance_checked": True,
            "picard_gram_isometry_checked": True,
            "degree_preservation_checked": True,
            "exact_rank_unrank_block_bijection_checked_for_all_7596_current_main_survivor_blocks": True,
            "hperp_text_sha256": hmeta["hperp_text_sha256"],
        },
        "interpretation": {
            "n101_globally_reopened": False,
            "why_not_global": "Only the exact current-MAIN e=8 g1-d008 numerical Picard leaf is tested; no all-strata FULL178 action and no lift/effectivity factorization is proved.",
            "next_exact_unit": "IF_NONTRIVIAL_GENERALIZE_ACTION_TO_OTHER_STRATA_WITH_EXACT_MULTIPLICITY_CONSERVATION_ELSE_SEARCH_DIFFERENT_AFFINE_SIGNATURE",
        },
        "credit": {
            "main_pruning_credit": False,
            "full178_complete": False,
            "n101_reopened_credit": False,
            "numerical_leaf_compression_credit": False,
            "effectivity_final": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    args.output.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": status,
        "valid_group_order": len(valid),
        "valid_permutations": [list(p) for p in valid],
        "block_orbit_count": block_orbit_count,
        "terminal_orbit_count": terminal_orbit_count,
        "strict_reduction": strict_reduction,
        "canonical": out["canonical_sha256_without_this_field"],
        "full178_complete": False,
        "main_pruning_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
