from pathlib import Path
p=Path('stages/stage15/15-6bv/result.md').read_text()
assert 'AUDIT_VERDICT=BLOCK' in p and 'CROSS_PROMOTION=false' in p
