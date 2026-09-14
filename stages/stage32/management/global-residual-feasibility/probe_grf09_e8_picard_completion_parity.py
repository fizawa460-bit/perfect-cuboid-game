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
CUT201_PREFLIGHT_BLOB = "87b2f139b576b3b8bddea336396c8c2da30014b1"
CUT201_PREFLIGHT_CANON = "2e09ff8e8f415f37b52f6f0395c6279276c57398222b02258ec962dbb0e0048b"
CUT201_EXACT_HEAD = "118c1df8f33759cc2e4da7e53fb8c8d7463a5bb0"
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
    repo = Path(__file__).resolve().parents[4]
    residual = repo / "stages/stage32/residual-32-01-production"
    interface_path = repo / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
    bundle_path = repo / "stages/stage33/33-07/picard_base_rows_retained.py"
    prefix_path = residual / "pairing_prefix_engine.py"
    family_path = residual / "compressed_terminal_family.py"
    indexer_path = residual / "compressed_terminal_indexer.py"
    cut201_path = repo / ".stage32-cut201/stages/stage32/full178-cut/CUT201-e8-common-adapter-wave9-preflight.json"

    interface = checked_json(interface_path, INTERFACE_BLOB, INTERFACE_CANON)
    cut201 = checked_json(cut201_path, CUT201_PREFLIGHT_BLOB, CUT201_PREFLIGHT_CANON)
    req(blob(family_path) == FAMILY_BLOB, "compressed family blob drift")
    req(blob(indexer_path) == INDEXER_BLOB, "compressed indexer blob drift")
    req(blob(prefix_path) == PREFIX_BLOB, "pairing prefix blob drift")
    req(blob(bundle_path) == BUNDLE_BLOB, "retained Picard bundle blob drift")

    target = cut201["target"]
    req(target["row_id"] == "g1-d008", "CUT201 row drift")
    req(int(target["g"]) == 1 and int(target["d"]) == 8 and int(target["e"]) == 8, "CUT201 stratum drift")
    offsets = [int(v) for v in target["survivor_offset_range"]]
    req(offsets == [2041, 2295], "CUT201 offset range drift")
    start_offset, end_offset = offsets
    block_count = end_offset - start_offset + 1
    req(block_count == int(target["block_count"]) == 255, "CUT201 block count drift")
    req(int(target["terminal_count"]) == 28815, "CUT201 terminal count drift")

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

    idx = CompressedTerminalIndexer(int(target["e"]), int(target["d"]))
    width = idx.normal_budget + 1
    req(width == 113, "e8 width drift")
    req(end_offset < idx.exceptional_count, "CUT201 offset range outside compressed exceptional family")
    req(block_count * width == int(target["terminal_count"]), "CUT201 terminal factorization drift")

    block_records: list[tuple[tuple[int, ...], int]] = []
    mask_counts: Counter[int] = Counter()
    for offset in range(start_offset, end_offset + 1):
        base = tuple(int(v) for v in idx.unrank(offset * width))
        req(base[NORMAL_INDEX] == 0, f"base x49 drift offset={offset}")
        mask = 0
        for r in range(8):
            x = list(base)
            x[NORMAL_INDEX] = r
            rhs = -(B_fixed * Matrix(x))
            if hnf_contains(H, rhs):
                mask |= 1 << r
        req(mask in (0x55, 0xAA), f"non-parity mask offset={offset} mask={mask:#x}")
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
    req(matching_models, "no affine GF2 x49 parity model on CUT201 e8 offset family")
    model = min(matching_models)

    coeff = {"constant": model & 1}
    for j, idx_i in enumerate(feature_indices, start=1):
        coeff[f"x{idx_i}"] = (model >> j) & 1

    # Replay exactly the 255 CUT201 exceptional offsets times all 113 x49 values.
    sat = 0
    unsat = 0
    for offset in range(start_offset, end_offset + 1):
        for r in range(width):
            rank = offset * width + r
            x = tuple(int(v) for v in idx.unrank(rank))
            req(x[NORMAL_INDEX] == r, f"x49 rank/order drift offset={offset} r={r}")
            pred = coeff["constant"]
            for idx_i in feature_indices:
                if coeff[f"x{idx_i}"]:
                    pred ^= x[idx_i] & 1
            parity_ok = (x[NORMAL_INDEX] & 1) == pred
            rhs = -(B_fixed * Matrix(x))
            exact = hnf_contains(H, rhs)
            req(exact == parity_ok, f"CUT201 replay mismatch offset={offset} r={r}")
            if exact:
                sat += 1
            else:
                unsat += 1

    even_blocks = int(mask_counts[0x55])
    odd_blocks = int(mask_counts[0xAA])
    req(sat == even_blocks * 57 + odd_blocks * 56, "SAT count reconstruction")
    req(unsat == even_blocks * 56 + odd_blocks * 57, "UNSAT count reconstruction")
    req(sat + unsat == int(target["terminal_count"]), "CUT201 partition count")

    summary = {
        "scope": "CUT201_g1_d008_e8_OFFSETS_2041_2295_INDEPENDENT_MAIN_PARITY_PROBE",
        "source_cut201_exact_head": CUT201_EXACT_HEAD,
        "source_cut201_preflight_blob": CUT201_PREFLIGHT_BLOB,
        "offset_range": [start_offset, end_offset],
        "block_count": block_count,
        "terminal_count": int(target["terminal_count"]),
        "completion_modulus": 8,
        "mask_distribution": {"0x55": even_blocks, "0xaa": odd_blocks},
        "affine_gf2_model_count": len(matching_models),
        "selected_affine_gf2_coefficients": coeff,
        "sat_terminal_count": sat,
        "unsat_terminal_count": unsat,
        "unsat_fraction": [unsat, int(target["terminal_count"])],
        "credit": {
            "independent_main_route_only": True,
            "current_main_residual_subset_identity_proved": False,
            "main_pruning_credit": False,
            "double_charge_authorized": False,
            "full178_complete": False,
        },
    }
    print(json.dumps(summary, sort_keys=True, indent=2))
    print("PASS_GRF09_CUT201_E8_PICARD_COMPLETION_PARITY_PROBE")


if __name__ == "__main__":
    main()
