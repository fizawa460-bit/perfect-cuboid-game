from pathlib import Path
base=Path('stages/stage15')
ch=(base/'15-6ch/result.md').read_text()
ci=(base/'15-6ci/result.md').read_text()
cj=(base/'15-6cj/result.md').read_text()
assert 'SMALL_RANGE_QUANTIFIED=true' in ch
assert 'EXACT_PHI_SUM_START=true' in ch
assert 'LARGE_RANGE_EXACT_RECEIVER=true' in ci
assert 'INVERSE_D0_DECAY_PROVED=false' in ci
assert 'COUPLED_OPTIMIZATION_AUDITED=true' in cj
assert 'POLYNOMIAL_D0_OPTIMIZATION_LEGAL=false' in cj
assert 'SPLIT_TRIGGER=false' in cj
assert 'AUDIT_REQUIRED=true' in cj and 'MERGE_ALLOWED=false' in cj
print('Stage15-6 main-batch ch-cj: PASS')
