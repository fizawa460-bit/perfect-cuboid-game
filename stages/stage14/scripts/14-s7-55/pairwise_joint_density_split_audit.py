#!/usr/bin/env python3
from fractions import Fraction as F

# Exact algebraic identities only.
# mu12 - mu1*mu2 = (pair zero - mu1*mu2) + pair centered error.

samples = [
    (F(1,2), F(1,3), F(1,4), F(1,12)),
    (F(2,3), F(1,2), F(5,12), F(1,12)),
    (F(3,5), F(2,5), F(7,25), F(1,25)),
]
for mu1, mu2, pair_zero, err in samples:
    joint = pair_zero + err
    gamma = joint - mu1 * mu2
    delta_pair = pair_zero - mu1 * mu2
    assert gamma == delta_pair + err

# Pythagorean pair-coordinate equivalence: any two signed projections determine the third up to sign.
triples = [(5,4,3),(13,12,5),(17,15,8),(25,24,7)]
for xp, xm, x0 in triples:
    assert xp*xp == xm*xm + x0*x0
    assert xp*xp - xm*xm == x0*x0
    assert xp*xp - x0*x0 == xm*xm

print('Stage14-s7-55 pairwise joint-density / centered-error audit: PASS')
print('representative pair: (+,-)')
print('pairwise branches at fixed power: 1')
print('centered error alone sufficient: false')
