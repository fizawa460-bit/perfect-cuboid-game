#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, math, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-factor-branch-support.json"
OUT=ROOT/"d2-stageA2-full-support-projective.json"
RANK0={1,2,10,26,66,195}


def factor(n:int)->list[int]:
    n=abs(n); out=[]; p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p=3 if p==2 else p+2
    if n>1: out.append(n)
    return out


def sf(n:int)->int:
    sign=-1 if n<0 else 1; n=abs(n); out=1
    for p in factor(n):
        parity=0
        while n%p==0:
            n//=p; parity^=1
        if parity: out*=p
    return sign*out


def csha(rows)->str:
    return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def forms(a:int,b:int,d:int,T:int,S:int,p:int):
    if d==1:
        U=(T*T-S*S)%p
        V=(2*T*S)%p
    else:
        U=(2*T*T-S*S)%p
        V=(2*T*T-4*T*S+S*S)%p
    A=(a*U+b*V)%p
    B=(b*U+a*V)%p
    return U,V,A,B


def locally_possible(delta:tuple[int,int,int,int],a:int,b:int,d:int,p:int)->bool:
    squares={x*x%p for x in range(p)}
    for T,S in [(t,1) for t in range(p)]+[(1,0)]:
        ok=True
        for f,dd in zip(forms(a,b,d,T,S,p),delta):
            dm=dd%p
            if dm==0:
                if f%p!=0:
                    ok=False; break
            elif (f*pow(dm,-1,p))%p not in squares:
                ok=False; break
        if ok:
            return True
    return False


def rankzero_keep(delta,d):
    e=abs(sf(int(delta[0])*int(delta[1])))
    if d==1:
        n=abs(sf(2*e))
        return n not in RANK0, n
    # The certified rank-zero reconstruction step closes only d2 e=1.
    return e!=1, e


data=json.loads(SRC.read_text())
assert data["status"]=="PASS_EXACT_SUPPORT_PRIME_LEGENDRE2_REFINEMENT"
assert data["survivors"]==1214

records=[]
rankzero_total=0
final_total=0
for rec in data["cases"]:
    q=rec["q"]; a=int(rec["a"]); b=int(rec["b"]); d=int(rec["d"])
    initial=[tuple(map(int,x)) for x in rec["survivor_squareclasses"]]
    post_rank=[]; rank_killed=[]
    for delta in initial:
        keep,n=rankzero_keep(delta,d)
        if keep: post_rank.append(delta)
        else: rank_killed.append({"delta":list(delta),"species":n})
    rankzero_total+=len(rank_killed)

    support=[p for p in factor(2*a*b*(a*a-b*b)) if p!=2]
    kept=[]; killed=[]; first_kill_counts={str(p):0 for p in support}
    for delta in post_rank:
        bad=[p for p in support if not locally_possible(delta,a,b,d,p)]
        if bad:
            first=min(bad)
            first_kill_counts[str(first)]+=1
            killed.append({"delta":list(delta),"obstructing_support_primes":bad})
        else:
            kept.append(delta)
    final_total+=len(kept)
    records.append({
      "q":q,"a":a,"b":b,"d":d,
      "input_after_legendre2":len(initial),
      "rankzero_reconstruction_eliminated":len(rank_killed),
      "after_rankzero":len(post_rank),
      "odd_support_primes":support,
      "support_projective_eliminated":len(killed),
      "survivors":len(kept),
      "first_obstruction_prime_counts":{k:v for k,v in first_kill_counts.items() if v},
      "survivor_sha256":csha(kept),
      "survivor_squareclasses":[list(x) for x in kept]
    })
    print(f"PASS {q} d={d}: {len(initial)} -> {len(post_rank)} -> {len(kept)} support={support}")

expected={
 "20/21:1":24,"20/21:2":0,
 "80/39:1":12,"80/39:2":0,
 "24/7:1":8,"24/7:2":0,
 "84/13:1":8,"84/13:2":0,
 "48/55:1":8,"48/55:2":0,
 "20/99:1":16,"20/99:2":0,
 "60/11:1":16,"60/11:2":0
}
assert {f"{r['q']}:{r['d']}":r['survivors'] for r in records}==expected
assert sum(r["after_rankzero"] for r in records)==1024
assert rankzero_total==190
assert final_total==92

payload={
 "schema":"STAGE34_02_D2_STAGEA2_FULL_SUPPORT_PROJECTIVE_SIEVE_V1",
 "status":"PASS_EXACT_FULL_SUPPORT_PROJECTIVE_REDUCTION",
 "source_support":"d2-stageA2-factor-branch-support.json",
 "source_rankzero":"d2-stageA2-reconstruction-rank-lock.json",
 "source_theorem":"d2-stageA2-full-support-projective-lock.json",
 "input_after_legendre2":1214,
 "rankzero_reconstruction_eliminated":rankzero_total,
 "input_after_rankzero":1024,
 "support_projective_eliminated":1024-final_total,
 "survivors":final_total,
 "remaining_d1":sum(r["survivors"] for r in records if r["d"]==1),
 "remaining_d2":sum(r["survivors"] for r in records if r["d"]==2),
 "cases":records,
 "credit":"No projective F_p solution at any tested odd support prime is a rigorous global branch exclusion by the locked primitive integral reduction lemma. Surviving branches are pruning only.",
 "firewalls":{"support_survivor_is_Q_point":False,"support_sieve_is_full_Qp_classification":False,"direct_cover_rational_points_complete":False,"all_multiples_closed":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"after_rankzero":1024,"survivors":92,"remaining_d1":92,"remaining_d2":0},sort_keys=True))
