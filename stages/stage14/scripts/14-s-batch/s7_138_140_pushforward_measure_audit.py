from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def text(rel):
    return (ROOT / rel).read_text()

s138 = text('stages/stage14/14-s7-138/result.md')
s139 = text('stages/stage14/14-s7-139/result.md')
s140 = text('stages/stage14/14-s7-140/result.md')
rep = text('stages/stage14/14-s-batch/s7-138-140-report.md')
work = text('stages/stage14/14-Work-cgX45/result.md')

for tok in [
    'S_Q17_KERNEL_PUSHFORWARD_DISINTEGRATION_PROVED=true',
    'S_CONDITIONED_MEASURE_TRANSFER_REDUCED_TO_PUSHFORWARD_WEIGHT_COMPARISON=true',
    'BO1_FIBER_DOES_NOT_IMPLY_LOWER_DOMINATION=true',
]:
    assert tok in s138, tok

for tok in [
    'Q17_TO_S_LOWER_DOMINATION_CRITERION_PROVED=true',
    'S_PUSHFORWARD_LOWER_DOMINATION_PROVED=false',
    'S_PUSHFORWARD_Q17_DOMAIN_COVERAGE_PROVED=false',
    'S_MEASURE_TRANSFER_VARIANT_COUNT=2',
]:
    assert tok in s139, tok

for tok in [
    'S_PUSHFORWARD_POINTWISE_UPPER_ENVELOPE=Bo1',
    'S_Q17_GOOD_PACKET_COVERAGE_PROVED=false',
    'S_CONDITIONED_MEASURE_COVERAGE_POSTMASK_LEDGER_PROVED=true',
    'Q17_INNER_KERNEL_DEFICIT_RECHARGED=false',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'NEXT=Stage14-s7-141',
]:
    assert tok in s140, tok

for tok in [
    'CONDITIONED_KERNEL_MEASURE_FIREWALL_LEMMA_PROVED=true',
    'IDENTICAL_KERNEL_DOES_NOT_IMPLY_MEASURE_TRANSFER=true',
    'Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false',
]:
    assert tok in work, tok

for tok in [
    'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3',
    'BATCH_STOP_REASON=receiver_change',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'S_ROUTE_H_NEEDED=false',
    'Q21_NEEDED=false',
    'NEXT=Stage14-s7-141',
    'STAGE14_AUTOMATION_SAFE=true',
    'STAGE14_ROUTE=s',
]:
    assert tok in rep, tok

# Basic weighted-transfer sanity: comparability transfers a lower ratio.
q = [3, 5, 2, 7]
s = [6, 10, 4, 14]
k = [1, 0, 1, 1]
q_ratio = sum(a*b for a,b in zip(q,k)) / sum(q)
s_ratio = sum(a*b for a,b in zip(s,k)) / sum(s)
assert abs(q_ratio-s_ratio) < 1e-12

print('STAGE14_S_BATCH_S7_138_140_AUDIT=PASS')
