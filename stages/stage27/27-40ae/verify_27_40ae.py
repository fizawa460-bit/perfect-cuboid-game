from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')

def data(rel):
    return json.loads(text(rel))

s14 = text('stages/stage14/final.md')
a40ad = text('stages/stage27/27-40ad/audit.md')
a40ae = text('stages/stage27/27-40ae/audit.md')
res = text('stages/stage27/27-40ae/result.md')
ctl = data('stages/stage27/27-controller.json')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')

for marker in ['U=L_x^+', 'V=L_x^-', 'primitive pair `(U,V)`']:
    assert marker in s14, marker
assert 'AUDIT_VERDICT=PASS' in a40ad
assert 'CONTINUE_UPPER_EXPLORATION_AFTER_PASS=true' in a40ad

for marker in [
    'T_OUTER_U_WEIGHTED_AVERAGING_ATTACK_EXECUTED=true',
    'OUTER_U_CARDINALITY_ALONE_ROUTE_CLOSED=true',
    'OUTER_U_DOUBLE_CHARGE_FIREWALL=true',
    'OUTER_PHYSICAL_WEIGHTED_EXCEPTIONAL_MASS_BOUND_PROVED=false',
    'OUTER_PHYSICAL_WEIGHTED_SECOND_MOMENT_PROVED=false',
    'STRICT_SUB_SQRT_UPPER_PROVED=false',
    'NEXT_CHECKPOINT=40',
    'NEXT_EXPECTED_COMMAND=Stage27-audit',
]:
    assert marker in res, marker

ad = ctl['derived_routes']['Stage27-40ad']
ae = ctl['derived_routes']['Stage27-40ae']
assert ad['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED'
assert ad['audit_status'] == 'PASS'
assert ad['pr'] == 1029
assert ad['merge_commit'] == '89e1ad0203484452994621a7f92b57f0ff3d4214'
assert ae['status'] in ('SUBMITTED_PENDING_FRESH_AUDIT', 'INTERMEDIATE_AUDITED_PASS_MERGED')
assert ae['outer_u_cardinality_alone_fixed_power_saving'] is False
assert ae['outer_physical_weighted_exceptional_mass_bound_proved'] is False
assert ae['outer_physical_weighted_second_moment_proved'] is False
if ae['status'] == 'INTERMEDIATE_AUDITED_PASS_MERGED':
    assert 'AUDIT_VERDICT=PASS' in a40ae
    assert ae['audit_status'] == 'PASS'
    assert ae['pr'] == 1030
    assert ae['merge_commit'] == '2b2bfb0768006e2fe66969726486ac765c589bbc'
else:
    assert ae['audit_status'] == 'PENDING'

assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['NEXT_CHECKPOINT'] == 40
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'].startswith('Stage27')
assert ctl['next_expected_command'].endswith('-audit')
assert 'STAGE27_40AD_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1029' in status
assert (
    'STAGE27_40AE_STATUS=T_OUTER_U_WEIGHTED_AVERAGING_SUBMITTED_PENDING_FRESH_AUDIT' in status
    or 'STAGE27_40AE_STATUS=INTERMEDIATE_AUDITED_PASS_MERGED_PR1030' in status
)

print('STAGE27_40AE_UPSTREAM_40AD_AUDIT=PASS')
print('STAGE27_40AE_STAGE14_OUTER_SUPPORT=PASS')
print('STAGE27_40AE_WEIGHTED_ADAPTER_CONTRACT=PASS')
print('STAGE27_40AE_SUCCESSOR_ROUTE_LIFECYCLE=PASS')
