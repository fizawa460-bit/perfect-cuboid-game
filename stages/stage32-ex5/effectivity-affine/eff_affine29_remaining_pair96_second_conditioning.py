#!/usr/bin/env python3
"""Exact second-pairing conditioning for remaining AFFINE24 pairing[96] values 1 and 0.

AFFINE28 closed value 2 structurally after direct FP42 growth became expensive.
Apply the same exact second-conditioner search to the two remaining values.
Unresolved 41D branches remain UNKNOWN. No downstream credit is promoted.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
AFF28=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine28_second_pairing_conditioning.py"
AFF28_BLOB="668303672b536019caa1aaaafa261d52cefabb7a"
EXPECTED={
    1:("835/24","355/24"),
    0:("841/24","361/24"),
}

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(path):
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec is not None and spec.loader is not None,"module spec")
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod; spec.loader.exec_module(mod)
    return mod

def analyze(first_value,expected_radius,expected_max,a28,eng,aff15,aff24,base_rows,base10,P,gram):
    a28.FIRST_VALUE=first_value
    first=aff24.build_conditioned_context(a28.FIRST_PAIR,base_rows,P,gram,aff15)
    req(first is not None and first["kernel_dimension"]==42,f"value{first_value} first context")
    cheap=aff24.branch_classification(first,base10,first_value,P,gram,eng)
    req(cheap["classification"]=="UNRESOLVED_AFTER_ONE_PAIRING_CONDITIONING",f"value{first_value} cheap class")
    req(cheap["exact_radius_squared"]==expected_radius,f"value{first_value} radius")
    req(cheap["exact_real_max_C2"]==expected_max,f"value{first_value} maxC2")

    t=aff24.selected_target(first,base10,first_value)
    icoord=first["invI"]*t
    req(all(getattr(v,"q",1)==1 for v in icoord),f"value{first_value} HNF")
    bp=first["A"]*icoord
    R=-(first["K"].T*gram*first["K"])
    forced=set(first["forced_indices"]+[a28.FIRST_PAIR])
    upper=[eng.NORMAL_MASS]*92+[eng.E]*48
    candidates=[]
    for pair_idx in range(140):
        if pair_idx in forced: continue
        coeff=P.row(pair_idx)*first["K"]
        if all(v==0 for v in coeff): continue
        domain=aff15.allowed_projection(P.row(pair_idx),bp,first["K"],R,first["solve_r"],gram,eng.LOW,upper[pair_idx])
        candidates.append({"pairing_index":pair_idx,"block":"normal" if pair_idx<92 else "exceptional",
                           "domain":domain,"domain_size":len(domain)})
    req(candidates,f"value{first_value} no candidates")
    candidates.sort(key=lambda r:(r["domain_size"],0 if r["block"]=="exceptional" else 1,r["pairing_index"]))

    immediate=next((r for r in candidates if r["domain_size"]==0),None)
    evaluated=[]
    if immediate is None:
        for cand in candidates[:a28.CANDIDATE_LIMIT]:
            ctx=a28.build_double_context(cand["pairing_index"],base_rows,P,gram,aff15)
            if ctx is None: continue
            branches=[a28.classify(ctx,base10,v,P,gram,eng) for v in cand["domain"]]
            unresolved=[b for b in branches if b["classification"]=="UNRESOLVED_AFTER_SECOND_PAIRING_CONDITIONING"]
            evaluated.append({
                "pairing_index":cand["pairing_index"],"block":cand["block"],
                "projection_domain":cand["domain"],"projection_domain_size":cand["domain_size"],
                "conditioned_image_index":ctx["image_index"],
                "branch_counts":{k:sum(1 for b in branches if b["classification"]==k)
                                 for k in sorted({b["classification"] for b in branches})},
                "unresolved_branch_count":len(unresolved),
                "unresolved_branches":unresolved,"branches":branches,
            })
    if immediate is not None:
        best={"pairing_index":immediate["pairing_index"],"block":immediate["block"],
              "projection_domain":[],"projection_domain_size":0,"unresolved_branch_count":0,
              "branches":[],"classification":"EMPTY_SECOND_INTEGER_PROJECTION_UNSAT"}
    else:
        req(evaluated,f"value{first_value} no independent candidates")
        evaluated.sort(key=lambda r:(r["unresolved_branch_count"],r["projection_domain_size"],r["pairing_index"]))
        best=evaluated[0]
    return {
        "pairing96_value":first_value,
        "exact_radius_squared":expected_radius,
        "exact_real_max_C2":expected_max,
        "candidate_universe":len(candidates),
        "candidate_limit":a28.CANDIDATE_LIMIT,
        "smallest_projection_candidates":candidates[:a28.CANDIDATE_LIMIT],
        "evaluated":evaluated,
        "best_conditioner":best,
        "closed_exactly":best["unresolved_branch_count"]==0,
    }

def main():
    req(AFF28.is_file() and blob(AFF28)==AFF28_BLOB,"AFFINE28 drift")
    a28=load(AFF28,"stage32ex5_eff_affine29_aff28")
    for path,expected,label in (
        (a28.ENGINE,a28.ENGINE_BLOB,"FP58 engine"),
        (a28.AFF15,a28.AFF15_BLOB,"AFFINE15"),
        (a28.AFF24,a28.AFF24_BLOB,"AFFINE24"),
        (a28.AFF27,a28.AFF27_BLOB,"AFFINE27"),
    ):
        req(path.is_file() and a28.blob(path)==expected,label+" drift")
    eng=a28.load(a28.ENGINE,"stage32ex5_eff_affine29_engine")
    aff15=a28.load(a28.AFF15,"stage32ex5_eff_affine29_aff15")
    aff24=a28.load(a28.AFF24,"stage32ex5_eff_affine29_aff24")

    F6,_A6,_I6,_RK58,_R58,_L,_d,_c,_u,P,gram=eng.build()
    Arow=sum((P.row(i) for i in range(92,104)),Matrix.zeros(1,64))
    ABrow=sum((P.row(i) for i in range(92,116)),Matrix.zeros(1,64))
    Crow=sum((P.row(i) for i in range(116,128)),Matrix.zeros(1,64))
    P100row=P.row(aff15.P100_INDEX)
    base_rows=[F6.row(i) for i in range(6)]+[Arow,ABrow,Crow,P100row]
    base10=[eng.D,eng.E,0,1,1,1,5,6,2,0]

    rows=[]
    for value in (1,0):
        radius,maxc2=EXPECTED[value]
        rows.append(analyze(value,radius,maxc2,a28,eng,aff15,aff24,base_rows,base10,P,gram))
    closed=all(r["closed_exactly"] for r in rows)
    out={
        "schema":"STAGE32EX5_EFF_AFFINE29_REMAINING_PAIR96_SECOND_CONDITIONING_V1",
        "status":"PASS_BOUNDED_EXACT_REMAINING_PAIR96_SECOND_CONDITIONING",
        "predecessor":{
            "affine28_pairing96_value2_closed_exactly":True,
            "direct_fp42_values_closed":[5,4,3],
            "remaining_values":[1,0],
        },
        "rows":rows,
        "remaining_values_0_1_closed_exactly":closed,
        "interpretation":{
            "what_is_proved":"For each remaining pairing[96] value, every classified second-conditioned branch uses exact HNF membership, exact completed-square emptiness, or exact real pairing separation. If closed_exactly=true for a value, that whole value branch is UNSAT.",
            "next_exact_unit":"If both values close, the exact-head AFFINE25-29 replay closes all six pairing[96] branches of the selected AFFINE23 43D fiber; then move to the next AFFINE22 residual 43D fiber rather than further subdividing this one. Otherwise continue only inside the smallest unresolved 41D branch.",
            "what_is_not_proved":"Other AFFINE22 residual fibers remain UNKNOWN. This script alone does not self-promote effectivity, MAIN, receiver, theorem, endpoint, or merge credit."
        },
        "credit":{"effectivity":False,"main":False,"receiver":False,"theorem":False,"endpoint":False,"merge":False},
    }
    print("EFF_AFFINE29_REMAINING_PAIR96="+json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
