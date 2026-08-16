#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
MERGE_1038 = 'e94dd7652c1c60cc32617ff00240f67734d39bed'
AUDIT_1038 = 'e3644f3f7303137550b01058eb02c49110bf58c2'

cp = ROOT / 'stages/stage27/27-controller.json'
ctl = json.loads(cp.read_text(encoding='utf-8'))

r402a = ctl['derived_routes']['Stage27-19-r402a']
r402a.update({
    'status': 'INTERMEDIATE_AUDITED_PASS_MERGED',
    'audit_status': 'PASS',
    'audit_record': 'stages/stage27/27-19-r402a/audit.md',
    'pr': 1038,
    'audit_commit': AUDIT_1038,
    'merge_commit': MERGE_1038,
    'advance_to_checkpoint50': False,
    'continue_upper_exploration': True,
    'advance_allowed': True,
    'merge_allowed': True,
})

ctl['derived_routes']['Stage27-19-r402b'] = {
    'status': 'SUBMITTED_PENDING_FRESH_AUDIT',
    'trigger_checkpoint': 40,
    'route_serial': '19-r402b',
    'route_kind': 'UPPER_REENTRY',
    'source_stage': 'Stage19',
    'parent_route': 'Stage27-19-r402a',
    'purpose': 'separate pointwise fixed-tau genus-one sparsity from the uniform moving-tau max-fiber theorem and test whether fiber control alone can break the half-power wall',
    'fixed_tau_ambient_conic_derived': True,
    'fixed_tau_toric_equation_derived': True,
    'fixed_tau_stage19_fiber_genus': 1,
    'fixed_tau_physical_fiber_smooth': True,
    'fixed_tau_physical_to_genus_one_bounded_multiplicity': True,
    'fixed_tau_z_height_bound_proved': True,
    'fixed_tau_z_height_bound': 'H(z)<3B',
    'fixed_tau_u_height_bound_proved': True,
    'fixed_tau_u_height_bound': 'H(u)<5B^(3/2)',
    'pointwise_fixed_tau_subpower_proved': True,
    'pointwise_fixed_tau_bound': 'polylog_B_with_t_dependent_rank_and_constant',
    'pointwise_uniform_in_t': False,
    'tau_uniform_fiber_subpower_proved': False,
    'pointwise_to_uniform_promotion_forbidden': True,
    'fiber_alone_strict_subhalf_route_closed': True,
    'fiber_plus_strict_support_can_reopen': True,
    'strict_tau_support_still_required_for_max_fiber_route': True,
    'tau_weighted_second_moment_proved': False,
    'strict_sub_sqrt_upper_proved': False,
    'new_mu_lt_half_proved': False,
    'true_N2_exponent_identified': False,
    'audit_status': 'PENDING',
    'advance_to_checkpoint50': False,
    'continue_upper_exploration': True,
    'next_derived_route': '27-19-r402c',
    'advance_allowed': False,
    'merge_allowed': False,
}

ctl['status'] = 'OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402B_PENDING_AUDIT'
ctl['checkpoint_status']['40'] = 'UPPER_ATTACK_AUDITED_PASS_MERGED_WITH_R402A_AUDITED_PASS_MERGED_AND_R402B_PENDING_AUDIT'
ctl['checkpoint_status']['50'] = 'BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE'
ctl['state'] = {
    'CURRENT_CHECKPOINT': 40,
    'MAIN_STATUS': 'UPPER_REENTRY_STAGE27_19_R402B_SUBMITTED_PENDING_FRESH_AUDIT',
    'AUDIT_STATUS': 'PENDING',
    'ADVANCE_ALLOWED': False,
    'NEXT_CHECKPOINT': 40,
    'NEXT_STAGE': '',
    'NEW_INPUT_REQUIRED': False,
    'HUMAN_DECISION_REQUIRED': False,
    'MERGE_ALLOWED': False,
}
ctl['safety']['pointwise_fixed_tau_promoted_to_uniform_max_fiber'] = False
ctl['safety']['fixed_tau_fiber_subpower_promoted_to_strict_subhalf_without_support'] = False
ctl['next_expected_command'] = 'Stage27-19-r402-audit'
cp.write_text(json.dumps(ctl, indent=2) + '\n', encoding='utf-8')

sp = ROOT / 'docs/00_CURRENT_RESEARCH_STATUS.md'
s = sp.read_text(encoding='utf-8')
replacements = [
    ('CURRENT_STAGE=Stage27-19-r402a-SUBMITTED-PENDING-FRESH-AUDIT', 'CURRENT_STAGE=Stage27-19-r402b-SUBMITTED-PENDING-FRESH-AUDIT'),
    ('STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402A_PENDING_AUDIT', 'STAGE27_STATUS=OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R402B_PENDING_AUDIT'),
    ('STAGE27_19_R402A_STATUS=TAU_HEIGHT_SUPPORT_SUBMITTED_PENDING_FRESH_AUDIT', 'STAGE27_19_R402A_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1038\nSTAGE27_19_R402B_STATUS=FIXED_TAU_FIBER_SUBMITTED_PENDING_FRESH_AUDIT'),
    ('STAGE27_ACTIVE_UPPER_REENTRY=27-19-r402a', 'STAGE27_ACTIVE_UPPER_REENTRY=27-19-r402b'),
]
for old, new in replacements:
    if old in s:
        s = s.replace(old, new, 1)

fiber_markers = '''STAGE27_FIXED_TAU_AMBIENT_CONIC_DERIVED=true
STAGE27_FIXED_TAU_STAGE19_FIBER_GENUS=1
STAGE27_FIXED_TAU_Z_HEIGHT_BOUND=H_LT_3B
STAGE27_FIXED_TAU_U_HEIGHT_BOUND=H_LT_5B_3_OVER_2
STAGE27_POINTWISE_FIXED_TAU_SUBPOWER_PROVED=true
STAGE27_POINTWISE_FIXED_TAU_UNIFORM_IN_T=false
STAGE27_FIBER_ALONE_STRICT_SUBHALF_ROUTE_CLOSED=true
'''
anchor = 'STAGE27_TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false\n'
if 'STAGE27_POINTWISE_FIXED_TAU_SUBPOWER_PROVED=true' not in s:
    if anchor not in s:
        raise SystemExit('missing tau uniform fiber anchor')
    s = s.replace(anchor, fiber_markers + anchor, 1)

op = s.find('## Current operation')
if op < 0:
    raise SystemExit('missing Current operation section')
s = s[:op] + '''## Current operation

Stage27-19-r402a passed hostile audit and PR #1038 merged at

```text
e94dd7652c1c60cc32617ff00240f67734d39bed
```

The reduced tau height theorem is accepted, but raw height/cardinality did not prove `sigma<1/2`. Stage27-19-r402b therefore audits fixed-tau physical fibers.

For reduced `tau=p/q>0`, the ambient two-face fiber is exactly

```text
p*y^2-q*x^2=p+q
p*n^2*(r^2-s^2)=q*s^2*(m^2+n^2).
```

Adding the Stage19 integral-space condition gives the already-audited smooth genus-one fiber `C_tau`. The physical cutoff yields coarse fiber-coordinate bounds

```text
H(z)<3B
H(u)<5B^(3/2).
```

Therefore for every fixed rational `t>0`, standard Mordell-Weil/Neron-Tate lattice counting gives a pointwise bound

```text
w_B(t) <<_t (1+log B)^(rank(E_t(Q))/2) = B^(o_t(1)).
```

This is not uniform as `t` moves with `B`; rank and height-lattice constants may vary. No theorem upgrades it to `max_t w_B(t)=B^o(1)`. Moreover even a hypothetical uniform subpower max-fiber would only reproduce the inherited half-power bound while the best tau-support upper remains `B^(1/2+epsilon)`. Thus the fiber-alone shortcut is closed at the present support boundary; it can reopen jointly with a strict horizontal support theorem.

The next r402-native object is the exact same-tau collision energy, route `27-19-r402c`.

```text
TASK_ID=Stage27-19-r402b
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
PARENT_R402A_AUDITED_PASS_MERGED=true
FIXED_TAU_AMBIENT_CONIC_DERIVED=true
FIXED_TAU_STAGE19_FIBER_GENUS=1
FIXED_TAU_Z_HEIGHT_BOUND=H(z)<3B
FIXED_TAU_U_HEIGHT_BOUND=H(u)<5B^(3/2)
POINTWISE_FIXED_TAU_SUBPOWER_PROVED=true
POINTWISE_FIXED_TAU_UNIFORM_IN_T=false
TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
FIBER_ALONE_STRICT_SUBHALF_ROUTE_CLOSED=true
TAU_WEIGHTED_SECOND_MOMENT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEXT_DERIVED_ROUTE=27-19-r402c
NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit
```
'''
sp.write_text(s, encoding='utf-8')
