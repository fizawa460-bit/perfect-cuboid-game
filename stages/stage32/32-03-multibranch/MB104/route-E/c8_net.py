"""Route E / E01 support: the canonical model of C8 and its net of quadrics (sympy, exact).
Checks: (1) the map (r,u,v) -> (2iu, 2iv, 2i*sqrt2*r, r^2, 2) lands on Q0 = Q1 = Q2 = 0 modulo
u^2 = (r^4+4)/4, v^2 = (r^4-4)/4;  (2) det(l*Q0 + m*Q1 + n*Q2) = l*m*n*(l^2 - m^2 - 4 n^2);
(3) the diagonal sign changes preserving each Q_i form a group of order 16, i.e. order 8 in PGL5 (the kernel of the
action on the net).  The remaining step |Aut(C8)| = 8 * |Stab(discriminant quintic)| = 8 * 24 = 192 is an argument
(audit round 2), not computed here."""
import itertools, sympy as sp
r, u, v, l, m, n = sp.symbols('r u v l m n')
x = [2*sp.I*u, 2*sp.I*v, 2*sp.I*sp.sqrt(2)*r, r**2, 2]
X = sp.symbols('x0:5')
Q0 = X[0]**2 + X[3]**2 + X[4]**2
Q1 = X[1]**2 + X[3]**2 - X[4]**2
Q2 = X[2]**2 + 4*X[3]*X[4]
sub = dict(zip(X, x))
ok = True
for name, Qi in (("Q0", Q0), ("Q1", Q1), ("Q2", Q2)):
    val = sp.expand(Qi.subs(sub).subs({u**2: (r**4 + 4)/4, v**2: (r**4 - 4)/4}))
    print(name, "on the model:", val); ok &= (val == 0)
M = sp.hessian(l*Q0 + m*Q1 + n*Q2, X) / 2
d = sp.factor(M.det()); print("net discriminant:", d)
ok &= sp.expand(d - l*m*n*(l**2 - m**2 - 4*n**2)) == 0
cnt = 0
for s in itertools.product((1, -1), repeat=5):
    S = dict(zip(X, [si*xi for si, xi in zip(s, X)]))
    if all(sp.expand(Qi.subs(S, simultaneous=True) - Qi) == 0 for Qi in (Q0, Q1, Q2)): cnt += 1
print("sign changes preserving every Q_i:", cnt, "-> projective kernel order", cnt // 2)
ok &= cnt == 16
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
