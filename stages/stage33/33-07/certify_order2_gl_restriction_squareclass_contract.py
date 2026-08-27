#!/usr/bin/env python3
"""Freeze the exact squareclass contract for Stage-A absolute localization.

Let Q=F2^26 be the retained order-two boundary source and
K=Br(Sbar)[2]=F2^14.  Over L=Q(i,sqrt(2)) both Q and K have trivial G_L action.
Hence extensions of Q by K over G_L are classified by

  H^1(G_L, Hom_F2(Q,K))
    = Hom_cont(G_L,F2) tensor_F2 Hom_F2(Q,K)
    = (L*/L*2) tensor_F2 Hom_F2(Q,K),

using Kummer theory (mu_2 subset L).  Since dim Hom(Q,K)=26*14=364, the
restriction of the real geometric lift torsor is exactly a 14x26 matrix of
L-squareclasses.  This is a shape statement, not a finite-dimensionality claim:
L*/L*2 itself is not replaced by a guessed finite basis.

For an absolute G_Q extension the resulting tensor must lie in the diagonal
V4-fixed part and has zero inflation-restriction transgression automatically.
The actual 364 squareclasses remain project data.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ABSREC = HERE / "order2-absolute-localization-receiver.json"
FINREC = HERE / "order2-localization-receiver.json"
BR2 = HERE / "proper-brauer2-from-discriminant.json"
OUT = HERE / "order2-gl-restriction-squareclass-contract.json"
SDIM, KDIM = 26, 14


def die(msg):
    raise SystemExit(msg)


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, label):
    x = json.loads(path.read_text(encoding="utf-8"))
    h = x.get("canonical_sha256")
    if not h:
        die(f"{label}: missing canonical hash")
    body = dict(x)
    body.pop("canonical_sha256")
    got = canonical_sha256(body)
    if got != h:
        die(f"{label}: canonical hash mismatch {h} != {got}")
    return x


absrec = load_locked(ABSREC, "absolute localization receiver")
finrec = load_locked(FINREC, "finite localization receiver")
br2 = load_locked(BR2, "proper Br2")
if absrec.get("schema") != "STAGE33_07_ORDER2_ABSOLUTE_LOCALIZATION_RECEIVER_V1":
    die("absolute receiver schema regression")
if finrec.get("finite_source_order2_dimension_f2") != SDIM:
    die("source dimension regression")
if finrec.get("finite_receiver_module_dimension_f2") != KDIM:
    die("coefficient dimension regression")
if br2.get("proper_geometric_Br2_dimension_f2") != KDIM:
    die("proper Br2 dimension regression")
if absrec["coefficient"]["G_L_action"] != "TRIVIAL":
    die("G_L coefficient action is no longer trivial")
if absrec["source"]["dimension_f2"] != SDIM:
    die("absolute source dimension regression")

source_names = [x["name"] for x in finrec["finite_source_basis"]]
if len(source_names) != SDIM or len(set(source_names)) != SDIM:
    die("source basis naming regression")

homdim = SDIM * KDIM
cert = {
    "schema": "STAGE33_07_ORDER2_GL_RESTRICTION_SQUARECLASS_CONTRACT_V1",
    "source_locks": {
        "absolute_localization_receiver_sha256": absrec["canonical_sha256"],
        "finite_localization_receiver_sha256": finrec["canonical_sha256"],
        "proper_brauer2_sha256": br2["canonical_sha256"],
    },
    "field": "L=Q(i,sqrt(2))",
    "galois_quotient": "Gal(L/Q)=V4=<cc,ct>",
    "source": {
        "module": "Q=F2^26",
        "dimension_f2": SDIM,
        "basis_names": source_names,
        "G_L_action": "TRIVIAL",
        "V4_action": "TRIVIAL because Q consists of G_Q-invariant residue directions",
    },
    "coefficient": {
        "module": "K=Br(Sbar)[2]",
        "dimension_f2": KDIM,
        "G_L_action": "TRIVIAL",
        "V4_action_source": "proper-brauer2-from-discriminant.json cc/ct matrices",
    },
    "extension_classification_over_GL": {
        "Hom_Q_K_dimension_f2": homdim,
        "Ext1": "Ext^1_{F2[G_L]}(Q,K) ~= H^1(G_L,Hom_F2(Q,K))",
        "trivial_action_reduction": "H^1(G_L,Hom(Q,K)) ~= Hom_cont(G_L,F2) tensor_F2 Hom(Q,K)",
        "kummer": "Hom_cont(G_L,F2) ~= H^1(L,Z/2) ~= L*/L*2",
        "final_form": "(L*/L*2) tensor_F2 F2^364",
        "project_data_shape": [KDIM, SDIM],
        "project_squareclass_entries": homdim,
        "interpretation": "one L-squareclass for each coefficient-basis/source-basis pair",
        "L_squareclass_group_finite_dimensional_claimed": False,
        "364_is_dimension_of_full_GL_extension_space": False,
    },
    "absolute_GQ_compatibility": {
        "required_V4_condition": "the 14x26 squareclass tensor is fixed by the diagonal V4 action on L*/L*2 and K; source Q is trivial",
        "required_transgression_condition": "its class has zero transgression to H^2(V4,Hom(Q,K)); automatic for data actually restricted from a G_Q extension",
        "V4_fixedness_of_project_tensor_computed": False,
        "project_transgression_computed": False,
    },
    "finite_span_execution_contract": {
        "purpose": "once the finitely many project squareclasses are explicit, close their V4 orbit span X inside L*/L*2 and compute Stage-A exactly",
        "required_input": {
            "squareclass_span_dimension_f2": "r",
            "squareclass_basis_labels": "r independent labels representing classes in L*/L*2",
            "squareclass_cc_action_f2": "r x r row-action matrix",
            "squareclass_ct_action_f2": "r x r row-action matrix",
            "restriction_source_tensors_f2": "26 tensors of shape 14 x r",
        },
        "consumer": "materialize_order2_gl_restriction_kernel_from_span.py",
        "consumer_outputs": [
            "diagonal V4-invariance check for every source image",
            "Stage-A restriction rank over F2",
            "kernel dimension and deterministic F2 basis in the 26 source coordinates",
        ],
    },
    "project_status": {
        "unknown_absolute_action_on_K_removed": True,
        "unknown_GL_restriction_data_reduced_to_explicit_squareclass_tensor_shape": True,
        "project_14x26_squareclass_matrix_materialized": False,
        "project_364_squareclass_entries_computed": False,
        "Stage_A_restriction_rank_computed": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
        "stage33_progress": "6/11",
    },
    "new_smallest_exact_kernel": "R33-BR2A-EXPLICIT-14x26-L-SQUARECLASS-RESTRICTION-TENSOR",
    "next_exact_leaf": "L33-07-MATERIALIZE-14x26-L-SQUARECLASSES-FROM-REAL-GEOMETRIC-GERSTEN-LIFTS",
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "source_dimension_f2": SDIM,
    "coefficient_dimension_f2": KDIM,
    "Hom_Q_K_dimension_f2": homdim,
    "project_squareclass_matrix_shape": [KDIM, SDIM],
    "project_squareclass_entries": homdim,
    "L_squareclass_group_finite_dimensional_claimed": False,
    "project_squareclasses_computed": False,
    "new_smallest_exact_kernel": cert["new_smallest_exact_kernel"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
