#!/usr/bin/env python3
from __future__ import annotations
import collections,itertools,json,pathlib,runpy
ROOT=pathlib.Path(__file__).resolve().parent
ns=runpy.run_path(str(ROOT/"run_d2_stageA2_rank1_mw_congruence_sieve.py"))
sel=ns["sel"]; first=ns["payload"]
residual={x["branch_id"] for x in first["unresolved"]}; assert len(residual)==52
selected=set(int(x["model_id"]) for x in sel["selected_rank1_models"]); assert len(selected)==14
# Every rank-one model present on the exact 76-branch table.
all_rank1=set()
rows=[]
for br in sel["branches"]:
    if br["branch_id"] not in residual:continue
    mids=sorted({int(x["model_id"]) for x in br["pair_ranks"] if int(x["rank"])==1})
    all_rank1.update(mids)
    extra=sorted(set(mids)-selected)
    rows.append({"branch_id":br["branch_id"],"q":br["q"],"rank1_models":mids,"additional_rank1_models":extra})
assert len(rows)==52
extra_models=sorted(all_rank1-selected)
coverage={m:{r["branch_id"] for r in rows if m in r["additional_rank1_models"]} for m in extra_models}
# Exhaust all subsets: maximize branch coverage, then minimize model count, then lexicographic ids.
def best_cover(models):
    best=None
    models=list(models)
    for mask in range(1<<len(models)):
        mids=[models[i] for i in range(len(models)) if mask>>i&1]
        cov=set()
        for m in mids:cov|=coverage[m]
        key=(-len(cov),len(mids),tuple(mids))
        if best is None or key<best[0]:best=(key,mids,cov)
    return best[1],best[2]
best_all,cov_all=best_cover(extra_models)
without6=[m for m in extra_models if m!=6]
best_no6,cov_no6=best_cover(without6)
no_extra=[r for r in rows if not r["additional_rank1_models"]]
per_model=[]
for m in extra_models:
    qs=collections.Counter(r["q"] for r in rows if m in r["additional_rank1_models"])
    per_model.append({"model_id":m,"covered_residual_branches":len(coverage[m]),"by_q":dict(sorted(qs.items()))})
covered_best=set(cov_all)
uncovered=[r for r in rows if r["branch_id"] not in covered_best]
rank1count=collections.Counter(str(len(r["rank1_models"])) for r in rows)
payload={
 "schema":"STAGE34_02_D2_STAGEA2_ADDITIONAL_RANK1_MODEL_COVER_PROBE_V1",
 "status":"DIAGNOSTIC_NO_CREDIT",
 "input_residual_branches":52,
 "already_certified_models":sorted(selected),
 "additional_rank1_model_ids":extra_models,
 "additional_rank1_model_count":len(extra_models),
 "per_model":per_model,
 "branches_with_no_additional_rank1":len(no_extra),
 "no_additional_rank1_by_q":dict(sorted(collections.Counter(r["q"] for r in no_extra).items())),
 "rank1_model_count_histogram_on_residual":dict(sorted(rank1count.items())),
 "best_all":{"models":best_all,"model_count":len(best_all),"covered":len(cov_all),"uncovered":52-len(cov_all)},
 "best_without_model6":{"models":best_no6,"model_count":len(best_no6),"covered":len(cov_no6),"uncovered":52-len(cov_no6)},
 "best_all_uncovered_by_q":dict(sorted(collections.Counter(r["q"] for r in uncovered).items())),
 "firewalls":{"probe_is_MW_basis_credit":False,"coverage_is_branch_closure":False,"uncovered_is_impossibility":False,"R29_EXT_CHANG_C_closed":False}
}
print("ADDITIONAL_RANK1_COVER_PROBE="+json.dumps(payload,sort_keys=True))
