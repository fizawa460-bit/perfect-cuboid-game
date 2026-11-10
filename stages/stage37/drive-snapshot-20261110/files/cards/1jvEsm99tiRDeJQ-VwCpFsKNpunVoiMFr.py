"""Exact finite replay for M3-T11-135. No finite screen proves the theorem."""
import json
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path

def sq(n):
    return n >= 0 and isqrt(n)**2 == n

def rsq(x):
    return sq(x.numerator) and sq(x.denominator)

counts = dict(singular_conic=0, square_norm_conic=0, cubic_factorizations=0,
              descent_pairwise_coprimality=0, descent_identities=0,
              singular_square_norm_survivors=0, physical_endpoints_enumerated=0)

# Primitive parametrization of w^2=u^2+2, with both parity normalizations.
for r in range(1, 181):
    for s in range(1, 181):
        if gcd(r,s) != 1:
            continue
        eps = 2 if r % 2 == 0 and s % 2 == 1 else 1
        a, b, w = (r*r-2*s*s)//eps, 2*r*s//eps, (r*r+2*s*s)//eps
        assert gcd(a,b) == 1 and w*w == a*a+2*b*b
        assert b > 0 and a != 0
        counts['singular_conic'] += 1
        if sq(a*a+b*b):
            counts['singular_square_norm_survivors'] += 1
        u = F(a,b); A = 1+u*u; S = -2*u/A
        E = 4*u*(S-u)/A; P = 4*u*u*S/A
        # Factorization coefficientwise; roots labelled separately from packet cores.
        coeff = [F(1), 2*u/A, -4*u*u*(A+2)/A**2, 8*u**3/A**2]
        assert coeff == [F(1), -S, E, -P]
        assert (F(w,b)+u)*(F(w,b)-u)/2 == 1
        # Conditional triangle identity: hypotenuse 2k needs k^2=A.
        assert (F(w,b)+u)**2+(F(w,b)-u)**2 == 4*A
        counts['cubic_factorizations'] += 1

# Independently sample the other conic: k^2=1+u^2.
for m in range(2, 181):
    for n in range(1,m):
        if gcd(m,n) != 1 or (m-n) % 2 == 0:
            continue
        a, b, c = m*m-n*n, 2*m*n, m*m+n*n
        assert a*a+b*b == c*c
        assert not sq(a*a+2*b*b)
        counts['square_norm_conic'] += 1

# Arithmetic lemma used in the proof: mn(m+n)(m-n) has coprime factors.
for m in range(2, 181):
    for n in range(1,m):
        if gcd(m,n) != 1 or (m-n) % 2 == 0:
            continue
        factors = [m,n,m+n,m-n]
        assert all(gcd(factors[i],factors[j]) == 1
                   for i in range(4) for j in range(i))
        counts['descent_pairwise_coprimality'] += 1

# Descent algebra on odd hypothetical square roots g>h. These are not
# counterexamples: m need not itself be a square in these algebraic samples.
for g in range(3, 181, 2):
    for h in range(1,g,2):
        r, s = (g+h)//2, (g-h)//2
        m, n = (g*g+h*h)//2, (g*g-h*h)//2
        assert r*r+s*s == m and 2*r*s == n
        assert F(r*s,2) == F(n,4)
        assert m < (m*m+n*n)**2
        counts['descent_identities'] += 1

assert counts['singular_square_norm_survivors'] == 0
out = dict(card='M3-T11-135', status='PASS', counts=counts,
           symbolic_replay=[0,0,1], finite_screen_is_proof=False,
           theorem_proof='Infinite descent in card; finite-u x=-1/8 empty',
           external_audit=False, global_counting_credit=0,
           generic_moving_support_proved=False)
Path('M3-T11-135-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
