from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def text(rel):
    return (ROOT / rel).read_text()

r = text('stages/stage14/14-Work-cgX45/result.md')
s = text('stages/stage14/14-s7-137/result.md')
x = text('stages/stage14/14-Work-cfX44/result.md')
q17 = text('stages/stage14/archive/docs/q-research/stage14-q17-summary.md')
q20 = text('stages/stage14/archive/docs/q-research/stage14-q20-summary.md')

for token in [
    'CONDITIONED_KERNEL_MEASURE_FIREWALL_LEMMA_PROVED=true',
    'IDENTICAL_KERNEL_DOES_NOT_IMPLY_MEASURE_TRANSFER=true',
    'Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false',
    'Q21_NEEDED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
]:
    assert token in r, token

assert 'S_CONDITIONED_RECIPROCAL_CRT_DEFICIT_LEDGER_PROVED=true' in s
assert 'Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false' in s
assert 'SECOND_REVERSE_SELF_COUPLED_MODULUS_CANCELLATION_PROVED=true' in x
assert 'RECIPROCAL_CRT_SUPPORT_DIRECT_THEOREM_FOUND=false' in q17
assert 'CONDITIONED_SECOND_REVERSE_CORRELATION_DIRECT_THEOREM_FOUND=false' in q20

print('Stage14-Work-cgX45 conditioned measure firewall audit: PASS')
