from pathlib import Path
base=Path('stages/stage15')
by=(base/'15-6by/result.md').read_text()
bz=(base/'15-6bz/result.md').read_text()
ca=(base/'15-6ca/result.md').read_text()
assert 'EXACT_DIVISOR_EXPANSION=true' in by
assert 'MOVING_NORMALIZER_FIREWALL=true' in bz
assert 'INTERNAL_ROUTE_SEARCH=EXHAUSTED_FOR_CURRENT_NORMAL_FORM' in ca
assert 'AUDIT_REQUIRED=true' in ca and 'CODEX_REQUIRED=false' in ca
print('Stage15-6 main-batch by-ca: PASS')
