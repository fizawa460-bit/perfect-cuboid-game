#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
AUDIT_1039 = 'e3c93fae20a98ccedf0d5ec974dc18aa0ef6c9fc'
MERGE_1039 = 'f70d5313cd3eb148d2fdcb99f5d573bd14e91f5e'

cp = ROOT / 'stages/stage27/27-controller.json'
ctl = json.loads(cp.read_text(encoding='utf-8'))

b = ctl['derived_routes']['Stage27-19-r402b']
b.update({
    'status': 'INTERMEDIATE_AUDITED_PASS_MERGED',
    'audit_status': 'PASS',
    'audit_record': 'stages/stage27/27-19-r402b/audit.md',
    'pr': 1039,
    'audit_commit': AUDIT_1039,
    'merge_commit': MERGE_1039,
    'advance_to_checkpoint50': False,
    'continue_upper_exploration': True,
    'advance_allowed': True,
    'merge_allowed': True,
})

common = {
    'status': 'BATCH_SUBMITTED_PENDING_FRESH_AUDIT',
    'trigger_checkpoint': 40,
    'route_kind': 'UPPER_REENTRY',
    'source_stage': 'Stage19',
    'audit_status': 'PENDING',
    'advance_to_checkpoint50': False,
    'continue_upper_exploration': True,
    'advance_allowed': False,
    'merge_allowed': False,
    'strict_sub_sqrt_upper_proved': False,
    'new_mu_lt_half_proved': False,
    'true_N2_exponent_identified': False,
    'batch_audit_group': 'Stage27-19-r402c-f',
}

ctl['derived_routes']['Stage27-19-r402c'] = {
    **common,
    'route_serial': '19-r402c',
    'parent_route': 'Stage27-19-r402b',
    'purpose': 'separate reduced tau primitive pair from the common integer core and derive the exact core-height tradeoff',
    'reduced_tau_core_scale_derived': True,
    'tau_core_equations_proved': True,
    'tau_core_height_tradeoff_proved': True,
    'tau_core_height_bound': 'g<2B^2/H(tau)',
    'core_tradeoff_fixed_power_saving_proved': False,
    'next_derived_route': '27-19-r402d',
}
ctl['derived_routes']['Stage27-19-r402d'] = {
    **common,
    'route_serial': '19-r402d',
    'parent_route': 'Stage27-19-r402c',
    'purpose': 'separate diagonal and off-diagonal tau collision energy and identify the diagonal barrier at the current half-power support boundary',
    'tau_full_energy_identity_proved': True,
    'tau_full_energy_identity': 'E_tau=N2+C_tau',
    'tau_energy_diagonal_lower_bound_proved': True,
    'tau_energy_diagonal_lower_bound': 'E_tau>=N2',
    'raw_second_moment_shortcut_closed_at_halfwall': True,
    'offdiagonal_collision_route_remains': True,
    'next_derived_route': '27-19-r402e',
}
ctl['derived_routes']['Stage27-19-r402e'] = {
    **common,
    'route_serial': '19-r402e',
    'parent_route': 'Stage27-19-r402d',
    'purpose': 'derive an exact support plus off-diagonal collision hybrid upper gate and heavy-fiber exceptional-mass interfaces',
    'tau_hybrid_bound_proved': True,
    'tau_hybrid_bound': 'N<=S+sqrt(S*C)',
    'tau_hybrid_exponent': 'max(sigma,(sigma+kappa)/2)',
    'tau_hybrid_strict_subhalf_gate': 'sigma<1/2_and_sigma+kappa<1',
    'tau_heavy_fiber_interfaces_proved': True,
    'offdiagonal_alone_breaks_halfwall': False,
    'next_derived_route': '27-19-r402f',
}
ctl['derived_routes']['Stage27-19-r402f'] = {
    **common,
    'route_serial': '19-r402f',
    'parent_route': 'Stage27-19-r402e',
    'purpose': 'combine tau height bands, the core-height tradeoff, and off-diagonal collision control into a uniform dyadic strict-subhalf restart contract',
    'tau_dyadic_height_decomposition_proved': True,
    'tau_band_core_tradeoff_proved': True,
    'tau_band_hybrid_bound_proved': True,
    'tau_band_hybrid_bound': 'N_T<=S_T+sqrt(S_T*C_T)',
    'tau_band_strict_subhalf_contract_materialized': True,
    'tau_band_strict_subhalf_theorem_proved': False,
    'batch_stop_reason': 'EXACT_ARITHMETIC_REPRESENTATION_THEOREM_REQUIRED',
    'next_derived_route': '27-19-r402g',
}

ctl['status'] = 'OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402C_F_BATCH_PENDING_AUDIT'
ctl['checkpoint_status']['40'] = 'UPPER_ATTACK_AUDITED_PASS_MERGED_WITH_R402B_AUDITED_PASS_MERGED_AND_R402C_F_BATCH_PENDING_AUDIT'
ctl['checkpoint_status']['50'] = 'BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE'
ctl['state'] = {
    'CURRENT_CHECKPOINT': 40,
    'MAIN_STATUS': 'UPPER_REENTRY_STAGE27_19_R402C_F_BATCH_SUBMITTED_PENDING_FRESH_AUDIT',
    'AUDIT_STATUS': 'PENDING',
    'ADVANCE_ALLOWED': False,
    'NEXT_CHECKPOINT': 40,
    'NEXT_STAGE': '',
    'NEW_INPUT_REQUIRED': False,
    'HUMAN_DECISION_REQUIRED': False,
    'MERGE_ALLOWED': False,
}
ctl['safety']['tau_core_tradeoff_promoted_to_fixed_power_saving'] = False
ctl['safety']['tau_full_energy_diagonal_ignored'] = False
ctl['safety']['tau_offdiagonal_collision_promoted_without_support'] = False
ctl['safety']['tau_dyadic_restart_contract_promoted_to_theorem'] = False
ctl['next_expected_command'] = 'Stage27-19-r402-audit'
cp.write_text(json.dumps(ctl, indent=2) + '\n', encoding='utf-8')

sp = ROOT / 'docs/00_CURRENT_RESEARCH_STATUS.md'
s = sp.read_text(encoding='utf-8')
for old, new in [
    ('CURRENT_STAGE=Stage27-19-r402b-SUBMITTED-PENDING-FRESH-AUDIT', 'CURRENT_STAGE=Stage27-19-r402c-f-BATCH-SUBMITTED-PENDING-FRESH-AUDIT'),
    ('STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402B_PENDING_AUDIT', 'STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402C_F_BATCH_PENDING_AUDIT'),
    ('STAGE27_19_R402B_STATUS=FIXED_TAU_FIBER_SUBMITTED_PENDING_FRESH_AUDIT', 'STAGE27_19_R402B_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1039\nSTAGE27_19_R402C_F_STATUS=MULTI_ROUTE_BATCH_SUBMITTED_PENDING_FRESH_AUDIT'),
    ('STAGE27_ACTIVE_UPPER_REENTRY=27-19-r402b', 'STAGE27_ACTIVE_UPPER_REENTRY=27-19-r402c-f'),
]:
    if old not in s:
        raise SystemExit(f'missing status replacement anchor: {old}')
    s = s.replace(old, new, 1)

markers = '''STAGE27_TAU_CORE_SCALE_DERIVED=true
STAGE27_TAU_CORE_HEIGHT_TRADEOFF_PROVED=true
STAGE27_TAU_CORE_HEIGHT_BOUND=G_LT_2B2_OVER_H_TAU
STAGE27_TAU_FULL_ENERGY_IDENTITY_PROVED=true
STAGE27_TAU_FULL_ENERGY_DIAGONAL_BARRIER_PROVED=true
STAGE27_TAU_RAW_SECOND_MOMENT_SHORTCUT_CLOSED_AT_HALFWALL=true
STAGE27_TAU_OFFDIAGONAL_HYBRID_GATE_PROVED=true
STAGE27_TAU_OFFDIAGONAL_HYBRID_GATE=SIGMA_LT_HALF_AND_SIGMA_PLUS_KAPPA_LT_1
STAGE27_TAU_HEAVY_FIBER_INTERFACES_PROVED=true
STAGE27_TAU_DYADIC_BAND_CONTRACT_MATERIALIZED=true
STAGE27_TAU_DYADIC_BAND_THEOREM_PROVED=false
'''
anchor = 'STAGE27_TAU_WEIGHTED_SECOND_MOMENT_PROVED=false\n'
if 'STAGE27_TAU_CORE_HEIGHT_TRADEOFF_PROVED=true' not in s:
    if anchor not in s:
        raise SystemExit('missing status marker anchor')
    s = s.replace(anchor, markers + anchor, 1)

op = s.find('## Current operation')
if op < 0:
    raise SystemExit('missing Current operation')
s = s[:op] + '''## Current operation

Stage27-19-r402b passed hostile audit and PR #1039 merged at

```text
f70d5313cd3eb148d2fdcb99f5d573bd14e91f5e
```

Per operator direction, the next closely coupled subroutes are batched rather than audited one by one. `Stage27-19-r402c` through `r402f` form one checkpoint40 upper-reentry batch.

The batch proves the exact reduced-tau core decomposition

```text
A=s^2(m^2+n^2)=p*g
D=n^2(r^2-s^2)=q*g
g=gcd(A,D)
g < 2B^2/H(tau)
```

and then separates full collision energy into diagonal plus ordered off-diagonal parts,

```text
E_tau=N2+C_tau,
E_tau>=N2.
```

This shows that at the current half-power support boundary a raw full-second-moment estimate below half would already contain the desired theorem in its diagonal term; it is not a cheaper shortcut.

The useful refinement is the exact off-diagonal hybrid inequality

```text
N2 <= S + sqrt(S*C_tau).
```

Thus if `S<<B^(sigma+o(1))` and `C_tau<<B^(kappa+o(1))`, then

```text
mu <= max(sigma,(sigma+kappa)/2).
```

A sufficient strict-subhalf gate is `sigma<1/2` and `sigma+kappa<1`. The same inequality is localized to dyadic tau-height bands. Since `H(tau)<2B^2` there are only `O(log B)` bands, and on `T<=H(tau)<2T` the core satisfies `g<<B^2/T`.

No bandwise representation theorem meeting the strict gate is proved. The batch deliberately stops here because the next step is genuinely arithmetic: bound representations of the simultaneous core equations uniformly across dyadic `(H(tau),g)` ranges, or prove an equivalent support/off-diagonal-collision theorem.

```text
TASK_BATCH=Stage27-19-r402c-f
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MULTI_ROUTE_BATCH
PARENT_R402B_AUDITED_PASS_MERGED=true
TAU_CORE_HEIGHT_TRADEOFF_PROVED=true
TAU_FULL_ENERGY_DIAGONAL_BARRIER_PROVED=true
TAU_OFFDIAGONAL_HYBRID_GATE_PROVED=true
TAU_DYADIC_BAND_CONTRACT_MATERIALIZED=true
TAU_DYADIC_BAND_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_STATUS=PENDING_BATCH_FRESH_AUDIT
ADVANCE_ALLOWED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEXT_DERIVED_ROUTE_AFTER_AUDIT=27-19-r402g
NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit
```
'''
sp.write_text(s, encoding='utf-8')
