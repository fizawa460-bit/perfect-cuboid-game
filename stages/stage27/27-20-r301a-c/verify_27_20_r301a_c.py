#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
a=(ROOT/'stages/stage27/27-20-r301a/result.md').read_text()
b=(ROOT/'stages/stage27/27-20-r301b/result.md').read_text()
c=(ROOT/'stages/stage27/27-20-r301c/result.md').read_text()
checks=[
('space cover', 'SPACE_DIAGONAL_DOUBLE_COVER_DERIVED=true' in a),
('branch class', 'SPACE_DIAGONAL_BRANCH_CLASS=-2K_Y' in a),
('k3 type', 'SPACE_DIAGONAL_K3_TYPE_PROVED=true' in a),
('same host', 'SAME_BASE_HOST=true' in b),
('same class', 'SAME_BRANCH_DIVISOR_CLASS=true' in b),
('not same divisor', 'SAME_BRANCH_DIVISOR=false' in b),
('no local transfer', 'STAGE20_LOCAL_DENSITIES_TRANSFER=false' in b),
('architecture only', 'SPACE_DIAGONAL_THIN_COVER_ARCHITECTURE_REUSABLE=true' in c),
('no direct theorem transfer', 'STAGE20_QUANTITATIVE_THEOREM_DIRECTLY_TRANSFERRED=false' in c),
('no strict upper', 'STRICT_SUB_SQRT_UPPER_PROVED=false' in c),
]
for name,ok in checks:
    assert ok, name
print('Stage27-20-r301a-c verifier PASS')
