#!/usr/bin/env python3
"""Exact k=2 skeleton census after Q[2]/2Q support, cc-mod2, and symmetry.

Starting from H ~= (Z/4)^2 +(Z/2)^5, the preceding exact support reductions
leave 988,553,216 structural H.  This leaf materializes only their (P,W)
skeletons, not the lift sections.  The Q[2]+2Q conditions have the exact W
parameterization:

  U=W cap Y coisotropic, T=U^perp,
  R=pr_X(W) <= P_X^perp cap E_X,
  D_X + <j> <= R,
  phi|D_X=0,
  phi(j) mod U = the unique coset representing t -> wt(t)/2 on T.

This yields exactly 88,288 skeletons.  The common mod-two reduction of every
retained cc lift swaps the two coordinates in each of the three Kb pieces and
fixes Kc/Ka.  Exact stability leaves 7,456 skeletons.  The integral source
symmetry S3(Kb)*(S2)^3*S3(Ka), order 288 with Kc fixed, then gives exactly 427
skeleton orbits.

No lift section is quotiented or rejected by the symmetry.  No full Q[4],
finite-q, integral cc/ct, actual-glue, HS, endpoint, or theorem credit is made.
"""
import hashlib
import itertools
import json
import runpy
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
if actions.get('canonical_sha256')!=ACTION_LOCK:
    raise SystemExit('retained action-choice source lock moved')
if twoq.get('schema')!='STAGE33_07_NONELEMENTARY_K12_2Q_SUPPORT_REDUCTION_V1':
    raise SystemExit('2Q-support predecessor schema regression')
if twoq['summary_by_number_of_Z4_factors']['2']['structural_H_after_endpoint_2Q_support_necessary_condition']!=988553216:
    raise SystemExit('k2 2Q predecessor total moved')

subspaces=base_ns['subspaces'];span=base_ns['span'];rank=base_ns['rank'];canon=base_ns['canon'];red_to_full=base_ns['red_to_full'];eqrc=base_ns['eq_rank_and_consistency']
coisotropic_y=q8_ns['coisotropic']
X_MASK=(1<<10)-1
J=X_MASK

def contains(B,x): return rank(list(B)+[x])==len(B)
def complement(base,whole):
    cur=list(canon(base));out=[]
    for v in canon(whole):
        if rank(cur+[v])>len(cur): cur.append(v);out.append(v)
    return tuple(out)
def perp(B,n):
    return canon(x for x in range(1,1<<n) if all((x&b).bit_count()%2==0 for b in B))
def rref_subspaces(n,k):
    if k==0:
        yield ();return
    for pivots in itertools.combinations(range(n),k):
        ps=set(pivots);free=[j for j in range(n) if j not in ps]
        slots=[(r,j) for j in free for r,p in enumerate(pivots) if p<j]
        for mask in range(1<<len(slots)):
            rows=[1<<p for p in pivots]
            for z,(r,j) in enumerate(slots):
                if (mask>>z)&1: rows[r]|=1<<j
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
        if len(result)!=target_dim: raise SystemExit('ambient subspace lift regression')
        yield result

def lambda_coset_representative(U):
    T=perp(U,4)
    solutions=[]
    for y in range(16):
        if all(((y&t).bit_count()&1)==((t.bit_count()//2)&1) for t in [0]+[x for x in range(1,16) if contains(T,x)]):
            solutions.append(y)
    if len(solutions)!=(1<<len(U)):
        raise SystemExit('unique lambda coset regression')
    return min(solutions)

def graph_skeletons(dx,R,U):
    y0=lambda_coset_representative(U)
    domain_base=canon(tuple(dx)+(J,))
    extra=complement(domain_base,R)
    ycomp=complement(U,canon(1<<j for j in range(4)))
    slots=[(i,j) for i in range(len(extra)) for j in range(len(ycomp))]
    for mask in range(1<<len(slots)):
        rows=list(dx)+[u<<10 for u in U]+[J|(y0<<10)]
        for i,x in enumerate(extra):
            y=0
            for bit,(ii,j) in enumerate(slots):
                if ii==i and (mask>>bit)&1:y^=ycomp[j]
            rows.append(x|(y<<10))
        W=canon(rows)
        if len(W)!=7: raise SystemExit('k2 W rank regression')
        yield W

skeletons=set();profile=Counter();p_eqrank={}
for reduced_p in sorted(subspaces[2]):
    supp=0
    for v in span(reduced_p):supp|=v
    if supp.bit_count()>7:continue
    t=rank([v&0b111 for v in reduced_p]);eqrank,ok=eqrc(reduced_p)
    if not ok or t>2:continue
    p=canon(red_to_full(v) for v in reduced_p);p_eqrank[p]=eqrank
    px=canon(v&X_MASK for v in p)
    x0=perp(px,10)
    xe=canon(v for v in [0]+[x for x in range(1,1<<10) if contains(x0,x)] if v and v.bit_count()%2==0)
    dx=canon((1<<(2*j))|(1<<(2*j+1)) for j in range(3) if (supp>>j)&1)
    dy=canon(1<<j for j in range(4) if (supp>>(3+j))&1)
    base=canon(tuple(dx)+(J,))
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
    raise SystemExit(f'k2 skeleton census regression {len(skeletons)} {profile}')
structural=sum(n*(1<<(14-eqrank)) for (t,eqrank),n in profile.items())
if structural!=988553216:raise SystemExit('k2 structural-H reconstruction regression')

# Common cc mod-two action.
for local in actions['pieces']['kb']['cc_actions']:
    if [[int(x)&1 for x in row] for row in local]!=[[0,1],[1,0]]:raise SystemExit('Kb cc mod2 regression')
for species in ('kc','ka'):
    for local in actions['pieces'][species]['cc_actions']:
        if [[int(x)&1 for x in row] for row in local]!=[[1,0],[0,1]]:raise SystemExit(f'{species} cc mod2 regression')
perm=list(range(14))
for a,b in ((0,1),(2,3),(4,5)):perm[a],perm[b]=b,a

def transport(v,p):
    out=0
    for old,new in enumerate(p):
        if (v>>old)&1:out|=1<<new
    return out
cc=set();cc_profile=Counter()
for p,W in skeletons:
    if canon(transport(v,perm) for v in p)!=p:raise SystemExit('P cc stability regression')
    if canon(transport(v,perm) for v in W)==W:
        cc.add((p,W));t=rank([v&X_MASK for v in p]);cc_profile[(t,p_eqrank[p])]+=1
if len(cc)!=7456 or cc_profile!=Counter({(1,1):5274,(2,1):1381,(0,0):801}):
    raise SystemExit(f'k2 cc-mod2 census regression {len(cc)} {cc_profile}')
structural_cc=sum(n*(1<<(14-eqrank)) for (t,eqrank),n in cc_profile.items())
if structural_cc!=67641344:raise SystemExit('k2 cc-mod2 structural-H regression')

# Integral source-species symmetry.
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
def move(s,g):
    p,W=s;return canon(transport(v,g) for v in p),canon(transport(v,g) for v in W)
unseen=set(cc);sizes=[];reps=[]
while unseen:
    seed=min(unseen);orb={move(seed,g) for g in sym}
    if not orb<=cc:raise SystemExit('k2 skeleton set not symmetry-stable')
    unseen.difference_update(orb);rep=min(orb);sizes.append(len(orb));reps.append({'P_basis_bits':list(rep[0]),'W_basis_bits':list(rep[1]),'orbit_size':len(orb),'eqrank':p_eqrank[rep[0]]})
hist=Counter(sizes)
expected_hist=Counter({18:195,9:117,36:75,3:24,6:12,12:2,1:1,24:1})
if len(sizes)!=427 or hist!=expected_hist or sum(sizes)!=7456:
    raise SystemExit(f'k2 orbit census regression {len(sizes)} {hist}')

cert={
 'schema':'STAGE33_07_NONELEMENTARY_K2_Q2_2Q_SKELETON_ORBITS_V1',
 'source_2Q_support_sha256':twoq['canonical_sha256'],
 'source_retained_action_choices_sha256':ACTION_LOCK,
 'abstract_H_type':'(Z/4)^2 direct_sum (Z/2)^5',
 'exact_P_W_skeleton_count':len(skeletons),
 'skeleton_profile_by_t_eqrank':{f't={t},eqrank={r}':n for (t,r),n in sorted(profile.items())},
 'structural_H_count_reconstructed':structural,
 'forced_cc_mod2_action':'swap each Kb pair; fix Kc and Ka coordinates',
 'forced_cc_mod2_compatible_skeleton_count':len(cc),
 'forced_cc_mod2_profile_by_t_eqrank':{f't={t},eqrank={r}':n for (t,r),n in sorted(cc_profile.items())},
 'structural_H_count_after_forced_cc_mod2':structural_cc,
 'structural_H_rejected_by_forced_cc_mod2':structural-structural_cc,
 'symmetry_description':'S3(Kb pieces) semidirect (S2)^3(Kb swaps) times S3(Ka pieces), Kc fixed',
 'symmetry_order':288,
 'exact_skeleton_orbit_count':len(sizes),
 'orbit_size_histogram':{str(k):v for k,v in sorted(hist.items())},
 'orbit_size_sum':sum(sizes),
 'orbit_representatives':reps,
 'surviving_lift_sections_quotiented_or_rejected':False,
 'full_Q4_condition_certified':False,
 'integral_cc_ct_certified':False,
 'endpoint_finite_q_certified':False,
 'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,
 'arithmetic_HS_closed':False,
 'next_exact_leaf':'L33-07-K2-INTEGRAL-CC-CT-AFFINE-FILTER-OVER-427-SKELETON-ORBITS',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k2-q2-2q-skeleton-orbits.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'skeletons':len(skeletons),'cc_mod2_skeletons':len(cc),'structural_H_after_cc_mod2':structural_cc,'skeleton_orbits':len(sizes),'certificate_sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
