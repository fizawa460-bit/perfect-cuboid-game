from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    return (ROOT / rel).read_text()

t152 = text('stages/stage14/14-t152/result.md')
t153 = text('stages/stage14/14-t153/result.md')
t154 = text('stages/stage14/14-t154/result.md')
t155 = text('stages/stage14/14-t155/result.md')
th31 = text('stages/stage14/14-tH31/result.md')

assert 'NEXT=Stage14-t153' in t152
assert 'N(q) <= exp(sqrt(log X)/O_K(1))' in th31
assert 'MITSUI_SAFE_LONG_HEADROOM_THEOREM_APPLICABLE=true' in th31

for tok in [
    'LONG_HEADROOM_DYADIC_SHELL_DEFINED=true',
    'LONG_COFACTOR_FIXED_RESIDUE_LATTICE_COUNT_PROVED=true',
    'LONG_AREA_CAPACITY_INDEPENDENT_OF_DYADIC_N=true',
    'NEXT=Stage14-t154',
]:
    assert tok in t153, tok

for tok in [
    'LONG_AREA_REGIME=N_GE_d2',
    'LONG_AREA_PRINCIPAL_CAPACITY=XU_OVER_qd_d2',
    'LONG_SPARSE_REGIME=N_LT_d2',
    'LONG_SPARSE_TOTAL_ACTUAL_COFACTORS=O(1)',
    'LONG_SPARSE_HEADROOM_FLOOR=qd_TIMES_BminusO1',
    'NEXT=Stage14-t155',
]:
    assert tok in t154, tok

# Elementary shell-term domination at N >= d^2.
for d in [3, 5, 11, 31]:
    N = d*d
    assert 1/(d*(N**0.5)) <= 1/(d*d) + 1e-15
    assert 1/N <= 1/(d*d) + 1e-15

for tok in [
    'ACTUAL_SCALE_KAI_ENVELOPE_DEFINED=true',
    'TH31_RECONSUMED_WITHOUT_RECHARGE=true',
    'ACTUAL_SCALE_KAI_ADMISSIBLE_LONG_FIXED_POWER_DEPLETION_RULED_OUT=true',
    'POSSIBLE_SIEGEL_ZERO_RETAINED=true',
    'RECEIVER_MATERIALLY_CHANGED=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'T_ROUTE_H_NEEDED=false',
    'TH33_NEEDED=false',
    'NEXT=Stage14-t156',
]:
    assert tok in t155, tok

print('Stage14-t-batch t153-t155 audit: OK')
