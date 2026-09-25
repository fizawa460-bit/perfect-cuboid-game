#!/usr/bin/env python3
"""Iterative exact singleton-forcing closure on the two AFFINE29 residual parents.

AFFINE29 proves several pairing coordinates are individually forced to zero:
for pairing[96]=1, indices 92,95,97,98; for pairing[96]=0, indices 93,94.
Those implications are simultaneous, so condition them all at once, rebuild the
saturated affine lattice, then search a bounded panel for additional coordinates
whose entire exact projection domain is UNSAT except for one surviving value.

Each forcing step is justified only by exact HNF image failure, negative-radius
emptiness, or exact real one-pairing separation. Multiple singleton implications
proved on the same parent are batched simultaneously. No downstream credit is
promoted here.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from flint import fmpz_mat
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
AFF29=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine29_remaining_pair96_second_conditioning.py"
AFF29_BLOB="232e7dae572b82dcc7c8a5ce51da3f7143bed644"
PANEL_LIMIT=16
MAX_ROUNDS=6
EXPECTED={1:("835/24","355/24"),0:("841/24","361/24")}

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

def build_context(base_rows,base10,P,gram,aff15,fixed):
    rows=list(base_rows); vals=list(base10)
    forced_d=list(range(128,140))
    for idx in forced_d:
        rows.append(P.row(idx)); vals.append(0)
    for idx in sorted(fixed):
        rows.append(P.row(idx)); vals.append(int(fixed[idx]))
    full=Matrix.vstack(*rows)
    y=Matrix(vals)
    pivots=list(full.T.rref()[1])
    F=full[pivots,:]
    target=Matrix([vals[i] for i in pivots])
    rank=F.rows
    hf,tf=fmpz_mat([[int(F[i,j]) for j in range(64)] for i in range(rank)]).transpose().hnf(transform=True)
    H=Matrix([[int(hf[i,j]) for j in range(hf.ncols())] for i in range(hf.nrows())])
    T=Matrix([[int(tf[i,j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    req(abs(int(tf.det()))==1 and H==T*F.T,"closure HNF replay")
    A=T.T[:,:rank]; K=T.T[:,rank:]; I=F*A
    icoord=I.inv()*target
    if not all(getattr(v,"q",1)==1 for v in icoord):
        return {"classification":"HNF_IMAGE_UNSAT","rank":rank,"kernel_dimension":64-rank}
    bp=A*icoord
    if full*bp!=y:
        return {"classification":"DEPENDENT_TARGET_UNSAT","rank":rank,"kernel_dimension":64-rank}
    req(full*K==Matrix.zeros(full.rows,64-rank),"closure full kernel")
    R=-(K.T*gram*K)
    solve_r=aff15.ldl_solver(R)
    cross=K.T*gram*bp
    center=solve_r(cross)
    q0=(bp.T*gram*bp)[0]
    radius=q0+20+(cross.T*center)[0]
    if radius<0:
        return {"classification":"EMPTY_ELLIPSOID_UNSAT","rank":rank,
                "kernel_dimension":64-rank,"exact_radius_squared":str(radius)}
    fixed_real=P*(bp+K*center)
    V=P*K; W=solve_r(V.T); G=V*W
    req(G==G.T,"closure dual Gram symmetry")
    dual=[G[i,i] for i in range(140)]
    upper=[342-40]*92+[8]*48  # NORMAL_MASS=302, E=8 for d=18,e=8
    # keep constants asserted against engine caller later
    return {
      "classification":"UNRESOLVED","rank":rank,"kernel_dimension":64-rank,
      "A":A,"K":K,"I":I,"bp":bp,"R":R,"solve_r":solve_r,
      "radius":radius,"fixed_real":fixed_real,"dual_diag":dual,
      "exact_radius_squared":str(radius),"exact_real_max_C2":str(-20+radius),
      "forced_d":forced_d
    }

def direct_classification(ctx,eng):
    if ctx["classification"]!="UNRESOLVED":
        return ctx
    fixed=ctx["fixed_real"]; radius=ctx["radius"]
    upper=[eng.NORMAL_MASS]*92+[eng.E]*48
    for k in range(140):
        c=fixed[k]; q=ctx["dual_diag"][k]
        if c<0 and c*c>radius*q:
            return {"classification":"REAL_PAIRING_SEPARATION_UNSAT",
                    "separator_index":k,"separator_side":"LOW",
                    "rank":ctx["rank"],"kernel_dimension":ctx["kernel_dimension"],
                    "exact_radius_squared":str(radius)}
        if c>upper[k] and (c-upper[k])*(c-upper[k])>radius*q:
            return {"classification":"REAL_PAIRING_SEPARATION_UNSAT",
                    "separator_index":k,"separator_side":"HIGH",
                    "rank":ctx["rank"],"kernel_dimension":ctx["kernel_dimension"],
                    "exact_radius_squared":str(radius)}
    return ctx

def child_class(base_rows,base10,P,gram,aff15,eng,fixed,pair_idx,value):
    f=dict(fixed); f[pair_idx]=value
    return direct_classification(build_context(base_rows,base10,P,gram,aff15,f),eng)

def analyze_parent(first_value,a29,a28,eng,aff15,aff24,base_rows,base10,P,gram):
    radius,maxc2=EXPECTED[first_value]
    seed=a29.analyze(first_value,radius,maxc2,a28,eng,aff15,aff24,base_rows,base10,P,gram)
    seed_forced=[]
    for e in seed["evaluated"]:
        u=e["unresolved_branches"]
        if len(u)==1 and u[0]["value"]==0:
            req(all(b["classification"]!="UNRESOLVED_AFTER_SECOND_PAIRING_CONDITIONING"
                    for b in e["branches"] if b["value"]!=0),"seed nonzero unresolved")
            seed_forced.append(e["pairing_index"])
    req(seed_forced,"no AFFINE29 singleton seed")
    fixed={96:first_value}
    for idx in seed_forced: fixed[idx]=0

    rounds=[]
    closed=False; final=None
    for round_id in range(MAX_ROUNDS+1):
        ctx=direct_classification(build_context(base_rows,base10,P,gram,aff15,fixed),eng)
        if ctx["classification"]!="UNRESOLVED":
            closed=True; final=ctx
            rounds.append({"round":round_id,"fixed":dict(sorted(fixed.items())),
                           "parent":{k:v for k,v in ctx.items() if k not in {"A","K","I","bp","R","solve_r","fixed_real","dual_diag"}}})
            break

        excluded=set(ctx["forced_d"])|set(fixed)
        candidates=[]
        for pair_idx in range(140):
            if pair_idx in excluded: continue
            coeff=P.row(pair_idx)*ctx["K"]
            if all(v==0 for v in coeff): continue
            upper=eng.NORMAL_MASS if pair_idx<92 else eng.E
            domain=aff15.allowed_projection(P.row(pair_idx),ctx["bp"],ctx["K"],ctx["R"],
                                            ctx["solve_r"],gram,eng.LOW,upper)
            candidates.append({"pairing_index":pair_idx,
                               "block":"normal" if pair_idx<92 else "exceptional",
                               "domain":domain,"domain_size":len(domain)})
        candidates.sort(key=lambda r:(r["domain_size"],0 if r["block"]=="exceptional" else 1,r["pairing_index"]))
        req(candidates,"closure no candidates")

        evaluated=[]; forced_now={}; parent_unsat=None
        for cand in candidates[:PANEL_LIMIT]:
            branches=[]
            for value in cand["domain"]:
                cc=child_class(base_rows,base10,P,gram,aff15,eng,fixed,cand["pairing_index"],value)
                branches.append({"value":value,"classification":cc["classification"],
                                 "rank":cc.get("rank"),"kernel_dimension":cc.get("kernel_dimension"),
                                 "exact_radius_squared":cc.get("exact_radius_squared"),
                                 "separator_index":cc.get("separator_index"),
                                 "separator_side":cc.get("separator_side")})
            unresolved=[b for b in branches if b["classification"]=="UNRESOLVED"]
            evaluated.append({"pairing_index":cand["pairing_index"],"block":cand["block"],
                              "projection_domain":cand["domain"],"projection_domain_size":cand["domain_size"],
                              "unresolved_count":len(unresolved),"unresolved":unresolved,"branches":branches})
            if len(unresolved)==0:
                parent_unsat={"classification":"DOMAIN_EXHAUSTED_UNSAT",
                              "pairing_index":cand["pairing_index"],"projection_domain":cand["domain"],
                              "rank":ctx["rank"],"kernel_dimension":ctx["kernel_dimension"],
                              "exact_radius_squared":ctx["exact_radius_squared"]}
                break
            if len(unresolved)==1:
                forced_now[cand["pairing_index"]]=unresolved[0]["value"]

        rounds.append({
          "round":round_id,"fixed":dict(sorted(fixed.items())),
          "parent":{"rank":ctx["rank"],"kernel_dimension":ctx["kernel_dimension"],
                    "exact_radius_squared":ctx["exact_radius_squared"],
                    "exact_real_max_C2":ctx["exact_real_max_C2"]},
          "candidate_universe":len(candidates),"candidate_limit":PANEL_LIMIT,
          "evaluated":evaluated,"singleton_forced":dict(sorted(forced_now.items()))
        })
        if parent_unsat is not None:
            closed=True; final=parent_unsat; break
        new={k:v for k,v in forced_now.items() if k not in fixed}
        if not new:
            final={"classification":"STABLE_UNRESOLVED",
                   "rank":ctx["rank"],"kernel_dimension":ctx["kernel_dimension"],
                   "exact_radius_squared":ctx["exact_radius_squared"],
                   "exact_real_max_C2":ctx["exact_real_max_C2"]}
            break
        fixed.update(new)

    return {
      "pairing96_value":first_value,
      "seed_zero_forced":sorted(seed_forced),
      "rounds":rounds,
      "final_fixed":dict(sorted(fixed.items())),
      "closed_exactly":closed,
      "final":final
    }

def main():
    req(AFF29.is_file() and blob(AFF29)==AFF29_BLOB,"AFFINE29 drift")
    a29=load(AFF29,"stage32ex5_eff_affine31_aff29")
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
    req((eng.D,eng.E,eng.LOW,eng.NORMAL_MASS)==(18,8,-20,302),"engine constants drift")
    aff15=a28.load(a28.AFF15,"stage32ex5_eff_affine31_aff15")
    aff24=a28.load(a28.AFF24,"stage32ex5_eff_affine31_aff24")

    F6,_A6,_I6,_RK58,_R58,_L,_d,_c,_u,P,gram=eng.build()
    Arow=sum((P.row(i) for i in range(92,104)),Matrix.zeros(1,64))
    ABrow=sum((P.row(i) for i in range(92,116)),Matrix.zeros(1,64))
    Crow=sum((P.row(i) for i in range(116,128)),Matrix.zeros(1,64))
    P100row=P.row(aff15.P100_INDEX)
    base_rows=[F6.row(i) for i in range(6)]+[Arow,ABrow,Crow,P100row]
    base10=[eng.D,eng.E,0,1,1,1,5,6,2,0]

    rows=[analyze_parent(v,a29,a28,eng,aff15,aff24,base_rows,base10,P,gram) for v in (1,0)]
    out={
      "schema":"STAGE32EX5_EFF_AFFINE31_SINGLETON_FORCED_CLOSURE_V1",
      "status":"PASS_BOUNDED_EXACT_SINGLETON_FORCED_CLOSURE",
      "predecessor":{"affine29_remaining_values_0_1_closed_exactly":False,
                     "affine30_third_conditioner_was_local_only":True},
      "rows":rows,
      "both_remaining_pair96_values_closed_exactly":all(r["closed_exactly"] for r in rows),
      "interpretation":{
        "what_is_proved":"Every singleton assignment is forced because all other exact projected values are eliminated by HNF image failure, negative-radius emptiness, or exact real pairing separation. Singleton implications proved on the same parent are combined simultaneously and replayed in one saturated affine lattice.",
        "next_exact_unit":"If both parents close, the selected AFFINE23 43D fiber is fully UNSAT. Otherwise continue only from the stable simultaneous-forcing residual, not from the older one-coordinate chain.",
        "what_is_not_proved":"Other AFFINE22 residual fibers remain UNKNOWN. No effectivity, MAIN, receiver, theorem, endpoint, or merge credit is self-promoted."
      },
      "credit":{"effectivity":False,"main":False,"receiver":False,"theorem":False,"endpoint":False,"merge":False}
    }
    print("EFF_AFFINE31_SINGLETON_CLOSURE="+json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
