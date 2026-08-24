#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

br0b = load(S33 / "33-03" / "audit-state.json")
br0g = load(S33 / "33-04" / "audit-state.json")
k3 = load(S33 / "33-05" / "audit-state.json")
line9 = load(S33 / "33-06" / "audit-state.json")
j2 = load(HERE / "j2-endpoint-q2-pullback.json")
controller = load(S33 / "controller.json")

# Closed prerequisites are authority; do not silently substitute pre-audit states.
assert br0b["unit_status"] == "CLOSED" and br0b["br0b"] == "DISCHARGED"
assert br0b["unresolved_unknown_in_scope"] == 0
assert br0g["unit_status"] == "CLOSED" and br0g["br0g"] == "DISCHARGED"
assert br0g["unresolved_unknown_in_scope"] == 0
assert k3["unit_status"] == "CLOSED" and k3["q_relevant_surviving_dim"] == 1
assert k3["q_surviving_geometric_br2_basis"] == ["J2"]
assert line9["unit_status"] == "CLOSED"
assert line9["exact_zero_survival_certificate"] is True
assert line9["endpoint_relevant_surviving_dimension_f2"] == 0
assert controller["stage33_progress"] == "6/11"
assert controller["stage33_07_released"] is True
assert controller["stage33_07_release_allowed"] is True

# The first Stage33-07 leaf proves the surviving K3 class is still nonzero on
# the full endpoint; it therefore cannot be discarded during integration.
assert j2["endpoint_local_lift_exists"] is True
assert j2["j2_endpoint_pullback_nonzero_certified"] is True
assert j2["corestriction_invariant"] == "1/2"

b0 = br0b["accepted_inventory"]
bg = br0g["accepted_exact_boundary_kernel"]

# Important firewall: the 44-dimensional unit-unit secondary-residue span in
# Stage33-04 is NOT identified here with the Stage33-03 X_Q^14 character-unit
# algebraic family.  They have different constructions.  The exact arithmetic
# residue/lift comparison is the remaining integration map to materialize.
residual = "R33-BR2A-BR0B-BR0G-ARITHMETIC-RESIDUE-OVERLAP-AND-LIFT-PRESENTATION"
next_leaf = "L33-07-MATERIALIZE-BR0B-TO-BOUNDARY-RESIDUE-MAP-AND-FINITE-LIFT-RELATIONS"

cert = {
    "schema": "STAGE33_07_BR2A_INTEGRATION_PREFIX_V1",
    "stage33_unit": "33-07",
    "pr": 1370,
    "source_locks": {
        "closure_contract": "stages/stage33/33-00/unit-closure-contract.md",
        "roadmap": "stages/stage33/ROADMAP.md",
        "br0b_audit_state": "stages/stage33/33-03/audit-state.json",
        "br0g_audit_state": "stages/stage33/33-04/audit-state.json",
        "k3_audit_state": "stages/stage33/33-05/audit-state.json",
        "line9_audit_state": "stages/stage33/33-06/audit-state.json",
        "creutz_viray_ruled_surface": "arXiv:1306.3251; Math. Ann. 362 (2015), Thm 2.5, Prop 3.1, Cor 3.2, Prop 3.4, Thm I, Thm 5.2, Cor 5.4",
        "creutz_viray_hyperelliptic": "arXiv:1403.2924; Manuscripta Math. 147 (2015), Rem 3.1, Prop 3.2, Lem 3.4, Lem 3.5",
    },
    "variable_dictionary": {
        "X_Q": "Hom_cont(G_Q,Q/Z)",
        "U_D": "ker(Div_D(Sbar)->Pic(Sbar)) = O(Ubar)^*/Qbar^*, rank 14",
        "KAPPA_1_KAPPA_2": "exact rank-two d2_01 image relations in X_Q^14 from Stage33-03",
        "BR0B": "Br_a(U)=H^2(G_Q,UPic(Ubar)), imported as the exact nonsplit filtration from Stage33-03",
        "BR0G_boundary": "Q-defined physical-boundary Gersten residue classes from the audited 72-component boundary",
        "J2": "unique Q-descended nonzero K_c geometric Br[2] class from Stage33-05, now certified nonzero after endpoint pullback",
        "line9": "seven-line Ford geometric Br[2] source; exact endpoint pullback zero by Stage33-06",
    },
    "imports": {
        "br0b_all_primary": {
            "unit_lattice": b0["unit_lattice"],
            "pic_u": b0["pic_u"],
            "odd_primary": b0["odd_primary"],
            "exact_filtration_sequence": b0["exact_filtration_sequence"],
            "filtration_extension_split_claimed": b0["filtration_extension_split_claimed"],
            "filtration_extension_class_exact": b0["filtration_extension_class_exact"],
            "quadratic_doubling_map": b0["quadratic_doubling_map"],
            "nonzero_quadratic_lift_orders": b0["nonzero_quadratic_lift_orders"],
            "finite_free_h1_lift_order": b0["finite_free_h1_lift_order"],
        },
        "br0g_relevant": {
            "physical_boundary_component_count": bg["physical_boundary_component_count"],
            "arithmetic_component_orbit_count": bg["arithmetic_component_orbit_count"],
            "odd_primary_boundary_character_module": bg["odd_primary_boundary_character_module"],
            "two_primary_constant_character_module": bg["two_primary_constant_character_module"],
            "two_primary_ramified_crossing_module": bg["two_primary_ramified_crossing_module"],
            "two_primary_unit_symbol_span_rank_f2": bg["two_primary_unit_symbol_span_rank_f2"],
            "order4_double_intersection_unit_symbol_span_rank_f2": bg["order4_double_intersection_unit_symbol_span_rank_f2"],
            "order4_double_image_mod_unit_symbol_span_rank_f2": bg["order4_double_image_mod_unit_symbol_span_rank_f2"],
        },
        "k3_j2": {
            "primary_order": 2,
            "provenance": "BR2_K3",
            "q_defined": True,
            "endpoint_pullback_nonzero": True,
            "q2_witness_invariant": j2["corestriction_invariant"],
            "j2_certificate_sha256": j2["canonical_sha256"],
        },
        "line9": {
            "source_dimension_f2": line9["accepted_exact_result"]["line9_source_h1_dimension_f2"],
            "endpoint_surviving_dimension_f2": line9["accepted_exact_result"]["endpoint_relevant_surviving_dimension_f2"],
            "exact_zero_survival_certificate": line9["accepted_exact_result"]["exact_zero_survival_certificate"],
        },
    },
    "firewalls": {
        "unit_unit_symbol_span_identified_with_br0b_character_unit_family": False,
        "stage33_04_diagnostic_z2_23_plus_z4_3_promoted_to_final_class_group": False,
        "br0b_filtration_split_claimed": False,
        "nf_phys2_invoked": False,
        "camp4_invoked": False,
        "nf_phys2_camp4_invocations_hypothesis_gated": True,
        "stage33_08_released": False,
        "endpoint_credit": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
    "closure_prefix": {
        "br0b_all_primary_classes_imported": True,
        "br0g_relevant_classes_imported": True,
        "relation_matrix_exact_for_two_primary_branch": False,
        "symbol_matrix_exact_for_two_primary_branch": False,
        "theorem_hypotheses_source_locked": True,
        "variable_dictionary_complete": True,
        "trivial_algebraic_duplicate_quotient_exact": False,
        "nf_phys2_camp4_invocations_hypothesis_gated": True,
        "complete_relevant_q_defined_class_list_for_stage33_brauer_scope": False,
        "every_class_has_primary_order_and_provenance": False,
        "br0b_all_primary_classes_accounted": True,
        "br2a": "OPEN",
        "unresolved_unknown_in_scope": 1,
    },
    "accepted_new_fact": {
        "j2_endpoint_pullback_nonzero_certified": True,
        "j2_endpoint_q2_invariant": "1/2",
    },
    "new_residual_kernel": residual,
    "next_exact_leaf": next_leaf,
    "unit_status": "RUNNING",
    "unit_closed": False,
    "downstream_released": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "hostile_audit": "NOT_READY",
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}

canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(HERE / "integration-prefix.json").write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "j2_endpoint_pullback_nonzero": True,
    "br0b_imported": True,
    "br0g_imported": True,
    "line9_survivor_dim": 0,
    "unresolved_unknown_in_scope": 1,
    "new_residual_kernel": residual,
    "next_exact_leaf": next_leaf,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
