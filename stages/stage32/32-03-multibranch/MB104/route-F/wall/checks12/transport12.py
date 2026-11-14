"""checks12 / transport12.py -- request 11: transport of the comparison map across a region, in the exact model.

Model: the unit disc with one cone point of order 2 at 0; F(z) = sqrt z is the map dev_2 o dev_1^{-1}.
For z1, z2 symmetric about the positive axis let g_i be the osculating isometry of F at z_i (same value, same
direction of the derivative), gamma = g_1^{-1} g_2, and m the midpoint of the geodesic z1 z2 (distance delta from 0,
half-length s = w/2).   Printed: the displacement d(gamma m, m) and the rotation angle of gamma at m, against
exp(-2 delta), for several (delta, w).  Outline claim of ANSWER-11 section 3: both are O(exp(-2 delta)), uniformly in w
(a cone point at distance delta from the segment, with foot point at the base point).
With the base point at one end instead (lever arm w/2), the displacement is O(exp(w/2 - 2 delta)).
usage:  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks12/transport12.py
"""
import mpmath as mp
mp.mp.dps = 50
ok = True
T = lambda c: (lambda z: (z + c) / (1 + mp.conj(c) * z))
Ti = lambda c: (lambda z: (z - c) / (1 - mp.conj(c) * z))
hd = lambda a, b: 2 * mp.atanh(abs((a - b) / (1 - mp.conj(a) * b)))


def osc(z):
    Fz = mp.sqrt(z); al = mp.arg(1 / (2 * Fz))
    e = mp.expj(al)
    return (lambda x: T(Fz)(e * Ti(z)(x))), (lambda y: T(z)(mp.conj(e) * Ti(Fz)(y)))


print(" delta    w     d(gamma m, m)   *exp(2 delta)   rotation at m   *exp(2 delta)   d(gamma z1, z1)  *exp(2 delta - w/2)")
for delta in (1, 2, 3, 4):
    for w in (1, 2, 4, 8, 12):
        s = mp.mpf(w) / 2; D = mp.acosh(mp.cosh(delta) * mp.cosh(s))
        th2 = mp.acos(mp.tanh(delta) / mp.tanh(D))               # half of the angle at 0
        r = mp.tanh(D / 2); z1, z2 = r * mp.expj(-th2), r * mp.expj(th2); m = mp.tanh(mp.mpf(delta) / 2)
        g1, g1i = osc(z1); g2, g2i = osc(z2)
        gam = lambda x: g1i(g2(x))
        dm = hd(gam(m), m)
        hh = mp.mpf(10) ** -20
        rot = abs(mp.arg((gam(m + hh) - gam(m)) / hh * (1 - abs(m) ** 2) / (1 - abs(gam(m)) ** 2)))
        d1 = hd(gam(z1), z1)
        a, b, c = dm * mp.exp(2 * delta), rot * mp.exp(2 * delta), d1 * mp.exp(2 * delta - s)
        ok &= a < 3 and b < 3 and c < 3
        print("  %d     %2d     %.3e       %.3f          %.3e      %.3f           %.3e        %.3f"
              % (delta, w, float(dm), float(a), float(rot), float(b), float(d1), float(c)))
print("PASS" if ok else "FAIL")
