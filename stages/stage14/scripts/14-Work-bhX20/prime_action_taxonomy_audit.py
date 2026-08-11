from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4dq/result.md': 'MAINLINE_ZERO_MODE_ARITHMETIC_RECEIVER_CONTRACTED=true',
    'stages/stage14/14-s7-60/result.md': 'SINGLE_PRIME_INFLUENCE_HAS_EXPLICIT_TWO_SQUARE_ADMISSIBILITY_PACKET=true',
    'stages/stage14/14-t100/result.md': 'SATURATION_REQUIRES_BOUNDARY_MOVER=true',
    'stages/stage14/14-Work-bhX20/result.md': 'COMMON_STABILIZER_MOVER_DICHOTOMY_PROVED=true',
}
for rel, needle in locks.items():
    text=(ROOT/rel).read_text()
    assert needle in text, (rel, needle)

# Abstract two-state prime action sanity.
def influence(a0,a1):
    return int(bool(a0) != bool(a1))
for a0 in (0,1):
    for a1 in (0,1):
        inf=influence(a0,a1)
        assert inf==0 if a0==a1 else inf==1

res=(ROOT/'stages/stage14/14-Work-bhX20/result.md').read_text()
for token in [
    'COMMON_SINGLE_PRIME_ACTION_LANGUAGE_PROVED=true',
    'GLOBAL_MOVER_TO_FIXED_U_ELEMENTARY_MOVER_MAP_PROVED=false',
    'COMMON_ARITHMETIC_ADAPTER_PROVED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_INTERNAL_TARGET=PrimeMoverDensityOrEnergyLemma',
]:
    assert token in res, token
print('Stage14-Work-bhX20 prime action taxonomy audit: PASS')
