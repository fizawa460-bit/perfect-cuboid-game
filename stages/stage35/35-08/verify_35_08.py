#!/usr/bin/env python3
import sympy as sp


t = sp.symbols("t")
X = sp.symbols("X")
alpha = ((t**2 - 1) / (t**2 + 1))**2
beta = 4*t**2 / (t**2 + 1)**2

assert sp.factor(alpha + beta - 1) == 0

curves = {
    "E4": X*(X-alpha)*(X+beta),
    "E3": X*(X-alpha)*(X+1),
    "E2": X*(X-beta)*(X-1),
    "E1": X*(X-(alpha+1))*(X-1),
    "E0": X*(X-(1-alpha**2))*(X-1),
}

expected = {
    "E4": 16*t**4*(t-1)**4*(t+1)**4/(t**2+1)**8,
    "E3": 4*(t-1)**4*(t+1)**4*(t**4+1)**2/(t**2+1)**8,
    "E2": 16*t**4*(t-1)**4*(t+1)**4/(t**2+1)**8,
    "E1": 4*(t-1)**4*(t+1)**4*(t**4+1)**2/(t**2+1)**8,
    "E0": 64*t**4*(t-1)**8*(t+1)**8*(t**4+1)**2/(t**2+1)**16,
}

for name, cubic in curves.items():
    disc = sp.factor(sp.discriminant(cubic, X))
    assert sp.factor(disc - expected[name]) == 0, (name, disc)

# Exact generic boundary sections with d=1.
r = (t**2 - 1)/(t**2 + 1)
s = 2*t/(t**2 + 1)

# C_t equations divided by (t^2+1)^2.
def check_point(x, y, p, q, d):
    return [
        sp.factor(x**2 + alpha*d**2 - p**2),
        sp.factor(y**2 + alpha*d**2 - q**2),
        sp.factor(x**2 + y**2 - beta*d**2),
    ]

for signs in [(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]:
    sy, sp_, sq = signs
    assert check_point(0, sy*s, sp_*r, sq, 1) == [0,0,0]
    sx, sp_, sq = signs
    assert check_point(sx*s, 0, sp_, sq*r, 1) == [0,0,0]

print("PASS STAGE35_35_08_ELLIPTIC_QUOTIENT_STRUCTURE_V1")
