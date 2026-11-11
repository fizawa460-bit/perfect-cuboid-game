# E15 Theorem E: constants (floating point, elementary functions).
#   eta(d)  := log( arccosh(cosh d + 1) / d )      -- if sup w < eta(d1) on the g1-geodesic, then 2cosh d2 < 2cosh d1 + 2
#   R_E(l)  := the radius with -log tanh(R/2) = eta(l), i.e. tanh(R/2) = exp(-eta(l))
# Checks: eta is decreasing on (0, 12]; the table for the lengths used in E13/E14.
import math
eta = lambda d: math.log(math.acosh(math.cosh(d) + 1) / d)
RE = lambda l: 2 * math.atanh(math.exp(-eta(l)))
xs = [0.01 * k for k in range(1, 1201)]
dec = all(eta(xs[i]) > eta(xs[i + 1]) for i in range(len(xs) - 1))
print("eta decreasing on (0, 12] (grid 0.01):", dec)
lmin = math.acosh(1 + math.sqrt(2))
print("   l        eta(l)     R_E(l)    (E13 Theorem B radius for L = 3.2: 10.78)")
for l in [lmin, 1.6, 2.0, 2.5, 3.048, 3.2, 6.4]:
    print("%8.4f  %9.5f  %8.4f" % (l, eta(l), RE(l)))
# the step used in the proof: for d1 <= l and sup w < eta(l) <= eta(d1):  cosh(e^w d1) < cosh d1 + 1
worst = max(math.cosh(math.exp(0.999999 * eta(d)) * d) - math.cosh(d) - 1 for d in xs)
print("max of cosh(e^{0.999999 eta} d) - cosh d - 1 on the grid: %.3e (must be < 0)" % worst)
print("PASS" if dec and worst < 0 else "FAIL")
