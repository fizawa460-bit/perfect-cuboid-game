#!/usr/bin/env python3
from __future__ import annotations

import bisect
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
WORKER=HERE/"run_fibration_nef_selective_picard_workunit.py"
WORKER_BLOB="3bbc4ba84f7ba5bf7188929d56c4a273ca0532f5"
FAST=HERE/"verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB="a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
ONE=HERE/"verify_fibration_nef_lowmass_separable_x4_0000.py"
ONE_BLOB="e2125399170e95a9ae5d09569b2b9d9e666ef7cf"
SELECTED5=HERE/"verify_fibration_nef_zero_center_selected5.py"
SELECTED5_BLOB="e100af258f9e928b23843ad764864449d3c25656"
SUPPORT=HERE/"verify_fibration_nef_zero_center_x4_support_bound.py"
SUPPORT_BLOB="58eb122b0c0154bd798d33ecbd7bedd9b30c2483"
WEIGHTED=HERE/"verify_fibration_nef_weighted_signature_counter_preflight.py"
WEIGHTED_BLOB="be2817633e1ef60e0415927889e1d589bec99aa4"
INDEXER=HERE.parents[3]/"stages/stage32/residual-32-01-production/compressed_terminal_indexer.py"
INDEXER_BLOB="4fb0a8dd34909494bd62646373e42877ed7a3c9e"


def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)


def git_blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def load_module(path:Path,name:str):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod)
    return mod


def indexed_h(poly):
    qs=sorted(poly)
    prefix=[]
    run=0
    for q in qs:
        run+=poly[q];prefix.append(run)
    return qs,prefix


def cumulative_indexed(aq,hidx,threshold:int)->int:
    if threshold<0:return 0
    qs,prefix=hidx
    total=0
    for qa,ma in aq.items():
        pos=bisect.bisect_right(qs,threshold-qa)-1
        if pos>=0: total+=ma*prefix[pos]
    return total


def stream_sha(rows)->str:
    h=hashlib.sha256()
    for row in rows:
        h.update(json.dumps(row,sort_keys=True,separators=(",",":")).encode());h.update(b"\n")
    return h.hexdigest()


def main()->None:
    locks={
      "worker":(WORKER,WORKER_BLOB),"closed":(FAST,FAST_BLOB),
      "x4one":(ONE,ONE_BLOB),"selected5":(SELECTED5,SELECTED5_BLOB),
      "support":(SUPPORT,SUPPORT_BLOB),"weighted":(WEIGHTED,WEIGHTED_BLOB),
      "compressed_terminal_indexer":(INDEXER,INDEXER_BLOB),
    }
    for name,(path,sha) in locks.items():
        req(path.is_file() and git_blob(path)==sha,f"source drift {name}")
    weighted_text=WEIGHTED.read_text()
    indexer_text=INDEXER.read_text()
    req('"x4_independent_of_exceptional_family": True' in weighted_text,
        "x4 independence source drift")
    req('stride = indexer.normal_budget + 1' in weighted_text,
        "canonical x4 stride source drift")
    req("return 19 * self.d - 5 * self.e" in indexer_text, "normal-budget formula drift")
    req("exceptional_rank, x4 = divmod(rank, self.normal_budget + 1)" in indexer_text,
        "canonical unrank x4 stride drift")
    req("rank = exceptional_rank * (self.normal_budget + 1) + x[4]" in indexer_text,
        "canonical rank x4 stride drift")

    worker=load_module(WORKER,"stage32_178_e32_worker")
    fast=load_module(FAST,"stage32_178_e32_closed")
    one=load_module(ONE,"stage32_178_e32_one")
    rt=worker.load_runtime()
    req((rt["g"],rt["d"],rt["e"],rt["qcap"])==(1,192,32,4992),"target drift")
    req(all(v==0 for v in rt["kernel"].center),"conditional center drift")
    req(tuple(rt["kernel"].r_degrees)==(0,0,0,0,0),"residual degrees drift")
    req(rt["kernel"].penalty==fast.EXPECTED_PENALTY,"penalty drift")

    normal_budget=19*rt["d"]-5*rt["e"]
    req(normal_budget==3488,"normal budget drift")
    qexc_global_max=rt["e"]*rt["e"]
    req(qexc_global_max==1024,"qexc max drift")

    # Static Picard/parity feasibility is independent of x4.
    base=[]
    static_picard_unsat=0
    parity_mass_unsat=0
    for a,b,c,t,min_q in rt["static_keys"]:
        R=rt["e"]-a-b-c
        req(R>=0,"static key exceeds e")
        req(0<=t<=a+b+c<=rt["e"],"t/mass bound drift")
        p=fast.parity_witness((a,b,c,t,0,rt["e"],rt["d"]))
        if p is None:
            static_picard_unsat+=1;continue
        p0,p1,p2,p3,p4=p
        req((p2,p3,p4)==(0,0,0),"tail parity drift")
        if p0+p1>R:
            parity_mass_unsat+=1;continue
        base.append((a,b,c,t,int(min_q),p0,p1))
    req(len(base)+static_picard_unsat+parity_mass_unsat==len(rt["static_keys"]),
        "base accounting mismatch")

    # Uniform full-pass band x4=0..109:
    # qexc<=1024 and the worst endpoint is x4=109,t=32 with |96-218-32|=154.
    # max residual minimum is 3/5, hence exact cut >=
    # 4992-154^2/6-6/5 > 1024.
    flat_lower=0;flat_upper=109
    flat_cut_lower=Fraction(4992)-Fraction(154*154,6)-Fraction(6,5)
    req(flat_cut_lower>qexc_global_max,"flat x4 band no longer uniformly passes qexc")

    # Uniform zero band x4>=135 from GRF04 at qexc=0 and t>=0.
    zero_from=135
    zero_rho=Fraction((96-2*zero_from)**2,12)
    req(zero_rho>2496,"uniform zero x4 boundary drift")

    # Materialize each exceptional polynomial once.  qcap=4992 is above the
    # exact qexc maximum 1024, so sum(A)*sum(H) is the full mass of one static key.
    a_cache={}
    h_cache={}
    h_index={}
    key_mass={}
    base_slice_mass=0
    for a,b,c,t,_min_q,_p0,_p1 in base:
        if a not in a_cache:a_cache[a]=rt["sel"].a_poly_for_key(a,rt["qcap"])
        hk=(b,c,t)
        if hk not in h_cache:
            h_cache[hk]=rt["sel"].h_poly_for_key(b,c,t,rt["qcap"])
            h_index[hk]=indexed_h(h_cache[hk])
        k=(a,b,c,t)
        mass=sum(a_cache[a].values())*sum(h_cache[hk].values())
        key_mass[k]=mass
        base_slice_mass+=mass

    req(base_slice_mass==324815269,
        "flat-slice mass no longer matches exact selected5 replay boundary")

    tail_rows=[]
    tail_total=0
    evidence=[]
    for x4 in range(110,135):
        pruned=0;survivors=0;mass_total=0;zero_mass=0
        tmin=None;tmax=None
        for a,b,c,t,min_q,p0,p1 in base:
            minimum,threshold=one.exact_threshold(
                g=rt["g"],d=rt["d"],t=t,x4=x4,p0=p0,p1=p1)
            tmin=threshold if tmin is None else min(tmin,threshold)
            tmax=threshold if tmax is None else max(tmax,threshold)
            if min_q>threshold:
                pruned+=1;continue
            survivors+=1
            mass=cumulative_indexed(a_cache[a],h_index[(b,c,t)],min(rt["qcap"],threshold))
            if mass==0:zero_mass+=1
            mass_total+=mass
        req(pruned+survivors==len(base),f"tail accounting mismatch x4={x4}")
        row={"x4":x4,"pruned_static_keys":pruned,"surviving_static_keys":survivors,
             "zero_mass_static_keys":zero_mass,"exact_weighted_mass":str(mass_total),
             "threshold_min":tmin,"threshold_max":tmax}
        tail_rows.append(row);tail_total+=mass_total;evidence.append(row)

    flat_slice_count=flat_upper-flat_lower+1
    flat_total=flat_slice_count*base_slice_mass
    full_row_total=flat_total+tail_total
    zero_slice_count=normal_budget-zero_from+1
    req(flat_slice_count+len(tail_rows)+zero_slice_count==normal_budget+1,
        "x4 partition count mismatch")

    out={
      "schema":"STAGE32_32_01_178_ZERO_CENTER_E32_FULL_X4_ROW_V1",
      "role":"COMPLETE_E32_X4_COVERAGE_RESEARCH_RESULT__ZERO_MAIN_CREDIT__AUDIT_PENDING",
      "source_locks":{name:sha for name,(_p,sha) in locks.items()},
      "target":{"row_id":"g1-d192","g":1,"d":192,"e":32,
                "normal_budget_x4_range":[0,normal_budget]},
      "exact_partition":{
        "flat_full_pass_x4":[0,109],"flat_slice_count":flat_slice_count,
        "tail_exact_x4":[110,134],"tail_slice_count":len(tail_rows),
        "uniform_zero_x4":[135,normal_budget],"uniform_zero_slice_count":zero_slice_count,
        "partition_covers_every_integer_x4":True,
        "x4_independent_of_exceptional_family":True,
      },
      "static_reduction":{
        "static_keys_before_picard":len(rt["static_keys"]),
        "static_picard_congruence_unsat_keys":static_picard_unsat,
        "minimum_parity_mass_unsat_keys":parity_mass_unsat,
        "x4_independent_picard_feasible_static_keys":len(base),
        "qexc_global_max":qexc_global_max,
      },
      "result":{
        "flat_one_slice_exact_weighted_mass":str(base_slice_mass),
        "flat_110_slice_exact_weighted_mass":str(flat_total),
        "tail_rows":tail_rows,
        "tail_25_slice_exact_weighted_mass":str(tail_total),
        "uniform_zero_band_exact_weighted_mass":"0",
        "complete_e32_x4_exact_weighted_mass":str(full_row_total),
        "A_keys_materialized":len(a_cache),"H_keys_materialized":len(h_cache),
        "tail_summary_stream_sha256":stream_sha(evidence),
      },
      "execution":{
        "old_depth2_survivor_pass_used":False,
        "five_dimensional_branch_and_bound_used":False,
        "runkey_used":False,"heavy_execution_armed":False,"artifact_production_armed":False,
      },
      "next_exact_step":"freeze this complete e32-row result with exact-head CI evidence and send it to hostile audit before any MAIN numerical credit; after audit, test which other low-e FULL178 rows satisfy the same zero-center/parity/x4-band architecture",
      "firewalls":{
        "complete_e32_x4_coverage_computed":True,
        "full_row_census_credit_claimed":False,
        "full178_census_claimed":False,"main_credit_changed":False,
        "theorem_credit_changed":False,"endpoint_credit_changed":False,"merge":False,
      },
    }
    print("ZERO_CENTER_E32_FULL_X4_ROW_SUMMARY="+json.dumps({
      "static_keys":len(rt["static_keys"]),"base_picard_feasible":len(base),
      "flat_slice_mass":str(base_slice_mass),"flat_slices":flat_slice_count,
      "tail_total":str(tail_total),"tail_slices":len(tail_rows),
      "zero_slices":zero_slice_count,"full_row_mass":str(full_row_total),
      "A_keys":len(a_cache),"H_keys":len(h_cache),
      "tail_rows":[{"x4":r["x4"],"survivors":r["surviving_static_keys"],
                    "mass":r["exact_weighted_mass"]} for r in tail_rows],
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
