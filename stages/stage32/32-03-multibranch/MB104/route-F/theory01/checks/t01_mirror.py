import itertools, numpy as np, collections
exec(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'t01_base_1x3.py')).read().split("stat=collections.Counter()")[0])
def cr(a,b,c,d): return (a-c)*(b-d)/((a-d)*(b-c))
maps=[]
for Sidx in itertools.combinations(range(6),4):
    for (num,den) in cubics([Bg[x] for x in Sidx]):
        maps.append((num,den,oddset(num,den,Sidx),Sidx))
def maxcirc(O):
    best=0;
    for tri in itertools.combinations(range(len(O)),3):
        n=3+sum(1 for k in range(len(O)) if k not in tri and abs(cr(O[tri[0]],O[tri[1]],O[tri[2]],O[k]).imag)<1e-8*(1+abs(cr(O[tri[0]],O[tri[1]],O[tri[2]],O[k]))))
        best=max(best,n)
    return best
def setequiv(P,Q):   # Moebius S with S(P)=Q as sets?
    for im in itertools.permutations(range(len(Q)),3):
        S=mobfrom(P[:3],[Q[k] for k in im])
        if all(min(abs(ap(S,z)-w) for w in Q)<1e-7 for z in P): return True
    return False
Os=[[z for z,_ in m[2]] for m in maps]
mc=[maxcirc(O) for O in Os]
print("max number of concyclic points of O, per map:",dict(collections.Counter(mc)))
# classes by holomorphic set-equivalence of O, and mirror relation
cls=[]
for i in range(60):
    for c in cls:
        if setequiv(Os[c[0]],Os[i]): c.append(i); break
    else: cls.append([i])
print("classes of O up to Moebius maps:",[len(c) for c in cls],"max concyclic per class:",[mc[c[0]] for c in cls])
for x in range(len(cls)):
    mir=[y for y in range(len(cls)) if setequiv([z.conjugate() for z in Os[cls[x][0]]],Os[cls[y][0]])]
    print("class",x,"mirror image is class",mir)
