#!/usr/bin/env python3
"""Materialize the exact Stage-B adjustment quotient on the full surface.

This is a contract certificate, not an HS-value computation.  Once the
Stage-A localization obstruction of a boundary direction vanishes, its
invariant geometric lifts form a torsor under

    P = Br(Sbar)[2]^{G_Q}.

Consequently the lift-independent Stage-B obstruction is a coset in the
cokernel of d2 restricted to P, rather than the d2 value of an arbitrary
chosen lift.  The certificate also prevents the audited K_c class q1 from
being silently promoted to the full cuboid surface S without a named
pullback/glue adapter.
"""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
BR2 = STAGE33 / "33-07" / "proper-brauer2-from-discriminant.json"
GLUE = STAGE33 / "33-07" / "coordinate-k3-transcendental-glue-index.json"
K3_AUDIT = STAGE33 / "33-05" / "audit-state.json"
H10 = STAGE33 / "33-10" / "handoff.json"
SCALARS = HERE / "boundary-function-scalar-descent-certificate.json"
CONTROLLER = STAGE33 / "controller.json"
OUT = HERE / "full-surface-hs-adjustment-contract.json"

EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_GLUE = "0cc5321d02b56cea801b8def71a4c3b0946bd8011d8c30767a9602faba2fa8d8"
EXPECTED_K3_AUDIT_FILE = "e702aff6051e747d0d2f29842c22c2bb8f39f1fdbf025ce2eb9497824917b672"
EXPECTED_H10 = "4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f"
EXPECTED_SCALARS = "e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b"
N = 14


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical source lock moved: {path}")
    return obj


def file_sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rank(rows):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    r = 0
    for c in range(len(a[0]) if a else N):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def fixed_dimension(cc, ct):
    equations = []
    for action in (cc, ct):
        for j in range(N):
            equations.append([action[i][j] ^ int(i == j) for i in range(N)])
    return N - rank(equations)


br2 = load_locked(BR2, EXPECTED_BR2)
glue = load_locked(GLUE, EXPECTED_GLUE)
h10 = load_locked(H10, EXPECTED_H10)
scalars = load_locked(SCALARS, EXPECTED_SCALARS)
k3_audit = json.loads(K3_AUDIT.read_text(encoding="utf-8"))
controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
if file_sha(K3_AUDIT) != EXPECTED_K3_AUDIT_FILE:
    raise SystemExit("Stage33-05 hostile-audit state moved")
if k3_audit["audit_verdict"] != "PASS_AFTER_INDEPENDENT_Q_SURVIVAL_AND_HS_D2_VERIFICATION":
    raise SystemExit("Stage33-05 audit verdict regression")
if not k3_audit["j2_q_descent_certified"] or not k3_audit["q1_hs_d2_nonzero"]:
    raise SystemExit("Stage33-05 J2/q1 interface regression")
if not all(
    controller["stage33_07"][key]
    for key in ("j2_q_defined", "j2_exact_order", "j2_proper_transcendental")
):
    raise SystemExit("authoritative full-surface J2 interface regression")
if h10["status"] != "CLOSED_EXACT":
    raise SystemExit("Stage33-10 is not exact-closed")
if glue["integral_glue"]["actual_glue_subgroup_identified"]:
    raise SystemExit("historical full-surface glue state unexpectedly promoted")
if not scalars["exact_conclusion"]["all_cc_ct_function_level_scalar_ratios_equal_one"]:
    raise SystemExit("boundary scalar adapter regression")

cc = br2["proper_Br2_cc_action_f2"]
ct = br2["proper_Br2_ct_action_f2"]
if fixed_dimension(cc, ct) != 10:
    raise SystemExit("full-surface proper invariant dimension regression")

directions = [f"A2_{i:02d}" for i in range(1, 27)]
certificate = {
    "schema": "STAGE33_12_FULL_SURFACE_HS_ADJUSTMENT_CONTRACT_V1",
    "source_locks": {
        "proper_brauer2_from_discriminant_sha256": EXPECTED_BR2,
        "coordinate_k3_transcendental_glue_sha256": EXPECTED_GLUE,
        "stage33_05_audit_state_file_sha256": EXPECTED_K3_AUDIT_FILE,
        "stage33_10_handoff_sha256": EXPECTED_H10,
        "boundary_function_scalar_descent_sha256": EXPECTED_SCALARS,
    },
    "full_surface_proper_adjustment_module": {
        "module": "P=Br(Sbar)[2]^{G_Q}",
        "dimension_f2": 10,
        "action_source": "source-locked 14-dimensional full-surface proper Br2 module",
        "hs_adjustment_map": "d2_S|P: P -> H^2(G_Q,Pic(Sbar))[2]",
        "map_materialized": False,
        "kernel_contains_q_defined_J2": True,
        "kernel_dimension_lower_bound_f2": 1,
        "kernel_dimension_upper_bound_f2": 10,
    },
    "k3_to_full_surface_firewall": {
        "audited_Kc_invariant_basis": ["J2", "q1"],
        "audited_Kc_d2_kernel_basis": ["J2"],
        "audited_Kc_q1_d2_nonzero": True,
        "J2_full_surface_q_defined_pullback_certified_elsewhere": True,
        "q1_full_surface_nonzero_pullback_certified": False,
        "q1_full_surface_d2_image_generator_promoted": False,
        "reason": "The retained Stage33-05 audit is on K_c; no named exact adapter identifies a nonzero q1 pullback inside the 14-dimensional full-surface module.",
    },
    "finite_stage_B_obstruction": {
        "directions": directions,
        "direction_count": 26,
        "stage_A_localization_zero_exact_audited": 26,
        "boundary_function_scalar_correction_zero_exact": 26,
        "invariant_geometric_lift_fiber": "torsor under P",
        "lift_independent_obstruction_target": "coker(d2_S|P)",
        "obstruction_coset_definition": "omega(r)=[d2(beta)] mod im(d2_S|P), for any invariant geometric lift beta of r",
        "independence_of_beta": "Changing beta by p in P changes d2(beta) by d2_S(p).",
        "global_Q_lift_criterion": "omega(r)=0",
        "obstruction_cosets_materialized": 0,
        "global_Q_lifts_promoted": 0,
    },
    "exact_information_boundary": {
        "literal_d2_zero_of_one_arbitrary_lift_required": False,
        "proper_adjustment_cokernel_is_the_correct_receiver": True,
        "zero_localization_and_zero_boundary_scalar_determine_any_stage_B_coset": False,
        "full_surface_proper_d2_map_or_equivalent_quotient_required": True,
        "one_full_surface_invariant_Kummer_defect_per_generator_or_equivalent_direct_coset_required": True,
    },
    "next_exact_leaf": "MATERIALIZE_FULL_SURFACE_PROPER_KUMMER_D2_ADJUSTMENT_MAP_AND_THE_FIRST_FINITE_OBSTRUCTION_COSET",
    "promotion_firewall": {
        "arithmetic_hs_d2_computed": False,
        "global_q_br0g_residue_lifts_complete": False,
        "stage33_12_closed": False,
        "stage33_07_closed": False,
        "stage33_progress": "6/11",
    },
}
certificate["canonical_sha256"] = csha(certificate)
OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "proper_invariant_dimension_f2": 10,
    "finite_obstruction_cosets_materialized": 0,
    "q1_full_surface_promotion": False,
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
