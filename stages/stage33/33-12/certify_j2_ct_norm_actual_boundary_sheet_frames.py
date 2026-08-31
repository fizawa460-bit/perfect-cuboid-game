#!/usr/bin/env python3
"""Certify exact boundary-sheet frame data for the corrected ct norm nullhomotopy.

This certificate intentionally stops before constructing the actual rank-two Cech
lattices of Lambda_D.  It fixes the sheetwise scalar valuations of the chosen
nullhomotopy u=(A+z)/(2t) on the q-cover at the load-bearing boundary divisors.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-ct-norm-actual-boundary-sheet-frames.json"

EXPLICIT_CECH_SHA = "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"
CT_SPLITTING_SHA = "b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2"


def canonical_sha(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    explicit = json.loads((HERE / "j2-corrected-explicit-cech-mu2-lift.json").read_text(encoding="utf-8"))
    splitting = json.loads((HERE / "j2-corrected-ct-norm-splitting-module.json").read_text(encoding="utf-8"))
    assert explicit["canonical_sha256"] == EXPLICIT_CECH_SHA
    assert splitting["canonical_sha256"] == CT_SPLITTING_SHA

    t, s, v, w, z = sp.symbols("t s v w z")
    I = sp.I

    q = t**4 - 6*t**2 + 1
    A = 1 - t**2 + 2*I*t*s
    g22 = 1 - s**2 + I*s*(1 - t**2)/t
    g21 = 1 - s**2 - I*s*(1 - t**2)/t

    assert sp.simplify(A**2 - q - 4*t**2*g22) == 0
    assert sp.expand(q.subs(t, 0)) == 1
    assert sp.expand(A.subs(t, 0)) == 1
    assert sp.simplify(sp.limit(t*g22, t, 0) - I*s) == 0

    q_inf = sp.expand(v**4 * q.subs(t, 1/v))
    A_inf = sp.expand(v**2 * A.subs(t, 1/v))
    g22_inf = sp.simplify(g22.subs(t, 1/v))
    assert sp.expand(q_inf - (1 - 6*v**2 + v**4)) == 0
    assert sp.expand(A_inf - (-1 + 2*I*s*v + v**2)) == 0
    assert sp.simplify(sp.limit(v*g22_inf, v, 0) + I*s) == 0
    assert sp.simplify(A_inf**2 - q_inf - 4*v**2*g22_inf) == 0

    A_w = sp.expand(w * A.subs(s, 1/w))
    g22_w = sp.simplify(g22.subs(s, 1/w))
    assert sp.expand(A_w - (w*(1 - t**2) + 2*I*t)) == 0
    assert sp.simplify(sp.limit(w**2*g22_w, w, 0) + 1) == 0

    poly = sp.Poly((A + z)*(A - z) - 4*t**2*g22, z, domain=sp.EX)
    rel = sp.Poly(z**2 - q, z, domain=sp.EX)
    rem = sp.rem(poly, rel)
    assert sp.simplify(rem.as_expr()) == 0

    assert sp.simplify(g22 - g21 - 2*I*s*(1 - t**2)/t) == 0

    payload = {
        "schema": "STAGE33_12_J2_CT_NORM_ACTUAL_BOUNDARY_SHEET_FRAMES_V1",
        "stage": "33-12",
        "repair_leaf": "33-05/R5e",
        "status": "PASS_EXACT_ACTUAL_CT_NORM_BOUNDARY_SHEET_FRAMES_RANK2_LATTICES_AND_OVERLAPS_STILL_OPEN",
        "source_locks": {
            "explicit_cech_mu2_lift_certificate": "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",
            "explicit_cech_mu2_lift_canonical_sha256": EXPLICIT_CECH_SHA,
            "ct_norm_splitting_module_certificate": "stages/stage33/33-12/j2-corrected-ct-norm-splitting-module.json",
            "ct_norm_splitting_module_canonical_sha256": CT_SPLITTING_SHA,
        },
        "actual_nullhomotopy": {
            "q": "t^4-6*t^2+1",
            "A": "1-t^2+2*i*t*s",
            "q_cover_relation": "z^2=q",
            "g22": "1-s^2+i*s*(1-t^2)/t",
            "u": "(A+z)/(2*t)",
            "sigma_u": "(A-z)/(2*t)",
            "exact_norm_identity": "u*sigma_u=g22",
            "polynomial_identity": "A^2-q=4*t^2*g22",
        },
        "boundary_sheet_frames": {
            "T0": {
                "uniformizer": "t",
                "cover_special_fiber": "z^2=1",
                "sheet_z_plus_1": {"ord_u": -1, "ord_sigma_u": 0, "regular_unit_frame_for_u": "t*u"},
                "sheet_z_minus_1": {"ord_u": 0, "ord_sigma_u": -1, "regular_unit_frame_for_u": "u"},
                "ord_norm": -1,
                "exact_check": "ord_t(g22)=-1 and (A+z)(A-z)=4*t^2*g22",
            },
            "Tinf": {
                "uniformizer": "v=1/t",
                "rescaled_cover_coordinate": "z_inf=v^2*z",
                "A_inf": "v^2*A=-1+2*i*s*v+v^2",
                "cover_special_fiber": "z_inf^2=1",
                "sheet_z_inf_plus_1": {"ord_u": 0, "ord_sigma_u": -1, "regular_unit_frame_for_u": "u"},
                "sheet_z_inf_minus_1": {"ord_u": -1, "ord_sigma_u": 0, "regular_unit_frame_for_u": "v*u"},
                "ord_norm": -1,
                "exact_check": "u=(A_inf+z_inf)/(2*v), ord_v(g22)=-1",
            },
            "Sinf": {
                "uniformizer": "w=1/s",
                "rewritten_numerator": "w*(A+z)=w*(1-t^2+z)+2*i*t",
                "all_generic_q_sheets": {"ord_u": -1, "ord_sigma_u": -1, "regular_unit_frame_for_u": "w*u"},
                "ord_norm": -2,
                "exact_check": "ord_w(g22)=-2 and w*(A+z)|_{w=0}=2*i*t",
            },
            "C22": {
                "generic_cover_components": ["D22_plus: z=A", "D22_minus: z=-A"],
                "D22_plus": {"ord_u": 0, "ord_sigma_u": 1, "regular_unit_frame_for_u": "u"},
                "D22_minus": {"ord_u": 1, "ord_sigma_u": 0, "regular_unit_frame_for_u": "u/g22"},
                "ord_norm": 1,
                "exact_check": "A^2=q on g22=0 and g22 is the norm of u",
            },
            "C21": {
                "generic_q_cover": "away from C21 intersection with C22 and boundary divisors",
                "all_generic_components": {"ord_u": 0, "ord_sigma_u": 0, "regular_unit_frame_for_u": "u"},
                "ord_norm": 0,
                "exact_check": "g22 is generically a unit on C21; A+z and A-z can vanish only over g22=0",
            },
        },
        "resolution_exceptionals": {
            "actual_sheet_frames_materialized": False,
            "reason": "The previously certified zero mu2 residue on resolution exceptionals does not determine the actual compactified rank-two lattice frame or overlap transition. Exact resolved-chart pullbacks are still required.",
        },
        "state": {
            "actual_ct_nullhomotopy_boundary_sheet_frames_materialized": True,
            "actual_lambda_D_local_rank2_lattices_materialized": False,
            "actual_overlap_transition_matrices_materialized": False,
            "marked_pic_mod2_defect_materialized": False,
            "HS_d2_2cocycle_materialized": False,
            "HS_d2_zero_proved": False,
        },
        "what_this_removes": [
            "The pole/zero sheet choices of the chosen ct nullhomotopy at T0 and Tinf are no longer left to a generic q-cover splitting template.",
            "The common simple pole at Sinf and the asymmetric simple zero over C22 are fixed for the actual u=(A+z)/(2t).",
            "Any eventual compactified rank-two lattice for the ct nullhomotopy must reproduce these exact local scalar valuations.",
        ],
        "what_remains": [
            "Pull the actual chosen Cech lambda_D and these ct frames through the explicit resolution charts, especially every resolution exceptional.",
            "Build the actual local rank-two lattices on T0,Tinf,Sinf,C21,C22 and the resolution charts.",
            "Materialize all overlap transition matrices and determinant divisors.",
            "Compare the cc and ct nullhomotopies in the marked Pic(Kc_bar)/2 basis.",
            "Choose integral Pic lifts and compute the Hochschild-Serre d2 2-cocycle and its cohomology class.",
        ],
        "next_exact_subleaf": "MATERIALIZE_RESOLVED_CHART_PULLBACKS_AND_ACTUAL_RANK2_CECH_LATTICES_FROM_THE_FIXED_BOUNDARY_SHEET_FRAMES_THEN_COMPUTE_OVERLAP_DETERMINANTS_MARKED_PIC_MOD2_AND_HS_D2",
        "promotion_firewall": {
            "actual_ct_Pic_mod2_defect_zero_claim": False,
            "Q_defined_descent_credit_restored": False,
            "stage33_05_reclosed": False,
            "stage33_12_closed": False,
            "stage33_13_released": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256"] = canonical_sha(payload)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(payload["status"])
    print(payload["canonical_sha256"])


if __name__ == "__main__":
    main()
