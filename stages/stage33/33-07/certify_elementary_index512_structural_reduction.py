#!/usr/bin/env python3
"""Exact structural reduction of all elementary order-512 index-512 glue H."""
import hashlib,itertools,json
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
ACT=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
TGT=json.loads((HERE/'target-discriminant-v4-fixed-module.json').read_text())
if ACT['canonical_sha256']!='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20': raise SystemExit('scaled action choices lock moved')
if TGT['canonical_sha256']!='a396d928ebe2a9dbc7b04aaf38b9fa30c3ef9366b1a2050409195642a690da88': raise SystemExit('target V4 fixed lock moved')
if TGT['target_discriminant_group']!='(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4': raise SystemExit('target group regression')
if TGT['ct_fixed_subgroup']['two_torsion_order_log2']!=13: raise SystemExit('target ct[2] regression')

def rank(vs):
    piv={}
    for x in vs:
        y=int(x)
        while y:
            p=y.bit_length()-1
            if p in piv:y^=piv[p]
            else:piv[p]=y;break
    return len(piv)
def canon(vs):
    piv={}
    for x in vs:
        y=int(x)
        while y:
            p=y.bit_length()-1
            if p in piv:y^=piv[p]
            else:
                for q in list(piv):
                    if (piv[q]>>p)&1:piv[q]^=y
                piv[p]=y;break
    return tuple(piv[p] for p in sorted(piv,reverse=True))
def contains(B,x):return rank(list(B)+[x])==len(B)
def rref_subspaces(n,k):
    if k==0:
        yield ();return
    for pivots in itertools.combinations(range(n),k):
        ps=set(pivots);free=[j for j in range(n) if j not in ps]
        slots=[(r,j) for j in free for r,p in enumerate(pivots) if p<j]
        for mask in range(1<<len(slots)):
            rows=[1<<p for p in pivots]
            for z,(r,j) in enumerate(slots):
                if (mask>>z)&1:rows[r]|=1<<j
            yield canon(rows)
def extend_basis(B,n):
    cur=list(canon(B));out=[]
    for i in range(n):
        e=1<<i
        if rank(cur+[e])>len(cur):cur.append(e);out.append(e)
    return out
def perp(B,n):return canon([x for x in range(1,1<<n) if all((x&b).bit_count()%2==0 for b in B)])

mods=[8]*10+[16]*4
piece_coords=[(0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13)]
ctsets=[ACT['pieces']['kb']['ct_actions']]*3+[ACT['pieces']['kc']['ct_actions']]+[ACT['pieces']['ka']['ct_actions']]*3
if [len(x) for x in ctsets]!=[2]*7:raise SystemExit('ct choice count regression')
def global_action(choice):
    M=[[0]*14 for _ in range(14)]
    for i in range(14):M[i][i]=1
    for (a,b),A in zip(piece_coords,choice):
        for ii,u in enumerate((a,b)):
            for jj,v in enumerate((a,b)):M[u][v]=int(A[ii][jj])%mods[v]
    return M
def half_lift_binary_map(M):
    rows=[]
    for i in range(14):
        x=[0]*14;x[i]=mods[i]//4
        y=[sum(x[k]*M[k][j] for k in range(14))%mods[j] for j in range(14)]
        out=0
        for j in range(14):
            d=(y[j]-x[j])%mods[j]
            if d not in (0,mods[j]//2):raise SystemExit('ct half-lift difference not order two')
            if d:out|=1<<j
        rows.append(out)
    return tuple(rows)
Lclasses=Counter(half_lift_binary_map(global_action(c)) for c in itertools.product(*ctsets))
if len(Lclasses)!=1 or next(iter(Lclasses.values()))!=128:raise SystemExit('ct half-lift binary action not universal')
L=next(iter(Lclasses));expected=tuple([0]*6+[1<<10,1<<11,1<<12,1<<13,1<<10,1<<11,1<<12,1<<13])
if L!=expected:raise SystemExit(f'universal ct half-lift map regression {L}')

Ssets={}
for s in (2,3,4):
    arr=[]
    for S in rref_subspaces(4,s):
        Sp=perp(S,4)
        if all(contains(S,x) for x in Sp):arr.append(S)
    Ssets[s]=arr
if {s:len(v) for s,v in Ssets.items()}!={2:3,3:7,4:1}:raise SystemExit('coisotropic Y-subspace census regression')

def KtoX(k):
    x=0
    if k&1:x^=(1<<0)|(1<<1)
    if k&2:x^=(1<<2)|(1<<3)
    if k&4:x^=(1<<4)|(1<<5)
    for j in range(4):
        if (k>>(3+j))&1:x^=1<<(6+j)
    return x
def TtoX(b):
    x=0
    if b&1:x^=1<<0
    if b&2:x^=1<<2
    if b&4:x^=1<<4
    return x
def rad_dim(P):
    gram=[]
    for x in P:
        row=0
        for j,y in enumerate(P):
            if (x&y).bit_count()%2:row|=1<<j
        gram.append(row)
    return len(P)-rank(gram)
def invariant_P(d):
    seen=set()
    for b in range(4):
        if d-b<b:continue
        for B in rref_subspaces(3,b):
            comp=extend_basis(B,7);qdim=d-2*b
            if not (0<=qdim<=len(comp)):continue
            for Cq in rref_subspaces(len(comp),qdim):
                C=[]
                for cv in Cq:
                    z=0
                    for j,q in enumerate(comp):
                        if (cv>>j)&1:z^=q
                    C.append(z)
                A=list(canon(list(B)+C));acomp=extend_basis(A,7);slots=b*len(acomp)
                for mask in range(1<<slots):
                    lifts=[]
                    for i,bb in enumerate(B):
                        z=0
                        for j,q in enumerate(acomp):
                            if (mask>>(i*len(acomp)+j))&1:z^=q
                        lifts.append(TtoX(bb)^KtoX(z))
                    P=canon([KtoX(a) for a in A]+lifts)
                    if P in seen:raise SystemExit('duplicate invariant P')
                    seen.add(P);yield P,b

target_rad={2:3,3:2,4:1};Pstats={};Ptarget={}
for s,d in ((2,7),(3,6),(4,5)):
    c=Counter();keep=Counter();total=0
    for P,b in invariant_P(d):
        r=rad_dim(P);c[(b,r)]+=1;total+=1
        if r==target_rad[s]:keep[b]+=1
    Pstats[s]={'dimension':d,'total_invariant_P':total,'by_b_rad':{f'{b},{r}':n for (b,r),n in sorted(c.items())}};Ptarget[s]=dict(sorted(keep.items()))
expected_target={2:{0:1,1:146,2:1008},3:{0:112,1:6848,2:17920},4:{0:1792,1:37376,2:27648}}
if Ptarget!=expected_target:raise SystemExit(f'target-rad P census regression {Ptarget}')

def rank1_map_count(m,q):
    if q==0:return 0
    if q==1:return (1<<m)-1
    if q==2:return 3*((1<<m)-1)
    raise ValueError(q)
pre_ct={};post_ct={}
for s,d in ((2,7),(3,6),(4,5)):
    q=4-s;ns=len(Ssets[s]);pre=0;post=0
    for b,np in Ptarget[s].items():
        m=d-b;pre+=ns*np*(1<<(m*q));post+=ns*np*rank1_map_count(m,q)
    pre_ct[s]=pre;post_ct[s]=post
if pre_ct!={2:4939776,3:3591168,4:66816}:raise SystemExit(f'pre-ct census regression {pre_ct}')
if post_ct!={2:365157,3:3417008,4:0}:raise SystemExit(f'post-ct census regression {post_ct}')
if sum(pre_ct.values())!=8597760 or sum(post_ct.values())!=3782165:raise SystemExit('total elementary census regression')

cert={'schema':'STAGE33_07_ELEMENTARY_INDEX512_STRUCTURAL_REDUCTION_V1','source_locks':{'scaled_action_choices_sha256':ACT['canonical_sha256'],'target_v4_fixed_module_sha256':TGT['canonical_sha256']},'ambient_discriminant_module':'(Z/8)^10 direct_sum (Z/16)^4','elementary_H_dimension_f2':9,'elementary_H_order':512,'target_group':'(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4','target_group_filtration':{'Q_order_log2':28,'Q2_order_log2':14,'Q4_order_log2':24,'exponent':8},'target_group_equivalent_conditions_for_elementary_H':['S=H cap Y is coisotropic: S_perp subset S','dim(S)+rad_dim(pr_X H)=5'],'coisotropic_S_counts':{str(s):len(Ssets[s]) for s in (2,3,4)},'target_rad_by_s':{str(k):v for k,v in target_rad.items()},'target_rad_sigma_invariant_P_counts_by_b':{str(s):{str(b):n for b,n in Ptarget[s].items()} for s in (2,3,4)},'universal_ct_half_lift_binary_map_rows':[int(x) for x in L],'universal_ct_choice_count':128,'target_ct_fixed_two_torsion_requires_rank_delta':1,'s4_branch_rejected_by_ct_two_torsion':True,'elementary_candidates_after_target_group_and_cc_stability_by_s':{str(k):v for k,v in pre_ct.items()},'elementary_candidates_after_ct_fixed_two_torsion_by_s':{str(k):v for k,v in post_ct.items()},'elementary_candidates_before_ct_filter_total':8597760,'elementary_candidates_after_ct_fixed_two_torsion_total':3782165,'all_elementary_order512_glue_rejected':False,'actual_index512_glue_identified':False,'next_exact_leaf':'L33-07-CENSUS-3782165-ELEMENTARY-H-BY-FULL-CT-FIXED-TYPE-Q-FORM-AND-V4-CONJUGACY','new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-GLUE-3782165-CENSUS-PLUS-NONELEMENTARY-GLUE','unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,'diagnostic_Pstats':Pstats}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-structural-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'coisotropic_S_counts':cert['coisotropic_S_counts'],'target_P_counts':cert['target_rad_sigma_invariant_P_counts_by_b'],'before_ct':8597760,'after_ct2':3782165,'s4_rejected':True,'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
