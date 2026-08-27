#!/usr/bin/env python3
"""Exactly split the 33 ambient linear carrier hyperplanes into boundary-only
and genuine off-boundary candidates by multiquadratic norm to P2_[a1:a2:a3].

On the cuboid surface
  b1^2=a2^2+a3^2, b2^2=a1^2+a3^2,
  b3^2=a1^2+a2^2, c^2=a1^2+a2^2+a3^2.
The full sign norm of a linear carrier L is therefore a degree-16 form in
(a1,a2,a3).  If every irreducible norm factor is a coordinate a_i, then every
divisorial component of L=0 lies over a coordinate hyperplane a_i=0.  Those
three inverse images are exactly the 24 frozen physical side conics: for a1=0,
for example, the surface equations force independently
  a2=+-b3, a3=+-b2, b1=+-c,
giving the eight A1 side conics, and cyclically for a2=0,a3=0.

A non-coordinate norm factor certifies that L=0 has off-boundary divisorial
support.  This leaf does not yet decompose those 15 hyperplane sections into
prime divisors or compute residues on them.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE=Path(__file__).resolve().parent
IN=HERE/'mixed-order-ambient-linear-divisor-support.json'
OUT=HERE/'ambient-linear-carrier-boundary-offboundary-split.json'
EXPECTED_CARRIER_SHA='8427c237e0489a615b2a19d532b76f7bcaeb6af54ee6420034208d8cc63c2381'

a1,a2,a3,b1,b2,b3,c=sp.symbols('a1 a2 a3 b1 b2 b3 c')
BASE=(a1,a2,a3)
RADICALS=(b1,b2,b3,c)
SQUARES={
 b1:a2*a2+a3*a3,
 b2:a1*a1+a3*a3,
 b3:a1*a1+a2*a2,
 c:a1*a1+a2*a2+a3*a3,
}
COORDS=(a1,a2,a3,b1,b2,b3,c)


def canonical_sha256(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def dec(z):
    return sp.Rational(int(z[0]),int(z[1]))+sp.I*sp.Rational(int(z[2]),int(z[3]))

def enc_qi(x):
    x=sp.cancel(sp.expand(x)); xc=sp.cancel(sp.conjugate(x))
    re=sp.cancel((x+xc)/2); im=sp.cancel((x-xc)/(2*sp.I))
    if re.is_Rational is not True or im.is_Rational is not True:
        raise SystemExit(f'coefficient escaped Q(i): {x}')
    return [int(sp.numer(re)),int(sp.denom(re)),int(sp.numer(im)),int(sp.denom(im))]

def reduce_quadratic(expr,var,sq):
    poly=sp.Poly(sp.expand(expr),var)
    even=0; odd=0
    for (k,),coef in poly.terms():
        if k%2==0: even += coef*sq**(k//2)
        else: odd += coef*sq**((k-1)//2)
    return sp.expand(even**2-sq*odd**2)

def full_sign_norm(expr):
    out=expr
    for var in RADICALS:
        out=reduce_quadratic(out,var,SQUARES[var])
    return sp.expand(out)

def normalized_factor_record(factor,exponent):
    p=sp.Poly(sp.expand(factor),*BASE,extension=sp.I)
    terms=p.terms()
    if not terms: raise SystemExit('zero factor')
    lead=terms[0][1]
    p=sp.Poly(sp.expand(p.as_expr()/lead),*BASE,extension=sp.I)
    rows=[]
    for mon,coef in p.terms():
        rows.append({'monomial_exponents':list(mon),'coefficient_Qi':enc_qi(coef)})
    expr=sp.expand(p.as_expr())
    coord=None
    for name,var in [('a1',a1),('a2',a2),('a3',a3)]:
        if sp.expand(expr-var)==0:
            coord=name
    return {
      'degree':int(p.total_degree()),
      'exponent_in_norm':int(exponent),
      'normalized_terms':rows,
      'coordinate_factor':coord,
    }

def form_expression(record):
    coeff=[dec(z) for z in record['canonical_linear_form_L_basis']]
    return sp.expand(sum(q*v for q,v in zip(coeff,COORDS)))

def form_record(expr):
    p=sp.Poly(expr,*COORDS,extension=sp.I)
    return [{'coordinate':str(v),'coefficient_Qi':enc_qi(p.coeff_monomial(v))}
            for v in COORDS if p.coeff_monomial(v)!=0]

carrier=json.load(open(IN))
claimed=carrier.pop('canonical_sha256')
if claimed!=EXPECTED_CARRIER_SHA or canonical_sha256(carrier)!=EXPECTED_CARRIER_SHA:
    raise SystemExit('ambient carrier source lock moved')
if carrier['distinct_projective_ambient_linear_forms']!=33 or carrier['total_linear_form_occurrences']!=720:
    raise SystemExit('carrier count regression')

rows=[]; boundary_count=off_count=0; boundary_occ=off_occ=0
all_noncoordinate={}
for idx,record in enumerate(carrier['ambient_linear_form_inventory'],1):
    expr=form_expression(record)
    norm=full_sign_norm(expr)
    if sp.Poly(norm,*BASE).total_degree()!=16:
        raise SystemExit(f'norm degree regression carrier {idx}')
    unit,factors=sp.factor_list(norm,*BASE,extension=sp.I)
    frecs=[normalized_factor_record(f,e) for f,e in factors]
    weighted=sum(r['degree']*r['exponent_in_norm'] for r in frecs)
    if weighted!=16:
        raise SystemExit(f'factor degree accounting regression carrier {idx}: {weighted}')
    boundary_only=all(r['coordinate_factor'] is not None for r in frecs)
    occ=int(record['occurrences'])
    if boundary_only:
        boundary_count+=1; boundary_occ+=occ
        kind='BOUNDARY_ONLY_COORDINATE_NORM_SUPPORT'
    else:
        off_count+=1; off_occ+=occ
        non=[r for r in frecs if r['coordinate_factor'] is None]
        if len(non)==2 and all(r['degree']==1 and r['exponent_in_norm']==8 for r in non):
            kind='OFF_BOUNDARY_SPLIT_LINEAR_BASE_NORM'
        elif len(non)==1 and non[0]['degree']==4 and non[0]['exponent_in_norm']==4:
            kind='OFF_BOUNDARY_IRREDUCIBLE_QUARTIC_BASE_NORM'
        else:
            raise SystemExit(f'unexpected off-boundary factor type carrier {idx}: {non}')
        for r in non:
            key=json.dumps(r['normalized_terms'],sort_keys=True,separators=(',',':'))
            all_noncoordinate[key]=r
    rows.append({
      'carrier_index_1based':idx,
      'ambient_linear_form':form_record(expr),
      'occurrences':occ,
      'source_count':int(record['source_count']),
      'component_count':int(record['component_count']),
      'vanishing_exceptional_node_count':len(record['vanishing_exceptional_node_ids']),
      'norm_factorization_over_Qi':frecs,
      'classification':kind,
      'boundary_only':boundary_only,
    })

if (boundary_count,off_count)!=(18,15): raise SystemExit(f'33-way split moved: {boundary_count}+{off_count}')
if (boundary_occ,off_occ)!=(530,190): raise SystemExit(f'720 occurrence split moved: {boundary_occ}+{off_occ}')
linear_off=sum(r['classification']=='OFF_BOUNDARY_SPLIT_LINEAR_BASE_NORM' for r in rows)
quartic_off=sum(r['classification']=='OFF_BOUNDARY_IRREDUCIBLE_QUARTIC_BASE_NORM' for r in rows)
if (linear_off,quartic_off)!=(3,12): raise SystemExit(f'off-boundary type split moved: {linear_off}+{quartic_off}')
base_factor_degrees=sorted(r['degree'] for r in all_noncoordinate.values())
if base_factor_degrees!=[1]*6+[4]*6:
    raise SystemExit(f'noncoordinate base factor inventory moved: {base_factor_degrees}')

cert={
 'schema':'STAGE33_07_AMBIENT_LINEAR_CARRIER_BOUNDARY_OFFBOUNDARY_SPLIT_V1',
 'source_lock':{'ambient_linear_carrier_certificate_sha256':EXPECTED_CARRIER_SHA},
 'surface_model':{
   'b1_square':'a2^2+a3^2','b2_square':'a1^2+a3^2',
   'b3_square':'a1^2+a2^2','c_square':'a1^2+a2^2+a3^2',
   'sign_norm_degree':16,
 },
 'coordinate_boundary_certificate':{
   'a1_zero':'exactly 8 A1 side conics via a2=+-b3, a3=+-b2, b1=+-c',
   'a2_zero':'exactly 8 A2 side conics via a1=+-b3, a3=+-b1, b2=+-c',
   'a3_zero':'exactly 8 A3 side conics via a1=+-b2, a2=+-b1, b3=+-c',
   'total_physical_side_conics':24,
 },
 'carrier_split':{
   'total_distinct_projective_ambient_linear_forms':33,
   'boundary_only_hyperplanes':18,
   'off_boundary_candidate_hyperplanes':15,
   'boundary_only_occurrences':530,
   'off_boundary_candidate_occurrences':190,
   'off_boundary_split_linear_hyperplanes':3,
   'off_boundary_irreducible_quartic_norm_hyperplanes':12,
   'distinct_noncoordinate_base_norm_factors':12,
   'noncoordinate_base_norm_factor_degree_histogram':{'1':6,'4':6},
 },
 'carrier_records':rows,
 'exact_checks':{
   'all_33_full_sign_norms_have_degree_16':True,
   'all_norm_factorizations_are_over_Qi':True,
   'coordinate_norm_support_implies_support_on_frozen_24_side_boundary':True,
   'exact_33_way_split_is_18_boundary_only_plus_15_off_boundary':True,
   'exact_720_occurrence_split_is_530_boundary_only_plus_190_off_boundary':True,
   'off_boundary_hyperplane_type_split_is_3_linear_plus_12_quartic':True,
   'distinct_noncoordinate_base_factor_inventory_is_6_lines_plus_6_quartics':True,
 },
 'constructive_progress':{
   'all_72_boundary_component_function_packages_ambientized':True,
   'ambient_linear_carrier_inventory_materialized':True,
   'boundary_vs_offboundary_carrier_split_closed':True,
   'off_boundary_hyperplane_sections_remaining_to_decompose':15,
   'global_geometric_Gersten_lifts_materialized_count':0,
   'off_boundary_codimension1_residue_certificates_materialized_count':0,
   'project_14x26_L_squareclass_tensor_materialized':False,
   'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False,
 },
 'new_smallest_exact_kernel':'R33-BR2A-15-OFFBOUNDARY-HYPERPLANE-SECTIONS-PRIME-DIVISOR-DECOMPOSITION-AND-RESIDUES',
 'next_exact_leaf':'L33-07-DECOMPOSE-3-BJ-SECTIONS-PLUS-12-QUARTIC-NORM-SECTIONS-IN-SURFACE-COORDINATE-RING',
 'stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
}
cert['canonical_sha256']=canonical_sha256(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({
 'success':True,'carrier_split':'18 boundary-only + 15 off-boundary',
 'occurrence_split':'530 boundary-only + 190 off-boundary',
 'off_boundary_types':'3 split-linear + 12 irreducible-quartic-norm',
 'distinct_noncoordinate_base_factors':'6 lines + 6 quartics',
 'certificate_sha256':cert['canonical_sha256'],
 'next_exact_leaf':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
