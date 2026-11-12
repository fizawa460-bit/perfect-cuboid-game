"""Stage37 review 2026-11-12: small checks for CONTINUATION-JUDGEMENT.md.

Run from the repo root:  python -I stages/stage37/review-20261112/check_low_degree_curves.py

(1) No nondegenerate rational curve of parametrisation degree n <= 3 on the Euler-brick surface
    (forms a,b,c in C[r,s] of degree n, gcd(a,b,c)=1, a^2+b^2, a^2+c^2, b^2+c^2 squares), except
    n=2 curves with a^2+b^2+c^2 = 0 identically (no real points) or a = +-b type (1+1=2 not a square).
    Parity lemma used (by hand): if g=gcd(a,b) then (a+ib)/g, (a-ib)/g are coprime with square
    product, so each is a square and n - deg g is even.
(2) Exponent arithmetic quoted in the report.
(3) Local growth exponents of the M3 census recorded in stages/stage20/final.md.
"""
from fractions import Fraction as Fr
from math import log, sqrt
from sympy import symbols, expand, Poly, discriminant, groebner, QQ, solve, I, simplify

r, s, j = symbols('r s j')

def disc_parts(P, Q):
    """disc_r of P + i*Q (at s=1) written as D0 + i*D1; both vanish iff P+iQ and P-iQ are squares
    (binary quadratics)."""
    D = Poly(expand(discriminant(Poly(expand((P + j*Q).subs(s, 1)), r))), j)
    c = D.all_coeffs()[::-1]
    D0 = sum(co*(-1)**(k//2) for k, co in enumerate(c) if k % 2 == 0)
    D1 = sum(co*(-1)**(k//2) for k, co in enumerate(c) if k % 2 == 1)
    return [expand(D0), expand(D1)]

ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name)
    ok = ok and bool(cond)

# ---- n = 2, all pairwise gcds trivial: normalise a+ib = r^2, a-ib = s^2 over C
c0, c1, c2 = symbols('c0 c1 c2')
a = (r**2 + s**2)/2
b = (r**2 - s**2)/(2*I)
c = c0*r**2 + c1*r*s + c2*s**2
def dsc(F):
    return expand(discriminant(Poly(expand(F.subs(s, 1)), r)))
eq2 = [dsc(a + I*c), dsc(a - I*c), dsc(b + I*c), dsc(b - I*c)]
sol2 = solve(eq2, [c0, c1, c2], dict=True)
print('n=2 coprime case solutions:', sol2)
check('n=2 coprime: every solution has a^2+b^2+c^2 == 0 (no real points)',
      len(sol2) > 0 and all(simplify(expand((a**2 + b**2 + c**2).subs(S))) == 0 for S in sol2))

# ---- n = 2, b = lam*a, (a,c) coprime: normalise a+ic = r^2, a-ic = s^2
lam = symbols('lam')
a = (r**2 + s**2)/2
c = (r**2 - s**2)/(2*I)
e = [dsc(lam*a + I*c), dsc(lam*a - I*c)]
sl = solve(e, [lam], dict=True)
print('n=2 proportional case: lam in', sl)
check('n=2 proportional: only lam = +-1, and 1+lam^2 = 2 is not a rational square',
      sorted(S[lam] for S in sl) == [-1, 1])

# ---- n = 3: all three pairwise gcds are linear and pairwise coprime (parity + gcd(a,b,c)=1);
#      normalise gcd(a,b)=r, gcd(a,c)=s, gcd(b,c)=r+s
a0, a1, b0, b1, g0, g1 = symbols('a0 a1 b0 b1 g0 g1')
al = a0*r + a1*s; be = b0*r + b1*s; ga = g0*r + g1*s
E = disc_parts(s*al, (r + s)*be) + disc_parts(r*al, (r + s)*ga) + disc_parts(r*be, s*ga)
G = groebner(E, a0, a1, b0, b1, g0, g1, order='grevlex', domain=QQ)
def in_radical_power(v, kmax=12):
    return any(G.contains(v**k) for k in range(1, kmax))
check('n=3: g1 vanishes on the solution set', in_radical_power(g1))
G2 = groebner(E + [g1], a0, a1, b0, b1, g0, g1, order='grevlex', domain=QQ)
check('n=3: then g0 vanishes too, i.e. c == 0 (degenerate)',
      any(G2.contains(g0**k) for k in range(1, 12)))

# ---- exponent arithmetic
d = 16
check('Salberger main exponent 3/sqrt(16) = 3/4 > 1/2 > 1/3', Fr(3, 4) == Fr(3, int(sqrt(d))) and Fr(3, 4) > Fr(1, 2))
check('number of auxiliary curves exponent 3/(2 sqrt 16) = 3/8 > 1/3', Fr(3, 8) > Fr(1, 3))
check('rational curve of degree n gives B^(2/n): n>=4 -> <=1/2, n=6 -> 1/3',
      Fr(2, 4) == Fr(1, 2) and Fr(2, 6) == Fr(1, 3))
check('A47 scale: #{h*m <= B^2, h <= H, m 7-full} ~ B^(2/7) H^(6/7); H = B^(1/18) gives exactly B^(1/3)',
      Fr(2, 7) + Fr(6, 7)*Fr(1, 18) == Fr(1, 3))
check('Salberger Thm 0.8 terms for d=16: 3/4, 3/8+2/3 = 25/24, 1  (all > 1/2)',
      Fr(3, 8) + Fr(2, 3) == Fr(25, 24) and min(Fr(3, 4), Fr(25, 24), Fr(1)) > Fr(1, 2))
check('Bombieri-Lang scenario: rational curve of degree >= 18 gives <= B^(1/9) < B^(1/3)', Fr(2, 18) < Fr(1, 3))

# ---- census exponents (values copied from stages/stage20/final.md section 2)
cen = [(2000, 7), (10000, 18), (50000, 42), (200000, 82), (1000000, 219)]
for (B1, m1), (B2, m2) in zip(cen, cen[1:]):
    print('  local exponent %7d -> %7d : %.3f' % (B1, B2, log(m2/m1)/log(B2/B1)))
for B, m in cen:
    print('  B=%7d  M3=%4d  M3/B^(1/2)=%.3f  M3/B^(1/3)=%.2f' % (B, m, m/B**0.5, m/B**(1/3)))
print('ALL PASS' if ok else 'SOME FAIL')
raise SystemExit(0 if ok else 1)
