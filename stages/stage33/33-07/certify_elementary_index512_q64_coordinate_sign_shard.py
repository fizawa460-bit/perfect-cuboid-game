#!/usr/bin/env python3
"""Exact q+cc+ct+seven-coordinate-sign simultaneous conjugacy on q64.

The previous q256 simultaneous-V4 solver supplies the exact quotient
presentation, finite quadratic form, and all induced cc/ct classes.  Here we
add the seven Q-rational coordinate sign involutions.  Stage29-02e proves that
sigma_x has +1 on exactly the rank-two T(K_x) piece and -1 on the other six
rank-two pieces.  On L0=<8>^10+<16>^4 this is therefore a literal block-scalar
integral action, with no extension choice.
"""
import hashlib,itertools,json,math,os
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp
from z3 import And,BitVec,BitVecVal,Extract,Or,Solver,ULT,Xor,sat,unsat
from elementary_index512_q256_retained import load as load_q256
HERE=Path(__file__).resolve().parent
# Load definitions only (not the shard main) from the already audited V4 solver.
src=(HERE/'certify_elementary_index512_q256_simultaneous_v4_shard.py').read_text()
prefix=src.split('# H0 regression:',1)[0]
NS={'__file__':str(HERE/'certify_elementary_index512_q256_simultaneous_v4_shard.py'),'__name__':'stage33_v4_common'}
exec(compile(prefix,'stage33_v4_common','exec'),NS)
build_source=NS['build_source'];mods=NS['mods'];mods0=NS['mods0'];Bt=NS['Bt'];CCt=NS['CCt'];CTt=NS['CTt']
qnum=NS['qnum'];bnum=NS['bnum'];gf2_rank_matrix=NS['gf2_rank_matrix'];bits=NS['bits'];gf2_basis=NS['gf2_basis'];dot=NS['dot']
SURV=load_q256()
V4=json.loads((HERE/'elementary-index512-q256-simultaneous-v4-census-retained.json').read_text())
SIG=json.loads((HERE/'endpoint-coordinate-sign-discriminant-actions.json').read_text())
if V4['canonical_sha256']!='a35211b2f18d2a7be3a91724fd7e13750a09d712201b56387fd3fad8adc5a252':raise SystemExit('q64 V4 lock moved')
if SIG['schema']!='STAGE33_07_ENDPOINT_COORDINATE_SIGN_DISCRIMINANT_ACTIONS_V1' or len(SIG['sign_actions_mixed_moduli'])!=7:raise SystemExit('endpoint sign source regression')
SIGNt=SIG['sign_actions_mixed_moduli']
# L0 pair order: Kb1,Kb2,Kb3,Kc,Ka1,Ka2,Ka3.
piece_coords=[(0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13)]
# endpoint coordinate order is a1,a2,a3,b1,b2,b3,c.
coord_to_piece=[4,5,6,0,1,2,3]

def presentation_inducer(Hbits):
    C=[[(int(h)>>i)&1 for i in range(14)] for h in Hbits];Cb=gf2_basis(Hbits)
    perp=[x for x in range(1<<14) if all(dot(x,c)==0 for c in Cb)];Pb=gf2_basis(perp)
    if len(Cb)!=9 or len(Pb)!=5:raise SystemExit('q64 H/perp dimension regression')
    P=[[(b>>i)&1 for i in range(14)] for b in Pb];pmap={}
    for mask in range(1<<5):
        x=0
        for k,b in enumerate(Pb):
            if (mask>>k)&1:x^=b
        pmap[x]=[(mask>>k)&1 for k in range(5)]
    rels=[]
    for k,p in enumerate(P):
        r=[0]*19;r[k]=2
        for i,b in enumerate(p):r[5+i]-=b
        rels.append(r)
    for i,d in enumerate(mods0):
        r=[0]*19;r[5+i]=d//2;rels.append(r)
    for c in C:
        r=[0]*19
        for i,b in enumerate(c):
            if b:r[5+i]=mods0[i]//4
        rels.append(r)
    R=sp.Matrix(rels);D,S,T=smith_normal_decomp(R,domain=ZZ)
    if S*R*T!=D or [abs(int(D[i,i])) for i in range(19)]!=[1]*5+mods:raise SystemExit('sign quotient Smith regression')
    Ti=T.inv();E=P+[[2 if j==i else 0 for j in range(14)] for i in range(14)]
    def apply(v,M):return [sum(int(v[i])*int(M[i][j]) for i in range(14))%mods0[j] for j in range(14)]
    def express(v):
        pb=bits([int(x)&1 for x in v])
        if pb not in pmap:raise SystemExit('coordinate sign left Hperp')
        a=pmap[pb];base=[sum(a[k]*P[k][i] for k in range(5)) for i in range(14)];z=[]
        for i,d in enumerate(mods0):
            diff=(int(v[i])-base[i])%d
            if diff%2:raise SystemExit('coordinate sign expression parity regression')
            z.append((diff//2)%(d//2))
        return a+z
    def induced(M):
        A=sp.Matrix([express(apply(v,M)) for v in E]);N=Ti*A*T
        return [[int(N[i,j])%mods[j-5] for j in range(5,19)] for i in range(5,19)]
    return induced

def source_signs(Hbits):
    induced=presentation_inducer(Hbits);out=[]
    for target_piece in coord_to_piece:
        M=[[0]*14 for _ in range(14)]
        for i,m in enumerate(mods0):M[i][i]=1 if i in piece_coords[target_piece] else (m-1)
        A=induced(M);out.append(A)
    # seven signs commute, square to one, product one on Q.
    def comp(A,B):return [[sum(int(A[i][k])*int(B[k][j]) for k in range(14))%mods[j] for j in range(14)] for i in range(14)]
    I=[[1 if i==j else 0 for j in range(14)] for i in range(14)]
    if any(comp(A,A)!=I for A in out):raise SystemExit('source sign involution regression')
    if any(comp(out[i],out[j])!=comp(out[j],out[i]) for i in range(7) for j in range(7)):raise SystemExit('source signs failed commute')
    p=I
    for A in out:p=comp(p,A)
    if p!=I:raise SystemExit('source seven-sign product regression')
    return out

def zsum(vs):
    z=BitVecVal(0,4)
    for v in vs:z=z+v
    return z
def bit0(x):return Extract(0,0,x)==BitVecVal(1,1)
def xorall(vs):
    z=vs[0]
    for v in vs[1:]:z=Xor(z,v)
    return z

def decide(Bs,ccclasses,ctclasses,ss,prefix):
    P=[[BitVec(f'{prefix}_p_{i}_{j}',4) for j in range(14)] for i in range(14)]
    s=Solver();s.set(timeout=180000);s.set(random_seed=0)
    for i,mi in enumerate(mods):
        for j,mj in enumerate(mods):
            s.add(ULT(P[i][j],BitVecVal(mj,4)));step=mj//math.gcd(mi,mj)
            if step>1:s.add((P[i][j]&BitVecVal(step-1,4))==BitVecVal(0,4))
    def q4(row):return zsum([row[a]*BitVecVal(Bt[a][b]%16,4)*row[b] for a in range(14) for b in range(14)])
    def b3(x,y):
        z=BitVecVal(0,3)
        for a in range(14):
            xa=Extract(2,0,x[a])
            for b in range(14):z=z+xa*BitVecVal(Bt[a][b]%8,3)*Extract(2,0,y[b])
        return z
    for i in range(14):s.add(q4(P[i])==BitVecVal(Bs[i][i]%16,4))
    for i in range(14):
        for j in range(i):s.add(b3(P[i],P[j])==BitVecVal(Bs[i][j]%8,3))
    for lo,hi in ((0,4),(4,10),(10,14)):
        for mask in range(1,1<<(hi-lo)):
            sel=[lo+r for r in range(hi-lo) if (mask>>r)&1]
            s.add(Or(*[xorall([bit0(P[r][c]) for r in sel]) for c in range(lo,hi)]))
    def inter(As,At):
        cs=[]
        for i in range(14):
            for j,mj in enumerate(mods):
                L=zsum([BitVecVal(int(As[i][k])%16,4)*P[k][j] for k in range(14)])
                R=zsum([P[i][k]*BitVecVal(int(At[k][j])%16,4) for k in range(14)])
                cs.append(((L-R)&BitVecVal(mj-1,4))==BitVecVal(0,4))
        return And(*cs)
    s.add(Or(*[inter(A,CCt) for A,_ in ccclasses]));s.add(Or(*[inter(A,CTt) for A,_ in ctclasses])
    for A,T in zip(ss,SIGNt):s.add(inter(A,T))
    res=s.check()
    if res==unsat:return False,None,[],[]
    if res!=sat:raise SystemExit(f'coordinate-sign solver non-decision {res}')
    m=s.model();W=[[m.eval(P[i][j],model_completion=True).as_long() for j in range(14)] for i in range(14)]
    for i,mi in enumerate(mods):
        for j,mj in enumerate(mods):
            if not(0<=W[i][j]<mj) or (mi*W[i][j])%mj:raise SystemExit('sign witness hom verification failed')
    for i in range(14):
        if qnum(W[i],Bt)!=Bs[i][i]%16:raise SystemExit('sign witness q verification failed')
        for j in range(i):
            if bnum(W[i],W[j],Bt)!=Bs[i][j]%8:raise SystemExit('sign witness bilinear verification failed')
    ranks=[gf2_rank_matrix([[W[i][j]&1 for j in range(lo,hi)] for i in range(lo,hi)]) for lo,hi in ((0,4),(4,10),(10,14))]
    if ranks!=[4,6,4]:raise SystemExit('sign witness automorphism rank failed')
    def okinter(As,At):
        return all(sum(int(As[i][k])*W[k][j] for k in range(14))%mods[j]==sum(W[i][k]*int(At[k][j]) for k in range(14))%mods[j] for i in range(14) for j in range(14))
    cm=[i for i,(A,_) in enumerate(ccclasses) if okinter(A,CCt)];tm=[i for i,(A,_) in enumerate(ctclasses) if okinter(A,CTt)]
    if not cm or not tm or any(not okinter(A,T) for A,T in zip(ss,SIGNt)):raise SystemExit('coordinate-sign SAT witness independent intertwining failed')
    return True,W,cm,tm

shard=int(os.environ.get('SHARD_INDEX','0'));nshard=int(os.environ.get('SHARD_COUNT','16'))
q64=set(int(x) for x in V4['survivor_indices'])
records=[r for r in SURV['records'] if int(r['index']) in q64 and int(r['index'])%nshard==shard]
if len(records)!=4:raise SystemExit(f'q64 sign shard size regression {len(records)}')
out=[];surv=0
for r in records:
    Bs,cc,ct=build_source(r['H_basis_bits']);ss=source_signs(r['H_basis_bits'])
    ok,W,cm,tm=decide(Bs,cc,ct,ss,f'sign{r["index"]}');surv+=int(ok)
    out.append({'index':int(r['index']),'simultaneous_q_cc_ct_7sign_conjugacy':bool(ok),'witness_sha256':None if W is None else hashlib.sha256(json.dumps(W,separators=(',',':')).encode()).hexdigest(),'matching_cc_class_indices':cm,'matching_ct_class_indices':tm})
cert={'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q64_COORDINATE_SIGN_SHARD_V1','source_q256_sha256':SURV['canonical_sha256'],'source_q64_v4_sha256':V4['canonical_sha256'],'endpoint_coordinate_sign_sha256':SIG['canonical_sha256'],'shard_index':shard,'shard_count':nshard,'candidate_count':4,'survivor_count':surv,'results':out,'actual_index512_glue_identified':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/f'elementary-index512-q64-coordinate-sign-shard-{shard}.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'shard':shard,'candidates':4,'survivors':surv,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
