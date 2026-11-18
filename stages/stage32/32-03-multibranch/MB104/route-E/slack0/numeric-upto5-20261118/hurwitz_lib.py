import itertools, sys
from collections import defaultdict
from math import factorial
def run(n):
    G=list(itertools.permutations(range(n))); idx={g:i for i,g in enumerate(G)}
    mul=[[idx[tuple(g[h[x]] for x in range(n))] for h in G] for g in G]
    def nt(g): return sum(1 for x in range(n) if g[x]!=x)//2
    inv=[i for i,g in enumerate(G) if idx[tuple(g[g[x]] for x in range(n))]==idx[tuple(range(n))]]
    bycls=defaultdict(list)
    for i in inv: bycls[nt(G[i])].append(i)
    def join(part,g):
        # part: tuple label per point; merge orbits under g
        lab=list(part)
        for x in range(n):
            a,b=lab[x],lab[G[g][x]]
            if a!=b: lab=[a if l==b else l for l in lab]
        # canonical
        m={};out=[]
        for l in lab:
            if l not in m: m[l]=len(m)
            out.append(m[l])
        return tuple(out)
    res={}
    e=idx[tuple(range(n))]
    for prof in itertools.product(range(n//2+1),repeat=6):
        if sum(prof)!=2*n-2: continue
        st={(e,tuple(range(n))):1}
        for t in prof:
            ns=defaultdict(int)
            for (g,pt),c in st.items():
                for h in bycls[t]:
                    ns[(mul[g][h],join(pt,h))]+=c
            st=ns
        tot=sum(c for (g,pt),c in st.items() if g==e and max(pt)==0)
        res[prof]=tot/factorial(n)
    return res
