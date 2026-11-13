import itertools, numpy as np, collections
src=open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'t01_3x3_all.py')).read().split("stat=collections.Counter()\nP4")[0]
exec(src)
def same(A,B_):   # projectively equal 2x2
    A=A/np.linalg.norm(A); B_=B_/np.linalg.norm(B_)
    return abs(abs(np.vdot(A.flatten(),B_.flatten()))-1)<1e-7
I2=np.eye(2,dtype=complex)
def order(s):
    M=I2.copy()
    for k in range(1,25):
        M=M@s
        if same(M,I2): return k
def fixpts(s):
    a,b,c,d=s.flatten(); r=np.roots([c,d-a,-b]); return list(r)
spec=[i for i in range(60) if len(G[i])==4]
print("special maps:",len(spec))
for i in spec[:12]:
    O=maps[i][2]; desc=[]
    for s,perm in G[i]:
        o=order(s)
        if o==1: continue
        f=fixpts(s); inO=sum(any(abs(x-z)<1e-7 for z,_ in O) for x in f)
        fixB=[k for k in range(6) if perm[k]==k]
        desc.append((o,inO,[Bn[k] for k in fixB]))
    print(i,"crit values",[Bn[k] for k in maps[i][3]],"elements (order, #fixed pts in O, B-points fixed by g):",desc)
# same dessin?
def samedessin(i1,i2):
    m1,m2=maps[i1],maps[i2]; O1,O2=m1[2],m2[2]
    for g,perm in Oct:
        cands=[[k for k in range(10) if O2[k][1]==perm[O1[b][1]]] for b in (0,1,2)]
        for im in itertools.product(*cands):
            if len(set(im))<3: continue
            s=mobfrom([O1[b][0] for b in (0,1,2)],[O2[k][0] for k in im])
            if all(abs(ev(m2,ap(s,t))-ap(g,ev(m1,t)))<1e-7*(1+abs(ev(m1,t))) for t in gen): return True
    return False
cls=[]
for i in range(60):
    for c in cls:
        if samedessin(c[0],i): c.append(i); break
    else: cls.append([i])
print("dessin classes (sizes):",[len(c) for c in cls], " special maps in classes:",[sum(i in spec for i in c) for c in cls])
cid={i:k for k,c in enumerate(cls) for i in c}
P4=list(itertools.permutations(range(4)))
stat=collections.Counter(); shown=0
for i1 in range(60):
  for i2 in range(60):
    if cid[i1]==cid[i2]: continue
    m1,m2=maps[i1],maps[i2]; O1=m1[2];O2=m2[2]; seen=[]
    for (j1,q1) in J[i1]:
        for (j2,q2) in J[i2]:
            if abs(j1-j2)>1e-6*(1+abs(j1)): continue
            for pm in P4:
                T=mobfrom([O1[q1[k]][0] for k in range(3)],[O2[q2[pm[k]]][0] for k in range(3)])
                if abs(ap(T,O1[q1[3]][0])-O2[q2[pm[3]]][0])>1e-7: continue
                if any(same(T,S) for S in seen): continue
                seen.append(T)
                co=[]
                for a_,(z,ja) in enumerate(O1):
                    w=ap(T,z)
                    for b_,(z2,jb) in enumerate(O2):
                        if abs(w-z2)<1e-7*(1+abs(z2)): co.append((a_,b_,ja,jb))
                jj=sum(lab[x]==lab[y] for _,_,x,y in co); hh=len(co)-jj
                Ti=np.linalg.inv(T)
                tr=tuple(sorted(order(s) for s,_ in G[i1] if order(s)>1 and any(same(T@s@Ti,s2) for s2,_ in G[i2])))
                fx=0
                for s,_ in G[i1]:
                    if order(s)>1:
                        for x in fixpts(s):
                            if any(a_ for a_ in [1] if any(abs(x-O1[c_[0]][0])<1e-7 for c_ in co)): fx+=1
                stat[(len(co),jj,hh,tr,(len(G[i1]),len(G[i2])),abs(jinv(cr(*[O1[q1[k]][0] for k in range(4)]))-1728)<1e-4)]+=1
print("DIFFERENT dessin classes only. c, j, h, transferred orders, (|G1|,|G2|), matched quadruple harmonic: count")
for k,v in sorted(stat.items()): print(k,v)
