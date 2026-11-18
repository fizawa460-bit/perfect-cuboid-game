#!/usr/bin/env python3
"""E19 stage 0 (roadmap, 2026-11-18): the chain of constants of sections 11-17, computed in order.

    eps0 -> R_seed -> K (gradient) -> C0 -> R0 -> M(R0) -> untransportable count -> final bound

Revised 2026-11-18 after three independent audits (E19 s.20):
  (1) eps(R) is computed as 2 atanh(e^{-R}) (= -log tanh(R/2)); the old form lost precision for R > 35 and
      inflated C0 by 0.65.  C0 now has the closed form log(3 C_X K / l_min) (eps(R) sinh(R - C) increases to e^{-C}).
  (2) the untransportable count takes the true minimum over t0 (s.17.2), not the crossing of the two terms.
  (3) bad threshold kappa = C0 + 1 + 8 l/3 = C0 + 5.08 (was C0 + 4.06; neighbour s' <= s + l and min(R_{k-1}, R_k)).
  (4) seedless factor 1 + 8 + 64 = 73 (was 65; the boundary vertices of a seedless component are not good either).
  (5) area -> vertex count: a vertex of U_r has its l/2-disc in U_{r - l/2}, so the exponent gets - l/2.
  (6) [outline] Lemma T2 integrated with the pointwise eps: the rotation carried over costs a factor (1 + L_{k-1}),
      L_{k-1} <= t, i.e. kappa(t) = C0 + 5.08 + log(1 + t).  Reported as a second headline ("with log term").

Labels:  [proved] = formula from a proved statement with an explicit constant;
         [outline] = statement of E19 that is an outline (audited as outline only);
         [est]    = constant not yet derived (a stated guess, varied in the sensitivity table).
Everything is floating point (log scale where numbers are huge).  Nothing here is a proof.

Links (E19 section numbers):
  eps(R)   = -log tanh(R/2)                    |w| at R-deep points (E14 Prop. L(b), s.7.2)         [proved]
  K        : |grad w| + |w| <= K eps on a unit hyperbolic disc where |w| <= eps                    [proved*]
             (*elementary interior estimate for Delta w = e^{2w} - 1; audited PASS, best constant ~1.16)
  C_X      : |X|_z <= C_X (|grad w| + |w|)   (2-jet of the best isometry, s.7.2 (1))               [est]
  E(L)     = 3 C_X K eps sinh L                transport error over a geodesic of length L,
                                               factor 3 = direct term + rotation carried over (s.9.2) [est]
  C0       : E < l_min whenever L <= R - C0  (pinning at the next anchor, delta_1 = l_min, s.9.1)
  bad      : anchor distance s >= (t - kappa)/3 at depth t, kappa = C0 + 5.08 (s.15.1, s.20)       [outline]
  eps0=0.2 : good vertex = F within eps0 of a lift of sigma on the unit disc (s.12.4)
  R_seed   = 10.78 (sheet condition for pair seeds, E13 R_B(3.2), s.15.3)                        [proved]
  R0       : >= R_seed + l_min (margin chosen here; s.15.3 says only "10.78 + margin")
  N_v(R)   = (cosh(R + l/2) - 1)/(cosh(l/2) - 1)  vertices in an H-ball (packing)                 [proved]
  Lemma P  : c = 1/(1 + 2 pi/l0), l0 = 2 l_min (s.13.2, s.15)                                     [outline]
  seedless : x (1 + 8 + 64) = 73 (interior <= 8 |dH|, |dH| <= 8 x bad, s.14.4, s.15.2, s.20)       [outline]
  Thm C    : a <= 11 + 216.3 M_bad (slack 0, s.12.2);  b <= 11 + 216.3 M_bad on the larger leg     [outline]
usage: python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e19/chain20.py
"""
import math, sys
sys.dont_write_bytecode = True
L = math.acosh(1 + math.sqrt(2))            # l_min
l0 = 2 * L                                   # systole of Gamma_0 (s.15: arithmetic proof)
C_DECAY = 1 / (1 + 2 * math.pi / l0)
EPS0 = 0.2
R_SEED = 10.78
KAPPA_ADD = 1 + 8 * L / 3                    # 5.0762 (s.20; was 4.06)
SEEDLESS = 73                                # 1 + 8 + 64 (s.20; was 65)
A_V = math.pi * (math.cosh(L / 2) - 1)       # smallest area per vertex (cone point: half of a disc of radius l/2)
log = math.log


def eps(R): return 2 * math.atanh(math.exp(-R))      # = -log tanh(R/2), without cancellation


def K_of(e):
    """interior estimate at the centre of a hyperbolic unit disc, disc model (metric lam^2|dz|^2, lam = 2/(1-|z|^2)).
    Delta_e w = lam^2 (e^{2w}-1); Euclidean radius r = tanh(1/2).  u = h + v (h harmonic, v Green potential of f):
    |grad h(0)| <= (2/r) sup|h|, sup|h| <= sup|w| + (r^2/4) sup|f|, |grad v(0)| <= r sup|f|.
    hyperbolic |grad| = Euclidean |grad| / lam(0) = /2."""
    r = math.tanh(0.5); lam = 2 / (1 - r * r)
    f = lam ** 2 * (math.exp(2 * e) - 1)
    ge = (2 / r) * (e + r * r / 4 * f) + r * f
    return (ge / 2 + e) / e


def chain(CX, logterm=False, coef=1/3, R_seed=None, verbose=False):
    R_seed = R_SEED if R_seed is None else R_seed
    K = K_of(eps(R_seed))
    E = lambda e, Ld: 3 * CX * K * e * math.sinh(Ld)
    # C0: sup over R >= R_seed of the least C with E(eps(R), R - C) < l_min.  eps(R) sinh(R - C) increases in R
    # with limit e^{-C}, so the sup is the limit.  Checked numerically below.
    C0 = log(3 * CX * K / L)
    for R in (R_seed, R_seed + 5, R_seed + 15, 30.0):
        assert E(eps(R), R - C0) <= L * (1 + 1e-12)
    kappa = (lambda t: C0 + KAPPA_ADD + log(1 + t)) if logterm else (lambda t: C0 + KAPPA_ADD)
    rbad = lambda t: coef * (t - kappa(t))       # anchor distance from which a depth-t point is bad
    # R0: least depth such that good vertices meet eps0 (transport over s + 1 at path depth t - s - 1)
    def ok_depth(t):
        s = (t - kappa(t)) / 3      # transport is always checked with the coefficient 1/3 of s.15.1
        if s < 1: return False
        fac = (2 + s) if logterm else 1.0
        return fac * E(eps(max(t - s - 1, 1e-9)), s + 1) < EPS0
    R0 = R_seed + L
    while not ok_depth(R0): R0 += 0.01
    if verbose:
        print("  links: eps(R_seed) = %.3e   K = %.3f [proved*]   C_X = %.1f [est]" % (eps(R_seed), K, CX))
        print("         C0 = %.3f   kappa = C0 + %.3f%s   R0 = %.3f   log10 N_v(R0) = %.2f   c = %.4f"
              % (C0, KAPPA_ADD, " + log(1+t)" if logterm else "", R0, logNv(R0) / log(10), C_DECAY))
    return dict(K=K, C0=C0, R0=R0, rbad=rbad)


def logNv(R):
    """log of (cosh(R + l/2) - 1)/(cosh(l/2) - 1), stable for large R"""
    x = R + L / 2
    lc = x - log(2) + log(1 + math.exp(-2 * x)) if x > 20 else log(math.cosh(x))
    return lc + log(1 - math.exp(-lc)) - log(math.cosh(L / 2) - 1)


def lse(u, v): return max(u, v) + log(1 + math.exp(-abs(u - v)))


def log_untransportable(la, ch, k, c, Kshort=0.0):
    """log of min over t0 of  k N_v(t0) + (2 pi a e^{-c(rbad(t0) - 1 - l/2)} + 2 pi Kshort)/A_V ;  la = log a.
    (Lemma P needs r - l/2 >= r0 = 1.)  True minimum by golden-section search (the function is unimodal)."""
    rb = ch["rbad"]
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


def log_bound(ch, k, Kshort=0.0, seedless=SEEDLESS, c=C_DECAY):
    """largest log a with a <= 11 + 216.3*seedless*(k N_v(R0) + untransportable(a))  (bisection on log a)."""
    lnear = log(k) + logNv(ch["R0"])
    def rhs(la):
        return lse(log(11), log(216.3 * seedless) + lse(lnear, log_untransportable(la, ch, k, c, Kshort)))
    lo, hi = 1.0, 5000.0
    if rhs(hi) > hi: return float("inf")
    for _ in range(80):
        mid = (lo + hi) / 2
        if rhs(mid) >= mid: lo = mid
        else: hi = mid
    return lo


L10 = log(10)
print("E19 stage 0: chain of constants (sections 11-17, revised after the audits of s.20)")
print("fixed: l_min = %.4f, l0 = %.4f, c = %.4f, eps0 = %.2f, R_seed = %.2f [proved], A_V = %.4f, kappa - C0 = %.3f, seedless = %d"
      % (L, l0, C_DECAY, EPS0, R_SEED, A_V, KAPPA_ADD, SEEDLESS))
print()
print("1. mixed slack (0,0) (4 defects): the final bound a_max, and which term decides it")
print("   C_X [est]     C0      R0     log10 N_v(R0)   log10 a_max   log10 a_max (with log term, outline)")
for CX in (1.0, 2.0, 5.0, 10.0):
    ch = chain(CX, verbose=(CX == 2.0))
    la = log_bound(ch, 4)
    lnear = log(4) + logNv(ch["R0"])
    lu = log_untransportable(la, ch, 4, C_DECAY)
    assert lu > lnear      # decided by the untransportable deep points (a^0.90), not by M(R0)
    la2 = log_bound(chain(CX, logterm=True), 4)
    print("   %6.1f     %6.3f  %6.3f   %10.2f      %10.2f    %10.2f" % (CX, ch["C0"], ch["R0"], logNv(ch["R0"]) / L10, la / L10, la2 / L10))
print("   (in every row the bound is decided by the untransportable deep points, not by M(R0))")
print()
print("2. positive slack (S defects incl. non-standard points; short circles K_short = S N_v(1.5 l0)):")
print("   b_max(S) and the slope C' = b_max/S; the closed range is rho = S/b <~ 1/C'")
ch = chain(2.0)
print("   S          log10 b_max     log10 C' = log10(b_max/S)")
for S in (10, 1e3, 1e6, 1e12, 1e24):
    Ks = S * math.exp(logNv(1.5 * l0))
    la = log_bound(ch, S, Ks)
    print("   %-8.0e   %10.2f     %10.2f" % (S, la / L10, (la - log(S)) / L10))
print()
print("3. structural limit (s.17.3): deep area survives only if sigma e^{R0} <~ b, i.e. rho <~ e^{-R0} = %.2e" % math.exp(-ch["R0"]))
print("   (for R0 = %.2f at C_X = 2).  Seeds alone need R_seed = %.2f: rho <~ %.2e." % (ch["R0"], R_SEED, math.exp(-R_SEED)))
print()
print("4. what moves the bound (C_X = 2): change one input at a time and recompute log10 a_max")
base = log_bound(chain(2.0), 4) / L10
print("   base log10 a_max = %.2f" % base)
rows = [
    ("R_seed 10.78 -> 4.98 (ANSWER-09 radius)", lambda: log_bound(chain(2.0, R_seed=4.98), 4)),
    ("seedless 73 -> 169 (pinches/holes, safe side)", lambda: log_bound(chain(2.0), 4, seedless=169)),
    ("with log term kappa += log(1+t) (outline)", lambda: log_bound(chain(2.0, logterm=True), 4)),
    ("log term and seedless 169 (all safe side)", lambda: log_bound(chain(2.0, logterm=True), 4, seedless=169)),
    ("coefficient 1/3 -> 1 (s.17.3, chains moving away)", lambda: log_bound(chain(2.0, coef=1.0), 4)),
    ("c 0.327 -> 1 (simply connected decay)", lambda: log_bound(chain(2.0), 4, c=1.0)),
]
for name, fn in rows:
    print("   %-52s log10 a_max = %8.2f" % (name, fn() / L10))
print("   exponent 3/(3+c) = %.4f, so a_max ~ (constant)^{%.2f}" % (3 / (3 + C_DECAY), (3 + C_DECAY) / C_DECAY))
print("PASS")
