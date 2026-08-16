#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
MERGE_1036 = 'b37bc86e045175238bf2520518b059574addc52b'

cp = ROOT / 'stages/stage27/27-controller.json'
ctl = json.loads(cp.read_text(encoding='utf-8'))

pd = ctl['derived_routes']['Stage27-19-r401d']
pd.update({
    'status': 'INTERMEDIATE_AUDITED_PASS_MERGED',
    'audit_status': 'PASS',
    'pr': 1036,
    'merge_commit': MERGE_1036,
    'mathematical_audit_status': 'PASS',
    'lower_bounded_reentry_stop_candidate': True,
    'advance_to_checkpoint50': False,
    'continue_lower_exploration': False,
    'advance_allowed': True,
    'merge_allowed': True,
})

ctl['derived_routes']['Stage27-19-r402'] = {
    'status': 'SUBMITTED_PENDING_FRESH_AUDIT',
    'trigger_checkpoint': 40,
    'route_serial': '19-r402',
    'route_kind': 'UPPER_REENTRY',
    'source_stage': 'Stage19',
    'parent_route': 'Stage27-19-r401d',
    'purpose': 'push the natural tau fibration forward as an outer physical label and derive exact support/fiber and collision-energy gates for a strict sub-square-root upper theorem',
    'tau_survivor_identity_proved': True,
    'tau_toric_formula_proved': True,
    'tau_defined_before_space_filter': True,
    'tau_outer_physical_rational_label': True,
    'tau_collision_receiver_derived': True,
    'r501_tau_projection_degree_used': 8,
    'r502_tau_projection_degree_used': 8,
    'tau_support_polynomial_lower_proved': True,
    'tau_support_lower_exponent': '1/4',
    'fixed_u_subpoly_class_obstruction_automatically_applies_to_tau': False,
    'tau_cardinality_alone_upper_saving': False,
    'tau_max_fiber_upper_gate': 'sigma+phi<1/2',
    'tau_second_moment_upper_gate': 'sigma+eta<1',
    'tau_support_strict_subhalf_proved': False,
    'tau_uniform_fiber_subpower_proved': False,
    'tau_weighted_second_moment_proved': False,
    'strict_sub_sqrt_upper_proved': False,
    'new_mu_lt_half_proved': False,
    'true_N2_exponent_identified': False,
    'audit_status': 'PENDING',
    'advance_to_checkpoint50': False,
    'continue_upper_exploration': True,
    'advance_allowed': False,
    'merge_allowed': False,
}
ctl['status'] = 'OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402_PENDING_AUDIT'
ctl['checkpoint_status']['40'] = 'UPPER_ATTACK_AUDITED_PASS_MERGED_WITH_DERIVED_ROUTES_THROUGH_R401D_AUDITED_PASS_MERGED_AND_R402_PENDING_AUDIT'
ctl['checkpoint_status']['50'] = 'BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE'
ctl['state'] = {
    'CURRENT_CHECKPOINT': 40,
    'MAIN_STATUS': 'UPPER_REENTRY_STAGE27_19_R402_SUBMITTED_PENDING_FRESH_AUDIT',
    'AUDIT_STATUS': 'PENDING',
    'ADVANCE_ALLOWED': False,
    'NEXT_CHECKPOINT': 40,
    'NEXT_STAGE': '',
    'NEW_INPUT_REQUIRED': False,
    'HUMAN_DECISION_REQUIRED': False,
    'MERGE_ALLOWED': False,
}
ctl['safety']['tau_cardinality_alone_promoted_to_power_saving'] = False
ctl['safety']['known_tau_support_lower_promoted_to_upper_support_bound'] = False
ctl['safety']['tau_fixed_u_class_obstruction_overgeneralized'] = False
ctl['next_expected_command'] = 'Stage27-19-r402-audit'
cp.write_text(json.dumps(ctl, indent=2) + '\n', encoding='utf-8')

sp = ROOT / 'docs/00_CURRENT_RESEARCH_STATUS.md'
s = sp.read_text(encoding='utf-8')
replacements = [
    ('CURRENT_STAGE=Stage27-19-r401d-REPAIR-SUBMITTED-PENDING-FRESH-AUDIT', 'CURRENT_STAGE=Stage27-19-r402-SUBMITTED-PENDING-FRESH-AUDIT'),
    ('STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_LOWER_REENTRY_R401D_REPAIR_PENDING_AUDIT', 'STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402_PENDING_AUDIT'),
    ('STAGE27_19_R401D_STATUS=R501_R502_CALIBRATION_REPAIR_SUBMITTED_PENDING_FRESH_AUDIT', 'STAGE27_19_R401D_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1036\nSTAGE27_19_R402_STATUS=TAU_PUSHFORWARD_UPPER_SUBMITTED_PENDING_FRESH_AUDIT'),
    ('STAGE27_LOWER_BOUNDED_REENTRY_STOP_CANDIDATE=true', 'STAGE27_LOWER_BOUNDED_REENTRY_STOP_ACCEPTED=true'),
    ('STAGE27_PREFERRED_POST_AUDIT_LANE=UPPER_REENTRY', 'STAGE27_LOWER_REENTRY_STATUS=BOUNDED_STOP_ACCEPTED'),
    ('STAGE27_NEXT_UPPER_ROUTE=27-40af', 'STAGE27_ACTIVE_UPPER_REENTRY=27-19-r402\nSTAGE27_40AF_STATUS=DEFERRED_BY_OPERATOR'),
    ('NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit', 'NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit'),
]
for old, new in replacements:
    if old in s:
        s = s.replace(old, new, 1)

tau_markers = '''STAGE27_TAU_SURVIVOR_IDENTITY_PROVED=true
STAGE27_TAU_TORIC_FORMULA_PROVED=true
STAGE27_TAU_DEFINED_BEFORE_SPACE_FILTER=true
STAGE27_TAU_OUTER_PHYSICAL_RATIONAL_LABEL=true
STAGE27_TAU_COLLISION_RECEIVER_DERIVED=true
STAGE27_TAU_SUPPORT_POLYNOMIAL_LOWER_PROVED=true
STAGE27_TAU_SUPPORT_LOWER_EXPONENT=1/4
STAGE27_TAU_MAX_FIBER_UPPER_GATE=sigma+phi<1/2
STAGE27_TAU_SECOND_MOMENT_UPPER_GATE=sigma+eta<1
STAGE27_TAU_SUPPORT_STRICT_SUBHALF_PROVED=false
STAGE27_TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
STAGE27_TAU_WEIGHTED_SECOND_MOMENT_PROVED=false
'''
anchor = 'STAGE27_STRICT_SUB_SQRT_UPPER_PROVED=false\n'
if 'STAGE27_TAU_SURVIVOR_IDENTITY_PROVED=true' not in s:
    if anchor not in s:
        raise SystemExit('missing strict upper status anchor')
    s = s.replace(anchor, tau_markers + anchor, 1)

op = s.find('## Current operation')
if op < 0:
    raise SystemExit('missing Current operation section')
s = s[:op] + '''## Current operation

Stage27-19-r401d passed fresh hostile re-audit and PR #1036 merged at

```text
b37bc86e045175238bf2520518b059574addc52b
```

The bounded lower reentry is frozen at the accepted quarter-power calibration boundary. The operator selected checkpoint40 Stage19 upper reentry `Stage27-19-r402` instead of immediately taking `27-40af`.

r402 reuses the audited natural `tau` fibration as an upper-side physical pushforward. On every Stage19 survivor,

```text
tau=(x^2-z^2)/(z^2-1)=(x^2+1)/(y^2-1)
   =s^2(m^2+n^2)/(n^2(r^2-s^2)).
```

The final toric expression is defined on the ambient positive two-face toric host before the integral-space filter. Using the audited R501/R502 calibration, the realized Stage19 tau support is already polynomial, at least `B^(1/4)` at exponent level. This prevents the fixed-U `B^o(1)` class-universe obstruction from automatically closing tau averaging, but cardinality alone is not credited as an upper saving.

```text
TASK_ID=Stage27-19-r402
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
PARENT_R401D_AUDITED_PASS_MERGED=true
TAU_SURVIVOR_IDENTITY_PROVED=true
TAU_TORIC_FORMULA_PROVED=true
TAU_DEFINED_BEFORE_SPACE_FILTER=true
TAU_COLLISION_RECEIVER_DERIVED=true
TAU_SUPPORT_POLYNOMIAL_LOWER_PROVED=true
TAU_SUPPORT_LOWER_EXPONENT=1/4
TAU_MAX_FIBER_UPPER_GATE=sigma+phi<1/2
TAU_SECOND_MOMENT_UPPER_GATE=sigma+eta<1
TAU_SUPPORT_STRICT_SUBHALF_PROVED=false
TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
TAU_WEIGHTED_SECOND_MOMENT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit
```
'''
sp.write_text(s, encoding='utf-8')
