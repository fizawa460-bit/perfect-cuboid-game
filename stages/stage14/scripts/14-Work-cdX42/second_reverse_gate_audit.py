from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


work = text("stages/stage14/14-Work-cdX42/result.md")
matrix = text("docs/stage14-toolbox/work-cdX42-receiver-matrix.md")
q19 = text("docs/stage14-q19-summary.md")
q19_radar = text("docs/stage14-q19-second-reverse-extension-literature-radar.md")
s128 = text("stages/stage14/14-s7-128/result.md")
th33 = text("stages/stage14/14-tH33/result.md")

for tok in [
    "WORK_RUN_GATE=RUN_NORMAL_REVISIT_TH33_PLUS_S7_128_AND_Q18_HANDOFF_SUCCESS",
    "Q18_FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=true",
    "Q18_FIRST_REVERSE_LAYER_TRANSFER_CONSUMED=true",
    "S_FIRST_LAYER_FILTERED_TAU3_AS_FINAL_OBSTRUCTION_SUPERSEDED=true",
    "S_SECOND_REVERSE_EXTENSION_IS_NEXT_BARE_ARITHMETIC_RECEIVER=true",
    "RESOLVED_INNER_SUPPORT_ADAPTER_CONSUMPTION_LEMMA_PROVED=true",
    "Q_COMPONENT=COMPLETE",
    "Q_TRIGGER_STAGE=Stage14-s7-128",
    "Q_LEDGER_BASELINE=Stage14-q18",
    "Q_RESULT_IMPORTED_BACK_TO_X=true",
    "MAINLINE_H_COMPLETED=true",
    "FIXED_U_H_COMPLETED=true",
    "TH33_COMPLETE_CONSUMED=true",
    "TH34_NEEDED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    "STAGE14_AUTOMATION_SAFE=true",
    "STAGE14_ROUTE=xq",
]:
    assert tok in work, tok

for tok in [
    "PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false",
    "MAIN_ALIGNED_EXTERNAL_GATE_PARKED=true",
    "FIXED_U_SUPER_KAI_EXTERNAL_GATE_PARKED=true",
    "WHOLE_STAGE14_BLOCKED_BY_EXTERNAL_GATES=false",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
]:
    assert tok in matrix, tok

for tok in [
    "STAGE14_Q19=COMPLETE_CONDITIONED_SECOND_REVERSE_EXTENSION_LITERATURE_RADAR",
    "DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
    "SECOND_REVERSE_EXTENSION_DIRECT_THEOREM_FOUND=false",
    "Q19_SECOND_REVERSE_EXACT_WEIGHT_ENCODING_TEST",
    "Q19_SECOND_REVERSE_CORRELATION_SHAPE_TEST",
    "Q19_PAIR_TO_SCALAR_TRANSFER_ALLOWED=false",
]:
    assert tok in q19, tok

for tok in [
    "NGUYEN_AP_II_SHIFTED_TAU3=NEAR_HIGH_PRIORITY_IF_EXACT_SHIFTED_ENCODING_EXISTS",
    "WEI_XUE_ZHANG_GENERAL_DIVISOR_AP=NEAR_CONDITIONAL",
    "FREI_SOFOS_BINARY_FORM_DIVISOR_SUMS=NEAR_STRUCTURE",
    "Q19_POST_MASK_SEARCHED=false",
]:
    assert tok in q19_radar, tok

# Merged receiving-stage facts.
assert "Q18_FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=true" in s128
assert "Q18_NEXT_SEARCH_TRIGGER_REACHED=true" in s128
assert "NEXT=Stage14-s7-129" in s128

for tok in [
    "STAGE14_TH33=COMPLETE_NEGATIVE_UNRESOLVED_SUPER_KAI_INDIVIDUAL_RESIDUE_GATE_AUDIT",
    "DIRECT_THEOREM_APPLICABLE=false",
    "SUPER_KAI_INDIVIDUAL_RESIDUE_LONG_INTERVAL_COVERED=false",
    "FIXED_U_H_COMPLETED=true",
    "FIXED_U_BLOCKED_BY_H=true",
    "NEXT_H_NEEDED=false",
]:
    assert tok in th33, tok

print("Stage14-Work-cdX42 + q19 second-reverse gate audit: PASS")
