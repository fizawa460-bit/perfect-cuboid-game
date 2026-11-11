import math
ach=math.acosh
lmin=ach(1+math.sqrt(2))          # min distance between two order-2 points of Gamma_0: 2cosh l = 2+2sqrt2
def R(l): return ach(math.cosh(l)+math.sinh(l)**2)      # gap 2: 2 sinh^2 l/(cosh R - cosh l) >= 2
def N(Rr): return (math.cosh(Rr+lmin/2)-1)/(math.cosh(lmin/2)-1)   # packing bound
print("l_min",round(lmin,4),"R(l_min)",round(R(lmin),4))
best=None
for i in range(2640,4000,5):
    ls=i/1000; f=1-1/(math.cosh(ls/2)-1)
    if f<=0: continue
    for M in (2,4):
        a=(M*N(R(ls))-4)/(2*f)
        if best is None or (M==4 and a<best[0]):
            if M==4: best=(a,ls)

a4,ls=best; f=1-1/(math.cosh(ls/2)-1)
print("optimal l*",ls,"R(l*)",round(R(ls),3),"N",round(N(R(ls))),"bound a (M=4):",int(a4),"(M=2):",int((2*N(R(ls))-4)/(2*f)))
