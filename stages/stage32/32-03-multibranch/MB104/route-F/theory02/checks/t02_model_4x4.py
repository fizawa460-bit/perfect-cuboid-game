import numpy as np, itertools, cmath, sys
from collections import Counter
z8=cmath.exp(1j*cmath.pi/4)
def k2(x): return (-x-1j)/(x+1)          # swaps -i<->0, -1<->inf
def k3(x): return -1j*(x+1)/(x+1j)        # swaps -i<->inf, -1<->0
def k1(x): return 1j/x
def run(b2,k,name):
    b1=1j
    def upre(x):
        s=cmath.sqrt((x-b1)/(x-b2)); return [s,-s]
    mu8=[z8**j for j in range(8)]
    A=[x for x in mu8 if abs(x-b1)>1e-9 and abs(x-b2)>1e-9]
    Ap=[x for x in (1j,-1j,z8**3,-z8**3) if abs(x-b1)>1e-9 and abs(x-b2)>1e-9]
    for c in (k(1),k(1j)):
        s=cmath.sqrt(c); Ap+=[s,-s]
    O1=np.array([t for x in A for t in upre(x)]); O2=np.array([t for x in Ap for t in upre(x)])
    typ1=[]
    for x in A:
        v=x*x; typ1+=[('F1' if abs(v-1)<1e-9 else 'Fi' if abs(v-1j)<1e-9 else 'Ub' if abs(v+1)<1e-9 else 'Ua')]*2
    typ2=['Ub' if abs(x*x+1)<1e-9 else 'Ua' for x in Ap[:2] for _ in (0,1)]+['C1']*4+['C2']*4
    def m(z):
        z1,z2,z3=z; return np.array([[z2-z3,-z1*(z2-z3)],[z2-z1,-z3*(z2-z1)]])
    uniq={}
    for tri in itertools.combinations(range(12),3):
        mz=m(O1[list(tri)])
        for img in itertools.permutations(range(12),3):
            M=np.linalg.inv(m(O2[list(img)]))@mz
            w=(M[0,0]*O1+M[0,1])/(M[1,0]*O1+M[1,1])
            d=np.abs(w[:,None]-O2[None,:])/np.sqrt((1+abs(w[:,None])**2)*(1+abs(O2[None,:])**2))
            hit=np.argwhere(d<1e-9)
            if len(hit)>=4: uniq[tuple(sorted(map(tuple,hit)))]=M
    cc=Counter(len(k_) for k_ in uniq)
    pat=Counter()
    for key in uniq:
        if len(key)>=5: pat[tuple(sorted((typ1[i],typ2[j]) for i,j in key))]+=1
    # circles: is O1 concyclic? cross ratios real
    def conc(P):
        P=list(P); 
        if len(P)<4: return True
        cr=[((P[0]-P[2])*(P[1]-z))/((P[0]-z)*(P[1]-P[2])) for z in P[3:]]
        return max(abs(c.imag)/(1+abs(c)) for c in cr)<1e-8
    print(name,'c-histogram',dict(cc),'O1 concyclic',conc(O1),'C concyclic',conc(O2[4:]),'O2 concyclic',conc(O2))
    for p,v in sorted(pat.items(),key=lambda kv:-kv[1]): print('   ',v,p)
run(z8**3,k2,'adjacent/k2'); run(z8**3,k3,'adjacent/k3'); run(z8**7,k2,'far/k2'); run(z8**7,k3,'far/k3'); run(z8**3,k1,'adjacent/k1(control, symmetry)')
