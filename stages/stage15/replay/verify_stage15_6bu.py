from pathlib import Path
p=Path('stages/stage15/15-6bu/result.md').read_text()
assert 'RAW_HEIGHT_FACTORIZATION=true' in p and 'ELEMENTARY_B_OVER_Q_PROVED=false' in p
