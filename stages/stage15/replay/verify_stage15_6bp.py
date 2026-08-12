from pathlib import Path
p=Path('stages/stage15/15-6bp/result.md').read_text()
assert 'NEIGHBOURHOOD_EXPONENT=10' in p and 'AUDIT_VERDICT=BLOCK' in p
