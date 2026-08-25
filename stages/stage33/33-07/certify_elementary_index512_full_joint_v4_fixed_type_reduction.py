#!/usr/bin/env python3
"""Exact full joint-V4 fixed-subgroup reduction after the full-cc census.

The endpoint joint fixed subgroup is
  (Z/2)^5 direct_sum (Z/4)^3 direct_sum Z/8,
with filtration signature (9,13,14).

For every allowed local (cc,ct) scaled-action pair this shard enumerates the
exact relation carried by x -> (parity(x),(cc-1)x,(ct-1)x,4x).  The raw
131,072 global action-pair choices collapse to 64 exact relation-pair types.
Those 64 types are then tested on every elementary H surviving the full-cc
fixed subgroup filter.
"""
import hashlib,itertools,json
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
ACT=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
TGT=json.loads((HERE/'target-discriminant-v4-fixed-module.json').read_text())
if ACT['canonical_sha256']!='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20':raise SystemExit('scaled action lock moved')
if TGT['canonical_sha256']!='a396d928ebe2a9dbc7b04aaf38b9fa30c3ef9366b1a2050409195642a690da88':raise SystemExit('target V4 lock moved')
for k in ('kb','kc','ka'):
    if not ACT['pieces'][k]['all_pairs_cartesian']:raise SystemExit(f'{k} action pairs are not cartesian')

# The preceding shard intentionally recomputes all prerequisites and exposes
# the exact H reconstruction and full-cc relation test.
import certify_elementary_index512_full_cc_fixed_type_reduction as CC
Q2=CC.Q2
FULLCC=json.loads((HERE/'elementary-index512-full-cc-fixed-type-reduction.json').read_text())
if FULLCC['schema']!='STAGE33_07_ELEMENTARY_INDEX512_FULL_CC_FIXED_TYPE_REDUCTION_V1':raise SystemExit('full cc schema regression')
if FULLCC['elementary_candidates_after_full_cc_fixed_type_total']!=17024:raise SystemExit('full cc survivor regression')

target=(int(TGT['joint_v4_fixed_subgroup']['two_torsion_order_log2']),int(TGT['joint_v4_fixed_subgroup']['four_torsion_order_log2']),int(TGT['joint_v4_fixed_subgroup']['order_log2']))
if target!=(9,13,14):raise SystemExit(f'target joint V4 signature regression {target}')

mods0=[8]*10+[16]*4
piece_coords=[(0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13)]
piece_names=['kb','kb','kb','kc','ka','ka','ka']

def local_joint_relation(mods,Ac,At,k4):
    counts=Counter()
    for x in itertools.product(*[range(m) for m in mods]):
        yc=[(sum(x[i]*Ac[i][j] for i in range(2))-x[j])%mods[j] for j in range(2)]
        yt=[(sum(x[i]*At[i][j] for i in range(2))-x[j])%mods[j] for j in range(2)]
        if any(yc[j] not in (0,mods[j]//2) for j in range(2)):continue
        if any(yt[j] not in (0,mods[j]//2) for j in range(2)):continue
        p=[x[j]&1 for j in range(2)]
        hc=[1 if yc[j] else 0 for j in range(2)]
        ht=[1 if yt[j] else 0 for j in range(2)]
        v=sum(p[j]<<j for j in range(2))+sum(hc[j]<<(2+j) for j in range(2))+sum(ht[j]<<(4+j) for j in range(2))
        if k4:
            z=[(4*x[j])%mods[j] for j in range(2)]
            if any(z[j] not in (0,mods[j]//2) for j in range(2)):continue
            h4=[1 if z[j] else 0 for j in range(2)]
            v+=sum(h4[j]<<(6+j) for j in range(2))
        counts[v]+=1
    vals=frozenset(counts);B=Q2.canon(vals)
    if set(Q2.span(B))!=set(vals):raise SystemExit('joint local relation is not an F2 subspace')
    fs=set(counts.values())
    if len(fs)!=1:raise SystemExit('joint local relation fibers are not uniform')
    return vals,B,next(iter(fs))

def decode(v,k4):
    p=sum(((v>>j)&1)<<j for j in range(2))
    hc=sum(((v>>(2+j))&1)<<j for j in range(2))
    ht=sum(((v>>(4+j))&1)<<j for j in range(2))
    h4=sum(((v>>(6+j))&1)<<j for j in range(2)) if k4 else 0
    return p,hc,ht,h4

def embed(t,coords):
    out=[]
    for v in t:
        z=0
        for j,c in enumerate(coords):
            if (v>>j)&1:z|=1<<c
        out.append(z)
    return tuple(out)

# Classify correlated local relation pairs (total,K4), retaining multiplicity
# among the raw local action pairs.
local_types=[];local_type_diagnostics={}
for pi,(coords,name) in enumerate(zip(piece_coords,piece_names)):
    mods=[mods0[coords[0]],mods0[coords[1]]]
    pair_records=[]
    for Ac in ACT['pieces'][name]['cc_actions']:
        for At in ACT['pieces'][name]['ct_actions']:
            rt=local_joint_relation(mods,Ac,At,False);r4=local_joint_relation(mods,Ac,At,True)
            pair_records.append((rt,r4))
    C=Counter((r[0][0],r[0][2],r[1][0],r[1][2]) for r in pair_records)
    types=[]
    for (vt,ft,v4,f4),mult in C.items():
        Bt=Q2.canon(vt);B4=Q2.canon(v4)
        types.append({'total_vals':vt,'total_basis':Bt,'total_fiber':ft,'k4_vals':v4,'k4_basis':B4,'k4_fiber':f4,'multiplicity':mult})
    types.sort(key=lambda z:(tuple(sorted(z['total_vals'])),tuple(sorted(z['k4_vals']))))
    local_types.append(types)
    local_type_diagnostics[str(pi)]={'piece':name,'raw_pair_count':len(pair_records),'relation_pair_type_count':len(types),'multiplicities':[z['multiplicity'] for z in types]}
if [len(x) for x in local_types]!=[4,4,4,1,1,1,1]:raise SystemExit('local joint relation-pair type count regression')
if any(sorted(local_type_diagnostics[str(i)]['multiplicities'])!=[2,2,2,2] for i in range(3)):raise SystemExit('Kb local pair multiplicity regression')
if any(local_type_diagnostics[str(i)]['multiplicities']!=[4] for i in range(3,7)):raise SystemExit('mixed local pair multiplicity regression')

# Build all 64 global relation-pair types.  Each has raw multiplicity 2048,
# accounting for all 64*2048=131072 exact global scaled (cc,ct) choices.
global_types=[]
for choice in itertools.product(*[range(len(x)) for x in local_types]):
    Bt=[];B4=[];mult=1;ft=1;f4=1
    for pi,ti in enumerate(choice):
        z=local_types[pi][ti];coords=piece_coords[pi]
        Bt.extend(embed(decode(v,False),coords) for v in z['total_basis'])
        B4.extend(embed(decode(v,True),coords) for v in z['k4_basis'])
        mult*=z['multiplicity'];ft*=z['total_fiber'];f4*=z['k4_fiber']
    if len(Bt)!=14 or len(B4)!=14:raise SystemExit('global joint relation basis length regression')
    if ft!=2**14 or f4!=2**14:raise SystemExit('global joint relation fiber regression')
    global_types.append((choice,Bt,B4,mult))
if len(global_types)!=64:raise SystemExit('global joint relation type count regression')
if Counter(z[3] for z in global_types)!=Counter({2048:64}):raise SystemExit('global joint raw multiplicity regression')
if sum(z[3] for z in global_types)!=131072:raise SystemExit('global joint raw action-pair count regression')

def syndrome_rank(H,rel,k4):
    H=Q2.canon(H);Hp=Q2.nullspace_basis(H,14);syn=[]
    for p,hc,ht,h4 in rel:
        s=0
        for i,h in enumerate(H):
            if Q2.dot(p,h):s|=1<<i
        for j,q in enumerate(Hp):
            if Q2.dot(hc,q):s|=1<<(9+j)
            if Q2.dot(ht,q):s|=1<<(14+j)
            if k4 and Q2.dot(h4,q):s|=1<<(19+j)
        syn.append(s)
    return Q2.rank(syn)

def joint_signature(H,Bt,B4):
    rt=syndrome_rank(H,Bt,False);r4=syndrome_rank(H,B4,True)
    # Both total and K4 joint relations have fiber 2^14 and dimension 14.
    # Quotient by H of order 2^9 gives 19-rank.
    return (9,19-r4,19-rt)

before=0;survivors=0;match_type_count_per_H=Counter();profile_per_H=Counter();aggregate_type_signatures=Counter()
for P,b in Q2.invariant_P(6):
    R=Q2.rad_basis(P)
    if len(R)!=2:continue
    NP=Q2.canon([Q2.Ncc(x) for x in P]);qstart,m,cmap=Q2.quotient_coordinates(P,NP)
    allowed_t=[t for t in Q2.EVEN_T if Q2.contains(P,Q2.jt(t))]
    if not allowed_t:continue
    dmask=[dm for dm in range(1,1<<m) if any((((cmap[r]>>qstart)&dm).bit_count()&1) for r in R)]
    K=Q2.canon([p for p in Q2.span(P) if Q2.Ncc(p)==0])
    Pb=list(Q2.canon(P));pc=[cmap[p]>>qstart for p in Pb];kc=[cmap[k]>>qstart for k in K]
    for t in allowed_t:
        J=Q2.jt(t);sb=Q2.Sbasis(t);ybit=1<<(10+((t&-t).bit_length()-1))
        pell=[Q2.dot(p,J) for p in Pb];kell=[Q2.dot(k,J) for k in K]
        for dm in dmask:
            lp=[e^((u&dm).bit_count()&1) for e,u in zip(pell,pc)]
            H=Q2.canon([p|(ybit if v else 0) for p,v in zip(Pb,lp)]+list(sb))
            HD=list(H)+list(Q2.D);rHD=Q2.rank(HD);kN=14-rHD
            lk=[e^((u&dm).bit_count()&1) for e,u in zip(kell,kc)]
            Hsig=[k|(ybit if v else 0) for k,v in zip(K,lk)]+list(sb)
            FH=[Q2.Fcc(h) for h in Hsig]
            rcc=Q2.rank(HD+FH)-rHD;ccfix=len(Hsig)-rcc+kN
            db=[((u&dm).bit_count()&1) for u in kc]+[0]*len(sb)
            aug=[FH[i]|(db[i]<<14) for i in range(len(Hsig))]
            rjoint=Q2.rank(HD+aug)-rHD;jointfix=len(Hsig)-rjoint+kN
            if (ccfix,jointfix)!=(10,9):continue
            if CC.full_cc_signature(H)[0]!=(10,15,18):continue
            before+=1
            C=Counter(joint_signature(H,Bt,B4) for _,Bt,B4,_ in global_types)
            for sig,n in C.items():aggregate_type_signatures[sig]+=n
            profile=tuple(sorted((sig,n) for sig,n in C.items()))
            profile_per_H[profile]+=1
            nm=C[target];match_type_count_per_H[nm]+=1
            if nm:survivors+=1
if before!=17024:raise SystemExit(f'full cc input reconstruction regression {before}')
expected_match=Counter({64:8192,0:8832})
if match_type_count_per_H!=expected_match:raise SystemExit(f'joint match-type census regression {match_type_count_per_H}')
expected_profiles=Counter({
 (((9,13,14),64),):8192,
 (((9,13,13),32),((9,14,14),32)):5760,
 (((9,14,14),64),):3072,
})
if profile_per_H!=expected_profiles:raise SystemExit(f'joint per-H profile regression {profile_per_H}')
if aggregate_type_signatures!=Counter({(9,13,14):524288,(9,14,14):380928,(9,13,13):184320}):raise SystemExit(f'joint aggregate type census regression {aggregate_type_signatures}')
if survivors!=8192:raise SystemExit(f'joint survivor regression {survivors}')

cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_FULL_JOINT_V4_FIXED_TYPE_REDUCTION_V1',
 'source_locks':{'scaled_action_choices_sha256':ACT['canonical_sha256'],'target_v4_fixed_module_sha256':TGT['canonical_sha256'],'full_cc_schema':FULLCC['schema']},
 'raw_global_scaled_cc_ct_pair_count':131072,
 'global_joint_relation_pair_type_count':64,
 'raw_multiplicity_per_relation_pair_type':2048,
 'joint_relation_fiber_log2':{'total':14,'K4':14},
 'target_joint_fixed_signature_log2_K2_K4_K':list(target),
 'before_full_joint_v4':before,
 'matching_relation_type_count_per_H_census':{str(k):v for k,v in sorted(match_type_count_per_H.items())},
 'per_H_relation_signature_profiles':{
   'target_all_64':8192,
   'split_32_K13_total13__32_K14_total14':5760,
   'K14_total14_all_64':3072,
 },
 'aggregate_relation_type_signature_census':{','.join(map(str,k)):v for k,v in sorted(aggregate_type_signatures.items())},
 'elementary_candidates_after_full_joint_v4_fixed_type_total':survivors,
 'survivors_match_target_joint_type_for_all_131072_raw_action_pairs':True,
 'all_elementary_order512_glue_rejected':False,'actual_index512_glue_identified':False,'simultaneous_endpoint_cc_ct_action_conjugacy_certified':False,
 'next_exact_leaf':'L33-07-CENSUS-8192-ELEMENTARY-H-BY-FINITE-QUADRATIC-FORM-AND-SIMULTANEOUS-ENDPOINT-V4-CONJUGACY',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-GLUE-8192-FINITE-Q-V4-CONJUGACY-CENSUS-PLUS-NONELEMENTARY-GLUE',
 'unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
 'local_relation_pair_type_diagnostics':local_type_diagnostics,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-full-joint-v4-fixed-type-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':before,'raw_action_pairs':131072,'relation_pair_types':64,'match_type_count_per_H':cert['matching_relation_type_count_per_H_census'],'after_full_joint':survivors,'survivors_match_all_raw_pairs':True,'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
