#!/usr/bin/env python3
from __future__ import annotations
import json,pathlib,runpy
from fractions import Fraction

ROOT=pathlib.Path(__file__).resolve().parent
ns=runpy.run_path(str(ROOT/"run_d2_stageA2_rank1_mw_congruence_sieve.py"))
sel=ns["sel"]; gens=ns["gens"]; first_payload=ns["payload"]
unresolved_ids={x["branch_id"] for x in first_payload["unresolved"]}
assert len(unresolved_ids)==52

def branch_data_pair(br,pair):
    mid=int(br["selected_rank1_model"]["model_id"])
    ent=next(x for x in br["pair_ranks"] if x["pair"]==pair)
    assert int(ent["model_id"])==mid and int(ent["rank"])==1
    s=int(ent["squareclass"]);q=br["q"];f1,f2=pair.split('*')
    roots1=ns["roots_form"](q,f1);r=next(x for x in roots1 if x is not None)
    A,B,C,D,pp,qq=ns["direct_cubic"](q,pair,s,r)
    a4=Fraction(int(ent["a4"]));a6=Fraction(int(ent["a6"]))
    assert a4==81*pp and a6==729*qq
    roots=roots1+ns["roots_form"](q,f2);assert len(roots)==4 and len(set(roots))==4
    tors=[None]
    for rr in roots:
        if rr==r:continue
        x=3*B if rr is None else 9*A/(rr-r)+3*B
        assert x**3+a4*x+a6==0
        tors.append((x,Fraction(0)))
    assert len(tors)==4 and len({str(x) for x in tors})==4
    G=gens[mid];assert G[1]**2==G[0]**3+a4*G[0]+a6
    return {"mid":mid,"pair":pair,"s":s,"q":q,"r":r,"A":A,"B":B,"a4":a4,"a6":a6,"tors":tors,"G":G}

closed=[];tested=0;eligible=0;details=[]
for br in sel["branches"]:
    if br["branch_id"] not in unresolved_ids:continue
    occ=list(br["selected_rank1_model"]["pair_occurrences"])
    if len(occ)<2:continue
    eligible+=1
    for pair in occ[1:]:
        tested+=1;bd=branch_data_pair(br,pair);ok,used,counts,mods=ns["sieve_branch"](br,bd)
        details.append({"q":br["q"],"branch_id":br["branch_id"],"model_id":bd["mid"],"pair":pair,"closed":ok,"used_primes":[[u["p"],u["generator_order"]] for u in used],"final_state_counts":counts})
        if ok:
            closed.append(br["branch_id"]);break
payload2={"schema":"STAGE34_02_D2_STAGEA2_RANK1_ALTERNATE_OCCURRENCE_PROBE_V1","status":"DIAGNOSTIC_NO_CREDIT","input_remaining":52,"eligible_multi_occurrence_branches":eligible,"alternate_occurrences_tested":tested,"newly_closed_count":len(set(closed)),"newly_closed_by_q":{},"details":details,"firewalls":{"probe_is_closure_credit":False,"remaining_branches_closed":False,"R29_EXT_CHANG_C_closed":False}}
from collections import Counter
cc=Counter(x["q"] for x in details if x["closed"]);payload2["newly_closed_by_q"]=dict(sorted(cc.items()))
print("ALT_OCCURRENCE_PROBE="+json.dumps({k:payload2[k] for k in ["status","input_remaining","eligible_multi_occurrence_branches","alternate_occurrences_tested","newly_closed_count","newly_closed_by_q"]},sort_keys=True))
