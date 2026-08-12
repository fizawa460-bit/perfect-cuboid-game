from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def text(rel):
    return (ROOT / rel).read_text()

s129 = text('stages/stage14/14-s7-129/result.md')
s130 = text('stages/stage14/14-s7-130/result.md')
s131 = text('stages/stage14/14-s7-131/result.md')
rep = text('stages/stage14/14-s-batch/s7-129-131-report.md')
q19 = text('docs/stage14-q19-summary.md')

for tok in [
    'Q19_SECOND_REVERSE_EXACT_WEIGHT_ENCODING_TEST',
    'Q19_SECOND_REVERSE_CORRELATION_SHAPE_TEST',
]:
    assert tok in q19, tok

for tok in [
    'Q19_SECOND_REVERSE_EXACT_WEIGHT_ENCODING_TEST=PASS',
    'S_SECOND_REVERSE_EXACT_EXTENSION_WEIGHT_DEFINED=true',
    'SECOND_REVERSE_EXTENSION_MULTIPLICITY_UPPER_ENVELOPE=Bo1',
    'POST_MASK_INSERTED_IN_N_REV2=false',
]:
    assert tok in s129, tok

for tok in [
    'SECOND_REVERSE_SUPPORT_FIRST_MOMENT_EQUIVALENCE_PROVED=true',
    'SECOND_REVERSE_OUTER_SUPPORT_JOINT_MOMENT_EQUIVALENCE_PROVED=true',
    'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
    'FIRST_LAYER_DEFICIT_RECHARGED=false',
]:
    assert tok in s130, tok

for tok in [
    'Q19_SECOND_REVERSE_CORRELATION_SHAPE_TEST=PASS_NEW_STABLE_CORRELATION',
    'SECOND_REVERSE_EXACT_JOINT_FIRST_MOMENT_FROZEN=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'Q19_NEXT_SEARCH_TRIGGER_REACHED=true',
]:
    assert tok in s131, tok

for tok in [
    'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3',
    'BATCH_STOP_REASON=receiver_change',
    'S_ROUTE_H_NEEDED=false',
    'NEXT=Stage14-s7-132',
    'STAGE14_AUTOMATION_SAFE=true',
    'STAGE14_ROUTE=s',
]:
    assert tok in rep, tok

# Toy support/moment sandwich: positive extension counts bounded by D.
vals = [0, 1, 3, 0, 2, 1]
supp = sum(v > 0 for v in vals)
m1 = sum(vals)
D = max(vals)
assert supp <= m1 <= D * supp

print('STAGE14_S_BATCH_S7_129_131_AUDIT=PASS')
