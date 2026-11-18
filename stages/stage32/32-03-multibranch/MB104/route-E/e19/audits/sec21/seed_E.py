import mpmath as mp
mp.mp.dps=20
exec(open('consts.py').read())
print("l_min =", mp.nstr(l,5))
for tc,Lm,floor in [(R0,4.8969,R0-4.8969-1),(R0-l,4.8969,5),(R0-l,3.0571,5),(R0,3.0571,5)]:
    tc=mp.mpf(tc); Lm=mp.mpf(Lm)
    uni=K1*eps(floor)*mp.sinh(Lm)
    pw=K1*mp.quad(lambda u: eps(max(tc-u-1,5))*mp.cosh(Lm-u),[0,Lm])
    print("t_c=%5.2f L=%4.2f: uniform bound (depth floor %.2f) = %s ; pointwise = %s" % (tc,Lm,floor,mp.nstr(uni,4),mp.nstr(pw,4)))
