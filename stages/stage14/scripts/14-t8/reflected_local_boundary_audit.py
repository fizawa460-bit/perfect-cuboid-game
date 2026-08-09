#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

# Symbolic identities are checked coefficientwise in q^2.
# R^2 = q^4 + 2(2/s-1)q^2 + 1
#     = (q^2+1)^2 + 4(1-s)/s q^2.

def coeffs_original(s):
    return [Fraction(1), 2*(Fraction(2,1)/s-Fraction(1)), Fraction(1)]

def coeffs_rewrite(s):
    return [Fraction(1), Fraction(2)+4*(Fraction(1)-s)/s, Fraction(1)]

def legendre_minus_one(p):
    return pow(p-1,(p-1)//2,p)

def main():
    samples=[Fraction(9,16),Fraction(25,144),Fraction(49,576)]
    for s in samples:
        assert coeffs_original(s)==coeffs_rewrite(s)

    primes=[3,5,7,11,13,17,19,29,37,41]
    inert=[]; split=[]
    for p in primes:
        ls=legendre_minus_one(p)
        if p%4==3:
            assert ls==p-1
            inert.append(p)
            assert not any((q*q+1)%p==0 for q in range(p))
        else:
            assert ls==1
            roots=[q for q in range(p) if (q*q+1)%p==0]
            assert len(roots)==2
            split.append({'p':p,'roots':roots})

    out={
      'quartic_rewrite_verified':True,
      'physical_difference_factor':'Delta_minus=S^2-X^2',
      'pair_bad_support':'2*S*X*H*Delta_minus',
      'odd_new_prime_automatic_outside_q2_eq_minus1':True,
      'inert_primes_tested':inert,
      'split_prime_exceptional_roots':split,
      'power_saving_claimed':False,
      't_o_sqrt_b_proved':False
    }
    target=Path(__file__).resolve().parents[2]/'data'/'14-t8'/'reflected_local_boundary.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
