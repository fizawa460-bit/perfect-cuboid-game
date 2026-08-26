#!/usr/bin/env python3
"""Exact k=1 cc-compatible skeleton census after Q[2]/2Q support.

The preceding support reductions leave 1,311,205,952 structural H of type
Z/4 +(Z/2)^7.  Enumerating all 20,487,593 support-admissible (P,W) skeletons
is unnecessary.  In the Q[2]+2Q graph parameterization, the common cc mod-two
involution sigma swaps the two coordinates in each Kb pair and fixes Kc/Ka.

For W=U plus graph(phi:R->Y/U), cc stability is exactly

  sigma(R)=R,  phi((sigma-I)R)=0,

in addition to the already-fixed phi(D_X)=0 and phi(j)=lambda_U.  This leaf
enumerates all and only those cc-compatible graph skeletons directly.  There
are exactly 105,049, carrying 6,723,136 lift sections (64 per skeleton).
The same order-288 integral source symmetry reduces them to 4,595 skeleton
orbits.  No fast/canonical pruning is used.

This remains only a mod-two action-stability/symmetry compression.  Integral
cc/ct, full Q[4], finite-q, actual glue, HS, endpoint and theorem credit remain
false.
"""
import hashlib,itertools,json,runpy
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
ACTION_LOCK='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20'
base_ns=runpy.run_path(str(HERE/'certify_nonelementary_sign_q2_structural_reduction.py'))
q8_ns=runpy.run_path(str(HERE/'certify_nonelementary_target_q8_exponent_reduction.py'))
runpy.run_path(str(HERE/'certify_nonelementary_k12_q2_support_reduction.py'))
runpy.run_path(str(HERE/'certify_nonelementary_k12_2q_support_reduction.py'))
twoq=json.loads((HERE/'nonelementary-k12-2q-support-reduction.json').read_text())
actions=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
if actions.get('canonical_sha256')!=ACTION_LOCK:raise SystemExit('action lock moved')
if twoq['summary_by_number_of_Z4_factors']['1']['structural_H_after_endpoint_2Q_support_necessary_condition']!=1311205952:raise SystemExit('k1 predecessor moved')
subspaces=base_ns['subspaces'];span=base_ns['span'];rank=base_ns['rank'];canon=base_ns['canon'];red_to_full=base_ns['red_to_full'];eqrc=base_ns['eq_rank_and_consistency'];cois=q8_ns['coisotropic']
X_MASK=(1<<10)-1;J=X_MASK

def contains(B,x):return rank(list(B)+[x])==len(B)
def complement(base,whole):
    cur=list(canon(base));out=[]
    for v in canon(whole):
        if rank(cur+[v])>len(cur):cur.append(v);out.append(v)
    return tuple(out)
def perp(B,n):return canon(x for x in range(1,1<<n) if all((x&b).bit_count()%2==0 for b in B))
def rref_subspaces(n,k):
    if k==0:yield ();return
    for piv in itertools.combinations(range(n),k):
        ps=set(piv);free=[j for j in range(n) if j not in ps];slots=[(r,j) for j in free for r,p in enumerate(piv) if p<j]
        for mask in range(1<<len(slots)):
            rows=[1<<p for p in piv]
            for z,(r,j) in enumerate(slots):
                if (mask>>z)&1:rows[r]|=1<<j
            yield canon(rows)
def ambient_subspaces_containing(base,ambient,target):
    base=canon(base);qb=complement(base,ambient);need=target-len(base)
    for abstract in rref_subspaces(len(qb),need):
        lifted=[]
        for row in abstract:
            v=0
            for j,b in enumerate(qb):
                if (row>>j)&1:v^=b
            lifted.append(v)
        yield canon(base+tuple(lifted))
def lambda_rep(U):
    T=perp(U,4);sol=[]
    for y in range(16):
        if all(((y&t).bit_count()&1)==((t.bit_count()//2)&1) for t in [0]+[x for x in range(1,16) if contains(T,x)]):sol.append(y)
    if len(sol)!=(1<<len(U)):raise SystemExit('lambda coset regression')
    return min(sol)
permX=list(range(10))
for a,b in ((0,1),(2,3),(4,5)):permX[a],permX[b]=b,a
def tx(v):
    out=0
    for old,new in enumerate(permX):
        if (v>>old)&1:out|=1<<new
    return out
def N(v):return tx(v)^v
def invariant(R):return canon(tx(v) for v in R)==canon(R)
def graph_skeletons_cc(dx,R,U):
    y0=lambda_rep(U);NR=canon(N(v) for v in R);zero=canon(tuple(dx)+NR)
    if contains(zero,J):raise SystemExit('j unexpectedly in forced-zero graph domain')
    fixed=canon(zero+(J,));extra=complement(fixed,R);ycomp=complement(U,canon(1<<j for j in range(4)))
    slots=[(i,j) for i in range(len(extra)) for j in range(len(ycomp))]
    for mask in range(1<<len(slots)):
        rows=list(dx)+[u<<10 for u in U]+[J|(y0<<10)]
        for v in NR:
            if not contains(dx,v):rows.append(v)
        for i,x in enumerate(extra):
            y=0
            for bit,(ii,j) in enumerate(slots):
                if ii==i and (mask>>bit)&1:y^=ycomp[j]
            rows.append(x|(y<<10))
        W=canon(rows)
        if len(W)!=8:raise SystemExit('k1 W rank regression')
        yield W

skeletons=set();profile=Counter()
for rp in sorted(subspaces[1]):
    supp=0
    for v in span(rp):supp|=v
    if supp.bit_count()>8:continue
    t=rank([v&0b111 for v in rp]);eqrank,ok=eqrc(rp)
    if not ok or t>2 or eqrank!=0:continue
    p=canon(red_to_full(v) for v in rp);px=canon(v&X_MASK for v in p);x0=perp(px,10)
    xe=canon(v for v in [x for x in range(1,1<<10) if contains(x0,x)] if v.bit_count()%2==0)
    dx=canon((1<<(2*j))|(1<<(2*j+1)) for j in range(3) if (supp>>j)&1);dy=canon(1<<j for j in range(4) if (supp>>(3+j))&1);base=canon(tuple(dx)+(J,))
    for U in cois:
        if any(not contains(U,v) for v in dy):continue
        rdim=8-len(U)
        if len(base)>rdim or any(not contains(xe,b) for b in base):continue
        for R in ambient_subspaces_containing(base,xe,rdim):
            if not invariant(R):continue
            for W in graph_skeletons_cc(dx,R,U):
                if any(not contains(W,v) for v in p):raise SystemExit('P not in W')
                key=(p,W)
                if key in skeletons:raise SystemExit('duplicate k1 cc skeleton')
                skeletons.add(key);profile[t]+=1
if len(skeletons)!=105049 or profile!=Counter({0:67733,1:37316}):raise SystemExit(f'k1 cc skeleton regression {len(skeletons)} {profile}')
structural=len(skeletons)*64
if structural!=6723136:raise SystemExit('k1 cc structural-H regression')

# Direct mod-two stability regression.
perm=list(range(14))
for a,b in ((0,1),(2,3),(4,5)):perm[a],perm[b]=b,a
def transport(v,p):
    out=0
    for old,new in enumerate(p):
        if (v>>old)&1:out|=1<<new
    return out
if any(canon(transport(v,perm) for v in W)!=W for _,W in skeletons):raise SystemExit('direct cc stability regression')

# Same integral source symmetry as k3/k2.
def symmetries():
    for kbp in itertools.permutations(range(3)):
        for sm in range(8):
            for kap in itertools.permutations(range(3)):
                p=list(range(14))
                for old in range(3):
                    new=kbp[old];sw=(sm>>old)&1;p[2*old]=2*new+sw;p[2*old+1]=2*new+(1-sw)
                p[6]=6;p[10]=10
                for old in range(3):new=kap[old];p[7+old]=7+new;p[11+old]=11+new
                yield tuple(p)
sym=tuple(symmetries())
if len(sym)!=288 or len(set(sym))!=288:raise SystemExit('symmetry order regression')
def move(s,g):p,W=s;return canon(transport(v,g) for v in p),canon(transport(v,g) for v in W)
unseen=set(skeletons);sizes=[];reps=[]
while unseen:
    seed=min(unseen);orb={move(seed,g) for g in sym}
    if not orb<=skeletons:raise SystemExit('k1 cc skeleton universe not symmetry-stable')
    unseen.difference_update(orb);rep=min(orb);sizes.append(len(orb));reps.append({'P_basis_bits':list(rep[0]),'W_basis_bits':list(rep[1]),'orbit_size':len(orb)})
hist=Counter(sizes);expected=Counter({18:2028,36:1512,9:846,3:65,72:54,6:50,12:16,144:12,24:8,1:4})
if len(sizes)!=4595 or hist!=expected or sum(sizes)!=105049:raise SystemExit(f'k1 orbit regression {len(sizes)} {hist}')
cert={'schema':'STAGE33_07_NONELEMENTARY_K1_Q2_2Q_CC_ORBITS_V1','source_2Q_support_sha256':twoq['canonical_sha256'],'source_retained_action_choices_sha256':ACTION_LOCK,'abstract_H_type':'Z/4 direct_sum (Z/2)^7','direct_cc_compatible_P_W_skeleton_count':len(skeletons),'cc_skeleton_profile_by_t':{str(k):v for k,v in sorted(profile.items())},'structural_H_count_after_forced_cc_mod2':structural,'lift_section_count_per_skeleton':64,'symmetry_order':288,'exact_skeleton_orbit_count':len(sizes),'orbit_size_histogram':{str(k):v for k,v in sorted(hist.items())},'orbit_size_sum':sum(sizes),'orbit_representatives':reps,'fast_or_heuristic_traversal_used':False,'surviving_lift_sections_quotiented_or_rejected':False,'full_Q4_condition_certified':False,'integral_cc_ct_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'next_exact_leaf':'L33-07-K1-INTEGRAL-CC-CT-AFFINE-FILTER-OVER-4595-SKELETON-ORBITS','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();(HERE/'nonelementary-k1-q2-2q-cc-orbits.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'cc_skeletons':len(skeletons),'structural_H_after_cc_mod2':structural,'skeleton_orbits':len(sizes),'certificate_sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
