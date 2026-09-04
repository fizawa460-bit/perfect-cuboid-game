#!/usr/bin/env python3
"""Verify V73: exact J1 semilinear translation torsor from the V71 cocycle."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
V73_PATH = HERE / "e3-b1-c22-j1-translation-torsor-v73.json"
V71_PATH = HERE / "e3-b1-c22-j1-cv-e2-cocycle-v71.json"
J2_TEMPLATE_PATH = HERE.parent / "33-05" / "j2-r4-correct-translation-torsor.json"
PW07_PATH = ROOT / "docs/arsenal/cards/provisional/S33-PW07.md"
ROADMAP_PATH = HERE.parent / "ROADMAP-33-12-V71-J1-TORSOR.md"

EXPECTED_V73 = "b6a8dd83cd83547525e8ff328cccc1572791c52bea6061137c2bc59a134fa09d"
EXPECTED_V71_BLOB = "5073a38366aa8715b5ce27115a1d055386a0869a"
EXPECTED_J2_TEMPLATE_BLOB = "5a0ac87e7afc7b048d6bbe9c12bea7fe91a0348b"
EXPECTED_PW07_BLOB = "7f1337858bc6f9006e101d810dd72e67aef534fd"
EXPECTED_ROADMAP_BLOB = "b979b286c8d2c8f009989fa26e1e7d98c12d2b53"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


# Tiny exact Laurent-polynomial check for invariance under
# w -> -w, x -> b/x, y -> -b*y/x^2, b -> b.
# Monomial exponents are (w,x,y,b); coefficients are integers.
def transform_monomial(m, coeff):
    ew, ex, ey, eb = m
    sign = -1 if (ew + ey) % 2 else 1
    return (ew, -ex - 2 * ey, ey, ex + ey + eb), coeff * sign


def transform(poly):
    out = {}
    for m, c in poly.items():
        mm, cc = transform_monomial(m, c)
        out[mm] = out.get(mm, 0) + cc
    return {m: c for m, c in out.items() if c}


def main():
    v73 = json.loads(V73_PATH.read_text())
    body = dict(v73)
    claimed = body.pop("canonical_sha256")
    require(claimed == EXPECTED_V73 == csha(body), "V73 canonical hash mismatch")

    require(blob_sha(V71_PATH) == EXPECTED_V71_BLOB, "V71 blob drift")
    require(blob_sha(J2_TEMPLATE_PATH) == EXPECTED_J2_TEMPLATE_BLOB, "J2 method-template blob drift")
    require(blob_sha(PW07_PATH) == EXPECTED_PW07_BLOB, "S33-PW07 blob drift")
    require(blob_sha(ROADMAP_PATH) == EXPECTED_ROADMAP_BLOB, "V71 roadmap blob drift")

    v71 = json.loads(V71_PATH.read_text())
    j2 = json.loads(J2_TEMPLATE_PATH.read_text())
    pw07 = PW07_PATH.read_text()

    require(v71["canonical_sha256"] == "3e9409ee7537ab4edb12e2416745bbd074f1cc1b02a4fc8a92be643075b8569a", "V71 canonical moved")
    require(v71["j1_full_l_representative"]["pair_in_L"] == "(f1,1)", "J1 L-pair moved")
    require(v71["j1_full_l_representative"]["f1"] == "(t-r1)/(t-r4)", "f1 moved")
    require(v71["cv_cocycle"]["xi_rho"] == "Tr", "J1 cocycle translation point moved")
    require(v71["cv_cocycle"]["cocycle_bits_in_fixed_basis"] == [0, 1], "J1 cocycle bits moved")
    require(v71["cv_cocycle"]["splitting_field"] == "Kgeom(sqrt(f1))", "J1 splitting field moved")
    require(v71["credit_firewall"]["j1_translation_torsor_materialized"] is False, "V71 historical boundary moved")

    require("TORSOR_BRAUER_INTEGRAL_KERNEL_ADAPTER" in pw07, "S33-PW07 role missing")
    require("semilinear translation descent using the SAME cocycle" in pw07, "S33-PW07 same-cocycle contract missing")
    require("isogeny-cover substitution" in pw07, "S33-PW07 isogeny firewall missing")

    require(j2["fixed_data"]["a"] == "(t^2+1)^2", "shifted a moved")
    require(j2["fixed_data"]["b"] == "[2*t*(t^2-1)]^2", "shifted b moved")
    require(j2["fixed_data"]["identity"] == "a^2-4*b=q^2", "discriminant-square identity moved")
    require(j2["correct_translation_descent"]["translation_by_Tr"] == "tau_Tr(x,y)=(b/x,-b*y/x^2)", "Tr translation formula moved")
    require(j2["correct_translation_descent"]["jacobian"] == "E: y^2=x*(x^2+a*x+b)", "method-template Jacobian moved")

    inp = v73["j1_cocycle_input"]
    require(inp["named_class"] == "kappa_A=J1", "V73 named class is not J1")
    require(inp["full_L_pair"] == "(f1,1)", "V73 L-pair is not J1")
    require(inp["d"] == "f1=(t-r1)/(t-r4)", "V73 d is not f1")
    require(inp["splitting_field"] == "L1=Kgeom(w), w^2=d", "V73 splitting field model moved")
    require(inp["rho_w"] == "rho(w)=-w", "V73 rho action moved")
    require(inp["xi_rho"] == "Tr", "V73 translation point moved")
    require(inp["cocycle_bits_in_fixed_E2_basis"] == [0, 1], "V73 cocycle bits moved")
    require(inp["semilinear_action"] == "tilde_rho=tau_Tr o rho", "V73 semilinear action moved")

    n = {(1, -1, 1, 0): 1}
    u0 = {(0, 1, 0, 0): 1, (0, -1, 0, 1): 1}
    v = {(1, 1, 0, 0): 1, (1, -1, 0, 1): -1}
    require(transform(n) == n, "n is not invariant")
    require(transform(u0) == u0, "u0 is not invariant")
    require(transform(v) == v, "v is not invariant")

    deriv = v73["semilinear_invariant_derivation"]
    require(deriv["invariant_functions"] == {"n": "w*y/x", "u0": "x+b/x", "v": "w*(x-b/x)"}, "invariant functions moved")
    require(deriv["relations"] == [
        "y^2/x^2=x+a+b/x=u0+a",
        "n^2=d*(u0+a)",
        "(x-b/x)^2=(x+b/x)^2-4*b=u0^2-4*b",
        "v^2=d*(u0^2-4*b)",
    ], "invariant relations moved")
    require(deriv["elimination"] == "u0=n^2/d-a and a^2-4*b=q^2 imply d*v^2=n^4-2*a*d*n^2+d^2*q^2", "quartic elimination moved")

    torsor = v73["translation_torsor"]
    require(torsor["affine_quartic"] == "d*v^2=n^4-2*a*d*n^2+d^2*q^2", "affine J1 torsor moved")
    require(torsor["homogeneous_weighted_quartic"] == "d*V^2=N^4-2*a*d*N^2*Z^2+d^2*q^2*Z^4", "homogeneous J1 torsor moved")
    require(torsor["twisting_squareclass"] == "d=f1", "J1 twisting squareclass moved")
    require(torsor["splitting_field"] == "Kgeom(sqrt(f1))", "J1 torsor splitting field moved")
    require(torsor["bisection_branch_points"] == ["r1=1+sqrt(2)", "r4=1-sqrt(2)"], "J1 bisection branch points moved")
    require(torsor["bisection_genus"] == 0, "J1 bisection genus moved")
    require(torsor["jacobian"] == "E: y^2=x*(x^2+a*x+b)", "J1 torsor Jacobian moved")
    require("direct Galois descent of E_L1" in torsor["jacobian_reason"], "Jacobian is not source-bound to direct translation descent")
    require("not the Tr-isogenous comparison curve" in torsor["jacobian_reason"], "isogeny-cover firewall missing")

    ind = v73["independence_from_j2"]
    require(ind["j2_squareclass_reused"] is False, "J2 squareclass reused")
    require(ind["j2_torsor_relabelled_as_j1"] is False, "J2 torsor relabelled")
    require(ind["j2_minimum_norm_8_reused"] is False, "J2 minimum norm reused")
    require(ind["j2_marked_coordinate_u1_reused"] is False, "J2 marked coordinate reused")

    nxt = v73["next_kernel_contract"]
    require(nxt["allowed_minimum_norm_outcomes"] == [4, 12], "J1 target outcomes moved")
    require(nxt["minimum_norm_materialized"] is False, "D2.2 prematurely materialized")
    require(nxt["marked_kc_coordinate_selected"] is False, "marked coordinate prematurely selected")

    fw = v73["credit_firewall"]
    require(fw["D2_1_closed"] is True, "D2.1 not closed")
    require(fw["D2_2_closed"] is False, "D2.2 prematurely closed")
    require(fw["j1_translation_torsor_materialized"] is True, "J1 torsor flag missing")
    for key in [
        "j1_twisted_kernel_minimum_norm_materialized",
        "j1_marked_kc_coordinate_selected",
        "identity_vs_shear_selected",
        "e3_kummer_column_materialized",
        "e3_mask20_membership_computed",
        "genuine_full_surface_H2_mu2_lift_for_e3",
        "stage33_12_closed",
        "stage33_13_released",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_credit",
        "merge_allowed",
    ]:
        require(fw[key] is False, f"firewall leaked: {key}")

    print(json.dumps({
        "success": True,
        "canonical_sha256": EXPECTED_V73,
        "j1_translation_torsor_materialized": True,
        "jacobian": torsor["jacobian"],
        "splitting_field": torsor["splitting_field"],
        "bisection_branch_points": torsor["bisection_branch_points"],
        "next_exact_leaf": nxt["next_exact_leaf"],
        "minimum_norm_materialized": False,
        "marked_kc_coordinate_selected": False,
        "merge_allowed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
