# Brute-force check of the pinning inequality of s.21.3 with the unsimplified pieces:
#  direct = K1 eps(R+) sinh L+  (exact eps, exact sinh)
#  rot    = h * Ep / sinh L- * sinh L+, Ep = K1 * int_0^{L-} eps(max(tc-u-1, tau*)) cosh(L- - u) du  (pointwise)
#  (h * E is valid because E- <= l_min holds by the uniform bound of the entry step's own direct term)
#  ranges: s < r(t), s' < r(t)+l/3, tc in [t-s, t+s], L- in [l, tc + 4l/3)
import mpmath as mp, itertools
mp.mp.dps = 20
exec(open('consts.py').read())
worst=0; wp=None
for t in [R0, R0+0.3, R0+1, 13.5, 15, 18, 25, 40, 70, 142, 400]:
    t=mp.mpf(t); r_=rb(t)
    for fs, fs2 in itertools.product([0,.3,.7,.99999],[0,.3,.7,.99999]):
        s=fs*r_; s2=fs2*(r_+l/3)
        Lp=s+s2+l; Rp=t-max(s,s2+l)-1
        direct=K1*eps(Rp)*mp.sinh(Lp)
        for ftc in [0,.5,1]:
            tc=t-s+2*s*ftc
            for fL in [0,.3,.7,.99999]:
                Lm=l+fL*(tc+4*l/3-l)
                Ep=K1*mp.quad(lambda u: eps(max(tc-u-1,tau_s))*mp.cosh(Lm-u),[0,Lm])
                D=direct+h*Ep/mp.sinh(Lm)*mp.sinh(Lp)
                if D/l>worst: worst=D/l; wp=[float(x) for x in (t,s,s2,tc,Lm)]
print("max D/l_min =", mp.nstr(worst,6), "at (t,s,s',tc,L-) =", wp)
