#!/usr/bin/env python3
"""Known general bound, quantified here as a baseline only; requires flint."""
import json
from math import factorial
from flint import arb,ctx
ctx.prec=256
D=117981248819779519774066150957208102315271607402605667641283959829993045399028658031316657246104332689903983273746149168969341985775210396795186114853102963382274291541213184
M=(4/arb.pi())**49*arb(factorial(105))/105**105*arb(D).sqrt()
assert arb('3e47')<M<arb('4e47')
print(json.dumps({'known_theorem_not_new':True,'degree':105,'complex_pairs':49,
 'Minkowski_bound_arb':str(M),'safe_unconditional_generation_bound':4*10**47,
 'small_bound_6768_generation_certified':False},indent=2))
