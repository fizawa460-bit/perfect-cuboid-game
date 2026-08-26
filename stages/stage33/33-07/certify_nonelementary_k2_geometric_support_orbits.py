#!/usr/bin/env python3
"""Exact pure-geometric orbit census for k=2 after Q[2]/2Q support.

Materializes all 88,288 support-admissible (P,W) skeletons of
H ~= (Z/4)^2 +(Z/2)^5 and quotients only by the order-288 integral coordinate
symmetry preserving the seven K3 source pieces.  No arithmetic cc/ct action is
loaded or used.
"""
import hashlib
import itertools
import json
import runpy
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
Q8_LOCK='4a5c84ad765f93442f08991ffdcea0bab6f1ae5a3ab6561157201bba262f75ee'
X_MASK=(1<<10)-1
J=X_MASK

base_ns=runpy.run_path(str(HERE/'certify_nonelementary_sign_q2_structural_reduction.py'))
q8_ns=runpy.run_path(str(HERE/'certify_nonelementary_target_q8_exponent_reduction.py'))
runpy.run_path(str(HERE/'certify_nonelementary_k12_q2_support_reduction.py'))
runpy.run_path(str(HERE/'certify_nonelementary_k12_2q_support_reduction.py'))
twoq=json.loads((HERE/'nonelementary-k12-2q-support-reduction.json').read_text())
q8=json.loads((HERE/'nonelementary-target-q8-exponent-reduction.json').read_text())
if q8.get('canonical_sha256')!=Q8_LOCK:raise SystemExit('Q8 source lock moved')
if twoq['summary_by_number_of_Z4_factors']['2']['structural_H_after_endpoint_2Q_support_necessary_condition']!=988553216:
    raise SystemExit('k2 2Q predecessor total moved')

subspaces=base_ns['subspaces'];span=base_ns['span'];rank=base_ns['rank'];canon=base_ns['canon'];red_to_full=base_ns['red_to_full'];eqrc=base_ns['eq_rank_and_consistency']
coisotropic_y=q8_ns['coisotropic']

def contains(B,x):return rank(list(B)+[x])==len(B)
def complement(base,whole):
    cur=list(canon(base));out=[]
    for v in canon(whole):
        if rank(cur+[v])>len(cur):cur.append(v);out.append(v)
    return tuple(out)
def perp(B,n):return canon(x for x in range(1,1<<n) if all((x&b).bit_count()%2==0 for b in B))
def rref_subspaces(n,k):
    if k==0:yield ();return
    for pivots in itertools.combinations(range(n),k):
        ps=set(pivots);free=[j for j in range(n) if j not in ps]
        slots=[(r,j) for j in free for r,p in enumerate(pivots) if p<j]
        for mask in range(1<<len(slots)):
            rows=[1<<p for p in pivots]
            for z,(r,j) in enumerate(slots):
                if (mask>>z)&1:rows[r]|=1<<j
            yield canon(rows)
def ambient_subspaces_containing(base,ambient,target_dim):
    base=canon(base);qb=complement(base,ambient);need=target_dim-len(base)
    for abstract in rref_subspaces(len(qb),need):
        lifted=[]
        for row in abstract:
            v=0
            for j,b in enumerate(qb):
                if (row>>j)&1:v^=b
            lifted.append(v)
        result=canon(base+tuple(lifted))
        if len(result)!=target_dim:raise SystemExit('ambient lift rank regression')
        yield result
def lambda_coset_representative(U):
    T=perp(U,4);sol=[]
    for y in range(16):
        if all(((y&t).bit_count()&1)==((t.bit_count()//2)&1) for t in [0]+[x for x in range(1,16) if contains(T,x)]):sol.append(y)
    if len(sol)!=(1<<len(U)):raise SystemExit('lambda coset regression')
    return min(sol)
def graph_skeletons(dx,R,U):
    y0=lambda_coset_representative(U);domain_base=canon(tuple(dx)+(J,));extra=complement(domain_base,R);ycomp=complement(U,canon(1<<j for j in range(4)))
    slots=[(i,j) for i in range(len(extra)) for j in range(len(ycomp))]
    for mask in range(1<<len(slots)):
        rows=list(dx)+[u<<10 for u in U]+[J|(y0<<10)]
        for i,x in enumerate(extra):
            y=0
            for bit,(ii,j) in enumerate(slots):
                if ii==i and (mask>>bit)&1:y^=ycomp[j]
            rows.append(x|(y<<10))
        W=canon(rows)
        if len(W)!=7:raise SystemExit('k2 W rank regression')
        yield W

skeletons=set();profile=Counter();p_eqrank={};p_t={}
for reduced_p in sorted(subspaces[2]):
    supp=0
    for v in span(reduced_p):supp|=v
    if supp.bit_count()>7:continue
    t=rank([v&0b111 for v in reduced_p]);eqrank,ok=eqrc(reduced_p)
    if not ok or t>2:continue
    p=canon(red_to_full(v) for v in reduced_p);p_eqrank[p]=eqrank;p_t[p]=t
    px=canon(v&X_MASK for v in p);x0=perp(px,10)
    xe=canon(v for v in range(1,1<<10) if contains(x0,v) and v.bit_count()%2==0)
    dx=canon((1<<(2*j))|(1<<(2*j+1)) for j in range(3) if (supp>>j)&1)
    dy=canon(1<<j for j in range(4) if (supp>>(3+j))&1);base=canon(tuple(dx)+(J,))
    for U in coisotropic_y:
        if any(not contains(U,v) for v in dy):continue
        rdim=7-len(U)
        if len(base)>rdim or any(not contains(xe,b) for b in base):continue
        for R in ambient_subspaces_containing(base,xe,rdim):
            for W in graph_skeletons(dx,R,U):
                if any(not contains(W,v) for v in p):raise SystemExit('P not contained in W')
                key=(p,W)
                if key in skeletons:raise SystemExit('duplicate k2 skeleton')
                skeletons.add(key);profile[(t,eqrank)]+=1
if len(skeletons)!=88288 or profile!=Counter({(1,1):53370,(0,0):32385,(2,1):2533}):
    raise SystemExit(f'k2 support skeleton regression {len(skeletons)} {profile}')
weighted=sum(n*(1<<(14-r)) for (_,r),n in profile.items())
if weighted!=988553216:raise SystemExit('k2 weighted-H reconstruction regression')

# Source-coordinate symmetry only: S3(Kb)*(S2)^3*S3(Ka), Kc fixed.
def symmetries():
    for kb_perm in itertools.permutations(range(3)):
        for swapmask in range(8):
            for ka_perm in itertools.permutations(range(3)):
                p=list(range(14))
                for old in range(3):
                    new=kb_perm[old];sw=(swapmask>>old)&1
                    p[2*old]=2*new+sw;p[2*old+1]=2*new+(1-sw)
                p[6]=6;p[10]=10
                for old in range(3):
                    new=ka_perm[old];p[7+old]=7+new;p[11+old]=11+new
                yield tuple(p)
sym=tuple(symmetries())
if len(sym)!=288 or len(set(sym))!=288:raise SystemExit('symmetry order regression')
def transport(v,g):
    out=0
    for old,new in enumerate(g):
        if (int(v)>>old)&1:out|=1<<new
    return out
def move(s,g):
    p,W=s;return canon(transport(v,g) for v in p),canon(transport(v,g) for v in W)

unseen=set(skeletons);sizes=[];reps=[];orbit_profile=Counter()
while unseen:
    seed=min(unseen);orb={move(seed,g) for g in sym}
    if not orb<=skeletons:raise SystemExit('pure k2 support universe not symmetry-stable')
    unseen.difference_update(orb);rep=min(orb);p=rep[0];size=len(orb)
    sizes.append(size);orbit_profile[(p_t[p],p_eqrank[p],size)]+=1
    reps.append({'P_basis_bits':list(p),'W_basis_bits':list(rep[1]),'orbit_size':size,'t':p_t[p],'section_equation_rank':p_eqrank[p],'lift_section_fibre_size':1<<(14-p_eqrank[p])})
if sum(sizes)!=88288:raise SystemExit('orbit size coverage regression')
rep_sections=sum(r['lift_section_fibre_size'] for r in reps)
weighted_orbit=sum(r['orbit_size']*r['lift_section_fibre_size'] for r in reps)
if weighted_orbit!=988553216:raise SystemExit('orbit weighted-H reconstruction regression')
reps.sort(key=lambda r:(r['P_basis_bits'],r['W_basis_bits']))
cert={
 'schema':'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_SUPPORT_ORBITS_V1',
 'source_2Q_support_sha256':twoq['canonical_sha256'],'arithmetic_generators_used':[],
 'firewall':'NO_ARITHMETIC_CC_CT_USED_IN_THIS_CERTIFICATE',
 'abstract_H_type':'(Z/4)^2 direct_sum (Z/2)^5','support_skeleton_count':len(skeletons),
 'support_profile_by_t_eqrank':{f't={t},eqrank={r}':n for (t,r),n in sorted(profile.items())},
 'weighted_structural_H_count':weighted,'source_integral_coordinate_symmetry_order':288,
 'exact_support_skeleton_orbit_count':len(reps),'orbit_size_histogram':{str(k):v for k,v in sorted(Counter(sizes).items())},
 'orbit_profile_by_t_eqrank_size':{f't={t},eqrank={r},size={s}':n for (t,r,s),n in sorted(orbit_profile.items())},
 'representative_lift_sections_for_next_exact_leaf':rep_sections,'orbit_representatives':reps,
 'full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,
 'next_exact_leaf':'L33-07-EXHAUST-K2-PURE-GEOMETRIC-SUPPORT-ORBITS-BY-FULL-Q4-THETA-RANK',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k2-geometric-support-orbits.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'skeletons':len(skeletons),'orbits':len(reps),'representative_lift_sections_next':rep_sections,'weighted_H':weighted,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
