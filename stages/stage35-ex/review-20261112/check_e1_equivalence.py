# Stage35-EX continuation judgement 2026-11-12: small checks used by the report (no new research computation).
# (1) Identities behind "E1 <=> no perfect cuboid among Master-Hits" (notation of stage29/29-08/peschmann-exact-crosswalk.md):
#       e = U1 U2, x = V1 U2, y = U1 V2;  M = x^2 + y^2 (Master condition: M is a square);
#       H = (W1 U2)^2 + (U1 V2)^2 = e^2 + x^2 + y^2 (space diagonal squared);  xi^2 + eta^2 = H / g0^2.
#     So for a Master-Hit, xi^2 + eta^2 is a square  <=>  the Euler brick (e, x, y) is a perfect cuboid.
# (2) A numerical illustration on the smallest Euler brick family member found by a tiny search (not evidence of anything).
# (3) Size of the unconditional class-group task for signed -30: number of primes below 2^94 (prime number theorem estimate).
import math
import sympy as sp
a, b, m, n = sp.symbols("a b m n", positive=True)
U1, V1, W1 = a**2 - b**2, 2*a*b, a**2 + b**2
U2, V2, W2 = m**2 - n**2, 2*m*n, m**2 + n**2
e, x, y = U1*U2, V1*U2, U1*V2
H = (W1*U2)**2 + (U1*V2)**2
ok = True
ok &= sp.expand(H - (e**2 + x**2 + y**2)) == 0
ok &= sp.expand((W1*U2)**2 - (e**2 + x**2)) == 0          # face diagonal p
ok &= sp.expand((U1*W2)**2 - (e**2 + y**2)) == 0          # face diagonal q
print("(1) H = e^2 + x^2 + y^2 and the two automatic face diagonals:", ok)
hit = None
for A in range(2, 40):
    for B in range(1, A):
        for Mm in range(2, 40):
            for N in range(1, Mm):
                if math.gcd(A, B) != 1 or math.gcd(Mm, N) != 1: continue
                u1, v1, w1 = A*A - B*B, 2*A*B, A*A + B*B
                u2, v2 = Mm*Mm - N*N, 2*Mm*N
                Mval = (v1*u2)**2 + (u1*v2)**2
                r = math.isqrt(Mval)
                if r*r == Mval and hit is None:
                    Hval = (w1*u2)**2 + (u1*v2)**2
                    g0 = math.gcd(w1*u2, u1*v2)
                    xi, eta = w1*u2//g0, u1*v2//g0
                    s = xi*xi + eta*eta
                    hit = (A, B, Mm, N, u1*u2, v1*u2, u1*v2, math.isqrt(s)**2 == s, Hval == g0*g0*s)
print("(2) first Master-Hit in the box (a, b, m, n, e, x, y, xi^2+eta^2 square?, H = g0^2 (xi^2+eta^2)?):", hit)
ok &= hit is not None and hit[8] and not hit[7]
X = 2.0**94
print("(3) primes below 2^94 ~ %.2e ; at 1e9 primes per second: %.1e years" % (X/math.log(X), X/math.log(X)/1e9/3.15e7))
print("PASS" if ok else "FAIL")
