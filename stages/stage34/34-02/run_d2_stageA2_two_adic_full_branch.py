#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-full-support-projective.json"
OUT=ROOT/"d2-stageA2-two-adic-full-branch.json"


def csha(rows):
    return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def forms(a,b,T,S,m):
    U=(T*T-S*S)%m
    V=(2*T*S)%m
    A=(a*U+b*V)%m
    B=(b*U+a*V)%m
    return U,V,A,B


def survives(delta,a,b,k):
    m=1<<k
    poss={d:{(d*r*r)%m for r in range(m)} for d in set(delta)}
    for T in range(m):
        for S in range(m):
            if T%2==0 and S%2==0: continue
            vals=forms(a,b,T,S,m)
            if all(v in poss[d] for v,d in zip(vals,delta)):
                return True
    return False


data=json.loads(SRC.read_text())
assert data["status"]=="PASS_EXACT_FULL_SUPPORT_PROJECTIVE_REDUCTION"
assert data["remaining_d1"]==92 and data["remaining_d2"]==0
records=[]
counts={k:0 for k in range(2,7)}
for rec in data["cases"]:
    if int(rec["d"])!=1 or int(rec["survivors"])==0: continue
    a,b=int(rec["a"]),int(rec["b"])
    initial=[tuple(map(int,x)) for x in rec["survivor_squareclasses"]]
    level={}
    cur=initial
    for k in range(2,7):
        cur=[d for d in cur if survives(d,a,b,k)]
        level[str(k)]={"modulus":1<<k,"survivors":len(cur),"sha256":csha(cur)}
        counts[k]+=len(cur)
    records.append({
      "q":rec["q"],"input":len(initial),"levels":level,
      "survivors":len(cur),"survivor_squareclasses":[list(x) for x in cur]
    })
    print(f"PASS {rec['q']}: {len(initial)} -> {level['2']['survivors']} -> {level['3']['survivors']} -> {level['4']['survivors']} -> {level['5']['survivors']} -> {len(cur)}")
expected={2:84,3:76,4:70,5:64,6:64}
assert counts==expected
byq={r["q"]:r["levels"]["5"]["survivors"] for r in records}
assert byq=={"20/21":8,"80/39":12,"24/7":8,"84/13":8,"48/55":8,"20/99":12,"60/11":8}
payload={
 "schema":"STAGE34_02_D2_STAGEA2_TWO_ADIC_FULL_BRANCH_V1",
 "status":"PASS_EXACT_PRIMITIVE_MOD32_BRANCH_OBSTRUCTION",
 "source":"d2-stageA2-full-support-projective.json",
 "source_lock":"d2-stageA2-two-adic-full-branch-lock.json",
 "input":92,
 "level_totals":{"4":84,"8":76,"16":70,"32":64,"64":64},
 "eliminated_by_mod32":28,
 "survivors":64,
 "cases":records,
 "credit":"No primitive mod-32 solution to the four square congruences is a rigorous Q_2 and Q obstruction. Survivors receive no Q_2 or Q-point credit.",
 "firewalls":{"mod32_survivor_is_Q2_point":False,"mod32_survivor_is_Q_point":False,"direct_cover_rational_points_complete":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"input":92,"survivors":64,"eliminated":28},sort_keys=True))
