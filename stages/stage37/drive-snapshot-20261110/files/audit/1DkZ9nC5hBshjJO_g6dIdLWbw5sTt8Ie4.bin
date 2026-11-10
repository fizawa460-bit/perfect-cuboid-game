from math import gcd,isqrt
from itertools import product
import json
from ti004_legendre import matrices,primes

def square(n):return n>=0 and isqrt(n)**2==n

def cover_obstruction(d,a,b,mod):
    sq={x*x%mod for x in range(mod)}
    return all((d*z**4+a*z*z*t*t+(b//d)*t**4)%mod not in sq
               for z in range(mod) for t in range(mod) if gcd(gcd(z,t),mod)==1)

checks=[]
for m,n in [(4,1),(9,4)]:
    r=matrices(m,n);u,v,w=r['U'],r['V'],r['W'];s=v*v+w*w
    for cols,rows,key in [(r['E_columns'],r['E_rows'],'E'),(r['Eprime_columns'],r['Eprime_rows'],'Eprime')]:
        kernel=[x for x in product((0,1),repeat=len(cols)) if all(sum(a*b for a,b in zip(x,row))%2==0 for row in rows)]
        assert len(kernel)==2**(len(cols)-r[key+'_rank'])
    for mask in product((0,1),repeat=len(r['E_columns'])):
        d=1
        for p,e in zip(r['E_columns'],mask):d*=p**e
        for q in primes(v*w):
            if q!=2 and pow(d%q,(q-1)//2,q)==q-1:
                assert cover_obstruction(d,-2*s,u**4,q);checks.append(['L1',m,n,d,q])
        for q in primes(u):
            if q%4==3 and d%q==0:
                assert cover_obstruction(d,-2*s,u**4,q**5);checks.append(['L2',m,n,d,q**5])
    for mask in product((0,1),repeat=len(r['Eprime_columns'])):
        d=1
        for p,e in zip(r['Eprime_columns'],mask):d*=p**e
        for sign in [1,-1]:
            for q in primes(u):
                if q%4==1 and pow(d%q,(q-1)//2,q)==q-1:
                    assert cover_obstruction(sign*d,4*s,16*v*v*w*w,q);checks.append(['L3',m,n,sign*d,q])

N=300
adj={x:set() for x in range(1,N+1)}
for x in adj:
    for y in range(x+1,N+1):
        if square(x*x+y*y):adj[x].add(y);adj[y].add(x)
records=[];seen=set()
for a in adj:
    for b in sorted(x for x in adj[a] if x>a):
        for c in sorted(x for x in adj[a]&adj[b] if x>b):
            if gcd(gcd(a,b),c)!=1:continue
            odd=[x for x in (a,b,c) if x%2];assert len(odd)==1
            X=odd[0];Y,Z=sorted(x for x in (a,b,c) if x!=X)
            sources=[]
            for leg in (Y,Z):
                h=gcd(X,leg);u,v=X//h,leg//h;w=isqrt(u*u+v*v)
                m,n=isqrt((w+u)//2),isqrt((w-u)//2)
                assert (m*m-n*n,2*m*n,m*m+n*n)==(u,v,w)
                sources.append((m,n,u,v))
            p,q=sources;g=gcd(p[2],q[2]);out=(p[2]*q[2]//g,p[3]*q[2]//g,p[2]*q[3]//g)
            assert out==(X,Y,Z)
            K=isqrt((p[3]*q[2])**2+(p[2]*q[3])**2);assert K*K==(p[3]*q[2])**2+(p[2]*q[3])**2 and K%g==0
            pair=(p[:2],q[:2]);assert pair not in seen;seen.add(pair)
            records.append(dict(edges=[X,Y,Z],sources=pair,g=g,D=K//g))
assert len(records)==2
result=dict(status='PASS',local_full_pair_checks=len(checks),local_checks=checks,
            master_independent_edge_enumeration={'diagnostic_max_edge':300,'bricks':records},
            warning='Diagnostic max edge is not the Stage37 physical R cutoff; no density or saving claim.')
open('ti004_audit.json','w').write(json.dumps(result,indent=2));print(json.dumps(result))
