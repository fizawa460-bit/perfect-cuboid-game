#!/usr/bin/env python3
from __future__ import annotations
import hashlib, itertools, json, math, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
FIBERS=[(20,21),(80,39),(24,7),(84,13),(48,55),(20,99),(60,11)]


def factor(n:int)->list[int]:
    n=abs(n); out=[]; p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p=3 if p==2 else p+2
    if n>1:out.append(n)
    return out

def v2(n:int)->int:
    n=abs(n); c=0
    while n and n%2==0:c+=1;n//=2
    return c

def isprime(n:int)->bool:
    if n<2:return False
    if n%2==0:return n==2
    p=3
    while p*p<=n:
        if n%p==0:return False
        p+=2
    return True

def csha(rows)->str:
    return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def leg(x:int,p:int)->int:
    x%=p
    if x==0:return 0
    return 1 if pow(x,(p-1)//2,p)==1 else -1

# Coordinate ordering: U,V,A=aU+bV,B=bU+aV.
def branch_deltas(a:int,b:int,d:int):
    states={(1,1,1,1)}
    for p in [x for x in factor(a) if x!=2]:
        opts=[(),(0,3),(1,2)] # p|a: {U,B} or {V,A}
        states={tuple(x[i]*(p if i in ids else 1) for i in range(4)) for x in states for ids in opts}
    for p in [x for x in factor(b) if x!=2]:
        opts=[(),(0,2),(1,3)] # p|b: {U,A} or {V,B}
        states={tuple(x[i]*(p if i in ids else 1) for i in range(4)) for x in states for ids in opts}
    for p in [x for x in factor(a*a-b*b) if x!=2]:
        opts=[(),(2,3)] # p|a^2-b^2: {A,B}
        states={tuple(x[i]*(p if i in ids else 1) for i in range(4)) for x in states for ids in opts}
    if d==2:
        opts2=[(),(0,1,2,3)]
    elif v2(a)==2:
        opts2=[(),(0,1,2,3)]
    else:
        opts2=[(),(1,2),(0,1,2,3)]
    states={tuple(x[i]*(2 if i in ids else 1) for i in range(4)) for x in states for ids in opts2}
    out=set()
    for x in states:
        for mask in range(16):
            if mask.bit_count()%2:continue # product sign positive
            y=list(x)
            for i in range(4):
                if mask>>i&1:y[i]*=-1
            out.add(tuple(y))
    # Every prime/sign occurs in an even number of squareclasses, so product is square.
    for x in out:
        z=math.prod(x)
        assert z>0 and math.isqrt(z)**2==z
    return sorted(out)

def forms(a:int,b:int,d:int,T:int,S:int,p:int):
    if d==1:
        U=(T*T-S*S)%p; V=(2*T*S)%p
    else:
        U=(2*T*T-S*S)%p; V=(2*T*T-4*T*S+S*S)%p
    A=(a*U+b*V)%p; B=(b*U+a*V)%p
    return U,V,A,B

def projective_signatures(a:int,b:int,d:int,p:int):
    sigs=set()
    for T in range(p):
        vals=forms(a,b,d,T,1,p)
        sigs.add(tuple(leg(z,p) for z in vals))
    vals=forms(a,b,d,1,0,p)
    sigs.add(tuple(leg(z,p) for z in vals))
    return sigs

def branch_locally_possible(delta,p,sigs):
    ds=tuple(leg(x,p) for x in delta)
    assert 0 not in ds
    for fs in sigs:
        if all(f==0 or f==d for f,d in zip(fs,ds)):
            return True
    return False

def support(a,b):return set(factor(2*a*b*(a*a-b*b)))

records=[]
for a,b in FIBERS:
    q=f"{a}/{b}"; supp=support(a,b)
    candidates=[p for p in range(3,212) if isprime(p) and p not in supp]
    for d in (1,2):
        initial=branch_deltas(a,b,d); cur=initial[:]; selected=[]; steps=[]
        sigcache={p:projective_signatures(a,b,d,p) for p in candidates}
        for _ in range(8):
            best=None
            for p in candidates:
                if p in selected:continue
                nxt=[x for x in cur if branch_locally_possible(x,p,sigcache[p])]
                key=(len(nxt),p)
                if best is None or key<best[0]:best=(key,p,nxt)
            if best is None:break
            _,p,nxt=best
            if len(nxt)>=len(cur):break
            selected.append(p); cur=nxt
            steps.append({"p":p,"survivors":len(cur),"survivor_sha256":csha(cur)})
            if not cur:break
        rec={
          "q":q,"a":a,"b":b,"d":d,"support_primes":sorted(supp),
          "initial_exact_overapprox_branches":len(initial),
          "selected_good_primes":selected,"steps":steps,
          "survivors":len(cur),"survivor_sha256":csha(cur),
          "survivor_squareclasses":[list(x) for x in cur]
        }
        records.append(rec)
        print(f"PASS {q} d={d}: {len(initial)} -> {len(cur)} using {selected}")

payload={
 "schema":"STAGE34_02_D2_STAGEA2_FACTOR_BRANCH_LOCAL_SIEVE_V1",
 "status":"PASS_EXACT_GOOD_PRIME_PROJECTIVE_LOCAL_NECESSARY_SIEVE",
 "source_odd_support":"d2-stageA2-odd-squareclass-support-lock.json",
 "source_two_adic":"d2-stageA2-two-adic-pattern-lock.json",
 "candidate_good_primes":"odd primes <=211 outside 2*a*b*(a^2-b^2)",
 "selection":"greedy up to eight primes, deterministic minimum-survivor then minimum-prime tie break",
 "cases":records,
 "total_initial_branches":sum(r["initial_exact_overapprox_branches"] for r in records),
 "total_survivors":sum(r["survivors"] for r in records),
 "globally_eliminated_cases":[[r["q"],r["d"]] for r in records if r["survivors"]==0],
 "credit":"A branch killed by absence of a projective mod-p solution at a good support-external prime is globally impossible. Surviving branches are necessary-condition survivors only.",
 "firewalls":{
   "surviving_local_branch_is_Q_point":False,
   "good_prime_filter_is_support_prime_Qp_analysis":False,
   "factor_branch_sieve_closes_receiver":False,
   "R29_EXT_CHANG_C_closed":False
 }
}
(ROOT/"d2-stageA2-factor-branch-local.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"initial":payload["total_initial_branches"],"survivors":payload["total_survivors"]},sort_keys=True))
