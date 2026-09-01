#!/usr/bin/env python3
from __future__ import annotations
import collections,json,pathlib,runpy
from fractions import Fraction
ROOT=pathlib.Path(__file__).resolve().parent
ns=runpy.run_path(str(ROOT/"run_d2_stageA2_rank1_mw_congruence_sieve.py"))
sel=ns["sel"]; first=ns["payload"]
add=json.loads((ROOT/"d2-stageA2-additional-rank1-selection.json").read_text())
mw=json.loads((ROOT/"d2-stageA2-additional-rank1-mw-default.json").read_text())
assert add["status"]=="PASS_EXACT_SEVEN_NON6_RANK1_MODELS_COVER_28_OF_52" and add["covered_branches"]==28
assert mw["status"]=="PASS_ALL_7_ADDITIONAL_UNCONDITIONAL_FULL_MW_BASES" and mw["certified_count"]==7
gens={int(x["model_id"]):ns["parse_gen"](x["mwrank_o_line"]) for x in mw["models"]}
brmap={x["branch_id"]:x for x in sel["branches"]}

def branch_data_pair(br,mid,pair):
 ent=next(x for x in br["pair_ranks"] if x["pair"]==pair and int(x["model_id"])==mid);assert int(ent["rank"])==1
 s=int(ent["squareclass"]);q=br["q"];f1,f2=pair.split('*');roots1=ns["roots_form"](q,f1);r=next(x for x in roots1 if x is not None)
 A,B,C,D,pp,qq=ns["direct_cubic"](q,pair,s,r);a4=Fraction(int(ent["a4"]));a6=Fraction(int(ent["a6"]));assert a4==81*pp and a6==729*qq
 roots=roots1+ns["roots_form"](q,f2);assert len(roots)==4 and len(set(roots))==4
 tors=[None]
 for rr in roots:
  if rr==r:continue
  x=3*B if rr is None else 9*A/(rr-r)+3*B;assert x**3+a4*x+a6==0;tors.append((x,Fraction(0)))
 assert len(tors)==4 and len({str(x) for x in tors})==4
 G=gens[mid];assert G[1]**2==G[0]**3+a4*G[0]+a6
 return {"mid":mid,"pair":pair,"s":s,"q":q,"r":r,"A":A,"B":B,"a4":a4,"a6":a6,"tors":tors,"G":G}
closed=[];details=[]
for rec in add["branches"]:
 br=brmap[rec["branch_id"]];mid=int(rec["selected_model_id"]);best=None
 for pair in rec["pair_occurrences"]:
  bd=branch_data_pair(br,mid,pair);ok,used,counts,mods=ns["sieve_branch"](br,bd)
  row={"q":br["q"],"branch_id":br["branch_id"],"model_id":mid,"pair":pair,"closed":ok,"used_primes":[[u["p"],u["generator_order"]] for u in used],"final_state_counts":counts}
  details.append(row)
  if ok:best=row;break
 if best:closed.append(best)
cc=collections.Counter(x["q"] for x in closed)
print("ADDITIONAL_RANK1_MW_SIEVE_PROBE="+json.dumps({"status":"DIAGNOSTIC_NO_CREDIT","input_targeted_branches":28,"newly_closed_count":len(closed),"newly_closed_by_q":dict(sorted(cc.items())),"remaining_from_52":52-len(closed),"closed":closed},sort_keys=True))
