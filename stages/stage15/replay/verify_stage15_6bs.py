from pathlib import Path
p=Path('stages/stage15/15-6bs/result.md').read_text()
assert 'AUDIT_VERDICT=NEW_GATE' in p and 'MULTIPLICATIVE_SIEVE' in p
