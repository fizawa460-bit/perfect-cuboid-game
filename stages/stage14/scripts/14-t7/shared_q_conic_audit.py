#!/usr/bin/env python3
from fractions import Fraction
import json

def main():
    # symbolic coefficient check by rational-function numerator arithmetic:
    # C-A = (2-s)/s - (1-s)/(1+s) = 2/(s(1+s)).
    # We also verify the physical square identity on exact sample Pythagorean slopes.
    samples=[]
    for m,n in [(2,1),(3,2),(4,1),(5,2),(5,4),(7,4)]:
        t=Fraction(2*m*n,m*m-n*n)
        h=Fraction(m*m+n*n,m*m-n*n)
        s=t*t
        A=(1-s)/(1+s)
        C=Fraction(2,1)/s-1
        assert C-A == Fraction(2,1)/(s*(1+s))
        coeff=Fraction(4,1)/(s*(1+s))
        root=Fraction(2,1)/(t*h)
        assert coeff == root*root
        for q in [Fraction(1,2),Fraction(2,3),Fraction(3,5)]:
            diff=2*(C-A)*q*q
            assert diff == (root*q)*(root*q)
        samples.append({'m':m,'n':n,'t':str(t),'h':str(h),'s':str(s),'difference_coefficient':str(coeff),'square_root':str(root)})
    out={
      'identity_C_minus_A':'2/(s(1+s))',
      'identity_R2_minus_W2':'4q^2/(s(1+s))',
      'physical_square_root':'2/(t h)',
      'sample_count':len(samples),
      'samples':samples,
      'naive_difference_squareclass_sieve':'vacuous_on_physical_base'
    }
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
