from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "stages/stage27/27-controller.json"
data = json.loads(path.read_text())

data["status"] = "OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R5AH_R5AI_PENDING_FRESH_AUDIT"
data["checkpoint_status"]["40"] = (
    "UPPER_ATTACK_AUDITED_PASS_MERGED_WITH_R402C_F_AUDITED_PASS_MERGED_"
    "AND_R5_AUDITED_PASS_MERGED_CLOSED_AND_R5AF_R5AG_AUDITED_PASS_MERGED_"
    "AND_R5AH_R5AI_PENDING_AUDIT"
)

old = data["derived_routes"].setdefault("Stage27-19-r5af-r5ag", {})
old.update(
    {
        "status": "AUDITED_PASS_MERGED",
        "trigger_checkpoint": 40,
        "route_serial": "19-r5af-r5ag",
        "route_kind": "UPPER_REENTRY_PARALLEL",
        "source_stage": "Stage19",
        "parent_route": "Stage27-19-r5",
        "batch_routes": ["27-19-r5af", "27-19-r5ag"],
        "audit_status": "PASS",
        "mathematical_audit": "PASS",
        "ci_audit": "PASS",
        "lifecycle_audit": "PASS_AFTER_REPAIR_REGISTRATION",
        "previous_fail_reason": "POST_R5AF_R5AG_FRESH_AUDIT_NOT_REGISTERED_IN_REPO",
        "audit_record": "stages/stage27/27-19-r5af/audit-final.md",
        "pr": 1051,
        "merge_commit": "e7e11fd67d147d4f7c78b153e330c6bb6ed0e1a9",
        "advance_to_checkpoint50": False,
        "advance_allowed": True,
        "merge_allowed": True,
        "strict_sub_sqrt_upper_proved": False,
        "new_mu_lt_half_proved": False,
        "true_N2_exponent_identified": False,
        "next_derived_route": "27-19-r5ah",
    }
)

new = data["derived_routes"].setdefault("Stage27-19-r5ah-r5ai", {})
new.update(
    {
        "status": "BATCH_SUBMITTED_PENDING_FRESH_AUDIT",
        "trigger_checkpoint": 40,
        "route_serial": "19-r5ah-r5ai",
        "route_kind": "UPPER_REENTRY_PARALLEL",
        "source_stage": "Stage19",
        "parent_route": "Stage27-19-r5af-r5ag",
        "batch_routes": ["27-19-r5ah", "27-19-r5ai"],
        "audit_status": "PENDING",
        "result_path": "stages/stage27/27-19-r5ah/result.md",
        "route_contract": "stages/stage27/27-19-r5ah/route-contract.json",
        "exact_primitive_scale_factorization_proved": True,
        "exact_primitive_scale": "Gamma=2*delta*epsilon*C",
        "cross_gcd_product": "C=gcd(m,r)*gcd(m,s0)*gcd(r,n0)",
        "exact_physical_diagonal_integer_product_proved": True,
        "exact_physical_diagonal_product": "R=(h/epsilon)*kappa*w_prime*c_prime",
        "h_kappa_bound_proved": True,
        "h_kappa_bound": "h*kappa<=epsilon*B<=2B",
        "hidden_gamma_branch_closed": True,
        "threshold_cancellation_dichotomy_proved": True,
        "small_h_kappa_population_fixed_power_bound_proved": False,
        "large_cross_gcd_cancellation_sparse_proved": False,
        "strict_sub_sqrt_upper_proved": False,
        "new_mu_lt_half_proved": False,
        "true_N2_exponent_identified": False,
        "advance_to_checkpoint50": False,
        "advance_allowed": False,
        "merge_allowed": False,
        "next_derived_route": "27-19-r5aj",
    }
)

state = data["state"]
state.update(
    {
        "CURRENT_CHECKPOINT": 40,
        "MAIN_STATUS": "UPPER_REENTRY_STAGE27_19_R5AH_R5AI_SUBMITTED_PENDING_FRESH_AUDIT",
        "AUDIT_STATUS": "PENDING",
        "ADVANCE_ALLOWED": False,
        "NEXT_CHECKPOINT": 40,
        "NEXT_STAGE": "",
        "NEW_INPUT_REQUIRED": False,
        "HUMAN_DECISION_REQUIRED": False,
        "MERGE_ALLOWED": False,
    }
)

data["next_expected_command"] = "Stage27-19-r5-audit"

path.write_text(json.dumps(data, indent=2) + "\n")
