# Stage33 strategy review 2026-11-12: facts used by the formal-lemma argument (review section C).
# Surface (Stoll--Testa coordinates): in P^6 with coordinates (a1, a2, a3, b1, b2, b3, c),
#   a2^2 + a3^2 = b1^2,  a1^2 + a3^2 = b2^2,  a1^2 + a2^2 = b3^2,  a1^2 + a2^2 + a3^2 = c^2.
# Checks:
#   (1) P0 = (3, 4, 0; 4, 3, 5; 5) is a Q-point of the surface and a SMOOTH point (Jacobian rank 4),
#       so it is a Q-point of the minimal resolution S; it is a degenerate cuboid (a3 = 0).
#   (2) a3 is a local parameter direction at P0: there is a tangent vector with d(a3) != 0.
#   (3) the curve Q_e = (3, 4, e; sqrt(16+e^2), sqrt(9+e^2), 5; sqrt(25+e^2)) lies on the surface (identity in e);
#       for real e > 0 it is a positive real box with all seven coordinates non-zero.
#   (4) for every prime p and e = p^k with k >= k0(p), the three radicands are squares in Q_p
#       (n^2 (1 + u), with v_p(u) >= 1 for odd p and >= 3 for p = 2, is a square by Hensel; k0(2) = 4, k0(3) = k0(5) = 2, else 1's lemma);
#       verified for all primes < 200 and four exponents each by an exact p-adic square test.
# So P0 is a limit of Q_v-points of the surface with a3 != 0, at every place v.
import sympy as sp
a1, a2, a3, b1, b2, b3, c, e = sp.symbols("a1 a2 a3 b1 b2 b3 c e")
X = [a1, a2, a3, b1, b2, b3, c]
F = [a2**2 + a3**2 - b1**2, a1**2 + a3**2 - b2**2, a1**2 + a2**2 - b3**2, a1**2 + a2**2 + a3**2 - c**2]
P0 = dict(zip(X, [3, 4, 0, 4, 3, 5, 5]))
ok = True
ok &= all(f.subs(P0) == 0 for f in F)
J = sp.Matrix([[sp.diff(f, x) for x in X] for f in F]).subs(P0)
ok &= J.rank() == 4
print("(1) P0 on the surface, Jacobian rank at P0 =", J.rank())
ker = J.nullspace()
# tangent space of the affine cone has dimension 3; modulo the radial vector it is the tangent plane
has_a3 = any(v[2] != 0 for v in ker)
print("(2) cone tangent space dimension =", len(ker), "; a tangent vector with d(a3) != 0 exists:", has_a3)
ok &= len(ker) == 3 and has_a3
Q = dict(zip(X, [3, 4, e, sp.sqrt(16 + e**2), sp.sqrt(9 + e**2), 5, sp.sqrt(25 + e**2)]))
ok3 = all(sp.simplify(f.subs(Q)) == 0 for f in F)
print("(3) Q_e lies on the surface for all e:", ok3); ok &= ok3
def vp(n, p):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k
def is_padic_square(num, den, p):
    """num/den > 0 rational, exact test in Q_p."""
    m = num * den                      # same square class
    k = vp(m, p)
    if k % 2: return False
    u = m // p**k
    return (u % 8 == 1) if p == 2 else (pow(u, (p - 1) // 2, p) == 1)
ok4 = True
for p in sp.primerange(2, 200):
    k0 = 4 if p == 2 else (2 if p in (3, 5) else 1)
    for k in range(k0, k0 + 4):
        ee = p**k
        ok4 &= all(is_padic_square(n * n + ee * ee, 1, p) for n in (3, 4, 5))
print("(4) radicands are p-adic squares for e = p^k, k >= k0(p), primes < 200:", ok4); ok &= ok4
print("PASS" if ok else "FAIL")
