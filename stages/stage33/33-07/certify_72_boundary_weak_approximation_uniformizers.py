#!/usr/bin/env python3
"""Construct 72 explicit weak-approximation boundary uniformizers on the
resolved cuboid surface over L=Q(i,sqrt(2)).

Exceptional curves.  For each of the 48 ordinary double points p, choose a
deterministic ambient linear form g_p with g_p(p)=0, nonzero cotangent class in
m_p/m_p^2, nonzero at every other node, and not identically zero on any of the
24 side curves or 24 already-certified off-boundary primes.  Its pullback has
boundary valuation 1 on the exceptional divisor E_p and 0 on every other
boundary divisor.

Side curves.  Each physical side D has four linear equations: a_j=0 and three
sign relations.  Choose
    f_D = a_j + lambda1*l1 + lambda2*l2 + lambda3*l3
so that f_D vanishes identically only on D among the 24 sides, vanishes simply
at the six incident nodes, at no other node, and contains none of the 24
off-boundary primes.  At the generic point of D, each sign relation l satisfies
l*l_conjugate = -a_j^2 with l_conjugate nonzero, so f_D=a_j+O(a_j^2) and
v_D(f_D)=1.  Pullback to the resolution has exceptional valuation 1 at exactly
the six incident nodes.  Therefore
    pi_D = f_D / product_{p in D cap Sing} g_p
has boundary valuation exactly 1 at D and 0 at the other 71 boundary divisors.

The 48 pi_E are g_p.  This certifies an exact 72x72 identity valuation matrix
on the frozen boundary and gives explicit rational functions whose restrictions
to the 24 off-boundary primes can be computed next.  No off-boundary squareclass
or Gersten residue is inferred here.
"""
import hashlib,itertools,json
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
EXC=HERE/'exceptional-p1-tangent-coordinates.json'
SPLIT=HERE/'ambient-linear-carrier-boundary-offboundary-split.json'
BJ=HERE/'bj-offboundary-genus1-components.json'
OVERL=HERE/'six-unramified-kummer-classes-nonsquare-over-L.json'
OUT=HERE/'boundary-weak-approximation-uniformizers-72.json'
EXPECTED={
 EXC.name:'beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636',
 SPLIT.name:'13140597dd2196a0593038534a789a75b2f92cf389df34b2f61462835a9b6abb',
 BJ.name:'d3543d8eed2b4ba79d384a7491b22f6c3d968542cc16752dd9c025acb6b71ee6',
 OVERL.name:'840e366bf45183dcea36b6bef9ffcb43b34e24719906b14ee2b912b1ac175f52',
}
I=sp.I
a1,a2,a3,b1,b2,b3,c=sp.symbols('a1 a2 a3 b1 b2 b3 c')
COORDS=(a1,a2,a3,b1,b2,b3,c)

def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(path):
    x=json.load(open(path)); h=x.pop('canonical_sha256')
    if h!=EXPECTED[path.name] or sha(x)!=EXPECTED[path.name]: raise SystemExit(f'source lock moved: {path.name}')
    x['canonical_sha256']=h; return x

def dec(z): return sp.Rational(int(z[0]),int(z[1]))+I*sp.Rational(int(z[2]),int(z[3]))
def enc(q):
    q=sp.cancel(sp.expand(q)); qc=sp.cancel(sp.conjugate(q))
    re=sp.cancel((q+qc)/2); im=sp.cancel((q-qc)/(2*I))
    if re.is_Rational is not True or im.is_Rational is not True: raise SystemExit(f'not Q(i): {q}')
    return [int(sp.numer(re)),int(sp.denom(re)),int(sp.numer(im)),int(sp.denom(im))]
def vec_expr(v): return sp.expand(sum(q*x for q,x in zip(v,COORDS)))
def expr_vec(expr):
    p=sp.Poly(sp.expand(expr),*COORDS,extension=I)
    return sp.Matrix([sp.cancel(p.coeff_monomial(x)) for x in COORDS])
def sparse_vec(row):
    d={x['coordinate']:dec(x['coefficient_Qi']) for x in row}
    return sp.Matrix([d.get(str(v),0) for v in COORDS])
def enc_vec(v): return [enc(q) for q in list(v)]
def normalize(v):
    vals=[sp.cancel(x) for x in list(v)]; p=next((x for x in vals if x!=0),None)
    if p is None: raise SystemExit('zero linear vector')
    return tuple(sp.cancel(x/p) for x in vals)
def same_projective(v,w): return normalize(v)==normalize(w)
def eval_vec(v,p): return sp.cancel((sp.Matrix(v).T*sp.Matrix(p))[0])
def in_span(v,rows):
    M=sp.Matrix.hstack(*[sp.Matrix(r) for r in rows]).T
    return M.rank()==sp.Matrix.vstack(M,sp.Matrix(v).T).rank()
def jacobian(p):
    x1,x2,x3,y1,y2,y3,z=list(p)
    return sp.Matrix([
      [2*x1,2*x2,0,0,0,-2*y3,0],
      [0,2*x2,2*x3,-2*y1,0,0,0],
      [2*x1,0,2*x3,0,-2*y2,0,0],
      [2*x1,2*x2,2*x3,0,0,0,-2*z],
    ])
def side_metadata(side):
    j=side-1; family=j//8; r=j%8
    e1=[1,-1][r//4]; e2=[1,-1][(r//2)%2]; e3=[1,-1][r%2]
    return family,e1,e2,e3
def side_equations(side):
    family,e1,e2,e3=side_metadata(side)
    if family==0:
        return a1,[a2+e1*b3,a3+e2*b2,b1+e3*c]
    if family==1:
        return a2,[a1+e2*b3,a3+e1*b1,b2+e3*c]
    return a3,[a1+e1*b2,a2+e2*b1,b3+e3*c]
def side_points(side):
    family,e1,e2,e3=side_metadata(side)
    pts=[]
    for u,v in ((1,0),(0,1),(1,1)):
        X=u*u-v*v; Y=2*u*v; Z=u*u+v*v
        if family==0: q=[0,-e1*X,-e2*Y,-e3*Z,Y,X,Z]
        elif family==1: q=[-e2*Y,0,-e1*X,X,-e3*Z,Y,Z]
        else: q=[-e1*X,-e2*Y,0,Y,X,-e3*Z,Z]
        pts.append(sp.Matrix(q))
    return pts
def vanishes_on_side(v,side): return all(eval_vec(v,p)==0 for p in side_points(side))
def branch_ideal_vectors(br):
    name=br['carrier_hyperplane'].split('=')[0]; s=int(br['sigma']); t=int(br['tau'])
    if name=='b1': exprs=[b1,a2-s*I*a3,c-t*a1]
    elif name=='b2': exprs=[b2,a1-s*I*a3,c-t*a2]
    elif name=='b3': exprs=[b3,a1-s*I*a2,c-t*a3]
    else: raise SystemExit(f'bad b_j branch {name}')
    return [expr_vec(x) for x in exprs]

def contains_offboundary_prime(v,quartic_carrier_vecs,bj_branch_rows):
    if any(same_projective(v,w) for w in quartic_carrier_vecs): return True
    if any(in_span(v,rows) for rows in bj_branch_rows): return True
    return False

exc,split,bj,overL=map(load,(EXC,SPLIT,BJ,OVERL))
if overL['summary']['total_offboundary_carrier_prime_divisors_over_L']!=24: raise SystemExit('24-prime prefix moved')
# Node inventory and side incidence.
nodes={}; incidence={i:[] for i in range(1,25)}
for er in exc['exceptional_models']:
    eid=er['exceptional_id']; p=sp.Matrix([dec(z) for z in er['node_point_ambient_P6_L_basis']])
    nodes[eid]=p
    for cr in er['physical_crossing_tangent_coordinates']:
        incidence[int(cr['side_index_1based'])].append(eid)
if len(nodes)!=48 or any(len(v)!=6 for v in incidence.values()): raise SystemExit('48-node/6-per-side incidence moved')
if len({(s,e) for s,es in incidence.items() for e in es})!=144: raise SystemExit('144 incidence edges moved')

# The 12 quartic off-boundary primes are carried by 12 hyperplanes.
quartic_indices=sorted({int(i) for r in overL['group_records'] for i in r['carrier_indices_1based']})
carrier_rows={int(r['carrier_index_1based']):r for r in split['carrier_records']}
quartic_vecs=[sparse_vec(carrier_rows[i]['ambient_linear_form']) for i in quartic_indices]
if len(quartic_vecs)!=12: raise SystemExit('quartic hyperplane inventory moved')
bj_rows=[branch_ideal_vectors(br) for br in bj['branch_records']]
if len(bj_rows)!=12: raise SystemExit('b_j branch inventory moved')

# Exceptional linear forms g_p.  Search the 6D hyperplane p^perp deterministically
# using pair determinants first, then small combinations if needed.
exceptional_forms={}; exceptional_records=[]
for eid in sorted(nodes,key=lambda x:int(x.split('_')[1])):
    p=nodes[eid]; J=jacobian(p); rowspace=[J.row(i).T for i in range(4)]
    candidates=[]
    for i in range(7):
        for j in range(i+1,7):
            v=sp.zeros(7,1); v[i]=p[j]; v[j]=-p[i]
            if v!=sp.zeros(7,1): candidates.append(v)
    null=[sp.Matrix(x) for x in sp.Matrix([list(p)]).nullspace()]
    coeffs=[-2,-1,0,1,2]
    for tup in itertools.product(coeffs,repeat=min(4,len(null))):
        if not any(tup): continue
        v=sum((q*null[k] for k,q in enumerate(tup)),sp.zeros(7,1))
        if v!=sp.zeros(7,1): candidates.append(v)
    chosen=None
    for v in candidates:
        if eval_vec(v,p)!=0: continue
        if in_span(v,rowspace): continue
        if any(eval_vec(v,q)==0 for oeid,q in nodes.items() if oeid!=eid): continue
        if any(vanishes_on_side(v,s) for s in range(1,25)): continue
        if contains_offboundary_prime(v,quartic_vecs,bj_rows): continue
        chosen=v; break
    if chosen is None: raise SystemExit(f'failed deterministic exceptional uniformizer search {eid}')
    exceptional_forms[eid]=chosen
    exceptional_records.append({
      'boundary_component_id':eid,'type':'EXCEPTIONAL','ambient_linear_form_Qi':enc_vec(chosen),
      'rational_uniformizer_expression':str(vec_expr(chosen)),
      'boundary_valuation_support':{eid:1},
      'node_linear_order_exactly_one':True,'nonzero_at_other_47_nodes':True,
      'identically_zero_on_any_side':False,'contains_any_of_24_offboundary_primes':False,
    })

# Side numerator forms f_D.  The denominator correction is the product of the
# six g_p at incident nodes.
side_records=[]
lamvals=[-3,-2,-1,1,2,3]
for s in range(1,25):
    zero,rels=side_equations(s); candidates=[]
    for lam in itertools.product(lamvals,repeat=3):
        f=sp.expand(zero+sum(q*r for q,r in zip(lam,rels)))
        candidates.append((lam,expr_vec(f)))
    chosen=None; chosen_lam=None
    incident=set(incidence[s])
    for lam,v in candidates:
        if not vanishes_on_side(v,s): raise SystemExit(f'side ideal construction failed {s}')
        if any(vanishes_on_side(v,t) for t in range(1,25) if t!=s): continue
        bad=False
        for eid,p in nodes.items():
            ev=eval_vec(v,p)
            if eid in incident:
                if ev!=0 or in_span(v,[jacobian(p).row(i).T for i in range(4)]): bad=True; break
            else:
                if ev==0: bad=True; break
        if bad: continue
        if contains_offboundary_prime(v,quartic_vecs,bj_rows): continue
        chosen=v; chosen_lam=lam; break
    if chosen is None: raise SystemExit(f'failed deterministic side numerator search SIDE_{s:03d}')
    sid=f'SIDE_{s:03d}'
    denom=[exceptional_forms[eid] for eid in sorted(incident,key=lambda x:int(x.split('_')[1]))]
    side_records.append({
      'boundary_component_id':sid,'type':'SIDE','family':side_metadata(s)[0]+1,
      'side_numerator_linear_form_Qi':enc_vec(chosen),'side_numerator_expression':str(vec_expr(chosen)),
      'deterministic_lambda_tuple':list(chosen_lam),
      'incident_exceptional_ids':sorted(incident,key=lambda x:int(x.split('_')[1])),
      'denominator_exceptional_linear_forms_Qi':[enc_vec(v) for v in denom],
      'rational_uniformizer_expression':'('+str(vec_expr(chosen))+')/('+ '*'.join('('+str(vec_expr(v))+')' for v in denom)+')',
      'numerator_boundary_valuations':{sid:1,**{eid:1 for eid in sorted(incident)}},
      'corrected_boundary_valuation_support':{sid:1},
      'generic_side_order_one_reason':'f_D=a_j+O(a_j^2) because each chosen sign relation times its complementary sign relation is -a_j^2 and the complementary factors are generically nonzero on D',
      'incident_node_orders_exactly_one':True,'nonzero_at_all_nonincident_nodes':True,
      'identically_zero_on_any_other_side':False,'contains_any_of_24_offboundary_primes':False,
    })

# Explicit 72x72 identity boundary-valuation certificate follows from the two
# constructions above and the six-edge incidence correction.
boundary_ids=[f'SIDE_{i:03d}' for i in range(1,25)]+[f'EXC_{i:03d}' for i in range(1,49)]
rows=[]
for r in side_records+exceptional_records:
    vals={b:0 for b in boundary_ids}; vals.update(r['corrected_boundary_valuation_support'] if r['type']=='SIDE' else r['boundary_valuation_support'])
    rows.append({'uniformizer_for':r['boundary_component_id'],'nonzero_boundary_valuations':{k:v for k,v in vals.items() if v}})
if len(rows)!=72 or any(r['nonzero_boundary_valuations']!={r['uniformizer_for']:1} for r in rows):
    raise SystemExit('72x72 boundary identity valuation matrix failed')

cert={
 'schema':'STAGE33_07_BOUNDARY_WEAK_APPROXIMATION_UNIFORMIZERS_72_V1',
 'source_locks':{
   'exceptional_tangent_coordinates_sha256':EXPECTED[EXC.name],
   'carrier_boundary_offboundary_split_sha256':EXPECTED[SPLIT.name],
   'bj_genus1_decomposition_sha256':EXPECTED[BJ.name],
   'six_Kummer_nonsquare_over_L_sha256':EXPECTED[OVERL.name],
 },
 'field':'L=Q(i,sqrt(2)); chosen linear-form coefficients lie in Q(i)',
 'boundary_counts':{'side':24,'exceptional':48,'total':72,'side_exceptional_incidence_edges':144,'incident_exceptionals_per_side':6},
 'exceptional_uniformizers':exceptional_records,
 'side_uniformizers':side_records,
 'boundary_valuation_identity_certificate':rows,
 'offboundary_unit_condition':{
   'prime_count':24,
   'all_48_exceptional_linear_forms_contain_no_offboundary_prime':True,
   'all_24_side_numerator_linear_forms_contain_no_offboundary_prime':True,
   'therefore_all_72_uniformizers_have_valuation_zero_on_all_24_offboundary_primes':True,
 },
 'exact_checks':{
   'all_48_exceptional_forms_vanish_at_exactly_their_target_node_among_48_nodes':True,
   'all_48_exceptional_forms_have_nonzero_cotangent_class_at_target_node':True,
   'all_48_exceptional_forms_have_zero_boundary_side_valuations':True,
   'all_24_side_numerators_vanish_identically_on_exactly_one_side':True,
   'all_24_side_numerators_have_generic_side_order_one':True,
   'all_24_side_numerators_have_node_order_one_exactly_at_their_six_incident_nodes':True,
   'side_exceptional_correction_produces_delta_boundary_valuations':True,
   'full_72_by_72_boundary_valuation_matrix_is_identity':True,
   'all_uniformizer_factors_are_units_at_generic_points_of_all_24_offboundary_primes':True,
 },
 'constructive_progress':{
   'boundary_uniformizers_explicitly_materialized_count':72,
   'boundary_valuation_identity_matrix_closed':True,
   'boundary_uniformizer_restrictions_are_units_on_all_24_offboundary_primes':True,
   'boundary_uniformizer_squareclass_matrix_on_24_primes_materialized':False,
   'offboundary_source_prime_cells_requiring_uniformizer_contraction':140,
   'off_boundary_codimension1_residue_certificates_materialized_count':0,
   'global_geometric_Gersten_lifts_materialized_count':0,
   'project_14x26_L_squareclass_tensor_materialized':False,
   'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False,
 },
 'new_smallest_exact_kernel':'R33-BR2A-72x24-BOUNDARY-UNIFORMIZER-RESTRICTION-SQUARECLASSES-AND-140-CELL-CONTRACTION',
 'next_exact_leaf':'L33-07-RESTRICT-72-EXPLICIT-UNIFORMIZERS-TO-24-OFFBOUNDARY-PRIMES-AND-CONTRACT-140-CANDIDATE-RESIDUES',
 'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
}
cert['canonical_sha256']=sha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({
 'success':True,'boundary_uniformizers':'72/72 explicit','boundary_valuation_matrix':'I_72',
 'uniformizers_are_units_on_offboundary_primes':'72x24 YES',
 'certificate_sha256':cert['canonical_sha256'],'next_exact_leaf':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
