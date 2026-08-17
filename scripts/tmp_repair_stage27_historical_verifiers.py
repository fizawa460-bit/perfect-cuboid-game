#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RESTORE = [
    "stages/stage27/27-19-r401a/verify_27_19_r401a.py",
    "stages/stage27/27-19-r401b/verify_27_19_r401b.py",
    "stages/stage27/27-19-r401c/verify_27_19_r401c.py",
    "stages/stage27/27-19-r401d/verify_27_19_r401d.py",
    "stages/stage27/27-19-r402/verify_27_19_r402.py",
]

for rel in RESTORE:
    content = subprocess.check_output(["git", "show", f"origin/main:{rel}"], cwd=ROOT)
    (ROOT / rel).write_bytes(content)


def replace_exact(rel: str, old: str, new: str) -> None:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    if old not in s:
        raise SystemExit(f"exact block not found in {rel}: {old[:120]!r}")
    p.write_text(s.replace(old, new, 1), encoding="utf-8")

# r401a: the route itself is already final PASS; keep all theorem checks and
# only stop pinning the mutable repository-wide active route / next command.
replace_exact(
    RESTORE[0],
    """assert ctl['state']['CURRENT_CHECKPOINT'] == 40\nassert ctl['state']['AUDIT_STATUS'] == 'PENDING'\nassert ctl['state']['MERGE_ALLOWED'] is False\nassert ctl['next_expected_command'] == 'Stage27-19-r401-audit'\nassert 'STAGE27_19_R401_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1031' in status\nassert (\n    'CURRENT_STAGE=Stage27-19-r401a-SUBMITTED-PENDING-FRESH-AUDIT' in status\n    or 'CURRENT_STAGE=Stage27-19-r401b-SUBMITTED-PENDING-FRESH-AUDIT' in status\n    or 'CURRENT_STAGE=Stage27-19-r401c-SUBMITTED-PENDING-FRESH-AUDIT' in status\n)\nassert (\n    'STAGE27_19_R401A_STATUS=GENUS_ONE_TORSOR_SUBMITTED_PENDING_FRESH_AUDIT' in status\n    or 'STAGE27_19_R401A_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1032' in status\n)\n""",
    """# Historical theorem regression: global active-route pointers are mutable.\nassert ctl['state']['CURRENT_CHECKPOINT'] == 40\nassert child['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'\nassert child['audit_status'] == 'PASS'\nassert child['pr'] == 1032\nassert child['merge_commit'] == '86b5428d42f7f4c7344bace93b067d580391d7ac'\n""",
)

# r401b: successor r401c is also final PASS now.
replace_exact(
    RESTORE[1],
    """assert pc['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'\nassert pc['all_affine_linear_multisections_classified'] is True\nassert pc['audit_status'] == 'PENDING'\nassert ctl['state']['CURRENT_CHECKPOINT'] == 40\nassert ctl['state']['AUDIT_STATUS'] == 'PENDING'\nassert ctl['state']['MERGE_ALLOWED'] is False\nassert ctl['next_expected_command'] == 'Stage27-19-r401-audit'\nassert 'CURRENT_STAGE=Stage27-19-r401c-SUBMITTED-PENDING-FRESH-AUDIT' in status\nassert 'STAGE27_19_R401B_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1033' in status\nassert 'STAGE27_19_R401C_STATUS=AFFINE_LINEAR_SUBMITTED_PENDING_FRESH_AUDIT' in status\n""",
    """assert pc['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'\nassert pc['all_affine_linear_multisections_classified'] is True\nassert pc['audit_status'] == 'PASS'\nassert pc['pr'] == 1035\nassert pc['merge_commit'] == '4ca03c43f4ff2c858c51ac8959d6e75f077c6de7'\n# Historical theorem regression: global active-route pointers are mutable.\nassert ctl['state']['CURRENT_CHECKPOINT'] == 40\n""",
)

# r401c: canonicalized after PR1035.
replace_exact(
    RESTORE[2],
    """assert pc['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'\nassert pc['all_affine_linear_multisections_classified'] is True\nassert pc['affine_linear_physical_genus_zero_route_exists'] is False\nassert pc['lower_exponent_above_one_quarter_proved'] is False\nassert pc['audit_status'] == 'PENDING'\nassert ctl['state']['CURRENT_CHECKPOINT'] == 40\nassert ctl['state']['AUDIT_STATUS'] == 'PENDING'\nassert ctl['state']['MERGE_ALLOWED'] is False\nassert ctl['next_expected_command'] == 'Stage27-19-r401-audit'\nassert 'CURRENT_STAGE=Stage27-19-r401c-SUBMITTED-PENDING-FRESH-AUDIT' in status\nassert 'STAGE27_19_R401B_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1033' in status\nassert 'STAGE27_19_R401C_STATUS=AFFINE_LINEAR_SUBMITTED_PENDING_FRESH_AUDIT' in status\n""",
    """assert pc['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'\nassert pc['all_affine_linear_multisections_classified'] is True\nassert pc['affine_linear_physical_genus_zero_route_exists'] is False\nassert pc['lower_exponent_above_one_quarter_proved'] is False\nassert pc['audit_status'] == 'PASS'\nassert pc['pr'] == 1035\nassert pc['merge_commit'] == '4ca03c43f4ff2c858c51ac8959d6e75f077c6de7'\n# Historical theorem regression: global active-route pointers are mutable.\nassert ctl['state']['CURRENT_CHECKPOINT'] == 40\n""",
)

# r401d: repair batch has long since passed and merged.
replace_exact(
    RESTORE[3],
    """assert pd['status'] == 'REPAIR_SUBMITTED_PENDING_FRESH_AUDIT'\nassert pd['r501_tau_projection_degree'] == 8\nassert pd['r502_tau_projection_degree'] == 8\nassert pd['r501_toric_degree_ledger'] == 'dx2_dy2_g0_h8'\nassert pd['r502_toric_degree_ledger'] == 'dx4_dy2_g4_h8'\nassert pd['r502_degree12_to_8_polynomial_cancellation_proved'] is True\nassert pd['one_parameter_algebraic_progress_gate'] == '2dx+2dy-g<8'\nassert pd['lower_bounded_reentry_stop_candidate'] is True\nassert pd['previous_audit_verdict'] == 'FAIL'\nassert pd['mathematical_audit_status'] == 'PASS'\nassert pd['previous_fail_reason'] == 'STALE_R401C_PENDING_STATE_AND_MISSING_R401D_CANONICAL_REGISTRATION'\nassert pd['audit_status'] == 'PENDING'\nassert pd['advance_to_checkpoint50'] is False\nassert pd['merge_allowed'] is False\nassert ctl['state']['CURRENT_CHECKPOINT'] == 40\nassert ctl['state']['AUDIT_STATUS'] == 'PENDING'\nassert ctl['state']['MERGE_ALLOWED'] is False\nassert ctl['next_expected_command'] == 'Stage27-19-r401-audit'\nassert 'CURRENT_STAGE=Stage27-19-r401d-REPAIR-SUBMITTED-PENDING-FRESH-AUDIT' in status\nassert 'STAGE27_19_R401C_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1035' in status\nassert 'STAGE27_AFFINE_LINEAR_RECEIVER_DERIVED=true' in status\nassert 'STAGE27_AFFINE_LINEAR_DISCRIMINANT_FACTORIZATION_PROVED=true' in status\nassert 'STAGE27_ALL_AFFINE_LINEAR_MULTISECTIONS_CLASSIFIED=true' in status\nassert 'STAGE27_19_R401D_STATUS=R501_R502_CALIBRATION_REPAIR_SUBMITTED_PENDING_FRESH_AUDIT' in status\nassert 'STAGE27_NEXT_UPPER_ROUTE=27-40af' in status\n""",
    """assert pd['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'\nassert pd['r501_tau_projection_degree'] == 8\nassert pd['r502_tau_projection_degree'] == 8\nassert pd['r501_toric_degree_ledger'] == 'dx2_dy2_g0_h8'\nassert pd['r502_toric_degree_ledger'] == 'dx4_dy2_g4_h8'\nassert pd['r502_degree12_to_8_polynomial_cancellation_proved'] is True\nassert pd['one_parameter_algebraic_progress_gate'] == '2dx+2dy-g<8'\nassert pd['lower_bounded_reentry_stop_candidate'] is True\nassert pd['previous_audit_verdict'] == 'FAIL'\nassert pd['mathematical_audit_status'] == 'PASS'\nassert pd['previous_fail_reason'] == 'STALE_R401C_PENDING_STATE_AND_MISSING_R401D_CANONICAL_REGISTRATION'\nassert pd['audit_status'] == 'PASS'\nassert pd['pr'] == 1036\nassert pd['merge_commit'] == 'b37bc86e045175238bf2520518b059574addc52b'\nassert pd['advance_to_checkpoint50'] is False\nassert pd['merge_allowed'] is True\n# Historical theorem regression: global active-route pointers are mutable.\nassert ctl['state']['CURRENT_CHECKPOINT'] == 40\n""",
)

# r402: upper route itself is final PASS; only historical live pointers are stale.
replace_exact(
    RESTORE[4],
    """assert p2['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'\nassert p2['trigger_checkpoint'] == 40\nassert p2['route_kind'] == 'UPPER_REENTRY'\nassert p2['tau_defined_before_space_filter'] is True\nassert p2['tau_support_polynomial_lower_proved'] is True\nassert p2['tau_support_lower_exponent'] == '1/4'\nassert p2['tau_max_fiber_upper_gate'] == 'sigma+phi<1/2'\nassert p2['tau_second_moment_upper_gate'] == 'sigma+eta<1'\nassert p2['strict_sub_sqrt_upper_proved'] is False\nassert p2['audit_status'] == 'PENDING'\nassert p2['merge_allowed'] is False\nassert ctl['state']['CURRENT_CHECKPOINT'] == 40\nassert ctl['state']['AUDIT_STATUS'] == 'PENDING'\nassert ctl['state']['MERGE_ALLOWED'] is False\nassert ctl['next_expected_command'] == 'Stage27-19-r402-audit'\nassert 'CURRENT_STAGE=Stage27-19-r402-SUBMITTED-PENDING-FRESH-AUDIT' in status\nassert 'STAGE27_19_R401D_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1036' in status\nassert 'STAGE27_19_R402_STATUS=TAU_PUSHFORWARD_UPPER_SUBMITTED_PENDING_FRESH_AUDIT' in status\nassert 'STAGE27_TAU_DEFINED_BEFORE_SPACE_FILTER=true' in status\nassert 'STAGE27_TAU_SUPPORT_POLYNOMIAL_LOWER_PROVED=true' in status\nassert 'NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit' in status\n""",
    """assert p2['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'\nassert p2['trigger_checkpoint'] == 40\nassert p2['route_kind'] == 'UPPER_REENTRY'\nassert p2['tau_defined_before_space_filter'] is True\nassert p2['tau_support_polynomial_lower_proved'] is True\nassert p2['tau_support_lower_exponent'] == '1/4'\nassert p2['tau_max_fiber_upper_gate'] == 'sigma+phi<1/2'\nassert p2['tau_second_moment_upper_gate'] == 'sigma+eta<1'\nassert p2['strict_sub_sqrt_upper_proved'] is False\nassert p2['audit_status'] == 'PASS'\nassert p2['pr'] == 1037\nassert p2['merge_commit'] == '77dc7bc7eb29f4113d59c8255ab4b2148bd52690'\nassert p2['merge_allowed'] is True\n# Historical theorem regression: global active-route pointers are mutable.\nassert ctl['state']['CURRENT_CHECKPOINT'] == 40\n""",
)

# r5ah is not restored: its theorem verifier remains current, but its own
# lifecycle moved from pending to audited+merged in this successor PR.
r5ah = ROOT / "stages/stage27/27-19-r5ah/verify_27_19_r5ah_r5ai.py"
s = r5ah.read_text(encoding="utf-8")
s = s.replace(
    'assert contract["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"',
    'assert contract["status"] == "CLOSED_AUDITED_PASS_MERGED"\nassert contract["final_audit"]["pr"] == 1054\nassert contract["final_audit"]["merge_commit"] == "38dd56bc3fdcc6830f39340f00bb7bcfc4ad66f9"',
    1,
)
s = s.replace(
    'assert controller["derived_routes"]["Stage27-19-r5ah-r5ai"]["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"',
    'assert controller["derived_routes"]["Stage27-19-r5ah-r5ai"]["status"] == "AUDITED_PASS_MERGED"\nassert controller["derived_routes"]["Stage27-19-r5ah-r5ai"]["audit_status"] == "PASS"\nassert controller["derived_routes"]["Stage27-19-r5ah-r5ai"]["merge_commit"] == "38dd56bc3fdcc6830f39340f00bb7bcfc4ad66f9"',
    1,
)
r5ah.write_text(s, encoding="utf-8")

print("exact historical verifier repair prepared")
