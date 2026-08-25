#!/usr/bin/env python3
"""Exact full-cc fixed-subgroup reduction for the 161,792 elementary H census.

For Q=H^perp/H the endpoint cc-fixed subgroup is
  (Z/2)^5 direct_sum (Z/4)^2 direct_sum (Z/8)^3,
so its filtration signature is (log2|K[2]|,log2|K[4]|,log2|K|)=(10,15,18).

This shard does NOT loop over 161,792*1024 scaled cc choices.  Instead it
exhausts every local scaled cc action and proves that the exact finite
relations needed for |Fix(cc,Q)| and |Fix(cc,Q)[4]| are extension-independent.
The remaining census is pure F2 rank arithmetic on each reconstructed H.
"""
import hashlib,itertools,json,math
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
ACT=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
TGT=json.loads((HERE/'target-discriminant-v4-fixed-module.json').read_text())
if ACT['canonical_sha256']!='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20':raise SystemExit('scaled action lock moved')
if TGT['canonical_sha256']!='a396d928ebe2a9dbc7b04aaf38b9fa30c3ef9366b1a2050409195642a690da88':raise SystemExit('target V4 lock moved')

# Importing the preceding exact shard intentionally recomputes the complete
# 423,168 -> 161,792 Q[2] census and exposes its locked F2 reconstruction.
import certify_elementary_index512_q2_v4_reduction as Q2
Q2CERT=json.loads((HERE/'elementary-index512-q2-v4-reduction.json').read_text())
if Q2CERT['canonical_sha256']!='c20300950bd550b448f70db0d89621f65b98765034740bfeb28b992b39a51418':raise SystemExit('Q2 V4 reduction lock moved')
if Q2CERT['target_cc_and_joint_Q2_survivors']!=161792:raise SystemExit('Q2 survivor census regression')

target=(int(TGT['cc_fixed_subgroup']['two_torsion_order_log2']),int(TGT['cc_fixed_subgroup']['four_torsion_order_log2']),int(TGT['cc_fixed_subgroup']['order_log2']))
if target!=(10,15,18):raise SystemExit(f'target cc fixed signature regression {target}')

mods0=[8]*10+[16]*4
piece_coords=[(0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13)]
piece_names=['kb','kb','kb','kc','ka','ka','ka']

def local_relation(mods,A,k4):
    """Image/fiber of x -> (parity(x), (cc-1)x in A[2], 4x in A[2])."""
    counts=Counter()
    for x in itertools.product(*[range(m) for m in mods]):
        y=[(sum(x[i]*A[i][j] for i in range(2))-x[j])%mods[j] for j in range(2)]
        if any(y[j] not in (0,mods[j]//2) for j in range(2)):continue
        p=[x[j]&1 for j in range(2)]
        hn=[1 if y[j] else 0 for j in range(2)]
        z=[]
        if k4:
            zz=[(4*x[j])%mods[j] for j in range(2)]
            if any(zz[j] not in (0,mods[j]//2) for j in range(2)):continue
            z=[1 if zz[j] else 0 for j in range(2)]
        v=sum(p[j]<<j for j in range(2))+sum(hn[j]<<(2+j) for j in range(2))
        if k4:v+=sum(z[j]<<(4+j) for j in range(2))
        counts[v]+=1
    vals=set(counts)
    B=Q2.canon(vals)
    if set(Q2.span(B))!=vals:raise SystemExit('local relation is not an F2 subspace')
    fs=set(counts.values())
    if len(fs)!=1:raise SystemExit('local relation fibers are not uniform')
    return vals,B,next(iter(fs))

def decode(v,k4):
    p=sum(((v>>j)&1)<<j for j in range(2))
    hn=sum(((v>>(2+j))&1)<<j for j in range(2))
    h4=sum(((v>>(4+j))&1)<<j for j in range(2)) if k4 else 0
    return p,hn,h4

def embed(t,coords):
    out=[]
    for v in t:
        z=0
        for j,c in enumerate(coords):
            if (v>>j)&1:z|=1<<c
        out.append(z)
    return tuple(out)

# Exhaust all local scaled cc choices.  For each piece, both the image relation
# and the fiber size are exactly independent of the extension choice.
local_locks={};global_total=[];global_k4=[];fiber_total=1;fiber_k4=1
for pi,(coords,name) in enumerate(zip(piece_coords,piece_names)):
    acts=ACT['pieces'][name]['cc_actions'];mods=[mods0[coords[0]],mods0[coords[1]]]
    rec={}
    for k4 in (False,True):
        rs=[local_relation(mods,A,k4) for A in acts]
        if any(r[0]!=rs[0][0] or r[2]!=rs[0][2] for r in rs[1:]):
            raise SystemExit(f'{name} cc relation depends on scaled extension')
        vals,B,f=rs[0]
        rec['k4' if k4 else 'total']={'relation_size':len(vals),'fiber_size':f,'raw_action_count':len(acts)}
        target_basis=global_k4 if k4 else global_total
        target_basis.extend(embed(decode(v,k4),coords) for v in B)
        if k4:fiber_k4*=f
        else:fiber_total*=f
    local_locks[str(pi)]=rec
if len(global_total)!=14 or len(global_k4)!=14:raise SystemExit('global relation rank-input regression')
if fiber_total!=2**19 or fiber_k4!=2**18:raise SystemExit(f'global relation fiber regression {fiber_total} {fiber_k4}')

# For a relation basis vector (p,h,h4), the conditions p in H^perp and
# h,h4 in H are tested by dot products against bases of H and H^perp.
# If r is the syndrome rank, the allowed relation subspace has dimension 14-r.
# Dividing the numerator by |H|=2^9 gives
#   log2 |Fix(cc,Q)|    = 19+(14-r_total)-9 = 24-r_total,
#   log2 |Fix(cc,Q)[4]|= 18+(14-r_k4)-9   = 23-r_k4.
def syndrome_rank(H,rel,k4):
    H=Q2.canon(H);Hp=Q2.nullspace_basis(H,14);syn=[]
    for p,hn,h4 in rel:
        s=0
        for i,h in enumerate(H):
            if Q2.dot(p,h):s|=1<<i
        for j,q in enumerate(Hp):
            if Q2.dot(hn,q):s|=1<<(9+j)
            if k4 and Q2.dot(h4,q):s|=1<<(14+j)
        syn.append(s)
    return Q2.rank(syn)

def full_cc_signature(H):
    rt=syndrome_rank(H,global_total,False);r4=syndrome_rank(H,global_k4,True)
    return (10,23-r4,24-rt),(rt,r4)

sig_counts=Counter();sig_by_b=Counter();rank_pair_counts=Counter();q2_total=0
for P,b in Q2.invariant_P(6):
    R=Q2.rad_basis(P)
    if len(R)!=2:continue
    NP=Q2.canon([Q2.Ncc(x) for x in P])
    if len(NP)!=b:raise SystemExit('N(P) dimension regression')
    qstart,m,cmap=Q2.quotient_coordinates(P,NP)
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
            q2_total+=1
            sig,(rt,r4)=full_cc_signature(H)
            sig_counts[sig]+=1;sig_by_b[(b,sig)]+=1;rank_pair_counts[(b,rt,r4)]+=1
if q2_total!=161792:raise SystemExit(f'Q2 input reconstruction regression {q2_total}')
expected=Counter({(10,14,16):102912,(10,15,16):40704,(10,15,18):17024,(10,16,18):1152})
if sig_counts!=expected:raise SystemExit(f'full cc signature census regression {sig_counts}')
expected_by_b=Counter({
 (1,(10,14,16)):102912,(1,(10,15,16)):36096,
 (2,(10,15,16)):4608,(2,(10,15,18)):17024,(2,(10,16,18)):1152,
})
if sig_by_b!=expected_by_b:raise SystemExit(f'full cc by-b census regression {sig_by_b}')
after=sig_counts[target]
if after!=17024:raise SystemExit(f'full cc target survivor regression {after}')
if sum(n for (b,s),n in sig_by_b.items() if b==1 and s==target)!=0:raise SystemExit('b=1 unexpectedly survives full cc')

cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_FULL_CC_FIXED_TYPE_REDUCTION_V1',
 'source_locks':{'scaled_action_choices_sha256':ACT['canonical_sha256'],'target_v4_fixed_module_sha256':TGT['canonical_sha256'],'q2_v4_reduction_sha256':Q2CERT['canonical_sha256']},
 'scaled_cc_raw_choice_count':1024,
 'local_total_and_k4_relations_extension_independent_exact':True,
 'global_relation_fiber_log2':{'total':19,'K4':18},
 'fixed_filtration_formula_exact':{'K2_log2':10,'K4_log2':'23-rank_k4_syndrome','K_log2':'24-rank_total_syndrome'},
 'target_cc_fixed_signature_log2_K2_K4_K':list(target),
 'before_full_cc':161792,
 'full_cc_signature_census':{','.join(map(str,k)):v for k,v in sorted(sig_counts.items())},
 'full_cc_signature_census_by_b':{f'{b}|{s[0]},{s[1]},{s[2]}':n for (b,s),n in sorted(sig_by_b.items())},
 'b1_target_survivors':0,
 'b2_target_survivors':after,
 'elementary_candidates_after_full_cc_fixed_type_total':after,
 'all_elementary_order512_glue_rejected':False,'actual_index512_glue_identified':False,'simultaneous_endpoint_cc_ct_action_conjugacy_certified':False,
 'next_exact_leaf':'L33-07-CENSUS-17024-ELEMENTARY-H-BY-FULL-JOINT-V4-FIXED-TYPE-FINITE-Q-FORM-AND-SIMULTANEOUS-V4-CONJUGACY',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-GLUE-17024-FULL-JOINT-Q-V4-CENSUS-PLUS-NONELEMENTARY-GLUE',
 'unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
 'diagnostic_rank_pair_census_by_b':{f'{b},{rt},{r4}':n for (b,rt,r4),n in sorted(rank_pair_counts.items())},
 'local_relation_locks':local_locks,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-full-cc-fixed-type-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':161792,'signature_census':cert['full_cc_signature_census'],'after_full_cc':after,'b1_target':0,'b2_target':after,'relations_extension_independent':True,'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
