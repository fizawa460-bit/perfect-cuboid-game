from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
HERE = ROOT / "stages" / "stage27" / "27-20-r301z"

result = (HERE / "result.md").read_text(encoding="utf-8")
registry = json.loads((HERE / "batch-registry.json").read_text(encoding="utf-8"))
delta = json.loads((HERE / "controller-sync-delta.json").read_text(encoding="utf-8"))
audit = (HERE / "audit.md").read_text(encoding="utf-8")
parent_audit = (ROOT / "stages" / "stage27" / "27-20-r301w-y" / "audit.md").read_text(encoding="utf-8")

required_result_markers = [
    "STATUS=AUDITED_PASS_MERGED",
    "FIXED_WIDTH_WALL_SLAB_RECEIVER_DERIVED=true",
    "WALL_SLAB_THETA_CONDITION=abs(theta-1/4)<eta0",
    "EXACT_THETA_LINE_ALONE_SUFFICIENT=false",
    "GLOBAL_DEFICIT_IF_WALL_THEOREM=Delta=min(delta,2eta0,1/16)",
    "R301Z_WALL_THEOREM_PROVED=false",
    "OFF_THE_SHELF_FIRST_MOMENT_APPLICABILITY_CLAIMED=false",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
    "NEW_MU_LT_HALF_PROVED=false",
    "AUDIT_STATUS=PASS",
    "ADVANCE_ALLOWED=true",
    "FRESH_REAUDIT_REQUIRED=false",
    "NEXT_BATCH=Stage27-20-r302-main-batch",
    "R301AA_FORBIDDEN=true",
]
for marker in required_result_markers:
    assert marker in result, marker

assert "AUDIT_VERDICT=PASS" in parent_audit
assert "NEXT_DERIVED_ROUTE=27-20-r301z" in parent_audit
assert "NUMBERING_AFTER_R301Z=Stage27-20-r302-main-batch" in parent_audit

assert "AUDIT_VERDICT=PASS" in audit
assert "MATHEMATICAL_AUDIT=PASS" in audit
assert "CI_AUDIT=PASS" in audit
assert "AUDIT_PR=1062" in audit
assert "PR_MERGE_COMMIT=96e99d8e4232ad06da748ad4e37b8c43f16e944b" in audit
assert "NEXT_BATCH=Stage27-20-r302-main-batch" in audit

assert registry["batch_id"] == "Stage27-20-r301z"
assert registry["checkpoint"] == 40
assert registry["status"] == "AUDITED_PASS_MERGED"
assert registry["audit_status"] == "PASS"
assert registry["merge_allowed"] is True
assert registry["advance_allowed"] is True
assert registry["fresh_reaudit_required"] is False
assert registry["merge_commit"] == "96e99d8e4232ad06da748ad4e37b8c43f16e944b"
assert registry["claims"]["fixed_width_wall_slab_receiver_derived"] is True
assert registry["claims"]["exact_theta_line_alone_sufficient"] is False
assert registry["claims"]["r301z_wall_theorem_proved"] is False
assert registry["claims"]["strict_sub_sqrt_upper_proved"] is False
assert registry["next_batch"] == "Stage27-20-r302-main-batch"
assert registry["numbering_contract"]["r301aa_forbidden"] is True

assert delta["global_controller_rewritten"] is False
assert delta["preserve_global_status_from_base"] is True
assert delta["consume_closeout"]["audit_status"] == "PASS"
assert delta["consume_closeout"]["merge_commit"] == "96e99d8e4232ad06da748ad4e37b8c43f16e944b"
assert delta["intended_stage20_delta"]["Stage27-20-r301z"] == "AUDITED_PASS_MERGED"
assert delta["next_batch_after_audit"] == "Stage27-20-r302-main-batch"
assert delta["advance_allowed"] is True
assert delta["fresh_reaudit_required"] is False
assert delta["r301aa_forbidden"] is True

# The gluing statement must explicitly retain both sources of saving.
assert "Delta=\\min(\\delta,2\\eta_0,1/16)>0" in result
assert "R301u handles the complement" in result
assert "exact line `theta=1/4`" in result

print("Stage27-20-r301z audited closeout verifier: PASS")
