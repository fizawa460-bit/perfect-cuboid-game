import sys,itertools
sys.argv=[sys.argv[0]]+sys.argv[1:]
from common import AUT
import hurwitz_lib
n=int(sys.argv[1])
H=hurwitz_lib.run(n)
seen=set(); reps=[]
for prof in sorted(H):
    if prof in seen: continue
    orb=set()
    for M,perm in AUT:
        # U∘f has profile t'(perm[y]) = t(y)
        t2=[0]*6
        for y in range(6): t2[perm[y]]=prof[y]
        orb.add(tuple(t2))
    seen|=orb; reps.append((prof,H[prof],len(orb)))
for r in reps: print(*r)
