#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass

import sympy
from sympy import Matrix

from pairing_prefix_engine import (
    INDLIST,
    PrefixMembershipOracle,
    RetainedBasisPairingTransform,
    close_permutation_group,
)

KNOWN_CURVE_COUNT = 140
PICARD_RANK = 64
EXPECTED_HPERP_MAGIC = "S32_D16_AUT_CANON_HPERP_V1"
EXPECTED_HPERP_SHA256 = "af373f16d6ab2bb8aed6ca09e0a15c8b28d565cbec6f242a8b76c590df81bb4f"
EXPECTED_HPERP_Q_DETERMINANT = 1073741824
EXPECTED_PICARD_DETERMINANT = -268435456
EXPECTED_AUT_GROUP_ORDER = 1536
GEN6_ASSIGNMENT_ORDER = [0, 1, 2, 3, 61, 4, 5, 6, 7, 8, 9]
GEN6_ACTIVE_ROWS = [0, 0, 0, 0, 16, 16, 16, 16, 16, 16, 16]
GEN6_MODULI = [8] * 11
GEN6_KNOWN_LABELS = [93, 94, 95, 96, 49, 97, 98, 99, 101, 102, 103]

# Exact ordered 64-class realization of the retained Magma Picard basis. This
# is fail-closed: the recovered all-140 intersection matrix must reproduce the
# retained 64x64 Gram entry for entry on these labels before acceptance.
RETAINED_BASIS_KNOWN_LABELS_1BASED = [
    1, 33, 12, 16, 7, 90, 87, 92, 51, 40, 77, 44, 20, 55, 19, 56,
    123, 118, 73, 117, 119, 122, 120, 121, 94, 96, 79, 95, 99, 75, 24, 98,
    132, 26, 125, 126, 128, 127, 129, 130, 108, 107, 52, 18, 11, 102, 3, 106,
    136, 137, 134, 139, 140, 133, 6, 135, 112, 110, 113, 115, 116, 114, 109, 111,
]
assert len(RETAINED_BASIS_KNOWN_LABELS_1BASED) == PICARD_RANK
assert len(set(RETAINED_BASIS_KNOWN_LABELS_1BASED)) == PICARD_RANK


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def _domain_det(m: Matrix) -> int:
    from sympy.polys.matrices import DomainMatrix
    return int(DomainMatrix.from_Matrix(m).det())


def _parse_hperp(text: str) -> tuple[Matrix, Matrix, Matrix, list[int], dict]:
    raw_sha = hashlib.sha256(text.encode()).hexdigest()
    if raw_sha != EXPECTED_HPERP_SHA256:
        raise ValueError(f"retained Hperp hash regression: {raw_sha}")
    lines = text.splitlines()
    if len(lines) < 5 or lines[0] != EXPECTED_HPERP_MAGIC:
        raise ValueError("retained Hperp magic regression")
    core_sha, source_blob, input_sha = lines[1], lines[2], lines[3]
    n, m = map(int, lines[4].split())
    if (n, m) != (63, KNOWN_CURVE_COUNT):
        raise ValueError(f"unexpected Hperp dimensions: {(n, m)}")
    if len(lines) != 5 + n + m:
        raise ValueError(f"unexpected Hperp line count: {len(lines)}")
    q = Matrix([list(map(int, lines[5 + i].split())) for i in range(n)])
    if q.shape != (63, 63) or q != q.T:
        raise ValueError("Hperp Q shape/symmetry regression")
    qdet = _domain_det(q)
    if qdet != EXPECTED_HPERP_Q_DETERMINANT:
        raise ValueError(f"Hperp Q determinant regression: {qdet}")
    records = [list(map(int, lines[5 + n + r].split())) for r in range(m)]
    if any(len(row) != 65 for row in records):
        raise ValueError("Hperp known-record width regression")
    degree = Matrix([row[0] for row in records])
    caps = [row[1] for row in records]
    linear = Matrix([row[2:] for row in records])
    return q, degree, linear, caps, {
        "hperp_text_sha256": raw_sha,
        "core_sha256": core_sha,
        "upstream_git_blob_sha1": source_blob,
        "input_sha256": input_sha,
        "dimensions": [n, m],
        "q_determinant": qdet,
    }


def _recover_full_intersection(q: Matrix, degree: Matrix, linear: Matrix) -> Matrix:
    # The Hperp records are exact affine pairing functionals. Restoring the
    # degree direction gives the all-140 intersection form:
    #   <C,C'> = deg(C)deg(C')/16 - ell(C) Q^{-1} ell(C')^T.
    full = degree * degree.T / 16 - linear * q.inv() * linear.T
    if full.shape != (KNOWN_CURVE_COUNT, KNOWN_CURVE_COUNT) or full != full.T:
        raise ValueError("recovered all-140 intersection shape/symmetry regression")
    if any(sympy.denom(v) != 1 for v in full):
        raise ValueError("recovered all-140 intersection matrix is not integral")
    full = Matrix([
        [int(full[i, j]) for j in range(KNOWN_CURVE_COUNT)]
        for i in range(KNOWN_CURVE_COUNT)
    ])
    diag = [int(full[i, i]) for i in range(KNOWN_CURVE_COUNT)]
    if diag[:92] != [-4] * 92 or diag[92:] != [-2] * 48:
        raise ValueError("recovered all-140 self-intersection regression")
    selected = [j - 1 for j in INDLIST]
    selected_gram = full.extract(selected, selected)
    if _domain_det(selected_gram) != EXPECTED_PICARD_DETERMINANT:
        raise ValueError("recovered selected64 discriminant regression")
    return full


def generation6_hnf_regression(bundle: dict) -> dict:
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    selected_known = transform.certificate["selected_known_indices_1based"]
    known_labels = [selected_known[i] for i in GEN6_ASSIGNMENT_ORDER]
    if known_labels != GEN6_KNOWN_LABELS:
        raise ValueError(f"generation6 label-order regression: {known_labels}")
    oracle = PrefixMembershipOracle(transform, GEN6_ASSIGNMENT_ORDER)
    cert = oracle.certificate()
    active = [int(c["active_congruence_rows"]) for c in cert["checks"]]
    moduli = [int(c["modulus"]) for c in cert["checks"]]
    if active != GEN6_ACTIVE_ROWS or moduli != GEN6_MODULI:
        raise ValueError(f"generation6 HNF regression: active={active}, moduli={moduli}")
    first_active = next((i + 1 for i, n in enumerate(active) if n), None)
    if first_active != 5:
        raise ValueError(f"generation6 first-active-depth regression: {first_active}")
    out = {
        "assignment_order": GEN6_ASSIGNMENT_ORDER,
        "known_label_order_1based": known_labels,
        "active_congruence_rows_by_depth": active,
        "modulus_by_depth": moduli,
        "first_active_depth": first_active,
        "depth5_modulus": moduli[4],
        "depth5_active_congruence_rows": active[4],
        "oracle_certificate_sha256": csha(cert),
        "exact_match": True,
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    return out


@dataclass(frozen=True)
class HperpIntegralPairingAdapter:
    pairing_matrix: Matrix
    class_coordinates_in_retained_basis: Matrix
    discovery_paths: tuple[str, ...]
    discovery_modes: tuple[str, ...]
    certificate: dict

    @classmethod
    def from_retained(cls, marking: dict, bundle: dict) -> "HperpIntegralPairingAdapter":
        gram = Matrix(bundle["picard_gram_64x64"])
        if gram.shape != (PICARD_RANK, PICARD_RANK) or gram != gram.T:
            raise ValueError("retained Picard Gram regression")
        if _domain_det(gram) != EXPECTED_PICARD_DETERMINANT:
            raise ValueError("retained Picard discriminant regression")
        hperp_text = marking.get("hperp_text")
        if not isinstance(hperp_text, str):
            raise ValueError("retained marking missing hperp_text")
        q, degree, linear, caps, hmeta = _parse_hperp(hperp_text)
        full = _recover_full_intersection(q, degree, linear)

        aut_payload = marking.get("aut_action")
        if not isinstance(aut_payload, dict):
            raise ValueError("retained marking missing aut_action")
        generators = aut_payload.get("permutations_1based")
        if not isinstance(generators, list) or not generators:
            raise ValueError("retained marking missing Aut permutations")
        for gi, p in enumerate(generators):
            idx = [int(v) - 1 for v in p]
            if len(idx) != KNOWN_CURVE_COUNT or sorted(idx) != list(range(KNOWN_CURVE_COUNT)):
                raise ValueError(f"Aut generator {gi} degree/permutation regression")
            if full.extract(idx, idx) != full:
                raise ValueError(f"Aut generator {gi} is not an isometry of recovered all140 intersection")
        group_order = len(close_permutation_group(generators))
        if group_order != EXPECTED_AUT_GROUP_ORDER:
            raise ValueError(f"Aut group order regression: {group_order}")

        retained_idx = [j - 1 for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]
        recovered_retained_gram = full.extract(retained_idx, retained_idx)
        if recovered_retained_gram != gram:
            raise ValueError("recovered retained-basis label realization does not match retained Picard Gram")

        pairing = full[:, retained_idx]
        coords_q = pairing * gram.inv()
        if any(sympy.denom(v) != 1 for v in coords_q):
            raise ValueError("all140 class coordinates are not integral in retained Picard basis")
        coords = Matrix([
            [int(coords_q[i, j]) for j in range(PICARD_RANK)]
            for i in range(KNOWN_CURVE_COUNT)
        ])
        if coords.extract(retained_idx, list(range(PICARD_RANK))) != Matrix.eye(PICARD_RANK):
            raise ValueError("retained-basis coordinate identity regression")
        if coords * gram != pairing:
            raise ValueError("all140 retained-basis pairing reconstruction regression")

        selected_idx = [j - 1 for j in INDLIST]
        selected_coords = coords.extract(selected_idx, list(range(PICARD_RANK)))
        selected_det = _domain_det(selected_coords)
        if abs(selected_det) != 1:
            raise ValueError(f"selected64-to-retained change of basis is not unimodular: det={selected_det}")
        selected_geo_gram = full.extract(selected_idx, selected_idx)
        if selected_coords * gram * selected_coords.T != selected_geo_gram:
            raise ValueError("selected64 Gram change-of-basis regression")

        gen6 = generation6_hnf_regression(bundle)
        cert = {
            "mode": "EXACT_HPERP_DEGREE_AUGMENTED_ALL140_TO_SATURATED_RETAINED_PICARD64",
            "discovery_paths": ["$.hperp_text + retained.picard_gram_64x64"],
            "discovery_modes": ["HPERP_DEGREE_AUGMENTED_INTEGRAL_SATURATION_ADAPTER"],
            "known_curve_count": KNOWN_CURVE_COUNT,
            "picard_rank": PICARD_RANK,
            "hperp": hmeta,
            "hperp_cap_sha256": csha(caps),
            "full_intersection_sha256": csha(matrix_list(full)),
            "full_intersection_integral": True,
            "normal_curve_self_intersection": -4,
            "exceptional_curve_self_intersection": -2,
            "retained_basis_known_labels_1based": RETAINED_BASIS_KNOWN_LABELS_1BASED,
            "retained_basis_gram_exact": True,
            "basis_row_regression_count": PICARD_RANK,
            "basis_row_regression_exact": True,
            "retained_basis_gram_sha256": csha(matrix_list(gram)),
            "pairing_matrix_sha256": csha(matrix_list(pairing)),
            "all140_retained_coordinates_sha256": csha(matrix_list(coords)),
            "all140_retained_coordinates_integral": True,
            "selected64_known_labels_1based": list(INDLIST),
            "selected64_change_of_basis_determinant": selected_det,
            "selected64_change_of_basis_unimodular": True,
            "selected64_change_of_basis_sha256": csha(matrix_list(selected_coords)),
            "selected64_gram_change_of_basis_exact": True,
            "selected64_geometric_gram_sha256": csha(matrix_list(selected_geo_gram)),
            "full_aut_group_order": group_order,
            "aut_generator_isometry_count": len(generators),
            "generation6_hnf_regression": gen6,
            "saturated_picard64_integral_adapter_validated": True,
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(
            pairing_matrix=pairing,
            class_coordinates_in_retained_basis=coords,
            discovery_paths=("$.hperp_text + retained.picard_gram_64x64",),
            discovery_modes=("HPERP_DEGREE_AUGMENTED_INTEGRAL_SATURATION_ADAPTER",),
            certificate=cert,
        )
