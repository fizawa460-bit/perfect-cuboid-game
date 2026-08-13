from pathlib import Path

base=Path('stages/stage15')
cw=(base/'15-6cw/result.md').read_text()
cx=(base/'15-6cx/result.md').read_text()
cy=(base/'15-6cy/result.md').read_text()

assert 'EXHAUSTIVE_VIEW_AUDIT=true' in cw
assert 'DIRECT_LATTICE=LIVE' in cw
assert 'DISPERSION=LIVE_UNTESTED' in cw
assert 'EXACT_RECONSTRUCTION=LIVE' in cw
assert 'LINEAR_FACTOR_SWITCH=UNTESTED' in cw

assert 'BLIND_REDISCOVERY=true' in cx
assert 'ROOT_RATIO_NORMALIZATION=true' in cx
assert 'DISCREPANCY_FORMULATION=true' in cx
assert 'EXACT_SURVIVOR_RECONSTRUCTION=LIVE_UNTESTED' in cx

assert 'EXHAUSTIVE_PROTOCOL_REPAIRED=true' in cy
assert 'LIVE_UNTESTED_CANDIDATES_PRESERVED=true' in cy
assert 'SELECTED_ROUTE=EXACT_SURVIVOR_RECONSTRUCTION_IN_CELL_NORMALIZED_ROOT_RATIOS' in cy
assert 'DISPERSION_ROUTE=LIVE_BACKUP' in cy
assert 'CONDITIONAL_BETA=-1' in cy
assert 'DELTA_PROVED=false' in cy
assert 'SIGMA_PROVED=false' in cy
assert 'SPLIT_TRIGGER=false' in cy
assert 'AUDIT_REQUIRED=true' in cy and 'MERGE_ALLOWED=false' in cy

print('Stage15-6 repair batch cw-cy: PASS')
