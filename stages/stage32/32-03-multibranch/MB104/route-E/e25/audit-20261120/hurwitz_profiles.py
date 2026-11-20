# E25 audit (section 3, supplement): for n <= 6, every 6-tuple (t_1..t_6) with sum 2n-2 and t_i <= n/2 is the
# profile (numbers of transpositions) of a transitive 6-tuple of involutions in S_n with product 1
# (= a slack-0 cover over the 6 points). Independent meet-in-the-middle search (not E21's hurwitz.py).
import itertools, sys
from collections import defaultdict
def invols(n):
    out=[]
    for p in itertools.permutations(range(n)):
        if all(p[p[x]]==x for x in range(n)):
            out.append((p, sum(1 for x in range(n) if p[x]!=x)//2))
    return out
def mul(p,q): return tuple(p[q[x]] for x in range(len(q)))  # p∘q
def inv(p):
    r=[0]*len(p)
    for i,x in enumerate(p): r[x]=i
    return tuple(r)
def orbits(n,gens):
    par=list(range(n))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for g in gens:
        for x in range(n): par[f(x)]=f(g[x])
    lab={}; return tuple(lab.setdefault(f(x),len(lab)) for x in range(n))
def join_single(n,P,Q):
    par=list(range(n))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for R in (P,Q):
        first={}
        for x,b in enumerate(R):
            if b in first: par[f(x)]=f(first[b])
            else: first[b]=x
    return len({f(x) for x in range(n)})==1
for n in range(2,int(sys.argv[1])+1 if len(sys.argv)>1 else 7):
    I=invols(n); e=tuple(range(n))
    F=defaultdict(lambda: defaultdict(set))
    for (a,ta),(b,tb),(c,tc) in itertools.product(I,repeat=3):
        g=mul(mul(a,b),c); F[g][orbits(n,(a,b,c))].add((ta,tb,tc))
    got=set()
    for g,D1 in F.items():
        D2=F.get(inv(g))
        if not D2: continue
        for P,S1 in D1.items():
            for Q,S2 in D2.items():
                if join_single(n,P,Q):
                    for s1 in S1:
                        for s2 in S2: got.add(s1+s2)
    target={t for t in itertools.product(range(n//2+1),repeat=6) if sum(t)==2*n-2}
    g0={t for t in got if sum(t)==2*n-2}   # genus-0 (slack-0) tuples
    print(n,'profiles',len(target),'realized',len(g0&target),'genus0 outside target (should be 0)',len(g0-target),
          'PASS' if g0==target else 'FAIL', flush=True)
