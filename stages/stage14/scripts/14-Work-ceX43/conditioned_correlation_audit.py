from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


work = text("stages/stage14/14-Work-ceX43/result.md")
matrix = text("docs/stage14-toolbox/work-ceX43-receiver-matrix.md")
q20 = text("docs/stage14-q20-summary.md")
radar = text("docs/stage14-q20-conditioned-divisor-correlation-literature-radar.md")
s129 = text("stages/stage14/14-s7-129/result.md")
s130 = text("stages/stage14/14-s7-130/result.md")
s131 = text("stages/stage14/14-s7-131/result.md")

for tok in [
    "WORK_RUN_GATE=RUN_S7_131_NORMAL_REVISIT_AND_Q19_HANDOFF_SUCCESS",
    "SECOND_REVERSE_EXACT_WEIGHT_ENCODING_CONSUMED=true",
    "SECOND_REVERSE_SUPPORT_FIRST_MOMENT_EQUIVALENCE_CONSUMED=true",
    "CONDITIONED_CORRELATION_RECEIVER_ISOLATION_LEMMA_PROVED=true",
    "RESOLVED_SUPPORT_TO_MOMENT_ADAPTER_RECHARGE_FORBIDDEN=true",
    "S_CONDITIONED_SECOND_REVERSE_CORRELATION_RECEIVER_PROVED=true",
    "S_THEOREM_SPECIES_MEASURE_VARIANT_COUNT=2",
    "Q_COMPONENT=COMPLETE",
    "Q_TRIGGER_STAGE=Stage14-s7-131",
    "Q_LEDGER_BASELINE=Stage14-q19",
    "Q_RESULT_IMPORTED_BACK_TO_X=true",
    "MAIN_ALIGNED_EXTERNAL_GATE_PARKED=true",
    "FIXED_U_SUPER_KAI_EXTERNAL_GATE_PARKED=true",
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
    "SECOND_REVERSE_SAVING_CROSS_PROMOTABLE_TO_POST_MASK=false",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "WHOLE_STAGE14_BLOCKED_BY_EXTERNAL_GATES=false",
]:
    assert tok in matrix, tok

for tok in [
    "STAGE14_Q20=COMPLETE_CONDITIONED_DIVISOR_CORRELATION_LITERATURE_RADAR",
    "DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
    "CONDITIONED_SECOND_REVERSE_CORRELATION_DIRECT_THEOREM_FOUND=false",
    "Q20_WITNESS_DEPENDENCE_SEPARABILITY_TEST",
    "Q20_FIXED_SHIFT_OR_BINARY_FORM_NORMAL_FORM_TEST",
    "Q20_POST_MASK_SEARCHED=false",
]:
    assert tok in radar, tok

for tok in [
    "Q20_COMPONENT_COMPLETE=true",
    "Q20_NEXT_SEARCH_TRIGGER_REACHED=false",
    "SHIFTED_D3_D_DIRECT_TRANSFER_PROVED=false",
    "BINARY_FORM_DIVISOR_SUM_DIRECT_TRANSFER_PROVED=false",
]:
    assert tok in q20, tok

# Merged receiving-stage facts.
assert "Q19_SECOND_REVERSE_EXACT_WEIGHT_ENCODING_TEST=PASS" in s129
assert "SECOND_REVERSE_SUPPORT_FIRST_MOMENT_EQUIVALENCE_PROVED=true" in s130
assert "Q19_SECOND_REVERSE_CORRELATION_SHAPE_TEST=PASS_NEW_STABLE_CORRELATION" in s131
assert "SECOND_REVERSE_EXACT_JOINT_FIRST_MOMENT_FROZEN=true" in s131
assert "POST_MASK_REMAINS_SEPARATE=true" in s131

print("Stage14-Work-ceX43 + q20 conditioned correlation audit: PASS")
