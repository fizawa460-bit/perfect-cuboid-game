#!/usr/bin/env python3
"""Certify the actual ct nullhomotopy scalar frames on all Kc resolution exceptionals.

This is an R5e hardening leaf only. It accounts for the four branch-crossing
A1 nodes and the eight unbranched lifts of the four quotient A1 nodes, but it
intentionally does not promote scalar frames to the compactified rank-two Cech
lattice or to a Pic/2/HS d2 conclusion.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-ct-norm-resolution-exceptional-sheet-frames.json"

BOUNDARY_SHA = "5b961822dc10e7a1a424ed87ba6307d83efd3a0b31671db305a609269094937b"
ADAPTER_SHA = "edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875"


def canonical_sha(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def scaled_limit(expr: sp.Expr, e: sp.Symbol, order: int) -> sp.Expr:
    return sp.simplify(sp.limit(expr / e**order, e, 0))


def assert_generic_nonzero(expr: sp.Expr, r: sp.Symbol) -> None:
    expr = sp.factor(expr)
    assert expr != 0
    num, den = sp.fraction(expr)
    assert sp.Poly(num, r, extension=sp.I).as_expr() != 0
    assert sp.Poly(den, r, extension=sp.I).as_expr() != 0


def main() -> None:
    boundary = json.loads((HERE / "j2-ct-norm-actual-boundary-sheet-frames.json").read_text(encoding="utf-8"))
    adapter = json.loads((HERE / "j2-corrected-branch-surface-mu2-adapter.json").read_text(encoding="utf-8"))
    assert boundary["canonical_sha256"] == BOUNDARY_SHA
    assert adapter["canonical_sha256"] == ADAPTER_SHA
    geom = adapter["double_cover_geometry"]
    assert geom["branch_crossing_count"] == 4
    assert geom["quotient_A1_node_count"] == 4
    assert geom["etale_preimage_node_count_on_Kc"] == 8
    assert adapter["resolution_adapter"]["quotient_A1_resolutions_unbranched"] is True

    I = sp.I
    A1, A2, A3, B1, B2, B3 = sp.symbols("A1 A2 A3 B1 B2 B3")
    variables = [A1, A2, A3, B1, B2, B3]
    eqs = [
        A1**2 + A2**2 - B3**2,
        A2**2 + A3**2 - B1**2,
        A1**2 + A3**2 - B2**2,
    ]
    jac = sp.Matrix(eqs).jacobian(variables)

    crossing_nodes = [(1, 0, 0, 0, e2, e3) for e2 in (1, -1) for e3 in (1, -1)]
    quotient_lifts = (
        [(0, 1, 0, d, 0, eps) for d in (1, -1) for eps in (1, -1)]
        + [(0, 0, 1, d, eps, 0) for d in (1, -1) for eps in (1, -1)]
    )
    all_nodes = crossing_nodes + quotient_lifts
    assert len(set(all_nodes)) == 12
    for point in all_nodes:
        subs = dict(zip(variables, point))
        assert all(sp.expand(f.subs(subs)) == 0 for f in eqs)
        assert jac.subs(subs).rank() == 2
    assert len(all_nodes) == geom["branch_crossing_count"] + geom["etale_preimage_node_count_on_Kc"]

    T0, T1, S0, S1 = sp.symbols("T0 T1 S0 S1")
    param = [
        (T0**2 - T1**2) * (S0**2 - S1**2),
        2 * T0 * T1 * (S0**2 - S1**2),
        2 * S0 * S1 * (T0**2 - T1**2),
        (S0**2 + S1**2) * (T0**2 - T1**2),
        (T0**2 + T1**2) * (S0**2 - S1**2),
    ]
    corners = {
        "E_00": ((1, 0, 1, 0), (1, 0, 0, 1, 1)),
        "E_0inf": ((1, 0, 0, 1), (1, 0, 0, -1, 1)),
        "E_inf0": ((0, 1, 1, 0), (1, 0, 0, 1, -1)),
        "E_infinf": ((0, 1, 0, 1), (1, 0, 0, -1, -1)),
    }
    for _, (p, expected) in corners.items():
        vals = [sp.expand(x.subs(dict(zip((T0, T1, S0, S1), p)))) for x in param]
        first = next(x for x in vals if x != 0)
        vals = tuple(sp.simplify(x / first) for x in vals)
        assert vals == expected

    t, s, v, w, e, r = sp.symbols("t s v w e r")
    q = t**4 - 6*t**2 + 1
    A = 1 - t**2 + 2*I*t*s
    g22 = 1 - s**2 + I*s*(1 - t**2)/t
    z0 = sp.sqrt(e**4 - 6*e**2 + 1)
    zinf = sp.sqrt(e**4 - 6*e**2 + 1)
    assert sp.simplify(A**2 - q - 4*t**2*g22) == 0

    def u0(ss: sp.Expr, zz: sp.Expr) -> sp.Expr:
        return sp.simplify((1 - e**2 + 2*I*e*ss + zz) / (2*e))

    def uinf(ss: sp.Expr, zzinf: sp.Expr) -> sp.Expr:
        return sp.simplify((-1 + 2*I*ss*e + e**2 + zzinf) / (2*e))

    exceptional_u = {
        "E_00_plus": (u0(e*r, z0), -1),
        "E_00_minus": (u0(e*r, -z0), 1),
        "E_0inf_plus": (u0(1/(e*r), z0), -1),
        "E_0inf_minus": (u0(1/(e*r), -z0), -1),
        "E_inf0_plus": (uinf(e*r, zinf), 1),
        "E_inf0_minus": (uinf(e*r, -zinf), -1),
        "E_infinf_plus": (uinf(1/(e*r), zinf), -1),
        "E_infinf_minus": (uinf(1/(e*r), -zinf), -1),
    }
    for expr, order in exceptional_u.values():
        assert_generic_nonzero(scaled_limit(expr, e, order), r)

    norm_orders = {
        "E_00": (g22.subs({t: e, s: e*r}), 0),
        "E_0inf": (g22.subs({t: e, s: 1/(e*r)}), -2),
        "E_inf0": (g22.subs({t: 1/e, s: e*r}), 0),
        "E_infinf": (g22.subs({t: 1/e, s: 1/(e*r)}), -2),
    }
    for expr, order in norm_orders.values():
        assert_generic_nonzero(scaled_limit(expr, e, order), r)

    z = sp.Symbol("z")
    u = (A + z) / (2*t)
    assert sp.expand(q.subs(t, 1)) == -4
    assert sp.expand(q.subs(t, -1)) == -4
    assert sp.simplify(u.subs({t: 1, z: 2*I}) - I*(s+1)) == 0
    assert sp.simplify(u.subs({t: 1, z: -2*I}) - I*(s-1)) == 0
    assert sp.simplify(u.subs({t: -1, z: 2*I}) - I*(s-1)) == 0
    assert sp.simplify(u.subs({t: -1, z: -2*I}) - I*(s+1)) == 0
    assert sp.simplify(g22.subs(s, 1) - I*(1-t**2)/t) == 0
    assert sp.simplify(g22.subs(s, -1) + I*(1-t**2)/t) == 0

    payload = {
        "schema": "STAGE33_12_J2_CT_NORM_RESOLUTION_EXCEPTIONAL_SHEET_FRAMES_V1",
        "stage": "33-12",
        "repair_leaf": "33-05/R5e",
        "status": "PASS_EXACT_RESOLUTION_EXCEPTIONAL_SCALAR_FRAMES_ACTUAL_RANK2_CECH_LATTICES_STILL_OPEN",
        "source_locks": {
            "boundary_sheet_frames_certificate": "stages/stage33/33-12/j2-ct-norm-actual-boundary-sheet-frames.json",
            "boundary_sheet_frames_canonical_sha256": BOUNDARY_SHA,
            "branch_surface_resolution_adapter_certificate": "stages/stage33/33-12/j2-corrected-branch-surface-mu2-adapter.json",
            "branch_surface_resolution_adapter_canonical_sha256": ADAPTER_SHA,
        },
        "singular_partition": {
            "Kc_equations": ["A1^2+A2^2-B3^2=0", "A2^2+A3^2-B1^2=0", "A1^2+A3^2-B2^2=0"],
            "total_Kc_A1_nodes": 12,
            "branch_crossing_nodes": 4,
            "unbranched_lifts_of_quotient_A1_nodes": 8,
            "partition_verified_by_exact_jacobian_rank": True,
            "branch_crossing_coordinates": [
                ["1", "0", "0", "0", "1", "1"], ["1", "0", "0", "0", "-1", "1"],
                ["1", "0", "0", "0", "1", "-1"], ["1", "0", "0", "0", "-1", "-1"],
            ],
            "quotient_A1_lift_families": [
                "[0,1,0,delta,0,epsilon], delta,epsilon in {+1,-1}",
                "[0,0,1,delta,epsilon,0], delta,epsilon in {+1,-1}",
            ],
        },
        "branch_crossing_corner_identification": {
            "quotient_parametrization": [
                "A1=(1-t^2)*(1-s^2)", "A2=2*t*(1-s^2)", "A3=2*s*(1-t^2)",
                "B2=(1+s^2)*(1-t^2)", "B3=(1+t^2)*(1-s^2)",
            ],
            "corners": {
                "E_00": {"corner": "(t,s)=(0,0)", "Kc_node": ["1", "0", "0", "0", "1", "1"]},
                "E_0inf": {"corner": "(t,w)=(0,0), w=1/s", "Kc_node": ["1", "0", "0", "0", "-1", "1"]},
                "E_inf0": {"corner": "(v,s)=(0,0), v=1/t", "Kc_node": ["1", "0", "0", "0", "1", "-1"]},
                "E_infinf": {"corner": "(v,w)=(0,0), v=1/t,w=1/s", "Kc_node": ["1", "0", "0", "0", "-1", "-1"]},
            },
            "blowup_divisorial_valuation_rule": "ord_E is total order in the maximal ideal of the displayed smooth corner; verified on a generic blowup chart by setting both corner parameters equal to e times units.",
        },
        "actual_ct_resolution_exceptional_sheet_frames": {
            "E_00": {
                "generic_blowup_substitution": "t=e, s=e*r",
                "q_sheet_plus_near": "+sqrt(q), z|e=0=+1", "q_sheet_minus_near": "-sqrt(q), z|e=0=-1",
                "sheet_plus": {"ord_u": -1, "ord_sigma_u": 1, "regular_unit_frame_for_u": "e*u"},
                "sheet_minus": {"ord_u": 1, "ord_sigma_u": -1, "regular_unit_frame_for_u": "u/e"}, "ord_norm": 0,
            },
            "E_0inf": {
                "generic_blowup_substitution": "t=e, w=e*r, w=1/s",
                "q_sheet_plus_near": "+sqrt(q), z|e=0=+1", "q_sheet_minus_near": "-sqrt(q), z|e=0=-1",
                "sheet_plus": {"ord_u": -1, "ord_sigma_u": -1, "regular_unit_frame_for_u": "e*u"},
                "sheet_minus": {"ord_u": -1, "ord_sigma_u": -1, "regular_unit_frame_for_u": "e*u"}, "ord_norm": -2,
            },
            "E_inf0": {
                "generic_blowup_substitution": "v=e, s=e*r, v=1/t", "rescaled_q_coordinate": "z_inf=v^2*z",
                "q_sheet_plus_near": "+sqrt(q_inf), z_inf|e=0=+1", "q_sheet_minus_near": "-sqrt(q_inf), z_inf|e=0=-1",
                "sheet_plus": {"ord_u": 1, "ord_sigma_u": -1, "regular_unit_frame_for_u": "u/e"},
                "sheet_minus": {"ord_u": -1, "ord_sigma_u": 1, "regular_unit_frame_for_u": "e*u"}, "ord_norm": 0,
            },
            "E_infinf": {
                "generic_blowup_substitution": "v=e, w=e*r, v=1/t,w=1/s", "rescaled_q_coordinate": "z_inf=v^2*z",
                "q_sheet_plus_near": "+sqrt(q_inf), z_inf|e=0=+1", "q_sheet_minus_near": "-sqrt(q_inf), z_inf|e=0=-1",
                "sheet_plus": {"ord_u": -1, "ord_sigma_u": -1, "regular_unit_frame_for_u": "e*u"},
                "sheet_minus": {"ord_u": -1, "ord_sigma_u": -1, "regular_unit_frame_for_u": "e*u"}, "ord_norm": -2,
            },
        },
        "quotient_A1_exceptional_frames": {
            "geometry": "The four quotient A1 resolutions are unbranched for the B1 double cover, hence give eight Kc exceptional curves.",
            "generic_ord_u_on_every_auxiliary_q_cover_component": 0,
            "generic_ord_sigma_u_on_every_auxiliary_q_cover_component": 0,
            "generic_ord_norm": 0,
            "t_node_restrictions": {
                "t=+1": "q=-4; on z=+2*i/-2*i sheets, u=i*(s+1) / i*(s-1), respectively",
                "t=-1": "q=-4; on z=+2*i/-2*i sheets, u=i*(s-1) / i*(s+1), respectively",
            },
            "s_node_restrictions": {
                "s=+1": "u=(1-t^2+2*i*t+z)/(2*t), generically nonzero on z^2=q",
                "s=-1": "u=(1-t^2-2*i*t+z)/(2*t), generically nonzero on z^2=q",
            },
            "warning": "Zeros at special points of an exceptional curve do not change the divisorial valuation of u along that exceptional; they belong to codimension-two overlap data.",
        },
        "exact_information_boundary": {
            "actual_ct_resolution_exceptional_scalar_frames_materialized": True,
            "all_12_Kc_resolution_exceptionals_accounted_for": True,
            "actual_lambda_D_local_rank2_lattices_materialized": False,
            "actual_cc_ct_overlap_transition_matrices_materialized": False,
            "actual_ct_defect_marked_Pic_mod2_materialized": False,
            "HS_d2_2cocycle_materialized": False,
            "HS_d2_zero_or_nonzero_proved": False,
            "reason": "Resolution-exceptional scalar valuations of the chosen ct nullhomotopy are now fixed, but scalar frames still do not select the actual compactified rank-two Cech lattice or its elementary transforms. Overlap matrices remain load-bearing.",
        },
        "what_this_removes": [
            "No resolution exceptional remains with an unknown generic scalar valuation for the chosen u=(A+z)/(2*t).",
            "The four branch-crossing exceptionals have exact sheetwise pole/zero orders, including the asymmetric E_00 and E_inf0 transforms.",
            "The eight unbranched quotient-A1 lift exceptionals are exact generic units for u and sigma(u).",
        ],
        "next_exact_subleaf": "BUILD_ACTUAL_RANK2_CECH_LATTICES_AND_OVERLAP_MATRICES_FROM_FIXED_BOUNDARY_AND_ALL_RESOLUTION_EXCEPTIONAL_SCALAR_FRAMES_THEN_COMPUTE_DETERMINANT_DIVISORS_MARKED_PIC_MOD2_AND_HS_D2",
        "promotion_firewall": {
            "actual_ct_Pic_mod2_defect_zero_claim": False, "Q_defined_descent_credit_restored": False,
            "stage33_05_reclosed": False, "stage33_12_closed": False, "stage33_13_released": False,
            "theorem_credit": False, "receiver_credit": False, "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256"] = canonical_sha(payload)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(payload["status"])
    print(payload["canonical_sha256"])


if __name__ == "__main__":
    main()
