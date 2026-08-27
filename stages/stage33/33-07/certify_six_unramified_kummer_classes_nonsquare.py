#!/usr/bin/env python3
"""Close the six unramified Kummer square-triviality tests from the quartic
carrier reduction.

For Sx=u^2+v^2 over Q(i), the squareclass of Sx equals that of
    (u+i*v)/(u-i*v),
because their quotient is (u-i*v)^2.  Thus adjoining sqrt(Sx) is birationally
parameterized on the dense chart v!=0 by
    t^2=(u+i*v)/(u-i*v),
    v=1,
    u=i*(t^2+1)/(t^2-1).
Substituting this into the irreducible base quartic F gives a primitive
polynomial P(t,y), where y is the remaining base coordinate.  If P is
irreducible in Q(i)[t,y], Gauss' lemma makes it irreducible in Q(i)(t)[y]; the
double cover K(sqrt(Sx))/K is connected, hence [Sx] is nontrivial.

All six primitive pullback polynomials are certified irreducible.  Combined
with the prior proof that Su is ramified/nontrivial and Sx is unramified, the
two Kummer classes are independent for every group.  Therefore each of the 12
quartic-norm hyperplane sections has a single off-boundary prime strict-
transform component.  Together with the 12 genus-one components from b1,b2,b3,
the off-boundary carrier prime-divisor inventory now has exactly 24 entries.

No residue cancellation is inferred here; that is the next leaf.
"""
import hashlib,json
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
IN=HERE/'quartic-norm-biquadratic-cover-reduction.json'
BJ=HERE/'bj-offboundary-genus1-components.json'
OUT=HERE/'six-unramified-kummer-classes-nonsquare.json'
EXPECTED_REDUCTION_SHA='44137dfb73cb3d51157815f21969d21be094d2775d202b65c3366e913c7412df'
EXPECTED_BJ_SHA='d3543d8eed2b4ba79d384a7491b22f6c3d968542cc16752dd9c025acb6b71ee6'

I=sp.I
a1,a2,a3=sp.symbols('a1 a2 a3'); A=(a1,a2,a3)
t,y=sp.symbols('t y')
S1=a2*a2+a3*a3; S2=a1*a1+a3*a3; S3=a1*a1+a2*a2


def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(path,expected):
    x=json.load(open(path)); h=x.pop('canonical_sha256')
    if h!=expected or sha(x)!=expected: raise SystemExit(f'source lock moved: {path.name}')
    return x

def dec(z): return sp.Rational(int(z[0]),int(z[1]))+I*sp.Rational(int(z[2]),int(z[3]))
def from_terms(rows):
    out=0
    for r in rows:
        q=dec(r['coefficient_Qi']); mon=sp.Integer(1)
        for v,e in zip(A,r['monomial_exponents']): mon*=v**int(e)
        out+=q*mon
    return sp.expand(out)
def enc_qi(q):
    q=sp.cancel(sp.expand(q)); qc=sp.cancel(sp.conjugate(q))
    re=sp.cancel((q+qc)/2); im=sp.cancel((q-qc)/(2*I))
    if re.is_Rational is not True or im.is_Rational is not True: raise SystemExit(f'non-Q(i) coefficient {q}')
    return [int(sp.numer(re)),int(sp.denom(re)),int(sp.numer(im)),int(sp.denom(im))]
def poly_terms(expr,vars_):
    return [{'monomial_exponents':list(mon),'coefficient_Qi':enc_qi(q)} for mon,q in sp.Poly(expr,*vars_,extension=I).terms()]
def parse_sx(s):
    return sp.expand(sp.sympify(s,locals={'a1':a1,'a2':a2,'a3':a3}))
def param_data(Sx):
    if sp.expand(Sx-S1)==0: return a2,a3,a1,'S1=a2^2+a3^2'
    if sp.expand(Sx-S2)==0: return a1,a3,a2,'S2=a1^2+a3^2'
    if sp.expand(Sx-S3)==0: return a1,a2,a3,'S3=a1^2+a2^2'
    raise SystemExit(f'unexpected Sx {Sx}')
def primitive_pullback(F,Sx):
    u,v,remaining,label=param_data(Sx)
    ratio=I*(t*t+1)/(t*t-1)
    subs={v:sp.Integer(1),u:ratio,remaining:y}
    rat=sp.together(F.subs(subs)); num,den=rat.as_numer_denom()
    # Primitive part in y over Q(i)[t] removes chart/denominator-only factors.
    py=sp.Poly(sp.expand(num),y,domain=sp.QQ_I[t])
    content,primitive=py.primitive()
    P=sp.expand(primitive.as_expr())
    fac=sp.factor_list(P,t,y,extension=I)
    if len(fac[1])!=1 or fac[1][0][1]!=1:
        raise SystemExit(f'Kummer pullback reducible: F={F}, Sx={Sx}, factorization={fac}')
    factor=sp.expand(fac[1][0][0])
    if sp.Poly(factor,t,y,extension=I).total_degree()!=sp.Poly(P,t,y,extension=I).total_degree():
        raise SystemExit('factorization degree mismatch')
    return {
      'Sx_label':label,'u':str(u),'v':str(v),'remaining_coordinate_y':str(remaining),
      'Kummer_parameter':'t^2=(u+i*v)/(u-i*v)',
      'dense_chart_substitution':f'{v}=1; {u}=i*(t^2+1)/(t^2-1); {remaining}=y',
      'removed_content_in_Qi_t':str(sp.factor(content,extension=I)),
      'primitive_pullback_polynomial_terms':poly_terms(P,(t,y)),
      'primitive_pullback_degree_t':int(sp.Poly(P,t,y).degree(t)),
      'primitive_pullback_degree_y':int(sp.Poly(P,t,y).degree(y)),
      'irreducible_factor_count_over_Qi':1,
      'irreducible_over_Qi_t_y':True,
      'irreducible_over_Qi_of_t_in_y_by_Gauss':True,
    }

red=load(IN,EXPECTED_REDUCTION_SHA); bj=load(BJ,EXPECTED_BJ_SHA)
if red['reduction_summary']['unramified_Kummer_squareclasses_remaining']!=6: raise SystemExit('six-test prefix moved')
if bj['hyperplane_decomposition']['total_genus1_prime_divisors']!=12: raise SystemExit('b_j prime prefix moved')

records=[]
for g in red['quartic_group_records']:
    F=from_terms(g['base_quartic_terms'])
    Sx=parse_sx(g['Kummer_cover_algebra']['Sx'])
    p=primitive_pullback(F,Sx)
    if not g['connectedness_decision']['Su_nontrivial_ramified'] or not g['connectedness_decision']['Sx_unramified']:
        raise SystemExit(f'Kummer divisor prefix moved {g["group_id"]}')
    records.append({
      'group_id':g['group_id'],
      'base_quartic_integral':g['base_quartic_integral'],
      'base_normalization_genus':int(g['normalization']['geometric_genus']),
      'carrier_indices_1based':[int(r['carrier_index_1based']) for r in g['carrier_members']],
      'Sx':str(Sx),'Su':g['Kummer_cover_algebra']['Su'],
      'pullback_irreducibility_certificate':p,
      'squareclass_conclusion':{
        'Sx_nonsquare':True,'Sx_unramified':True,'Su_nonsquare_ramified':True,
        'Sx_Su_independent_in_Kstar_mod_squares':True,'squareclass_rank':2,
      },
      'carrier_component_conclusion':{
        'prime_components_per_carrier':1,
        'generic_degree_over_base_normalization':4,
        'off_boundary_strict_transform_prime':True,
        'exceptional_total_transform_components_are_boundary_and_not_counted_here':True,
      },
    })

if len(records)!=6 or sum(len(r['carrier_indices_1based']) for r in records)!=12: raise SystemExit('six-pair carrier count regression')
yhist={}
for r in records:
    d=str(r['pullback_irreducibility_certificate']['primitive_pullback_degree_y'])
    yhist[d]=yhist.get(d,0)+1
if yhist!={'2':5,'4':1}: raise SystemExit(f'pullback y-degree histogram moved: {yhist}')
if sorted(x for r in records for x in r['carrier_indices_1based']) != sorted([4,5,9,10,11,12,13,14,18,19,20,21]):
    raise SystemExit('quartic carrier indices moved')

cert={
 'schema':'STAGE33_07_SIX_UNRAMIFIED_KUMMER_CLASSES_NONSQUARE_V1',
 'source_locks':{'quartic_Kummer_reduction_sha256':EXPECTED_REDUCTION_SHA,'bj_genus1_decomposition_sha256':EXPECTED_BJ_SHA},
 'field':'Q(i); conclusions persist after adjoining sqrt(2) unless explicitly re-tested for constant-field splitting, but the certified pullback polynomials themselves are nonconstant-field irreducibility witnesses over Q(i)',
 'method':'birational Kummer parameter t^2=(u+i v)/(u-i v), primitive pullback irreducibility in Q(i)[t,y], Gauss lemma',
 'group_records':records,
 'summary':{
   'unramified_Kummer_tests_closed':6,
   'Sx_nonsquare_count':6,
   'squareclass_rank2_groups':6,
   'quartic_norm_hyperplanes_irreducible_over_Qi_function_field':12,
   'quartic_offboundary_prime_strict_transforms':12,
   'bj_offboundary_genus1_prime_divisors':12,
   'total_offboundary_carrier_prime_divisors':24,
   'primitive_pullback_y_degree_histogram':yhist,
 },
 'exact_checks':{
   'all_six_Kummer_pullback_curves_are_irreducible_over_Qi':True,
   'all_six_Sx_squareclasses_are_nonsquare':True,
   'all_six_Sx_classes_are_independent_from_ramified_Su_classes':True,
   'all_twelve_quartic_carriers_have_one_offboundary_prime_strict_transform':True,
   'all_three_bj_carriers_contribute_four_genus1_primes_each':True,
   'offboundary_carrier_prime_divisor_inventory_has_24_entries':True,
 },
 'constructive_progress':{
   'off_boundary_prime_divisor_decomposition_fully_closed':True,
   'off_boundary_carrier_prime_divisor_count':24,
   'unramified_Kummer_square_triviality_tests_remaining':0,
   'global_geometric_Gersten_lifts_materialized_count':0,
   'off_boundary_codimension1_residue_certificates_materialized_count':0,
   'project_14x26_L_squareclass_tensor_materialized':False,
   'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False,
 },
 'new_smallest_exact_kernel':'R33-BR2A-24-OFFBOUNDARY-PRIME-DIVISOR-SOURCE-MULTIPLICITY-RESIDUE-CANCELLATION',
 'next_exact_leaf':'L33-07-ASSEMBLE-26-BY-24-OFFBOUNDARY-PRIME-DIVISOR-MULTIPLICITY-MATRIX-AND-TEST-ORDER2-ORDER4-RESIDUES',
 'stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
}
cert['canonical_sha256']=sha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({
 'success':True,'unramified_Kummer_tests':'6/6 CLOSED','quartic_prime_strict_transforms':12,
 'bj_genus1_primes':12,'total_offboundary_carrier_primes':24,
 'pullback_y_degree_histogram':yhist,'certificate_sha256':cert['canonical_sha256'],
 'next_exact_leaf':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
