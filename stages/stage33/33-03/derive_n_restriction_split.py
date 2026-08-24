#!/usr/bin/env python3
"""Reduce the absolute two-primary d2_11 wall by restriction to N=Gal(Qbar/L).

Here L=Q(i,sqrt(2)) is the source-locked splitting field for the geometric
boundary/Picard action, so N acts trivially on the exact two-term complex
C=[Div_D -> Pic(Sbar)].  The integral Smith data then split C over N into
independent kernel, torsion-resolution, free-cokernel, and acyclic summands.
Consequently the Postnikov k-invariant coupling H^1(C)=Pic(Ubar) to
H^0(C)=U_D restricts to zero on N.  Naturality of the hypercohomology edge
transgression therefore forces every absolute d2_11 image to lie in the
restriction kernel in H^3(Q,U_D).  The unresolved N-character source is also
exponent two, since only the fixed (Z/2)^2 torsion of Pic(Ubar) contributes to
H^1(N,Pic(Ubar)).

This is a structural reduction only.  It does not assert that the remaining
absolute N-character transgression vanishes.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
upic = json.loads((ROOT / "upic-v4-action-certificate.json").read_text())
picu = json.loads((ROOT / "picu-integral-action.json").read_text())
finite = json.loads((ROOT / "finite-transgression-ranks.json").read_text())
d201 = json.loads((ROOT / "d2-01-image.json").read_text())

complex_shape = upic["complex"]
if complex_shape != {
    "div_boundary_rank": 72,
    "picard_rank": 64,
    "unit_lattice_rank": 14,
    "pic_u_free_rank": 6,
    "pic_u_torsion": [2, 2],
}:
    raise SystemExit(f"unexpected exact complex shape: {complex_shape}")
if picu["pic_u_group"] != {"free_rank": 6, "torsion": [2, 2]}:
    raise SystemExit("Pic(Ubar) structure regression")
if picu["torsion_joint_fixed_dimension_f2"] != 2:
    raise SystemExit("full Pic(Ubar)[2] is no longer V4-fixed")
if finite["rank_d2_01"] != 2 or finite["rank_d2_11"] != 2:
    raise SystemExit("finite transgression rank lock regression")
if not d201["finite_d2_01_image_exact"] or d201["image_f2_rank"] != 2:
    raise SystemExit("exact finite d2_01 image certificate missing")

# The exact rank/cokernel data determine the Smith normal form of
# Div_D -> Pic(Sbar): rank 58 with coker Z^6 + (Z/2)^2, hence 56 unit
# elementary divisors and two elementary divisors equal to 2.  The remaining
# 14 divisor coordinates are the kernel U_D.
image_rank = complex_shape["div_boundary_rank"] - complex_shape["unit_lattice_rank"]
if image_rank != 58:
    raise SystemExit("boundary-to-Picard image rank regression")
smith_nonzero = [1] * 56 + [2, 2]
if len(smith_nonzero) != image_rank:
    raise SystemExit("Smith shape arithmetic regression")

# N is the kernel of the source-locked quotient G_Q -> Gal(L/Q)=V4.  Since the
# boundary and Picard actions used throughout this leaf are defined over L, N
# acts trivially on both terms of C.  Any integral Smith basis change is thus
# N-equivariant.  In those coordinates the restricted complex is the direct
# sum below, so there is no derived coupling between the rank-14 H^0 summand
# and H^1=Z^6+(Z/2)^2.
restricted_decomposition = {
    "acyclic_identity_summands": 56,
    "torsion_resolution_summands_Z_times2_to_Z": 2,
    "unit_kernel_Z_degree0": 14,
    "free_cokernel_Z_degree1": 6,
}

cert = {
    "schema": "STAGE33_03_ABSOLUTE_N_RESTRICTION_SPLIT_V1",
    "source_locks": {
        "splitting_field": "L=Q(i,sqrt(2))",
        "quotient": "Gal(L/Q)=V4",
        "kernel": "N=Gal(Qbar/L)",
        "upic_v4_action_sha256": upic["canonical_sha256"],
        "picu_integral_action_sha256": picu["canonical_sha256"],
        "finite_transgression_ranks_sha256": finite["canonical_sha256"],
        "d2_01_exact_image_sha256": d201["canonical_sha256"],
    },
    "smith_nonzero_elementary_divisors": smith_nonzero,
    "restricted_complex_N_action": "trivial",
    "restricted_complex_N_equivariant_smith_decomposition": restricted_decomposition,
    "restricted_postnikov_k_invariant_between_PicU_and_unit": 0,
    "restricted_d2_01_on_N": 0,
    "restricted_d2_11_on_N": 0,
    "absolute_d2_11_image_restricts_to_zero_on_N": True,
    "absolute_d2_11_target_reduced_to": "ker(H^3(G_Q,U_D)->H^3(N,U_D))[2]",
    "absolute_N_character_source": (
        "kernel of the inflation-restriction transgression from "
        "Hom_cont(N,(Z/2)^2)^V4 to H^2(V4,Pic(Ubar)), modulo the already-accounted finite inflation part"
    ),
    "absolute_N_character_source_exponent": 2,
    "free_PicU_part_contributes_to_H1_N": False,
    "finite_V4_subproblem_closed": True,
    "remaining_wall_strictly_absolute": True,
    "remaining_wall": "R33-BR0B-ABSOLUTE-N-QUADRATIC-CHARACTER-TRANSGRESSION-IN-KER-RES",
    "next_exact_leaf": "L33-03-N-QUADRATIC-CHARACTER-TRANSGRESSION-IN-KER-RES",
    "br0b_all_primary_classes_accounted": False,
    "unit_closed": False,
    "new_theorem_required": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "absolute-n-restriction-split.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "restricted_postnikov_k_invariant": 0,
    "absolute_d2_11_target_reduced_to": cert["absolute_d2_11_target_reduced_to"],
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
