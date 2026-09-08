#!/usr/bin/env python3
"""Verify the standard-cusp rank-3 ruling / modular four-jet adapter.

Scratch only.  This verifies only the displayed local theta-series identity
through the quotient-normal fourth jet.  It grants no endpoint or MAIN credit.
"""
import json
import sympy as sp

p, u = sp.symbols("p u")
q = u * p

# Freitag--Salvati Manni use p=e^(2*pi*i*z/8), q=e^(2*pi*i*w/8).
# From the Jacobi theta series:
#   theta00(2z) = 1 + 2 p^8 + O(p^32)
#   theta10(z)  = 2 p + 2 p^9 + O(p^25)
#   theta10(2w) = 2 q^2 + O(q^18)
#   theta10(w)  = 2 q + 2 q^9 + O(q^25).
# These terms are sufficient for the p^8 coefficient after q=u*p.
th00_2z = 1 + 2 * p**8
th10_2w = 2 * q**2
th10_z = 2 * p + 2 * p**9
th10_w = 2 * q + 2 * q**9

# At the standard cusp, r3=a1^2+a2^2-b3^2 is
# W1^2+W2^2-Z3^2.  The ruling parameter aligned with u=q/p is
#   T=(W1+i W2)/Z3
#    =2 theta00(2z) theta10(2w)/(theta10(z) theta10(w)).
T = sp.cancel(2 * th00_2z * th10_2w / (th10_z * th10_w))
fourjet_p = sp.series(T, p, 0, 10).removeO()
expected_p = u + u * (1 - u**8) * p**8
assert sp.expand(fourjet_p - expected_p) == 0

# Quotient normal coordinate x=p^2.  Compose with a general resolved branch
# u(x)=lambda+c1*x+...+c4*x^4+O(x^5).
x, lam, c1, c2, c3, c4 = sp.symbols("x lam c1 c2 c3 c4")
ubr = lam + c1*x + c2*x**2 + c3*x**3 + c4*x**4
Tbr = ubr + ubr * (1 - ubr**8) * x**4
fourjet_x = sp.series(Tbr, x, 0, 5).removeO()
expected_x = (
    lam + c1*x + c2*x**2 + c3*x**3
    + (c4 + lam * (1 - lam**8)) * x**4
)
assert sp.expand(fourjet_x - expected_x) == 0

print(json.dumps({
    "success": True,
    "standard_cusp_rank3_quadric": "r3=a1^2+a2^2-b3^2",
    "global_ruling_parameter": "T=(a1+i*a2)/b3=(W1+iW2)/Z3",
    "ambient_fourjet": "T=u+u(1-u^8)x^4+O(x^5) through fourth jet, x=p^2, u=q/p",
    "branch_fourth_coefficient": "d4=c4+lambda(1-lambda^8)",
    "an_fourflat_implies_rank3_fourflat_iff": "lambda^8=1",
    "o266_endpoint_excluded": False,
    "o264_descent_authorized": False,
}, indent=2, sort_keys=True))
