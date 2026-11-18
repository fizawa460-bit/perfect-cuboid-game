# Independent check of the combinatorial part of s.21.4 on random sphere triangulations WITH multi-edges
# (built by random edge flips; loops forbidden).  For random vertex subsets H (complement = "bad"):
#   H° = vertices of H all of whose neighbours lie in H;  D = triangles with a vertex in H°;
#   fans = maximal runs of D-triangles around each vertex of H \ H°.
# Checks: (a) every fan has >= 2 triangles; (b) at most floor((deg-2+1)/3) fans per vertex (2 for deg 8, 1 for deg 4)
#         (c) sum_{H°}(6-d) + sum_fans(3-j) = 6 chi(D^)  with chi from V-E+F of the resolved complex
#         (d) sum_{H°}(d-6) <= sum_fans(6-j) - 12*(#components)   (boundary circles have >= 2 fan-vertices)
import random
rng = random.Random(11)
def octa():
    T=[(0,2,4),(2,1,4),(1,3,4),(3,0,4),(2,0,5),(1,2,5),(3,1,5),(0,3,5)]
    return 6,[list(t) for t in T]
def subdivide(n,T):
    out=[]
    for (a,b,c) in T:
        m=n; n+=1; out+= [[a,b,m],[b,c,m],[c,a,m]]
    return n,out
def flip_random(n,T,k):
    for _ in range(k):
        i=rng.randrange(len(T)); t=T[i]; e=rng.randrange(3); u,v=t[e],t[(e+1)%3]; x=t[(e+2)%3]
        # find the other triangle containing directed edge v->u
        js=[j for j,s in enumerate(T) if j!=i and any(s[q]==v and s[(q+1)%3]==u for q in range(3))]
        if len(js)!=1: continue
        j=js[0]; s=T[j]; q=[q for q in range(3) if s[q]==v and s[(q+1)%3]==u][0]; y=s[(q+2)%3]
        if x==y: continue
        # degree >=3 preservation
        deg=lambda a: sum(a in tt for tt in T)
        if deg(u)<=3 or deg(v)<=3: continue
        T[i]=[x,y,v] if True else None; T[j]=[y,x,u]
        # orientation: original (u,v,x) and (v,u,y); new (x,y,v)?? check: keep ccw: (u,y,x)?  use (x,u,y) and (y,v,x)
        T[i]=[x,u,y]; T[j]=[y,v,x]
    return T
def star(T,v):
    # cyclic list of triangles around v (ordered), using directed edges
    tris=[t for t in T if v in t]
    nxt={}
    for t in tris:
        q=t.index(v); a=t[(q+1)%3]; b=t[(q+2)%3]
        nxt.setdefault(a,[]).append((b,tuple(t)))
    # walk
    order=[]; start=tris[0]; q=start.index(v); a=start[(q+1)%3]
    used=set(); cur=a; 
    # handle multi: use triangle identity
    tlist=[tuple(t) for t in tris]
    seq=[tlist[0]]; usedi={0}
    while len(seq)<len(tlist):
        t=seq[-1]; q=t.index(v); b=t[(q+2)%3]
        cand=[k for k,s in enumerate(tlist) if k not in usedi and s[(s.index(v)+1)%3]==b]
        if not cand: return None
        usedi.add(cand[0]); seq.append(tlist[cand[0]])
    return seq
bad=0; cnt=0; maxfans={}
multi=0
for trial in range(800):
    n,T=octa()
    for _ in range(rng.randrange(1,4)): n,T=subdivide(n,T)
    T=flip_random(n,T,rng.randrange(50,400))
    # sanity: Euler
    E=set(); 
    nb={v:[] for v in range(n)}
    for t in T:
        for q in range(3): nb[t[q]].append(t[(q+1)%3])
    stars={v:star(T,v) for v in range(n)}
    from collections import Counter as _C
    if any(max(_C(nb[v]).values())>1 for v in range(n)): multi+=1
    if any(s is None for s in stars.values()): continue
    for sub in range(15):
        p=rng.uniform(.5,.97)
        H={v for v in range(n) if rng.random()<p}
        if len(H)==n or not H: continue
        Ho={v for v in H if all(u in H for u in nb[v])}
        if not Ho: continue
        D=[tuple(t) for t in T if any(x in Ho for x in t)]
        Dset=set(map(lambda t: tuple(t),D))
        fans=[]  # (v, list of triangles)
        for v in H-Ho:
            seq=stars[v]; inD=[t in Dset for t in seq]
            if not any(inD): continue
            assert not all(inD)
            k0=inD.index(False); m=len(seq)
            run=[]
            for i in range(1,m+1):
                t=seq[(k0+i)%m]
                if t in Dset: run.append(t)
                elif run: fans.append((v,run)); run=[]
            if run: fans.append((v,run))
        # (a)
        if any(len(r)<2 for _,r in fans): bad+=1; print("fan of 1 triangle!")
        from collections import Counter
        fc=Counter(v for v,_ in fans)
        for v,k in fc.items():
            d=len(stars[v]); maxfans[d]=max(maxfans.get(d,0),k)
            if k>(d-2+1)//3: bad+=1; print("too many fans", d, k)
        # resolved complex: vertex ids: interior v -> ('i',v); fan -> ('f',idx)
        vid={}
        for idx,(v,r) in enumerate(fans):
            for t in r: vid[(t,v)]=('f',idx)
        def rv(t,v): return ('i',v) if v in Ho else vid[(t,v)]
        F=len(D); edges={}
        for t in D:
            for q in range(3):
                a=rv(t,t[q]); b=rv(t,t[(q+1)%3])
                key=frozenset([a,b]) if a!=b else None
                assert key is not None
                edges.setdefault((min(t[q],t[(q+1)%3]),max(t[q],t[(q+1)%3]),key),[]).append(t)
        # edges with same endpoints but different underlying multi-edges: distinguish by adjacent triangle pairing
        # count edges: each D-triangle side; interior edge shared by 2 D-triangles that are adjacent across it.
        sides=0; shared=0
        for t in D:
            for q in range(3):
                a,b=t[q],t[(q+1)%3]
                # neighbour triangle across directed edge a->b is the one with b->a
                nbt=[s for s in T if any(s[w]==b and s[(w+1)%3]==a for w in range(3))]
                # with multi-edges, several; pick the one adjacent in the star of a
                st=stars[a]; i=st.index(t); prev=st[(i-1)%len(st)]
                sides+=1
                if prev in Dset: shared+=1
        Ecount=sides-shared//2
        Vcount=len(Ho)+len(fans)
        chi=Vcount-Ecount+F
        lhs=sum(6-len(stars[v]) for v in Ho)+sum(3-len(r) for _,r in fans)
        if lhs!=6*chi: bad+=1; print("GB identity fails", lhs, chi)
        # components of D^ via union-find on resolved vertices
        par={}
        def fd(x):
            while par.setdefault(x,x)!=x: x=par[x]
            return x
        for t in D:
            vs=[rv(t,x) for x in t]
            for x in vs[1:]: par[fd(x)]=fd(vs[0])
        ncomp=len({fd(x) for x in par})
        if sum(len(stars[v])-6 for v in Ho) > sum(6-len(r) for _,r in fans)-12*ncomp: bad+=1; print("inequality (d) fails")
        cnt+=1
print("triangulations with multi-edges:",multi,"cases:",cnt,"failures:",bad,"max fans by degree:",dict(sorted(maxfans.items())))
