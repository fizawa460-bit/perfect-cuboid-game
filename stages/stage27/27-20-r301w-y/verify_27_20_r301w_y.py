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
audit = (S / '27-20-r301w-y' / 'audit.md').read_text()
prev = json.loads((S / '27-20-r301t-v' / 'batch-registry.json').read_text())
prev_audit = (S / '27-20-r301t-v' / 'audit.md').read_text()
ctl = json.loads((S / '27-controller.json').read_text())

for text, route in [(w, 'W'), (x, 'X'), (y, 'Y')]:
    assert 'STATUS=AUDITED_PASS_MERGED' in text
    assert f'STAGE27_20_R301{route}_STATUS=AUDITED_PASS_MERGED' in text
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

assert prev['status'] == 'AUDITED_PASS_MERGED'
assert prev['audit_status'] == 'PASS'
assert prev['fresh_reaudit_required'] is False
assert 'AUDIT_VERDICT=PASS' in prev_audit

assert reg['status'] == 'AUDITED_PASS_MERGED'
assert reg['audit_status'] == 'PASS'
assert reg['merge_allowed'] is True and reg['advance_allowed'] is True
assert reg['fresh_reaudit_required'] is False
assert reg['pr'] == 1058
assert reg['merge_commit'] == '2ba3bc1b0bce3bbd4610b93d4cdef1124a0cbe8e'
assert reg['next_derived_route'] == '27-20-r301z'
assert reg['numbering_contract']['after_r301z'] == 'Stage27-20-r302-main-batch'
assert reg['numbering_contract']['r301aa_forbidden'] is True
assert 'AUDIT_VERDICT=PASS' in audit
assert 'R301W_MATHEMATICS=PASS' in audit
assert 'R301X_MATHEMATICS=PASS' in audit
assert 'R301Y_MATHEMATICS=PASS' in audit
assert 'SHRINKING_NEAR_WALL_CONTROL' in audit

# Parallel-lane firewall: do not rewrite the global controller from this Stage20 closeout.
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['NEXT_CHECKPOINT'] == 40
assert ctl['stage20_r301_numbering_contract']['after_r301z'] == 'Stage27-20-r302-main-batch'
assert ctl['stage20_r301_numbering_contract']['r301aa_forbidden'] is True

assert delta['consume_closeout']['audit_status'] == 'PASS'
assert delta['preserve_live_stage19']['do_not_overwrite_global_state'] is True
assert delta['stage20_route_updates']['Stage27-20-r301v'] == 'AUDITED_PASS_MERGED'
assert delta['stage20_route_updates']['Stage27-20-r301w'] == 'AUDITED_PASS_MERGED'
assert delta['stage20_route_updates']['Stage27-20-r301x'] == 'AUDITED_PASS_MERGED'
assert delta['stage20_route_updates']['Stage27-20-r301y'] == 'AUDITED_PASS_MERGED'
assert delta['stage20_batch_audit']['audit_status'] == 'PASS'
assert delta['stage20_next_derived_route'] == '27-20-r301z'

print('Stage27-20-r301w-y audited closeout verifier: PASS')
