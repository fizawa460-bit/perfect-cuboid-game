from pathlib import Path

DOC = Path('stages/stage13/13-13fl/gaussian-hecke-normalization.md').read_text()
RESULT = Path('stages/stage13/13-13fl/result.md').read_text()

required = [
    'HLR_XI_K=(alpha/bar_alpha)^(2k)',
    'HLR_ANGULAR_EXPONENT=4k',
    'HLR_GAMMA_SHIFT=2*abs(k)',
    'PROOF_FOURIER_EXPONENT=8*ell',
    'PROOF_TO_HLR_INDEX=k_HLR=2*ell',
    'RETAINED_ELL_MIN=1',
    'NONZERO_ANGULAR_L_ENTIRE=true',
    'NONZERO_ANGULAR_POLE_AT_1=false',
    'UNMAPPED_HECKE_ASSUMPTIONS=0',
]
for token in required:
    assert token in DOC, token
assert 'HLR_GAMMA_SHIFT_ON_RETAINED_FAMILY=4*ell' in RESULT
assert 'THEOREM_CHANGED=false' in RESULT
print('Stage13-13fl Gaussian-Hecke normalization audit: PASS')
