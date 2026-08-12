from pathlib import Path
p=Path('stages/stage15/15-6bt/result.md').read_text()
assert 'AUDIT_VERDICT=BLOCK' in p and 'QUANTITATIVE_SELBERG_THEOREM_APPLICABLE=false' in p
