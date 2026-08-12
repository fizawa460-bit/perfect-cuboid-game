from pathlib import Path
p=Path('stages/stage15/15-6bw/result.md').read_text()
assert 'CHANNEL_GCD_MAJORANT=q|G_S*G_O' in p and 'MARKOV_HIGH_CORE_REDUCTION=true' in p
