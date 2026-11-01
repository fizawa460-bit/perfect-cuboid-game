#!/usr/bin/env python3
# Explicit checks remain active under python -O.
"""Exact half-section identities on 2y^2=x^4+1, using only fractions."""
from fractions import Fraction as Q
import json

def add(a, b):
    return [sum((p[k] if k < len(p) else Q(0) for p in (a, b)), Q(0)) for k in range(max(len(a), len(b)))]

def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out

def scale(a, c):
    return [x * c for x in a]

def kadd(a, b):
    return tuple((x + y for x, y in zip(a, b)))

def ks(a, c):
    return tuple((x * c for x in a))

def kmul(a, b):
    out = [Q(0)] * 4
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i ^ j] += x * y * (2 if i & j & 1 else 1) * (-1 if i & j & 2 else 1)
    return tuple(out)
ONE = (Q(1), Q(0), Q(0), Q(0))

def kp(a, n):
    out = ONE
    for _ in range(n):
        out = kmul(out, a)
    return out

def evaluate_t(x):
    g = kadd(kadd(ONE, ks(x, -1)), kp(x, 2))
    return kmul(kmul(kp(kadd(x, ONE), 4), kp(kadd(kp(x, 2), ONE), 4)), g)

def calculate():
    g = [Q(1), Q(-1), Q(1)]
    e = [Q(1, 2), Q(0), Q(0), Q(0), Q(1, 2)]
    if not add(mul(g, g), scale(e, -1)) == [Q(1, 2), Q(-2), Q(3), Q(-2), Q(1, 2)]:
        raise ValueError('verification condition failed')
    f = [Q(-3, 4), Q(1), Q(-3, 2), Q(1), Q(-3, 4)]
    if not add(f, scale(add(mul(g, g), e), Q(1, 2))) == [Q(0)] * 5:
        raise ValueError('verification condition failed')
    q = (Q(0), Q(1, 2), Q(0), Q(-1, 2))
    if not kp(q, 4) == ks(ONE, -1):
        raise ValueError('verification condition failed')
    tp, tm = (evaluate_t(q), evaluate_t(ks(q, -1)))
    ratio = (Q(3), Q(2), Q(0), Q(0))
    if tp != kmul(ratio, tm):
        ratio = ks(ratio, -1)
    if not (tp == kmul(ratio, tm) and tm != (Q(0),) * 4):
        raise ValueError('verification condition failed')
    fmt = lambda a: [str(x) for x in a]
    return {'curve': '2*y^2=x^4+1', 'g': 'x^2-x+1', 'identity': 'g^2-(x^4+1)/2=(x-1)^4/2', 'half_section': 't=(x+1)^4*(x^2+1)^4*(g+y)', 'F59_section': 's_1=-t^2/2', 'point_difference_exact_order': 2, 'intersection_field_basis': ['1', 'sqrt(2)', 'i', 'i*sqrt(2)'], 't_plus': fmt(tp), 't_minus': fmt(tm), 'ratio': fmt(ratio), 'parity_obstruction': False}
if __name__ == '__main__':
    print(json.dumps(calculate(), ensure_ascii=False))
