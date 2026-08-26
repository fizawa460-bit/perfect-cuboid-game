#!/usr/bin/env python3
"""Exact simultaneous endpoint finite-q + V4 conjugacy census shard for q256.

For each elementary H surviving every fixed-type/q filter, construct Q=H^perp/H
in Smith coordinates, its exact quadratic form, and all induced scaled cc/ct
action classes. The raw 1024 cc and 128 ct choices are deduplicated separately;
piecewise action choices are Cartesian, so any surviving cc class may pair with
any surviving ct class. One finite bit-vector SMT query then asks for an
isometry P to the endpoint quadratic module that simultaneously intertwines
some induced cc class and some induced ct class. SAT witnesses are independently
verified using ordinary integer arithmetic.
"""
import hashlib,itertools,json,math,os
from collections import Counter
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp
from z3 import And,BitVec,BitVecVal,Extract,Or,Solver,ULT,Xor,sat,unsat
from elementary_index512_q256_retained import load as load_q256

HERE=Path(__file__).resolve().parent
SURV=load_q256()
ACT=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
TGT=json.loads((HERE/'picard-discriminant-compact.json').read_text())
FULLQ=json.loads((HERE/'elementary-index512-q256-full-q-census-retained.json').read_text())
if SURV['canonical_sha256']!='3c68ac5ff99e8e4dd9f57733f1fd64b0637e8a7d7f69454e3bf391b9b8127506':raise SystemExit('q256 lock moved')
if ACT['canonical_sha256']!='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20':raise SystemExit('scaled action lock moved')
if TGT['canonical_sha256']!='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0':raise SystemExit('endpoint q/action lock moved')
if FULLQ['canonical_sha256']!='9555ccb575e96ab46f400a353184d4a25ccafc882e8bd3250cc6c811c12fa19e' or FULLQ['full_finite_q_isometric_count']!=256:raise SystemExit('q256 full-q lock moved')
if any(not ACT['pieces'][k]['all_pairs_cartesian'] for k in ('kb','kc','ka')):raise SystemExit('piece action choices not Cartesian')
mods0=[8]*10+[16]*4
mods=[2]*4+[4]*6+[8]*4
Bt=[[-int(x)%(16 if i==j else 8) for j,x in enumerate(row)] for i,row in enumerate(TGT['discriminant_bilinear_numerator_over_8_reduced'])]
CCt=[[int(x)%mods[j] for j,x in enumerate(row)] for row in TGT['cc_action_mixed_moduli']]
CTt=[[int(x)%mods[j] for j,x in enumerate(row)] for row in TGT['ct_action_mixed_moduli']]
piece_coords=[(0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13)]
piece_names=['kb','kb','kb','kc','ka','ka','ka']

def bits(row):return sum((int(v)&1)<<i for i,v in enumerate(row))
def gf2_basis(rows):
    piv={}
    for row in rows:
        x=int(row) if isinstance(row,int) else bits(row)
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return tuple(piv[p] for p in sorted(piv,reverse=True))
def dot(a,b):return (int(a)&int(b)).bit_count()&1
def qnum(x,B):return sum(int(x[i])*B[i][j]*int(x[j]) for i in range(14) for j in range(14))%16
def bnum(x,y,B):return sum(int(x[i])*B[i][j]*int(y[j]) for i in range(14) for j in range(14))%8
def gf2_rank_matrix(rows):
    piv={}
    for row in rows:
        x=sum((int(v)&1)<<j for j,v in enumerate(row))
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)
def compose(A,B):return [[sum(int(A[i][k])*int(B[k][j]) for k in range(14))%mods[j] for j in range(14)] for i in range(14)]
def identity():return [[1 if i==j else 0 for j in range(14)] for i in range(14)]
I=identity()
def add_action(A,D):return [[(int(A[i][j])+int(D[i][j]))%mods[j] for j in range(14)] for i in range(14)]
def sub_action(A,B):return [[(int(A[i][j])-int(B[i][j]))%mods[j] for j in range(14)] for i in range(14)]
def action_key(A):return json.dumps(A,separators=(',',':'))
def preserves_q(A,B):
    for i in range(14):
        if qnum(A[i],B)!=B[i][i]%16:return False
        for j in range(i):
            if bnum(A[i],A[j],B)!=B[i][j]%8:return False
    return True
def well_defined_action(A):
    for i,mi in enumerate(mods):
        for j,mj in enumerate(mods):
            if (mi*int(A[i][j]))%mj:return False
    return True

def build_source(Hbits):
    C=[[(int(h)>>i)&1 for i in range(14)] for h in Hbits]
    Cb=gf2_basis(Hbits)
    if len(Cb)!=9:raise SystemExit('H rank regression')
    perp=[x for x in range(1<<14) if all(dot(x,c)==0 for c in Cb)]
    Pb=gf2_basis(perp)
    if len(Pb)!=5:raise SystemExit('Hperp parity dimension regression')
    P=[[(b>>i)&1 for i in range(14)] for b in Pb]
    pmap={}
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
    if S*R*T!=D:raise SystemExit('presentation Smith transform regression')
    diag=[abs(int(D[i,i])) for i in range(19)]
    if diag!=[1]*5+mods:raise SystemExit(f'quotient Smith regression {diag}')
    Ti=T.inv()
    # Old presentation generators are five parity representatives P and 2e_i.
    E=P+[[2 if j==i else 0 for j in range(14)] for i in range(14)]
    B16=sp.zeros(19)
    for a in range(19):
        for b in range(19):
            B16[a,b]=sum((16//mods0[j])*E[a][j]*E[b][j] for j in range(14))
    NB=sp.simplify(Ti*B16*Ti.T)
    core=NB[5:19,5:19]
    if any(int(core[i,j])%2 for i in range(14) for j in range(14)):raise SystemExit('presentation q denominator regression')
    Bs=[[int(core[i,j]//2)%(16 if i==j else 8) for j in range(14)] for i in range(14)]
    def apply(v,M):return [sum(int(v[i])*int(M[i][j]) for i in range(14))%mods0[j] for j in range(14)]
    def express(v):
        pb=bits([int(x)&1 for x in v])
        if pb not in pmap:raise SystemExit('action left Hperp')
        a=pmap[pb];base=[sum(a[k]*P[k][i] for k in range(5)) for i in range(14)];z=[]
        for i,d in enumerate(mods0):
            diff=(int(v[i])-base[i])%d
            if diff%2:raise SystemExit('Hperp expression parity regression')
            z.append((diff//2)%(d//2))
        return a+z
    def induced(M):
        A=sp.Matrix([express(apply(v,M)) for v in E]);N=Ti*A*T
        out=[[int(N[i,j])%mods[j-5] for j in range(5,19)] for i in range(5,19)]
        if not well_defined_action(out):raise SystemExit('induced action homomorphism regression')
        return out
    def global_action(local):
        M=[[0]*14 for _ in range(14)]
        for i in range(14):M[i][i]=1
        for (a,b),A in zip(piece_coords,local):
            for ii,u in enumerate((a,b)):
                for jj,v in enumerate((a,b)):M[u][v]=int(A[ii][jj])%mods0[v]
        return M
    def classes(kind):
        sets=[ACT['pieces'][name][kind+'_actions'] for name in piece_names]
        defaults=[x[0] for x in sets]
        base=induced(global_action(defaults))
        cur={action_key(base):(base,1)}
        for pi,opts in enumerate(sets):
            deltas=[]
            for opt in opts:
                local=list(defaults);local[pi]=opt
                deltas.append(sub_action(induced(global_action(local)),base))
            nxt={}
            for A,mult in cur.values():
                for delta in deltas:
                    B=add_action(A,delta);k=action_key(B)
                    if k in nxt:nxt[k]=(nxt[k][0],nxt[k][1]+mult)
                    else:nxt[k]=(B,mult)
            cur=nxt
        expected=1024 if kind=='cc' else 128
        if sum(m for A,m in cur.values())!=expected:raise SystemExit(f'{kind} raw multiplicity regression')
        out=list(cur.values())
        for A,m in out:
            if not preserves_q(A,Bs):raise SystemExit(f'{kind} action failed q preservation')
            if compose(A,A)!=I:raise SystemExit(f'{kind} action failed involution')
        return out
    cc=classes('cc');ct=classes('ct')
    for A,_ in cc:
        for B,_ in ct:
            if compose(A,B)!=compose(B,A):raise SystemExit('induced cc/ct failed commute after forced-commutator filter')
    return Bs,cc,ct

def zsum(vs):
    z=BitVecVal(0,4)
    for v in vs:z=z+v
    return z
def bit0(x):return Extract(0,0,x)==BitVecVal(1,1)
def xorall(vs):
    z=vs[0]
    for v in vs[1:]:z=Xor(z,v)
    return z

def decide(Bs,ccclasses,ctclasses,prefix):
    P=[[BitVec(f'{prefix}_p_{i}_{j}',4) for j in range(14)] for i in range(14)]
    s=Solver();s.set(timeout=180000);s.set(random_seed=0)
    for i,mi in enumerate(mods):
        for j,mj in enumerate(mods):
            s.add(ULT(P[i][j],BitVecVal(mj,4)))
            step=mj//math.gcd(mi,mj)
            if step>1:s.add((P[i][j]&BitVecVal(step-1,4))==BitVecVal(0,4))
    def q4(row):
        return zsum([row[a]*BitVecVal(Bt[a][b]%16,4)*row[b] for a in range(14) for b in range(14)])
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
        n=hi-lo
        for mask in range(1,1<<n):
            sel=[lo+r for r in range(n) if (mask>>r)&1]
            s.add(Or(*[xorall([bit0(P[r][c]) for r in sel]) for c in range(lo,hi)]))
    def intertwine_constraints(As,At):
        out=[]
        for i in range(14):
            for j,mj in enumerate(mods):
                left=zsum([BitVecVal(int(As[i][k])%16,4)*P[k][j] for k in range(14)])
                right=zsum([P[i][k]*BitVecVal(int(At[k][j])%16,4) for k in range(14)])
                out.append(((left-right)&BitVecVal(mj-1,4))==BitVecVal(0,4))
        return And(*out)
    s.add(Or(*[intertwine_constraints(A,CCt) for A,m in ccclasses]))
    s.add(Or(*[intertwine_constraints(A,CTt) for A,m in ctclasses]))
    res=s.check()
    if res==unsat:return False,None,[],[]
    if res!=sat:raise SystemExit(f'simultaneous V4 solver non-decision {res}')
    m=s.model();W=[[m.eval(P[i][j],model_completion=True).as_long() for j in range(14)] for i in range(14)]
    # Independent finite-q automorphism verification.
    for i,mi in enumerate(mods):
        for j,mj in enumerate(mods):
            if not(0<=W[i][j]<mj) or (mi*W[i][j])%mj:raise SystemExit('V4 witness hom verification failed')
    for i in range(14):
        if qnum(W[i],Bt)!=Bs[i][i]%16:raise SystemExit('V4 witness q verification failed')
        for j in range(i):
            if bnum(W[i],W[j],Bt)!=Bs[i][j]%8:raise SystemExit('V4 witness bilinear verification failed')
    ranks=[gf2_rank_matrix([[W[i][j]&1 for j in range(lo,hi)] for i in range(lo,hi)]) for lo,hi in ((0,4),(4,10),(10,14))]
    if ranks!=[4,6,4]:raise SystemExit('V4 witness automorphism rank failed')
    def intertwines(As,At):
        for i in range(14):
            for j,mj in enumerate(mods):
                L=sum(int(As[i][k])*W[k][j] for k in range(14))%mj
                R=sum(W[i][k]*int(At[k][j]) for k in range(14))%mj
                if L!=R:return False
        return True
    cm=[i for i,(A,mult) in enumerate(ccclasses) if intertwines(A,CCt)]
    tm=[i for i,(A,mult) in enumerate(ctclasses) if intertwines(A,CTt)]
    if not cm or not tm:raise SystemExit('SAT witness failed independent intertwining verification')
    return True,W,cm,tm

# H0 regression: q-isometric but endpoint ct action type mismatch, so simultaneous conjugacy must fail.
def H0_bits():
    C5=[[1,1,0,0,1,1,0,0,0,0],[1,0,0,0,0,1,1,0,1,0],[0,0,1,0,1,0,0,0,0,0],[1,1,1,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,1,0,1]]
    C=[r+[0]*4 for r in C5]
    for j in range(4):
        r=[0]*14;r[10+j]=1;C.append(r)
    return [bits(r) for r in C]

shard=int(os.environ.get('SHARD_INDEX','0'));nshard=int(os.environ.get('SHARD_COUNT','16'))
if not(0<=shard<nshard):raise SystemExit('bad shard')
if shard==0:
    hB,hcc,hct=build_source(H0_bits())
    ok,W,cm,tm=decide(hB,hcc,hct,'h0')
    if ok:raise SystemExit('H0 simultaneous V4 rejection regression failed')
records=[r for r in SURV['records'] if int(r['index'])%nshard==shard]
if len(records)!=16:raise SystemExit(f'V4 shard size regression {len(records)}')
out=[];surv=0;ccclass=Counter();ctclass=Counter()
for r in records:
    Bs,cc,ct=build_source(r['H_basis_bits']);ccclass[len(cc)]+=1;ctclass[len(ct)]+=1
    ok,W,cm,tm=decide(Bs,cc,ct,f'h{r["index"]}')
    surv+=int(ok)
    out.append({'index':int(r['index']),'cc_induced_class_count':len(cc),'ct_induced_class_count':len(ct),'simultaneous_q_v4_conjugacy':bool(ok),'witness_sha256':None if W is None else hashlib.sha256(json.dumps(W,separators=(',',':')).encode()).hexdigest(),'matching_cc_class_indices':cm,'matching_ct_class_indices':tm})
cert={'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q256_SIMULTANEOUS_V4_SHARD_V1','q256_sha256':SURV['canonical_sha256'],'full_q_census_sha256':FULLQ['canonical_sha256'],'scaled_action_sha256':ACT['canonical_sha256'],'endpoint_q_action_sha256':TGT['canonical_sha256'],'shard_index':shard,'shard_count':nshard,'candidate_count':16,'simultaneous_q_v4_survivor_count':surv,'cc_induced_class_count_census':{str(k):v for k,v in sorted(ccclass.items())},'ct_induced_class_count_census':{str(k):v for k,v in sorted(ctclass.items())},'results':out,'h0_rejection_regressed':shard==0,'actual_index512_glue_identified':False,'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/f'elementary-index512-q256-simultaneous-v4-shard-{shard}.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'shard':shard,'candidates':16,'survivors':surv,'cc_class_census':cert['cc_induced_class_count_census'],'ct_class_census':cert['ct_induced_class_count_census'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
