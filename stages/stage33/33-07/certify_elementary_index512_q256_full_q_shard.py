#!/usr/bin/env python3
"""Exact full finite-q isometry shard for the retained 256 elementary H."""
import hashlib,json,math,os
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_decomp
from z3 import BitVec,BitVecVal,Extract,Or,Solver,ULT,Xor,sat,unsat

HERE=Path(__file__).resolve().parent
TGT=json.loads((HERE/'picard-discriminant-compact.json').read_text())
SURV=json.loads((HERE/'elementary-index512-q256-survivors.json').read_text())
TARGET_LOCK='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
QFILTER_LOCK='1e9999ab0b150803d77da0271ef5c6b87eccb353701220c7565a5fddff8c6edc'
if TGT['canonical_sha256']!=TARGET_LOCK: raise SystemExit('target q source lock moved')
if SURV['schema']!='STAGE33_07_ELEMENTARY_INDEX512_Q256_SURVIVORS_V1' or SURV['candidate_count']!=256: raise SystemExit('q256 survivor schema regression')
if SURV['source_q_filtration_sha256']!=QFILTER_LOCK: raise SystemExit('q256 parent lock moved')
mods=[2]*4+[4]*6+[8]*4
Bt=[[-int(x)%(16 if i==j else 8) for j,x in enumerate(row)] for i,row in enumerate(TGT['discriminant_bilinear_numerator_over_8_reduced'])]
D0=sp.diag(*([8]*10+[16]*4))

def bitsrow(x): return [(int(x)>>j)&1 for j in range(14)]
def red_b8(M): return [[int(M[i,j])%(16 if i==j else 8) for j in range(14)] for i in range(14)]
def candidate_b8(Hbits):
    C=[bitsrow(x) for x in Hbits]
    gens=sp.Matrix(2*sp.eye(14)).col_join(sp.Matrix(C))
    Kbasis=hermite_normal_form(gens.T).T
    B=Kbasis/2
    G=sp.simplify(B*D0*B.T)
    if any(v.q!=1 for v in G): raise SystemExit('nonintegral candidate Gram')
    if any(int(G[i,i])%2 for i in range(14)): raise SystemExit('candidate Gram not even')
    if abs(int(G.det()))!=2**28: raise SystemExit('candidate determinant regression')
    D,S,T=smith_normal_decomp(G,domain=ZZ)
    smith=[abs(int(D[i,i])) for i in range(14)]
    if smith!=mods: raise SystemExit(f'candidate Smith regression {smith}')
    Sinv=S.inv(); M=sp.simplify(8*(Sinv.T*G.inv()*Sinv))
    if any(v.q!=1 for v in M): raise SystemExit('candidate B8 nonintegral')
    return red_b8(M)

def qnum(row,B): return sum(row[a]*B[a][b]*row[b] for a in range(14) for b in range(14))%16
def bnum(x,y,B): return sum(x[a]*B[a][b]*y[b] for a in range(14) for b in range(14))%8
def gf2_rank(rows):
    piv={}
    for row in rows:
        x=sum((int(v)&1)<<j for j,v in enumerate(row))
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)

def solve_isometry(Bc):
    P=[[BitVec(f'p_{i}_{j}',4) for j in range(14)] for i in range(14)]
    s=Solver();s.set(timeout=60000);s.set(random_seed=0)
    for i,mi in enumerate(mods):
        for j,mj in enumerate(mods):
            s.add(ULT(P[i][j],BitVecVal(mj,4)))
            step=mj//math.gcd(mi,mj)
            if step>1:s.add((P[i][j]&BitVecVal(step-1,4))==BitVecVal(0,4))
    def q4(row):
        z=BitVecVal(0,4)
        for a in range(14):
            for b in range(14): z=z+row[a]*BitVecVal(Bt[a][b]%16,4)*row[b]
        return z
    def b3(x,y):
        z=BitVecVal(0,3)
        for a in range(14):
            xa=Extract(2,0,x[a])
            for b in range(14): z=z+xa*BitVecVal(Bt[a][b]%8,3)*Extract(2,0,y[b])
        return z
    for i in range(14):s.add(q4(P[i])==BitVecVal(Bc[i][i]%16,4))
    for i in range(14):
        for j in range(i):s.add(b3(P[i],P[j])==BitVecVal(Bc[i][j]%8,3))
    def bit0(x):return Extract(0,0,x)==BitVecVal(1,1)
    def xorall(vs):
        z=vs[0]
        for v in vs[1:]:z=Xor(z,v)
        return z
    for lo,hi in ((0,4),(4,10),(10,14)):
        n=hi-lo
        for mask in range(1,1<<n):
            sel=[lo+r for r in range(n) if (mask>>r)&1]
            s.add(Or(*[xorall([bit0(P[r][c]) for r in sel]) for c in range(lo,hi)]))
    res=s.check()
    if res==unsat:return False,None
    if res!=sat:raise SystemExit(f'full q solver non-decision {res}')
    m=s.model();W=[[m.eval(P[i][j],model_completion=True).as_long() for j in range(14)] for i in range(14)]
    for i,mi in enumerate(mods):
        for j,mj in enumerate(mods):
            if not(0<=W[i][j]<mj) or (mi*W[i][j])%mj:raise SystemExit('witness hom verification failed')
    for i in range(14):
        if qnum(W[i],Bt)!=Bc[i][i]%16:raise SystemExit('witness q verification failed')
        for j in range(i):
            if bnum(W[i],W[j],Bt)!=Bc[i][j]%8:raise SystemExit('witness b verification failed')
    ranks=[]
    for lo,hi in ((0,4),(4,10),(10,14)):
        r=gf2_rank([[W[i][j]&1 for j in range(lo,hi)] for i in range(lo,hi)]);ranks.append(r)
    if ranks!=[4,6,4]:raise SystemExit('witness automorphism rank failed')
    return True,W

shard=int(os.environ.get('SHARD_INDEX','0')); nshard=int(os.environ.get('SHARD_COUNT','8'))
if not(0<=shard<nshard):raise SystemExit('bad shard index')
records=[r for r in SURV['records'] if int(r['index'])%nshard==shard]
if len(records)!=256//nshard:raise SystemExit(f'shard size regression {len(records)}')
cache={};out=[];sat_count=0
for r in records:
    Bc=candidate_b8(r['H_basis_bits'])
    bkey=hashlib.sha256(json.dumps(Bc,separators=(',',':')).encode()).hexdigest()
    if bkey not in cache:cache[bkey]=solve_isometry(Bc)
    ok,W=cache[bkey];sat_count+=int(ok)
    wh=None if W is None else hashlib.sha256(json.dumps(W,separators=(',',':')).encode()).hexdigest()
    out.append({'index':r['index'],'b8_sha256':bkey,'full_q_isometric':bool(ok),'witness_sha256':wh})
cert={'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q256_FULL_Q_SHARD_V1','q256_survivor_sha256':SURV['canonical_sha256'],'target_sha256':TARGET_LOCK,'shard_index':shard,'shard_count':nshard,'candidate_count':len(records),'distinct_B8_matrices':len(cache),'full_q_isometric_count':sat_count,'results':out,'solver':'z3-solver 4.15.3 finite bit-vector exact; SAT witnesses independently integer-verified','actual_index512_glue_identified':False,'simultaneous_endpoint_cc_ct_action_conjugacy_certified':False,'stage33_progress':'6/11','stage33_08_released':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
fn=HERE/f'elementary-index512-q256-full-q-shard-{shard}.json';fn.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'shard':shard,'candidates':len(records),'distinct_B8':len(cache),'full_q_isometric':sat_count,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
