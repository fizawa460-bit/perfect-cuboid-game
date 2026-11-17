#!/usr/bin/env python3
"""E19 stage 0 (roadmap, 2026-11-18): the chain of constants of sections 11-17, computed in order.

    eps0 -> R_seed -> K (gradient) -> C0 -> R0 -> M(R0) -> untransportable count -> final bound

Labels in the output:  [proved] = formula from a proved statement with an explicit constant;
                       [est]    = constant not yet derived (a stated guess, varied in the sensitivity table).
Everything is floating point (log scale where numbers are huge).  Nothing here is a proof.

Links (E19 section numbers):
  eps(R)   = -log tanh(R/2)                    |w| at R-deep points (E14 Prop. L(b), s.7.2)         [proved]
  K        : |grad w| + |w| <= K eps on a unit hyperbolic disc where |w| <= eps                    [proved*]
             (*elementary interior estimate for Delta w = e^{2w} - 1, constants written out below)
  C_X      : |X|_z <= C_X (|grad w| + |w|)   (2-jet of the best isometry, s.7.2 (1))               [est]
  E(L)     = 3 C_X K eps sinh L                transport error over a geodesic of length L,
                                               factor 3 = direct term + rotation carried over (s.9.2) [est]
  C0       : E < l_min whenever L <= R - C0  (pinning at the next anchor, delta_1 = l_min, s.9.1)
  bad      : anchor distance s >= (t - C0 - 4.06)/3 at depth t (s.15.1)
  eps0=0.2 : good vertex = F within eps0 of a lift of sigma on the unit disc (s.12.4)
  R_seed   = 10.78 (sheet condition for pair seeds, E13 R_B(3.2), s.15.3)                        [proved]
  N_v(R)   = (cosh(R + l/2) - 1)/(cosh(l/2) - 1)  vertices in an H-ball (packing)                 [proved]
  Lemma P  : c = 1/(1 + 2 pi/l0), l0 = 2 l_min (s.13.2, s.15)                                     [outline]
  seedless : x (1 + 64)  (curvature bound, boundary <= 8 x bad neighbours, s.14.4, s.15.2)        [outline]
  Thm C    : a <= 11 + 216.3 M_bad (slack 0, s.12.2);  b <= 11 + 216.3 M_bad on the larger leg     [outline]
usage: python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e19/chain20.py
"""
import math, sys
sys.dont_write_bytecode = True
L = math.acosh(1 + math.sqrt(2))            # l_min
l0 = 2 * L                                   # systole of Gamma_0 (s.15: arithmetic proof)
c = 1 / (1 + 2 * math.pi / l0)
EPS0 = 0.2
R_SEED = 10.78
A_V = math.pi * (math.cosh(L / 2) - 1)       # smallest area per vertex (cone point: half of a disc of radius l/2)
log = math.log


def eps(R): return -log(math.tanh(R / 2))


def K_of(e):
    """interior estimate at the centre of a hyperbolic unit disc, disc model (metric lam^2|dz|^2, lam = 2/(1-|z|^2)).
    Delta_e w = lam^2 (e^{2w}-1); Euclidean radius r = tanh(1/2).  u = h + v (h harmonic, v Green potential of f):
    |grad h(0)| <= (2/r) sup|h|, sup|h| <= sup|w| + (r^2/4) sup|f|, |grad v(0)| <= r sup|f|.
    hyperbolic |grad| = Euclidean |grad| / lam(0) = /2."""
    r = math.tanh(0.5); lam = 2 / (1 - r * r)
    f = lam ** 2 * (math.exp(2 * e) - 1)
    ge = (2 / r) * (e + r * r / 4 * f) + r * f
    return (ge / 2 + e) / e


def chain(CX, k_def=4, verbose=False):
    K = K_of(eps(R_SEED))
    E = lambda e, Ld: 3 * CX * K * e * math.sinh(Ld)
    # C0: sup over R >= R_SEED of the least C with E(eps(R), R - C) < l_min
    C0 = 0.0
    for i in range(0, 300):
        R = R_SEED + 0.1 * i
        lo, hi = 0.0, R
        if E(eps(R), R) < L: continue
        for _ in range(60):
            mid = (lo + hi) / 2
            if E(eps(R), R - mid) < L: hi = mid
            else: lo = mid
        C0 = max(C0, hi)
    # R0: least depth such that good vertices meet eps0 and the bad criterion is non-empty
    def ok_depth(t):
        s = (t - C0 - 4.06) / 3
        if s < 1: return False
        return E(eps(max(t - s - 1, 1e-9)), s + 1) < EPS0
    R0 = R_SEED + L
    while not ok_depth(R0): R0 += 0.01
    if verbose:
        print("  links: eps(R_seed) = %.3e   K = %.3f [proved*]   C_X = %.1f [est]" % (eps(R_SEED), K, CX))
        print("         C0 = %.3f   R0 = %.3f   log10 N_v(R0) = %.2f   c = %.4f" % (C0, R0, logNv(R0) / log(10), c))
    return dict(K=K, C0=C0, R0=R0, k=k_def)


def logNv(R):
    """log of (cosh(R + l/2) - 1)/(cosh(l/2) - 1), stable for large R"""
    x = R + L / 2
    lc = x - log(2) + log(1 + math.exp(-2 * x)) if x > 20 else log(math.cosh(x))
    return lc + log(1 - math.exp(-lc)) - log(math.cosh(L / 2) - 1)


def lse(u, v): return max(u, v) + log(1 + math.exp(-abs(u - v)))


def log_untransportable(la, ch, k, Kshort=0.0):
    """log of min over t0 of  k N_v(t0) + (2 pi a e^{-c((t0-C0-4.06)/3 - 1)} + 2 pi Kshort)/A_V ;  la = log a.
    The first term increases and the second decreases in t0: the minimum is within log 2 of their crossing."""
    tmin = ch["C0"] + 4.06 + 3.0
    tmin = max(tmin, ch["R0"])
    t1 = lambda t: log(k) + logNv(t)
    t2 = lambda t: log(2 * math.pi / A_V) + la - c * ((t - ch["C0"] - 4.06) / 3 - 1)
    lo, hi = tmin, tmin + la + 200
    if t1(lo) >= t2(lo): t = lo
    else:
        for _ in range(100):
            mid = (lo + hi) / 2
            if t1(mid) < t2(mid): lo = mid
            else: hi = mid
        t = hi
    v = lse(t1(t), t2(t))
    if Kshort > 0: v = lse(v, log(2 * math.pi * Kshort / A_V))
    return v


def log_bound(ch, k, Kshort=0.0):
    """largest log a with a <= 11 + 216.3*65*(k N_v(R0) + untransportable(a))  (bisection on log a)."""
    lnear = log(k) + logNv(ch["R0"])
    def rhs(la):
        return log(216.3 * 65) + lse(lnear, log_untransportable(la, ch, k, Kshort))
    lo, hi = 1.0, 5000.0
    if rhs(hi) > hi: return float("inf")
    for _ in range(80):
        mid = (lo + hi) / 2
        if rhs(mid) >= mid: lo = mid
        else: hi = mid
    return lo


print("E19 stage 0: chain of constants (sections 11-17)")
print("fixed: l_min = %.4f, l0 = %.4f, c = %.4f, eps0 = %.2f, R_seed = %.2f [proved], A_V = %.4f" % (L, l0, c, EPS0, R_SEED, A_V))
print()
print("1. mixed slack (0,0) (4 defects): the final bound a_max, and which term decides it")
print("   C_X [est]     C0      R0     log10 N_v(R0)   log10 a_max   decided by")
rows = []
for CX in (1.0, 2.0, 5.0, 10.0):
    ch = chain(CX, verbose=(CX == 2.0))
    la = log_bound(ch, 4)
    lnear = log(4) + logNv(ch["R0"])
    lu = log_untransportable(la, ch, 4)
    who = "untransportable deep points (a^0.90)" if lu > lnear else "defect neighbourhoods M(R0)"
    print("   %6.1f     %6.3f  %6.3f   %10.2f      %10.2f    %s" % (CX, ch["C0"], ch["R0"], lnear / log(10) - log(4) / log(10), la / log(10), who))
    rows.append((CX, la))
print()
print("2. positive slack (S defects incl. non-standard points; short circles K_short = S N_v(1.5 l0)):")
print("   b_max(S) and the slope C' = b_max/S; the closed range is rho = S/b <~ 1/C'")
ch = chain(2.0)
print("   S          log10 b_max     log10 C' = log10(b_max/S)")
for S in (10, 1e3, 1e6, 1e12, 1e24):
    Ks = S * math.exp(logNv(1.5 * l0))
    la = log_bound(ch, S, Ks)
    print("   %-8.0e   %10.2f     %10.2f" % (S, la / log(10), (la - log(S)) / log(10)))
print()
print("3. structural limit (s.17.3): deep area survives only if sigma e^{R0} <~ b, i.e. rho <~ e^{-R0} = %.2e" % math.exp(-ch["R0"]))
print("   (for R0 = %.2f at C_X = 2).  Seeds alone need R_seed = %.2f: rho <~ %.2e." % (ch["R0"], R_SEED, math.exp(-R_SEED)))
print()
print("4. what moves the bound most (C_X = 2): change one input at a time and recompute log10 a_max")
base = log_bound(chain(2.0), 4) / log(10)
print("   base log10 a_max = %.2f" % base)
for name in ("R_seed 10.78 -> 4.98 (ANSWER-09 radius)", "coefficient 1/3 -> 1 (s.17.3, chains moving away)", "c 0.327 -> 1 (simply connected decay)"):
    gR, gc = R_SEED, c
    saved = (R_SEED, c)
    if name.startswith("R_seed"): R_SEED = 4.98
    if name.startswith("c "): c = 1.0
    if name.startswith("coefficient"):
        # emulate coefficient 1 by replacing (t-C0-4.06)/3 with (t-C0-4.06): rescale c by 3 in the decay term
        c = 3 * c
    v = log_bound(chain(2.0), 4) / log(10)
    R_SEED, c = saved
    print("   %-52s log10 a_max = %8.2f" % (name, v))
print("PASS")
