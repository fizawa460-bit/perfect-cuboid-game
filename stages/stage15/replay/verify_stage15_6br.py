from pathlib import Path
p=Path('stages/stage15/15-6br/result.md').read_text()
assert 'GEOMETRIC_SIEVE_SPECIES_MATCH=true' in p and 'AUDIT_VERDICT=BLOCK' in p
