#!/usr/bin/env python3
"""Materialize the current V25 lambda_D rank-two lattices wherever the ct norm
order is even, including the doubled C22 ramification valuation.

This leaf deliberately leaves T0/Tinf and q-root overlap selection open.  It
uses only the current V25 Cech lift plus V27/V28 scalar geometry; the revoked
historical pre-Kummer sheet selection is not imported.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-current-lambda-D-even-norm-rank2-lattices-v29.json"

LOCKS = {
    "v25_current_named_j2": (HERE / "j2-genuine-h2-mu2-kummer-adapter-v25.json", "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
    "explicit_cech_mu2_lift": (HERE / "j2-corrected-explicit-cech-mu2-lift.json", "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"),
    "v27_boundary_valuations": (HERE / "j2-ct-norm-splitting-boundary-valuations-v27.json", "355c2a6dcb27f163ba6236a4e6790f090d03dbd7e74c89d76c2cf7a5c2e1ccc4"),
    "actual_boundary_sheet_frames": (HERE / "j2-ct-norm-actual-boundary-sheet-frames.json", "5b961822dc10e7a1a424ed87ba6307d83efd3a0b31671db305a609269094937b"),
    "resolution_exceptional_sheet_frames": (HERE / "j2-ct-norm-resolution-exceptional-sheet-frames.json", "bbde421a54d2b7159f8d3ff4cf641cbddf2bbbc45fe4791cb7ed18d7cfb69591"),
    "v28_exceptional_overlap_audit": (HERE / "j2-post-v27-exceptional-overlap-inheritance-audit-v28.json", "919c1fd1dfb57f0e86677e64052636918082d7ef0cf9a9f79afe51051eb96095"),
}
EXPECTED = "b4caf6675d619f85a9a22463a384541d27c54002076d03363ee00b0538a6ec5b"


def csha(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), (path, claimed, csha(body))
    return obj


def record(label: str, uniformizer: str, k: int, ou: int, osig: int, chart: str, sheet: str) -> dict:
    assert k % 2 == 0
    half = k // 2
    u0 = ou - half
    s0 = osig - half
    assert u0 + s0 == 0
    return {
        "label": label,
        "chart": chart,
        "sheet": sheet,
        "uniformizer": uniformizer,
        "raw_orders": {"u": ou, "sigma_u": osig, "norm": k},
        "normalized_orders": {"u0": u0, "sigma_u0": s0, "norm0": 0},
        "normalized_scalars": {
            "u0": f"{uniformizer}^({-half})*u",
            "sigma_u0": f"{uniformizer}^({-half})*sigma(u)",
            "b0": f"{uniformizer}^({-k})*g22",
        },
        "integral_rank2_lattice_basis": [f"({uniformizer}^({-half})*sigma(u))*e1", "e2"],
        "punctured_overlap_transition_matrix": [[f"{uniformizer}^({-half})*sigma(u)", "0"], ["0", "1"]],
        "determinant_valuation": s0,
        "determinant_parity": s0 % 2,
        "overlap_ring": f"O_{label}[1/{uniformizer}]",
        "construction": "G=diag(sigma_u0,1); G*Y0*G^-1=J0 with Y0=[[0,u0],[sigma_u0,0]], J0=[[0,b0],[1,0]]",
    }


def build() -> dict:
    d = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
    v25 = d["v25_current_named_j2"]
    explicit = d["explicit_cech_mu2_lift"]
    v27 = d["v27_boundary_valuations"]
    boundary = d["actual_boundary_sheet_frames"]
    exc = d["resolution_exceptional_sheet_frames"]
    v28 = d["v28_exceptional_overlap_audit"]

    assert v25["genuine_h2_mu2_adapter"]["kc_lift_class"] == "lambda_D=alpha(e_D), represented generically by {f2,g22}"
    assert v25["current_named_source"]["retained10_mask_decimal"] == 6
    assert v25["current_named_source"]["two_bit_value_a_b"] == [0, 1]
    assert explicit["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True
    assert "valuation 2" in explicit["surface_mu2_lift"]["ramification_check"]
    assert v27["norm_consistency"]["all_rows_satisfy_v_u_plus_v_deck_u_equals_v_g22"] is True
    assert v28["historical_overlap_promotion_audit"]["historical_candidate_inherited_as_current_authority"] is False

    bf = boundary["boundary_sheet_frames"]
    ef = exc["actual_ct_resolution_exceptional_sheet_frames"]
    rows = []
    rows.append(record("C21_generic", "eta21", bf["C21"]["ord_norm"], 0, 0, "C21", "generic"))
    rows.append(record("Sinf_generic", "w", bf["Sinf"]["ord_norm"], bf["Sinf"]["all_generic_q_sheets"]["ord_u"], bf["Sinf"]["all_generic_q_sheets"]["ord_sigma_u"], "s=infinity", "generic"))
    rows.append(record("C22_ramification", "rho", 2, 0, 2, "Kc ramification over C22", "orientation u unit / sigma_u order 2"))

    for name in ("E_00", "E_0inf", "E_inf0", "E_infinf"):
        for sheet_key, short in (("sheet_plus", "plus"), ("sheet_minus", "minus")):
            x = ef[name]
            s = x[sheet_key]
            rows.append(record(f"{name}_{short}", "e", x["ord_norm"], s["ord_u"], s["ord_sigma_u"], "resolution exceptional", short))

    q = exc["quotient_A1_exceptional_frames"]
    assert q["generic_ord_norm"] == 0
    assert q["generic_ord_u_on_every_auxiliary_q_cover_component"] == 0
    assert q["generic_ord_sigma_u_on_every_auxiliary_q_cover_component"] == 0
    for i in range(1, 9):
        rows.append(record(f"Q_A1_{i}", "e", 0, 0, 0, "unbranched quotient-A1 exceptional", f"lift_{i}"))

    assert len(rows) == 19
    parity = {r["label"]: r["determinant_parity"] for r in rows}
    assert parity["C21_generic"] == parity["Sinf_generic"] == 0
    assert parity["C22_ramification"] == 1
    assert [parity["E_00_plus"], parity["E_00_minus"]] == [1, 1]
    assert [parity["E_0inf_plus"], parity["E_0inf_minus"]] == [0, 0]
    assert [parity["E_inf0_plus"], parity["E_inf0_minus"]] == [1, 1]
    assert [parity["E_infinf_plus"], parity["E_infinf_minus"]] == [0, 0]
    assert all(parity[f"Q_A1_{i}"] == 0 for i in range(1, 9))
    forced = v28["retainable_local_parity_constraints"]["forced_parities"]
    assert forced["C21"] == 0 and forced["Sinf"] == 0
    assert forced["C22_on_Kc_ramification_pullback"] == 1
    assert forced["E_00"] == 1 and forced["E_0inf"] == 0
    assert forced["E_inf0"] == 1 and forced["E_infinf"] == 0

    out = {
        "schema": "STAGE33_12_J2_CURRENT_LAMBDA_D_EVEN_NORM_RANK2_LATTICES_V29",
        "stage": "33-12",
        "repair_leaf": "33-05/R5e",
        "status": "PASS_EXACT_CURRENT_LAMBDA_D_EVEN_NORM_AND_C22_RAMIFICATION_RANK2_LATTICES_MATERIALIZED_ODD_BOUNDARY_QROOT_OVERLAPS_OPEN",
        "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
        "current_lambda_D": {
            "class": "lambda_D=alpha(e_D), represented generically by {f2,g22}",
            "named_source_retained10_mask_decimal": 6,
            "two_bit_value_a_b": [0, 1],
            "historical_weight15_target_used": False,
            "pre_kummer_sheet_selection_used": False,
        },
        "normalized_norm_basis_model": {
            "ambient_operator": "Y0=[[0,u0],[sigma_u0,0]]",
            "normalized_scalars": "for even k=ord(g22), u0=pi^(-k/2)u, sigma_u0=pi^(-k/2)sigma(u), b0=pi^(-k)g22",
            "identity": "u0*sigma_u0=b0 is a DVR unit",
            "lattice_basis": "L=<sigma_u0*e1,e2>",
            "transition_matrix": "G=diag(sigma_u0,1) on the punctured DVR overlap",
            "conjugation": "G*Y0*G^-1=[[0,b0],[1,0]]",
            "determinant_valuation": "ord(sigma_u)-k/2",
            "integrality_meaning": "the displayed generators are an O_DVR-basis of the selected fractional rank-two lattice inside the generic two-dimensional space; G is required only over O_DVR[1/pi]",
        },
        "materialized_local_lattices": {
            "record_count": 19,
            "named_even_norm_or_ramification_sites": [
                "C21", "Sinf", "C22 ramification pullback",
                "E_00 plus/minus", "E_0inf plus/minus", "E_inf0 plus/minus", "E_infinf plus/minus",
                "eight unbranched quotient-A1 exceptional lifts",
            ],
            "records": rows,
            "parity_summary": {
                "C21": 0, "Sinf": 0, "C22_on_Kc_ramification_pullback": 1,
                "E_00": [1, 1], "E_0inf": [0, 0], "E_inf0": [1, 1], "E_infinf": [0, 0],
                "eight_unbranched_quotient_A1_exceptionals": [0, 0, 0, 0, 0, 0, 0, 0],
            },
            "reproduces_v28_forced_even_norm_parities": True,
            "all_matrices_explicit_2x2_on_declared_punctured_overlap_ring": True,
        },
        "exact_information_boundary": {
            "current_lambda_D_even_norm_local_rank2_lattices_materialized": True,
            "current_lambda_D_C22_ramification_rank2_lattice_materialized": True,
            "current_lambda_D_T0_Tinf_rank2_lattices_materialized": False,
            "current_lambda_D_qroot_rank2_lattices_materialized": False,
            "actual_full_cech_local_rank2_lattice_system_materialized": False,
            "actual_full_cc_ct_overlap_transition_system_materialized": False,
            "actual_ct_defect_marked_Pic_mod2_materialized": False,
            "full_Galois_Pic_mod2_1cocycle_materialized": False,
            "integral_Pic_lift_materialized": False,
            "HS_d2_2cocycle_materialized": False,
            "standard_kummer_columns_materialized": 0,
        },
        "unresolved_load_bearing_overlaps": {
            "T0": "ord(g22)=-1, so the even-norm normalization used here does not select an integral lattice; current lambda_D overlap data still required.",
            "Tinf": "ord(g22)=-1, same obstruction.",
            "q_roots": "ramified q-cover overlaps require actual current Cech square witnesses/lattice gluing; historical pre-Kummer sheet choices remain non-authoritative.",
            "cc_component": "not computed in this leaf.",
        },
        "next_exact_leaf": "MATERIALIZE_CURRENT_LAMBDA_D_T0_TINF_AND_QROOT_RANK2_LATTICES_WITH_EXPLICIT_2X2_OVERLAP_MATRICES_FROM_CURRENT_V25_CECH_LIFT_ONLY_THEN_ASSEMBLE_CURRENT_CT_MARKED_PIC_MOD2_DEFECT",
        "promotion_firewall": {
            "stage33_progress": "6/11", "stage33_12_closed_exact": False,
            "stage33_07_reclosed": False, "stage33_08_released": False,
            "theorem_credit": False, "receiver_credit": False, "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False,
            "merge_allowed": False,
        },
    }
    assert csha(out) == EXPECTED
    return out


def main() -> None:
    out = build()
    if "--check" in sys.argv:
        assert locked(OUT, EXPECTED) == {**out, "canonical_sha256": EXPECTED}
    else:
        payload = dict(out)
        payload["canonical_sha256"] = EXPECTED
        OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "success": True,
        "canonical_sha256": EXPECTED,
        "materialized_local_rank2_lattice_records": 19,
        "T0_Tinf_qroot_open": True,
        "historical_pre_kummer_selection_used": False,
        "marker": "PROOF_REPLAY_COMPLETE",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
