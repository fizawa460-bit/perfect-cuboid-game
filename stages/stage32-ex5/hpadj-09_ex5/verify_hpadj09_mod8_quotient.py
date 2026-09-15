#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from sympy import Matrix, eye
from sympy.matrices.normalforms import hermite_normal_form

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFLIGHT = HERE / "PREFLIGHT.json"
INTERFACE = ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
PAIRING = ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"

sys.path.insert(0, str(RESIDUAL))
sys.path.insert(0, str(BUNDLE_DIR))
from pairing_prefix_engine import RetainedBasisPairingTransform
import picard_base_rows_retained as retained_bundle

PREFLIGHT_BLOB = "4fb4b22b0577c19e98aeefa43c073ba062556dff"
PREFLIGHT_CANON = "d41612200ecf621de4d1f44bca128b721c84e73ad50bce7ce1c550f3daf87441"
INTERFACE_BLOB = "8a30e3aa30777460f344eb19836dc725dd442329"
INTERFACE_CANON = "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6"
PAIRING_BLOB = "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"
BUNDLE_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
BUNDLE_CANON = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
B_SHA = "7b4d0601585f011e168bf5c4b15086950b0e3e3e16c90826b7413cdbe183c233"
FIXED_SHA = "e8f4a9004177fc2a2023775431505d4ef39b7b808bd41cb517787c235ab170fe"
FREE_SHA = "ad27fa86fbc98d55a97af5fd9d247fb880af9dac58d6429ca029d6b8ca4c288b"
ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(value: dict) -> str:
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def matrix_sha(m: Matrix) -> str:
    return hashlib.sha256(
        json.dumps(matrix_list(m), sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    req(PREFLIGHT.is_file() and blob(PREFLIGHT) == PREFLIGHT_BLOB, "preflight blob drift")
    pre = json.loads(PREFLIGHT.read_text())
    req(pre.get("canonical_sha256_without_this_field") == PREFLIGHT_CANON, "preflight stored canonical drift")
    req(canon(pre) == PREFLIGHT_CANON, "preflight canonical drift")
    req(pre.get("status") == "ACTIVE_SUCCESSOR_BOUNDED_QUOTIENT_DIAGNOSTIC", "preflight status drift")

    req(INTERFACE.is_file() and blob(INTERFACE) == INTERFACE_BLOB, "interface blob drift")
    interface = json.loads(INTERFACE.read_text())
    req(interface.get("canonical_sha256_without_this_field") == INTERFACE_CANON, "interface stored canonical drift")
    req(canon(interface) == INTERFACE_CANON, "interface canonical drift")
    req(PAIRING.is_file() and blob(PAIRING) == PAIRING_BLOB, "pairing engine blob drift")
    req(BUNDLE_SOURCE.is_file() and blob(BUNDLE_SOURCE) == BUNDLE_BLOB, "Picard bundle source blob drift")

    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == BUNDLE_CANON, "Picard bundle canonical drift")
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    req(int(transform.den) == 8, "selected64 denominator drift")
    labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    req(len(labels) == 64 and len(set(labels)) == 64, "selected64 label identity drift")

    fixed_positions = [labels.index(label) for label in ASSIGNMENT_LABELS]
    free_positions = [i for i in range(64) if i not in fixed_positions]
    req(len(fixed_positions) == 11 and len(free_positions) == 53, "fixed/free partition drift")
    req(sorted(fixed_positions + free_positions) == list(range(64)), "selected64 partition not exhaustive")

    B = transform.inverse_integer
    req(B.shape == (64, 64), "inverse integer matrix shape drift")
    fixed = B.extract(list(range(64)), fixed_positions)
    free = B.extract(list(range(64)), free_positions)
    req(matrix_sha(B) == B_SHA, "inverse integer matrix identity drift")
    req(matrix_sha(fixed) == FIXED_SHA, "fixed matrix identity drift")
    req(matrix_sha(free) == FREE_SHA, "free matrix identity drift")

    lattice_free = free.row_join(8 * eye(64))
    lattice_all = free.row_join(fixed).row_join(8 * eye(64))
    H_free = hermite_normal_form(lattice_free)
    H_all = hermite_normal_form(lattice_all)
    req(H_free.shape == (64, 64) and H_all.shape == (64, 64), "HNF rank/shape drift")

    det_free = abs(int(H_free.det()))
    det_all = abs(int(H_all.det()))
    req(det_free > 0 and det_all > 0, "zero HNF determinant")
    req(det_free % det_all == 0, "lattice index nonintegral")
    image_size = det_free // det_all

    residue_cube = 8 ** 11
    req(image_size >= 1 and residue_cube % image_size == 0, "fixed residue quotient size incompatible with mod 8 cube")
    accepted_residue_classes = residue_cube // image_size
    rejected_residue_classes = residue_cube - accepted_residue_classes
    strict = image_size > 1

    result = {
        "schema": "STAGE32EX5_HPADJ09_MOD8_QUOTIENT_DIAGNOSTIC_V1",
        "status": "STRICT_NONTRIVIAL_OBSTRUCTION" if strict else "TRIVIAL_NO_REJECTION_AT_RESIDUE_LEVEL",
        "source": {
            "preflight_blob_sha1": PREFLIGHT_BLOB,
            "preflight_canonical_sha256": PREFLIGHT_CANON,
            "interface_blob_sha1": INTERFACE_BLOB,
            "interface_canonical_sha256": INTERFACE_CANON,
            "selected64_inverse_denominator": 8,
            "fixed_dimension": 11,
            "free_dimension": 53,
        },
        "lattice": {
            "free_hnf_sha256": matrix_sha(H_free),
            "all_hnf_sha256": matrix_sha(H_all),
            "det_free": det_free,
            "det_all": det_all,
            "fixed_image_size": image_size,
        },
        "residue_cube": {
            "total_classes": residue_cube,
            "accepted_classes": accepted_residue_classes,
            "rejected_classes": rejected_residue_classes,
            "strict_obstruction": strict,
        },
        "semantics": {
            "claim": "Residue classes outside the kernel cannot admit an integral selected64 Picard64 completion.",
            "terminal_population_rejection_measured": False,
            "reverse_realization_claimed": False,
            "full178_scaleout_authorized": False,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
        },
    }
    result["canonical_sha256_without_this_field"] = canon(result)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
