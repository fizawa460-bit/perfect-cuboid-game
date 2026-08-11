from itertools import product
from math import isclose

checks=0
for r in range(1,9):
    pts=list(product((-1,1), repeat=r))
    reps=[]; seen=set()
    for x in pts:
        if x in seen: continue
        y=tuple(-v for v in x)
        seen.add(x); seen.add(y); reps.append(x)
    n=len(reps)
    for mask in range(min(1<<n,256)):
        f=[(mask>>j)&1 for j in range(n)]
        mu=sum(f)/n
        var=sum((v-mu)**2 for v in f)/n
        assert isclose(var,mu*(1-mu),rel_tol=0,abs_tol=1e-12)
        checks+=1
print({'variance_checks':checks,'max_rank':8})