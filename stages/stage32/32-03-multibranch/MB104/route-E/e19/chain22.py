#!/usr/bin/env python3
"""E19 s.22: the chain of constants with two new links (2026-11-18).  Same chain as chain20.py (s.21, audited PASS),
with Lemma P and Theorem C replaced:

  * Lemma P' (s.22.1): decay of the anchor-free area A(r) = A(U_r) from the Gauss-Bonnet identity of the level sets
        A + coth(r) L = T + Psi      (T = sum over components of 2 pi (k - 2) + pi n_def, Psi = sum of corner angles)
    and the corner law  dphi/dr = -2 tan(phi/2) coth r.  With T <= alpha L (alpha = 2 pi / l0, every boundary curve
    has length >= l0 for r >= r0 > 0.865) the quantity Q = N + mu A, N = A + coth(r) L, satisfies Q' <= -c Q, so
        A(r) <= [A(r0) + coth(r0) L(r0) / (1 + mu)] e^{-c (r - r0)},   c (1 + mu) <= 1,  mu >= k (alpha + c - k), k in [1, coth r0].
    c = 0.399 (r0 = 0.9) instead of c = 1/(1 + alpha) = 0.327.  A(r0) <= 2 pi a, L(r0) <= (2a + 4) pi sinh r0.
  * Theorem C' (s.22.2): zeros of q' = sigma o p counted at their location (vertex, edge midpoint, face centre) and
    summed over all 24 sigma:  24 (a + b) >= 50 a + 2 - (49/3) M,  so  a <= 11 + (49/6) M  (was 11 + 216.3 M).
    M = number of vertices that are not good (bad vertices and seedless components, the factor 121 of s.21.4).

Everything else (eps, K, K1, kappa(t), R0, N_v, seedless 121) is copied unchanged from chain20.py.
usage: python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e19/chain22.py
"""
import math, sys
sys.dont_write_bytecode = True
L = math.acosh(1 + math.sqrt(2))            # l_min
l0 = 2 * L                                   # systole of Gamma_0 (s.15: arithmetic proof)
C_DECAY_OLD = 1 / (1 + 2 * math.pi / l0)     # Lemma P (s.13.2), used only in the comparison rows
ALPHA = 2 * math.pi / l0
R_P0 = 0.9                                   # start of Lemma P': pi sinh(r0) >= l0 needs r0 >= 0.865
THM_C = 49 / 6                               # Theorem C' (s.22.2); Theorem C (s.12.2) had 216.3


def lemma_p_prime(r0, alpha=ALPHA):
    """largest c with c (1 + mu) <= 1, mu = max_{k in [1, coth r0]} k (alpha + c - k).  Returns (c, mu, k0)."""
    k0 = 1 / math.tanh(r0)
    def mu_of(c):
        kk = min(max(1.0, (alpha + c) / 2), k0)
        return max(k * (alpha + c - k) for k in (1.0, k0, kk))
    lo, hi = 0.0, 1.0
    for _ in range(200):
        c = (lo + hi) / 2
        if c * (1 + mu_of(c)) <= 1: lo = c
        else: hi = c
    c = lo; mu = mu_of(c)
    for i in range(1001):                    # check the two conditions on a grid of k in [1, k0]
        k = 1 + (k0 - 1) * i / 1000
        assert k * k - k * alpha + mu - c * k >= -1e-12 and c * (1 + mu) <= k + 1e-12
    return c, mu, k0


C_DECAY, MU, K0 = lemma_p_prime(R_P0)
P1 = 2 * math.pi + K0 * 2 * math.pi * math.sinh(R_P0) / (1 + MU)     # A(r) <= (P1 a + P2) e^{-c(r - r0)}
P2 = K0 * 4 * math.pi * math.sinh(R_P0) / (1 + MU)                    # (from the +4 in #anchors <= 2a + 4)


def p2_of(k):
    """additive term for k defects: area(X) <= 2 pi (a + s), #cone points <= 2a + 4 + 2s, s <= k - 4 (s.16.2)"""
    s = max(0.0, k - 4)
    return P2 + 2 * math.pi * s * (1 + K0 * math.sinh(R_P0) / (1 + MU))
EPS0 = 0.2
R_SEED = 10.78
SEED_MAX = 4.8969                            # longest seed distance (s.11.2)
TAU_STAR = 5.0                               # assumed lower bound for the unit-neighbourhood depth on every path
SEEDLESS = 121                               # 1 + 8 + 8*14 (s.21.4; 61 without pinches/double edges, 73 the s.20.4 count, 169 audit safe side)
A_V = math.pi * (math.cosh(L / 2) - 1)       # smallest area per vertex (cone point: half of a disc of radius l/2)
log = math.log


def eps(R): return 2 * math.atanh(math.exp(-R))      # = -log tanh(R/2), without cancellation


def leps(R): return log(eps(R)) if R < 30 else log(2) - R + math.exp(-2 * R) / 3   # log eps, stable


def K_of(e):
    """interior estimate at the centre of a hyperbolic unit disc, disc model (metric lam^2|dz|^2, lam = 2/(1-|z|^2)).
    Delta_e w = lam^2 (e^{2w}-1); Euclidean radius r = tanh(1/2).  u = h + v (h harmonic, v Green potential of f):
    |grad h(0)| <= (2/r) sup|h|, sup|h| <= sup|w| + (r^2/4) sup|f|, |grad v(0)| <= r sup|f|.
    hyperbolic |grad| = Euclidean |grad| / lam(0) = /2.  Returns K with |grad w| + |w| <= K e."""
    r = math.tanh(0.5); lam = 2 / (1 - r * r)
    f = lam ** 2 * (math.exp(2 * e) - 1)
    ge = (2 / r) * (e + r * r / 4 * f) + r * f
    return (ge / 2 + e) / e


ESTAR = eps(TAU_STAR)
assert all(K_of(ESTAR * x) <= K_of(ESTAR) for x in (0.001, 0.01, 0.1, 0.5, 0.9))   # K increases with e
K = K_of(ESTAR)
K1 = K - 1 + math.exp(ESTAR)                 # Lemma T2': translation |e^w - 1| <= e^{eps} eps, rotation <= (K-1) eps
BETA = 1 / (1 - math.exp(-2 * TAU_STAR))     # eps(tau) <= 2 BETA e^{-tau} for tau >= tau*
GAMMA = 2 / (1 - math.exp(-2 * L))           # cosh(L - s)/sinh L <= GAMMA e^{-s} for L >= l_min
HFAC = 2 * math.sinh(L / 2) / L              # 2 sinh(E/2) <= HFAC E for E <= l_min


def kappa(t):
    """bad-threshold constant at depth t: every chain step at depth t pins (Thm T', s.21.2), closed form."""
    return 1 + log(BETA * K1 / L) + log(math.exp(8 * L / 3) + HFAC * GAMMA * (t + 4 * L / 3) * math.exp(4 * L / 3))


def rbad(t, coef=1/3): return coef * (t - kappa(t))     # coef != 1/3 only in the sensitivity table


def lsinh(x): return x - log(2) + log(1 - math.exp(-2 * x))      # log sinh x, x > 0


def pin_D(t, s, s2):
    """the un-simplified pinning bound D of Thm T' for a step from x (depth t, anchor distance s) to its neighbour x'
    (anchor distance s2), with the worst entry path L^- < t_c + 4l/3 and t_c >= t - s."""
    Lp = s + s2 + L                       # exit path length
    Rp = t - max(s, s2 + L) - 1           # exit path unit-neighbourhood depth
    tc = t - s
    direct = log(K1 * 2 * BETA) - Rp + lsinh(Lp)
    rot = log(HFAC * K1 * 2 * BETA * GAMMA * (tc + 4 * L / 3)) + 1 - tc + lsinh(Lp)
    return math.exp(lse(direct, rot)), Rp


def eps0_test(t):
    """G within eps0 of the identity on the unit disc around a good vertex at depth t (s.21.3), worst s = rbad(t)."""
    s = rbad(t)
    if s < 1: return False
    tau = t - max(s, 1) - 1
    direct = log(K1) + leps(tau) + lsinh(s + 1)
    rot = log(HFAC * K1 * 2 * BETA * GAMMA * (t - s + 4 * L / 3)) + 1 - (t - s) + lsinh(s + 1)
    return lse(direct, rot) < log(EPS0)


def chain(verbose=False):
    # R0: least t >= R_seed + l_min with the eps0 test for every t' >= t (grid check up to 3000)
    R0 = R_SEED + L
    grid = lambda a: [a + 0.05 * i for i in range(0, 2000)] + [a + 100 + 10 * i for i in range(300)]
    while not all(eps0_test(u) for u in grid(R0)): R0 += 0.01
    # checks of Thm T' on a grid of depths: worst s, s' (s' < r(t) + l/3), and the depth floor tau*
    tau_min = R0 - SEED_MAX - 1             # seed pairs
    for t in grid(R0):
        s = rbad(t) * (1 - 1e-12); s2 = (rbad(t) + L / 3) * (1 - 1e-12)
        for (a, b) in ((s, s2), (s, 0.0), (0.0, s2), (s / 2, s2)):
            D, Rp = pin_D(t, a, b)
            assert D < L, (t, a, b, D)
            tau_min = min(tau_min, Rp)
    assert tau_min >= TAU_STAR, tau_min
    for t in (R0, 50.0, 150.0, 1000.0):     # kappa' < 1, so r is nondecreasing (used in s.17.2 and s.21.2)
        assert (kappa(t + 1e-3) - kappa(t)) / 1e-3 < 1
    if verbose:
        print("  links: eps(tau*) = %.3e   K = %.3f [proved*]   K1 = %.3f [proved]   beta = %.6f   gamma = %.4f   h = %.4f"
              % (ESTAR, K, K1, BETA, GAMMA, HFAC))
        print("         kappa(t) = %.3f + log(%.2f + %.3f (t + %.3f))   kappa(R0) = %.3f   R0 = %.3f   log10 N_v(R0) = %.2f"
              % (1 + log(BETA * K1 / L), math.exp(8 * L / 3), HFAC * GAMMA * math.exp(4 * L / 3), 4 * L / 3,
                 kappa(R0), R0, logNv(R0) / log(10)))
        print("         smallest path depth used = %.3f >= tau* = %.1f   c = %.4f" % (tau_min, TAU_STAR, C_DECAY))
    return dict(R0=R0)


def logNv(R):
    """log of (cosh(R + l/2) - 1)/(cosh(l/2) - 1), stable for large R"""
    x = R + L / 2
    lc = x - log(2) + log(1 + math.exp(-2 * x)) if x > 20 else log(math.cosh(x))
    return lc + log(1 - math.exp(-lc)) - log(math.cosh(L / 2) - 1)


def lse(u, v): return max(u, v) + log(1 + math.exp(-abs(u - v)))


def log_untransportable(la, ch, k, c, Kshort=0.0, coef=1/3, lemma="P'"):
    """log of min over t0 of  k N_v(t0) + (area bound of U_{rbad(t0) - l/2} + short-circle term)/A_V ;  la = log a.
    Lemma P' (s.22.1): area <= (P1 a + P2) e^{-c (r - r0)}, short circles add 2 pi coth(r0) Kshort / (c (1 + mu)).
    lemma="P" gives the old Lemma P (2 pi a e^{-c (r - 1)}, short circles 2 pi Kshort), for the comparison rows."""
    rb = lambda t: rbad(t, coef)
    if lemma == "P":
        r0 = 1.0; lpref = log(2 * math.pi) + la; ks = 2 * math.pi * Kshort
    else:
        r0 = R_P0; lpref = lse(log(P1) + la, log(p2_of(k)))
        ks = 2 * math.pi * K0 * Kshort / (c * (1 + MU))
    tmin = ch["R0"]
    while rb(tmin) < r0 + L / 2: tmin += 0.01
    f = lambda t: lse(log(k) + logNv(t), lpref - log(A_V) - c * (rb(t) - r0 - L / 2))
    lo, hi = tmin, tmin + 3 * la + 200
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        m1 = hi - g * (hi - lo); m2 = lo + g * (hi - lo)
        if f(m1) < f(m2): hi = m2
        else: lo = m1
    v = min(f(lo), f(tmin))
    if Kshort > 0: v = lse(v, log(ks / A_V))
    return v


def log_bound(ch, k, Kshort=0.0, seedless=SEEDLESS, c=None, coef=1/3, thm_c=THM_C, lemma="P'"):
    """largest log a with a <= 11 + thm_c*seedless*(k N_v(R0) + untransportable(a))  (bisection on log a)."""
    if c is None: c = C_DECAY if lemma == "P'" else C_DECAY_OLD
    lnear = log(k) + logNv(ch["R0"])
    def rhs(la):
        return lse(log(11), log(thm_c * seedless) + lse(lnear, log_untransportable(la, ch, k, c, Kshort, coef, lemma)))
    lo, hi = 1.0, 5000.0
    if rhs(hi) > hi: return float("inf")
    for _ in range(80):
        mid = (lo + hi) / 2
        if rhs(mid) >= mid: lo = mid
        else: hi = mid
    return lo


L10 = log(10)
print("E19 s.22: chain of constants with Lemma P' (s.22.1) and Theorem C' (s.22.2); other links as in chain20.py (s.21)")
print("fixed: l_min = %.4f, l0 = %.4f, eps0 = %.2f, R_seed = %.2f [proved], A_V = %.4f, seedless = %d"
      % (L, l0, EPS0, R_SEED, A_V, SEEDLESS))
print("Lemma P': alpha = 2 pi/l0 = %.4f, r0 = %.2f, coth r0 = %.4f, mu = %.4f, c = %.4f (Lemma P: %.4f)"
      % (ALPHA, R_P0, K0, MU, C_DECAY, C_DECAY_OLD))
print("          area bound (P1 a + P2) e^{-c (r - r0)}: P1 = %.4f = %.3f * 2 pi, P2 = %.4f" % (P1, P1 / (2 * math.pi), P2))
print("Theorem C': a <= 11 + %.4f M   (Theorem C: 216.3)" % THM_C)
print()
print("1. mixed slack (0,0) (4 defects): the bound a_max")
ch = chain(verbose=True)
la = log_bound(ch, 4)
lnear = log(4) + logNv(ch["R0"])
lu = log_untransportable(la, ch, 4, C_DECAY)
assert lu > lnear      # still decided by the untransportable deep points
print("   log10 a_max = %.2f   (decided by the untransportable deep points, not by M(R0))" % (la / L10))
print("   floor from the defects alone: 11 + %.3f*%d*4 N_v(R0) = 10^%.2f" % (THM_C, SEEDLESS, (log(THM_C * SEEDLESS) + lnear) / L10))
print()
print("2. what each new link does (log10 a_max)")
rows = [
    ("s.21 (Lemma P, Theorem C 216.3)  [official before s.22]", dict(lemma="P", thm_c=216.3)),
    ("Lemma P' only (Theorem C 216.3)", dict(thm_c=216.3)),
    ("Theorem C' only (Lemma P)", dict(lemma="P")),
    ("both (s.22)", dict()),
]
for name, kw in rows:
    print("   %-58s %8.2f" % (name, log_bound(ch, 4, **kw) / L10))
print()
print("3. positive slack (S defects incl. non-standard points; short circles K_short = S N_v(1.5 l0)), both new links:")
print("   S          log10 b_max     log10 C' = log10(b_max/S)")
for S in (10, 1e3, 1e6, 1e12, 1e24):
    Ks = S * math.exp(logNv(1.5 * l0))
    lb = log_bound(ch, S, Ks)
    print("   %-8.0e   %10.2f     %10.2f" % (S, lb / L10, (lb - log(S)) / L10))
print("   (Theorem C' for positive slack: same count on the larger leg; the vertex total only grows with slack, s.16.2)")
print()
print("4. what moves the bound now: change one input at a time (both new links in place)")
base = la / L10
print("   base log10 a_max = %.2f" % base)
rows = [
    ("seedless 121 -> 61 (if pinches/double edges were excluded)", dict(seedless=61)),
    ("seedless 121 -> 1", dict(seedless=1)),
    ("coefficient 1/3 -> 1/2", dict(coef=0.5)),
    ("coefficient 1/3 -> 1 (s.17.3, chains moving away)", dict(coef=1.0)),
    ("c 0.399 -> 0.6", dict(c=0.6)),
    ("c 0.399 -> 1 (simply connected decay)", dict(c=1.0)),
    ("c -> 1 and coefficient -> 1", dict(c=1.0, coef=1.0)),
]
for name, kw in rows:
    print("   %-58s log10 a_max = %8.2f" % (name, log_bound(ch, 4, **kw) / L10))
print("   exponent 3/(3+c) = %.4f, so a_max ~ (constant)^{%.2f}" % (3 / (3 + C_DECAY), (3 + C_DECAY) / C_DECAY))
print("PASS")
