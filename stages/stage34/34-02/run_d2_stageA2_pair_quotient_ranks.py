#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, re, subprocess

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-full-support-projective.json"
OUT=ROOT/"d2-stageA2-pair-quotient-ranks.json"
RAW=ROOT/"d2-stageA2-pair-quotient-ranks-stdout.txt"
FULL="The rank and full Mordell-Weil basis have been determined unconditionally."
PAIR_LIST=[(0,2),(0,3),(1,2),(1,3),(2,3)]
NAMES=["U","V","A","B"]
BOUNDS=[None,12,14,15]


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
        while n%p==0:
            n//=p; parity^=1
        if parity:out*=p
    return sign*out


def form_coeffs(a:int,b:int):
    return [
      [1,0,-1],
      [0,2,0],
      [a,2*b,-a],
      [b,2*a,-b]
    ]


def mul_quadratics(q1,q2):
    out=[0]*5
    for i,x in enumerate(q1):
        for j,y in enumerate(q2):
            out[i+j]+=x*y
    return out


def invariants(c):
    a,b,c2,d,e=c
    I=12*a*e-3*b*d+c2*c2
    J=72*a*c2*e+9*b*c2*d-27*a*d*d-27*b*b*e-2*c2**3
    return I,J


def parse_rank(stdout:str):
    lines=[ln.strip().replace(" ","") for ln in stdout.splitlines() if ln.strip().startswith("[[")]
    for ln in reversed(lines):
        m=re.match(r"^\[\[(\d+)\],",ln)
        if m:return int(m.group(1)),ln
    raise RuntimeError("could not parse mwrank rank line")


def h(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def certify_curve(curve:str,idx:int,a4:int,a6:int):
    attempts=[]
    hard_bad=["unable to saturate","saturation failed","not saturated"]
    for bound in BOUNDS:
        cmd=["mwrank","-q","-v","1","-o"]
        if bound is not None: cmd += ["-b",str(bound)]
        proc=subprocess.run(cmd,input=curve,text=True,capture_output=True,timeout=240)
        txt=proc.stdout+("\nSTDERR:\n"+proc.stderr if proc.stderr else "")
        attempts.append({"bound":10 if bound is None else bound,"command":" ".join(cmd),"returncode":proc.returncode,"stdout":txt})
        low=txt.lower()
        if proc.returncode!=0:
            continue
        if any(s in low for s in hard_bad):
            raise RuntimeError(f"mwrank saturation warning model {idx} bound={bound}")
        if FULL in txt and "conditional rank" not in low:
            rank,oline=parse_rank(txt)
            return rank,oline,attempts
    # Persist all inconclusive attempts before failing closed.
    RAW.write_text("\n".join(
      f"===== model={idx} a4={a4} a6={a6} bound={a['bound']} cmd={a['command']} =====\n{a['stdout']}"
      for a in attempts
    ))
    raise RuntimeError(f"no unconditional full-basis marker model {idx} through bound 15")


data=json.loads(SRC.read_text())
assert data["status"]=="PASS_EXACT_FULL_SUPPORT_PROJECTIVE_REDUCTION"
assert data["remaining_d1"]==92 and data["remaining_d2"]==0

models={}
parent=[]
for rec in data["cases"]:
    if int(rec["d"])!=1 or int(rec["survivors"])==0:continue
    q=rec["q"]; a=int(rec["a"]); b=int(rec["b"]); forms=form_coeffs(a,b)
    for delta0 in rec["survivor_squareclasses"]:
        delta=tuple(map(int,delta0)); branch_id=h([q,delta])[:20]
        entries=[]
        for i,j in PAIR_LIST:
            s=sf(delta[i]*delta[j])
            quartic=[s*x for x in mul_quadratics(forms[i],forms[j])]
            I,J=invariants(quartic)
            a4=-27*I; a6=-27*J
            assert 4*a4**3+27*a6**2!=0
            key=(a4,a6)
            if key not in models:
                models[key]={
                  "a4":a4,"a6":a6,"I":I,"J":J,
                  "quartic_example":quartic,
                  "associations":[]
                }
            assoc={"q":q,"branch_id":branch_id,"pair":f"{NAMES[i]}*{NAMES[j]}","pair_indices":[i,j],"squareclass":s}
            models[key]["associations"].append(assoc)
            entries.append({"pair":assoc["pair"],"model_key":[a4,a6],"squareclass":s})
        parent.append({"q":q,"delta":list(delta),"branch_id":branch_id,"quotients":entries})

assert len(parent)==92
assert sum(len(x["quotients"]) for x in parent)==460
assert len(models)==48

raw=[]; model_records=[]; rank_by_key={}
for idx,key in enumerate(sorted(models),1):
    m=models[key]; a4,a6=key
    curve=f"[0,0,0,{a4},{a6}]\n"
    try:
        rank,oline,attempts=certify_curve(curve,idx,a4,a6)
    except Exception:
        # Include all completed prior models as well as the failing-model attempts.
        if raw:
            prev="\n".join(raw)
            failtxt=RAW.read_text() if RAW.exists() else ""
            RAW.write_text(prev+"\n"+failtxt)
        raise
    for attempt in attempts:
        raw.append(f"===== model={idx} a4={a4} a6={a6} bound={attempt['bound']} cmd={attempt['command']} =====\n{attempt['stdout']}")
    rank_by_key[key]=rank
    accepted=next(a for a in reversed(attempts) if FULL in a["stdout"] and "conditional rank" not in a["stdout"].lower() and a["returncode"]==0)
    model_records.append({
      "model_id":idx,"a4":a4,"a6":a6,"I":m["I"],"J":m["J"],
      "rank":rank,"unconditional_full_basis":True,"mwrank_o_line":oline,
      "accepted_bound":accepted["bound"],"attempted_bounds":[a["bound"] for a in attempts],
      "association_count":len(m["associations"]),
      "association_sha256":h(m["associations"]),
      "raw_section_sha256":hashlib.sha256(accepted["stdout"].encode()).hexdigest(),
      "example_association":m["associations"][0]
    })
    print(f"PASS model={idx}/48 rank={rank} bound={accepted['bound']} associations={len(m['associations'])}")

RAW.write_text("\n".join(raw))
rank0_models={key for key,r in rank_by_key.items() if r==0}
parent_out=[]
branches_with_rank0=0
for p in parent:
    r0=[]; ranks=[]
    for ent in p["quotients"]:
        key=tuple(ent["model_key"]); rr=rank_by_key[key]
        ranks.append({"pair":ent["pair"],"rank":rr,"squareclass":ent["squareclass"]})
        if rr==0:r0.append(ent["pair"])
    if r0:branches_with_rank0+=1
    parent_out.append({"q":p["q"],"branch_id":p["branch_id"],"delta":p["delta"],"pair_ranks":ranks,"rank0_pairs":r0})

rank_hist={}
for r in rank_by_key.values():rank_hist[str(r)]=rank_hist.get(str(r),0)+1
payload={
 "schema":"STAGE34_02_D2_STAGEA2_PAIR_QUOTIENT_RANKS_V2_BOUND_ESCALATION",
 "status":"PASS_UNCONDITIONAL_PAIR_QUOTIENT_JACOBIAN_RANKS",
 "source":"d2-stageA2-full-support-projective.json",
 "source_lock":"d2-stageA2-pair-quotient-lock.json",
 "mwrank_bound_source_lock":"d2-stageA2-pair-quotient-mwrank-bound-lock.json",
 "software":{"package":"eclib-tools","routine":"mwrank","base_command":"mwrank -q -v 1 -o","fallback_bounds":[12,14,15],"required_success_marker":FULL},
 "parent_branches":92,
 "quotient_conditions":460,
 "distinct_models":48,
 "rank_histogram":rank_hist,
 "rank_zero_models":len(rank0_models),
 "branches_with_at_least_one_rank_zero_quotient":branches_with_rank0,
 "models":model_records,
 "branches":parent_out,
 "credit":"This is target selection only. Rank zero gives no parent-branch exclusion until the quotient quartic rational-point set is proved complete (or empty) and pulled back exactly.",
 "firewalls":{"rank_zero_jacobian_closes_torsor":False,"positive_rank_is_Q_point":False,"pair_quotient_rank_table_closes_branch":False,"direct_cover_rational_points_complete":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"models":48,"rank_histogram":rank_hist,"rank0_models":len(rank0_models),"branches_with_rank0":branches_with_rank0},sort_keys=True))
