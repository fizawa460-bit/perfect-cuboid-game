import itertools, cmath, numpy as np, collections
Bn=['0','inf','1','-1','i','-i']
mu=lambda t:(t*(0.7+0.2j)+0.3-0.1j)/(t*(0.2-0.5j)+1.1+0.4j)
Bg=[mu(0),(0.7+0.2j)/(0.2-0.5j),mu(1),mu(-1),mu(1j),mu(-1j)]
lab=[2,2,1,1,0,0]
def mob3(s1,s2,s3):
    c=(s3-s2)/(s3-s1); return np.array([[c,-c*s1],[1,-s2]])
def ap(M,t): return (M[0,0]*t+M[0,1])/(M[1,0]*t+M[1,1])
def mobfrom(z,w):  # T with T(z_i)=w_i
    A=mob3(*z); Bm=mob3(*w); return np.linalg.inv(Bm)@A
sig=np.array([[0.9+0.3j,0.2-0.6j],[0.4+0.1j,1.0-0.2j]])
def comp(num,den,S):
    n=max(len(num),len(den))-1
    a=np.array([S[0,0],S[0,1]]);c=np.array([S[1,0],S[1,1]])
    def sub(p):
        p=np.concatenate([np.zeros(n+1-len(p)),p]);out=np.zeros(1,dtype=complex)
        for j,co in enumerate(p):
            t=np.array([co],dtype=complex)
            for _ in range(n-j): t=np.polymul(t,a)
            for _ in range(j): t=np.polymul(t,c)
            out=np.polyadd(out,t)
        return out
    return sub(num),sub(den)
def cubics(S):
    N=mob3(S[0],S[1],S[2]);z=ap(N,S[3]);Ni=np.linalg.inv(N)
    H=np.polysub(np.polymul([1,0],np.polymul([3,-2],np.polymul([3,-2],[3,-2]))),z*np.array([2,-1]))
    out=[]
    for k in np.roots(H):
        num=np.array([2*k-1,2-3*k,0,0]);den=np.array([1,-k]);num,den=comp(num,den,sig)
        d=np.concatenate([np.zeros(len(num)-len(den)),den])
        out.append((Ni[0,0]*num+Ni[0,1]*d,Ni[1,0]*num+Ni[1,1]*d))
    return out
def oddset(num,den,Sidx):
    O=[]
    for j,v in enumerate(Bg):
        r=list(np.roots(np.polysub(num,v*den)))
        if j in Sidx:
            d=sorted((abs(r[x]-r[y]),x,y) for x in range(3) for y in range(x+1,3))
            O.append((r[3-d[0][1]-d[0][2]],j))
        else: O+=[(x,j) for x in r]
    return O
stat=collections.Counter(); ex=[]
for Sidx in itertools.combinations(range(6),4):
    for (num,den) in cubics([Bg[x] for x in Sidx]):
        O=oddset(num,den,Sidx); seen=set()
        for tri in itertools.combinations(range(10),3):
            for img in itertools.permutations(range(6),3):
                T=mobfrom([O[t][0] for t in tri],[Bg[i] for i in img])
                co=[]
                for k,(z,j) in enumerate(O):
                    w=ap(T,z)
                    for bi,bv in enumerate(Bg):
                        if abs(w-bv)<1e-7*(1+abs(bv)): co.append((k,j,bi))
                if len(co)>=4:
                    key=tuple(sorted(co))
                    if key in seen: continue
                    seen.add(key)
                    jj=sum(lab[j]==lab[bi] for k,j,bi in co); hh=len(co)-jj
                    fib=tuple(sorted(collections.Counter(j for k,j,bi in co).values()))
                    crit=sum(1 for k,j,bi in co if j in Sidx)
                    stat[(jj,hh,fib,crit)]+=1
                    if jj==4 and len(ex)<3: ex.append((Sidx,[(Bn[j],Bn[bi]) for k,j,bi in co]))
for k,v in sorted(stat.items()): print("(j,h)=",k[:2],"fibre pattern",k[2],"#pts over critical values",k[3],"count",v)
for e in ex: print(e)
