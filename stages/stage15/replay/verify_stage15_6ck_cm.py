from pathlib import Path
base=Path('stages/stage15')
ck=(base/'15-6ck/result.md').read_text()
cl=(base/'15-6cl/result.md').read_text()
cm=(base/'15-6cm/result.md').read_text()
assert 'EXACT_PHI_RESUMMATION_TESTED=true' in ck
assert 'PHI_RESUMMATION_ALONE_SOFTENS_LEVEL=false' in ck
assert 'COMPLEMENTARY_VOLUME_SHRINK=D0^-2' in cl
assert 'WEIGHTED_COUNT_DECAY_PROVED=false' in cl
assert 'COUPLED_OPTIMIZATION_RECOMPUTED=true' in cm
assert 'POLYNOMIAL_OVERLAP_WINDOW_PROVED=false' in cm
assert 'SPLIT_TRIGGER=false' in cm
assert 'AUDIT_REQUIRED=true' in cm and 'MERGE_ALLOWED=false' in cm
print('Stage15-6 main-batch ck-cm: PASS')
