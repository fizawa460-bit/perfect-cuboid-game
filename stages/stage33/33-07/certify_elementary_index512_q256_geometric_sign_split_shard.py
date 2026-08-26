#!/usr/bin/env python3
"""Exact elementary q256 finite-q + seven geometric-sign census shard.

This leaf intentionally does NOT use arithmetic cc/ct actions.  For each of the
256 elementary order-512 glues that already has the endpoint finite quadratic
form, construct Q=H^perp/H exactly and ask whether one q-isometry to the locked
endpoint simultaneously intertwines the seven Q-rational coordinate-sign
involutions.  The source signs are literal block-scalar integral actions on
L0=<8>^10 + <16>^4, so this is usable for actual geometry without promoting
formal finite-discriminant cc/ct lifts to the integral Betti lattice.
"""
import hashlib,json,math,os
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp
from z3 import And,BitVec,BitVecVal,Extract,Or,Solver,ULT,Xor,sat,unsat
from elementary_index512_q256_retained import load as load_q256

HERE=Path(__file__).resolve().parent
SURV=load_q256()
FULLQ=json.loads((HERE/'elementary-index512-q256-full-q-census-retained.json').read_text())
SIG=json.loads((HERE/'endpoint-coordinate-sign-discriminant-actions-split.json').read_text())
if SURV['canonical_sha256']!='3c68ac5ff99e8e4dd9f57733f1fd64b0637e8a7d7f69454e3bf391b9b8127506':raise SystemExit('q256 lock moved')
if FULLQ['canonical_sha256']!='9555ccb575e96ab46f400a353184d4a25ccafc882e8bd3250cc6c811c12fa19e' or FULLQ['full_finite_q_isometric_count']!=256:raise SystemExit('q256 full-q lock moved')
if SIG['schema']!='STAGE33_07_ENDPOINT_COORDINATE_SIGN_DISCRIMINANT_ACTIONS_SPLIT_V2':raise SystemExit('endpoint sign schema moved')
if len(SIG['sign_actions_mixed_moduli'])!=7:raise SystemExit('endpoint sign count moved')
mods0=[8]*10+[16]*4
mods=[2]*4+[4]*6+[8]*4
if SIG['discriminant_moduli']!=mods:raise SystemExit('endpoint sign moduli moved')
if not SIG['all_actions_well_defined_involutions_and_q_isometries']:raise SystemExit('endpoint sign q-isometry regression')
if not SIG['seven_sign_involutions_commute'] or not SIG['seven_sign_product_identity']:raise SystemExit('endpoint sign relation regression')
# Split package is Picard discriminant; T-discriminant q is its negative.
Bt=[[-int(x)%(16 if i==j else 8) for j,x in enumerate(row)] for i,row in enumerate(SIG['discriminant_bilinear_numerator_over_8_reduced'])]
SIGNt=[[[int(x)%mods[j] for j,x in enumerate(row)] for row in A] for A in SIG['sign_actions_mixed_moduli']]
piece_coords=[(0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13)]
# Endpoint order a1,a2,a3,b1,b2,b3,c versus source piece order Kb1,Kb2,Kb3,Kc,Ka1,Ka2,Ka3.
coord_to_piece=[4,5,6,0,1,2,3]

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
def well_defined_action(A):
    return all((mods[i]*int(A[i][j]))%mods[j]==0 for i in range(14) for j in range(14))
def preserves_q(A,B):
    for i in range(14):
        if qnum(A[i],B)!=B[i][i]%16:return False
        for j in range(i):
            if bnum(A[i],A[j],B)!=B[i][j]%8:return False
    return True

def source_data(Hbits):
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
    Ti=T.inv();E=P+[[2 if j==i else 0 for j in range(14)] for i in range(14)]
    B16=sp.zeros(19)
    for a in range(19):
        for b in range(19):
            B16[a,b]=sum((16//mods0[j])*E[a][j]*E[b][j] for j in range(14))
    NB=sp.simplify(Ti*B16*Ti.T);core=NB[5:19,5:19]
    if any(int(core[i,j])%2 for i in range(14) for j in range(14)):raise SystemExit('presentation q denominator regression')
    Bs=[[int(core[i,j]//2)%(16 if i==j else 8) for j in range(14)] for i in range(14)]
    def apply(v,M):return [sum(int(v[i])*int(M[i][j]) for i in range(14))%mods0[j] for j in range(14)]
    def express(v):
        pb=bits([int(x)&1 for x in v])
        if pb not in pmap:raise SystemExit('geometric sign left Hperp')
        a=pmap[pb];base=[sum(a[k]*P[k][i] for k in range(5)) for i in range(14)];z=[]
        for i,d in enumerate(mods0):
            diff=(int(v[i])-base[i])%d
            if diff%2:raise SystemExit('Hperp expression parity regression')
            z.append((diff//2)%(d//2))
        return a+z
    def induced(M):
        A=sp.Matrix([express(apply(v,M)) for v in E]);N=Ti*A*T
        out=[[int(N[i,j])%mods[j-5] for j in range(5,19)] for i in range(5,19)]
        if not well_defined_action(out):raise SystemExit('induced sign homomorphism regression')
        return out
    signs=[]
    for target_piece in coord_to_piece:
        M=[[0]*14 for _ in range(14)]
        for i,m in enumerate(mods0):M[i][i]=1 if i in piece_coords[target_piece] else (m-1)
        A=induced(M)
        if not preserves_q(A,Bs):raise SystemExit('source geometric sign failed q preservation')
        signs.append(A)
    if any(compose(A,A)!=I for A in signs):raise SystemExit('source sign involution regression')
    if any(compose(signs[i],signs[j])!=compose(signs[j],signs[i]) for i in range(7) for j in range(7)):raise SystemExit('source signs failed commute')
    p=I
    for A in signs:p=compose(p,A)
    if p!=I:raise SystemExit('source seven-sign product regression')
    return Bs,signs

def zsum(vs):
    z=BitVecVal(0,4)
    for v in vs:z=z+v
    return z
def bit0(x):return Extract(0,0,x)==BitVecVal(1,1)
def xorall(vs):
    z=vs[0]
    for v in vs[1:]:z=Xor(z,v)
    return z

def decide(Bs,ss,prefix):
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
    for A,T in zip(ss,SIGNt):s.add(inter(A,T))
    res=s.check()
    if res==unsat:return False,None
    if res!=sat:raise SystemExit(f'geometric-sign solver non-decision {res}')
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
    if any(not okinter(A,T) for A,T in zip(ss,SIGNt)):raise SystemExit('geometric-sign witness independent intertwining failed')
    return True,W

shard=int(os.environ.get('SHARD_INDEX','0'));nshard=int(os.environ.get('SHARD_COUNT','32'))
records=[r for r in SURV['records'] if int(r['index'])%nshard==shard]
expected=256//nshard
if 256%nshard or len(records)!=expected:raise SystemExit(f'q256 geometric sign shard size regression {len(records)} expected {expected}')
out=[];surv=0
for r in records:
    Bs,ss=source_data(r['H_basis_bits'])
    ok,W=decide(Bs,ss,f'gsign{r["index"]}');surv+=int(ok)
    out.append({'index':int(r['index']),'simultaneous_q_7geometric_sign_conjugacy':bool(ok),'witness_sha256':None if W is None else hashlib.sha256(json.dumps(W,separators=(',',':')).encode()).hexdigest()})
cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q256_GEOMETRIC_SIGN_SPLIT_SHARD_V1',
 'source_q256_sha256':SURV['canonical_sha256'],
 'source_full_q_sha256':FULLQ['canonical_sha256'],
 'endpoint_coordinate_sign_sha256':SIG['canonical_sha256'],
 'arithmetic_cc_ct_used':False,
 'geometric_coordinate_signs_used':7,
 'shard_index':shard,'shard_count':nshard,'candidate_count':len(records),'survivor_count':surv,'results':out,
 'actual_index512_glue_identified':False,'INDEX512_GLUE_ACTUAL_GEOMETRY_PROVED':False,
 'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/f'elementary-index512-q256-geometric-sign-shard-{shard}.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'shard':shard,'candidates':len(records),'survivors':surv,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
