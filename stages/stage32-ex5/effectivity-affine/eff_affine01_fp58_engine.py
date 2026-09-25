#!/usr/bin/env python3
"""Exact 58D Fincke--Pohst engine for EX5 EFF-AFFINE01.

This is an independent exact-arithmetic port of the historical Stage32 54D
FP140 recursion to the six fixed observables (d,e,a,b,c,t).  It grants no
effectivity or MAIN credit by itself.
"""
from __future__ import annotations

import argparse, hashlib, importlib.util, json, sys, time
from pathlib import Path
import flint
from flint import fmpq, fmpz_mat
from sympy import Matrix, Rational

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/"stages/stage32-ex5/breadth-cycle-2/bc2_02_one_indexed_full178_terminal_to_picard64_completion.py"
RELAXED=ROOT/"stages/stage32/management/btva-compressed-lift/run_btva_static7_bounded_panel.py"
PARENT=ROOT/"stages/stage32/management/btva-compressed-lift/run_btva_base4_normalmass_bounded_panel.py"
RETAINED=ROOT/"stages/stage33/33-07/picard_base_rows_retained.py"
MARKING=ROOT/"stages/stage33/33-07/stage32_picard_marking_retained.py"
LOCKS={BASE:"6b4c3514b5b4cbccd8e66cbffc7f61f8830d1633",RELAXED:"e44bec7ad9c0b7a4d8d7d87a455f181a681035c6",PARENT:"29114c0cd8a2c604d24b2a9ad3418fc2b5200171",RETAINED:"82e4d450a1d852e34f6615440fb88a029c6e54eb",MARKING:"5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"}
D,E,G=18,8,0
NORMAL_MASS=19*D-5*E
LOW=-D-2+2*G
HIGH=D-15
N=58

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p); req(s and s.loader,"module "+n)
    m=importlib.util.module_from_spec(s); sys.modules[n]=m; s.loader.exec_module(m); return m
def fq(x):
    x=Rational(x); return fmpq(int(x.p),int(x.q))
def csha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def build():
    for p,h in LOCKS.items(): req(p.is_file() and blob(p)==h,"source lock "+str(p))
    parent=load(PARENT,"ex5_fp58_parent"); old=load(RELAXED,"ex5_fp58_relaxed")
    req(old.BASE==BASE and blob(old.BASE)==LOCKS[BASE],"base lock")
    v1=load(BASE,"ex5_fp58_base")
    bundle=v1.load_retained(RETAINED,"ex5_fp58_bundle")
    marking=v1.load_retained(MARKING,"ex5_fp58_marking")
    data=v1.reconstruct_translation_data(marking,bundle)
    P=Matrix(data["adapter"].pairing_matrix); bridge=data["bridge"]; gram=Matrix(bundle["picard_gram_64x64"])
    rows=[Matrix(1,64,[int(x) for x in bridge.degree_functional]),Matrix(1,64,[int(x) for x in bridge.exceptional_mass_functional])]
    assigned=[P.row(i-1) for i in old.ASSIGNMENT]
    for i in range(4):
        r=Matrix.zeros(1,64)
        for j,s in enumerate(assigned): r += int(old.L[i][j])*s
        rows.append(r)
    F=Matrix.vstack(*rows); req(F.rank()==6,"fixed rank")
    hf,tf=fmpz_mat([[int(F[i,j]) for j in range(64)] for i in range(6)]).transpose().hnf(transform=True)
    T=Matrix([[int(tf[i,j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    A=T.T[:,:6]; K=T.T[:,6:]; I=F*A
    req(K.shape==(64,N) and F*K==Matrix.zeros(6,N),"kernel")
    Q=-(K.T*gram*K)
    qf,lf=fmpz_mat([[int(Q[i,j]) for j in range(N)] for i in range(N)]).lll(transform=True,rep="gram",gram="exact")
    U=Matrix([[int(lf[i,j]) for j in range(N)] for i in range(N)])
    R=Matrix([[int(qf[i,j]) for j in range(N)] for i in range(N)])
    RK=K*U.T; req(R==-(RK.T*gram*RK),"LLL replay")
    Ls,Ds=R.LDLdecomposition(hermitian=False); diag=[fq(Ds[i,i]) for i in range(N)]
    req(all(x>0 for x in diag),"positive definite")
    L=[[fq(Ls[i,j]) for j in range(N)] for i in range(N)]
    IR=P*RK; coeff=[]
    for k in range(140):
        src=[fmpq(int(IR[k,j])) for j in range(N)]; row=[]
        for j in range(N):
            z=src[j]
            for i in range(j): z-=row[i]*L[j][i]
            row.append(z)
        coeff.append(row)
    dual=[]
    for row in coeff:
        s=fmpq(0); q=[]
        for i in range(N): s+=row[i]*row[i]/diag[i]; q.append(s)
        dual.append(q)
    return F,A,I,RK,R,L,diag,coeff,dual,P,gram

def solve(base4, shard_id=0, shard_count=1, split_index=53):
    F,A,I,RK,R,L,diag,coeff,dual,P,gram=build()
    target=Matrix([D,E,*base4]); ic=I.inv()*target
    if not all(getattr(x,"q",1)==1 for x in ic):
        return {"classification":"HNF_IMAGE_UNSAT","base4":list(base4),"complete":True}
    bp=A*ic; req(all(getattr(x,"q",1)==1 for x in bp),"integral base point")
    q0=(bp.T*gram*bp)[0]; cross=RK.T*gram*bp
    center_s=R.inv()*cross; center=[fq(x) for x in center_s]
    radius_s=q0-LOW+(cross.T*R.inv()*cross)[0]; req(radius_s>=0,"radius")
    radius=fq(radius_s)
    fixed=[fq(x) for x in P*(bp+RK*center_s)]
    req(shard_count>=1 and 0<=shard_id<shard_count,"shard bounds")
    req(0<=split_index<N,"split index")
    coords=[0]*N; nodes=prunes=lower_prunes=upper_prunes=leaves=0; witness=None; tr=hashlib.sha256()
    pair_upper=[NORMAL_MASS]*92+[E]*48
    assigned_prefixes=skipped_prefixes=0

    def ev(*p): tr.update(("|".join(map(str,p))+"\n").encode())
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
        nonlocal nodes,leaves,witness,assigned_prefixes,skipped_prefixes
        if witness is not None: return
        nodes+=1; ev("N",i,rem)
        alpha=-center[i]
        for j in range(i+1,N): alpha+=L[j][i]*(coords[j]-center[j])
        exact=-alpha; base=int(exact.p)//int(exact.q)
        # Exact interval: expand symmetrically until both sides exceed remaining.
        step=0
        while True:
            vals=[base] if step==0 else [base-step,base+step]
            any_possible=False
            for val in vals:
                transformed=val+alpha; cost=diag[i]*transformed*transformed
                if cost>rem: continue
                any_possible=True; coords[i]=val
                for k in range(140): fixed[k]+=coeff[k][i]*transformed
                nr=rem-cost
                # Exact sharding happens on complete feasible prefixes at one
                # recursion level.  A prefix is assigned by a stable SHA256
                # residue, so shards are pairwise disjoint and their union is
                # exactly the unsharded search tree below split_index.
                assigned=True
                if i==split_index and shard_count>1:
                    prefix=tuple(coords[j] for j in range(i,N))
                    residue=int(hashlib.sha256(repr(prefix).encode()).hexdigest(),16)%shard_count
                    assigned=(residue==shard_id)
                    if assigned: assigned_prefixes+=1
                    else: skipped_prefixes+=1
                if assigned and viable(i-1,nr):
                    if i: rec(i-1,nr)
                    else:
                        leaves+=1
                        x=bp+RK*Matrix(coords); pair=P*x; c2=int((x.T*gram*x)[0])
                        req(min(pair)>=0 and c2>=LOW,"leaf verification")
                        req(max(pair[:92,:])<=NORMAL_MASS and max(pair[92:,:])<=E,"leaf pairing upper bounds")
                        # The Fincke--Pohst ellipsoid is bounded by the
                        # adjunction lower edge only.  Leaves above HIGH are
                        # valid relaxed-fiber points, not bad-shell witnesses;
                        # keep enumerating until a LOW..HIGH witness is found
                        # or the complete ellipsoid is exhausted.
                        if c2<=HIGH:
                            witness={"C2":c2,"picard_coordinates":[int(v) for v in x]}
                for k in range(140): fixed[k]-=coeff[k][i]*transformed
                if witness is not None: return
            if step>0 and not any_possible:
                left=fq(base-step)+alpha; right=fq(base+step)+alpha
                if diag[i]*left*left>rem and diag[i]*right*right>rem: break
            step+=1
    t=time.perf_counter(); rec(N-1,radius); elapsed=time.perf_counter()-t
    return {"schema":"STAGE32EX5_EFF_AFFINE01_FP58_KEY_V1","base4":list(base4),"bad_shell":[LOW,HIGH],
      "classification":"BAD_SHELL_SAT_WITNESS" if witness else "BAD_SHELL_UNSAT_EXACT",
      "complete":True,"kernel_dimension":N,"all140_pruning":True,"two_sided_pairing_pruning":True,"node_count":nodes,
      "intersection_prune_count":prunes,"lower_pairing_prune_count":lower_prunes,
      "upper_pairing_prune_count":upper_prunes,"feasible_leaf_count":leaves,"transcript_sha256":tr.hexdigest(),
      "elapsed_seconds":elapsed,"witness":witness,
      "shard":{"id":shard_id,"count":shard_count,"split_index":split_index,
               "assigned_prefix_count":assigned_prefixes,"skipped_prefix_count":skipped_prefixes,
               "partition":"SHA256_REPR_PREFIX_MOD_COUNT_V1"},
      "credit":{"effectivity":False,"main":False}}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--base4",nargs=4,type=int,required=True); ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--shard-id",type=int,default=0); ap.add_argument("--shard-count",type=int,default=1); ap.add_argument("--split-index",type=int,default=53); a=ap.parse_args()
    out=solve(tuple(a.base4),a.shard_id,a.shard_count,a.split_index); out["canonical_sha256_without_this_field"]=csha(out)
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("EFF_AFFINE01_FP58="+out["classification"]); print("CANONICAL="+out["canonical_sha256_without_this_field"])
if __name__=="__main__": main()
