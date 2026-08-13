from pathlib import Path
base=Path('stages/stage15')
ce=(base/'15-6ce/result.md').read_text()
cf=(base/'15-6cf/result.md').read_text()
cg=(base/'15-6cg/result.md').read_text()
assert 'POINTWISE_STRUCTURAL_DOMINATION_TESTED=true' in ce
assert 'POINTWISE_STRUCTURAL_DOMINATION_PROVED=false' in ce
for token in [
    'PHYSICAL_DIVISOR_SWITCH_EXACT=true',
    'COMPLEMENTARY_COFACTORS_DEFINED=true',
    'COMPLEMENTARY_MAP_BIJECTIVE=true',
    'PHI_WEIGHTS_EXACT_UNTIL_BOUND=true',
    'MULTIPLICITY_ONE=true',
    'PRIMITIVITY_PRESERVED=true',
    'PHYSICAL_R_LE_B_PRESERVED=true',
    'QUANTIFIER_ORDER_D0_FIRST=true',
    'RECOMBINATION_EXACT=true',
    'MEASURE_CORRECT=true',
    'NO_DOUBLE_CHARGE=true',
]:
    assert token in cf
assert 'REPAIRED_RECEIVER=true' in cg
assert 'SPLIT_TRIGGER=false' in cg
assert 'AUDIT_REQUIRED=true' in cg and 'MERGE_ALLOWED=false' in cg
print('Stage15-6 main-batch ce-cg repaired: PASS')
