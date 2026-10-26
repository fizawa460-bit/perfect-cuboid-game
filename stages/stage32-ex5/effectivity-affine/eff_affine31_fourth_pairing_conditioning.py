#!/usr/bin/env python3
"""Fourth exact pairing conditioning on the three AFFINE30 residual 40D branches.

AFFINE30 leaves exactly three branches on its best third-conditioner routes:
  A: 96=1, 92=0, 97=0
  B: 96=0, 93=0, 92=0
  C: 96=0, 93=0, 92=1
all with radius^2=835/24.  Add one more independent pairing observable to each
branch, producing rank-25 / kernel-39 affine lattices.  Classify only by exact
saturated HNF image failure, negative completed-square radius, or exact real
one-pairing separation. Anything else remains UNKNOWN.

No downstream credit is promoted here.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from flint import fmpz_mat
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
AFF30=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine30_third_pairing_conditioning.py"
AFF30_BLOB="fe9c93db55e6f4ba8a402e89050e203ce2637946"
CANDIDATE_LIMIT=16
RESIDUALS=(
    {"label":"A","first_value":1,"second_pair":92,"second_value":0,
     "third_pair":97,"third_value":0,"radius":"835/24","max_c2":"355/24"},
    {"label":"B","first_value":0,"second_pair":93,"second_value":0,
     "third_pair":92,"third_value":0,"radius":"835/24","max_c2":"355/24"},
    {"label":"C","first_value":0,"second_pair":93,"second_value":0,
     "third_pair":92,"third_value":1,"radius":"835/24","max_c2":"355/24"},
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

def build_quad_context(res,fourth_pair,base_rows,P,gram,aff15):
    rows=list(base_rows)
    forced=[]
    for bit,(_name,indices) in enumerate(aff15.GROUPS):
        if not (8 & (1<<bit)): continue
        for idx in indices:
            rows.append(P.row(idx)); forced.append(idx)
    rows.append(P.row(96))
    rows.append(P.row(res["second_pair"]))
    rows.append(P.row(res["third_pair"]))
    rows.append(P.row(fourth_pair))
    full=Matrix.vstack(*rows)
    pivots=list(full.T.rref()[1])
    F=full[pivots,:]
    rank=F.rows
    if rank!=25: return None
    req(F.rank()==25,"quad-conditioned rank")
    hf,tf=fmpz_mat([[int(F[i,j]) for j in range(64)] for i in range(rank)]).transpose().hnf(transform=True)
    H=Matrix([[int(hf[i,j]) for j in range(hf.ncols())] for i in range(hf.nrows())])
    T=Matrix([[int(tf[i,j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    req(abs(int(tf.det()))==1 and H==T*F.T,"quad-conditioned HNF replay")
    A=T.T[:,:rank]; K=T.T[:,rank:]; I=F*A
    req(K.shape==(64,39),"quad-conditioned kernel shape")
    req(F*K==Matrix.zeros(rank,39),"quad-conditioned kernel equality")
    R=-(K.T*gram*K); solve_r=aff15.ldl_solver(R)
    V=P*K; W=solve_r(V.T); G=V*W
    req(G==G.T,"quad-conditioned dual Gram symmetry")
    return {
        "forced_indices":forced,"pivots":pivots,"rank":rank,"kernel_dimension":39,
        "image_index":abs(int(I.det())),"A":A,"K":K,"invI":I.inv(),
        "solve_r":solve_r,"dual_diag":[G[i,i] for i in range(140)]
    }

def target_for(ctx,base10,res,fourth_value):
    vals=list(base10)+[0]*len(ctx["forced_indices"])+[
        res["first_value"],res["second_value"],res["third_value"],fourth_value
    ]
    return Matrix([vals[i] for i in ctx["pivots"]])

def classify(ctx,base10,res,fourth_value,P,gram,eng):
    t=target_for(ctx,base10,res,fourth_value)
    icoord=ctx["invI"]*t
    if not all(getattr(v,"q",1)==1 for v in icoord):
        return {"value":fourth_value,"classification":"HNF_IMAGE_UNSAT"}
    bp=ctx["A"]*icoord
    req(all(getattr(v,"q",1)==1 for v in bp),"quad-conditioned integral base point")
    K=ctx["K"]; cross=K.T*gram*bp; center=ctx["solve_r"](cross)
    q0=(bp.T*gram*bp)[0]; radius=q0-eng.LOW+(cross.T*center)[0]
    if radius<0:
        return {"value":fourth_value,"classification":"EMPTY_ELLIPSOID_UNSAT",
                "exact_radius_squared":str(radius)}
    fixed=P*(bp+K*center)
    upper=[eng.NORMAL_MASS]*92+[eng.E]*48
    for k in range(140):
        c=fixed[k]; q=ctx["dual_diag"][k]
        if c<0 and c*c>radius*q:
            return {"value":fourth_value,"classification":"REAL_PAIRING_SEPARATION_UNSAT",
                    "separator_index":k,"separator_side":"LOW","exact_radius_squared":str(radius)}
        if c>upper[k] and (c-upper[k])*(c-upper[k])>radius*q:
            return {"value":fourth_value,"classification":"REAL_PAIRING_SEPARATION_UNSAT",
                    "separator_index":k,"separator_side":"HIGH","exact_radius_squared":str(radius)}
    return {"value":fourth_value,"classification":"UNRESOLVED_AFTER_FOURTH_PAIRING_CONDITIONING",
            "kernel_dimension":39,"exact_radius_squared":str(radius),
            "exact_real_max_C2":str(eng.LOW+radius)}

def analyze(res,a30,eng,aff15,base_rows,base10,P,gram):
    triple=a30.build_triple_context(res["first_value"],res["second_pair"],res["third_pair"],
                                    base_rows,P,gram,aff15)
    req(triple is not None and triple["kernel_dimension"]==40,res["label"]+" triple context")
    cheap=a30.classify(triple,base10,res["second_value"],res["third_value"],P,gram,eng)
    req(cheap["classification"]=="UNRESOLVED_AFTER_THIRD_PAIRING_CONDITIONING",
        res["label"]+" triple classification")
    req(cheap["exact_radius_squared"]==res["radius"],res["label"]+" radius")
    req(cheap["exact_real_max_C2"]==res["max_c2"],res["label"]+" maxC2")

    t=a30.target_for(triple,base10,res["second_value"],res["third_value"])
    icoord=triple["invI"]*t
    req(all(getattr(v,"q",1)==1 for v in icoord),res["label"]+" HNF")
    bp=triple["A"]*icoord
    R=-(triple["K"].T*gram*triple["K"])
    excluded=set(triple["forced_indices"]+[96,res["second_pair"],res["third_pair"]])
    upper=[eng.NORMAL_MASS]*92+[eng.E]*48
    candidates=[]
    for pair_idx in range(140):
        if pair_idx in excluded: continue
        coeff=P.row(pair_idx)*triple["K"]
        if all(v==0 for v in coeff): continue
        domain=aff15.allowed_projection(P.row(pair_idx),bp,triple["K"],R,triple["solve_r"],
                                        gram,eng.LOW,upper[pair_idx])
        candidates.append({"pairing_index":pair_idx,
                           "block":"normal" if pair_idx<92 else "exceptional",
                           "domain":domain,"domain_size":len(domain)})
    req(candidates,res["label"]+" no fourth candidates")
    candidates.sort(key=lambda r:(r["domain_size"],0 if r["block"]=="exceptional" else 1,r["pairing_index"]))
    immediate=next((r for r in candidates if r["domain_size"]==0),None)
    evaluated=[]
    if immediate is None:
        for cand in candidates[:CANDIDATE_LIMIT]:
            ctx=build_quad_context(res,cand["pairing_index"],base_rows,P,gram,aff15)
            if ctx is None: continue
            branches=[classify(ctx,base10,res,v,P,gram,eng) for v in cand["domain"]]
            unresolved=[b for b in branches if b["classification"]=="UNRESOLVED_AFTER_FOURTH_PAIRING_CONDITIONING"]
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
              "branches":[],"classification":"EMPTY_FOURTH_INTEGER_PROJECTION_UNSAT"}
    else:
        req(evaluated,res["label"]+" no independent fourth candidates")
        evaluated.sort(key=lambda r:(r["unresolved_branch_count"],r["projection_domain_size"],r["pairing_index"]))
        best=evaluated[0]
    return {
        "label":res["label"],"pairing96_value":res["first_value"],
        "second_pair":res["second_pair"],"second_value":res["second_value"],
        "third_pair":res["third_pair"],"third_value":res["third_value"],
        "exact_radius_squared":res["radius"],"exact_real_max_C2":res["max_c2"],
        "candidate_universe":len(candidates),"candidate_limit":CANDIDATE_LIMIT,
        "smallest_projection_candidates":candidates[:CANDIDATE_LIMIT],
        "evaluated":evaluated,"best_conditioner":best,
        "closed_exactly":best["unresolved_branch_count"]==0
    }

def main():
    req(AFF30.is_file() and blob(AFF30)==AFF30_BLOB,"AFFINE30 drift")
    a30=load(AFF30,"stage32ex5_eff_affine31_aff30")
    req(a30.AFF29.is_file() and a30.blob(a30.AFF29)==a30.AFF29_BLOB,"AFFINE29 drift")
    a29=a30.load(a30.AFF29,"stage32ex5_eff_affine31_aff29")
    req(a29.AFF28.is_file() and a29.blob(a29.AFF28)==a29.AFF28_BLOB,"AFFINE28 drift")
    a28=a29.load(a29.AFF28,"stage32ex5_eff_affine31_aff28")
    for path,expected,label in (
        (a28.ENGINE,a28.ENGINE_BLOB,"FP58 engine"),
        (a28.AFF15,a28.AFF15_BLOB,"AFFINE15"),
        (a28.AFF24,a28.AFF24_BLOB,"AFFINE24"),
        (a28.AFF27,a28.AFF27_BLOB,"AFFINE27"),
    ):
        req(path.is_file() and a28.blob(path)==expected,label+" drift")
    eng=a28.load(a28.ENGINE,"stage32ex5_eff_affine31_engine")
    aff15=a28.load(a28.AFF15,"stage32ex5_eff_affine31_aff15")

    F6,_A6,_I6,_RK58,_R58,_L,_d,_c,_u,P,gram=eng.build()
    Arow=sum((P.row(i) for i in range(92,104)),Matrix.zeros(1,64))
    ABrow=sum((P.row(i) for i in range(92,116)),Matrix.zeros(1,64))
    Crow=sum((P.row(i) for i in range(116,128)),Matrix.zeros(1,64))
    P100row=P.row(aff15.P100_INDEX)
    base_rows=[F6.row(i) for i in range(6)]+[Arow,ABrow,Crow,P100row]
    base10=[eng.D,eng.E,0,1,1,1,5,6,2,0]

    rows=[analyze(r,a30,eng,aff15,base_rows,base10,P,gram) for r in RESIDUALS]
    closed=all(r["closed_exactly"] for r in rows)
    unresolved=[]
    for r in rows:
        for e in r["evaluated"]:
            for b in e["unresolved_branches"]:
                unresolved.append({
                    "label":r["label"],"pairing96_value":r["pairing96_value"],
                    "second_pair":r["second_pair"],"second_value":r["second_value"],
                    "third_pair":r["third_pair"],"third_value":r["third_value"],
                    "fourth_pair":e["pairing_index"],"fourth_value":b["value"],
                    "kernel_dimension":b["kernel_dimension"],
                    "exact_radius_squared":b["exact_radius_squared"],
                    "exact_real_max_C2":b["exact_real_max_C2"]
                })
    out={
        "schema":"STAGE32EX5_EFF_AFFINE31_FOURTH_PAIRING_CONDITIONING_V1",
        "status":"PASS_BOUNDED_EXACT_FOURTH_PAIRING_CONDITIONING_PROBE",
        "predecessor":{"affine30_both_closed_exactly":False,"residual_40d_count":3},
        "rows":rows,"all_affine30_residuals_closed_exactly":closed,
        "unresolved_39d_branches":unresolved,
        "interpretation":{
            "what_is_proved":"Every classified fourth-conditioned branch uses exact HNF membership, exact completed-square emptiness, or exact real pairing separation. A row with closed_exactly=true is fully UNSAT.",
            "next_exact_unit":"If all three rows close, the selected AFFINE23 43D fiber is fully UNSAT under AFFINE25-31. Otherwise continue only on best-route unresolved 39D branches, preferably structurally before any bounded FP39 benchmark.",
            "what_is_not_proved":"Other AFFINE22 residual fibers remain UNKNOWN. No effectivity, MAIN, receiver, theorem, endpoint, or merge credit is self-promoted."
        },
        "credit":{"effectivity":False,"main":False,"receiver":False,"theorem":False,"endpoint":False,"merge":False}
    }
    print("EFF_AFFINE31_FOURTH_PAIRING="+json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
