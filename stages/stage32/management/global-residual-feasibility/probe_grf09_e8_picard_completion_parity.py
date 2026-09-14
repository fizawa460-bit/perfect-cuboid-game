#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

INTERFACE_BLOB = "8a30e3aa30777460f344eb19836dc725dd442329"
INTERFACE_CANON = "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6"
FAMILY_BLOB = "90ff82ed312dcc0cb32cf207935945f550e29170"
INDEXER_BLOB = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"
PREFIX_BLOB = "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"
BUNDLE_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
BUNDLE_CANON = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
NORMAL_INDEX = 4


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked_json(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(blob(path) == expected_blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift {path}")
    req(canon(obj) == expected_canon, f"canonical drift {path}")
    return obj


def hnf_contains(H: Matrix, b: Matrix) -> bool:
    n = H.rows
    req(H.cols == n and b.rows == n and b.cols == 1, "HNF shape")
    y = [0] * n
    for i in range(n - 1, -1, -1):
        rhs = int(b[i, 0])
        for j in range(i + 1, n):
            rhs -= int(H[i, j]) * y[j]
        diag = int(H[i, i])
        req(diag > 0, f"HNF diagonal {i}")
        if rhs % diag:
            return False
        y[i] = rhs // diag
    return True


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    residual = repo / "stages/stage32/residual-32-01-production"
    interface_path = repo / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
    bundle_path = repo / "stages/stage33/33-07/picard_base_rows_retained.py"
    prefix_path = residual / "pairing_prefix_engine.py"
    family_path = residual / "compressed_terminal_family.py"
    indexer_path = residual / "compressed_terminal_indexer.py"

    interface = checked_json(interface_path, INTERFACE_BLOB, INTERFACE_CANON)
    req(blob(family_path) == FAMILY_BLOB, "compressed family blob drift")
    req(blob(indexer_path) == INDEXER_BLOB, "compressed indexer blob drift")
    req(blob(prefix_path) == PREFIX_BLOB, "pairing prefix blob drift")
    req(blob(bundle_path) == BUNDLE_BLOB, "retained Picard bundle blob drift")

    sys.path.insert(0, str(residual))
    bundle_mod = load_module(bundle_path, "grf09_retained_bundle")
    bundle = bundle_mod.load()
    req(bundle["canonical_sha256"] == BUNDLE_CANON, "retained bundle canonical drift")

    from pairing_prefix_engine import RetainedBasisPairingTransform
    from compressed_terminal_indexer import CompressedTerminalIndexer

    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    req(int(transform.den) == 8, "selected64 inverse denominator drift")
    tmap = interface["terminal_to_picard64_map"]
    req(tmap["terminal_assignment_labels_1based"] == ASSIGNMENT_LABELS, "assignment labels drift")
    req(tmap["inverse_denominator"] == 8, "interface denominator drift")
    req(transform.certificate["inverse_integer_sha256"] == tmap["inverse_integer_matrix_sha256"], "inverse matrix hash drift")

    labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    fixed_positions = [labels.index(label) for label in ASSIGNMENT_LABELS]
    req(fixed_positions == tmap["terminal_fixed_selected_positions_0based"], "fixed positions drift")
    free_positions = [i for i in range(64) if i not in fixed_positions]
    req(free_positions == tmap["free_selected_positions_0based"], "free positions drift")

    B = transform.inverse_integer
    B_fixed = B.extract(list(range(64)), fixed_positions)
    B_free = B.extract(list(range(64)), free_positions)
    lattice = B_free.row_join(8 * Matrix.eye(64))
    H = hermite_normal_form(lattice)
    req(H.shape == (64, 64), "completion HNF rank drift")

    idx = CompressedTerminalIndexer(8, 8)
    width = idx.normal_budget + 1
    req(width == 113, "e8 width drift")
    block_count = idx.exceptional_count
    req(idx.terminal_count == block_count * width, "terminal factorization drift")

    block_records: list[tuple[tuple[int, ...], int]] = []
    mask_counts: Counter[int] = Counter()
    for block in range(block_count):
        base = tuple(int(v) for v in idx.unrank(block * width))
        req(base[NORMAL_INDEX] == 0, f"base x49 drift block={block}")
        mask = 0
        for r in range(8):
            x = list(base)
            x[NORMAL_INDEX] = r
            rhs = -(B_fixed * Matrix(x))
            if hnf_contains(H, rhs):
                mask |= 1 << r
        req(mask in (0x55, 0xAA), f"non-parity mask block={block} mask={mask:#x}")
        required = 0 if mask == 0x55 else 1
        block_records.append((base, required))
        mask_counts[mask] += 1

    feature_indices = [i for i in range(11) if i != NORMAL_INDEX]
    matching_models: list[int] = []
    # affine GF(2) models: bit 0 is constant; bits 1..10 correspond to feature_indices.
    for model in range(1 << (1 + len(feature_indices))):
        good = True
        for base, required in block_records:
            pred = model & 1
            for j, idx_i in enumerate(feature_indices, start=1):
                if (model >> j) & 1:
                    pred ^= base[idx_i] & 1
            if pred != required:
                good = False
                break
        if good:
            matching_models.append(model)
    req(matching_models, "no affine GF2 x49 parity model on full e8 family")
    model = min(matching_models)

    coeff = {"constant": model & 1}
    for j, idx_i in enumerate(feature_indices, start=1):
        coeff[f"x{idx_i}"] = (model >> j) & 1

    # Replay all 28,815 terminals against the fitted parity identity and exact HNF membership.
    sat = 0
    unsat = 0
    for rank in range(idx.terminal_count):
        x = tuple(int(v) for v in idx.unrank(rank))
        pred = coeff["constant"]
        for idx_i in feature_indices:
            if coeff[f"x{idx_i}"]:
                pred ^= x[idx_i] & 1
        parity_ok = (x[NORMAL_INDEX] & 1) == pred
        rhs = -(B_fixed * Matrix(x))
        exact = hnf_contains(H, rhs)
        req(exact == parity_ok, f"full replay mismatch rank={rank}")
        if exact:
            sat += 1
        else:
            unsat += 1

    even_blocks = int(mask_counts[0x55])
    odd_blocks = int(mask_counts[0xAA])
    req(sat == even_blocks * 57 + odd_blocks * 56, "SAT count reconstruction")
    req(unsat == even_blocks * 56 + odd_blocks * 57, "UNSAT count reconstruction")
    req(sat + unsat == idx.terminal_count, "partition count")

    summary = {
        "scope": "FULL_COMPRESSED_g1_d008_e8_255_BLOCK_FAMILY_PRE_CURRENT_RESIDUAL_INTERSECTION",
        "block_count": block_count,
        "terminal_count": idx.terminal_count,
        "completion_modulus": 8,
        "mask_distribution": {"0x55": even_blocks, "0xaa": odd_blocks},
        "affine_gf2_model_count": len(matching_models),
        "selected_affine_gf2_coefficients": coeff,
        "sat_terminal_count": sat,
        "unsat_terminal_count": unsat,
        "unsat_fraction": [unsat, idx.terminal_count],
        "credit": {
            "current_residual_subset_identity_proved": False,
            "main_pruning_credit": False,
            "double_charge_authorized": False,
            "full178_complete": False,
        },
    }
    print(json.dumps(summary, sort_keys=True, indent=2))
    print("PASS_GRF09_E8_PICARD_COMPLETION_PARITY_PROBE")


if __name__ == "__main__":
    main()
