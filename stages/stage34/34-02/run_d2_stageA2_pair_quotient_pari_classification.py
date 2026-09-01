#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, re, subprocess, sys

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-full-support-projective.json"
LOCK=ROOT/"d2-stageA2-pair-quotient-pari-classification-lock.json"
OUT=ROOT/"d2-stageA2-pair-quotient-pari-classification.json"
RAW=ROOT/"d2-stageA2-pair-quotient-pari-classification-stdout.txt"
PAIR_LIST=[(0,2),(0,3),(1,2),(1,3),(2,3)]
NAMES=["U","V","A","B"]
TIMEOUT=120

def factor(n:int):
    n=abs(n); out=[]; p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p=3 if p==2 else p+2
    if n>1:out.append(n)
    return out

def sf(n:int)->int:
    sign=-1 if n<0 else 1; n=abs(n); out=1
    for p in factor(n):
        parity=0
        while n%p==0:n//=p; parity^=1
        if parity:out*=p
    return sign*out

def form_coeffs(a:int,b:int):
    return [[1,0,-1],[0,2,0],[a,2*b,-a],[b,2*a,-b]]

def mul_quadratics(q1,q2):
    out=[0]*5
    for i,x in enumerate(q1):
        for j,y in enumerate(q2):out[i+j]+=x*y
    return out

def invariants(c):
    a,b,c2,d,e=c
    I=12*a*e-3*b*d+c2*c2
    J=72*a*c2*e+9*b*c2*d-27*a*d*d-27*b*b*e-2*c2**3
    return I,J

def h(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def pari_interval(a4:int,a6:int):
    program=f"E=ellinit([0,0,0,{a4},{a6}]);R=ellrank(E,0);print(\"STAGE34_RESULT=\",R[1],\",\",R[2],\",\",R[3]);quit;\n"
    try:
        proc=subprocess.run(["gp","-q","-f"],input=program,text=True,capture_output=True,timeout=TIMEOUT)
    except subprocess.TimeoutExpired as e:
        txt=(e.stdout.decode(errors='replace') if isinstance(e.stdout,bytes) else (e.stdout or ''))
        return None,None,None,"TIMEOUT",txt
    txt=proc.stdout+("\nSTDERR:\n"+proc.stderr if proc.stderr else "")
    m=re.search(r"STAGE34_RESULT=(-?\d+),(-?\d+),(-?\d+)",txt)
    if proc.returncode!=0 or not m:return None,None,None,"PARSE_OR_PROCESS_FAILURE",txt
    r,R,s=map(int,m.groups())
    if not (0<=r<=R):return None,None,None,"INVALID_INTERVAL",txt
    if R==0:status="PROVED_RANK_ZERO"
    elif r>=1:status="PROVED_RANK_NONZERO"
    else:status="UNRESOLVED_INTERVAL"
    return r,R,s,status,txt

lock=json.loads(LOCK.read_text()); data=json.loads(SRC.read_text())
assert lock["status"]=="SOURCE_LOCKED"
assert data["status"]=="PASS_EXACT_FULL_SUPPORT_PROJECTIVE_REDUCTION"
assert data["remaining_d1"]==92 and data["remaining_d2"]==0
models={}; parents=[]
for rec in data["cases"]:
    if int(rec["d"])!=1 or int(rec["survivors"])==0:continue
    q=rec["q"]; a=int(rec["a"]); b=int(rec["b"]); forms=form_coeffs(a,b)
    for delta0 in rec["survivor_squareclasses"]:
        delta=tuple(map(int,delta0)); branch_id=h([q,delta])[:20]; entries=[]
        for i,j in PAIR_LIST:
            s=sf(delta[i]*delta[j]); quartic=[s*x for x in mul_quadratics(forms[i],forms[j])]
            I,J=invariants(quartic); key=(-27*I,-27*J)
            assert 4*key[0]**3+27*key[1]**2!=0
            models.setdefault(key,{"a4":key[0],"a6":key[1],"I":I,"J":J,"associations":[]})
            assoc={"q":q,"branch_id":branch_id,"pair":f"{NAMES[i]}*{NAMES[j]}","squareclass":s}
            models[key]["associations"].append(assoc); entries.append({"pair":assoc["pair"],"model_key":list(key),"squareclass":s})
        parents.append({"q":q,"delta":list(delta),"branch_id":branch_id,"quotients":entries})
assert len(parents)==92 and sum(len(p["quotients"]) for p in parents)==460 and len(models)==48

raw=[]; model_records=[]; decision_by_key={}; unresolved=[]
for idx,key in enumerate(sorted(models),1):
    m=models[key]; r,R,s,status,txt=pari_interval(*key)
    raw.append(f"===== model={idx} a4={key[0]} a6={key[1]} =====\n{txt}")
    if status not in ("PROVED_RANK_ZERO","PROVED_RANK_NONZERO"):
        unresolved.append({"model_id":idx,"a4":key[0],"a6":key[1],"status":status,"interval":[r,R]})
    exact=r if r is not None and r==R else None
    decision_by_key[key]=status
    model_records.append({"model_id":idx,"a4":key[0],"a6":key[1],"I":m["I"],"J":m["J"],"rank_lower_bound":r,"rank_upper_bound":R,"exact_rank":exact,"sha2_mod_2sha4_rank":s,"classification":status,"association_count":len(m["associations"]),"association_sha256":h(m["associations"]),"example_association":m["associations"][0]})
    print(f"model={idx}/48 status={status} interval=[{r},{R}] associations={len(m['associations'])}")
RAW.write_text("\n".join(raw))
if unresolved:
    OUT.write_text(json.dumps({"schema":"STAGE34_02_D2_STAGEA2_PAIR_QUOTIENT_PARI_CLASSIFICATION_V1","status":"INCONCLUSIVE_UNRESOLVED_MODELS","unresolved":unresolved,"models":model_records,"firewalls":{"classification_closes_parent_branch":False,"R29_EXT_CHANG_C_closed":False}},indent=2,sort_keys=True)+"\n")
    raise SystemExit(2)

zero_keys={k for k,v in decision_by_key.items() if v=="PROVED_RANK_ZERO"}
branch_records=[]; branches_with_zero=0
for p in parents:
    zero=[]; pairs=[]
    for e in p["quotients"]:
        key=tuple(e["model_key"]); cls=decision_by_key[key]
        pairs.append({"pair":e["pair"],"classification":cls,"squareclass":e["squareclass"]})
        if key in zero_keys:zero.append(e["pair"])
    if zero:branches_with_zero+=1
    branch_records.append({"q":p["q"],"branch_id":p["branch_id"],"delta":p["delta"],"rank_zero_pairs":zero,"pair_classifications":pairs})
summary={"PROVED_RANK_ZERO":0,"PROVED_RANK_NONZERO":0}
for v in decision_by_key.values():summary[v]+=1
payload={"schema":"STAGE34_02_D2_STAGEA2_PAIR_QUOTIENT_PARI_CLASSIFICATION_V1","status":"PASS_ZERO_VS_NONZERO_RANK_CLASSIFICATION","source":"d2-stageA2-full-support-projective.json","source_lock":"d2-stageA2-pair-quotient-pari-classification-lock.json","software":{"package":"pari-gp","routine":"ellrank","effort":0},"parent_branches":92,"quotient_conditions":460,"distinct_models":48,"classification_histogram":summary,"rank_zero_models":len(zero_keys),"branches_with_at_least_one_rank_zero_quotient":branches_with_zero,"models":model_records,"branches":branch_records,"credit":"Target selection only; rank-zero quotient models require complete torsor pointset and exact pullback before any parent branch closes.","firewalls":{"rank_zero_jacobian_closes_quotient_torsor":False,"proved_positive_rank_is_Q_point_on_torsor":False,"classification_closes_parent_branch":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"models":48,"rank_zero_models":len(zero_keys),"branches_with_rank_zero":branches_with_zero,"classification_histogram":summary},sort_keys=True))
