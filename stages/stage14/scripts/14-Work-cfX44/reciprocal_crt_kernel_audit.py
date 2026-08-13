from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


work = text("stages/stage14/14-Work-cfX44/result.md")
matrix = text("docs/stage14-toolbox/work-cfX44-receiver-matrix.md")
s134 = text("stages/stage14/14-s7-134/result.md")
q17 = text("stages/stage14/archive/docs/q-research/stage14-q17-summary.md")
q20 = text("stages/stage14/archive/docs/q-research/stage14-q20-summary.md")

for tok in [
    "WORK_RUN_GATE=RUN_S7_134_MATERIAL_RECEIVER_CHANGE",
    "TOOLBOX_COMPONENT_COMPLETE=true",
    "X_COMPONENT_COMPLETE=true",
    "SECOND_REVERSE_SELF_COUPLED_MODULUS_CANCELLATION_PROVED=true",
    "QUADRATIC_DIVISOR_ROOT_AS_FINAL_INNER_KERNEL_SUPERSEDED=true",
    "CANCELLATION_LOSS=0",
    "S_NONALIGNED_SECOND_REVERSE_INNER_KERNEL_IDENTIFIED_WITH_Q17_RECIPROCAL_CRT_FORM=true",
    "Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false",
    "RESOLVED_SUPPORT_TO_MOMENT_ADAPTER_RECHARGE_FORBIDDEN=true",
    "POST_MASK_REMAINS_SEPARATELY_CHARGED=true",
    "Q_COMPONENT=NOT_TRIGGERED",
    "Q21_NEEDED=false",
    "TH34_NEEDED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "STAGE14_AUTOMATION_SAFE=true",
    "STAGE14_ROUTE=xq",
]:
    assert tok in work, tok

for tok in [
    "COMMON_INNER_KERNEL_DOES_NOT_IDENTIFY_CHARGED_MEASURE=true",
    "S_THEOREM_SPECIES_MEASURE_VARIANT_COUNT=2",
    "PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false",
    "Q17_INNER_KERNEL_ALREADY_SEARCHED=true",
    "Q20_CONDITIONED_CORRELATION_ALREADY_SEARCHED=true",
    "WHOLE_STAGE14_BLOCKED_BY_EXTERNAL_GATES=false",
]:
    assert tok in matrix, tok

# Receiving-stage exact quadratic-looking form.
for tok in [
    "W1(lambda)+f^2 == 0 (mod 2*U*f)",
    "W1(lambda)-f^2 == 0 (mod 2*V*f)",
    "S_QUADRATIC_DIVISOR_ROOT_THEOREM_SPECIES_FROZEN=true",
    "Q20_NEXT_SEARCH_TRIGGER_REACHED=true",
]:
    assert tok in s134, tok

# q17 exact reciprocal-CRT inner equations.
for tok in [
    "F_-F_+=4*r*s*epsilon_k*p*q",
    "F_+ + F_- == 0 mod 2U",
    "F_+ - F_- == 0 mod 2V",
    "RECIPROCAL_CRT_SUPPORT_DIRECT_THEOREM_FOUND=false",
]:
    assert tok in q17, tok

# q20 already searched the conditioned-correlation architecture.
for tok in [
    "STAGE14_Q20=COMPLETE_CONDITIONED_DIVISOR_CORRELATION_LITERATURE_RADAR",
    "CONDITIONED_SECOND_REVERSE_CORRELATION_DIRECT_THEOREM_FOUND=false",
]:
    assert tok in q20, tok

# Pure arithmetic sanity check of the cancellation used by X44.
for W, f, U, V in [
    (72, 6, 3, 3),
    (120, 10, 5, 1),
    (180, 6, 1, 3),
    (240, 12, 2, 1),
]:
    assert W % f == 0
    n = W // f
    assert ((W + f * f) % (2 * U * f) == 0) == ((n + f) % (2 * U) == 0)
    assert ((W - f * f) % (2 * V * f) == 0) == ((n - f) % (2 * V) == 0)

print("Stage14-Work-cfX44 reciprocal CRT kernel audit: PASS")
