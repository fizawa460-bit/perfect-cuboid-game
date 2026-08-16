#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
MERGE_1037 = '77dc7bc7eb29f4113d59c8255ab4b2148bd52690'
AUDIT_1037 = '30639268257f7aada044ed44c9897d19dc418322'

cp = ROOT / 'stages/stage27/27-controller.json'
ctl = json.loads(cp.read_text(encoding='utf-8'))

r402 = ctl['derived_routes']['Stage27-19-r402']
r402.update({
    'status': 'INTERMEDIATE_AUDITED_PASS_MERGED',
    'audit_status': 'PASS',
    'audit_record': 'stages/stage27/27-19-r402/audit.md',
    'pr': 1037,
    'audit_commit': AUDIT_1037,
    'merge_commit': MERGE_1037,
    'advance_to_checkpoint50': False,
    'continue_upper_exploration': True,
    'advance_allowed': True,
    'merge_allowed': True,
})

ctl['derived_routes']['Stage27-19-r402a'] = {
    'status': 'SUBMITTED_PENDING_FRESH_AUDIT',
    'trigger_checkpoint': 40,
    'route_serial': '19-r402a',
    'route_kind': 'UPPER_REENTRY',
    'source_stage': 'Stage19',
    'parent_route': 'Stage27-19-r402',
    'purpose': 'quantify reduced tau height on R<=B and test whether physical-height/cardinality support counting alone gives sigma<1/2',
    'reduced_slope_pair_height_bound_proved': True,
    'm2_plus_n2_lt_2B': True,
    'r2_plus_s2_lt_2B': True,
    'tau_reduced_height_bound_proved': True,
    'tau_reduced_height_bound': 'H(tau)<2B^2',
    'tau_rational_height_count_exponent': 4,
    'tau_ambient_toric_count_exponent': 2,
    'tau_support_lower_exponent': '1/4',
    'tau_best_certified_support_upper': '1/2+epsilon',
    'tau_support_strict_subhalf_proved': False,
    'tau_support_exponent_identified': False,
    'height_only_support_route_closed': True,
    'tau_uniform_fiber_subpower_proved': False,
    'tau_weighted_second_moment_proved': False,
    'strict_sub_sqrt_upper_proved': False,
    'new_mu_lt_half_proved': False,
    'true_N2_exponent_identified': False,
    'audit_status': 'PENDING',
    'advance_to_checkpoint50': False,
    'continue_upper_exploration': True,
    'next_derived_route': '27-19-r402b',
    'advance_allowed': False,
    'merge_allowed': False,
}

ctl['status'] = 'OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402A_PENDING_AUDIT'
ctl['checkpoint_status']['40'] = 'UPPER_ATTACK_AUDITED_PASS_MERGED_WITH_R402_AUDITED_PASS_MERGED_AND_R402A_PENDING_AUDIT'
ctl['checkpoint_status']['50'] = 'BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE'
ctl['state'] = {
    'CURRENT_CHECKPOINT': 40,
    'MAIN_STATUS': 'UPPER_REENTRY_STAGE27_19_R402A_SUBMITTED_PENDING_FRESH_AUDIT',
    'AUDIT_STATUS': 'PENDING',
    'ADVANCE_ALLOWED': False,
    'NEXT_CHECKPOINT': 40,
    'NEXT_STAGE': '',
    'NEW_INPUT_REQUIRED': False,
    'HUMAN_DECISION_REQUIRED': False,
    'MERGE_ALLOWED': False,
}
ctl['safety']['tau_height_bound_promoted_to_strict_support_saving'] = False
ctl['safety']['ambient_toric_cardinality_promoted_to_survivor_support_saving'] = False
ctl['next_expected_command'] = 'Stage27-19-r402-audit'
cp.write_text(json.dumps(ctl, indent=2) + '\n', encoding='utf-8')

sp = ROOT / 'docs/00_CURRENT_RESEARCH_STATUS.md'
s = sp.read_text(encoding='utf-8')
replacements = [
    ('CURRENT_STAGE=Stage27-19-r402-SUBMITTED-PENDING-FRESH-AUDIT', 'CURRENT_STAGE=Stage27-19-r402a-SUBMITTED-PENDING-FRESH-AUDIT'),
    ('STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402_PENDING_AUDIT', 'STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402A_PENDING_AUDIT'),
    ('STAGE27_19_R402_STATUS=TAU_PUSHFORWARD_UPPER_SUBMITTED_PENDING_FRESH_AUDIT', 'STAGE27_19_R402_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1037\nSTAGE27_19_R402A_STATUS=TAU_HEIGHT_SUPPORT_SUBMITTED_PENDING_FRESH_AUDIT'),
    ('STAGE27_ACTIVE_UPPER_REENTRY=27-19-r402', 'STAGE27_ACTIVE_UPPER_REENTRY=27-19-r402a'),
]
for old, new in replacements:
    if old in s:
        s = s.replace(old, new, 1)

height_markers = '''STAGE27_TAU_REDUCED_HEIGHT_BOUND_PROVED=true
STAGE27_TAU_REDUCED_HEIGHT_BOUND=H_LT_2B2
STAGE27_TAU_RATIONAL_HEIGHT_COUNT_EXPONENT=4
STAGE27_TAU_AMBIENT_TORIC_COUNT_EXPONENT=2
STAGE27_TAU_BEST_CERTIFIED_SUPPORT_UPPER=1/2_PLUS_EPSILON
STAGE27_HEIGHT_ONLY_SUPPORT_ROUTE_CLOSED=true
'''
anchor = 'STAGE27_TAU_SUPPORT_STRICT_SUBHALF_PROVED=false\n'
if 'STAGE27_TAU_REDUCED_HEIGHT_BOUND_PROVED=true' not in s:
    if anchor not in s:
        raise SystemExit('missing tau support anchor')
    s = s.replace(anchor, height_markers + anchor, 1)

op = s.find('## Current operation')
if op < 0:
    raise SystemExit('missing Current operation section')
s = s[:op] + '''## Current operation

Stage27-19-r402 passed hostile audit and PR #1037 merged at

```text
77dc7bc7eb29f4113d59c8255ab4b2148bd52690
```

The accepted tau pushforward has polynomial realized support, but no strict support upper theorem or strict sub-square-root theorem. The next derived route `Stage27-19-r402a` quantifies reduced tau height on the exact physical cutoff.

For reduced positive toric representatives, the shared-edge face identities and `G<=4rs`, `G<=4mn` imply

```text
m^2+n^2 < 2B
r^2+s^2 < 2B
n^2 < B
s^2 < B
```

on `R<=B`. Hence for reduced `tau=p/q`,

```text
H(tau)=max(p,q) < 2B^2.
```

This height theorem does not yield a useful support saving: rational-height counting gives only `O(B^4)` and direct ambient toric pair counting gives only `O(B^2)`, both weaker than the inherited tautological `#T(B)<=N2(B)<<_eps B^(1/2+eps)`. Thus no `sigma<1/2` is obtained from height/cardinality alone. The audited support corridor is currently `B^(1/4) << #T(B) <<_eps B^(1/2+eps)`.

The height-only support route is closed in this scoped sense. The next candidate after audit is fixed-tau physical fiber counting `27-19-r402b`.

```text
TASK_ID=Stage27-19-r402a
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
PARENT_R402_AUDITED_PASS_MERGED=true
TAU_REDUCED_HEIGHT_BOUND_PROVED=true
TAU_REDUCED_HEIGHT_BOUND=H(tau)<2B^2
TAU_SUPPORT_LOWER_EXPONENT=1/4
TAU_BEST_CERTIFIED_SUPPORT_UPPER=1/2_PLUS_EPSILON
TAU_SUPPORT_STRICT_SUBHALF_PROVED=false
HEIGHT_ONLY_SUPPORT_ROUTE_CLOSED=true
TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
TAU_WEIGHTED_SECOND_MOMENT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEXT_DERIVED_ROUTE=27-19-r402b
NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit
```
'''
sp.write_text(s, encoding='utf-8')
