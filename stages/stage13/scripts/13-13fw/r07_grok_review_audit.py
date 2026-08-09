#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
grok = (ROOT / 'stages/stage13/13-13fw/grok-r07-verdict.md').read_text()
claude = (ROOT / 'stages/stage13/13-13fw/claude-r07-verdict.md').read_text()
deepseek = (ROOT / 'stages/stage13/13-13fw/deepseek-r07-verdict.md').read_text()
result = (ROOT / 'stages/stage13/13-13fw/result.md').read_text()

for token in [
    'GROK_R07_VERDICT=CLOSED',
    'GROK_R07_CLOSED_VOTE_COUNTED=true',
    'GROK_R07_GATE_A=PASS',
    'GROK_R07_GATE_B=PASS',
    'GROK_R07_GATE_C=PASS',
    'GROK_R07_GATE_D=PASS',
    'R08_REQUIRED=true',
    'PROMOTE_TO_13_13G=false',
]:
    assert token in grok, token

assert 'CLAUDE_R07_VERDICT=OPEN' in claude
assert 'QR0_UNDEFINED=ACCEPTED' in claude
assert 'DEEPSEEK_R07_VERDICT=CLOSED' in deepseek
assert 'DEEPSEEK_R07_CLOSED_VOTE_COUNTED=true' in deepseek

for token in [
    'R07_EXTERNAL_REVIEWS_RECORDED=3',
    'CLAUDE_R07_VERDICT=OPEN',
    'GROK_R07_VERDICT=CLOSED',
    'DEEPSEEK_R07_VERDICT=CLOSED',
    'R07_INDEPENDENT_CLOSED_VERDICTS=2',
    'R07_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2',
    'R07_MATHEMATICAL_REVIEW_THRESHOLD_MET=true',
    'R07_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0',
    'R07_UNRESOLVED_SELF_CONTAINED_BLOCKERS=2',
    'R08_REQUIRED=true',
    'PROMOTE_TO_13_13G=false',
    'NEXT=13-13fx',
]:
    assert token in result, token

# CLOSED votes cannot erase independently accepted review-target blockers.
assert 'R07_QR0_UNDEFINED_BLOCKER=true' in result
assert 'R07_FULL_JACOBI_SUM_EMBED_BLOCKER=true' in result

print('Stage13-13fw Grok/DeepSeek integrated R07 review audit: PASS')
