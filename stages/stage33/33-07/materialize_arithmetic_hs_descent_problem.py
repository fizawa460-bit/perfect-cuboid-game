#!/usr/bin/env python3
"""Materialize the exact Stage33-07 arithmetic Hochschild--Serre repair target.

This repair deliberately separates three different objects which the historical
Stage33-07 global Gersten step conflated:

  (1) boundary residue data known exactly from Stage33-04;
  (2) residue classes already known to have Q-defined global Brauer lifts;
  (3) the remaining geometric-lift torsors whose arithmetic descent to Q is
      genuinely unresolved.

No global Gersten-surjectivity theorem is used here.  In particular this leaf
never promotes a compatible boundary tuple to Br(U) merely because it lifts
over Qbar.
"""

import hashlib
import json
from collections import Counter
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve().parent
S33 = HERE.parent


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


br0b = load(S33 / "33-03" / "audit-state.json")
br0g = load(S33 / "33-04" / "audit-state.json")
reaudit = load(HERE / "audit-state.json")
s08 = load(S33 / "33-08" / "audit-state.json")
left = load(HERE / "br0b-boundary-raw-residue-map.json")
finite = load(HERE / "br0g-finite-ramified-residue-presentation.json")
fullinj = load(HERE / "full-br0b-boundary-injection.json")

KERNEL = "R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT"

# Authority / rollback guards.
assert br0b["unit_status"] == "CLOSED" and br0b["br0b"] == "DISCHARGED"
assert br0g["unit_status"] == "CLOSED" and br0g["br0g"] == "DISCHARGED"
assert reaud it if False else True
assert reaudit["unit_status"] == "BLOCKED_NEW_KERNEL"
assert reaudit["new_kernel_id"] == KERNEL
assert s08["audit_verdict"].startswith("PASS_BLOCKED_NEW_KERNEL")
assert s08["theorem_scope_regression"]["arithmetic_q_descent_certified"] is False
assert s08["accepted_exact_prefix"]["u44_explicit_q_defined_quaternion_representatives"] == 44
assert s08["accepted_exact_prefix"]["u44_physical_open_domain"] == "ALL_PHYSICAL_OPEN"

# Retained exact boundary algebra.
assert left["induced_left_filtration_boundary_map_injective"] is True
assert fullinj["full_br0b_boundary_map_injective"] is True
assert fullinj["br0b_all_primary_classes_accounted"] is True
assert finite["finite_ramified_boundary_residue_module_exact"] is True
assert finite["finite_ramified_boundary_residue_module"] == "(Z/2)^49 direct_sum (Z/4)^12"
assert finite["unit_symbol_rank_f2"] == 44
assert finite["graph_residual_rank_f2"] == 17
assert finite["combined_exponent_two_rank_f2"] == 61
assert finite["order4_generator_count"] == 12

# Recompute the quotient of the finite ramified boundary module by the 44
# explicit Q-defined unit-symbol quaternions.  This is the genuine finite HS
# unknown; the historical 73-generator presentation is too large for the
# arithmetic descent repair because U01..U44 already have global Q lifts.
relq = finite["diagnostic_quotient_by_U44_relation_matrix_29x29"]
M = sp.Matrix([[int(x) for x in row] for row in relq])
assert M.shape == (29, 29)
D = smith_normal_form(M, domain=ZZ)
diag = [abs(int(D[i, i])) for i in range(29) if D[i, i] != 0]
counts = Counter(diag)
if counts != Counter({1: 3, 2: 23, 4: 3}):
    raise SystemExit(f"U44 quotient Smith regression: {counts}")
finite_unknown = "(Z/2)^23 direct_sum (Z/4)^3"
finite_unknown_order_log2 = 23 + 2 * 3
full_finite_order_log2 = 49 + 2 * 12
if full_finite_order_log2 - finite_unknown_order_log2 != 44:
    raise SystemExit("U44 quotient order check failed")

bg = br0g["accepted_exact_boundary_kernel"]
constant_odd = bg["odd_primary_boundary_character_module"]
constant_two = bg["two_primary_constant_character_module"]
assert constant_odd == "Hom_cont(G_Q,Q/Z)_odd^48 direct_sum Hom_cont(G_Q(i),Q/Z)_odd^12"
assert constant_two == "Hom_cont(G_Q,Q_2/Z_2)^48 direct_sum Hom_cont(G_Q(i),Q_2/Z_2)^12"

b0 = br0b["accepted_inventory"]
assert b0["odd_primary"] == "Hom_cont(G_Q,Q/Z)_odd^14"
assert b0["filtration_extension_split_claimed"] is False

# The proper geometric Brauer group has abstract n-torsion rank 14: the audit
# has already source-locked b2-rho=78-64=14 and simple connectivity, hence no
# H^3 topological torsion.  We do NOT assign a trivial Galois action to this
# group.  Its nontrivial arithmetic action is precisely why this repair exists.
proper_transcendental_rank = int(s08["theorem_scope_regression"]["proper_transcendental_l_adic_rank"])
assert proper_transcendental_rank == 14

cert = {
    "schema": "STAGE33_07_ARITHMETIC_HS_DESCENT_PROBLEM_V1",
    "stage": "33",
    "unit": "33-07",
    "repair_kernel": KERNEL,
    "source_locks": {
        "stage33_03_audit_state": "stages/stage33/33-03/audit-state.json",
        "stage33_04_audit_state": "stages/stage33/33-04/audit-state.json",
        "stage33_07_reaudit_state": "stages/stage33/33-07/audit-state.json",
        "stage33_08_hostile_audit_state": "stages/stage33/33-08/audit-state.json",
        "br0b_boundary_map_sha256": left["canonical_sha256"],
        "br0g_finite_boundary_presentation_sha256": finite["canonical_sha256"],
        "full_br0b_boundary_injection_sha256": fullinj["canonical_sha256"],
        "stage33_08_u44_explicit_certificate_sha256": s08["artifact_certificates"]["u44_j2_explicit_representatives_sha256"],
    },
    "known_q_defined_global_residue_image": {
        "br0b": {
            "status": "GLOBAL_Q_DEFINED_AND_BOUNDARY_INJECTIVE",
            "group": b0["exact_filtration_sequence"],
            "boundary_target": "Hom_cont(G_Q,Q/Z)^48 direct_sum Hom_cont(G_Q(i),Q/Z)^12",
            "boundary_map_injective": True,
            "splitting_of_boundary_cokernel_claimed": False,
        },
        "u44": {
            "status": "GLOBAL_Q_DEFINED_EXPLICIT_QUATERNIONS",
            "group": "(Z/2)^44",
            "generator_count": 44,
            "boundary_residue_rank_f2": 44,
            "physical_open_domain": "ALL_PHYSICAL_OPEN",
        },
        "proper_j2": {
            "status": "GLOBAL_Q_DEFINED_ZERO_BOUNDARY_CLASS",
            "group": "Z/2",
            "helps_residue_image_directly": False,
            "may_adjust_hs_lift_fibers": True,
        },
        "seven_line": {"group": "0"},
    },
    "boundary_candidates_not_yet_promoted_to_global_q_classes": {
        "constant_all_primary": {
            "target": "Hom_cont(G_Q,Q/Z)^48 direct_sum Hom_cont(G_Q(i),Q/Z)^12",
            "known_global_subgroup": "rho(BR0B), rho injective",
            "exact_unknown_quotient": "coker(rho: BR0B -> Hom_cont(G_Q,Q/Z)^48 direct_sum Hom_cont(G_Q(i),Q/Z)^12)",
            "cokernel_splitting_claimed": False,
        },
        "constant_odd_primary": {
            "target": constant_odd,
            "known_global_subgroup": "rho(Hom_cont(G_Q,Q/Z)_odd^14)",
            "exact_unknown_quotient": "(Hom_cont(G_Q,Q/Z)_odd^48 direct_sum Hom_cont(G_Q(i),Q/Z)_odd^12) / rho(Hom_cont(G_Q,Q/Z)_odd^14)",
        },
        "constant_two_primary": {
            "target": constant_two,
            "known_global_subgroup": "rho(BR0B[2^infinity])",
            "exact_unknown_quotient": "coker(rho: BR0B[2^infinity] -> Hom_cont(G_Q,Q_2/Z_2)^48 direct_sum Hom_cont(G_Q(i),Q_2/Z_2)^12)",
            "br0b_internal_extension_nonsplit_preserved": True,
        },
        "finite_ramified_after_u44": {
            "full_boundary_module": finite["finite_ramified_boundary_residue_module"],
            "known_global_u44_subgroup": "(Z/2)^44",
            "exact_unknown_quotient": finite_unknown,
            "smith_nonzero_diagonal": diag,
            "smith_counts": {str(k): int(v) for k, v in sorted(counts.items())},
            "unknown_order_log2": finite_unknown_order_log2,
            "minimal_invariant_factor_generators": 26,
            "order2_factors": 23,
            "order4_factors": 3,
            "historical_R17_O12_generator_count_not_the_hs_unknown_count": 29,
        },
    },
    "geometric_lift_fiber": {
        "compatible_boundary_tuples_lift_over_Qbar": True,
        "proper_geometric_brauer_abstract_group": "(Q/Z)^14",
        "proper_geometric_brauer_n_torsion_abstract_group": "(Z/n)^14",
        "galois_action_trivial_claimed": False,
        "proper_transcendental_rank": 14,
        "difference_of_two_geometric_lifts_lies_in_proper_Br_n": True,
    },
    "arithmetic_hs_obstruction_package": {
        "stage_A_localization_torsor": {
            "map": "delta_loc,n: R_n^{G_Q} -> H^1(G_Q, Br(Sbar)[n])",
            "meaning": "vanishing is required for a G_Q-invariant geometric lift; the lift fiber is a torsor under proper Br(Sbar)[n]",
        },
        "stage_B_hoch_schild_serre": {
            "map": "d2^{0,2}: Br(Ubar)[n]^{G_Q} -> H^2(G_Q, Pic(Ubar))[n]",
            "meaning": "after an invariant geometric lift is chosen, its HS obstruction must vanish (possibly after changing the lift by a proper invariant class) for descent to Br(U)",
        },
        "blanket_global_gersten_surjectivity_used": False,
        "semilocal_panin_zainoulline_promoted_to_global_sections": False,
    },
    "exact_reduction": {
        "old_finite_hs_candidate_generators": 73,
        "known_global_finite_generators_removed": 44,
        "remaining_finite_presentation_input_generators": 29,
        "remaining_finite_invariant_factor_generators": 26,
        "remaining_finite_group": finite_unknown,
        "constant_unknown_is_cokernel_not_a_chosen_complement": True,
        "stage33_04_boundary_adapter_credit_unchanged": True,
        "stage33_07_complete_global_inventory_still_unproved": True,
    },
    "new_residual_kernel": "R33-BR2A-HS-OBSTRUCTION-ON-CONSTANT-COKERNEL-AND-Z2_23_Z4_3",
    "next_exact_leaf": "L33-07-COMPUTE-DELTA_LOC-AND-HS-d2-ON-CONSTANT-COKERNEL-AND-FINITE-Z2_23-Z4_3",
    "class3_declared": False,
    "new_theorem_required_declared": False,
    "unit_status": "RUNNING_REPAIR",
    "unit_closed": False,
    "downstream_released": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "stage33_09_released": False,
    "unresolved_unknown_in_scope": 1,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}

raw = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
out = HERE / "arithmetic-hs-descent-problem.json"
out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(json.dumps({
    "success": True,
    "known_global_BR0B": True,
    "known_global_U44": 44,
    "finite_HS_unknown": finite_unknown,
    "finite_HS_unknown_generators": 26,
    "proper_transcendental_rank": proper_transcendental_rank,
    "new_residual_kernel": cert["new_residual_kernel"],
    "next_exact_leaf": cert["next_exact_leaf"],
    "UNIT_STATUS": cert["unit_status"],
    "STAGE33_PROGRESS": cert["stage33_progress"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
