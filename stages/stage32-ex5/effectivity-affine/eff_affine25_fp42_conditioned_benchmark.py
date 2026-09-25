#!/usr/bin/env python3
"""Bounded exact FP42 benchmark for AFFINE24 pairing[96]=5.

This runs one exact LLL/LDL Fincke--Pohst benchmark on the smallest unresolved
AFFINE24 conditioned branch only. A node cap leaves it UNKNOWN. No horizontal
scaleout or downstream credit is performed here.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys, time
from pathlib import Path
from flint import fmpq, fmpz_mat
from sympy import Matrix, Rational

ROOT=Path(__file__).resolve().parents[3]
ENGINE=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB="e7857e9213ca9107edada1424012a7a1c902a625"
AFF15=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine15_forced_zero_collapse.py"
AFF15_BLOB="40255b3c62753f3df837c006b9481f3a8c02c717"
AFF17=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine17_empty_ellipsoid_sweep.py"
AFF17_BLOB="2f173365fe48d91630b1d88d454951469537c42b"
AFF19=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine19_fp43_wave.py"
AFF19_BLOB="d9e977f88072fa39f528a954c980de7ada84c9f5"
AFF24=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine24_single_pairing_conditioning.py"
AFF24_BLOB="1a48ef328a0d1ded2b663caa9865cedcbe24ea7f"

TARGET_BASE4=(0,1,1,1)
TARGET_A,TARGET_AB,TARGET_C,TARGET_P100=5,6,2,0
TARGET_MASK=8
TARGET_PAIRING_INDEX=96
TARGET_PAIRING_VALUE=5
TARGET_RADIUS="211/24"
DIM=42
NODE_CAP=50000

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
def csha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def fq(x):
    x=Rational(x); return fmpq(int(x.p),int(x.q))

def build_lll42(ctx,P,gram):
    K=ctx["K"]
    req(ctx["kernel_dimension"]==DIM and K.shape==(64,DIM),"FP42 context dimension")
    Q=-(K.T*gram*K)
    qf,lf=fmpz_mat([[int(Q[i,j]) for j in range(DIM)] for i in range(DIM)]).lll(transform=True,rep="gram",gram="exact")
    U=Matrix([[int(lf[i,j]) for j in range(DIM)] for i in range(DIM)])
    R=Matrix([[int(qf[i,j]) for j in range(DIM)] for i in range(DIM)])
    RK=K*U.T
    req(abs(int(lf.det()))==1,"FP42 LLL transform")
    req(R==-(RK.T*gram*RK),"FP42 LLL replay")
    Ls,Ds=R.LDLdecomposition(hermitian=False)
    req(R==Ls*Ds*Ls.T,"FP42 LDL replay")
    diag=[fq(Ds[i,i]) for i in range(DIM)]
    req(all(x>0 for x in diag),"FP42 positive definite")
    L=[[fq(Ls[i,j]) for j in range(DIM)] for i in range(DIM)]
    IR=P*RK
    coeff=[]
    for k in range(140):
        src=[fmpq(int(IR[k,j])) for j in range(DIM)]; row=[]
        for j in range(DIM):
            z=src[j]
            for i in range(j): z-=row[i]*L[j][i]
            row.append(z)
        coeff.append(row)
    dual=[]
    for row in coeff:
        total=fmpq(0); prefix=[]
        for i in range(DIM):
            total+=row[i]*row[i]/diag[i]; prefix.append(total)
        dual.append(prefix)
    return {"RK":RK,"R":R,"L":L,"diag":diag,"coeff":coeff,"dual":dual}

def solve42(ctx,lc,base10,P,gram,eng,aff24):
    target=aff24.selected_target(ctx,base10,TARGET_PAIRING_VALUE)
    icoord=ctx["invI"]*target
    req(all(getattr(v,"q",1)==1 for v in icoord),"FP42 target HNF drift")
    bp=ctx["A"]*icoord
    req(all(getattr(v,"q",1)==1 for v in bp),"FP42 integral base point")
    RK,R,L,diag,coeff,dual=(lc[k] for k in ("RK","R","L","diag","coeff","dual"))
    q0=(bp.T*gram*bp)[0]
    cross=RK.T*gram*bp
    Rinv=R.inv()
    center_s=Rinv*cross
    center=[fq(x) for x in center_s]
    radius_s=q0-eng.LOW+(cross.T*Rinv*cross)[0]
    req(str(radius_s)==TARGET_RADIUS,f"FP42 radius drift: {radius_s}")
    radius=fq(radius_s)
    max_real_c2=Rational(eng.LOW)+radius_s
    fixed=[fq(x) for x in P*(bp+RK*center_s)]
    for idx in ctx["forced_indices"]:
        req(all(coeff[idx][j]==0 for j in range(DIM)),f"forced row {idx} kernel drift")
        req(fixed[idx]==0,f"forced row {idx} affine drift")
    req(all(coeff[TARGET_PAIRING_INDEX][j]==0 for j in range(DIM)),"conditioned pairing kernel drift")
    req(fixed[TARGET_PAIRING_INDEX]==TARGET_PAIRING_VALUE,"conditioned pairing affine drift")
    pair_upper=[eng.NORMAL_MASS]*92+[eng.E]*48
    coords=[0]*DIM
    nodes=prunes=leaves=lower_prunes=upper_prunes=0
    witness=None; capped=False; tr=hashlib.sha256()

    def ev(*parts):
        tr.update(("|".join(map(str,parts))+"\n").encode())
    def viable(next_i,rem):
        nonlocal prunes,lower_prunes,upper_prunes
        for k in range(140):
            v=fixed[k]; upper=fmpq(pair_upper[k])
            if 0<=v<=upper: continue
            dist=-v if v<0 else v-upper
            impossible=next_i<0 or dist*dist>rem*dual[k][next_i]
            if impossible:
                prunes+=1
                if v<0: lower_prunes+=1; side="LOW"
                else: upper_prunes+=1; side="HIGH"
                ev("P2",next_i,k,side,v,upper,rem)
                return False
        return True
    def rec(i,rem):
        nonlocal nodes,leaves,witness,capped
        if witness is not None or capped: return
        if nodes>=NODE_CAP: capped=True; return
        nodes+=1; ev("N",i,rem)
        alpha=-center[i]
        for j in range(i+1,DIM): alpha+=L[j][i]*(coords[j]-center[j])
        exact=-alpha; base=int(exact.p)//int(exact.q); step=0
        while True:
            vals=[base] if step==0 else [base-step,base+step]
            any_possible=False
            for val in vals:
                transformed=val+alpha; cost=diag[i]*transformed*transformed
                if cost>rem: continue
                any_possible=True; coords[i]=val
                for k in range(140): fixed[k]+=coeff[k][i]*transformed
                nr=rem-cost
                if viable(i-1,nr):
                    if i: rec(i-1,nr)
                    else:
                        leaves+=1
                        x=bp+RK*Matrix(coords); pair=P*x; c2=int((x.T*gram*x)[0])
                        req(min(pair)>=0 and c2>=eng.LOW,"FP42 leaf verification")
                        req(max(pair[:92,:])<=eng.NORMAL_MASS,"FP42 normal upper")
                        req(max(pair[92:,:])<=eng.E,"FP42 exceptional upper")
                        req(int(pair[TARGET_PAIRING_INDEX])==TARGET_PAIRING_VALUE,"FP42 pairing leaf drift")
                        if c2<=eng.HIGH:
                            witness={"C2":c2,"picard_coordinates":[int(v) for v in x],"pairings_sha256":csha([int(v) for v in pair])}
                for k in range(140): fixed[k]-=coeff[k][i]*transformed
                if witness is not None or capped: return
            if step>0 and not any_possible:
                left=fq(base-step)+alpha; right=fq(base+step)+alpha
                if diag[i]*left*left>rem and diag[i]*right*right>rem: break
            step+=1

    t0=time.perf_counter(); rec(DIM-1,radius); elapsed=time.perf_counter()-t0
    if witness is not None: classification="BAD_SHELL_SAT_WITNESS_EXACT_FP42"; complete=True
    elif capped: classification="UNKNOWN_BENCHMARK_NODE_CAP"; complete=False
    else: classification="BAD_SHELL_UNSAT_EXACT_FP42"; complete=True
    return {
        "base4":list(TARGET_BASE4),"A":TARGET_A,"AB":TARGET_AB,"B":TARGET_AB-TARGET_A,
        "C":TARGET_C,"D":eng.E-TARGET_AB-TARGET_C,"p100":TARGET_P100,
        "zero_pattern_mask":TARGET_MASK,"pairing_index":TARGET_PAIRING_INDEX,
        "pairing_value":TARGET_PAIRING_VALUE,"kernel_dimension":DIM,
        "exact_radius_squared":str(radius),"exact_real_max_C2":str(max_real_c2),
        "classification":classification,"complete":complete,"node_cap":NODE_CAP,
        "node_count":nodes,"intersection_prune_count":prunes,
        "lower_pairing_prune_count":lower_prunes,"upper_pairing_prune_count":upper_prunes,
        "feasible_leaf_count":leaves,"elapsed_seconds":elapsed,
        "transcript_sha256":tr.hexdigest(),"witness":witness,
    }

def main():
    for path,expected,label in (
        (ENGINE,ENGINE_BLOB,"FP58 engine"),(AFF15,AFF15_BLOB,"AFFINE15"),
        (AFF17,AFF17_BLOB,"AFFINE17"),(AFF19,AFF19_BLOB,"AFFINE19"),
        (AFF24,AFF24_BLOB,"AFFINE24"),
    ):
        req(path.is_file() and blob(path)==expected,label+" drift")
    eng=load(ENGINE,"stage32ex5_eff_affine25_engine")
    aff15=load(AFF15,"stage32ex5_eff_affine25_aff15")
    load(AFF17,"stage32ex5_eff_affine25_aff17")
    load(AFF19,"stage32ex5_eff_affine25_aff19")
    aff24=load(AFF24,"stage32ex5_eff_affine25_aff24")
    F6,_A6,_I6,_RK58,_R58,_L,_d,_c,_u,P,gram=eng.build()
    Arow=sum((P.row(i) for i in range(92,104)),Matrix.zeros(1,64))
    ABrow=sum((P.row(i) for i in range(92,116)),Matrix.zeros(1,64))
    Crow=sum((P.row(i) for i in range(116,128)),Matrix.zeros(1,64))
    P100row=P.row(aff15.P100_INDEX)
    base_rows=[F6.row(i) for i in range(6)]+[Arow,ABrow,Crow,P100row]
    base10=[eng.D,eng.E,*TARGET_BASE4,TARGET_A,TARGET_AB,TARGET_C,TARGET_P100]
    ctx=aff24.build_conditioned_context(TARGET_PAIRING_INDEX,base_rows,P,gram,aff15)
    req(ctx is not None,"AFFINE24 conditioned context missing")
    req(ctx["rank"]==22 and ctx["kernel_dimension"]==DIM,"AFFINE24 conditioned dimension drift")
    cheap=aff24.branch_classification(ctx,base10,TARGET_PAIRING_VALUE,P,gram,eng)
    req(cheap["classification"]=="UNRESOLVED_AFTER_ONE_PAIRING_CONDITIONING","AFFINE24 branch classification drift")
    req(cheap["exact_radius_squared"]==TARGET_RADIUS,"AFFINE24 branch radius drift")
    req(cheap["exact_real_max_C2"]=="-269/24","AFFINE24 branch max-C2 drift")
    result=solve42(ctx,build_lll42(ctx,P,gram),base10,P,gram,eng,aff24)
    out={
        "schema":"STAGE32EX5_EFF_AFFINE25_FP42_CONDITIONED_BENCHMARK_V1",
        "status":"PASS_BOUNDED_EXACT_FP42_CONDITIONED_BENCHMARK",
        "predecessor":{"affine24_status":"PASS_BOUNDED_EXACT_SINGLE_PAIRING_CONDITIONING_PROBE",
            "selected_fiber_closed_exactly":False,"pairing_index":TARGET_PAIRING_INDEX,
            "pairing_value":TARGET_PAIRING_VALUE,"kernel_dimension":DIM,
            "exact_radius_squared":TARGET_RADIUS,"exact_real_max_C2":"-269/24"},
        "selection":{"rule":"AFFINE24 bounded-panel smallest unresolved conditioned branch",
            "node_cap":NODE_CAP,"horizontal_scaleout":False},
        "result":result,
        "interpretation":{
            "what_is_proved":"If complete=true, this one saturated AFFINE24 pairing[96]=5 branch is resolved exactly by Fincke--Pohst. If complete=false, it remains UNKNOWN.",
            "next_exact_unit":"If this branch closes cheaply, use it only to choose the next smallest bounded conditioned branch or an exact structural separator. If it hits the node cap, do not scale out; add another exact conditioning/separation observable first.",
            "what_is_not_proved":"The other five pairing[96] branches and all other AFFINE22 residual fibers remain untouched. No effectivity, MAIN, receiver, theorem, endpoint, or merge credit is self-promoted."},
        "credit":{"effectivity":False,"main":False,"receiver":False,"theorem":False,"endpoint":False,"merge":False},
    }
    print("EFF_AFFINE25_FP42_CONDITIONED="+json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
