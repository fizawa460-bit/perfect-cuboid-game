# E14: constants of Theorem A' (linear bound), Proposition L and Theorem B'. Floating point; elementary functions only.
import math
ach = math.acosh
r2 = math.sqrt(2)
lmin = ach(1 + r2)                                   # side of the (pi/4)^3 triangle: 2cosh l = 2+2sqrt2
h = math.asinh(math.sinh(lmin) * math.sin(math.pi / 4))   # altitude
print("l_min = %.6f   altitude h = %.6f   2h = %.6f   cosh 2h = %.6f (3+2sqrt2 = %.6f)"
      % (lmin, h, 2 * h, math.cosh(2 * h), 3 + 2 * r2))
# area of the equilateral triangle with angles pi/4 and of the rhombus
print("triangle area pi/4, rhombus area pi/2; cosh side from angles: %.6f (1+sqrt2 = %.6f)"
      % ((math.cos(math.pi / 4) + math.cos(math.pi / 4) ** 2) / math.sin(math.pi / 4) ** 2, 1 + r2))
def R(l): return ach(math.cosh(l) + math.sinh(l) ** 2)
def N(Rr): return (math.cosh(Rr + lmin / 2) - 1) / (math.cosh(lmin / 2) - 1)
# Theorem A':  2a+4+2s1 <= theta*2b + N*(2s1+m),  b = a+s1+m/2,  theta = 1/(cosh(l*/2)-1)
best = None
for i in range(2640, 4000):
    ls = i / 1000
    th = 1 / (math.cosh(ls / 2) - 1)
    if th >= 1: continue
    c1 = N(R(ls)) / (1 - th)
    if best is None or c1 < best[0]: best = (c1, ls, th)
c1, ls, th = best
Nn = N(R(ls))
print("l* = %.3f  R(l*) = %.4f  N = %.2f  theta = %.4f" % (ls, R(ls), Nn, th))
print("Theorem A':  a + s1 <= (N(2 s1 + m) + theta m - 4) / (2(1-theta))")
for m in (0, 2, 4):
    print("   m = %d:  a + s1 <= %.1f * s1 + %.1f" % (m, Nn / (1 - th), (Nn * m + th * m - 4) / (2 * (1 - th))))
print("   area form:  b - a >= (b(1-theta) + 2)/(N+1),  (1-theta)/(N+1) = %.3e" % ((1 - th) / (Nn + 1)))
# Proposition L / Theorem B': non-deep counts
for Rr in (5.0, R(ls), 10.78):
    print("R = %.3f: non-deep cone points per unit of defect cost <= 2 N0(R) = %.0f; non-deep area <= 2 pi (2 cosh R - 1) = %.0f; tanh(R/2) = 1 - %.2e"
          % (Rr, 2 * N(Rr), 2 * math.pi * (2 * math.cosh(Rr) - 1), 1 - math.tanh(Rr / 2)))
