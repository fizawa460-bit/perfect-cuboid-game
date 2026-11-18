# Independent recomputation of the E19 stage-0 chain (mpmath, 50 digits). Written from E19 text, not reusing chain20.py code.
from mpmath import mp, mpf, acosh, sqrt, tanh, log, exp, sinh, cosh, pi, atanh, findroot, log10
mp.dps = 50
lmin = acosh(1+sqrt(2)); l0 = 2*lmin; c = 1/(1+2*pi/l0)
RSEED = mpf('10.78'); EPS0 = mpf('0.2'); AV = pi*(cosh(lmin/2)-1)
eps = lambda R: 2*atanh(exp(-R))          # = -log tanh(R/2), exact form
def K_of(e):
    r = tanh(mpf(1)/2); lam = 2/(1-r*r); f = lam**2*(exp(2*e)-1)
    return (((2/r)*(e+r*r/4*f)+r*f)/2+e)/e
def logNv(R): return log((cosh(R+lmin/2)-1)/(cosh(lmin/2)-1))
def chain(CX, C0override=None):
    K = K_of(eps(RSEED))
    E = lambda e, Ld: 3*CX*K*e*sinh(Ld)
    # C0 = sup_{R>=Rseed} least C with E(eps(R),R-C) < lmin. eps(R)sinh(R-C) increases in R -> limit e^{-C}
    C0 = log(3*CX*K/lmin)
    # check monotonicity numerically
    def need(R): return findroot(lambda C: E(eps(R), R-C)-lmin, mpf(3))
    assert all(need(RSEED+i) < need(RSEED+i+1) for i in range(0,40,5)) and need(mpf(60)) < C0
    if C0override is not None: C0 = C0override
    def ok(t):
        s = (t-C0-mpf('4.06'))/3
        return s >= 1 and E(eps(t-s-1), s+1) < EPS0
    R0 = RSEED+lmin
    while not ok(R0): R0 += mpf('0.01')
    return K, C0, R0
def logMbad_deep(la, C0, R0, k=4, coef=mpf(1)/3, cc=None):
    cc = c if cc is None else cc
    tmin = max(C0+mpf('4.06')+3, R0)
    f = lambda t: log(k*exp(logNv(t)) + 2*pi/AV*exp(la - cc*(coef*(t-C0-mpf('4.06'))-1)))
    # golden-section minimisation over t0
    lo, hi = tmin, tmin+la+200
    g = (sqrt(5)-1)/2
    for _ in range(300):
        m1 = hi-g*(hi-lo); m2 = lo+g*(hi-lo)
        if f(m1) < f(m2): hi = m2
        else: lo = m1
    return min(f(lo), f(tmin))
def amax(CX, seedless=65, C0override=None, coef=mpf(1)/3, cc=None, k=4):
    K, C0, R0 = chain(CX, C0override)
    near = k*exp(logNv(R0))
    def gap(la): return log(11 + mpf('216.3')*seedless*(near + exp(logMbad_deep(la, C0, R0, k, coef, cc)))) - la
    lo, hi = mpf(1), mpf(5000)
    for _ in range(200):
        m = (lo+hi)/2
        if gap(m) >= 0: lo = m
        else: hi = m
    return K, C0, R0, lo/log(10)
print("lmin=%s l0=%s c=%s AV=%s" % tuple(mp.nstr(x, 6) for x in (lmin, l0, c, AV)))
print("eps(Rseed)=%s K=%s log10 Nv(4)=%s Nv(4)=%s" % (mp.nstr(eps(RSEED),5), mp.nstr(K_of(eps(RSEED)),6), mp.nstr(logNv(4)/log(10),4), mp.nstr(exp(logNv(4)),5)))
print("\nA. corrected C0 (exact eps), seedless 65")
for CX in (1,2,5,10):
    K,C0,R0,la = amax(CX); print(" CX=%-4s C0=%s R0=%s log10Nv(R0)=%s log10 a_max=%s" % (CX, mp.nstr(C0,5), mp.nstr(R0,5), mp.nstr(logNv(R0)/log(10),4), mp.nstr(la,5)))
print("\nB. reproduce chain20 (C0 as printed by chain20), seedless 65")
for CX, C0b in ((1,'3.358656'),(2,'4.051803'),(5,'4.968094'),(10,'5.661241')):
    K,C0,R0,la = amax(CX, C0override=mpf(C0b)); print(" CX=%-4s C0=%s R0=%s log10 a_max=%s" % (CX, mp.nstr(C0,5), mp.nstr(R0,5), mp.nstr(la,5)))
print("\nC. corrected C0, seedless 73 (= 1 + 9*8: interior <= 8|dH| plus the boundary vertices themselves)")
for CX in (1,2,5,10):
    K,C0,R0,la = amax(CX, seedless=73); print(" CX=%-4s log10 a_max=%s" % (CX, mp.nstr(la,5)))
print("\nD. sensitivity at CX=2 (corrected C0, seedless 65)")
print(" coef 1/3 -> 1 :", mp.nstr(amax(2, coef=mpf(1))[3],5))
print(" c -> 1        :", mp.nstr(amax(2, cc=mpf(1))[3],5))
print(" exponent 3/(3+c) =", mp.nstr(3/(3+c),5), " 1/(1-exponent) =", mp.nstr((3+c)/c,5))
