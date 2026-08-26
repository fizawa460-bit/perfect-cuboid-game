#!/usr/bin/env python3
"""Reject the retained elementary order-512 glue candidate by exact ct-fixed type.

The previous shard proved that this H gives the correct finite quadratic form.
Here we retain every exact scaled coordinate-K3 action choice from the historical
successful artifact, induce all 2^7 ct choices on H^perp/H, and compare the
fixed subgroup filtration with the exact endpoint ct-fixed subgroup.

This rejects only this explicit H. It does not eliminate every elementary
order-512 glue subgroup and does not identify the actual integral glue.
"""
import hashlib,itertools,json,math
from collections import Counter
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp, smith_normal_form

HERE=Path(__file__).resolve().parent
CAND=json.loads((HERE/'elementary-index512-glue-candidate.json').read_text())
FULLQ=json.loads((HERE/'elementary-index512-full-finite-q-isometry.json').read_text())
ACT=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
TGT=json.loads((HERE/'target-discriminant-v4-fixed-module.json').read_text())

if ACT['canonical_sha256']!='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20': raise SystemExit('scaled action choices lock moved')
if ACT['source_full_certificate_canonical_sha256']!='7227ad24125d83c4172dd4e63aaa6277abf463460b0c1ea294f537c2ec843a10': raise SystemExit('full action certificate lock moved')
if TGT['canonical_sha256']!='a396d928ebe2a9dbc7b04aaf38b9fa30c3ef9366b1a2050409195642a690da88': raise SystemExit('target V4 fixed module lock moved')
if FULLQ['canonical_sha256']!='9a58a145848a8332fd697d852bfa8ab0be99f4b6500352aa99e16ac1b6ec6c1a': raise SystemExit('full finite q-isometry lock moved')
if not FULLQ['full_finite_quadratic_form_isometry_certified']: raise SystemExit('finite q isometry regression')
if CAND['candidate_H_type']!='(Z/2)^9' or CAND['candidate_H_order']!=512: raise SystemExit('candidate H regression')
if any(not ACT['pieces'][k]['all_pairs_cartesian'] for k in ('kb','kc','ka')): raise SystemExit('piece action pair cartesian regression')

mods0=[8]*10+[16]*4
C=[[int(v)&1 for v in r] for r in CAND['candidate_code_basis_f2']]
if len(C)!=9 or any(len(r)!=14 for r in C): raise SystemExit('candidate code shape regression')
def bits(r): return sum((int(v)&1)<<i for i,v in enumerate(r))
def gf2_basis(rows):
    piv={}
    for row in rows:
        x=row if isinstance(row,int) else bits(row)
        while x:
            p=x.bit_length()-1
            if p in piv: x^=piv[p]
            else: piv[p]=x; break
    return list(piv.values())
Cb=gf2_basis(C)
if len(Cb)!=9: raise SystemExit('candidate code rank regression')
perp=[x for x in range(1<<14) if all((x&b).bit_count()%2==0 for b in Cb)]
Pb=gf2_basis(perp)
if len(Pb)!=5: raise SystemExit('Cperp rank regression')
P=[[(b>>i)&1 for i in range(14)] for b in Pb]
pmap={}
for mask in range(1<<5):
    x=0
    for k,b in enumerate(Pb):
        if (mask>>k)&1: x^=b
    pmap[x]=[(mask>>k)&1 for k in range(5)]

rels=[]
for k,p in enumerate(P):
    r=[0]*19; r[k]=2
    for i,b in enumerate(p): r[5+i]-=b
    rels.append(r)
for i,d in enumerate(mods0):
    r=[0]*19; r[5+i]=d//2; rels.append(r)
for c in C:
    r=[0]*19
    for i,b in enumerate(c):
        if b: r[5+i]=mods0[i]//4
    rels.append(r)
R=sp.Matrix(rels)
D,S,T=smith_normal_decomp(R,domain=ZZ)
if S*R*T!=D: raise SystemExit('Smith transform verification failed')
diag=[abs(int(D[i,i])) for i in range(19)]
if diag!=[1]*5+[2]*4+[4]*6+[8]*4: raise SystemExit(f'candidate quotient Smith regression {diag}')
mods=diag[5:]; Ti=T.inv()

def apply(v,M): return [sum(v[i]*M[i][j] for i in range(14))%mods0[j] for j in range(14)]
def express(v):
    pb=bits([x&1 for x in v])
    if pb not in pmap: raise SystemExit('action left Hperp')
    a=pmap[pb]; base=[sum(a[k]*P[k][i] for k in range(5)) for i in range(14)]; z=[]
    for i,d in enumerate(mods0):
        diff=(v[i]-base[i])%d
        if diff%2: raise SystemExit('Hperp coordinate expression parity failure')
        z.append((diff//2)%(d//2))
    return a+z

def induced_smith(M):
    emb=P+[[2 if j==i else 0 for j in range(14)] for i in range(14)]
    A=sp.Matrix([express(apply(v,M)) for v in emb]); N=Ti*A*T
    return [[int(N[i,j])%mods[j-5] for j in range(5,19)] for i in range(5,19)]

pairs=[(0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13)]
def global_action(local):
    M=[[0]*14 for _ in range(14)]
    for i in range(14): M[i][i]=1
    for (a,b),A in zip(pairs,local):
        for ii,u in enumerate((a,b)):
            for jj,v in enumerate((a,b)): M[u][v]=int(A[ii][jj])%mods0[v]
    return M
ctsets=[ACT['pieces']['kb']['ct_actions']]*3+[ACT['pieces']['kc']['ct_actions']]+[ACT['pieces']['ka']['ct_actions']]*3
if [len(x) for x in ctsets]!=[2]*7: raise SystemExit('ct choice cardinality regression')
classes={}
for choice in itertools.product(*ctsets):
    A=induced_smith(global_action(choice)); key=json.dumps(A,separators=(',',':')); classes[key]=classes.get(key,0)+1
if len(classes)!=4 or Counter(classes.values())!=Counter({32:4}): raise SystemExit('induced ct class count regression')

n=14; I=[[1 if i==j else 0 for j in range(n)] for i in range(n)]; Qlog=sum(int(math.log2(m)) for m in mods)
def kernel_pair_log(F,G):
    rows=[]
    for block in (0,1):
        for i,m in enumerate(mods):
            r=[0]*(2*n); r[block*n+i]=m; rows.append(r)
    for i in range(n): rows.append(F[i]+G[i])
    SD=smith_normal_form(sp.Matrix(rows),domain=ZZ); cok=1
    for i in range(2*n):
        d=abs(int(SD[i,i]))
        if not d: raise SystemExit('unexpected free factor in fixed-subgroup coker')
        cok*=d
    k=cok//(2**Qlog)
    if k<=0 or k&(k-1): raise SystemExit('fixed subgroup order is not a 2-power')
    return k.bit_length()-1
def signature(A):
    F=[[A[i][j]-I[i][j] for j in range(n)] for i in range(n)]
    def scalar(q): return [[q if i==j else 0 for j in range(n)] for i in range(n)]
    return (kernel_pair_log(F,scalar(2)),kernel_pair_log(F,scalar(4)),kernel_pair_log(F,scalar(8)))

sig_counts=Counter(); class_records=[]
for key,mult in classes.items():
    A=json.loads(key); sig=signature(A); sig_counts[sig]+=mult
    class_records.append({'multiplicity':mult,'fixed_signature_log2_K2_K4_K':list(sig),'ct_action_smith_coords':A})
target=(int(TGT['ct_fixed_subgroup']['two_torsion_order_log2']),int(TGT['ct_fixed_subgroup']['four_torsion_order_log2']),int(TGT['ct_fixed_subgroup']['order_log2']))
if target!=(13,19,22): raise SystemExit('target ct fixed signature regression')
if any(tuple(r['fixed_signature_log2_K2_K4_K'])==target for r in class_records): raise SystemExit('unexpected surviving ct class')
if sig_counts!=Counter({(14,20,24):32,(14,19,22):64,(14,20,22):32}): raise SystemExit(f'candidate ct signature census regression {sig_counts}')

cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_CANDIDATE_V4_REJECTION_V1',
 'source_locks':{'candidate_sha256':CAND['canonical_sha256'],'full_finite_q_isometry_sha256':FULLQ['canonical_sha256'],'scaled_action_choices_sha256':ACT['canonical_sha256'],'target_v4_fixed_module_sha256':TGT['canonical_sha256']},
 'candidate_H_type':CAND['candidate_H_type'],'candidate_H_order':512,
 'candidate_discriminant_group':'(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4','full_finite_quadratic_form_isometry_certified':True,
 'scaled_ct_raw_choice_count':128,'scaled_ct_induced_distinct_class_count':4,'scaled_ct_class_multiplicity_each':32,
 'candidate_ct_fixed_signature_census':{'14,20,24':32,'14,19,22':64,'14,20,22':32},'target_ct_fixed_signature_log2_K2_K4_K':list(target),
 'candidate_ct_two_torsion_log2_always':14,'target_ct_two_torsion_log2':13,'ct_fixed_subgroup_type_mismatch_exact':True,
 'simultaneous_endpoint_cc_ct_action_conjugacy_possible':False,'retained_elementary_H0_rejected':True,'all_elementary_order512_glue_rejected':False,
 'actual_index512_glue_identified':False,'candidate_promoted_to_endpoint_T_lattice':False,
 'new_residual_kernel':'R33-BR2A-INDEX512-GLUE-EMBEDDING-SEARCH-AFTER-ELEMENTARY-H0-REJECTION',
 'next_exact_leaf':'L33-07-ENUMERATE-ELEMENTARY-ORDER512-H-STABLE-UNDER-A2-AND-MATCH-ENDPOINT-SMITH-Q-V4',
 'unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
 'class_records':class_records,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-candidate-v4-rejection.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'ct_raw_choices':128,'ct_induced_classes':4,'signature_census':cert['candidate_ct_fixed_signature_census'],'target_signature':list(target),'retained_H0_rejected':True,'all_elementary_rejected':False,'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
