#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
CTL = ROOT / 'stages/stage27/27-controller.json'
STATUS = ROOT / 'docs/00_CURRENT_RESEARCH_STATUS.md'
VERIFY = ROOT / 'stages/stage27/27-19-r401d/verify_27_19_r401d.py'

# 1. Canonical Stage27 controller lifecycle sync.
ctl = json.loads(CTL.read_text(encoding='utf-8'))
ctl['status'] = 'OPEN_CHECKPOINT40_WITH_STAGE19_LOWER_REENTRY_R401D_REPAIR_PENDING_AUDIT'
ctl['checkpoint_status']['40'] = (
    'UPPER_ATTACK_AUDITED_PASS_MERGED_WITH_40AA_AE_AUDITED_PASS_MERGED_'
    'AND_27_19_R401_R401A_R401B_R401C_AUDITED_PASS_MERGED_AND_R401D_REPAIR_PENDING_AUDIT'
)

c = ctl['derived_routes']['Stage27-19-r401c']
c.update({
    'status': 'INTERMEDIATE_AUDITED_PASS_MERGED',
    'audit_status': 'PASS',
    'audit_record': 'stages/stage27/27-19-r401c/audit.md',
    'pr': 1035,
    'merge_commit': '4ca03c43f4ff2c858c51ac8959d6e75f077c6de7',
    'advance_to_checkpoint50': False,
    'continue_lower_exploration': True,
    'advance_allowed': True,
    'merge_allowed': True,
})

ctl['derived_routes']['Stage27-19-r401d'] = {
    'status': 'REPAIR_SUBMITTED_PENDING_FRESH_AUDIT',
    'trigger_checkpoint': 40,
    'route_serial': '19-r401d',
    'route_kind': 'LOWER_REENTRY',
    'source_stage': 'Stage19',
    'parent_route': 'Stage27-19-r401c',
    'purpose': 'calibrate audited R501/R502 quarter-power families inside the natural tau-fibration and freeze a bounded lower-reentry stopping rule',
    'r501_tau_embedding_proved': True,
    'r502_tau_embedding_proved': True,
    'r501_tau_projection_degree': 8,
    'r502_tau_projection_degree': 8,
    'r501_toric_degree_ledger': 'dx2_dy2_g0_h8',
    'r502_toric_degree_ledger': 'dx4_dy2_g4_h8',
    'r502_degree12_to_8_polynomial_cancellation_proved': True,
    'one_parameter_algebraic_progress_gate': '2dx+2dy-g<8',
    'lower_bounded_reentry_stop_candidate': True,
    'reopen_lower_on': 'NEW_H_LT_8_RATIONAL_CURVE_OR_STRONGER_CANCELLATION_OR_POLYNOMIALLY_THICKER_FAMILY',
    'preferred_post_audit_lane': 'UPPER_REENTRY',
    'next_upper_route': '27-40af',
    'lower_exponent_above_one_quarter_proved': False,
    'true_N2_exponent_identified': False,
    'previous_audit_verdict': 'FAIL',
    'mathematical_audit_status': 'PASS',
    'previous_fail_reason': 'CANONICAL_LIFECYCLE_SYNC_MISSING',
    'audit_record': 'stages/stage27/27-19-r401d/audit.md',
    'audit_status': 'PENDING',
    'pr': 1036,
    'advance_to_checkpoint50': False,
    'continue_lower_exploration': False,
    'advance_allowed': False,
    'merge_allowed': False,
}

ctl['state'].update({
    'CURRENT_CHECKPOINT': 40,
    'MAIN_STATUS': 'LOWER_REENTRY_STAGE27_19_R401D_REPAIR_SUBMITTED_PENDING_FRESH_AUDIT',
    'AUDIT_STATUS': 'PENDING',
    'ADVANCE_ALLOWED': False,
    'NEXT_CHECKPOINT': 40,
    'NEXT_STAGE': '',
    'NEW_INPUT_REQUIRED': False,
    'HUMAN_DECISION_REQUIRED': False,
    'MERGE_ALLOWED': False,
})
ctl['safety']['r401d_calibration_promoted_to_exponent_upgrade'] = False
ctl['next_expected_command'] = 'Stage27-19-r401-audit'
CTL.write_text(json.dumps(ctl, indent=2) + '\n', encoding='utf-8')

# 2. Human-readable canonical status sync.
text = STATUS.read_text(encoding='utf-8')
head, sep, _tail = text.partition('## Current operation')
lines = head.rstrip().splitlines()

def set_key(key, value, after_key=None):
    prefix = key + '='
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            lines[i] = prefix + value
            return
    insert_at = None
    if after_key:
        ap = after_key + '='
        for i, line in enumerate(lines):
            if line.startswith(ap):
                insert_at = i + 1
                break
    if insert_at is None:
        for i, line in enumerate(lines):
            if line.startswith('NEXT_EXPECTED_COMMAND='):
                insert_at = i
                break
    if insert_at is None:
        insert_at = len(lines)
    lines.insert(insert_at, prefix + value)

set_key('CURRENT_STAGE', 'Stage27-19-r401d-REPAIR-SUBMITTED-PENDING-FRESH-AUDIT')
set_key('STAGE27_STATUS', 'OPEN_CHECKPOINT40_WITH_LOWER_REENTRY_R401D_REPAIR_PENDING_AUDIT')
set_key('STAGE27_19_R401C_STATUS', 'INTERMEDIATE_AUDITED_PASS_MERGED_PR1035')
set_key('STAGE27_19_R401D_STATUS', 'R501_R502_CALIBRATION_REPAIR_SUBMITTED_PENDING_FRESH_AUDIT', 'STAGE27_19_R401C_STATUS')
set_key('STAGE27_R501_TAU_PROJECTION_DEGREE', '8', 'STAGE27_19_R401D_STATUS')
set_key('STAGE27_R502_TAU_PROJECTION_DEGREE', '8', 'STAGE27_R501_TAU_PROJECTION_DEGREE')
set_key('STAGE27_R502_DEGREE12_TO_8_POLYNOMIAL_CANCELLATION_ACCEPTED', 'true', 'STAGE27_R502_TAU_PROJECTION_DEGREE')
set_key('STAGE27_ONE_PARAMETER_ALGEBRAIC_PROGRESS_GATE', '2dx+2dy-g<8', 'STAGE27_R502_DEGREE12_TO_8_POLYNOMIAL_CANCELLATION_ACCEPTED')
set_key('STAGE27_LOWER_BOUNDED_REENTRY_STOP_CANDIDATE', 'true', 'STAGE27_ONE_PARAMETER_ALGEBRAIC_PROGRESS_GATE')
set_key('STAGE27_PREFERRED_POST_AUDIT_LANE', 'UPPER_REENTRY', 'STAGE27_LOWER_BOUNDED_REENTRY_STOP_CANDIDATE')
set_key('STAGE27_NEXT_UPPER_ROUTE', '27-40af', 'STAGE27_PREFERRED_POST_AUDIT_LANE')
set_key('STAGE27_LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED', 'false')
set_key('STAGE27_TRUE_N2_EXPONENT_IDENTIFIED', 'false')
set_key('NEXT_EXPECTED_COMMAND', 'Stage27-19-r401-audit')

operation = '''## Current operation

Stage27-19-r401c passed hostile audit and PR #1035 merged at

```text
4ca03c43f4ff2c858c51ac8959d6e75f077c6de7
```

Stage27-19-r401d then passed mathematical audit but failed overall only because the canonical lifecycle surfaces had not been synchronized. The mathematical calibration is retained: R501 and R502 both project to the natural `tau`-line with degree eight; R501 has toric ledger `dx2_dy2_g0_h8`, while R502 has `dx4_dy2_g4_h8` via the exact degree-four common factor `4mn(m^2+3n^2)`.

This repair registers r401d canonically and keeps checkpoint40 open. It does not improve the lower exponent beyond `1/4`, does not identify the true exponent, and does not advance to checkpoint50. The bounded lower-reentry stopping rule remains a candidate pending fresh audit; if accepted, the preferred next lane is upper reentry `27-40af`.

```text
TASK_ID=Stage27-19-r401d
CHECKPOINT=40
ROUTE_KIND=LOWER_REENTRY
PARENT_R401C_AUDITED_PASS_MERGED=true
R501_TAU_EMBEDDING_PROVED=true
R502_TAU_EMBEDDING_PROVED=true
R501_TAU_PROJECTION_DEGREE=8
R502_TAU_PROJECTION_DEGREE=8
R501_TORIC_DEGREE_LEDGER=dx2_dy2_g0_h8
R502_TORIC_DEGREE_LEDGER=dx4_dy2_g4_h8
R502_DEGREE12_TO_8_POLYNOMIAL_CANCELLATION_PROVED=true
ONE_PARAMETER_ALGEBRAIC_PROGRESS_GATE=2dx+2dy-g<8
LOWER_BOUNDED_REENTRY_STOP_CANDIDATE=true
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PREVIOUS_AUDIT_VERDICT=FAIL
MATHEMATICAL_AUDIT=PASS
PREVIOUS_FAIL_REASON=CANONICAL_LIFECYCLE_SYNC_MISSING
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
PREFERRED_POST_AUDIT_LANE=UPPER_REENTRY
NEXT_UPPER_ROUTE=27-40af
NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit
```
'''
STATUS.write_text('\n'.join(lines).rstrip() + '\n\n' + operation, encoding='utf-8')

# 3. Extend the dedicated verifier so SUCCESS cannot miss canonical lifecycle drift again.
v = VERIFY.read_text(encoding='utf-8')
marker = '# Canonical lifecycle synchronization after first hostile audit.'
if marker not in v:
    block = r'''

# Canonical lifecycle synchronization after first hostile audit.
ctl = data('stages/stage27/27-controller.json')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')
self_audit = text('stages/stage27/27-19-r401d/audit.md')
assert 'MATHEMATICAL_AUDIT=PASS' in self_audit
assert 'FAIL_REASON=CANONICAL_LIFECYCLE_SYNC_MISSING' in self_audit

pc = ctl['derived_routes']['Stage27-19-r401c']
pd = ctl['derived_routes']['Stage27-19-r401d']
assert pc['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert pc['audit_status'] == 'PASS'
assert pc['pr'] == 1035
assert pc['merge_commit'] == '4ca03c43f4ff2c858c51ac8959d6e75f077c6de7'
assert pd['status'] == 'REPAIR_SUBMITTED_PENDING_FRESH_AUDIT'
assert pd['r501_tau_projection_degree'] == 8
assert pd['r502_tau_projection_degree'] == 8
assert pd['r501_toric_degree_ledger'] == 'dx2_dy2_g0_h8'
assert pd['r502_toric_degree_ledger'] == 'dx4_dy2_g4_h8'
assert pd['r502_degree12_to_8_polynomial_cancellation_proved'] is True
assert pd['one_parameter_algebraic_progress_gate'] == '2dx+2dy-g<8'
assert pd['lower_bounded_reentry_stop_candidate'] is True
assert pd['previous_audit_verdict'] == 'FAIL'
assert pd['mathematical_audit_status'] == 'PASS'
assert pd['audit_status'] == 'PENDING'
assert pd['advance_to_checkpoint50'] is False
assert pd['merge_allowed'] is False
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-19-r401-audit'
assert 'CURRENT_STAGE=Stage27-19-r401d-REPAIR-SUBMITTED-PENDING-FRESH-AUDIT' in status
assert 'STAGE27_19_R401C_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1035' in status
assert 'STAGE27_19_R401D_STATUS=R501_R502_CALIBRATION_REPAIR_SUBMITTED_PENDING_FRESH_AUDIT' in status
assert 'STAGE27_NEXT_UPPER_ROUTE=27-40af' in status
'''
    anchor = "print('STAGE27_19_R401D_PARENT_AUDIT=PASS')"
    assert anchor in v
    v = v.replace(anchor, block + '\n' + anchor)
    VERIFY.write_text(v, encoding='utf-8')

print('STAGE27_19_R401D_CANONICAL_LIFECYCLE_SYNC=READY')
