from pathlib import Path
base=Path('stages/stage15')
cn=(base/'15-6cn/result.md').read_text()
co=(base/'15-6co/result.md').read_text()
cp=(base/'15-6cp/result.md').read_text()
assert 'POLYNOMIAL_WINDOW_CONDITION=theta*(beta+2)<delta' in cn
assert 'ELEMENTARY_LATTICE_DELTA_PROVED=false' in cn
assert 'RAW_HEIGHT_POINTWISE_DOMINATION=false' in co
assert 'COUNTERSCALING=n=s=1,m=r=T' in co
assert 'CONDITIONAL_OVERLAP_WINDOW=0<theta<delta/(beta+2)' in cp
assert 'POLYNOMIAL_OVERLAP_WINDOW_CERTIFIED=false' in cp
assert 'SPLIT_TRIGGER=false' in cp
assert 'AUDIT_REQUIRED=true' in cp and 'MERGE_ALLOWED=false' in cp
print('Stage15-6 main-batch cn-cp: PASS')
