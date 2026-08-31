#!/usr/bin/env python3
"""Record the exact ct norm splitting-module checkpoint in controller.json."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
CONTROLLER = S33 / "controller.json"
CERT = S33 / "33-12" / "j2-corrected-ct-norm-splitting-module.json"
EXPECTED_CERT = "b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


cert = json.loads(CERT.read_text(encoding="utf-8"))
body = dict(cert)
claimed = body.pop("canonical_sha256")
assert claimed == EXPECTED_CERT == csha(body)

next_leaf = cert["next_exact_leaf"]
missing = (
    "ACTUAL_CECH_LOCAL_RANK2_LATTICES_AND_OVERLAP_TRANSITIONS_TO_CC_CT_"
    "DETERMINANT_PARITY_AND_MARKED_PIC_MOD2_THEN_HS_D2"
)

c = json.loads(CONTROLLER.read_text(encoding="utf-8"))
c["schema"] = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V32_CT_NORM_SPLITTING_MODULE_AMBIGUITY"
c["status"] = (
    "STAGE33_05_R0_TO_R4_PASS_R5_GEOMETRIC_PASS_CT_NORM_SPLITTING_MODULE_"
    "STANDARD_EVEN_DETERMINANT_AND_PARITY_AMBIGUITY_DONE_ACTUAL_CECH_"
    "LATTICES_PIC_MOD2_AND_HS_D2_OPEN_33_12_BLOCKED_33_13_BLOCKED"
)

h = c["stage33_05_hostile_reopen"]
h.update({
    "ct_norm_generic_rank2_splitting_matrices_materialized": True,
    "ct_norm_normalized_u": "(1-t^2+2*i*t*s+z)/(2*t)",
    "ct_norm_standard_auxiliary_q_cover_determinant": "O(-2,0)",
    "ct_norm_standard_auxiliary_q_cover_determinant_mod2_zero": True,
    "ct_norm_compactification_parity_ambiguity_materialized": True,
    "ct_norm_splitting_module_certificate": "stages/stage33/33-12/j2-corrected-ct-norm-splitting-module.json",
    "ct_norm_splitting_module_canonical_sha256": EXPECTED_CERT,
    "actual_lambda_D_local_rank2_lattices_materialized": False,
    "ct_norm_splitting_determinant_line_bundle_materialized": False,
})

loop = c["loop_guard_policy"]
loop.update({
    "current_stagnation_count": 0,
    "current_stagnation_reset_reason": "CT_NORM_GENERIC_SPLITTING_MATRICES_STANDARD_EVEN_DETERMINANT_AND_EXPLICIT_COMPACTIFICATION_PARITY_AMBIGUITY",
    "active_missing_interface": missing,
    "last_loop_audit_verdict": "POST_R5_CT_NORM_SPLITTING_MODULE_PASS_ACTUAL_CECH_LOCAL_LATTICES_PIC_MOD2_AND_HS_D2_OPEN",
})

child = next(x for x in c["repair_children"] if x["id"] == "33-12")
child.update({
    "loop_stagnation_count": 0,
    "loop_active_missing_interface": missing,
    "loop_new_exact_information": "NORMALIZED_CT_NORM_U;_EXACT_RANK2_SPLITTING_MATRICES;_STANDARD_AUXILIARY_Q_COVER_DETERMINANT_O_MINUS2_MOD2_ZERO;_ELEMENTARY_TRANSFORM_PARITY_AMBIGUITY;_ACTUAL_CECH_LATTICES_OPEN",
    "next_exact_leaf": next_leaf,
    "j2_ct_norm_generic_rank2_splitting_matrices_materialized": True,
    "j2_ct_norm_normalized_u": "(1-t^2+2*i*t*s+z)/(2*t)",
    "j2_ct_norm_standard_auxiliary_q_cover_determinant": "O(-2,0)",
    "j2_ct_norm_standard_auxiliary_q_cover_determinant_mod2_zero": True,
    "j2_ct_norm_compactification_parity_ambiguity_materialized": True,
    "j2_ct_norm_splitting_module_certificate": "stages/stage33/33-12/j2-corrected-ct-norm-splitting-module.json",
    "j2_ct_norm_splitting_module_canonical_sha256": EXPECTED_CERT,
    "j2_actual_lambda_D_local_rank2_lattices_materialized": False,
    "j2_ct_norm_splitting_determinant_line_bundle_materialized": False,
})

c.update({
    "current_item": "Stage33-05_POST_R5_ACTUAL_CECH_LOCAL_LATTICES_MARKED_PIC_MOD2_AND_HS_D2",
    "audit_scope": "STAGE33_05_R0_TO_R4_AND_R5_GEOMETRIC_PASS_CT_NORM_SPLITTING_MODULE_AND_STANDARD_EVEN_DETERMINANT_PASS_ACTUAL_CECH_LATTICES_PIC_MOD2_AND_HS_D2_OPEN_STAGE33_12_EXACT_CHILD_CLOSURE_NOT_REACHED",
    "next_item": "Stage33-05_MATERIALIZE_ACTUAL_CECH_LOCAL_LATTICES_THEN_MARKED_PIC_MOD2_AND_HS_D2",
})

# Firewalls are assertions, not fields to be promoted by this checkpoint.
assert c["stage33_progress"] == "5/11"
assert c["merge_allowed"] is False
assert c["theorem_credit"] is False
assert c["receiver_credit"] is False
assert c["endpoint_credit"] is False
assert child["stage33_12_closed_exact"] is False
assert child["j2_Q_descent_credit_restored"] is False
assert child["j2_HS_d2_materialized"] is False
assert next(x for x in c["repair_children"] if x["id"] == "33-13")["released"] is False

CONTROLLER.write_text(
    json.dumps(c, sort_keys=False, separators=(",", ":")) + "\n",
    encoding="utf-8",
)
print(json.dumps({
    "success": True,
    "controller_schema": c["schema"],
    "stage33_progress": c["stage33_progress"],
    "stage33_05_reclosed": h.get("stage33_05_reclosed", False),
    "stage33_12_closed_exact": child["stage33_12_closed_exact"],
    "stage33_13_released": next(x for x in c["repair_children"] if x["id"] == "33-13")["released"],
    "next_exact_leaf": next_leaf,
}, indent=2, sort_keys=True))
