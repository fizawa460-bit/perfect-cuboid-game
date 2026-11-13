import itertools, numpy as np, collections, cmath, sys
exec(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'t01_base_1x3.py')).read().split("stat=collections.Counter()")[0])
def cr(a,b,c,d): return (a-c)*(b-d)/((a-d)*(b-c))
def jinv(l): return 256*(l*l-l+1)**3/(l*l*(l-1)**2)
def nrm(M):
    M=M/np.sqrt(np.linalg.det(M)); k=np.argmax(abs(M)); M=M/ (M.flat[k]/abs(M.flat[k]));
    return M
def key(M): 
    M=nrm(M); return tuple(np.round(np.concatenate([M.real.flatten(),M.imag.flatten()]),5))
# octahedral group on target (Bg coordinates): Moebius maps permuting Bg
Oct=[]
for img in itertools.permutations(range(6),3):
    g=mobfrom([Bg[0],Bg[1],Bg[2]],[Bg[i] for i in img])
    perm=[]
    for bv in Bg:
        w=ap(g,bv); d=[abs(w-x) for x in Bg]; k=int(np.argmin(d))
        if d[k]<1e-8: perm.append(k)
    if len(perm)==6 and len(set(perm))==6: Oct.append((g,tuple(perm)))
assert len(Oct)==24
maps=[]
for Sidx in itertools.combinations(range(6),4):
    for (num,den) in cubics([Bg[x] for x in Sidx]):
        maps.append((num,den,oddset(num,den,Sidx),Sidx))
def ev(m,t): return np.polyval(m[0],t)/np.polyval(m[1],t)
gen=[0.123+0.456j,-0.77+0.21j,1.3-0.9j]
def extaut(m):
    O=m[2]; res={}
    base=[0,1,2]
    for g,perm in Oct:
        cands=[[k for k in range(10) if O[k][1]==perm[O[b][1]]] for b in base]
        for im in itertools.product(*cands):
            if len(set(im))<3: continue
            s=mobfrom([O[b][0] for b in base],[O[k][0] for k in im])
            if all(abs(ev(m,ap(s,t))-ap(g,ev(m,t)))<1e-7*(1+abs(ev(m,t))) for t in gen): res[key(s)]=(s,perm)
    return list(res.values())
G=[extaut(m) for m in maps]
print("extended automorphism group orders of the 60 cubics:",dict(collections.Counter(len(x) for x in G)))
def order(s):
    M=np.eye(2,dtype=complex)
    for k in range(1,25):
        M=M@s
        if key(M)==key(np.eye(2,dtype=complex)): return k
J=[]
for m in maps:
    O=m[2]; J.append([(jinv(cr(*[O[i][0] for i in q])),q) for q in itertools.combinations(range(10),4)])
stat=collections.Counter()
P4=list(itertools.permutations(range(4)))
for i1,m1 in enumerate(maps):
    for i2,m2 in enumerate(maps):
        O1=m1[2];O2=m2[2]; seen={}
        for (j1,q1) in J[i1]:
            for (j2,q2) in J[i2]:
                if abs(j1-j2)>1e-6*(1+abs(j1)): continue
                for pm in P4:
                    T=mobfrom([O1[q1[k]][0] for k in range(3)],[O2[q2[pm[k]]][0] for k in range(3)])
                    if abs(ap(T,O1[q1[3]][0])-O2[q2[pm[3]]][0])>1e-7: continue
                    kk=key(T)
                    if kk in seen: continue
                    co=[]
                    for a_,(z,ja) in enumerate(O1):
                        w=ap(T,z)
                        for b_,(z2,jb) in enumerate(O2):
                            if abs(w-z2)<1e-7*(1+abs(z2)): co.append((ja,jb))
                    seen[kk]=1
                    jj=sum(lab[x]==lab[y] for x,y in co); hh=len(co)-jj
                    # birational?  q(T t) = M(p1(t)) : test constancy on a p1-fibre
                    c0=ev(m1,gen[0]); r=np.roots(np.polysub(m1[0],c0*m1[1])); vals=[ev(m2,ap(T,t)) for t in r]
                    bir = max(abs(vals[0]-v) for v in vals)>1e-6
                    # transfer: some nontrivial s1 in G1 with T s1 T^-1 in G2
                    K2={key(s):order(s) for s,_ in G[i2]}
                    tr=sorted(set(K2[key(T@s@np.linalg.inv(T))] for s,_ in G[i1] if key(T@s@np.linalg.inv(T)) in K2)-{1})
                    stat[(len(co),jj,hh,bir,tuple(tr),(len(G[i1]),len(G[i2])))]+=1
print("c, j, h, birational, orders of transferred symmetries, (|G1|,|G2|): count")
for k,v in sorted(stat.items()): print(k,v)
