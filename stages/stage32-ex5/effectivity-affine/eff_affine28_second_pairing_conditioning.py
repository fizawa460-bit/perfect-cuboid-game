#!/usr/bin/env python3
"""Exact second-pairing conditioning on the AFFINE24 pairing[96]=2 branch.

AFFINE25/26/27 closed pairing[96] values 5,4,3 by bounded exact FP42, but node
growth reached 27,467 at value 3. Do not continue direct FP42 scaleout to value
2. Instead condition the value-2 branch by one additional exact pairing
observable and classify its value branches by saturated HNF membership,
completed-square emptiness, and exact real pairing separation.

This is a structural probe only. Unresolved 41D branches remain UNKNOWN and no
downstream credit is promoted.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from flint import fmpz_mat
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
ENGINE=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB="e7857e9213ca9107edada1424012a7a1c902a625"
AFF15=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine15_forced_zero_collapse.py"
AFF15_BLOB="40255b3c62753f3df837c006b9481f3a8c02c717"
AFF24=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine24_single_pairing_conditioning.py"
AFF24_BLOB="1a48ef328a0d1ded2b663caa9865cedcbe24ea7f"
AFF27=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine27_fp42_growth_probe.py"
AFF27_BLOB="921b2d5f87dc09f86ce1fefef8e6512cea3c292f"

FIRST_PAIR=96
FIRST_VALUE=2
FIRST_RADIUS="769/24"
FIRST_MAX_C2="289/24"
CANDIDATE_LIMIT=16

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

def build_double_context(second_pair,base_rows,P,gram,aff15):
    rows=list(base_rows)
    forced=[]
    for bit,(_name,indices) in enumerate(aff15.GROUPS):
        if not (8 & (1<<bit)): continue
        for idx in indices:
            rows.append(P.row(idx)); forced.append(idx)
    rows.append(P.row(FIRST_PAIR))
    rows.append(P.row(second_pair))
    full=Matrix.vstack(*rows)
    pivots=list(full.T.rref()[1])
    F=full[pivots,:]
    rank=F.rows
    if rank!=23: return None
    req(F.rank()==23,"double-conditioned rank")
    hf,tf=fmpz_mat([[int(F[i,j]) for j in range(64)] for i in range(rank)]).transpose().hnf(transform=True)
    H=Matrix([[int(hf[i,j]) for j in range(hf.ncols())] for i in range(hf.nrows())])
    T=Matrix([[int(tf[i,j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    req(abs(int(tf.det()))==1 and H==T*F.T,"double-conditioned HNF replay")
    A=T.T[:,:rank]
    K=T.T[:,rank:]
    I=F*A
    req(K.shape==(64,41),"double-conditioned kernel shape")
    req(F*K==Matrix.zeros(rank,41),"double-conditioned kernel equality")
    R=-(K.T*gram*K)
    solve_r=aff15.ldl_solver(R)
    V=P*K
    W=solve_r(V.T)
    G=V*W
    req(G==G.T,"double-conditioned dual Gram symmetry")
    return {
        "second_pair":second_pair,"forced_indices":forced,"pivots":pivots,
        "rank":rank,"kernel_dimension":41,"image_index":abs(int(I.det())),
        "A":A,"K":K,"invI":I.inv(),"solve_r":solve_r,
        "dual_diag":[G[i,i] for i in range(140)]
    }

def target_for(ctx,base10,second_value):
    all_targets=list(base10)+[0]*len(ctx["forced_indices"])+[FIRST_VALUE,second_value]
    return Matrix([all_targets[i] for i in ctx["pivots"]])

def classify(ctx,base10,second_value,P,gram,eng):
    t=target_for(ctx,base10,second_value)
    icoord=ctx["invI"]*t
    if not all(getattr(v,"q",1)==1 for v in icoord):
        return {"value":second_value,"classification":"HNF_IMAGE_UNSAT"}
    bp=ctx["A"]*icoord
    req(all(getattr(v,"q",1)==1 for v in bp),"double-conditioned integral base point")
    K=ctx["K"]
    cross=K.T*gram*bp
    center=ctx["solve_r"](cross)
    q0=(bp.T*gram*bp)[0]
    radius=q0-eng.LOW+(cross.T*center)[0]
    if radius<0:
        return {"value":second_value,"classification":"EMPTY_ELLIPSOID_UNSAT",
                "exact_radius_squared":str(radius)}
    fixed=P*(bp+K*center)
    pair_upper=[eng.NORMAL_MASS]*92+[eng.E]*48
    for k in range(140):
        c=fixed[k]; upper=pair_upper[k]; q=ctx["dual_diag"][k]
        if c<0 and c*c>radius*q:
            return {"value":second_value,"classification":"REAL_PAIRING_SEPARATION_UNSAT",
                    "separator_index":k,"separator_side":"LOW","exact_radius_squared":str(radius)}
        if c>upper and (c-upper)*(c-upper)>radius*q:
            return {"value":second_value,"classification":"REAL_PAIRING_SEPARATION_UNSAT",
                    "separator_index":k,"separator_side":"HIGH","exact_radius_squared":str(radius)}
    return {"value":second_value,"classification":"UNRESOLVED_AFTER_SECOND_PAIRING_CONDITIONING",
            "kernel_dimension":41,"exact_radius_squared":str(radius),
            "exact_real_max_C2":str(eng.LOW+radius)}

def main():
    for path,expected,label in (
        (ENGINE,ENGINE_BLOB,"FP58 engine"),(AFF15,AFF15_BLOB,"AFFINE15"),
        (AFF24,AFF24_BLOB,"AFFINE24"),(AFF27,AFF27_BLOB,"AFFINE27"),
    ):
        req(path.is_file() and blob(path)==expected,label+" drift")
    eng=load(ENGINE,"stage32ex5_eff_affine28_engine")
    aff15=load(AFF15,"stage32ex5_eff_affine28_aff15")
    aff24=load(AFF24,"stage32ex5_eff_affine28_aff24")

    F6,_A6,_I6,_RK58,_R58,_L,_d,_c,_u,P,gram=eng.build()
    Arow=sum((P.row(i) for i in range(92,104)),Matrix.zeros(1,64))
    ABrow=sum((P.row(i) for i in range(92,116)),Matrix.zeros(1,64))
    Crow=sum((P.row(i) for i in range(116,128)),Matrix.zeros(1,64))
    P100row=P.row(aff15.P100_INDEX)
    base_rows=[F6.row(i) for i in range(6)]+[Arow,ABrow,Crow,P100row]
    base10=[eng.D,eng.E,*aff24.TARGET_BASE4,aff24.TARGET_A,aff24.TARGET_AB,aff24.TARGET_C,aff24.TARGET_P100]

    first=aff24.build_conditioned_context(FIRST_PAIR,base_rows,P,gram,aff15)
    req(first is not None and first["kernel_dimension"]==42,"first conditioned context drift")
    cheap=aff24.branch_classification(first,base10,FIRST_VALUE,P,gram,eng)
    req(cheap["classification"]=="UNRESOLVED_AFTER_ONE_PAIRING_CONDITIONING","value2 predecessor classification drift")
    req(cheap["exact_radius_squared"]==FIRST_RADIUS,"value2 predecessor radius drift")
    req(cheap["exact_real_max_C2"]==FIRST_MAX_C2,"value2 predecessor max-C2 drift")

    t=aff24.selected_target(first,base10,FIRST_VALUE)
    icoord=first["invI"]*t
    req(all(getattr(v,"q",1)==1 for v in icoord),"value2 predecessor HNF drift")
    bp=first["A"]*icoord
    R=-(first["K"].T*gram*first["K"])
    pair_upper=[eng.NORMAL_MASS]*92+[eng.E]*48
    fixed=set(first["forced_indices"])|{FIRST_PAIR}

    candidates=[]
    for idx in range(140):
        if idx in fixed: continue
        coeff=P.row(idx)*first["K"]
        if all(v==0 for v in coeff): continue
        domain=aff15.allowed_projection(P.row(idx),bp,first["K"],R,first["solve_r"],gram,eng.LOW,pair_upper[idx])
        candidates.append({"pairing_index":idx,"block":"normal" if idx<92 else "exceptional",
                           "domain":domain,"domain_size":len(domain)})
    req(candidates,"no second-conditioning candidates")
    candidates.sort(key=lambda r:(r["domain_size"],0 if r["block"]=="exceptional" else 1,r["pairing_index"]))

    immediate=next((r for r in candidates if r["domain_size"]==0),None)
    evaluated=[]
    if immediate is None:
        for cand in candidates[:CANDIDATE_LIMIT]:
            ctx=build_double_context(cand["pairing_index"],base_rows,P,gram,aff15)
            if ctx is None: continue
            branches=[classify(ctx,base10,v,P,gram,eng) for v in cand["domain"]]
            unresolved=[b for b in branches if b["classification"]=="UNRESOLVED_AFTER_SECOND_PAIRING_CONDITIONING"]
            evaluated.append({
                "pairing_index":cand["pairing_index"],"block":cand["block"],
                "projection_domain":cand["domain"],"projection_domain_size":cand["domain_size"],
                "conditioned_image_index":ctx["image_index"],
                "branch_counts":{key:sum(1 for b in branches if b["classification"]==key)
                                 for key in sorted({b["classification"] for b in branches})},
                "unresolved_branch_count":len(unresolved),
                "unresolved_branches":unresolved,"branches":branches
            })

    if immediate is not None:
        best={"pairing_index":immediate["pairing_index"],"block":immediate["block"],
              "projection_domain":[],"projection_domain_size":0,
              "unresolved_branch_count":0,"branches":[],
              "classification":"PAIRING96_VALUE2_UNSAT_EMPTY_SECOND_PROJECTION"}
    else:
        req(evaluated,"no independent second-conditioning candidates")
        evaluated.sort(key=lambda r:(r["unresolved_branch_count"],r["projection_domain_size"],r["pairing_index"]))
        best=evaluated[0]

    unresolved_all=[]
    for row in evaluated:
        for b in row["unresolved_branches"]:
            unresolved_all.append({
                "pairing_index":row["pairing_index"],"value":b["value"],
                "exact_radius_squared":b["exact_radius_squared"],
                "exact_real_max_C2":b["exact_real_max_C2"],"kernel_dimension":41
            })
    def radius_key(r):
        from fractions import Fraction
        return Fraction(r["exact_radius_squared"])
    unresolved_all.sort(key=lambda r:(radius_key(r),r["pairing_index"],r["value"]))

    out={
      "schema":"STAGE32EX5_EFF_AFFINE28_SECOND_PAIRING_CONDITIONING_V1",
      "status":"PASS_BOUNDED_EXACT_SECOND_PAIRING_CONDITIONING_PROBE",
      "predecessor":{
        "pairing_index":FIRST_PAIR,"pairing_value":FIRST_VALUE,
        "kernel_dimension":42,"exact_radius_squared":FIRST_RADIUS,
        "exact_real_max_C2":FIRST_MAX_C2,
        "direct_fp42_skipped":True,
        "reason":"AFFINE25/26/27 node growth 146 -> 5184 -> 27467"
      },
      "selection":{
        "candidate_universe":len(candidates),"candidate_limit":CANDIDATE_LIMIT,
        "ordering":"projection_domain_size,exceptional_first,pairing_index",
        "smallest_projection_candidates":candidates[:CANDIDATE_LIMIT]
      },
      "evaluated":evaluated,"best_conditioner":best,
      "pairing96_value2_closed_exactly":best["unresolved_branch_count"]==0,
      "smallest_unresolved_41d":unresolved_all[0] if unresolved_all else None,
      "interpretation":{
        "what_is_proved":"Every classified second-conditioned branch uses only exact saturated HNF membership, completed-square emptiness, or exact real pairing separation.",
        "next_exact_unit":"If value2 closes, move structurally to value1 without direct FP42. Otherwise benchmark only the smallest unresolved 41D branch or add a third exact separator if its projected domain is still broad.",
        "what_is_not_proved":"Unresolved 41D branches, pairing[96] values 0..1, and all other AFFINE22 residual fibers remain UNKNOWN. No effectivity, MAIN, receiver, theorem, endpoint, or merge credit is self-promoted."
      },
      "credit":{"effectivity":False,"main":False,"receiver":False,"theorem":False,"endpoint":False,"merge":False}
    }
    print("EFF_AFFINE28_SECOND_PAIRING="+json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
