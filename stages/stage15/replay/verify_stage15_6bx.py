from pathlib import Path
p=Path('stages/stage15/15-6bx/result.md').read_text()
assert 'AUDIT_VERDICT=NEW_GATE' in p and 'PHYSICAL_CHANNEL_GCD_PRODUCT_FIRST_MOMENT' in p
