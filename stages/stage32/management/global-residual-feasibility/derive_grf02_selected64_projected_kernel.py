#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"
HANDOFF = ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
GRF01 = HERE / "GRF-01-CONTRACT.json"
PREFIX = RESIDUAL / "pairing_prefix_engine.py"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"

sys.path.insert(0, str(RESIDUAL))
sys.path.insert(0, str(BUNDLE_DIR))

from pairing_prefix_engine import PrefixMembershipOracle, RetainedBasisPairingTransform
import picard_base_rows_retained as retained_bundle

SOURCE_LOCKS = {
    HANDOFF: "8a30e3aa30777460f344eb19836dc725dd442329",
    GRF01: "a81ebccfa0e235fe33926e16a0bd67bfcb29cbc0",
    PREFIX: "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    BUNDLE_SOURCE: "82e4d450a1d852e34f6615440fb88a029c6e54eb",
}
EXPECTED_GRF01_CANONICAL = "18ce801f45bd95fec8e0a2f6001eff9fd80a9b6f6b416ccc9190d3b37adc3c43"
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(
        json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def primitive_row(row: tuple[int, ...], modulus: int) -> tuple[int, tuple[int, ...]]:
    g = modulus
    for v in row:
        g = math.gcd(g, int(v))
    q = modulus // g
    vals = tuple((int(v) // g) % q for v in row)
    if q == 1:
        return 1, tuple(0 for _ in row)
    units = [u for u in range(1, q) if math.gcd(u, q) == 1]
    reps = [tuple((u * v) % q for v in vals) for u in units]
    return q, min(reps)


def main() -> None:
    for path, expected in SOURCE_LOCKS.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    grf01 = json.loads(GRF01.read_text())
    stored = grf01.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_GRF01_CANONICAL and csha(grf01) == EXPECTED_GRF01_CANONICAL,
        "GRF-01 canonical drift")
    req(grf01["status"] == "FAMILY_LEVEL_OBSTRUCTION_DESIGN_ONLY_HANDOFF_TO_178_NO_CREDIT",
        "GRF-01 ownership/status drift")

    handoff = json.loads(HANDOFF.read_text())
    tm = handoff["terminal_to_picard64_map"]
    assignment_labels = [int(v) for v in tm["terminal_assignment_labels_1based"]]
    req(len(assignment_labels) == 11 and len(set(assignment_labels)) == 11,
        "terminal fixed-label identity drift")
    req(int(tm["inverse_denominator"]) == 8, "selected64 denominator drift")

    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == EXPECTED_BUNDLE_CANONICAL, "Picard bundle canonical drift")
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    selected_labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    fixed_positions = [selected_labels.index(label) for label in assignment_labels]
    fixed_set = set(fixed_positions)
    free_positions = [i for i in range(64) if i not in fixed_set]
    req(len(free_positions) == 53, "selected64 fixed/free partition drift")

    oracle = PrefixMembershipOracle(transform, fixed_positions)
    check = oracle.checks[-1]
    req(check.depth == 11 and check.modulus == 8, "projected HNF modulus/depth drift")
    coeff = [tuple(int(v) % 8 for v in row) for row in check.coefficients]
    req(coeff, "projected HNF kernel unexpectedly trivial")

    primitive = sorted(set(primitive_row(row, 8) for row in coeff))
    primitive_rows = [
        {"modulus": int(q), "coefficients": list(row)}
        for q, row in primitive if q != 1
    ]

    B = transform.inverse_integer
    Bfixed = B[:, fixed_positions]
    Bfree = B[:, free_positions]
    L = Bfree.row_join(8 * Matrix.eye(64))
    M = B.row_join(8 * Matrix.eye(64))
    HL = hermite_normal_form(L)
    HM = hermite_normal_form(M)
    req(HL.shape == (64, 64) and HM.shape == (64, 64), "HNF shape drift")
    inclusion_q = HM.inv() * HL
    req(all(v.q == 1 for v in inclusion_q), "projected quotient inclusion is not integral")
    inclusion = Matrix([[int(inclusion_q[i, j]) for j in range(64)] for i in range(64)])
    snf = smith_normal_form(inclusion, domain=ZZ)
    invariants = sorted(abs(int(snf[i, i])) for i in range(64) if abs(int(snf[i, i])) > 1)
    quotient_order = math.prod(invariants) if invariants else 1
    det_ratio = abs(int(HL.det())) // abs(int(HM.det()))
    req(quotient_order == det_ratio, "projected quotient order mismatch")

    signatures: dict[int, tuple[int, ...]] = {}
    orders: dict[int, int] = {}
    C = Matrix(coeff)
    for j, label in enumerate(assignment_labels):
        sig = tuple(int(C[i, j]) % 8 for i in range(C.rows))
        signatures[label] = sig
        order = next(t for t in (1, 2, 4, 8) if all((t * v) % 8 == 0 for v in sig))
        orders[label] = order

    classes: dict[tuple[int, ...], list[int]] = {}
    for label in assignment_labels:
        classes.setdefault(signatures[label], []).append(label)
    equivalence_classes = sorted((sorted(v) for v in classes.values()), key=lambda x: (x[0], len(x), x))

    groups = handoff["stored_10_exceptional_coordinate_identity"]["groups"]
    group_sum_collapse = {}
    for name in ("a", "b", "c"):
        labels = [int(v) for v in groups[name]]
        group_sum_collapse[name] = len({signatures[label] for label in labels}) == 1

    body = {
        "schema": "STAGE32_MAIN_GRF02_SELECTED64_PROJECTED_KERNEL_DERIVATION_V1",
        "stage": 32,
        "surface": "MAIN",
        "status": "SYMBOLIC_PROJECTED_KERNEL_ONLY_NO_CONCRETE_178_TARGET_NO_CREDIT",
        "source": {
            "grf01_contract_blob_sha1": SOURCE_LOCKS[GRF01],
            "grf01_canonical_sha256": EXPECTED_GRF01_CANONICAL,
            "hpadj_picard64_interface_blob_sha1": SOURCE_LOCKS[HANDOFF],
            "pairing_prefix_engine_blob_sha1": SOURCE_LOCKS[PREFIX],
            "picard_bundle_source_blob_sha1": SOURCE_LOCKS[BUNDLE_SOURCE],
            "picard_bundle_canonical_sha256": EXPECTED_BUNDLE_CANONICAL,
        },
        "fixed_selected64": {
            "assignment_labels_1based": assignment_labels,
            "selected_positions_0based": fixed_positions,
            "free_coordinate_count": 53,
            "inverse_denominator": 8,
        },
        "projected_hnf_kernel": {
            "modulus": int(check.modulus),
            "active_congruence_row_count": len(coeff),
            "quotient_index_from_prefix_oracle": int(check.quotient_index),
            "hnf_sha256": check.hnf_sha256,
            "coefficient_rows_mod8": [list(row) for row in coeff],
            "coefficient_rows_sha256": csha([list(row) for row in coeff]),
            "primitive_equation_rows": primitive_rows,
            "primitive_equation_rows_sha256": csha(primitive_rows),
        },
        "projected_quotient": {
            "meaning": "image of the 11 fixed selected64 coordinate directions in Z^64/(B_free*Z^53 + 8*Z^64)",
            "smith_nontrivial_invariant_factors": invariants,
            "order": int(quotient_order),
            "free_completion_hnf_determinant": abs(int(HL.det())),
            "all_selected_hnf_determinant": abs(int(HM.det())),
            "inclusion_matrix_sha256": csha(matrix_list(inclusion)),
        },
        "fixed_coordinate_classes": {
            "equivalence_classes_by_projected_mod8_signature": equivalence_classes,
            "individual_class_orders": {str(k): int(orders[k]) for k in assignment_labels},
            "signature_stream_sha256": csha({str(k): list(signatures[k]) for k in assignment_labels}),
            "hpadj_group_collapses_to_group_sum": group_sum_collapse,
        },
        "ownership": {
            "main_scope": "fixed symbolic lattice kernel only",
            "concrete_row_or_stratum_selected": False,
            "population_replay_performed": False,
            "bounded_leaf_search_performed": False,
            "exact_subset_certificate_generated": False,
            "concrete_application_owner": "stage32-01-178-mainbatch",
        },
        "credit_firewall": {
            "main_pruning_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    print(json.dumps(body, sort_keys=True, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
