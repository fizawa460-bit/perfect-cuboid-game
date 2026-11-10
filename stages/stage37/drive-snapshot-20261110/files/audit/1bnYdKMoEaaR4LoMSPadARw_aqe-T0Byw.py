"""Exact integer diagnostics and COMPLETE projective finite-field proof for TI-002.
No rank computations or physical density inference. Python standard library only.
"""
from math import gcd
from collections import Counter
from fractions import Fraction as F

def count_curve(q, alpha, beta):
    return 1 + sum(sum((y*y-x*(x-alpha)*(x-beta)) % q == 0
                        for y in range(q)) for x in range(q))

tables = {}
for q in (7, 11, 13, 17):
    table = Counter()
    # Every good projective source has n != 0, so [m:n]=[k:1].
    for k in range(q):
        u, v, w = (k*k-1) % q, (2*k) % q, (k*k+1) % q
        if u*v*w % q:
            table[count_curve(q, (k+1)**4 % q, (k-1)**4 % q)] += 1
    assert all(order % 3 for order in table)
    tables[q] = dict(sorted(table.items()))
assert tables == {7:{8:4}, 11:{8:4,16:4}, 13:{16:8}, 17:{16:12}}
print('COMPLETE projective residue-class proof:', tables)

checked = 0
for m in range(2, 101):
    for n in range(1, m):
        if gcd(m,n) != 1 or (m-n) % 2 == 0:
            continue
        u,v,w = m*m-n*n, 2*m*n, m*m+n*n
        alpha,beta = (m+n)**4, (m-n)**4
        assert u*u+v*v == w*w and gcd(u,v) == gcd(v,w) == gcd(u,w) == 1
        assert (2*beta-alpha-1) % 4 == 0 and beta*(beta-alpha) % 16 == 0
        a2,a4 = (2*beta-alpha-1)//4, beta*(beta-alpha)//16
        b2,b4,b8 = 1+4*a2,2*a4,-a4*a4
        c4,delta = b2*b2-24*b4,-b2*b2*b8-8*b4**3
        assert c4 == u**4+16*v*v*w*w
        assert delta == u**8*v*v*w*w//16 and gcd(c4,delta) == 1
        for x,y in ((0,0),(1,2),(-3,5)):
            assert ((8*y+4*x)**2-(4*x+beta)*(4*x+beta-alpha)*(4*x)) == 64*(y*y+x*y-x**3-a2*x*x-a4*x)
        # Independent inverse-formula identity for generic rational elliptic x,y.
        # Given Y^2=X(X-alpha)(X-beta), compare rational symbolic-in-Y^2 form.
        for X in (F(1,2), F(-2,3), F(alpha+1)):
            Y2 = X*(X-alpha)*(X-beta)
            if not Y2:
                continue
            h2 = 16*u*u*X*X/Y2
            eta = h2*(X-v*v-w*w)/2-4*u*u
            assert eta*eta == (v*v*h2+4*u*u)*(w*w*h2+4*u*u)
        checked += 1
print('Integer/rational formula diagnostics (NOT a universal proof):', checked)
print('No ranks, physical M3 weights, or 1072 rows computed.')
