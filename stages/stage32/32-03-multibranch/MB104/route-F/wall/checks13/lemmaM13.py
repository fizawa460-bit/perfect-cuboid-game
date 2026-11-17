"""checks13 / lemmaM13.py -- STRATEGY-13b candidate 1, prediction 1 [estimate]: depth needed for L = 1.6 if E13's
eps(R, L) is replaced by a summed Lemma-M bound.

Lemma M (ANSWER-11, transport12.out): one cone point at distance delta from a segment, lever arm lam, moves the
comparison map by about A * exp(lam - 2 delta) (A ~ 1.05 for displacement, ~ 2.96 for rotation).
All anchors outside the disc B(c, R) contribute.  Their number within distance r is at most N0(r) ~ 3.5 e^r
(packing, merge10.N0), so the summed bound is  sum_j A exp(lam - 2 delta_j)  with delta_j >= r_j - shift:
      S(R) = A e^{lam + 2 shift} * int_R^inf e^{-2r} dN0(r)   ~  A e^{lam+2 shift} * 3.5 e^{-R}.
Exponent: e^{-R}, the same as E13 (per-lift rate 2 minus counting rate 1).  Only the constant can change.
Criterion as in E13 (thmb_L1.6.out): S(R) < 2 w_min = 0.5.  Three geometries for (lam, shift):
  optimistic  lam = L/2, shift = 0     (cone point seen from the centre of the star)
  middle      lam = L,   shift = L/2
  conservative lam = L,  shift = L     (delta >= r - L)
First-order superposition of the contributions is assumed (not proved).
"""
import math
S2 = math.sqrt(2); lmin = math.acosh(1 + S2)
def N0(R): return (math.cosh(R + lmin / 2) - 1) / (math.cosh(lmin / 2) - 1)
def eps13(R, L):
    t, u = math.tanh(R / 2), math.tanh(L / 2)
    s = u / t; eta = 1 - t * t
    E = s * eta * (1 + s) / (1 - s) + u * (1 - t) / t
    return 2 * E / (1 - (u + E) ** 2) if u + E < 1 else float("inf")
def S(R, A, lam, shift):
    a = lmin / 2; K = math.cosh(a) - 1        # dN0 = sinh(r + a)/K dr, integrated in closed form
    tot = (math.exp(a) * math.exp(-R) - math.exp(-a) * math.exp(-3 * R) / 3) / (2 * K)
    return A * math.exp(lam + 2 * shift) * tot
L = 1.6; target = 0.5
print("E13: eps13(4.98, 1.6) = %.3f (criterion 0.5), N0(4.98) = %.0f" % (eps13(4.98, L), N0(4.98)))
print("geometry       A      R_needed   N0(R)   (E13: 4.98 / 505)")
for name, lam, sh in (("optimistic", L / 2, 0), ("middle", L, L / 2), ("conservative", L, L)):
    for A in (1.05, 2.96):
        R = 0.5
        while S(R, A, lam, sh) >= target: R += 0.01
        print("%-13s  %.2f   %5.2f    %7.0f" % (name, A, R, N0(R)))
print("decay check: S(R+1)/S(R) = %.4f (e^-1 = %.4f)" % (S(6, 1, 0, 0) / S(5, 1, 0, 0), math.exp(-1)))
