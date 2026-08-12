from pathlib import Path

root = Path(__file__).resolve().parents[4]
result = (root / 'stages/stage14/14-Work-cjX48/result.md').read_text()
matrix = (root / 'docs/stage14-toolbox/work-cjX48-receiver-matrix.md').read_text()
q22 = (root / 'stages/stage14/14-q22/result.md').read_text()
qsum = (root / 'stages/stage14/14-q22/summary.md').read_text()
s144 = (root / 'stages/stage14/14-s7-144/result.md').read_text()
s145 = (root / 'stages/stage14/14-s7-145/result.md').read_text()
s146 = (root / 'stages/stage14/14-s7-146/result.md').read_text()

for token in [
    'GOOD_PACKET_INDICATOR_FIRST_MOMENT_ENCODING_CONSUMED=true',
    'GOOD_PACKET_SECOND_MOMENT_AUTOCONTROL_CONSUMED=true',
    'GOOD_PACKET_SECOND_MOMENT_AS_INDEPENDENT_GATE_SUPERSEDED=true',
    'GOOD_PACKET_SECOND_MOMENT_RECHARGE_FORBIDDEN=true',
    'Q22_GOOD_INDICATOR_DIRECT_THEOREM_FOUND=false',
    'TH34_NEEDED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
]:
    assert token in result, token

for token in [
    'GOOD_PACKET_SECOND_MOMENT_RECHARGE_FORBIDDEN=true',
    'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
    'POST_MASK_REMAINS_SEPARATELY_CHARGED=true',
]:
    assert token in matrix, token

for token in [
    'DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0',
    'GOOD_PACKET_INDICATOR_FIRST_MOMENT_DIRECT_THEOREM_FOUND=false',
    'AP_DISTRIBUTION_TO_POSITIVE_INDICATOR_ADAPTER_PROVED=false',
    'VARIANCE_TO_POSITIVE_INDICATOR_ADAPTER_PROVED=false',
]:
    assert token in q22, token
    assert token in qsum, token

assert 'M1_G' in s144
assert 'M2_G' in s145
assert 'Q22_THEOREM_TARGET_NOW_STABLE=true' in s146

# Finite-model sanity: second moment bounded by max occupancy times first moment.
a = [0, 1, 3, 2, 0, 4]
m1 = sum(a)
m2 = sum(x*x for x in a)
assert m2 <= max(a) * m1

print('Stage14-Work-cjX48/q22 deterministic audit: PASS')
