#!/usr/bin/env python3
"""Exact balanced (U,R)-orbit subshard for the two heavy k=1 P orbits.

The old one-P-orbit implementation materialized every W for a fixed P before
quotienting by Stab(P). P orbits 5 and 7 are too large for one hosted runner.
This leaf partitions the candidate (U,R) pairs into full Stab(P)-orbits, then
balances those invariant groups across subshards. Because U=W cap Y and
R=pr_X(W) are intrinsic to W, a W orbit cannot cross a subshard boundary.
No arithmetic cc/ct action is loaded or used.
"""
import hashlib,json,os
from collections import Counter
from pathlib import Path
from nonelementary_k1_geometric_support_orbit_common import *

HERE=Path(__file__).resolve().parent
pidx=int(os.environ.get('P_ORBIT_INDEX','5'))
sidx=int(os.environ.get('UR_SHARD_INDEX','0'))
scount=int(os.environ.get('UR_SHARD_COUNT','32'))
if not 0<=pidx<len(P_ORBITS) or not 0<=sidx<scount or scount<1:
    raise SystemExit('invalid balanced support-subshard coordinates')
p,p_orbit,stab=P_ORBITS[pidx]
FULL4=canon(1<<j for j in range(4))

def transport_local_subspace(B,g,offset,width):
    out=[]
    for raw in canon(B):
        v=0
        for old in range(width):
            if (int(raw)>>old)&1:
                new_full=int(g[offset+old])
                if not offset<=new_full<offset+width:
                    raise SystemExit('source symmetry left local coordinate block')
                v|=1<<(new_full-offset)
        out.append(v)
    return canon(out)

def support_setup(p):
    rp=(reduced_from_full(p),);supp=rp[0];t=rank([rp[0]&0b111]);eqrank,ok=eqrc(rp)
    if not ok or eqrank!=0 or t not in (0,1):raise SystemExit('k1 P shape regression')
    pb=canon((int(p),));px=canon(v&X_MASK for v in pb);x0=perp(px,10)
    xe=canon(v for v in range(1,1<<10) if contains(x0,v) and v.bit_count()%2==0)
    dx=canon((1<<(2*j))|(1<<(2*j+1)) for j in range(3) if (supp>>j)&1)
    dy=canon(1<<j for j in range(4) if (supp>>(3+j))&1)
    base=canon(tuple(dx)+(J,))
    return xe,dx,dy,base

xe,dx,dy,base=support_setup(p)

def candidate_pairs():
    out=set()
    for U0 in coisotropic:
        U=canon(U0)
        if any(not contains(U,v) for v in dy):continue
        rdim=8-len(U)
        if len(base)>rdim or rdim>len(xe) or any(not contains(xe,b) for b in base):continue
        for R in ambient_subspaces_containing(base,xe,rdim):
            pair=(U,canon(R))
            if pair in out:raise SystemExit('duplicate candidate (U,R) pair')
            out.add(pair)
    return out

def move_pair(pair,g):
    U,R=pair
    return (transport_local_subspace(U,g,10,4),transport_local_subspace(R,g,0,10))

def pair_work(pair):
    U,R=pair
    extra=complement(base,R);ycomp=complement(U,FULL4)
    return 1<<(len(extra)*len(ycomp))

universe=candidate_pairs();unseen=set(universe);groups=[]
while unseen:
    seed=min(unseen);orb={move_pair(seed,g) for g in stab}
    if not orb<=universe:raise SystemExit('candidate (U,R) universe not P-stabilizer-stable')
    unseen.difference_update(orb)
    groups.append({'key':min(orb),'members':tuple(sorted(orb)),'estimated_graph_masks':sum(pair_work(z) for z in orb)})
groups.sort(key=lambda z:z['key'])
if sum(len(z['members']) for z in groups)!=len(universe):raise SystemExit('candidate (U,R) orbit partition regression')

loads=[0]*scount;assignment=[[] for _ in range(scount)]
for gi in sorted(range(len(groups)),key=lambda i:(-int(groups[i]['estimated_graph_masks']),groups[i]['key'])):
    s=min(range(scount),key=lambda j:(loads[j],j))
    assignment[s].append(gi);loads[s]+=int(groups[gi]['estimated_graph_masks'])
for a in assignment:a.sort()
partition_payload={'p_orbit_index':pidx,'shard_count':scount,'groups':[{'key':g['key'],'members':g['members'],'estimated_graph_masks':g['estimated_graph_masks']} for g in groups],'assignment':assignment}
partition_sha=hashlib.sha256(json.dumps(partition_payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
selected_groups=assignment[sidx]
selected_pairs={pair for gi in selected_groups for pair in groups[gi]['members']}

Ws=set()
for U,R in sorted(selected_pairs):
    for W in graph_skeletons(dx,R,U):
        if not contains(W,p):continue
        if W in Ws:raise SystemExit('duplicate W inside balanced support subshard')
        Ws.add(W)

unseen=set(Ws);records=[];hist=Counter();fixed_total=0
while unseen:
    seed=min(unseen);orb={canon(transport(v,g) for v in seed) for g in stab}
    if not orb<=Ws:raise SystemExit('W orbit crossed balanced (U,R)-orbit subshard boundary')
    unseen.difference_update(orb);rep=min(orb);wsz=len(orb);pair_size=len(p_orbit)*wsz
    pair_stab=sum(1 for g in SYM if transport(p,g)==p and canon(transport(v,g) for v in rep)==rep)
    if pair_size*pair_stab!=288:raise SystemExit('pair orbit-stabilizer regression')
    hist[wsz]+=1;fixed_total+=wsz
    records.append({'P_basis_bits':[p],'W_basis_bits':list(rep),'P_orbit_size':len(p_orbit),'P_stabilizer_order':len(stab),'W_orbit_size_under_P_stabilizer':wsz,'pair_orbit_size':pair_size,'lift_section_fibre_size':64})
records.sort(key=lambda r:r['W_basis_bits'])
if fixed_total!=len(Ws):raise SystemExit('balanced subshard W-orbit coverage regression')

cert={'schema':'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SUPPORT_UR_SUBSHARD_V1','source_2Q_support_sha256':twoq['canonical_sha256'],'arithmetic_generators_used':[],'firewall':'NO_ARITHMETIC_CC_CT_USED__SOURCE_COORDINATE_SYMMETRY_ONLY','p_orbit_index':pidx,'P_basis_bits':[p],'P_orbit_size':len(p_orbit),'P_stabilizer_order':len(stab),'P_orbit_members':list(p_orbit),'ur_shard_index':sidx,'ur_shard_count':scount,'UR_partition_sha256':partition_sha,'total_candidate_UR_pair_count':len(universe),'total_UR_orbit_group_count':len(groups),'selected_UR_orbit_group_indices':selected_groups,'selected_candidate_UR_pair_count':len(selected_pairs),'estimated_graph_masks_total':sum(int(g['estimated_graph_masks']) for g in groups),'estimated_graph_masks_selected':loads[sidx],'fixed_P_support_skeleton_count':len(Ws),'fixed_P_W_orbit_count':len(records),'fixed_P_W_orbit_size_histogram':{str(k):v for k,v in sorted(hist.items())},'full_pair_skeletons_covered':sum(int(r['pair_orbit_size']) for r in records),'representative_lift_sections_for_next_exact_leaf':64*len(records),'weighted_structural_H_covered':64*sum(int(r['pair_orbit_size']) for r in records),'orbit_representatives':records,'all_selected_UR_orbits_exhausted_exactly':True,'full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'next_exact_leaf':'L33-07-MERGE-HEAVY-K1-P-ORBIT-SUPPORT-SUBSHARDS','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
out=HERE/f'nonelementary-k1-geometric-support-ur-subshard-p{pidx}-s{sidx}.json';out.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'p_orbit_index':pidx,'subshard':sidx,'groups':len(selected_groups),'candidate_pairs':len(selected_pairs),'estimated_masks':loads[sidx],'fixed_P_skeletons':len(Ws),'W_orbits':len(records),'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
