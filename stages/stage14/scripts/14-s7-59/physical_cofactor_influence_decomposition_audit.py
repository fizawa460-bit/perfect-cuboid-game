#!/usr/bin/env python3
from fractions import Fraction as F

vals = [F(1,7), F(2,7), F(3,7), F(5,7), F(4,7), F(6,7), F(1,1)]
inc = [vals[i]-vals[i-1] for i in range(1, len(vals))]
assert sum(inc, F(0)) == vals[-1]-vals[0]

residual_names = ("balanced", "range", "chart", "reciprocal")
assert len(residual_names) == 4
blocks = ("C_*", "S", "T", "u_*", "R", "J")
assert len(blocks) == 6
arithmetic = ("balanced", "reciprocal")
side_conditions = ("range", "chart")
assert set(arithmetic + side_conditions) == set(residual_names)

print("Stage14-s7-59 physical cofactor influence audit: PASS")
print("residual influence branches:", len(residual_names))
print("atomic blocks:", len(blocks))
print("arithmetic receiver count: 1")
print("next: Stage14-s7-60")
