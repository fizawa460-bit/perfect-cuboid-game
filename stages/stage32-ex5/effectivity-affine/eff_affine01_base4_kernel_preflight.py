#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import flint
from flint import fmpz_mat
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
HISTORICAL_FP_ALGORITHM_ID = "HNF_KERNEL_EXACT_GRAM_LLL_FP140_V1"
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

    historical_fp = load_module(HISTORICAL_AFFINE, "stage32ex5_eff_affine01_historical_fp")
    req(historical_fp.ALGORITHM_ID == HISTORICAL_FP_ALGORITHM_ID, "historical Fincke-Pohst algorithm drift")
    req(callable(historical_fp.solve_cell), "historical Fincke-Pohst recursion missing")

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

    # Exact saturated integer affine decomposition, following the retained
    # historical Stage32 affine-lattice backend but for the six-observable
    # (d,e,a,b,c,t) fiber instead of the old ten-budget map.
    fixed_rows = [[int(fixed_map[i, j]) for j in range(PICARD_RANK)] for i in range(6)]
    fixed_flint = fmpz_mat(fixed_rows)
    hnf_flint, transform_flint = fixed_flint.transpose().hnf(transform=True)
    hnf = Matrix([[int(hnf_flint[i, j]) for j in range(hnf_flint.ncols())]
                  for i in range(hnf_flint.nrows())])
    transform = Matrix([[int(transform_flint[i, j]) for j in range(transform_flint.ncols())]
                        for i in range(transform_flint.nrows())])
    req(hnf == transform * fixed_map.T, "HNF transform replay drift")
    req(abs(int(transform_flint.det())) == 1, "HNF transform is not unimodular")
    req(all(hnf[i, j] == 0 for i in range(6, PICARD_RANK) for j in range(6)),
        "HNF image/kernel split drift")

    transform_t = transform.T
    affine_columns = transform_t[:, :6]
    integer_kernel = transform_t[:, 6:]
    image_basis = fixed_map * affine_columns
    req(image_basis == hnf[:6, :].T, "HNF image basis replay drift")
    req(integer_kernel.shape == (PICARD_RANK, 58), "integer kernel shape drift")
    req(integer_kernel.rank() == 58, "integer kernel rank drift")
    req(fixed_map * integer_kernel == Matrix.zeros(6, 58), "integer kernel equality replay drift")

    negative_gram = -(integer_kernel.T * gram * integer_kernel)
    req(negative_gram == negative_gram.T, "restricted negative Gram lost symmetry")
    negative_flint = fmpz_mat([[int(negative_gram[i, j]) for j in range(58)] for i in range(58)])
    reduced_flint, lll_flint = negative_flint.lll(transform=True, rep="gram", gram="exact")
    lll_transform = Matrix([[int(lll_flint[i, j]) for j in range(58)] for i in range(58)])
    reduced_gram = Matrix([[int(reduced_flint[i, j]) for j in range(58)] for i in range(58)])
    req(abs(int(lll_flint.det())) == 1, "Gram-LLL transform is not unimodular")
    req(reduced_gram == lll_transform * negative_gram * lll_transform.T,
        "Gram-LLL replay drift")

    ldl_l, ldl_d = reduced_gram.LDLdecomposition(hermitian=False)
    req(reduced_gram == ldl_l * ldl_d * ldl_l.T, "exact LDL replay drift")
    diagonal = [ldl_d[i, i] for i in range(ldl_d.rows)]
    req(all(v > 0 for v in diagonal), "base4/e/d saturated kernel is not negative definite")

    target = Matrix([TARGET_DEGREE, TARGET_EXCEPTIONAL_MASS, 0, 1, 1, 1])
    image_coordinates = image_basis.inv() * target
    sample_integral_image = all(getattr(v, "q", 1) == 1 for v in image_coordinates)
    sample_base_point = affine_columns * image_coordinates
    req(fixed_map * sample_base_point == target, "sample HNF affine solve drift")

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE01_BASE4_KERNEL_PREFLIGHT_V1",
        "stage": "32EX5",
        "route_id": "EX5-EFF-AFFINE01",
        "status": "STRUCTURAL_PASS_HNF_SATURATED_KERNEL58_NEGATIVE_DEFINITE_GRAM_LLL_READY",
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
            "saturated_integer_kernel_dimension": integer_kernel.cols,
            "fixed_map_sha256": matrix_sha_strings(fixed_map),
            "hnf_sha256": matrix_sha_strings(hnf),
            "hnf_transform_sha256": matrix_sha_strings(transform),
            "image_basis_sha256": matrix_sha_strings(image_basis),
            "hnf_image_diagonal": [int(image_basis[i, i]) for i in range(6)],
            "hnf_image_index": abs(int(image_basis.det())),
            "integer_kernel_sha256": matrix_sha_strings(integer_kernel),
            "negative_restricted_gram_sha256": matrix_sha_strings(negative_gram),
            "lll_transform_sha256": matrix_sha_strings(lll_transform),
            "reduced_gram_sha256": matrix_sha_strings(reduced_gram),
            "ldl_diagonal_sha256": csha([str(v) for v in diagonal]),
            "restricted_negative_gram_positive_definite": True,
            "hnf_transform_unimodular": True,
            "gram_lll_transform_unimodular": True,
            "normal_mass_implied_exactly_by_d_e": True,
            "exceptional_mass_row_equals_all48_sum": True,
            "sample_base4_key": [0, 1, 1, 1],
            "sample_hnf_image_integral": sample_integral_image,
            "sample_hnf_image_coordinates": [str(v) for v in image_coordinates],
        },
        "historical_fp_backend": {
            "algorithm_id": HISTORICAL_FP_ALGORITHM_ID,
            "source_blob_sha1": HISTORICAL_AFFINE_BLOB,
            "complete_recursion_available": True,
            "all140_continuous_pruning_available": True,
            "direct_reuse_without_dimension_port": False,
            "historical_kernel_dimension": 54,
            "target_kernel_dimension": 58,
        },
        "interpretation": {
            "what_is_proved":
                "The EFF-CFRR01 base4/e/d relaxed Picard64 fiber has an exact saturated 58-dimensional integer H-perp kernel, a unimodular HNF image/kernel split, and a positive-definite exact Gram-LLL reduced -intersection form. The remaining independent certification step is complete Fincke-Pohst bad-shell enumeration with all140 pruning.",
            "what_is_not_proved":
                "No bad-shell UNSAT, no five-key MAIN pilot result, no effectivity or carrier conclusion, and no MAIN credit are established by this structural preflight.",
            "next_exact_unit":
                "Port the source-locked historical exact Fincke-Pohst recursion from 54D to the saturated 58D six-equality base4/e/d fiber, retain all140 nonnegativity pruning, then independently replay only keys whose MAIN diagnostic reports bad-shell UNSAT.",
        },
        "firewalls": {
            "main_eff_cfrr01_pilot_executed_by_ex5": False,
            "integer_affine_kernel_and_image_basis_certified": True,
            "individual_base4_image_membership_requires_per_key_hnf_check": True,
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
    print("EFF_AFFINE01_KERNEL_DIM=" + str(integer_kernel.cols))
    print("EFF_AFFINE01_CANONICAL=" + out["canonical_sha256_without_this_field"])
    print("EFF_AFFINE01_RESULT_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
