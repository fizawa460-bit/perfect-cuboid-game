#!/usr/bin/env python3
"""Materialize the exact two-stage absolute order-two localization receiver.

The coefficient action on K=Br(Sbar)[2] factors through
L=Q(i,sqrt(2))/Q with Gal(L/Q)=V4, but inflation--restriction is not a direct
sum.  Therefore an arbitrary absolute localization class has no canonical
"finite V4 component" before its restriction to G_L is known to vanish.

This certificate freezes the correct decision order for each of the 26
order-two boundary source directions:

  (A) compute res_L(delta) in H^1(G_L,K)^V4
      = ((L*/L*2) tensor_F2 K)^V4 by Kummer;
  (B) only when (A)=0, the class is uniquely inflated from H^1(V4,K), and the
      existing exact ambient-extension adapter computes that 16-dimensional
      finite class;
  (C) the absolute localization obstruction vanishes iff both tests vanish.

No project restriction class or project V4 extension is invented here.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ABS = HERE / "order2-absolute-h1-inflation-restriction.json"
FINITE = HERE / "order2-localization-receiver.json"
OUT = HERE / "order2-absolute-localization-receiver.json"


def die(msg):
    raise SystemExit(msg)


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, label):
    x = json.loads(path.read_text(encoding="utf-8"))
    claimed = x.get("canonical_sha256")
    if not claimed:
        die(f"{label}: missing canonical hash")
    y = dict(x)
    y.pop("canonical_sha256")
    got = canonical_sha256(y)
    if got != claimed:
        die(f"{label}: canonical hash mismatch {claimed} != {got}")
    return x


absrec = load_locked(ABS, "absolute H1 receiver")
finite = load_locked(FINITE, "finite localization receiver")
if absrec.get("schema") != "STAGE33_07_ORDER2_ABSOLUTE_H1_INFLATION_RESTRICTION_V2":
    die("absolute H1 predecessor schema regression")
fac = absrec["coefficient_action_factorization"]
if not fac["absolute_GQ_action_on_K_factors_through_V4"]:
    die("coefficient action factorization predecessor not closed")
if fac["N_action_on_K"] != "TRIVIAL" or fac["kernel"] != "N=G_L=Gal(Qbar/L)":
    die("G_L coefficient action regression")
bar = absrec["bar_complex"]
if (bar["H1_V4_K_dimension_f2"], bar["H2_V4_K_dimension_f2"]) != (16, 22):
    die("finite V4 cohomology regression")
if finite.get("finite_source_order2_dimension_f2") != 26:
    die("finite source dimension regression")
if finite.get("finite_receiver_module_dimension_f2") != 14:
    die("coefficient dimension regression")
if finite.get("finite_receiver_H1_dimension_f2") != 16:
    die("finite H1 receiver dimension regression")

# Kummer is exact here because mu_2={+-1} is contained in L (indeed in Q), and
# G_L acts trivially on the F2 coefficient module K.  Tensor notation records
# the diagonal V4 action: field automorphisms on L*/L*2 and the exact 14D action
# on K already source-locked in the predecessor.
cert = {
    "schema": "STAGE33_07_ORDER2_ABSOLUTE_LOCALIZATION_RECEIVER_V1",
    "source_locks": {
        "absolute_h1_inflation_restriction_sha256": absrec["canonical_sha256"],
        "finite_order2_localization_receiver_sha256": finite["canonical_sha256"],
    },
    "source": {
        "group": "finite order-two subgroup of (Z/2)^23 direct_sum (Z/4)^3 after U44",
        "dimension_f2": 26,
        "basis_contract": "the exact 26 source directions of order2-localization-receiver.json",
    },
    "coefficient": {
        "module": "K=Br(Sbar)[2]",
        "dimension_f2": 14,
        "splitting_field": "L=Q(i,sqrt(2))",
        "G_L_action": "TRIVIAL",
    },
    "stage_A_restriction_receiver": {
        "map": "res_L o delta_loc,2 : F2^26 -> H^1(G_L,K)^V4",
        "kummer_identification": "H^1(G_L,K) ~= (L*/L*2) tensor_F2 K",
        "target": "((L*/L*2) tensor_F2 K)^V4",
        "V4_action": "diagonal: Gal(L/Q) acts on L*/L*2 by field automorphisms and on K by the certified cc/ct matrices",
        "target_finite_dimensional_claimed": False,
        "project_map_computed": False,
        "project_map_zero_claimed": False,
        "meaning": "a nonzero restriction already proves the absolute localization obstruction is nonzero",
    },
    "stage_B_finite_inflation_receiver": {
        "domain_condition": "defined only on source combinations whose Stage-A restriction is zero",
        "exact_reason": "inflation H^1(V4,K)->H^1(G_Q,K) is injective and its image is exactly ker(res_L)",
        "target": "H^1(V4,K)=F2^16",
        "target_dimension_f2": 16,
        "transgression_target": "H^2(V4,K)=F2^22",
        "transgression_target_dimension_f2": 22,
        "adapter": "materialize_order2_localization_extension_from_ambient.py",
        "required_descended_ambient_extension": "0 -> F2^14 -> M -> F2^26 -> 0 after restricting to the Stage-A kernel",
        "project_finite_map_computed": False,
    },
    "absolute_zero_criterion": {
        "statement": "delta_loc,2(x)=0 iff res_L(delta_loc,2(x))=0 and the unique descended V4 class is zero",
        "stage_A_must_precede_stage_B": True,
        "finite_V4_H1_is_not_a_canonical_projection_of_absolute_H1": True,
        "finite_16x26_matrix_for_all_26_sources_before_GL_restriction_is_not_authorized": True,
    },
    "ambiguity_accounting": {
        "abstract_descended_V4_extension_space_dimension_f2": 416,
        "meaning_of_416": "all 16x26 matrices occur at the finite descended layer",
        "416_is_full_absolute_ambiguity_dimension": False,
        "additional_absolute_data": "the 26 G_L-restriction classes in ((L*/L*2) tensor K)^V4, subject to transgression/realizability",
    },
    "project_status": {
        "coefficient_action_factorization_closed": True,
        "G_L_restriction_map_materialized": False,
        "Stage_A_kernel_dimension_f2_known": False,
        "real_descended_V4_extension_materialized": False,
        "absolute_delta_loc_computed": False,
        "HS_d2_after_localization_computed": False,
        "arithmetic_hs_closed": False,
        "stage33_progress": "6/11",
    },
    "next_exact_leaf": "L33-07-COMPUTE-GL-RESTRICTION-OF-26-GEOMETRIC-LIFT-TORSORS-THEN-DESCENDED-V4-DELTA",
    "new_smallest_exact_kernel": "R33-BR2A-GL-RESTRICTION-OF-REAL-GEOMETRIC-LIFT-TORSOR",
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "source_dimension_f2": 26,
    "coefficient_dimension_f2": 14,
    "stage_A_target": cert["stage_A_restriction_receiver"]["target"],
    "stage_B_target_dimension_f2": 16,
    "finite_matrix_before_GL_restriction_authorized": False,
    "absolute_delta_loc_computed": False,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
