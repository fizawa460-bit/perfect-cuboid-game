l = mp.acosh(1+mp.sqrt(2)); eps = lambda R: 2*mp.atanh(mp.e**(-R)); tau_s=mp.mpf(5); es=eps(tau_s)
r=mp.tanh(mp.mpf(1)/2); lam=2/(1-r*r); f=lam**2*(mp.e**(2*es)-1)
K=(((2/r)*(es+r*r/4*f)+r*f)/2)/es+1; K1=K-1+mp.e**es
beta=1/(1-mp.e**(-2*tau_s)); gam=2/(1-mp.e**(-2*l)); h=2*mp.sinh(l/2)/l
kap=lambda t: 1+mp.log(beta*K1/l)+mp.log(mp.e**(8*l/3)+h*gam*(t+4*l/3)*mp.e**(4*l/3))
R0=mp.mpf('10.78')+l; rb=lambda t:(t-kap(t))/3
