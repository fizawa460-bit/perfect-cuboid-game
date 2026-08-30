#!/usr/bin/env python3
"""Certify local determinant-parity constraints for the corrected-J2 ct nullhomotopy.

This is an R5e narrowing certificate.  It uses the already fixed scalar frames
of u=(A+z)/(2t) to determine determinant parity wherever the normalized local
norm order is even, reconstructs the marked Picard coordinates of all twelve
Kc exceptional curves, and isolates the still load-bearing overlap choices at
t=0, t=infinity, and the four ramified q-roots.  It deliberately does not
promote a full ct Pic/2 defect or an HS d2 value.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-ct-norm-local-lattice-parity-constraints.json"

LOCKS = {
    "semantic": ("j2-semantic-kc-picard-basis.json", "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0"),
    "support": ("j2-corrected-ct-norm-picard-support.json", "77af329d2baf2fe807bf23722c9b320fdfddec2bd1df90ced7758d411c9cf021"),
    "splitting": ("j2-corrected-ct-norm-splitting-module.json", "b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2"),
    "boundary": ("j2-ct-norm-actual-boundary-sheet-frames.json", "5b961822dc10e7a1a424ed87ba6307d83efd3a0b31671db305a609269094937b"),
    "exceptionals": ("j2-ct-norm-resolution-exceptional-sheet-frames.json", "bbde421a54d2b7159f8d3ff4cf641cbddf2bbbc45fe4791cb7ed18d7cfb69591"),
    "explicit": ("j2-corrected-explicit-cech-mu2-lift.json", "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"),
}

EXPECTED_EXCEPTIONAL_COORDS = [
    [0,0,0,0,0,0,0,-1,0,1,0,-1,0,-1,1,1,0,-1,0,0],
    [0,0,-1,-1,0,0,0,0,1,0,0,0,0,0,0,0,0,-1,0,0],
    [0,0,1,1,0,0,0,-1,-1,-1,0,1,0,1,-1,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,-1,-1,-1,-1,0,1,1,1,0,-1,-1,-1,2,1,-1,-2,-1,0],
    [-1,1,-1,-1,-1,-1,0,1,1,2,-1,-1,0,-2,2,1,-1,-2,-1,0],
    [1,-1,0,0,0,0,0,0,0,-1,1,0,1,1,-2,-1,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [-1,-1,3,1,2,2,0,-2,-1,-2,0,2,-1,1,-2,0,1,4,0,1],
    [1,1,-1,-1,-1,-1,0,1,-1,1,0,-1,0,-1,1,1,0,-2,0,-1],
    [0,0,-2,0,-1,-1,0,1,0,1,0,-1,1,0,1,0,0,-2,0,-1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
]


def csha(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(key: str) -> dict:
    name, expected = LOCKS[key]
    obj = json.loads((HERE / name).read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), (name, claimed, csha(body))
    return obj


def gram20(semantic: dict) -> list[list[int]]:
    g17 = semantic["gram17"]
    inc = semantic["incidence17x12"]
    triple = semantic["semantic_exceptional_indices_0based"]
    out = [row[:] + [inc[i][j] for j in triple] for i, row in enumerate(g17)]
    for a, j in enumerate(triple):
        row = [inc[i][j] for i in range(17)] + [0, 0, 0]
        row[17+a] = -2
        out.append(row)
    return out


def solve_row_coordinates(gram: list[list[int]], pairings: list[int]) -> list[int]:
    n = len(gram)
    aug = [[Fraction(gram[j][i]) for j in range(n)] + [Fraction(pairings[i])] for i in range(n)]
    for col in range(n):
        pivot = next(j for j in range(col, n) if aug[j][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x/scale for x in aug[col]]
        for j in range(n):
            if j == col or not aug[j][col]:
                continue
            scale = aug[j][col]
            aug[j] = [x-scale*y for x, y in zip(aug[j], aug[col])]
    ans = [aug[i][-1] for i in range(n)]
    assert all(x.denominator == 1 for x in ans)
    return [int(x) for x in ans]


def exceptional_coordinates(semantic: dict) -> list[list[int]]:
    g = gram20(semantic)
    inc = semantic["incidence17x12"]
    triple = semantic["semantic_exceptional_indices_0based"]
    out = []
    for j in range(12):
        pair = [inc[i][j] for i in range(17)] + [(-2 if j == h else 0) for h in triple]
        out.append(solve_row_coordinates(g, pair))
    return out


def even_norm_split_parity(a: int, b: int, k: int) -> int:
    """Parity forced by a normalized split DVR lattice, independent of common twist."""
    assert a + b == k and k % 2 == 0
    aa, bb = a-k//2, b-k//2
    assert aa + bb == 0
    return aa % 2


def xor_vectors(*rows: list[int]) -> list[int]:
    return [sum(values) % 2 for values in zip(*rows)]


def main() -> None:
    semantic = load_locked("semantic")
    support = load_locked("support")
    splitting = load_locked("splitting")
    boundary = load_locked("boundary")
    exc = load_locked("exceptionals")
    explicit = load_locked("explicit")

    coords = exceptional_coordinates(semantic)
    assert coords == EXPECTED_EXCEPTIONAL_COORDS
    labels = [x["label"] for x in semantic["semantic_point_order"]]
    assert labels[:4] == [
        "A1_B2+1_B3+1", "A1_B2+1_B3-1",
        "A1_B2-1_B3+1", "A1_B2-1_B3-1",
    ]
    corners = exc["branch_crossing_corner_identification"]["corners"]
    corner_index = {}
    for name, rec in corners.items():
        node = rec["Kc_node"]
        idx = next(i for i, p in enumerate(semantic["semantic_point_order"]) if p["coords"] == node)
        corner_index[name] = idx
    assert corner_index == {"E_00": 0, "E_0inf": 2, "E_inf0": 1, "E_infinf": 3}

    bf = boundary["boundary_sheet_frames"]
    ef = exc["actual_ct_resolution_exceptional_sheet_frames"]
    assert even_norm_split_parity(0, 0, bf["C21"]["ord_norm"]) == 0
    assert even_norm_split_parity(-1, -1, bf["Sinf"]["ord_norm"]) == 0
    assert even_norm_split_parity(ef["E_00"]["sheet_plus"]["ord_u"], ef["E_00"]["sheet_plus"]["ord_sigma_u"], ef["E_00"]["ord_norm"]) == 1
    assert even_norm_split_parity(ef["E_0inf"]["sheet_plus"]["ord_u"], ef["E_0inf"]["sheet_plus"]["ord_sigma_u"], ef["E_0inf"]["ord_norm"]) == 0
    assert even_norm_split_parity(ef["E_inf0"]["sheet_plus"]["ord_u"], ef["E_inf0"]["sheet_plus"]["ord_sigma_u"], ef["E_inf0"]["ord_norm"]) == 1
    assert even_norm_split_parity(ef["E_infinf"]["sheet_plus"]["ord_u"], ef["E_infinf"]["sheet_plus"]["ord_sigma_u"], ef["E_infinf"]["ord_norm"]) == 0
    assert exc["quotient_A1_exceptional_frames"]["generic_ord_u_on_every_auxiliary_q_cover_component"] == 0
    assert exc["quotient_A1_exceptional_frames"]["generic_ord_sigma_u_on_every_auxiliary_q_cover_component"] == 0

    assert "valuation 2" in explicit["surface_mu2_lift"]["ramification_check"]
    assert even_norm_split_parity(0, 2, 2) == 1
    assert bf["T0"]["ord_norm"] == -1 and bf["Tinf"]["ord_norm"] == -1

    qa = splitting["q_root_local_audit"]
    assert qa["all_roots_simple_and_nonzero"] and qa["g22_specializes_to_square_of_displayed_root"]
    assert len(qa["roots"]) == len(qa["specialized_square_roots"]) == 4
    qrows = support["ct_norm_support"]["q_zero_fiber_components"]
    assert len(qrows) == 8 and sorted(x["CsK_index_1based"] for x in qrows) == list(range(27, 35))

    c22 = semantic["j2_branch_carrier"]["marked_semantic_picK_coords"]
    fixed_partial = xor_vectors(c22, coords[corner_index["E_00"]], coords[corner_index["E_inf0"]])
    assert fixed_partial == [0,0,1,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0]

    payload = {
        "schema": "STAGE33_12_J2_CT_NORM_LOCAL_LATTICE_PARITY_CONSTRAINTS_V1",
        "stage": "33-12",
        "repair_leaf": "33-05/R5e",
        "status": "PASS_EXACT_EVEN_NORM_LOCAL_DETERMINANT_PARITIES_ODD_BOUNDARY_AND_QROOT_OVERLAPS_STILL_OPEN",
        "source_locks": {key: {"path": f"stages/stage33/33-12/{name}", "canonical_sha256": sha} for key, (name, sha) in LOCKS.items()},
        "local_lattice_lemma": {
            "scope": "split or unramified quadratic DVR after an even base rescaling makes Norm(u) a unit",
            "sheet_orders": "a=ord_P(u), b=ord_sigmaP(u), k=a+b even",
            "normalized_orders": "a0=a-k/2, b0=b-k/2=-a0",
            "forced_relative_lattice_exponent": "m_P-m_sigmaP=a0 modulo common twist",
            "determinant_parity": "a0 mod 2; common twists change determinant by an even integer",
        },
        "forced_local_determinant_parities": {
            "C21": 0, "Sinf": 0, "C22_on_Kc_ramification_pullback": 1,
            "E_00": 1, "E_0inf": 0, "E_inf0": 1, "E_infinf": 0,
            "eight_unbranched_quotient_A1_exceptionals": 0,
        },
        "marked_exceptional_reconstruction": {
            "all_12_coordinates_reconstructed_exactly": True,
            "semantic_point_labels": labels,
            "marked_semantic_PicK_coordinates": coords,
            "corner_to_semantic_point_index_0based": corner_index,
        },
        "fixed_partial_marked_pic_mod2": {
            "meaning": "sum of already forced odd divisor contributions C22 + E_00 + E_inf0; unresolved T0/Tinf and q-root overlap contributions are intentionally excluded",
            "coordinates": fixed_partial,
            "is_final_ct_defect": False,
        },
        "q_root_overlap_obstruction": {
            "q_roots_simple_nonzero": True,
            "displayed_g22_square_roots_fixed": qa["specialized_square_roots"],
            "q_fiber_component_count": 8,
            "q_fiber_CsK_indices_1based": list(range(27, 35)),
            "two_stable_local_lattices_with_same_generic_split_data": ["L0=<e1,e2>", "L1=<pi*e1,e2>"],
            "basis_change": "diag(pi,1)",
            "determinant_parity_difference": 1,
            "consequence": "the actual Cech q-root overlap matrix, not the unit specialization of u alone, must select the lattice",
        },
        "odd_boundary_obstruction": {
            "divisors": ["T0", "Tinf"], "norm_order_each": -1,
            "reason": "odd norm order is outside the even-rescaling lattice lemma; exact q-square local trivialization overlap matrices are still required",
        },
        "exact_information_boundary": {
            "all_12_exceptional_marked_coordinates_materialized": True,
            "even_norm_local_determinant_parities_materialized": True,
            "fixed_partial_marked_Pic_mod2_materialized": True,
            "T0_Tinf_overlap_determinants_materialized": False,
            "q_root_actual_overlap_determinants_materialized": False,
            "actual_lambda_D_full_local_rank2_lattices_materialized": False,
            "actual_cc_ct_overlap_transition_matrices_materialized": False,
            "actual_ct_defect_marked_Pic_mod2_materialized": False,
            "integral_Pic_lift_materialized": False,
            "HS_d2_2cocycle_materialized": False,
            "HS_d2_zero_or_nonzero_proved": False,
        },
        "next_exact_subleaf": "MATERIALIZE_T0_TINF_QSQUARE_AND_QROOT_RAMIFIED_ACTUAL_CECH_OVERLAP_MATRICES_THEN_ADD_TO_FIXED_LOCAL_PARITY_CLASS_AND_COMPUTE_ACTUAL_MARKED_PIC_MOD2",
        "promotion_firewall": {
            "actual_ct_Pic_mod2_defect_zero_claim": False, "Q_defined_descent_credit_restored": False,
            "stage33_05_reclosed": False, "stage33_12_closed": False, "stage33_13_released": False,
            "theorem_credit": False, "receiver_credit": False, "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256"] = csha(payload)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["status"])
    print(payload["canonical_sha256"])


if __name__ == "__main__":
    main()
