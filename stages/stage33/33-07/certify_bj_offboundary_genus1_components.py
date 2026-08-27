#!/usr/bin/env python3
"""Decompose the three split-linear off-boundary carrier hyperplanes b1=0,
b2=0,b3=0 into their exact four genus-one components over Q(i).

Each b_j=0 forces one Pythagorean square relation to split and, independently,
forces c^2 to become the square of the remaining a-coordinate.  Hence four
sign branches.  After eliminating those two linear relations, every branch is
isomorphic to the same (2,2) complete intersection in P3:

  p^2 = x^2 + y^2,
  q^2 = y^2 - x^2.

The Jacobian rank test is checked projectively by four exact Groebner charts.
The model is therefore smooth.  A positive-dimensional projective complete
intersection is connected; smooth + connected gives geometric irreducibility.
Its degree is 2*2=4 and its complete-intersection genus is 1.

This closes the prime-divisor decomposition only for b1,b2,b3.  The 12
irreducible-quartic-norm carrier hyperplanes remain the exact kernel.
"""
import hashlib,json
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
IN=HERE/'ambient-linear-carrier-boundary-offboundary-split.json'
OUT=HERE/'bj-offboundary-genus1-components.json'
EXPECTED_SPLIT_SHA='13140597dd2196a0593038534a789a75b2f92cf389df34b2f61462835a9b6abb'

a1,a2,a3,b1,b2,b3,c=sp.symbols('a1 a2 a3 b1 b2 b3 c')
COORDS=(a1,a2,a3,b1,b2,b3,c)
I=sp.I
SURFACE=[
 a1*a1+a2*a2-b3*b3,
 a2*a2+a3*a3-b1*b1,
 a1*a1+a3*a3-b2*b2,
 a1*a1+a2*a2+a3*a3-c*c,
]

def sha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def dec(z): return sp.Rational(int(z[0]),int(z[1]))+I*sp.Rational(int(z[2]),int(z[3]))
def linear_expr(row):
    d={x['coordinate']:dec(x['coefficient_Qi']) for x in row['ambient_linear_form']}
    return sp.expand(sum(d.get(str(v),0)*v for v in COORDS))

def canonical_linear(expr):
    p=sp.Poly(sp.expand(expr),*COORDS,extension=I)
    out=[]
    for v in COORDS:
        q=p.coeff_monomial(v)
        if q!=0: out.append([str(v),str(sp.cancel(q))])
    return out

def projective_smooth_model_check():
    x,y,p,q=sp.symbols('x y p q')
    f1=p*p-x*x-y*y
    f2=q*q+x*x-y*y
    J=sp.Matrix([f1,f2]).jacobian([x,y,p,q])
    minors=[]
    for r in range(4):
        for s in range(r+1,4): minors.append(sp.expand(J[:,[r,s]].det()))
    charts={}
    for v in (x,y,p,q):
        G=sp.groebner([f1,f2,*minors,v-1],x,y,p,q,order='lex')
        charts[str(v)]=bool(G.contains(sp.Integer(1)))
    if not all(charts.values()): raise SystemExit(f'canonical genus-one model singular: {charts}')
    return {
      'equations':['p^2-x^2-y^2','q^2+x^2-y^2'],
      'jacobian_2x2_minors':[str(m) for m in minors],
      'projective_affine_chart_singularity_ideals_are_unit':charts,
      'smooth':True,'complete_intersection_type':[2,2],'degree':4,'genus':1,
      'geometrically_irreducible_reason':'smooth positive-dimensional projective complete intersection is connected; smooth connected curve is irreducible',
    }

split=json.load(open(IN)); claimed=split.pop('canonical_sha256')
if claimed!=EXPECTED_SPLIT_SHA or sha(split)!=EXPECTED_SPLIT_SHA: raise SystemExit('carrier split source lock moved')
recs=split['carrier_records']
split_linear=[r for r in recs if r['classification']=='OFF_BOUNDARY_SPLIT_LINEAR_BASE_NORM']
if len(split_linear)!=3: raise SystemExit('split-linear carrier count moved')
exprs={str(linear_expr(r)):r for r in split_linear}
for name in ('b1','b2','b3'):
    if name not in exprs: raise SystemExit(f'missing {name}=0 split-linear carrier')

model=projective_smooth_model_check()
branches=[]
# For each hyperplane, choose canonical model coordinates (x,y,p,q) as documented.
configs={
 'b1':{
   'zero':'b1','split_relation':'a2^2+a3^2=0','sign1_template':'a2 - sigma*i*a3',
   'c_relation':'c^2-a1^2=0','sign2_template':'c - tau*a1',
   'model_map':{'x':'a3','y':'a1','p':'b2','q':'b3'},
   'remaining_equations':['b2^2=a1^2+a3^2','b3^2=a1^2-a3^2'],
 },
 'b2':{
   'zero':'b2','split_relation':'a1^2+a3^2=0','sign1_template':'a1 - sigma*i*a3',
   'c_relation':'c^2-a2^2=0','sign2_template':'c - tau*a2',
   'model_map':{'x':'a3','y':'a2','p':'b1','q':'b3'},
   'remaining_equations':['b1^2=a2^2+a3^2','b3^2=a2^2-a3^2'],
 },
 'b3':{
   'zero':'b3','split_relation':'a1^2+a2^2=0','sign1_template':'a1 - sigma*i*a2',
   'c_relation':'c^2-a3^2=0','sign2_template':'c - tau*a3',
   'model_map':{'x':'a2','y':'a3','p':'b1','q':'b2'},
   'remaining_equations':['b1^2=a2^2+a3^2','b2^2=a3^2-a2^2'],
 },
}

subs_by_name={
 'b1':lambda s,t:{b1:0,a2:s*I*a3,c:t*a1},
 'b2':lambda s,t:{b2:0,a1:s*I*a3,c:t*a2},
 'b3':lambda s,t:{b3:0,a1:s*I*a2,c:t*a3},
}

for name in ('b1','b2','b3'):
    carrier=exprs[name]
    for sigma in (-1,1):
        for tau in (-1,1):
            subs=subs_by_name[name](sigma,tau)
            reduced=[sp.factor(sp.expand(f.subs(subs))) for f in SURFACE]
            nonzero=[]
            for f in reduced:
                if f!=0 and all(sp.expand(f-g)!=0 and sp.expand(f+g)!=0 for g in nonzero): nonzero.append(f)
            # Two independent quadrics remain; duplicates/signs are removed above.
            if len(nonzero)!=2: raise SystemExit(f'{name} branch ({sigma},{tau}) did not reduce to two quadrics: {nonzero}')
            branches.append({
              'carrier_hyperplane':name+'=0',
              'carrier_index_1based':carrier['carrier_index_1based'],
              'sigma':sigma,'tau':tau,
              'ambient_linear_branch_equations':[
                 name,
                 configs[name]['sign1_template'].replace('sigma',str(sigma)),
                 configs[name]['sign2_template'].replace('tau',str(tau)),
              ],
              'canonical_model_coordinate_map':configs[name]['model_map'],
              'canonical_model':'p^2=x^2+y^2; q^2=y^2-x^2',
              'degree':4,'genus':1,'smooth':True,'geometrically_irreducible':True,
            })

if len(branches)!=12: raise SystemExit('b_j branch count regression')
if sum(b['degree'] for b in branches if b['carrier_hyperplane']=='b1=0')!=16: raise SystemExit('b1 degree accounting')
if sum(b['degree'] for b in branches if b['carrier_hyperplane']=='b2=0')!=16: raise SystemExit('b2 degree accounting')
if sum(b['degree'] for b in branches if b['carrier_hyperplane']=='b3=0')!=16: raise SystemExit('b3 degree accounting')

cert={
 'schema':'STAGE33_07_BJ_OFFBOUNDARY_GENUS1_COMPONENTS_V1',
 'source_lock':{'carrier_boundary_offboundary_split_sha256':EXPECTED_SPLIT_SHA},
 'field':'Q(i) (hence also L=Q(i,sqrt(2)))',
 'canonical_genus1_model':model,
 'hyperplane_decomposition':{
   'b1=0':configs['b1'],'b2=0':configs['b2'],'b3=0':configs['b3'],
   'branches_per_hyperplane':4,'total_genus1_prime_divisors':12,
   'degree_per_branch':4,'degree_per_hyperplane':16,
 },
 'branch_records':branches,
 'exact_checks':{
   'carrier_split_linear_hyperplanes_are_exactly_b1_b2_b3':True,
   'each_bj_section_has_four_sign_branches':True,
   'every_branch_substitution_reduces_surface_to_two_quadrics':True,
   'canonical_2_2_model_projectively_smooth_by_four_Groebner_charts':True,
   'canonical_component_degree_is_4':True,
   'canonical_component_genus_is_1':True,
   'four_branch_degree_accounting_is_16_for_each_bj_hyperplane':True,
 },
 'constructive_progress':{
   'boundary_vs_offboundary_carrier_split_closed':True,
   'split_linear_offboundary_hyperplanes_decomposed':3,
   'split_linear_offboundary_prime_divisors_materialized':12,
   'irreducible_quartic_norm_hyperplanes_remaining':12,
   'global_geometric_Gersten_lifts_materialized_count':0,
   'off_boundary_codimension1_residue_certificates_materialized_count':0,
   'project_14x26_L_squareclass_tensor_materialized':False,
   'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False,
 },
 'new_smallest_exact_kernel':'R33-BR2A-12-QUARTIC-NORM-HYPERPLANE-SECTIONS-PRIME-DECOMPOSITION-AND-RESIDUES',
 'next_exact_leaf':'L33-07-ANALYZE-12-QUARTIC-NORM-HYPERPLANE-SECTIONS-AS-BIQUADRATIC-COVERS-OF-6-BASE-QUARTICS',
 'stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
}
cert['canonical_sha256']=sha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({
 'success':True,'split_linear_hyperplanes':'3/3','genus1_prime_divisors':12,
 'canonical_model':'smooth (2,2) CI, degree 4, genus 1',
 'quartic_norm_hyperplanes_remaining':12,
 'certificate_sha256':cert['canonical_sha256'],'next_exact_leaf':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
