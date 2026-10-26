#!/usr/bin/env python3
"""Third exact pairing conditioning for the two AFFINE29 residual 41D branches.

AFFINE29 reduces pairing[96]=1 and pairing[96]=0 to one unresolved 41D branch
apiece:
  (96=1, 92=0), radius^2=835/24
  (96=0, 93=0), radius^2=841/24
This leaf adds one more exact pairing observable to each residual, giving a
rank-24 / 40D affine lattice whenever independent. Branches are classified only
by exact saturated HNF image failure, negative completed-square radius, or exact
real one-pairing separation. Anything else remains UNKNOWN.

No downstream credit is promoted here.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from flint import fmpz_mat
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
AFF29=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine29_remaining_pair96_second_conditioning.py"
AFF29_BLOB="232e7dae572b82dcc7c8a5ce51da3f7143bed644"
CANDIDATE_LIMIT=16
RESIDUALS=(
    {"first_value":1,"second_pair":92,"second_value":0,
     "radius":"835/24","max_c2":"355/24"},
    {"first_value":0,"second_pair":93,"second_value":0,
     "radius":"841/24","max_c2":"361/24"},
)

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

def build_triple_context(first_value,second_pair,third_pair,base_rows,P,gram,aff15):
    rows=list(base_rows)
    forced=[]
    for bit,(_name,indices) in enumerate(aff15.GROUPS):
        if not (8 & (1<<bit)): continue
        for idx in indices:
            rows.append(P.row(idx)); forced.append(idx)
    rows.append(P.row(96))
    rows.append(P.row(second_pair))
    rows.append(P.row(third_pair))
    full=Matrix.vstack(*rows)
    pivots=list(full.T.rref()[1])
    F=full[pivots,:]
    rank=F.rows
    if rank!=24: return None
    req(F.rank()==24,"triple-conditioned rank")
    hf,tf=fmpz_mat([[int(F[i,j]) for j in range(64)] for i in range(rank)]).transpose().hnf(transform=True)
    H=Matrix([[int(hf[i,j]) for j in range(hf.ncols())] for i in range(hf.nrows())])
    T=Matrix([[int(tf[i,j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    req(abs(int(tf.det()))==1 and H==T*F.T,"triple-conditioned HNF replay")
    A=T.T[:,:rank]; K=T.T[:,rank:]; I=F*A
    req(K.shape==(64,40),"triple-conditioned kernel shape")
    req(F*K==Matrix.zeros(rank,40),"triple-conditioned kernel equality")
    R=-(K.T*gram*K); solve_r=aff15.ldl_solver(R)
    V=P*K; W=solve_r(V.T); G=V*W
    req(G==G.T,"triple-conditioned dual Gram symmetry")
    return {
      "first_value":first_value,"second_pair":second_pair,"third_pair":third_pair,
      "forced_indices":forced,"pivots":pivots,"rank":rank,"kernel_dimension":40,
      "image_index":abs(int(I.det())),"A":A,"K":K,"invI":I.inv(),
      "solve_r":solve_r,"dual_diag":[G[i,i] for i in range(140)]
    }

def target_for(ctx,base10,second_value,third_value):
    vals=list(base10)+[0]*len(ctx["forced_indices"])+[
        ctx["first_value"],second_value,third_value
    ]
    return Matrix([vals[i] for i in ctx["pivots"]])

def classify(ctx,base10,second_value,third_value,P,gram,eng):
    t=target_for(ctx,base10,second_value,third_value)
    icoord=ctx["invI"]*t
    if not all(getattr(v,"q",1)==1 for v in icoord):
        return {"value":third_value,"classification":"HNF_IMAGE_UNSAT"}
    bp=ctx["A"]*icoord
    req(all(getattr(v,"q",1)==1 for v in bp),"triple-conditioned integral base point")
    K=ctx["K"]; cross=K.T*gram*bp; center=ctx["solve_r"](cross)
    q0=(bp.T*gram*bp)[0]; radius=q0-eng.LOW+(cross.T*center)[0]
    if radius<0:
        return {"value":third_value,"classification":"EMPTY_ELLIPSOID_UNSAT",
                "exact_radius_squared":str(radius)}
    fixed=P*(bp+K*center)
    upper=[eng.NORMAL_MASS]*92+[eng.E]*48
    for k in range(140):
        c=fixed[k]; q=ctx["dual_diag"][k]
        if c<0 and c*c>radius*q:
            return {"value":third_value,"classification":"REAL_PAIRING_SEPARATION_UNSAT",
                    "separator_index":k,"separator_side":"LOW",
                    "exact_radius_squared":str(radius)}
        if c>upper[k] and (c-upper[k])*(c-upper[k])>radius*q:
            return {"value":third_value,"classification":"REAL_PAIRING_SEPARATION_UNSAT",
                    "separator_index":k,"separator_side":"HIGH",
                    "exact_radius_squared":str(radius)}
    return {"value":third_value,"classification":"UNRESOLVED_AFTER_THIRD_PAIRING_CONDITIONING",
            "kernel_dimension":40,"exact_radius_squared":str(radius),
            "exact_real_max_C2":str(eng.LOW+radius)}

def analyze(res,a28,eng,aff15,aff24,base_rows,base10,P,gram):
    first_value=res["first_value"]; second_pair=res["second_pair"]; second_value=res["second_value"]
    a28.FIRST_VALUE=first_value
    double=a28.build_double_context(second_pair,base_rows,P,gram,aff15)
    req(double is not None and double["kernel_dimension"]==41,"AFFINE29 residual context drift")
    cheap=a28.classify(double,base10,second_value,P,gram,eng)
    req(cheap["classification"]=="UNRESOLVED_AFTER_SECOND_PAIRING_CONDITIONING",
        "AFFINE29 residual classification drift")
    req(cheap["exact_radius_squared"]==res["radius"],"AFFINE29 residual radius drift")
    req(cheap["exact_real_max_C2"]==res["max_c2"],"AFFINE29 residual max-C2 drift")

    t=a28.target_for(double,base10,second_value)
    icoord=double["invI"]*t
    req(all(getattr(v,"q",1)==1 for v in icoord),"AFFINE29 residual HNF drift")
    bp=double["A"]*icoord
    R=-(double["K"].T*gram*double["K"])
    excluded=set(double["forced_indices"]+[96,second_pair])
    upper=[eng.NORMAL_MASS]*92+[eng.E]*48

    candidates=[]
    for pair_idx in range(140):
        if pair_idx in excluded: continue
        coeff=P.row(pair_idx)*double["K"]
        if all(v==0 for v in coeff): continue
        domain=aff15.allowed_projection(P.row(pair_idx),bp,double["K"],R,double["solve_r"],
                                        gram,eng.LOW,upper[pair_idx])
        candidates.append({"pairing_index":pair_idx,
                           "block":"normal" if pair_idx<92 else "exceptional",
                           "domain":domain,"domain_size":len(domain)})
    req(candidates,"no third conditioner candidates")
    candidates.sort(key=lambda r:(r["domain_size"],0 if r["block"]=="exceptional" else 1,r["pairing_index"]))

    immediate=next((r for r in candidates if r["domain_size"]==0),None)
    evaluated=[]
    if immediate is None:
        for cand in candidates[:CANDIDATE_LIMIT]:
            ctx=build_triple_context(first_value,second_pair,cand["pairing_index"],
                                     base_rows,P,gram,aff15)
            if ctx is None: continue
            branches=[classify(ctx,base10,second_value,v,P,gram,eng) for v in cand["domain"]]
            unresolved=[b for b in branches if b["classification"]=="UNRESOLVED_AFTER_THIRD_PAIRING_CONDITIONING"]
            evaluated.append({
              "pairing_index":cand["pairing_index"],"block":cand["block"],
              "projection_domain":cand["domain"],"projection_domain_size":cand["domain_size"],
              "conditioned_image_index":ctx["image_index"],
              "branch_counts":{k:sum(1 for b in branches if b["classification"]==k)
                               for k in sorted({b["classification"] for b in branches})},
              "unresolved_branch_count":len(unresolved),
              "unresolved_branches":unresolved,"branches":branches
            })
    if immediate is not None:
        best={"pairing_index":immediate["pairing_index"],"block":immediate["block"],
              "projection_domain":[],"projection_domain_size":0,"unresolved_branch_count":0,
              "branches":[],"classification":"EMPTY_THIRD_INTEGER_PROJECTION_UNSAT"}
    else:
        req(evaluated,"no independent triple-conditioned candidates")
        evaluated.sort(key=lambda r:(r["unresolved_branch_count"],r["projection_domain_size"],r["pairing_index"]))
        best=evaluated[0]
    return {
      "pairing96_value":first_value,"second_pair":second_pair,"second_value":second_value,
      "exact_radius_squared":res["radius"],"exact_real_max_C2":res["max_c2"],
      "candidate_universe":len(candidates),"candidate_limit":CANDIDATE_LIMIT,
      "smallest_projection_candidates":candidates[:CANDIDATE_LIMIT],
      "evaluated":evaluated,"best_conditioner":best,
      "closed_exactly":best["unresolved_branch_count"]==0
    }

def main():
    req(AFF29.is_file() and blob(AFF29)==AFF29_BLOB,"AFFINE29 drift")
    a29=load(AFF29,"stage32ex5_eff_affine30_aff29")
    req(a29.AFF28.is_file() and a29.blob(a29.AFF28)==a29.AFF28_BLOB,"AFFINE28 drift")
    a28=a29.load(a29.AFF28,"stage32ex5_eff_affine30_aff28")
    for path,expected,label in (
      (a28.ENGINE,a28.ENGINE_BLOB,"FP58 engine"),
      (a28.AFF15,a28.AFF15_BLOB,"AFFINE15"),
      (a28.AFF24,a28.AFF24_BLOB,"AFFINE24"),
      (a28.AFF27,a28.AFF27_BLOB,"AFFINE27"),
    ):
        req(path.is_file() and a28.blob(path)==expected,label+" drift")
    eng=a28.load(a28.ENGINE,"stage32ex5_eff_affine30_engine")
    aff15=a28.load(a28.AFF15,"stage32ex5_eff_affine30_aff15")
    aff24=a28.load(a28.AFF24,"stage32ex5_eff_affine30_aff24")

    F6,_A6,_I6,_RK58,_R58,_L,_d,_c,_u,P,gram=eng.build()
    Arow=sum((P.row(i) for i in range(92,104)),Matrix.zeros(1,64))
    ABrow=sum((P.row(i) for i in range(92,116)),Matrix.zeros(1,64))
    Crow=sum((P.row(i) for i in range(116,128)),Matrix.zeros(1,64))
    P100row=P.row(aff15.P100_INDEX)
    base_rows=[F6.row(i) for i in range(6)]+[Arow,ABrow,Crow,P100row]
    base10=[eng.D,eng.E,0,1,1,1,5,6,2,0]

    rows=[analyze(r,a28,eng,aff15,aff24,base_rows,base10,P,gram) for r in RESIDUALS]
    closed=all(r["closed_exactly"] for r in rows)
    unresolved=[]
    for r in rows:
        for e in r["evaluated"]:
            for b in e["unresolved_branches"]:
                unresolved.append({
                  "pairing96_value":r["pairing96_value"],"second_pair":r["second_pair"],
                  "second_value":r["second_value"],"third_pair":e["pairing_index"],
                  "third_value":b["value"],"kernel_dimension":b["kernel_dimension"],
                  "exact_radius_squared":b["exact_radius_squared"],
                  "exact_real_max_C2":b["exact_real_max_C2"]
                })
    out={
      "schema":"STAGE32EX5_EFF_AFFINE30_THIRD_PAIRING_CONDITIONING_V1",
      "status":"PASS_BOUNDED_EXACT_THIRD_PAIRING_CONDITIONING_PROBE",
      "predecessor":{"affine29_remaining_values_0_1_closed_exactly":False,
                     "residual_41d_count":2},
      "rows":rows,"both_affine29_residuals_closed_exactly":closed,
      "unresolved_40d_branches":unresolved,
      "interpretation":{
        "what_is_proved":"Every classified third-conditioned branch uses exact HNF membership, exact completed-square emptiness, or exact real pairing separation. If a row has closed_exactly=true, that entire AFFINE29 residual 41D branch is UNSAT.",
        "next_exact_unit":"If both rows close, the selected AFFINE23 43D fiber is fully UNSAT under AFFINE25-30. Otherwise continue only inside the smallest unresolved 40D branch; do not return to broad FP42 scaleout.",
        "what_is_not_proved":"Other AFFINE22 residual fibers remain UNKNOWN. No effectivity, MAIN, receiver, theorem, endpoint, or merge credit is self-promoted."
      },
      "credit":{"effectivity":False,"main":False,"receiver":False,"theorem":False,"endpoint":False,"merge":False}
    }
    print("EFF_AFFINE30_THIRD_PAIRING="+json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
