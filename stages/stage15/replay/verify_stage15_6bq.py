from pathlib import Path
p=Path('stages/stage15/15-6bq/result.md').read_text()
assert '1/24' in p and 'AUDIT_VERDICT=PASS' in p
