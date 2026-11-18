# Independent recomputation of E19 s.21 constants and the bound (mpmath, written from the formulas, not chain20.py)
import mpmath as mp
mp.mp.dps = 30
l = mp.acosh(1+mp.sqrt(2)); l0 = 2*l
c = 1/(1+2*mp.pi/l0)
eps = lambda R: 2*mp.atanh(mp.e**(-R))
tau_s = mp.mpf(5); es = eps(tau_s)
r = mp.tanh(mp.mpf(1)/2); lam = 2/(1-r*r)
def Kof(e):
    f = lam**2*(mp.e**(2*e)-1)
    grad = ((2/r)*e + r*f)/2        # harmonic part uses sup|h| <= e (max principle); Green part r*sup f (2r/3 is sharp)
    return grad/e + 1
def Kof_doc(e):
    f = lam**2*(mp.e**(2*e)-1)
    grad = ((2/r)*(e + r*r/4*f) + r*f)/2
    return grad/e + 1
K = Kof_doc(es); K1 = K-1+mp.e**es
beta = 1/(1-mp.e**(-2*tau_s)); gam = 2/(1-mp.e**(-2*l)); h = 2*mp.sinh(l/2)/l
print("l_min=%s l0=%s c=%s" % (mp.nstr(l,8), mp.nstr(l0,8), mp.nstr(c,6)))
print("eps(5)=%s K=%s K1=%s beta=%s gamma=%s h=%s" % tuple(mp.nstr(x,7) for x in (es,K,K1,beta,gam,h)))
print("  (K with max-principle harmonic part and 2r/3 Green: %s -> sharper K1 %s)" % (mp.nstr(Kof(es)*0+ (( (2/r)*es + (2*r/3)*lam**2*(mp.e**(2*es)-1))/2)/es+1,6), ""))
A0 = 1+mp.log(beta*K1/l); B0 = mp.e**(8*l/3); C0 = h*gam*mp.e**(4*l/3)
kap = lambda t: A0 + mp.log(B0 + C0*(t+4*l/3))
print("kappa(t) = %s + log(%s + %s (t + %s))" % tuple(mp.nstr(x,6) for x in (A0,B0,C0,4*l/3)))
R0 = mp.mpf('10.78') + l
rb = lambda t: (t-kap(t))/3
print("R0=%s kappa(R0)=%s r(R0)=%s kappa(140)=%s kappa(142)=%s" % tuple(mp.nstr(x,6) for x in (R0,kap(R0),rb(R0),kap(140),kap(142))))
# --- brute-force pinning check with UNSIMPLIFIED bounds (exact eps, exact cosh/sinh, exact 2 sinh(E/2))
def pin(t, s, s2, tc, Lm):
    Lp = s+s2+l
    Rp = t - max(s, s2+l) - 1
    if Rp < tau_s: return None
    direct = K1*eps(Rp)*mp.sinh(Lp)
    # E^- with pointwise eps along entry path, depth floor max(tc-u-1, tau*)
    f = lambda u: eps(max(tc-u-1, tau_s))*mp.cosh(Lm-u)
    Em = K1*mp.quad(f, [0, min(Lm, max(tc-1-tau_s,0)) if tc-1-tau_s>0 else Lm, Lm])
    rot = 2*mp.sinh(Em/2)/mp.sinh(Lm)*mp.sinh(Lp)
    return direct+rot, Em
worst = 0; worstpt=None
import itertools
for t in [R0, R0+0.5, R0+1, 14, 16, 20, 30, 50, 100, 142, 300]:
    t = mp.mpf(t); r_ = rb(t)
    for fs, fs2 in itertools.product([0, .5, .9, .999999], [0, .5, .9, .999999]):
        s = fs*r_; s2 = fs2*(r_+l/3)
        for ftc in [0, .3, 1, 2]:
            tc = t - s + ftc*s*2      # depth of c in [t-s, t+s]
            for fL in [0, .5, .9, .999999]:
                Lm = l + fL*(tc+4*l/3 - l)
                res = pin(t, s, s2, tc, Lm)
                if res is None: continue
                D, Em = res
                if D/l > worst: worst = D/l; worstpt=(float(t),float(s),float(s2),float(tc),float(Lm),float(Em))
print("max D/l_min over grid (unsimplified, exact functions) = %s at %s" % (mp.nstr(worst,6), worstpt))
# --- eps0 test (good vertex), worst s = r(t)
def e0(t):
    s = rb(t); tau = t - max(s,1) - 1
    d = K1*eps(tau)*mp.sinh(s+1)
    rot = h*gam*2*beta*K1*mp.e*(t-s+4*l/3)*mp.e**(-(t-s))*mp.sinh(s+1)
    return d+rot
mx = max(e0(R0+mp.mpf(k)/100) for k in range(0, 3000))
mx2 = max(e0(mp.mpf(t)) for t in range(40, 5000, 7))
print("eps0 test: max over [R0, R0+30] = %s, over [40,5000] = %s  (needs < 0.2); at R0: %s" % (mp.nstr(mx,5), mp.nstr(mx2,5), mp.nstr(e0(R0),5)))
# smallest R0 with the test
lo=mp.mpf(8); 
for k in range(0,600):
    tt = mp.mpf(8)+mp.mpf(k)/100
    if rb(tt) >= 1 and all(e0(tt+mp.mpf(j)/20) < 0.2 for j in range(0,200)): print("smallest t with eps0 test (and r>=1) ~", mp.nstr(tt,5)); break
# path depth floor
print("exit-path depth floor at R0: (2t+kappa)/3 - 4l/3 - 1 =", mp.nstr((2*R0+kap(R0))/3-4*l/3-1,5), "; seed path R0-4.8969-1 =", mp.nstr(R0-4.8969-1,5))
# --- the bound
AV = mp.pi*(mp.cosh(l/2)-1)
def lNv(R): return mp.log((mp.cosh(R+l/2)-1)/(mp.cosh(l/2)-1))
def lU(la, coefc=c):
    # min over t0 of 4 N_v(t0) + 2 pi a e^{-c (r(t0) - 1 - l/2)} / A_V  ; dense grid then refine
    best = mp.inf
    t = R0
    while rb(t) < 1 + l/2: t += mp.mpf('0.001')
    tmin = t
    grid = [tmin + mp.mpf(k)/20 for k in range(0, int(20*(3*la+50)))]
    vals = [(mp.log(4*mp.e**lNv(tt) + 2*mp.pi/AV*mp.e**(la - coefc*(rb(tt)-1-l/2))), tt) for tt in grid]
    v, tt = min(vals)
    f = lambda x: mp.log(4*mp.e**lNv(x) + 2*mp.pi/AV*mp.e**(la - coefc*(rb(x)-1-l/2)))
    xm = mp.findroot(lambda x: mp.diff(f, x), tt) if tt > tmin else tt
    return min(v, f(xm)), xm
def bound(SL):
    near = 4*mp.e**lNv(R0)
    g = lambda la: mp.log(11 + mp.mpf('216.3')*SL*(near + mp.e**lU(la)[0])) - la
    lo, hi = mp.mpf(10), mp.mpf(400)
    for _ in range(60):
        m = (lo+hi)/2
        if g(m) >= 0: lo = m
        else: hi = m
    return lo
for SL in (121, 73, 169):
    la = bound(SL)
    v, t0 = lU(la)
    print("seedless %d: log10 a_max = %s   (optimal t0 = %s, untransportable/near = 10^%s)" % (SL, mp.nstr(la/mp.log(10),5), mp.nstr(t0,5), mp.nstr((v - mp.log(4)-lNv(R0))/mp.log(10),4)))
print("log10 N_v(R0) =", mp.nstr(lNv(R0)/mp.log(10),4))
