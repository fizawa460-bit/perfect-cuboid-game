#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path
from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18

HERE = Path(__file__).resolve().parent
BC2_17 = HERE / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
BC2_18 = HERE / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json"
BC2_19 = HERE / "bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json"
PREFLIGHT = HERE / "bc2-21-first64-unknown-parent-slice-preflight.json"

EXPECTED_BC2_17 = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
EXPECTED_BC2_18 = "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
EXPECTED_BC2_19 = "62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"
EXPECTED_PREFLIGHT = "7af1bad407a8bfebdbbe1048a6d309092a16fcae818fd7ba1e26b996e5845c47"
EXPECTED_PARENT_COUNT = 7336
NORMAL_COUNT, ALL140_COUNT, PICARD_RANK = 92, 140, 64
NORMAL_MASS, TARGET_E = 112, 8

def csha(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def checked(path, expected, replay=True):
    o=json.loads(path.read_text())
    if o.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"canonical field drift: {path.name}")
    if replay:
        q=dict(o); q.pop("canonical_sha256_without_this_field",None)
        if csha(q)!=expected:
            raise ValueError(f"canonical replay drift: {path.name}")
    return o

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--per-parent-timeout-ms",type=int,default=5000)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    if a.per_parent_timeout_ms<=0: raise ValueError("timeout")

    c17=checked(BC2_17,EXPECTED_BC2_17)
    c18=checked(BC2_18,EXPECTED_BC2_18,replay=False)
    c19=checked(BC2_19,EXPECTED_BC2_19)
    pf=checked(PREFLIGHT,EXPECTED_PREFLIGHT)
    targets=[int(x) for x in pf["slice"]["indices"]]
    if len(targets)!=64 or len(set(targets))!=64 or targets!=sorted(targets):
        raise ValueError("target slice regression")
    if c19["result"]["unknown_count"]!=236 or c19["result"]["unsat_count"]!=7100 or c19["result"]["sat_count"]!=0:
        raise ValueError("BC2-19 partition regression")
    if c18["exact_decomposition"]["mod8_extendable_parent_count"]!=EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-18 count regression")

    fixed={int(k):int(v) for k,v in c17["retarget"]["fixed_exceptional_pairings"].items()}
    bundle=d18.load_retained(d18.RETAINED,"s32ex5_bc221_bundle")
    marking=d18.load_retained(d18.MARKING,"s32ex5_bc221_marking")
    adapter=d18.HperpIntegralPairingAdapter.from_retained(marking,bundle)
    P=Matrix(adapter.pairing_matrix)
    if P.shape!=(ALL140_COUNT,PICARD_RANK): raise ValueError("matrix shape")
    selected_labels=[int(v) for v in d18.INDLIST]
    selected_indices=[v-1 for v in selected_labels]
    Psel=P.extract(selected_indices,list(range(PICARD_RANK)))
    Pinv=Psel.inv(); den=d18.lcm_denominator(Pinv)
    if den!=8: raise ValueError("denominator")
    Bq=Pinv*den
    B=Matrix([[int(Bq[i,j]) for j in range(Bq.cols)] for i in range(Bq.rows)])
    selN=[j for j,l in enumerate(selected_labels) if l<=NORMAL_COUNT]
    selE=[j for j,l in enumerate(selected_labels) if l>NORMAL_COUNT]
    selElabels=[selected_labels[j] for j in selE]
    free=[l for l in selElabels if l not in fixed]
    full_check=d18.build_hnf_extension_check(B,den,selE,selN)

    parents=[]
    for comp in d18.weak_compositions_at_most(6,len(free)):
        by=dict(fixed); by.update({l:int(v) for l,v in zip(free,comp)})
        yE=[by[l] for l in selElabels]
        if d18.feasible(full_check,yE):
            parents.append((tuple(int(v) for v in comp),yE))
    if len(parents)!=EXPECTED_PARENT_COUNT: raise ValueError("parent enumeration drift")
    if max(targets)>=len(parents): raise ValueError("slice index range")

    x=[Int(f"x_{j}") for j in range(PICARD_RANK)]
    p=[sum(int(P[i,j])*x[j] for j in range(PICARD_RANK)) for i in range(ALL140_COUNT)]
    s=SolverFor("QF_LIA"); s.set(timeout=a.per_parent_timeout_ms)
    for i in range(NORMAL_COUNT): s.add(p[i]>=0,p[i]<=NORMAL_MASS)
    for i in range(NORMAL_COUNT,ALL140_COUNT): s.add(p[i]>=0,p[i]<=TARGET_E)
    s.add(sum(p[:NORMAL_COUNT])==NORMAL_MASS)
    s.add(sum(p[NORMAL_COUNT:])==TARGET_E)
    for l,v in fixed.items(): s.add(p[l-1]==v)

    results=[]; sat_witness=None
    for idx in targets:
        comp,yE=parents[idx]
        s.push()
        for l,v in zip(selElabels,yE): s.add(p[l-1]==int(v))
        r=s.check()
        rec={"parent_index":idx,"result":str(r)}
        if r==unknown: rec["reason_unknown"]=s.reason_unknown()
        elif r==sat:
            m=s.model()
            xv=[int(m.eval(q,model_completion=True).as_long()) for q in x]
            pv=[sum(int(P[i,j])*xv[j] for j in range(PICARD_RANK)) for i in range(ALL140_COUNT)]
            if min(pv)<0 or sum(pv[:NORMAL_COUNT])!=NORMAL_MASS or sum(pv[NORMAL_COUNT:])!=TARGET_E:
                raise ValueError("SAT witness validation")
            rec["all140_pairings_sha256"]=csha(pv)
            if sat_witness is None:
                sat_witness={"parent_index":idx,"picard64_coordinates":xv,"all140_pairings":pv,
                             "all140_pairings_sha256":csha(pv)}
        results.append(rec); s.pop()

    u=sum(r["result"]=="unsat" for r in results)
    q=sum(r["result"]=="unknown" for r in results)
    t=sum(r["result"]=="sat" for r in results)
    if t:
        status="PASS_FIRST64_SLICE_PICARD64_FEASIBLE_WITNESS_FOUND_NO_CURVE_CREDIT"
        nxt="BC2_22_ANALYZE_FIRST64_SLICE_SAT_WITNESS"
    elif q==0:
        status="PASS_FIRST64_RETAINED_UNKNOWN_SLICE_EXACT_UNSAT"
        nxt="BC2_22_RECOVER_OR_REPLAY_REMAINING_172_UNKNOWN_IDENTITIES"
    else:
        status="BLOCKED_FIRST64_RETAINED_UNKNOWN_SLICE_HAS_UNKNOWN"
        nxt="BC2_22_RESOLVE_FIRST64_RESIDUAL_UNKNOWN_WITH_LONGER_OR_PARTITIONED_CHECK"
    body={
      "schema":"STAGE32EX5_BC2_21_FIRST64_RETAINED_UNKNOWN_PARENT_SLICE_V1",
      "stage":"32EX5","unit":"BC2_21_FIRST64_RETAINED_UNKNOWN_PARENT_SLICE","status":status,
      "source_locks":{"bc2_17":EXPECTED_BC2_17,"bc2_18":EXPECTED_BC2_18,"bc2_19":EXPECTED_BC2_19,
                      "preflight":EXPECTED_PREFLIGHT,"retained_bundle":d18.EXPECTED_BUNDLE_CANONICAL,
                      "retained_marking":d18.EXPECTED_MARKING_CANONICAL},
      "slice":{"source_bc2_19_unknown_count":236,"checked_indices":targets,"checked_count":64,
               "other_unknown_identity_count":172,"other_unknown_identities_not_inferred":True},
      "result":{"unsat_count":u,"unknown_count":q,"sat_count":t,"records":results,
                "per_parent_timeout_ms":a.per_parent_timeout_ms,"solver":"Z3_QF_LIA",
                "z3_version":get_version_string()},
      "sat_witness":sat_witness,
      "credit":{"first64_slice_exact_unsat":t==0 and q==0,"whole_first_block_unsat":False,
                "whole_stratum_closed":False,"full178_complete":False,"stage32_main_credit":False,
                "effectivity_or_actual_curve_existence_proved":False},
      "firewalls":{"other_172_unknown_relabelled_unsat":False,"unknown_relabelled_unsat":False,
                   "sat_relabelled_actual_curve":False,"main_promotion":False,"merge_authorized":False},
      "next_exact_unit":{"id":nxt,"main_promotion_authorized":False}
    }
    body["canonical_sha256_without_this_field"]=csha(body)
    a.output.write_text(json.dumps(body,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"canonical":body["canonical_sha256_without_this_field"],"status":status,
                      "unsat":u,"unknown":q,"sat":t,"next":nxt},sort_keys=True))

if __name__=="__main__": main()
