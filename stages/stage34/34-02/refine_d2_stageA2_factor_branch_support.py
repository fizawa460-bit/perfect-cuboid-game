#!/usr/bin/env python3
import json, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
src=ROOT/"d2-stageA2-factor-branch-local.json"
data=json.loads(src.read_text())

def leg2(p:int)->int:
    return 1 if pow(2,(p-1)//2,p)==1 else -1

def factor(n:int):
    n=abs(n); out=[]; p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p=3 if p==2 else p+2
    if n>1:out.append(n)
    return out

records=[]
for rec in data["cases"]:
    a,b,d=int(rec["a"]),int(rec["b"]),int(rec["d"])
    before=int(rec["survivors"])
    cur=[tuple(x) for x in rec["survivor_squareclasses"]]
    bad=[]
    if d==2:
        bad=[p for p in factor(a*b) if p!=2 and leg2(p)==-1]
        cur=[x for x in cur if not any(any(abs(v)%p==0 for v in x) for p in bad)]
    out={
      "q":rec["q"],"a":a,"b":b,"d":d,
      "input_survivors":before,
      "legendre2_nonsquare_support_primes":bad,
      "survivors":len(cur),
      "survivor_squareclasses":[list(x) for x in cur]
    }
    records.append(out)
    print(f"PASS {rec['q']} d={d}: {before} -> {len(cur)} bad={bad}")

expected={
 "20/21:1":88,"20/21:2":24,
 "80/39:1":384,"80/39:2":12,
 "24/7:1":20,"24/7:2":8,
 "84/13:1":48,"84/13:2":4,
 "48/55:1":120,"48/55:2":8,
 "20/99:1":232,"20/99:2":8,
 "60/11:1":240,"60/11:2":18
}
assert {f"{r['q']}:{r['d']}":r['survivors'] for r in records}==expected
payload={
 "schema":"STAGE34_02_D2_STAGEA2_FACTOR_BRANCH_SUPPORT_REFINEMENT_V1",
 "status":"PASS_EXACT_SUPPORT_PRIME_LEGENDRE2_REFINEMENT",
 "source_local":"d2-stageA2-factor-branch-local.json",
 "source_theorem":"d2-stageA2-support-prime-legendre2-lock.json",
 "input_survivors":sum(r["input_survivors"] for r in records),
 "survivors":sum(r["survivors"] for r in records),
 "cases":records,
 "firewalls":{"survivor_is_Q_point":False,"support_refinement_is_full_Qp_classification":False,"receiver_closed":False,"R29_EXT_CHANG_C_closed":False}
}
assert payload["input_survivors"]==1946
assert payload["survivors"]==1214
(ROOT/"d2-stageA2-factor-branch-support.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"input":1946,"survivors":1214},sort_keys=True))
