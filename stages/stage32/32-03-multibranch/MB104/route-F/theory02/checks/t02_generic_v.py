import numpy as np, itertools, cmath
from collections import Counter
z8=cmath.exp(1j*cmath.pi/4)
def k1(x): return 1j/x
def k2(x): return (-x-1j)/(x+1)
def k3(x): return k1(k2(x))
def run(v,b2=z8**3,withU=True):
    b1=1j
    def upre(x):
        s=cmath.sqrt((x-b1)/(x-b2)); return [s,-s]
    Ux=[-b1,-b2]
    src=[s for x in (cmath.sqrt(v),-cmath.sqrt(v),cmath.sqrt(k1(v)),-cmath.sqrt(k1(v))) for s in upre(x)]
    tgt=[s for x in (cmath.sqrt(k2(v)),-cmath.sqrt(k2(v)),cmath.sqrt(k3(v)),-cmath.sqrt(k3(v))) for s in upre(x)]
    U=[s for x in Ux for s in upre(x)]
    O1=np.array(src+(U if withU else [])); O2=np.array(tgt+(U if withU else []))
    n1,n2=len(O1),len(O2)
    def m(z):
        z1,z2,z3=z; return np.array([[z2-z3,-z1*(z2-z3)],[z2-z1,-z3*(z2-z1)]])
    uniq={}
    for tri in itertools.combinations(range(n1),3):
        mz=m(O1[list(tri)])
        for img in itertools.permutations(range(n2),3):
            M=np.linalg.inv(m(O2[list(img)]))@mz
            w=(M[0,0]*O1+M[0,1])/(M[1,0]*O1+M[1,1])
            d=np.abs(w[:,None]-O2[None,:])/np.sqrt((1+abs(w[:,None])**2)*(1+abs(O2[None,:])**2))
            hit=np.argwhere(d<1e-9)
            if len(hit)>=4: uniq[tuple(sorted(map(tuple,hit)))]=1
    return dict(Counter(len(k) for k in uniq))
print('v=1 (the real case):',run(1+0j))
print('v=0.37+0.81j:',run(0.37+0.81j))
print('v=2.3-0.4j:',run(2.3-0.4j))
print('v=0.37+0.81j, far map:',run(0.37+0.81j,b2=z8**7))
print('v=0.37+0.81j, no U:',run(0.37+0.81j,withU=False))
