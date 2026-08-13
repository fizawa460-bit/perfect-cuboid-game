from pathlib import Path
base=Path('stages/stage15')
cq=(base/'15-6cq/result.md').read_text()
cr=(base/'15-6cr/result.md').read_text()
cs=(base/'15-6cs/result.md').read_text()
assert 'DYADIC_JOINT_LATTICE_EXPANSION=true' in cq
assert 'CONDITIONAL_BETA=-1' in cq
assert 'PRIMITIVE_NORMALIZER_REINSERTED=true' in cr
assert 'SIGMA_PROVED=false' in cr
assert 'DELTA_BETA_SIGMA_LEDGER_UPDATED=true' in cs
assert 'CONDITIONAL_OVERLAP_WINDOW=0<theta<delta' in cs
assert 'SPLIT_TRIGGER=false' in cs
assert 'AUDIT_REQUIRED=true' in cs and 'MERGE_ALLOWED=false' in cs
print('Stage15-6 main-batch cq-cs: PASS')
