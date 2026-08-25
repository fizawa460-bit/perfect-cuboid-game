#!/usr/bin/env python3
"""Scout exact action-filtration invariants on sampled non-elementary k1/k2 survivors.

For sampled exact Q2+2Q-profile survivors, reconstruct H <= A0, compute
Q=H^perp/H in Smith coordinates, transport every retained cc/ct action class,
and compare fixed dimensions on the characteristic filtration
Q[2] >= Q[2] cap 2Q >= Q[2] cap 4Q.  The cc, ct, and joint-V4 fixed dimensions
are conjugacy invariants.  A mismatch is an exact action-conjugacy rejection;
a match is only inconclusive.  This is deliberately a scout, not an exhaustive
endpoint-action certificate.
"""
import hashlib,itertools,json,os,runpy
from collections import Counter
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp

HERE=Path(__file__).resolve().parent
MODS0=[8]*10+[16]*4
MODS=[2]*4+[4]*6+[8]*4
ACTION_LOCK='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20'
TARGET_LOCK='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
Q2_LOCK='18d33892d04de286bfa8aa006fb8e4d133d7b51472e950c51bc74cc67a366300'
Q2_BIN_LOCK='4eebb36004d88917a233a7f449056e9d20082de94018d9ce4b48bbbbfe144c36'
OUT=HERE/'nonelementary-k12-action-filtration-scout.json'

# Reuse the already-regressed materialized-H decoder without solving any
# finite-q sample in this process.
old_s=os.environ.get('SAMPLE_PER_KIND'); old_t=os.environ.get('Z3_TIMEOUT_MS')
os.environ['SAMPLE_PER_KIND']='0'; os.environ['Z3_TIMEOUT_MS']='1'
base=runpy.run_path(str(HERE/'scout_nonelementary_k12_full_q_isometry.py'))
if old_s is None: os.environ.pop('SAMPLE_PER_KIND',None)
else: os.environ['SAMPLE_PER_KIND']=old_s
if old_t is None: os.environ.pop('Z3_TIMEOUT_MS',None)
else: os.environ['Z3_TIMEOUT_MS']=old_t
reconstruct_rows=base['reconstruct_rows']; verify_isotropic=base['verify_isotropic']
quantile_sample=base['quantile_sample']; all_records=base['all_records']

q2=json.loads((HERE/'nonelementary-k12-exact-q2-2q-profile-filter.json').read_text())
u=dict(q2); s=u.pop('canonical_sha256',None)
if s!=Q2_LOCK or hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()!=s:
    raise SystemExit('Q2 certificate lock moved')
b=(HERE/'nonelementary-k12-exact-q2-2q-profile-surviving-orbits.bin').read_bytes()
if hashlib.sha256(b).hexdigest()!=Q2_BIN_LOCK or len(b)!=104028*7: raise SystemExit('Q2 binary lock moved')
actions=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
if actions.get('canonical_sha256')!=ACTION_LOCK: raise SystemExit('action lock moved')
target=json.loads((HERE/'picard-discriminant-compact.json').read_text())
if target.get('canonical_sha256')!=TARGET_LOCK: raise SystemExit('target lock moved')
CCt=[[int(x)%MODS[j] for j,x in enumerate(r)] for r in target['cc_action_mixed_moduli']]
CTt=[[int(x)%MODS[j] for j,x in enumerate(r)] for r in target['ct_action_mixed_moduli']]
PIECES=[(0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13)]
NAMES=['kb','kb','kb','kc','ka','ka','ka']
if any(not actions['pieces'][k]['all_pairs_cartesian'] for k in ('kb','kc','ka')): raise SystemExit('action Cartesian lock moved')

def add(a,b): return tuple((int(x)+int(y))%m for x,y,m in zip(a,b,MODS0))
def scale(c,a): return tuple((int(c)*int(x))%m for x,m in zip(a,MODS0))
def apply(v,M): return tuple(sum(int(v[i])*int(M[i][j]) for i in range(14))%MODS0[j] for j in range(14))
def subgroup(rows,kind):
    orders=[4]*kind+[2]*(len(rows)-kind); out=set()
    for cs in itertools.product(*[range(o) for o in orders]):
        x=(0,)*14
        for c,r in zip(cs,rows): x=add(x,scale(c,r))
        out.add(x)
    if len(out)!=512: raise SystemExit('H order regression')
    return out

def quotient_context(rows):
    n=len(rows); cong=[[int(h[j])*(16//MODS0[j]) for j in range(14)] for h in rows]
    aug=sp.Matrix([cong[i]+[-16*int(i==j) for j in range(n)] for i in range(n)])
    D,L,R=smith_normal_decomp(aug,domain=ZZ)
    if L*aug*R!=D: raise SystemExit('Hperp Smith regression')
    rank=sum(D[i,i]!=0 for i in range(min(D.shape)))
    B=sp.Matrix([[int(R[i,j]) for i in range(14)] for j in range(rank,R.cols)])
    if B.shape!=(14,14) or abs(int(B.det()))!=512: raise SystemExit('Hperp basis regression')
    Bi=B.inv(); rel=[]
    for j,m in enumerate(MODS0):
        r=[0]*14; r[j]=m; rel.append(r)
    rel.extend(rows); coords=[]
    for r in rel:
        v=sp.Matrix([r])*Bi
        if any(x.q!=1 for x in v): raise SystemExit('relation coordinate regression')
        coords.append([int(x) for x in v])
    RR=sp.Matrix(coords); Q,S,T=smith_normal_decomp(RR,domain=ZZ)
    if S*RR*T!=Q: raise SystemExit('quotient Smith regression')
    inv=[abs(int(Q[i,i])) for i in range(14)]
    if inv!=MODS: raise SystemExit(f'quotient factors moved {inv}')
    return B,Bi,T,T.inv()

def global_action(local):
    M=[[int(i==j) for j in range(14)] for i in range(14)]
    for (a,b),A in zip(PIECES,local):
        for ii,u in enumerate((a,b)):
            for jj,v in enumerate((a,b)): M[u][v]=int(A[ii][jj])%MODS0[v]
    return M

def akey(A): return json.dumps(A,separators=(',',':'))
def aadd(A,D): return [[(int(A[i][j])+int(D[i][j]))%MODS[j] for j in range(14)] for i in range(14)]
def asub(A,B): return [[(int(A[i][j])-int(B[i][j]))%MODS[j] for j in range(14)] for i in range(14)]
def compose(A,B): return [[sum(int(A[i][k])*int(B[k][j]) for k in range(14))%MODS[j] for j in range(14)] for i in range(14)]
ID=[[int(i==j) for j in range(14)] for i in range(14)]
def well(A): return all((MODS[i]*int(A[i][j]))%MODS[j]==0 for i in range(14) for j in range(14))

def classes(rows,kind,B,Bi,T,Ti,H):
    def induced(M):
        if any(apply(r,M) not in H for r in rows): raise SystemExit(f'{kind} action lost H')
        O=B*sp.Matrix(M)*Bi
        if any(x.q!=1 for x in O): raise SystemExit('Hperp action nonintegral')
        N=Ti*O*T
        if any(x.q!=1 for x in N): raise SystemExit('Smith action nonintegral')
        A=[[int(N[i,j])%MODS[j] for j in range(14)] for i in range(14)]
        if not well(A): raise SystemExit('induced action hom regression')
        return A
    sets=[actions['pieces'][name][kind+'_actions'] for name in NAMES]
    defaults=[x[0] for x in sets]; baseA=induced(global_action(defaults)); cur={akey(baseA):(baseA,1)}
    for pi,opts in enumerate(sets):
        ds=[]
        for opt in opts:
            local=list(defaults); local[pi]=opt; ds.append(asub(induced(global_action(local)),baseA))
        nxt={}
        for A,m in cur.values():
            for D in ds:
                C=aadd(A,D); k=akey(C)
                nxt[k]=(C,nxt.get(k,(None,0))[1]+m)
        cur=nxt
    exp=1024 if kind=='cc' else 128
    if sum(m for A,m in cur.values())!=exp: raise SystemExit(f'{kind} multiplicity regression')
    out=list(cur.values())
    if any(compose(A,A)!=ID for A,m in out): raise SystemExit(f'{kind} involution regression')
    return out

def q2rows(A):
    out=[]
    for i,mi in enumerate(MODS):
        h=mi//2; mask=0
        for j,mj in enumerate(MODS):
            v=(h*int(A[i][j]))%mj
            if v not in (0,mj//2): raise SystemExit('Q2 reduction regression')
            if v: mask|=1<<j
        out.append(mask)
    return out

def rank(rows):
    piv={}
    for raw in rows:
        x=int(raw)
        while x:
            p=x.bit_length()-1
            if p in piv: x^=piv[p]
            else: piv[p]=x; break
    return len(piv)
def fixed_dim(A,lo):
    R=q2rows(A); eq=[]
    for i in range(lo,14):
        if R[i]&((1<<lo)-1): raise SystemExit('characteristic Q2 layer not preserved')
    for j in range(lo,14):
        m=1<<j
        for i in range(lo,14):
            if (R[i]>>j)&1: m^=1<<i
        if m: eq.append(m>>lo)
    return (14-lo)-rank(eq)
def joint_dim(A,B,lo):
    RA=q2rows(A); RB=q2rows(B); eq=[]
    for R in (RA,RB):
        for i in range(lo,14):
            if R[i]&((1<<lo)-1): raise SystemExit('joint layer not preserved')
        for j in range(lo,14):
            m=1<<j
            for i in range(lo,14):
                if (R[i]>>j)&1: m^=1<<i
            if m: eq.append(m>>lo)
    return (14-lo)-rank(eq)
def sig(A): return tuple(fixed_dim(A,lo) for lo in (0,4,10))
def jsig(A,B): return tuple(joint_dim(A,B,lo) for lo in (0,4,10))
TCC=sig(CCt); TCT=sig(CTt); TJ=jsig(CCt,CTt)

n=int(os.environ.get('SAMPLE_PER_KIND','8')); selected=[]
for kind in (1,2): selected.extend((kind,)+r for r in quantile_sample(all_records[kind],n))
results=[]; hist=Counter(); by={1:Counter(),2:Counter()}
for kind,ordinal,sk,sol in selected:
    rows=reconstruct_rows(kind,sk,sol); verify_isotropic(rows); H=subgroup(rows,kind); B,Bi,T,Ti=quotient_context(rows)
    cc=classes(rows,'cc',B,Bi,T,Ti,H); ct=classes(rows,'ct',B,Bi,T,Ti,H)
    cm=[i for i,(A,m) in enumerate(cc) if sig(A)==TCC]; tm=[i for i,(A,m) in enumerate(ct) if sig(A)==TCT]; pairs=[]
    for ci in cm:
        for ti in tm:
            A=cc[ci][0]; C=ct[ti][0]
            if compose(A,C)==compose(C,A) and jsig(A,C)==TJ: pairs.append((ci,ti))
    status='ACTION_FILTRATION_MATCH' if pairs else 'ACTION_FILTRATION_REJECT'; hist[status]+=1; by[kind][status]+=1
    results.append({'kind':kind,'ordinal':ordinal,'skeleton_orbit_index':sk,'affine_solution_mask':sol,
      'cc_induced_classes':len(cc),'ct_induced_classes':len(ct),'matching_cc_classes':len(cm),'matching_ct_classes':len(tm),
      'matching_joint_pairs':len(pairs),'status':status})
out={'schema':'STAGE33_07_NONELEMENTARY_K12_ACTION_FILTRATION_SCOUT_V1','source_q2_sha256':Q2_LOCK,'source_q2_binary_sha256':Q2_BIN_LOCK,
 'source_action_sha256':ACTION_LOCK,'source_endpoint_sha256':TARGET_LOCK,'sample_per_kind':n,'sample_count':len(selected),
 'filtration':'Q[2] >= Q[2] cap 2Q >= Q[2] cap 4Q','target_cc_fixed_dimensions':list(TCC),'target_ct_fixed_dimensions':list(TCT),
 'target_joint_v4_fixed_dimensions':list(TJ),'status_counts':dict(sorted(hist.items())),
 'status_counts_by_kind':{f'k{k}':dict(sorted(v.items())) for k,v in by.items()},'results':results,
 'exact_sampled_action_filtration_certified':True,'ACTION_FILTRATION_REJECT_is_exact_no_conjugacy_for_sampled_H':True,
 'ACTION_FILTRATION_MATCH_is_only_necessary_match':True,'full_action_exhaustive_certified':False,'endpoint_finite_q_certified':False,
 'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'stage33_progress':'6/11',
 'stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
 'next_exact_leaf':'L33-07-USE-ACTION-FILTRATION-PREFILTER-BEFORE-SIMULTANEOUS-Q-V4'}
raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(raw).hexdigest(); OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'target':{'cc':TCC,'ct':TCT,'joint':TJ},'sample_count':len(selected),'status_counts':out['status_counts'],'by_kind':out['status_counts_by_kind'],'sha256':out['canonical_sha256']},indent=2,sort_keys=True))
