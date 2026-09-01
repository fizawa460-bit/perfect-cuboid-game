#!/usr/bin/env python3
from __future__ import annotations
import collections,json,pathlib,runpy
ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-additional-rank1-selection-lock.json"
OUT=ROOT/"d2-stageA2-additional-rank1-selection.json"
ns=runpy.run_path(str(ROOT/"run_d2_stageA2_rank1_mw_congruence_sieve.py"))
sel=ns["sel"]; first=ns["payload"]
lock=json.loads(LOCK.read_text()); assert lock["status"]=="SOURCE_LOCKED_PREEXECUTION"
residual={x["branch_id"] for x in first["unresolved"]}; assert len(residual)==int(lock["input_remaining_branches"])
chosen=set(map(int,lock["selected_additional_rank1_model_ids"])); assert len(chosen)==7 and 6 not in chosen
rows=[]; models={}; cov=collections.Counter()
for br in sel["branches"]:
    if br["branch_id"] not in residual:continue
    occ=[]
    for x in br["pair_ranks"]:
        mid=int(x["model_id"]); rank=int(x["rank"])
        if mid in chosen:
            assert rank==1
            occ.append({"pair":x["pair"],"model_id":mid,"squareclass":int(x["squareclass"]),"a4":int(x["a4"]),"a6":int(x["a6"])})
            models.setdefault(mid,{"model_id":mid,"rank":1,"a4":int(x["a4"]),"a6":int(x["a6"])})
            assert models[mid]["a4"]==int(x["a4"]) and models[mid]["a6"]==int(x["a6"])
    mids=sorted({x["model_id"] for x in occ})
    if mids:
        assert len(mids)==1
        mid=mids[0]; cov[br["q"]]+=1
        rows.append({"q":br["q"],"branch_id":br["branch_id"],"delta":br["delta"],"selected_model_id":mid,"pair_occurrences":sorted(x["pair"] for x in occ),"squareclasses":sorted({x["squareclass"] for x in occ})})
assert sorted(models)==sorted(chosen)
covered={r["branch_id"] for r in rows}; uncovered=[x for x in first["unresolved"] if x["branch_id"] not in covered]
exp=lock["expected"]
assert len(rows)==int(exp["covered_branches"]) and len(uncovered)==int(exp["uncovered_branches"])
assert dict(sorted(cov.items()))==dict(sorted((k,int(v)) for k,v in exp["covered_by_q"].items()))
unc=collections.Counter(x["q"] for x in uncovered)
assert dict(sorted(unc.items()))==dict(sorted((k,int(v)) for k,v in exp["uncovered_by_q"].items()))
for mid in models:
    models[mid]["covered_branches"]=sum(r["selected_model_id"]==mid for r in rows)
payload={
 "schema":"STAGE34_02_D2_STAGEA2_ADDITIONAL_RANK1_SELECTION_V1",
 "status":"PASS_EXACT_SEVEN_NON6_RANK1_MODELS_COVER_28_OF_52",
 "source_lock":"d2-stageA2-additional-rank1-selection-lock.json",
 "input_remaining_branches":52,
 "selected_models":[models[m] for m in sorted(models)],
 "covered_branches":len(rows),"covered_by_q":dict(sorted(cov.items())),"branches":rows,
 "uncovered_branches":len(uncovered),"uncovered_by_q":dict(sorted(unc.items())),"uncovered_branch_ids":sorted(x["branch_id"] for x in uncovered),
 "credit":"Exact workload compression only. These seven rank-one models cover 28 residual parent branches; no MW basis or closure follows.",
 "firewalls":{"selection_is_MW_basis_credit":False,"selection_is_branch_closure":False,"uncovered_24_closed":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"selected_models":sorted(models),"covered":len(rows),"covered_by_q":payload["covered_by_q"],"uncovered":len(uncovered),"uncovered_by_q":payload["uncovered_by_q"]},sort_keys=True))
