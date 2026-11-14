from mpmath import mp, mpf, mpc, quad, sqrt, matrix, lu_solve, identify, nstr
mp.dps=30
# E': y^2 = x(x+1)(x+i).  Doubling on x: D(x) = (x^2 - e2 e3)^2 / (4 x (x-e2)(x-e3)), e2=-1,e3=-i
e2,e3=mpc(-1),mpc(0,-1)
def D(x): return (x*x-e2*e3)**2/(4*x*(x-e2)*(x-e3))
for x0,name in ((mpc(1),'x=1'),(mpc(0,1),'x=i')):
    x=x0; seq=[x]
    for k in range(12):
        x=D(x); seq.append(x)
    print(name,[nstr(v,8) for v in seq[:7]])
    # torsion test: is some 2^k P = +-2^j P ?
    rep=[(j,k) for j in range(len(seq)) for k in range(j+1,len(seq)) if abs(seq[j]-seq[k])<mpf(10)**-15]
    print('  repeats among 2^k multiples:',rep[:5])
# multiplication by 3 test via division polynomial is longer; use height growth instead: log|num| growth
