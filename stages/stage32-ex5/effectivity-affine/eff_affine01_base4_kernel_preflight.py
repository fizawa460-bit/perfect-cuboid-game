#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix
from sympy.matrices import MatrixBase

ROOT = Path(__file__).resolve().parents[3]

BASE = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_02_one_indexed_full178_terminal_to_picard64_completion.py"
BASE_BLOB = "6b4c3514b5b4cbccd8e66cbffc7f61f8830d1633"
RELAXED = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_static7_bounded_panel.py"
RELAXED_BLOB = "e44bec7ad9c0b7a4d8d7d87a455f181a681035c6"
PARENT = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_base4_normalmass_bounded_panel.py"
PARENT_BLOB = "29114c0cd8a2c604d24b2a9ad3418fc2b5200171"
EFF_PREFLIGHT = ROOT / "stages/stage32/final-chain/32-02-effectivity/compressed-fiber-rr/EFF-CFRR01-PREFLIGHT.json"
EFF_PREFLIGHT_BLOB = "abd993bf3356484a57a7b0824f7c371cb6b6ca2b"
EFF_WORKER = ROOT / "stages/stage32/final-chain/32-02-effectivity/compressed-fiber-rr/run_eff_cfrr01_d18e8_base4_pilot.py"
EFF_WORKER_BLOB = "c18c06fc9c1be7b972564e69bac730542db2febd"
HISTORICAL_AFFINE = ROOT / "stages/stage32/32-03/affine_lattice.py"
HISTORICAL_AFFINE_BLOB = "8aaa29208508c5314d30952044e037a6deb14b61"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
RETAINED_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
MARKING_BLOB = "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"

PICARD_RANK = 64
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
TARGET_DEGREE = 18
TARGET_EXCEPTIONAL_MASS = 8


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {name}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def row64(value) -> Matrix:
    if isinstance(value, MatrixBase):
        vals = list(value)
    else:
        vals = list(value)
    req(len(vals) == PICARD_RANK, "expected 64-entry linear functional")
    return Matrix(1, PICARD_RANK, [int(v) for v in vals])


def matrix_sha_strings(m: Matrix) -> str:
    return csha([[str(m[i, j]) for j in range(m.cols)] for i in range(m.rows)])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    locks = {
        BASE: BASE_BLOB,
        RELAXED: RELAXED_BLOB,
        PARENT: PARENT_BLOB,
        EFF_PREFLIGHT: EFF_PREFLIGHT_BLOB,
        EFF_WORKER: EFF_WORKER_BLOB,
        HISTORICAL_AFFINE: HISTORICAL_AFFINE_BLOB,
        RETAINED: RETAINED_BLOB,
        MARKING: MARKING_BLOB,
    }
    for path, expected in locks.items():
        req(path.is_file(), f"missing source lock: {path}")
        req(git_blob(path) == expected, f"source lock drift: {path}")

    eff = json.loads(EFF_PREFLIGHT.read_text(encoding="utf-8"))
    req(eff["schema"] == "STAGE32_MAIN_32_02_EFF_CFRR01_PREFLIGHT_V1", "EFF-CFRR01 schema drift")
    req(eff["status"] == "STRUCTURAL_ROUTE_PASS__D18_E8_FIVE_BASE4_PILOT_NOT_RUN__ZERO_CREDIT",
        "EFF-CFRR01 route status drift")
    req(eff["pilot"]["degree"] == TARGET_DEGREE and eff["pilot"]["exceptional_mass"] == TARGET_EXCEPTIONAL_MASS,
        "EFF-CFRR01 target drift")
    req(eff["independent_certification_gap"]["historical_exact_backend_available"].startswith("HNF saturated affine kernel"),
        "independent-checker gap drift")

    parent = load_module(PARENT, "stage32ex5_eff_affine01_parent")
    req(parent.RELAXED.is_file() and git_blob(parent.RELAXED) == RELAXED_BLOB,
        "base4 parent relaxed source drift")
    old = load_module(parent.RELAXED, "stage32ex5_eff_affine01_relaxed")
    req(old.BASE.is_file() and git_blob(old.BASE) == BASE_BLOB, "Picard64 base drift")
    req(tuple(old.ASSIGNMENT) == (95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96),
        "assignment order drift")
    req(len(old.L) >= 4 and all(len(row) == len(old.ASSIGNMENT) for row in old.L[:4]),
        "base4 aggregate matrix drift")

    v1 = load_module(old.BASE, "stage32ex5_eff_affine01_base")
    bundle = v1.load_retained(RETAINED, "stage32ex5_eff_affine01_bundle")
    marking = v1.load_retained(MARKING, "stage32ex5_eff_affine01_marking")
    data = v1.reconstruct_translation_data(marking, bundle)
    adapter = data["adapter"]
    bridge = data["bridge"]
    P = Matrix(adapter.pairing_matrix)
    gram = Matrix(bundle["picard_gram_64x64"])

    req(P.shape == (140, PICARD_RANK), "pairing matrix shape")
    req(gram.shape == (PICARD_RANK, PICARD_RANK) and gram == gram.T, "Picard Gram shape/symmetry")
    req(bridge.certificate.get("mass_identity_exact_on_picard64") is True,
        "Picard64 mass identity source drift")

    degree_row = row64(bridge.degree_functional)
    exceptional_row = row64(bridge.exceptional_mass_functional)
    assignment_rows = [P.row(label - 1) for label in old.ASSIGNMENT]
    base4_rows = []
    for i in range(4):
        row = Matrix.zeros(1, PICARD_RANK)
        for j, source in enumerate(assignment_rows):
            row += int(old.L[i][j]) * source
        base4_rows.append(row)

    fixed_map = Matrix.vstack(degree_row, exceptional_row, *base4_rows)
    fixed_rank = int(fixed_map.rank())
    req(fixed_rank == 6, f"base4/e/d equality rank changed: {fixed_rank}")

    exceptional_sum = Matrix.zeros(1, PICARD_RANK)
    normal_sum = Matrix.zeros(1, PICARD_RANK)
    for i in range(NORMAL_COUNT):
        normal_sum += P.row(i)
    for i in range(NORMAL_COUNT, NORMAL_COUNT + EXCEPTIONAL_COUNT):
        exceptional_sum += P.row(i)
    req(exceptional_sum == exceptional_row, "exceptional-mass functional mismatch")
    req(normal_sum + 5 * exceptional_sum == 19 * degree_row,
        "normal+5 exceptional=19 degree identity mismatch")

    nullspace = fixed_map.nullspace()
    req(len(nullspace) == PICARD_RANK - fixed_rank, "rational kernel dimension drift")
    kernel = Matrix.hstack(*nullspace)
    req(kernel.shape == (PICARD_RANK, 58), "kernel shape drift")
    req(fixed_map * kernel == Matrix.zeros(6, 58), "kernel equality replay drift")

    negative_gram = -(kernel.T * gram * kernel)
    req(negative_gram == negative_gram.T, "restricted negative Gram lost symmetry")
    ldl_l, ldl_d = negative_gram.LDLdecomposition(hermitian=False)
    req(negative_gram == ldl_l * ldl_d * ldl_l.T, "exact LDL replay drift")
    diagonal = [ldl_d[i, i] for i in range(ldl_d.rows)]
    req(all(v > 0 for v in diagonal), "base4/e/d kernel is not negative definite")

    target = Matrix([TARGET_DEGREE, TARGET_EXCEPTIONAL_MASS, 0, 1, 1, 1])
    # This target is the first retained EFF-CFRR01 sample key.  Structural
    # preflight only checks rational affine consistency; integral HNF image
    # certification is deliberately left to the next exact unit.
    rational_solution = fixed_map.gauss_jordan_solve(target)[0]
    req(fixed_map * rational_solution == target, "sample rational affine solve drift")

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE01_BASE4_KERNEL_PREFLIGHT_V1",
        "stage": "32EX5",
        "route_id": "EX5-EFF-AFFINE01",
        "status": "STRUCTURAL_PASS_RANK6_KERNEL58_NEGATIVE_DEFINITE__INTEGER_SATURATION_NOT_YET_CERTIFIED",
        "authority": {
            "repository_main": "e7fd29d24dd21e8529dbdb45b221a53f2cc21ed3",
            "stage32_primary_incomplete": "32-02_EFFECTIVITY_SURVIVOR_DISPOSAL",
            "main_eff_cfrr01_pilot_owned_by_ex5": False,
            "ex5_role": "PICARD64_NODE_SUPPORT_PRODUCER_REFINEMENT_ONLY",
        },
        "source_locks": {
            "picard64_base_blob_sha1": BASE_BLOB,
            "btva_relaxed_blob_sha1": RELAXED_BLOB,
            "btva_base4_parent_blob_sha1": PARENT_BLOB,
            "eff_cfrr01_preflight_blob_sha1": EFF_PREFLIGHT_BLOB,
            "eff_cfrr01_worker_blob_sha1": EFF_WORKER_BLOB,
            "historical_affine_lattice_blob_sha1": HISTORICAL_AFFINE_BLOB,
            "retained_picard_bundle_blob_sha1": RETAINED_BLOB,
            "retained_stage32_marking_blob_sha1": MARKING_BLOB,
        },
        "fixed_fiber": {
            "fixed_observables": ["d", "e", "a", "b", "c", "t"],
            "fixed_map_rank": fixed_rank,
            "rational_kernel_dimension": kernel.cols,
            "fixed_map_sha256": matrix_sha_strings(fixed_map),
            "rational_kernel_sha256": matrix_sha_strings(kernel),
            "negative_restricted_gram_sha256": matrix_sha_strings(negative_gram),
            "ldl_diagonal_sha256": csha([str(v) for v in diagonal]),
            "restricted_negative_gram_positive_definite": True,
            "normal_mass_implied_exactly_by_d_e": True,
            "exceptional_mass_row_equals_all48_sum": True,
            "sample_rational_affine_key": [0, 1, 1, 1],
            "sample_rational_affine_consistent": True,
        },
        "interpretation": {
            "what_is_proved":
                "The EFF-CFRR01 base4/e/d relaxed Picard64 fiber has an exact 58-dimensional rational H-perp kernel with positive-definite -intersection form, so an HNF/Gram-LLL/Fincke-Pohst independent bad-shell checker is structurally applicable.",
            "what_is_not_proved":
                "No saturated integer kernel, no bad-shell UNSAT, no five-key pilot result, no effectivity or carrier conclusion, and no MAIN credit are established by this structural preflight.",
            "next_exact_unit":
                "Construct the saturated integer affine kernel/image certificate for the six equalities and port exact Fincke-Pohst shell enumeration with all140 nonnegativity; only then replay candidate bad-shell UNSAT keys independently.",
        },
        "firewalls": {
            "main_eff_cfrr01_pilot_executed_by_ex5": False,
            "integer_affine_image_certified": False,
            "fincke_pohst_bad_shell_checker_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "main_pruning_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("EFF_AFFINE01_STATUS=" + out["status"])
    print("EFF_AFFINE01_FIXED_RANK=" + str(fixed_rank))
    print("EFF_AFFINE01_KERNEL_DIM=" + str(kernel.cols))
    print("EFF_AFFINE01_CANONICAL=" + out["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
