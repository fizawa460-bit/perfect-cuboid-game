# E25 audit: independent enumeration of the parity table (E25 section 2).
# Points of Omega carry vectors in G=(Z/2)^3: a point of O1\O2 or O2\O1 with label c gives e_c,
# a common point with labels c!=d gives e_c+e_d. Condition: sum = 0. delta = |span|. RH (gamma=0):
# 2g-2 = -2 delta + (delta/2)|Omega|.
import itertools
def vec(*ls):
    v=0
    for l in ls: v^=1<<l
    return v
def span(vs):
    S={0}
    for v in vs: S|={s^v for s in S}
    return len(S)
cases={'(1,1)':(1,1),'(2,2)':(2,2),'(1,3)':(1,3)}
for name,(m1,m2) in cases.items():
    for h in range(0,5-(m1+m2)):
        res={}
        diffpairs=[(c,d) for c in range(3) for d in range(3) if c!=d]
        for L1 in itertools.product(range(3),repeat=m1):
            for L2 in itertools.product(range(3),repeat=m2):
                for H in itertools.product(diffpairs,repeat=h):
                    vs=[vec(c) for c in L1]+[vec(c) for c in L2]+[vec(c,d) for c,d in H]
                    s=0
                    for v in vs: s^=v
                    if s: continue
                    dl=span(vs); om=m1+m2+h
                    g2=-2*dl+dl*om//2+2
                    assert g2%2==0
                    res.setdefault(dl,set()).add(g2//2)
        print(name,'h=',h,'|Omega|=',m1+m2+h,'delta->g:',{k:sorted(v) for k,v in sorted(res.items())} or 'none')
