from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[3]
S = ROOT / 'stages' / 'stage27'

w = (S / '27-20-r301w' / 'result.md').read_text()
x = (S / '27-20-r301x' / 'result.md').read_text()
y = (S / '27-20-r301y' / 'result.md').read_text()
reg = json.loads((S / '27-20-r301w-y' / 'batch-registry.json').read_text())
delta = json.loads((S / '27-20-r301w-y' / 'controller-sync-delta.json').read_text())
prev = json.loads((S / '27-20-r301t-v' / 'batch-registry.json').read_text())
prev_audit = (S / '27-20-r301t-v' / 'audit.md').read_text()
ctl = json.loads((S / '27-controller.json').read_text())

for text, route in [(w, 'W'), (x, 'X'), (y, 'Y')]:
    assert 'STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT' in text
    assert f'STAGE27_20_R301{route}_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT' in text
    assert 'STRICT_SUB_SQRT_UPPER_PROVED=false' in text
    assert 'NEW_MU_LT_HALF_PROVED=false' in text
    assert 'TRUE_N2_EXPONENT_IDENTIFIED=false' in text

assert 'CRITICAL_LOCAL_LEDGER_ALREADY_CHARGED=true' in w
assert 'STAGE14_LOCAL_LEDGER_INDEPENDENT_SUPPORT_SAVING=false' in w
assert 'STAGE14_HOST_SIEVE_MULTIPLIED_WITH_HALF_POWER=false' in w
assert 'TARGET_SPECIFIC_GROWING_MODULUS_DEFICIT_PROVED=false' in w
assert 'NEXT_DERIVED_ROUTE=27-20-r301x' in w

assert 'Q1_Q0_MOBIUS_BIJECTION_RETAINED=true' in x
assert 'NATURAL_Q0_COLLISION_MULTIPLICITY_LE_1=true' in x
assert 'NATURAL_Q0_COLLISION_ENERGY_EQUALS_SUPPORT=true' in x
assert 'NATURAL_Q0_OFFDIAGONAL_COLLISIONS=0' in x
assert 'NEXT_DERIVED_ROUTE=27-20-r301y' in x

# Exact Möbius inverse check on representative reduced rational slopes.
for q0 in [Fraction(1, 5), Fraction(2, 7), Fraction(3, 8), Fraction(4, 9)]:
    q1 = (1 + q0) / (1 - q0)
    assert q1 > 1
    assert (q1 - 1) / (q1 + 1) == q0

assert 'Q1_TO_Q0_PROJECTION_BIRATIONAL=true' in y
assert 'Q1_TO_Q0_SUPPORT_CARDINALITY_PRESERVED=true' in y
assert 'Q1_TO_J_PHYSICAL_MULTIPLICITY_BOUNDED=true' in y
assert 'Q1_AND_J_CRITICAL_SUPPORT_EXPONENTS_EQUAL=true' in y
assert 'EXISTING_PROJECTIONS_FIXED_POWER_SAVING_PROVED=false' in y
assert 'NEXT_DERIVED_ROUTE=27-20-r301z' in y

# Consume the final hostile-audit closeout rather than the stale global Stage20 entries.
assert prev['status'] == 'AUDITED_PASS_MERGED'
assert prev['audit_status'] == 'PASS'
assert prev['merge_allowed'] is True and prev['advance_allowed'] is True
assert prev['fresh_reaudit_required'] is False
assert prev['next_derived_route'] == '27-20-r301w'
assert 'AUDIT_VERDICT=PASS' in prev_audit

assert reg['status'] == 'BATCH_SUBMITTED_PENDING_FRESH_AUDIT'
assert reg['audit_status'] == 'PENDING'
assert reg['merge_allowed'] is False and reg['advance_allowed'] is False
assert reg['fresh_reaudit_required'] is True
assert reg['next_derived_route'] == '27-20-r301z'
assert reg['numbering_contract']['after_r301z'] == 'Stage27-20-r302-main-batch'
assert reg['numbering_contract']['r301aa_forbidden'] is True

# Parallel-lane firewall: preserve the live Stage19 lifecycle exactly as inherited from main.
live19 = ctl['derived_routes']['Stage27-19-r5aj-r5ak']
assert live19['status'] == 'BATCH_SUBMITTED_PENDING_FRESH_AUDIT'
assert live19['next_derived_route'] == '27-19-r5al'
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['NEXT_CHECKPOINT'] == 40
assert ctl['stage20_r301_numbering_contract']['after_r301z'] == 'Stage27-20-r302-main-batch'
assert ctl['stage20_r301_numbering_contract']['r301aa_forbidden'] is True

assert delta['consume_closeout']['audit_status'] == 'PASS'
assert delta['preserve_live_stage19']['route'] == 'Stage27-19-r5aj-r5ak'
assert delta['preserve_live_stage19']['do_not_overwrite_global_state'] is True
assert delta['stage20_route_updates']['Stage27-20-r301v'] == 'AUDITED_PASS_MERGED'
assert delta['stage20_route_updates']['Stage27-20-r301w'] == 'BATCH_SUBMITTED_PENDING_FRESH_AUDIT'
assert delta['stage20_next_derived_route'] == '27-20-r301z'

print('Stage27-20-r301w-y critical support weapon-audit verifier: PASS')
