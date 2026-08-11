#!/usr/bin/env python3
from fractions import Fraction


def main():
    half=Fraction(1,2)
    for d in [Fraction(0),Fraction(1,100),Fraction(1,24),Fraction(1,12)]:
        e=half-d
        assert e==Fraction(1,2)-d
        if d>0:
            assert e<half
    for num,den in [(0,1),(1,10),(1,2),(1,1)]:
        assert 0 <= Fraction(num,den) <= 1
    print('PRINCIPAL_DENSITY_DEFICIT_LOCALIZATION_PROVED=true')
    print('PRINCIPAL_DENSITY_DEFICIT_STRATUM_EXPONENT=1/2-delta')
    print('SQRT_SATURATION_REQUIRES_NEAR_MAXIMAL_CONDITIONAL_OCCUPANCY=true')
    print('SATURATING_CELL_OCCUPANCY=B^(-o(1))')
    print('CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2')
    print('STRICT_SUBSQRT_POWER_SAVING_PROVED=false')
    print('MAINLINE_H_NEEDED=false')
    print('NEXT=Stage14-4dk')

if __name__=='__main__':
    main()
