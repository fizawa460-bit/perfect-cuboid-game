import numpy as np, itertools
# B in homogeneous coords (y0,y1) meaning y0/y1 ; labels: e={0,inf}, b={+-1}, a={+-i}
BP=[(0,1),(1,0),(1,1),(-1,1),(1j,1),(-1j,1)]
BNAME=['0','inf','1','-1','i','-i']
BLAB=[0,0,1,1,2,2]   # 0=e,1=b,2=a
def mob_apply(M,z):  # z homogeneous (z0,z1)
    return (M[0][0]*z[0]+M[0][1]*z[1], M[1][0]*z[0]+M[1][1]*z[1])
def hom_eq(u,v,tol=1e-9):
    return abs(u[0]*v[1]-u[1]*v[0]) <= tol*max(1e-300,(abs(u[0])+abs(u[1]))*(abs(v[0])+abs(v[1])))
def autB():
    out=[]
    for tr in itertools.permutations(range(6),3):
        # Mobius sending 0->B[tr0], inf->B[tr1], 1->B[tr2]
        a=np.array(BP[tr[0]],complex); b=np.array(BP[tr[1]],complex); c=np.array(BP[tr[2]],complex)
        # M = [b*lam, a*mu] columns: M(inf)=b, M(0)=a, M(1)=lam b + mu a = c
        A=np.array([[b[0],a[0]],[b[1],a[1]]]); lm=np.linalg.solve(A,c)
        M=np.array([[b[0]*lm[0],a[0]*lm[1]],[b[1]*lm[0],a[1]*lm[1]]])
        perm=[]
        for z in BP:
            w=mob_apply(M,z); k=[i for i in range(6) if hom_eq(w,BP[i])]
            if len(k)!=1: break
            perm.append(k[0])
        else: out.append((M,tuple(perm)))
    return out
AUT=autB()
assert len(AUT)==24
