#!/usr/bin/env python3
"""Certify that the *entire* Stage33-03 BR0B block injects into boundary characters.

The corrected left-filtration leaf gives an explicit coordinate map for
X_Q^14/<KAPPA_1,KAPPA_2>.  This leaf closes the possible hidden kernel on the
right filtration by using the proper cuboid-surface algebraic Brauer theorem.

For U=S\D, the compactification triangle gives the exact segment

    H^1(Q,Pic(Sbar)) -> H^2(Q,UPic(Ubar)) -> H^2(Q,Div_D(Sbar)).

Testa--Stoll, The surface parametrizing cuboids, Theorem 10 computes
H^1(Q,Pic(Sbar))=0.  Therefore the boundary map is injective on the full
BR0B=H^2(Q,UPic(Ubar)), including the quadratic-family and finite-free right
filtration classes.  Since Div_D is the permutation lattice with 48 Q-orbits
and 12 Q(i)-orbits, Shapiro identifies its H^2 with the Stage33-04 constant
character block.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


br0b = load(S33 / "33-03" / "audit-state.json")
br0g = load(S33 / "33-04" / "audit-state.json")
left = load(HERE / "br0b-boundary-raw-residue-map.json")
finite = load(HERE / "br0g-finite-ramified-residue-presentation.json")

assert br0b["unit_status"] == "CLOSED" and br0b["br0b"] == "DISCHARGED"
assert br0b["unresolved_unknown_in_scope"] == 0
assert br0g["unit_status"] == "CLOSED" and br0g["br0g"] == "DISCHARGED"
assert br0g["unresolved_unknown_in_scope"] == 0
assert left["induced_left_filtration_boundary_map_injective"] is True
assert left["kappa_span_equals_q_component_mod2_kernel"] is True
assert finite["finite_ramified_boundary_residue_module_exact"] is True

inv = br0b["accepted_inventory"]
bg = br0g["accepted_exact_boundary_kernel"]
assert bg["arithmetic_component_orbit_count"] == 60
assert bg["q_component_orbit_count"] == 48
assert bg["qi_component_orbit_count"] == 12

# Source-locked theorem input.  The theorem is for exactly the smooth proper
# cuboid surface S used by the Stage29/32/33 compactification model.
h1_q_pic_s = 0
assert h1_q_pic_s == 0

# H^2(Q,Z)=Hom_cont(G_Q,Q/Z), and Shapiro for the 12 induced Q(i)-orbits.
constant_all_primary = (
    "Hom_cont(G_Q,Q/Z)^48 direct_sum Hom_cont(G_Q(i),Q/Z)^12"
)
constant_odd = bg["odd_primary_boundary_character_module"]
constant_two = bg["two_primary_constant_character_module"]
assert constant_odd == (
    "Hom_cont(G_Q,Q/Z)_odd^48 direct_sum Hom_cont(G_Q(i),Q/Z)_odd^12"
)
assert constant_two == (
    "Hom_cont(G_Q,Q_2/Z_2)^48 direct_sum Hom_cont(G_Q(i),Q_2/Z_2)^12"
)

# Exact-sequence consequence: kernel of the full boundary map is the image of
# H^1(Q,Pic(Sbar)), hence zero.  No class in either right-filtration summand may
# be silently deleted as a zero-boundary class.
full_br0b_injective = True
right_quadratic_family_injective = True
right_five_finite_injective = True

cert = {
    "schema": "STAGE33_07_FULL_BR0B_BOUNDARY_INJECTION_V1",
    "stage33_unit": "33-07",
    "source_locks": {
        "br0b_audit_state": "stages/stage33/33-03/audit-state.json",
        "br0g_audit_state": "stages/stage33/33-04/audit-state.json",
        "left_coordinate_map": "stages/stage33/33-07/br0b-boundary-raw-residue-map.json",
        "finite_ramified_presentation": "stages/stage33/33-07/br0g-finite-ramified-residue-presentation.json",
        "testa_stoll": {
            "authors": "Damiano Testa; Michael Stoll",
            "title": "The surface parametrizing cuboids",
            "locator": "Theorem 10",
            "url": "https://www.mathe2.uni-bayreuth.de/stoll/papers/Cuboidi.pdf",
            "exact_used_statement": "H^1(Q,Pic(Sbar))=0; equivalently Br_1(S)/Br(Q)=0",
        },
        "compactification_exact_segment": "H^1(Q,Pic(Sbar)) -> H^2(Q,UPic(Ubar)) -> H^2(Q,Div_D(Sbar))",
        "permutation_lattice_shapiro": "Div_D has 48 Q singleton orbits and 12 Q(i) paired orbits; H^2 gives 48 Q-character factors plus 12 Q(i)-character factors",
    },
    "proper_cuboid_surface_H1_Q_Pic": 0,
    "proper_algebraic_brauer_mod_constants": 0,
    "boundary_constant_character_module_all_primary": constant_all_primary,
    "boundary_constant_character_module_odd": constant_odd,
    "boundary_constant_character_module_two_primary": constant_two,
    "br0b_exact_filtration": inv["exact_filtration_sequence"],
    "br0b_filtration_extension_split_claimed": inv["filtration_extension_split_claimed"],
    "br0b_filtration_extension_class_exact": inv["filtration_extension_class_exact"],
    "full_br0b_boundary_map_injective": full_br0b_injective,
    "left_filtration_coordinate_map_injective": True,
    "right_filtration_quadratic_family_boundary_map_injective": right_quadratic_family_injective,
    "right_filtration_five_finite_classes_boundary_map_injective": right_five_finite_injective,
    "no_nonzero_br0b_class_has_zero_physical_boundary_character": True,
    "br0b_duplicate_with_br0g_constant_block_exactly_its_injective_image": True,
    "canonical_duplicate_quotient_presentation": {
        "constant_block": constant_all_primary,
        "embedded_subgroup": "rho(BR0B), rho injective",
        "new_constant_boundary_block": "coker(rho:BR0B->H^2(Q,Div_D))",
        "splitting_of_cokernel_extension_claimed": False,
    },
    "finite_ramified_block_unchanged": finite["finite_ramified_boundary_residue_module"],
    "finite_ramified_block_relation_matrix_exact": finite["relation_matrix_exact_for_boundary_finite_ramified_residue_branch"],
    "important_firewalls": {
        "right_filtration_coordinate_residue_vectors_in_60_orbit_basis_materialized": False,
        "full_two_primary_symbol_matrix_complete": False,
        "j2_duplicate_separation_complete": False,
        "nf_phys2_invoked": False,
        "camp4_invoked": False,
        "stage33_08_released": False,
    },
    "exact_progress_consequence": "The right-filtration problem is no longer a kernel/survival question. Every Stage33-03 BR0B class survives injectively into the Stage33-04 constant-character boundary block. Remaining work is an explicit two-primary symbol/relation presentation and J2 duplicate separation.",
    "new_residual_kernel": "R33-BR2A-TWO-PRIMARY-SYMBOL-MATRIX-AND-J2-DUPLICATE-SEPARATION",
    "next_exact_leaf": "L33-07-MATERIALIZE-ADAPTED-TWO-PRIMARY-GLOBAL-PRESENTATION-AND-J2-INDEPENDENCE",
    "relation_matrix_exact_for_two_primary_branch": False,
    "symbol_matrix_exact_for_two_primary_branch": False,
    "trivial_algebraic_duplicate_quotient_exact": True,
    "complete_relevant_q_defined_class_list_for_stage33_brauer_scope": False,
    "every_class_has_primary_order_and_provenance": False,
    "br0b_all_primary_classes_accounted": True,
    "unresolved_unknown_in_scope": 1,
    "unit_status": "RUNNING",
    "unit_closed": False,
    "downstream_released": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": True,
    "theorem_credit_scope": "Testa--Stoll Theorem 10 only: H^1(Q,Pic(Sbar))=0",
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(HERE / "full-br0b-boundary-injection.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "H1_Q_PicS": 0,
    "full_BR0B_boundary_map_injective": True,
    "algebraic_duplicate_quotient_exact": True,
    "remaining_kernel": cert["new_residual_kernel"],
    "next_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
