from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def text(rel):
    return (ROOT / rel).read_text()

s132 = text('stages/stage14/14-s7-132/result.md')
s133 = text('stages/stage14/14-s7-133/result.md')
s134 = text('stages/stage14/14-s7-134/result.md')
rep = text('stages/stage14/14-s-batch/s7-132-134-report.md')
q20 = text('stages/stage14/archive/docs/q-research/stage14-q20-summary.md')

for tok in [
    'Q20_WITNESS_DEPENDENCE_SEPARABILITY_TEST=FAIL_INTRINSIC_FIRST_WITNESS_DEPENDENCE',
    'SECOND_REVERSE_W1_OUTER_ONLY=false',
    'FIRST_LAYER_WITNESS_CAN_BE_SUMMED_AWAY_FOR_FREE=false',
]:
    assert tok in s132, tok

for tok in [
    'S_SECOND_REVERSE_QUADRATIC_DIVISOR_ROOT_ENCODING_EXACT=true',
    'W1 + f^2 == 0 (mod 2*U*f)',
    'W1 - f^2 == 0 (mod 2*V*f)',
    'Q20_FIXED_SHIFT_OR_BINARY_FORM_NORMAL_FORM_TEST=FAIL_MOVING_W1_AND_DIVISOR_HOSTED_MODULUS',
]:
    assert tok in s133, tok

for tok in [
    'S_QUADRATIC_DIVISOR_ROOT_THEOREM_SPECIES_FROZEN=true',
    'POST_MASK_REMAINS_SEPARATELY_CHARGED=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'Q20_NEXT_SEARCH_TRIGGER_REACHED=true',
    'NEXT=Stage14-s7-135',
]:
    assert tok in s134, tok

for tok in [
    'Q20_WITNESS_DEPENDENCE_SEPARABILITY_TEST',
    'Q20_FIXED_SHIFT_OR_BINARY_FORM_NORMAL_FORM_TEST',
]:
    assert tok in q20, tok

for tok in [
    'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3',
    'BATCH_STOP_REASON=receiver_change',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'S_ROUTE_H_NEEDED=false',
    'NEXT=Stage14-s7-135',
]:
    assert tok in rep, tok

# Elementary equivalence used in s7-133 on deterministic samples.
for W1, U, V, f in [(60,1,1,2),(144,2,1,4),(360,1,3,6),(840,2,5,10)]:
    if W1 % f:
        continue
    Fp = W1 // f
    lhs1 = (Fp + f) % (2*U) == 0
    lhs2 = (Fp - f) % (2*V) == 0
    rhs1 = (W1 + f*f) % (2*U*f) == 0
    rhs2 = (W1 - f*f) % (2*V*f) == 0
    assert lhs1 == rhs1
    assert lhs2 == rhs2

print('STAGE14_S_BATCH_S7_132_134_AUDIT=PASS')
