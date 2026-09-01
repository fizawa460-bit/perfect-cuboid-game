#!/usr/bin/env python3
from __future__ import annotations
import collections, hashlib, json, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-full-support-projective.json"
CLOSED=ROOT/"d2-stageA2-rankzero-AB-complete-pullback.json"
LOCK=ROOT/"d2-stageA2-rank1-cover-selection-lock.json"
OUT=ROOT/"d2-stageA2-rank1-cover-selection.json"
PAIR_LIST=[(0,2),(0,3),(1,2),(1,3),(2,3)]
NAMES=["U","V","A","B"]

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

def form_coeffs(a:int,b:int):return [[1,0,-1],[0,2,0],[a,2*b,-a],[b,2*a,-b]]
def mul(q1,q2):
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

lock=json.loads(LOCK.read_text()); data=json.loads(SRC.read_text()); closed=json.loads(CLOSED.read_text())
assert lock["status"]=="SOURCE_LOCKED"
assert data["status"]=="PASS_EXACT_FULL_SUPPORT_PROJECTIVE_REDUCTION" and data["remaining_d1"]==92
assert closed["status"]=="PASS_COMPLETE_QPOINTSETS_AND_EXACT_PARENT_PULLBACK" and closed["remaining_d1_factor_branches"]==76
rankvec=list(map(int,lock["source_pair_classification"]["model_ranks_by_sorted_model_id_1_to_48"]))
assert len(rankvec)==48 and rankvec.count(0)==2 and rankvec.count(1)==26 and rankvec.count(2)==18 and rankvec.count(3)==2
selected=set(map(int,lock["selected_rank1_model_ids"])); assert len(selected)==14
closed_ids={b["branch_id"] for b in closed["branches"]}; assert len(closed_ids)==16

model_keys=set(); branch_raw=[]
for rec in data["cases"]:
    if int(rec["d"])!=1 or int(rec["survivors"])==0:continue
    q=rec["q"]; a=int(rec["a"]); b=int(rec["b"]); forms=form_coeffs(a,b)
    for delta0 in rec["survivor_squareclasses"]:
        delta=tuple(map(int,delta0)); branch_id=h([q,delta])[:20]; entries=[]
        for i,j in PAIR_LIST:
            s=sf(delta[i]*delta[j]); coeff=[s*x for x in mul(forms[i],forms[j])]; I,J=invariants(coeff); key=(-27*I,-27*J)
            model_keys.add(key); entries.append((f"{NAMES[i]}*{NAMES[j]}",key,s))
        branch_raw.append((q,branch_id,delta,entries))
assert len(branch_raw)==92 and len(model_keys)==48
sorted_keys=sorted(model_keys); id_by_key={k:i+1 for i,k in enumerate(sorted_keys)}; rank_by_key={k:rankvec[i] for i,k in enumerate(sorted_keys)}
assert all(rank_by_key[sorted_keys[mid-1]]==1 for mid in selected)

rows=[]; pattern_hist=collections.Counter(); rank1count_hist=collections.Counter(); pair_occ_hist=collections.Counter(); selected_coverage=collections.Counter()
for q,branch_id,delta,entries in branch_raw:
    if branch_id in closed_ids:continue
    pairs=[]; selected_occurrences=[]
    for pair,key,s in entries:
        mid=id_by_key[key]; rank=rank_by_key[key]
        pairs.append({"pair":pair,"model_id":mid,"rank":rank,"squareclass":s,"a4":key[0],"a6":key[1]})
        if mid in selected:
            assert rank==1; selected_occurrences.append({"pair":pair,"model_id":mid})
    selected_ids=sorted({x["model_id"] for x in selected_occurrences})
    assert len(selected_ids)==int(lock["expected_distinct_selected_model_count_per_branch"])
    chosen_mid=selected_ids[0]
    chosen_pairs=sorted(x["pair"] for x in selected_occurrences if x["model_id"]==chosen_mid)
    assert len(chosen_pairs) in (1,2)
    pair_occ_hist[str(len(chosen_pairs))]+=1
    pattern=tuple(x["rank"] for x in pairs); pattern_hist[str(list(pattern))]+=1
    rank1count_hist[str(sum(r==1 for r in pattern))]+=1
    selected_coverage[str(chosen_mid)]+=1
    rows.append({"q":q,"branch_id":branch_id,"delta":list(delta),"pair_ranks":pairs,"selected_rank1_model":{"model_id":chosen_mid,"pair_occurrences":chosen_pairs}})
assert len(rows)==76
expected_patterns={str(k):int(v) for k,v in lock["expected_rank_patterns_in_pair_order_UA_UB_VA_VB_AB"].items()}
def compact(s):return s.replace(" ","")
assert {compact(k):v for k,v in pattern_hist.items()}=={compact(k):v for k,v in expected_patterns.items()}
assert dict(sorted(rank1count_hist.items()))==dict(sorted((str(k),int(v)) for k,v in lock["expected_rank1_quotient_count_per_branch_histogram"].items()))
assert dict(sorted(pair_occ_hist.items()))==dict(sorted((str(k),int(v)) for k,v in lock["expected_selected_pair_occurrence_histogram_per_branch"].items()))
assert sum(selected_coverage.values())==76
models=[]
for mid in sorted(selected):
    key=sorted_keys[mid-1]
    models.append({"model_id":mid,"rank":1,"a4":key[0],"a6":key[1],"covered_branches":selected_coverage[str(mid)]})
payload={
 "schema":"STAGE34_02_D2_STAGEA2_RANK1_MODEL_COVER_SELECTION_V2_DISTINCT_MODEL",
 "status":"PASS_EXACT_14_MODEL_RANK1_COVER_OF_76_BRANCHES",
 "source":"d2-stageA2-full-support-projective.json",
 "source_lock":"d2-stageA2-rank1-cover-selection-lock.json",
 "input_d1_branches":92,"closed_rankzero_AB_branches":16,"remaining_branches":76,
 "pair_order":["U*A","U*B","V*A","V*B","A*B"],
 "rank_pattern_histogram":dict(sorted(pattern_hist.items())),
 "rank1_quotient_count_per_branch_histogram":dict(sorted(rank1count_hist.items())),
 "selected_pair_occurrence_histogram_per_branch":dict(sorted(pair_occ_hist.items())),
 "distinct_selected_model_count_per_branch":1,
 "selected_rank1_models":models,
 "branches":rows,
 "credit":"Workload compression only: every remaining branch has quotient occurrence(s) from exactly one designated model among the 14 selected rank-one Jacobians. Duplicate symmetric pair occurrences do not duplicate MW-basis work. No branch closure or rational-point claim follows.",
 "firewalls":{"rank1_cover_is_branch_closure":False,"fourteen_is_proved_minimum":False,"duplicate_pair_occurrences_are_distinct_MW_models":False,"selected_quotient_point_is_parent_point":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"branches":76,"selected_models":14,"selected_pair_occurrence_histogram":dict(sorted(pair_occ_hist.items())),"coverage":dict(sorted(selected_coverage.items()))},sort_keys=True))
