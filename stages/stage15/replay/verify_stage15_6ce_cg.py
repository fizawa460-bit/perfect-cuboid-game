from pathlib import Path
base=Path('stages/stage15')
ce=(base/'15-6ce/result.md').read_text()
cf=(base/'15-6cf/result.md').read_text()
cg=(base/'15-6cg/result.md').read_text()
assert 'POINTWISE_STRUCTURAL_DOMINATION_TESTED=true' in ce
assert 'POINTWISE_STRUCTURAL_DOMINATION_PROVED=false' in ce
assert 'PHYSICAL_DIVISOR_SWITCH_EXACT=true' in cf
assert 'MEASURE_CORRECT=true' in cf and 'NO_DOUBLE_CHARGE=true' in cf
assert 'TWO_NON_EQUIVALENT_LIVE_OBSTRUCTIONS=true' in cg
assert 'SPLIT_TRIGGER=true' in cg
assert 'AUDIT_REQUIRED=true' in cg and 'MERGE_ALLOWED=false' in cg
print('Stage15-6 main-batch ce-cg: PASS')
