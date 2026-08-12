from fractions import Fraction

def exponents(theta):
    low=Fraction(5,8)+theta/2
    high=1-theta
    return low,high

def balance():
    t=Fraction(1,4)
    lo,hi=exponents(t)
    return t,lo,hi
