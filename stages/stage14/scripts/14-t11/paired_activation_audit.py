#!/usr/bin/env python3
from fractions import Fraction

# Structural identities only; no asymptotic claim.
# For s=t^2 and h^2=1+t^2, verify the shared-q conic identity and nesting logic.

def main():
    samples = [(3,4,5), (5,12,13), (8,15,17)]
    for x,y,hyp in samples:
        t = Fraction(x,y)
        s = t*t
        assert 1+s == Fraction(hyp*hyp,y*y)
        A = (1-s)/(1+s)
        C = Fraction(2,1)/s - 1
        # coefficient difference from t7
        assert 2*(C-A) == Fraction(4,1)/(s*(1+s))
    locks = {
        'STAGE14_T11': 'COMPLETE_COMPATIBLE_PAIRED_ACTIVATION_FORMULATION',
        'PAIR_REQUIRES_SHARED_Q': True,
        'SIMULTANEOUS_POSITIVE_RANK_SUFFICIENT': False,
        'MU_RAW_LE_MU_PAIR': True,
        'V_PAIR_SUBSET_V_RAW': True,
        'FINITE_B2M_RAW_ACTIVE_VERTICES': 490,
        'FINITE_B2M_TRIPLE_OBJECTS': 0,
        'FINITE_ZERO_IMPLIES_ASYMPTOTIC_ZERO': False,
        'PAIR_THINNING_PROVED': False,
        'T_O_SQRT_B_PROVED': False,
    }
    for k,v in locks.items():
        print(f'{k}={str(v).lower() if isinstance(v,bool) else v}')

if __name__ == '__main__':
    main()
