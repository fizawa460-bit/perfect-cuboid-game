from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def text(rel):
    return (ROOT / rel).read_text()

s135 = text('stages/stage14/14-s7-135/result.md')
s136 = text('stages/stage14/14-s7-136/result.md')
s137 = text('stages/stage14/14-s7-137/result.md')
work = text('stages/stage14/14-Work-cfX44/result.md')
report = text('stages/stage14/14-s-batch/s7-135-137-report.md')

for tok in [
    'SECOND_REVERSE_SELF_COUPLED_MODULUS_CANCELLATION_PROVED=true',
    'S_NONALIGNED_SECOND_REVERSE_INNER_KERNEL_IDENTIFIED_WITH_Q17_RECIPROCAL_CRT_FORM=true',
    'Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false',
]:
    assert tok in work, tok

for tok in [
    'S_SECOND_REVERSE_INNER_KERNEL_EQUALS_Q17_RECIPROCAL_CRT=true',
    'CANCELLATION_LOSS=0',
    'Q17_INNER_KERNEL_RESEARCH_RECHARGED=false',
]:
    assert tok in s135, tok

for tok in [
    'Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_TEST=FAIL',
    'FILTERED_TAU3_WITNESS_LABELS_CAN_BE_SUMMED_AWAY=false',
    'BO1_WITNESS_FIBER_IMPLIES_MEASURE_TRANSFER=false',
]:
    assert tok in s136, tok

for tok in [
    'S_CONDITIONED_RECIPROCAL_CRT_DEFICIT_LEDGER_PROVED=true',
    'S_HEAVY_SURVIVAL_BUDGET=sigma_mult_minus_delta_crt_cond_minus_delta_post_ge_mu',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'NEXT=Stage14-s7-138',
]:
    assert tok in s137, tok

for tok in [
    'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3',
    'BATCH_STOP_REASON=receiver_change',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'S_ROUTE_H_NEEDED=false',
    'NEXT=Stage14-s7-138',
]:
    assert tok in report, tok

# Exact cancellation sanity checks.
for W in range(1, 60):
    for f in range(1, W + 1):
        if W % f:
            continue
        n = W // f
        for U in range(1, 5):
            for V in range(1, 5):
                qdr = ((W + f*f) % (2*U*f) == 0 and (W - f*f) % (2*V*f) == 0)
                crt = ((n + f) % (2*U) == 0 and (n - f) % (2*V) == 0)
                assert qdr == crt, (W, f, U, V)

print('Stage14-s-batch s7-135..137 audit: OK')
