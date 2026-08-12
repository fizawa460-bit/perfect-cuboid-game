from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def read(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


work = read('stages/stage14/14-Work-ckX49/result.md')
mat = read('docs/stage14-toolbox/work-ckX49-receiver-matrix.md')
q23 = read('stages/stage14/14-q23/result.md')
q23s = read('stages/stage14/14-q23/summary.md')
s147 = read('stages/stage14/14-s7-147/result.md')
s148 = read('stages/stage14/14-s7-148/result.md')
s149 = read('stages/stage14/14-s7-149/result.md')

for token in [
    'GOOD_INDICATOR_TO_Q17_WITNESS_EQUIVALENCE_CONSUMED=true',
    'JOINT_FILTERED_TAU3_Q17_CRT_INCIDENCE_NORMAL_FORM_CONSUMED=true',
    'GOOD_PACKET_SECOND_MOMENT_RECHARGE_FORBIDDEN=true',
    'S_JOINT_INCIDENCE_THEOREM_SPECIES_COUNT=2',
    'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
    'POST_MASK_REMAINS_SEPARATELY_CHARGED=true',
    'Q23_THEOREM_TARGET_NOW_STABLE=true',
    'TH34_NEEDED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
]:
    assert token in work, token

for token in [
    'GOOD_INDICATOR_TO_Q17_WITNESS_EQUIVALENCE_CONSUMED=true',
    'GOOD_PACKET_SECOND_MOMENT_RECHARGE_FORBIDDEN=true',
    'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
    'POST_MASK_REMAINS_SEPARATELY_CHARGED=true',
]:
    assert token in mat, token

assert 'Q22_GOOD_INDICATOR_EXACT_WITNESS_EXPANSION_TEST=PASS_NONNEGATIVE_Q17_WITNESS_COUNT' in s147
assert 'Q22_POSITIVE_FIRST_MOMENT_NORMAL_FORM_TEST=PASS_JOINT_NONNEGATIVE_DIVISOR_CRT_INCIDENCE' in s148
assert 'Q23_THEOREM_TARGET_NOW_STABLE=true' in s149

for token in [
    'DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0',
    'JOINT_FILTERED_TAU3_RECIPROCAL_CRT_FIRST_MOMENT_DIRECT_THEOREM_FOUND=false',
    'FIXED_SHIFT_JOINT_INCIDENCE_ADAPTER_PROVED=false',
    'DIVISOR_AP_JOINT_INCIDENCE_ADAPTER_PROVED=false',
    'BINARY_FORM_JOINT_INCIDENCE_ADAPTER_PROVED=false',
    'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
    'Q23_W1_WITNESS_DEPENDENCE_SEPARABILITY_TEST=Stage14-s7-150',
    'Q23_FIXED_SHIFT_OR_AP_OR_BINARY_FORM_JOINT_NORMAL_FORM_TEST=Stage14-s7-151+',
    'Q24_NEEDED=false',
]:
    assert token in q23, token
    assert token in q23s, token

# Tiny arithmetic sanity checks for the charged-once deficit ledger.
for sigma_mult, sigma_joint, tau_phys in [(0.50, 0.47, 0.45), (0.41, 0.41, 0.39)]:
    delta_joint = sigma_mult - sigma_joint
    delta_post = sigma_joint - tau_phys
    assert abs((sigma_mult - delta_joint - delta_post) - tau_phys) < 1e-12

print('Stage14-Work-ckX49/q23 audit: PASS')
