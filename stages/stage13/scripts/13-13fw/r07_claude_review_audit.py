#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
verdict = (ROOT / 'stages/stage13/13-13fw/claude-r07-verdict.md').read_text()
plan = (ROOT / 'stages/stage13/13-13fw/r08-repair-plan.md').read_text()
result = (ROOT / 'stages/stage13/13-13fw/result.md').read_text()
proof = (ROOT / 'stages/stage13/13-13fu/stage13-r07-canonical-proof.md').read_text()

# The R07 source really uses QR_0 without an explicit set definition.
assert 'QR_0(\\mathbf F_p)' in proof
assert 'QR_0(\\mathbf F_p):=' not in proof

# The final unit-count chain is present, but R08 must inline the full S_i reduction.
assert '|\\Omega^W_{p,U}|' in proof
assert '\\frac{(p+1)^2}{2}' in proof

required_verdict = [
    'CLAUDE_R07_VERDICT=OPEN',
    'QR0_UNDEFINED=ACCEPTED',
    'JACOBI_SUM_SELF_CONTAINED_BLOCKER=ACCEPTED',
    'R07_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0',
    'R07_UNRESOLVED_SELF_CONTAINED_BLOCKERS=2',
    'R08_REQUIRED=true',
]
for token in required_verdict:
    assert token in verdict, token

required_plan = [
    'QR_0(\\mathbf F_p):=\\{t^2:t\\in\\mathbf F_p\\}',
    'S3=A+B-C-D=-2',
    'R08_FULL_JACOBI_SUM_EMBED_REQUIRED=true',
    'R08_THEOREM_CHANGE_REQUIRED=false',
]
for token in required_plan:
    assert token in plan, token

required_result = [
    'STAGE13_13FW=COMPLETE_R07_CLAUDE_REVIEW_ADJUDICATION',
    'R07_INDEPENDENT_CLOSED_VERDICTS=0',
    'R07_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0',
    'R07_UNRESOLVED_SELF_CONTAINED_BLOCKERS=2',
    'THEOREM_CHANGED=false',
    'NEXT=13-13fx',
]
for token in required_result:
    assert token in result, token

# Claude's p=3 sanity check under the intended definition.
p = 3
alpha = (p + 1) / (2 * (p - 1))
lam = (p + 5) / (2 * (p + 1))
assert alpha == 1
assert lam == 1

print('Stage13-13fw Claude R07 review audit: PASS')
