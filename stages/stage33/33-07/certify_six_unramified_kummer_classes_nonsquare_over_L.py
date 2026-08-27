#!/usr/bin/env python3
"""Upgrade the six Q(i)-Kummer nonsquare certificates to the actual arithmetic
working field L=Q(i,sqrt(2)).

A polynomial irreducible over Q(i) can split after a constant-field extension,
so the Q(i) certificate is not by itself sufficient.  This leaf refactors each
primitive pullback polynomial over Q(i,sqrt(2))[t,y].  All six remain
irreducible; hence all six Sx classes stay nonsquare over the exact downstream
field L and the 12 quartic carrier strict transforms remain prime over L.
"""
import hashlib,json
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
IN=HERE/'six-unramified-kummer-classes-nonsquare.json'
OUT=HERE/'six-unramified-kummer-classes-nonsquare-over-L.json'
I=sp.I; SQ2=sp.sqrt(2); t,y=sp.symbols('t y')

def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def dec(z): return sp.Rational(int(z[0]),int(z[1]))+I*sp.Rational(int(z[2]),int(z[3]))
def poly_from_terms(rows):
    out=0
    for r in rows:
        q=dec(r['coefficient_Qi']); mon=sp.Integer(1)
        for v,e in zip((t,y),r['monomial_exponents']): mon*=v**int(e)
        out+=q*mon
    return sp.expand(out)

q=json.load(open(IN)); qh=q.pop('canonical_sha256')
if sha(q)!=qh: raise SystemExit('Q(i) Kummer certificate canonical hash mismatch')
if q['schema']!='STAGE33_07_SIX_UNRAMIFIED_KUMMER_CLASSES_NONSQUARE_V1': raise SystemExit('Q(i) Kummer schema moved')
if q['summary']['unramified_Kummer_tests_closed']!=6 or q['summary']['quartic_offboundary_prime_strict_transforms']!=12:
    raise SystemExit('Q(i) Kummer prefix moved')

records=[]
for r in q['group_records']:
    P=poly_from_terms(r['pullback_irreducibility_certificate']['primitive_pullback_polynomial_terms'])
    fac=sp.factor_list(P,t,y,extension=[I,SQ2])
    if len(fac[1])!=1 or fac[1][0][1]!=1:
        raise SystemExit(f'constant-field splitting over L for {r["group_id"]}: {fac}')
    f=fac[1][0][0]
    if sp.Poly(f,t,y,extension=[I,SQ2]).total_degree()!=sp.Poly(P,t,y,extension=[I,SQ2]).total_degree():
        raise SystemExit(f'L factor degree mismatch for {r["group_id"]}')
    records.append({
      'group_id':r['group_id'],
      'base_normalization_genus':r['base_normalization_genus'],
      'carrier_indices_1based':r['carrier_indices_1based'],
      'Sx':r['Sx'],'Su':r['Su'],
      'primitive_pullback_degree_y':r['pullback_irreducibility_certificate']['primitive_pullback_degree_y'],
      'factor_count_over_Qi_sqrt2':1,
      'irreducible_over_L_t_y':True,
      'Sx_nonsquare_over_L':True,
      'Sx_Su_squareclass_rank_over_L':2,
      'prime_components_per_carrier_over_L':1,
    })

if len(records)!=6 or sum(len(r['carrier_indices_1based']) for r in records)!=12: raise SystemExit('L group count regression')
cert={
 'schema':'STAGE33_07_SIX_UNRAMIFIED_KUMMER_CLASSES_NONSQUARE_OVER_L_V1',
 'source_lock':{'Qi_Kummer_certificate_sha256':qh},
 'field':'L=Q(i,sqrt(2))',
 'constant_field_extension_check':'direct exact factorization of every primitive Kummer pullback polynomial over Q(i,sqrt(2))[t,y]',
 'group_records':records,
 'summary':{
   'Kummer_groups_checked_over_L':6,
   'Sx_nonsquare_over_L_count':6,
   'squareclass_rank2_groups_over_L':6,
   'quartic_offboundary_prime_strict_transforms_over_L':12,
   'bj_offboundary_genus1_prime_divisors_over_Qi_prefix':12,
   'total_offboundary_carrier_prime_divisors_over_L':24,
 },
 'exact_checks':{
   'all_six_Qi_pullback_certificates_rehashed':True,
   'all_six_pullback_polynomials_remain_irreducible_after_adjoining_sqrt2':True,
   'all_six_Sx_classes_remain_nonsquare_over_L':True,
   'all_six_Sx_Su_pairs_have_squareclass_rank2_over_L':True,
   'all_twelve_quartic_carriers_have_one_offboundary_prime_strict_transform_over_L':True,
   'offboundary_carrier_prime_divisor_inventory_over_L_has_24_entries':True,
 },
 'constructive_progress':{
   'off_boundary_prime_divisor_decomposition_over_L_fully_closed':True,
   'off_boundary_carrier_prime_divisor_count_over_L':24,
   'unramified_Kummer_square_triviality_tests_over_L_remaining':0,
   'global_geometric_Gersten_lifts_materialized_count':0,
   'off_boundary_codimension1_residue_certificates_materialized_count':0,
   'project_14x26_L_squareclass_tensor_materialized':False,
   'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False,
 },
 'new_smallest_exact_kernel':'R33-BR2A-24-OFFBOUNDARY-PRIME-DIVISOR-SOURCE-MULTIPLICITY-RESIDUE-CANCELLATION-OVER-L',
 'next_exact_leaf':'L33-07-ASSEMBLE-26-BY-24-OFFBOUNDARY-PRIME-DIVISOR-MULTIPLICITY-MATRIX-OVER-L-AND-TEST-RESIDUES',
 'stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
}
cert['canonical_sha256']=sha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({
 'success':True,'field':'L=Q(i,sqrt(2))','Kummer_tests_over_L':'6/6 CLOSED',
 'quartic_prime_strict_transforms_over_L':12,'total_offboundary_carrier_primes_over_L':24,
 'certificate_sha256':cert['canonical_sha256'],'next_exact_leaf':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
