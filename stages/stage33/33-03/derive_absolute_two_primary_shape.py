#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

upic = json.loads((ROOT / "upic-v4-action-certificate.json").read_text())
picu = json.loads((ROOT / "picu-integral-action.json").read_text())
finite = json.loads((ROOT / "finite-v4-hypercohomology.json").read_text())
odd = json.loads((ROOT / "odd-primary-closure.json").read_text())

# Frozen exact inputs from earlier leaves.
assert upic["complex"]["unit_lattice_rank"] == 14
assert upic["unit_v4_rational_character_multiplicities"]["cc+1_ct+1"] == 14
assert all(upic["unit_v4_rational_character_multiplicities"][k] == 0
           for k in ("cc+1_ct-1", "cc-1_ct+1", "cc-1_ct-1"))
assert picu["pic_u_group"]["free_rank"] == 6
assert picu["pic_u_group"]["torsion"] == [2, 2]
assert picu["torsion_joint_fixed_dimension_f2"] == 2
assert upic["pic_u_free_v4_rational_character_multiplicities"]["cc+1_ct+1"] == 0
assert finite["finite_v4_h2_free_rank"] == 0
assert finite["finite_v4_h2_torsion_invariants"] == [2] * 33
assert odd["odd_primary_br0b_parametrically_complete"] is True

# For C=UPic(Ubar) with H^0(C)=U_D and H^1(C)=Pic(Ubar), the hypercohomology
# spectral sequence has, in total degree two, the standard filtration
#
# 0 -> H^2(Q,U_D)/im(d2^{0,1})
#   -> H^2(Q,C)
#   -> ker(d2^{1,1}: H^1(Q,Pic(Ubar))->H^3(Q,U_D)) -> 0.
#
# U_D=Z^14 is a trivial absolute-Galois lattice because the full action on the
# compactification complex factors through V4 and both V4 generators act as 1.
# From 0->Z->Q->Q/Z->0 and divisibility of Q,
# H^2(Q,Z^14)=Hom_cont(G_Q,Q/Z)^14.
#
# Pic(Ubar)^G has no free part (the rational trivial-character multiplicity is
# zero) and its full (Z/2)^2 torsion is fixed. Therefore the source of the
# left transgression is exactly (Z/2)^2. Its image is exponent two and has F2
# rank at most two. Since the k-invariant/action data already descend to V4,
# this transgression factors through the V4 quadratic-character subspace.
# Thus the absolute 2-primary left filtration is necessarily an infinite
# character family; the finite (Z/2)^33 computation cannot be the full answer.

cert = {
    "schema": "STAGE33_03_ABSOLUTE_2PRIMARY_FILTRATION_SHAPE_V1",
    "source_locks": {
        "extended_picard": "Borovoi--van Hamel, J. reine angew. Math. 627 (2009), Prop. 2.19 and UPic definitions",
        "internal_adapter": "stages/stage29/29-02f/open-algebraic-brauer-adapter.md",
        "upic_v4_action_sha256": upic["canonical_sha256"],
        "picu_integral_action_sha256": picu["canonical_sha256"],
        "finite_v4_h2_sha256": finite["canonical_sha256"],
        "odd_primary_sha256": odd["canonical_sha256"],
    },
    "hypercohomology_total_degree_2_filtration": {
        "left": "H^2(Q,U_D)/im(d2_01)",
        "middle": "H^2(Q,UPic(Ubar)) = Br_a(U)",
        "right": "ker(d2_11: H^1(Q,Pic(Ubar))->H^3(Q,U_D))",
    },
    "unit_lattice": {
        "group": "Z^14",
        "absolute_galois_action": "trivial",
        "H2": "Hom_cont(G_Q,Q/Z)^14",
        "H2_2primary": "Hom_cont(G_Q,Q/Z)[2^infinity]^14",
    },
    "pic_u_invariants": {
        "free_invariant_rank": 0,
        "torsion_invariants": [2, 2],
        "group": "(Z/2)^2",
    },
    "left_transgression": {
        "source": "(Z/2)^2",
        "image_exponent_divides": 2,
        "image_f2_rank_upper_bound": 2,
        "image_factors_through_visible_V4": True,
        "visible_V4_quadratic_character_ambient_rank": 28,
        "exact_image_not_yet_materialized": True,
    },
    "absolute_two_primary_left_filtration": "Hom_cont(G_Q,Q/Z)[2^infinity]^14 / im(d2_01)",
    "absolute_two_primary_left_filtration_infinite": True,
    "finite_v4_h2": "(Z/2)^33",
    "finite_v4_h2_is_full_absolute_two_primary": False,
    "all_characters_of_order_greater_than_2_cannot_be_killed_by_d2_01": True,
    "non_V4_quadratic_character_directions_cannot_lie_in_d2_01_image": True,
    "right_filtration_transgression_complete": False,
    "br0b_all_primary_classes_accounted": False,
    "new_residual_kernel": "R33-BR0B-ABSOLUTE-2PRIMARY-PICU-H1-TO-UNIT-H3-TRANSGRESSION",
    "next_exact_leaf": "L33-03-ABSOLUTE-PICU-H1-INFLATION-RESTRICTION-AND-d2_11",
    "new_theorem_required": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "absolute-two-primary-shape.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "absolute_2primary_left_filtration_infinite": True,
    "d2_01_image_rank_upper_bound": 2,
    "finite_v4_h2": "(Z/2)^33",
    "new_residual_kernel": cert["new_residual_kernel"],
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
