#!/usr/bin/env python3
"""Independent audit of K = 7.65 (E19 chain20.py, K_of).

Claim: if Delta_hyp w = e^{2w} - 1 on the hyperbolic unit disc B(z,1) and |w| <= eps there,
then |grad w(z)|_hyp + |w(z)| <= K eps, with K = 7.647 at eps = eps(10.78).

A. recompute K from scratch (mpmath, 30 digits)
B. check each ingredient numerically (quadrature)
C. exact solutions w = log(|F'| lam(F)/lam) for holomorphic F (Liouville): max observed ratio
D. linearised sharp constant (ODE for the modes of Delta - 2)
"""
import mpmath as mp, random, math
mp.mp.dps = 30

# ---------------- A ----------------
eps = -mp.log(mp.tanh(mp.mpf('10.78') / 2))
r = mp.tanh(mp.mpf(1) / 2)
assert abs(2 * mp.atanh(r) - 1) < mp.mpf(10) ** -25          # hyperbolic radius of |z|<=r is 1
lam_max = 2 / (1 - r ** 2)                                   # lambda is largest on the boundary
lam0 = mp.mpf(2)
F = lam_max ** 2 * (mp.e ** (2 * eps) - 1)                   # sup |Delta_euc w| on the disc
supv = r ** 2 / 4 * F                                         # |v| <= r^2/4 sup|f|  (v Dirichlet potential)
grad_h = (2 / r) * (eps + supv)                               # mean-value gradient bound, harmonic h
grad_v_code = r * F                                           # bound used in chain20.py
grad_v_true = 2 * r / 3 * F                                   # exact L1 norm of grad_x G(0,.)
K_code = (grad_h + grad_v_code) / lam0 / eps + 1
print("A. eps(R_seed) = %s" % mp.nstr(eps, 10))
print("   r = tanh(1/2) = %s, lam(r) = %s, sup|f|/eps = %s" % (mp.nstr(r, 10), mp.nstr(lam_max, 10), mp.nstr(F / eps, 10)))
print("   K (same inequalities as chain20.py) = %s" % mp.nstr(K_code, 10))
K_tight = ((4 / (mp.pi * r)) * (eps + supv) + grad_v_true) / lam0 / eps + 1
print("   K with the sharp versions of the two gradient bounds (4/(pi r), 2r/3) = %s" % mp.nstr(K_tight, 10))

# ---------------- B ----------------
print("B. ingredients")
# B1 harmonic gradient: grad P(.,theta) at 0 = e^{i theta}/(pi r) (per d theta); L1 norm over theta
l1 = mp.quad(lambda t: abs(mp.cos(t)) / (mp.pi * r), [0, mp.pi / 2, 3 * mp.pi / 2, 2 * mp.pi])
print("   harmonic: sup |grad h(0)| / sup|h| = %s  (code uses 2/r = %s)  ok=%s" % (mp.nstr(l1, 10), mp.nstr(2 / r, 10), l1 <= 2 / r))
# B2 Dirichlet Green function of the disc: G(x,y) = (1/2pi)(log|x-y| - log(|y||x-y*|/r)), y* = r^2 y/|y|^2
def gradG0(y):                      # |grad_x G(0,y)|, by finite differences in x
    def G(x):
        if abs(y) < 1e-30: return mp.log(abs(x - y)) / (2 * mp.pi)
        ys = r ** 2 * y / abs(y) ** 2
        return (mp.log(abs(x - y)) - mp.log(abs(y) * abs(x - ys) / r)) / (2 * mp.pi)
    h = mp.mpf(10) ** -12
    return abs((G(h) - G(-h)) / (2 * h) + 1j * (G(1j * h) - G(-1j * h)) / (2 * h))
l1G = mp.quad(lambda rho: 2 * mp.pi * rho * gradG0(rho * mp.e ** (0.3j)), [0, r])   # radial (|grad G| is rotation invariant)
print("   Green: integral of |grad_x G(0,y)| over the disc = %s ; 2r/3 = %s ; code uses r = %s" % (mp.nstr(l1G, 10), mp.nstr(2 * r / 3, 10), mp.nstr(r, 10)))
# B3 sup of the Dirichlet potential of 1: (r^2 - |x|^2)/4, max r^2/4
print("   Green: sup |v| for |f|<=1 is r^2/4 = %s (torsion function, exact)" % mp.nstr(r ** 2 / 4, 10))
# B4 |e^{2w}-1| <= e^{2 eps}-1 for |w|<=eps
print("   nonlinearity: 1-e^{-2eps} = %s <= e^{2eps}-1 = %s" % (mp.nstr(1 - mp.e ** (-2 * eps), 8), mp.nstr(mp.e ** (2 * eps) - 1, 8)))

# ---------------- C ----------------
# exact solutions: F holomorphic, |F|<1 on the closed disc; w = log((1-|z|^2)|F'| / (1-|F|^2)) solves Delta_hyp w = e^{2w}-1.
print("C. exact solutions from holomorphic F (Liouville)")
rf = float(r)
NR, NT = 24, 96
grid = [rf * (i / NR) * complex(math.cos(2 * math.pi * j / NT), math.sin(2 * math.pi * j / NT)) for i in range(1, NR + 1) for j in range(NT)]
def wfun(c, z):
    Fz = sum(ck * z ** k for k, ck in enumerate(c))
    dF = sum(k * ck * z ** (k - 1) for k, ck in enumerate(c) if k)
    return math.log((1 - abs(z) ** 2) * abs(dF) / (1 - abs(Fz) ** 2))
def ratio(c):
    w0 = wfun(c, 0j)
    h = 1e-5
    gx = (wfun(c, h) - wfun(c, -h)) / (2 * h); gy = (wfun(c, 1j * h) - wfun(c, -1j * h)) / (2 * h)
    ghyp = math.hypot(gx, gy) / 2                          # lambda(0) = 2
    sup = max(abs(w0), max(abs(wfun(c, z)) for z in grid))
    return (ghyp + abs(w0)) / sup, sup
random.seed(1)
best = (0, None)
for trial in range(300):
    deg = random.randint(2, 6)
    d = 10 ** random.uniform(-4, -2)
    c = [0j, 1 + 0j] + [0j] * (deg - 1)
    c = [ck + d * complex(random.gauss(0, 1), random.gauss(0, 1)) for ck in c]
    q, s = ratio(c)
    if q > best[0]: best = (q, c)
q0, c = best
# hill climb on the best one
step = 0.3
for it in range(400):
    c2 = [ck + step * abs(c[2]) * complex(random.gauss(0, 1), random.gauss(0, 1)) for ck in c]
    q2, s2 = ratio(c2)
    if q2 > q0 and s2 < 0.05: q0, c = q2, c2
    if it % 100 == 99: step /= 2
print("   300 random F + hill climbing: largest (|grad w(0)| + |w(0)|)/sup|w| = %.4f   (K = %.4f)" % (q0, float(K_code)))

# ---------------- D ----------------
# linearised problem Delta_hyp u = 2u on B(0,1) (hyperbolic polar coords rho), |u| <= 1 on the boundary.
# mode 0: g0'' + coth g0' = 2 g0, g0(0)=1;  mode 1: g1'' + coth g1' - g1/sinh^2 = 2 g1, g1 ~ rho.
def solve(m):
    if m == 0:
        f = lambda t, y: [y[1], 2 * y[0] - mp.coth(t) * y[1]]
        t0 = mp.mpf('1e-6'); y0 = [1 + t0 ** 2 / 2, t0]          # g0 = 1 + rho^2/2 + ...
    else:
        f = lambda t, y: [y[1], 2 * y[0] + y[0] / mp.sinh(t) ** 2 - mp.coth(t) * y[1]]
        t0 = mp.mpf('1e-6'); y0 = [t0, 1]
    sol = mp.odefun(f, t0, y0)
    return sol(1)[0]
g0 = solve(0); g1 = solve(1)
a = 1 / (mp.pi * g1)           # grad part of kernel: a cos(theta)  (g1'(0) = 1)
b = 1 / (2 * mp.pi * g0)       # value part: b
Klin = mp.quad(lambda t: abs(a * mp.cos(t) + b), [0, mp.acos(-b / a), 2 * mp.pi - mp.acos(-b / a), 2 * mp.pi]) if b < a else 2 * mp.pi * b
print("D. linearised sharp constant: g0(1) = %s, g1(1) = %s" % (mp.nstr(g0, 8), mp.nstr(g1, 8)))
print("   sharp sup |grad u(0)| = %s ;  sharp sup(|grad u(0)| + |u(0)|) = %s" % (mp.nstr(4 / (mp.pi * g1), 8), mp.nstr(Klin, 8)))
print("   (for comparison, the code's K = %s is %.2f times the sharp value)" % (mp.nstr(K_code, 8), float(K_code / Klin)))
# the extremal datum sign(a cos + b) on the boundary realises Klin; this is consistent with C if C < Klin(1+o(1)).
print("   ratio eps(R-1)/eps(R) at R = 10.78: %s" % mp.nstr(mp.log(mp.tanh(mp.mpf('9.78') / 2)) / mp.log(mp.tanh(mp.mpf('10.78') / 2)), 8))
