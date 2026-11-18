# independent mpmath check of the revised chain (C_X = 2): kappa = C0 + 1 + 8l/3, seedless 73, area shift l/2
from mpmath import mp, mpf, acosh, sqrt, tanh, log, exp, sinh, cosh, pi, atanh
mp.dps = 40
l = acosh(1+sqrt(2)); c = 1/(1+2*pi/(2*l)); AV = pi*(cosh(l/2)-1)
eps = lambda R: 2*atanh(exp(-R))
r = tanh(mpf(1)/2); lam = 2/(1-r*r); e = eps(mpf('10.78')); f = lam**2*(exp(2*e)-1)
K = (((2/r)*(e+r*r/4*f)+r*f)/2+e)/e
CX = 2; C0 = log(3*CX*K/l); kap = C0 + 1 + 8*l/3; R0 = mpf('10.78') + l
E = lambda e, Ld: 3*CX*K*e*sinh(Ld)
s0 = (R0-kap)/3; assert s0 >= 1 and E(eps(R0-s0-1), s0+1) < mpf('0.2')
Nv = lambda R: (cosh(R+l/2)-1)/(cosh(l/2)-1)
def M(la):
    F = lambda t: log(4*Nv(t) + 2*pi/AV*exp(la - c*((t-kap)/3 - 1 - l/2)))
    lo, hi = R0, R0 + 3*la + 200; g = (sqrt(5)-1)/2
    for _ in range(150):
        a1 = hi-g*(hi-lo); a2 = lo+g*(hi-lo)
        if F(a1) < F(a2): hi = a2
        else: lo = a1
    return F(lo)
lo, hi = mpf(1), mpf(1000)
for _ in range(100):
    m = (lo+hi)/2
    if log(11 + mpf('216.3')*73*(4*Nv(R0) + exp(M(m)))) >= m: lo = m
    else: hi = m
print("C0 =", mp.nstr(C0, 6), "kappa =", mp.nstr(kap, 6), "log10 a_max =", mp.nstr(lo/log(10), 6))
