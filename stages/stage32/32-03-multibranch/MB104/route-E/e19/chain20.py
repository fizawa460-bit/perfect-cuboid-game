#!/usr/bin/env python3
"""E19 stage 0: the chain of constants of sections 11-17, computed in order (revised 2026-11-18, E19 s.21).

    eps0 -> R_seed -> K (gradient) -> kappa(t) (pinning, s.21) -> R0 -> M(R0) -> untransportable count -> bound

Second revision (E19 s.21, closes the hole of s.20.3 and removes both [est] inputs):
  * Lemma T2' (s.21.1): the 2-jet constant is exact.  The Maurer-Cartan field of z -> A_z has translation part
    |e^w - 1| and rotation part <= |grad w| per unit length, so the old C_X [est] is replaced by
    K1 = K(eps*) - 1 + e^{eps*} (K = interior estimate, audited PASS).
  * Theorem T' (s.21.2): the rotation carried over is bounded by integrating T2' with the POINTWISE eps along the
    entry path; it is decided by the depth of the anchor, not by the entry path.  The old factor 3 [est] is replaced
    by the explicit pinning inequality  beta K1 e^{1-kappa} [e^{8l/3} + h gamma (t + 4l/3) e^{4l/3}] <= l_min,
    i.e. kappa(t) = 1 + log(beta K1 / l_min) + log(e^{8l/3} + h gamma (t + 4l/3) e^{4l/3})   (the log term).
  * Seedless components (s.21.4): Gauss-Bonnet on the resolved closed-star complex, with pinches, holes and double
    edges allowed: interior <= 14 |boundary|, so the factor is 1 + 8 + 8*14 = 121 (61 with no pinches and no double edges).
Earlier revision (E19 s.20): eps(R) = 2 atanh(e^{-R}); true minimum over t0; area shift l/2.

Labels:  [proved] = formula from a proved statement with an explicit constant;
         [outline] = statement of E19 that is an outline (audited as outline only).
There is no [est] input any more.  Everything is floating point (log scale where numbers are huge).

Links (E19 section numbers):
  eps(R)   = 2 atanh(e^{-R}) = -log tanh(R/2)  |w| at R-deep points (E14 Prop. L(b), s.7.2)         [proved]
  K        : |grad w| + |w| <= K eps at the centre of a unit disc where |w| <= eps                    [proved*]
             (*elementary interior estimate for Delta w = e^{2w} - 1; audited PASS)
  K1       = K(eps*) - 1 + e^{eps*}: |X| <= K1 eps(tau) (Lemma T2', s.21.1)                          [proved]
  kappa(t) : pinning at the next anchor (delta_1 = l_min) for every chain step at depth t (Thm T', s.21.2) [proved]
  bad      : anchor distance s >= r(t) = (t - kappa(t))/3 at depth t (s.15.1, s.21.3)               [outline]
  eps0=0.2 : good vertex = G within eps0 of the identity on the unit disc (s.12.4)                  [proved]
  R_seed   = 10.78 (sheet condition for pair seeds, E13 R_B(3.2), s.15.3)                          [proved]
  R0       : >= R_seed + l_min and the eps0 test holds for all t >= R0 (s.21.3)
  tau*     = 5: every path used has unit-neighbourhood depth >= tau* (checked below)
  N_v(R)   = (cosh(R + l/2) - 1)/(cosh(l/2) - 1)  vertices in an H-ball (packing)                   [proved]
  Lemma P  : c = 1/(1 + 2 pi/l0), l0 = 2 l_min (s.13.2, s.15)                                       [outline]
  seedless : x (1 + 8 + 8*14) = 121 (s.21.4)                                                         [outline: uses s.15.2]
  Thm C    : a <= 11 + 216.3 M_bad (slack 0, s.12.2);  b <= 11 + 216.3 M_bad on the larger leg       [outline]
usage: python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e19/chain20.py
"""
import math, sys
sys.dont_write_bytecode = True
L = math.acosh(1 + math.sqrt(2))            # l_min
l0 = 2 * L                                   # systole of Gamma_0 (s.15: arithmetic proof)
C_DECAY = 1 / (1 + 2 * math.pi / l0)
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


def log_untransportable(la, ch, k, c, Kshort=0.0, coef=1/3):
    """log of min over t0 of  k N_v(t0) + (2 pi a e^{-c(rbad(t0) - 1 - l/2)} + 2 pi Kshort)/A_V ;  la = log a.
    (Lemma P needs r - l/2 >= r0 = 1.)  True minimum by golden-section search (the function is unimodal)."""
    rb = lambda t: rbad(t, coef)
    tmin = ch["R0"]
    while rb(tmin) < 1 + L / 2: tmin += 0.01
    f = lambda t: lse(log(k) + logNv(t), log(2 * math.pi / A_V) + la - c * (rb(t) - 1 - L / 2))
    lo, hi = tmin, tmin + 3 * la + 200
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        m1 = hi - g * (hi - lo); m2 = lo + g * (hi - lo)
        if f(m1) < f(m2): hi = m2
        else: lo = m1
    v = min(f(lo), f(tmin))
    if Kshort > 0: v = lse(v, log(2 * math.pi * Kshort / A_V))
    return v


def log_bound(ch, k, Kshort=0.0, seedless=SEEDLESS, c=C_DECAY, coef=1/3):
    """largest log a with a <= 11 + 216.3*seedless*(k N_v(R0) + untransportable(a))  (bisection on log a)."""
    lnear = log(k) + logNv(ch["R0"])
    def rhs(la):
        return lse(log(11), log(216.3 * seedless) + lse(lnear, log_untransportable(la, ch, k, c, Kshort, coef)))
    lo, hi = 1.0, 5000.0
    if rhs(hi) > hi: return float("inf")
    for _ in range(80):
        mid = (lo + hi) / 2
        if rhs(mid) >= mid: lo = mid
        else: hi = mid
    return lo


L10 = log(10)
print("E19 stage 0: chain of constants (sections 11-17; s.20 audits; s.21 Lemma T2', Theorem T', seedless 121)")
print("fixed: l_min = %.4f, l0 = %.4f, c = %.4f, eps0 = %.2f, R_seed = %.2f [proved], A_V = %.4f, seedless = %d"
      % (L, l0, C_DECAY, EPS0, R_SEED, A_V, SEEDLESS))
print()
print("1. mixed slack (0,0) (4 defects): the bound a_max (no [est] input; T2 hole closed)")
ch = chain(verbose=True)
la = log_bound(ch, 4)
lnear = log(4) + logNv(ch["R0"])
lu = log_untransportable(la, ch, 4, C_DECAY)
assert lu > lnear      # decided by the untransportable deep points (a^0.90), not by M(R0)
print("   log10 a_max = %.2f   (decided by the untransportable deep points, not by M(R0))" % (la / L10))
print("   depth of the worst bad point ~ log a: kappa(log a_max) = %.3f" % kappa(la))
print()
print("2. positive slack (S defects incl. non-standard points; short circles K_short = S N_v(1.5 l0)):")
print("   b_max(S) and the slope C' = b_max/S; the closed range is rho = S/b <~ 1/C'")
print("   S          log10 b_max     log10 C' = log10(b_max/S)")
for S in (10, 1e3, 1e6, 1e12, 1e24):
    Ks = S * math.exp(logNv(1.5 * l0))
    lb = log_bound(ch, S, Ks)
    print("   %-8.0e   %10.2f     %10.2f" % (S, lb / L10, (lb - log(S)) / L10))
print()
print("3. structural limit (s.17.3): deep area survives only if sigma e^{R0} <~ b, i.e. rho <~ e^{-R0} = %.2e" % math.exp(-ch["R0"]))
print("   (for R0 = %.2f).  Seeds alone need R_seed = %.2f: rho <~ %.2e." % (ch["R0"], R_SEED, math.exp(-R_SEED)))
print()
print("4. what moves the bound: change one input at a time and recompute log10 a_max")
base = la / L10
print("   base log10 a_max = %.2f" % base)
rows = [
    ("seedless 121 -> 61 (if pinches/double edges were excluded)", lambda: log_bound(ch, 4, seedless=61)),
    ("seedless 121 -> 73 (the s.20.4 count)", lambda: log_bound(ch, 4, seedless=73)),
    ("seedless 121 -> 169 (audit's safe side)", lambda: log_bound(ch, 4, seedless=169)),
    ("coefficient 1/3 -> 1 (s.17.3, chains moving away)", lambda: log_bound(ch, 4, coef=1.0)),
    ("c 0.327 -> 1 (simply connected decay)", lambda: log_bound(ch, 4, c=1.0)),
]
for name, fn in rows:
    print("   %-58s log10 a_max = %8.2f" % (name, fn() / L10))
print("   exponent 3/(3+c) = %.4f, so a_max ~ (constant)^{%.2f}" % (3 / (3 + C_DECAY), (3 + C_DECAY) / C_DECAY))
print("PASS")
