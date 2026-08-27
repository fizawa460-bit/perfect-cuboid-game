#!/usr/bin/env python3
"""Certify existence (not explicit representatives) of all 26 mixed-order
geometric Gersten lifts over L=Q(i,sqrt(2)).

The previous construction materializes boundary H^1 residue functions for 17
order-2 and 9 order-4 source directions.  This leaf verifies the *full*
codimension-two Gersten compatibility of those tuples, including the pole at
infinity on every boundary P1, and then applies purity/Gersten exactness for
the smooth regular surface S_L.

Important distinction: exactness gives a global function-field Brauer class
whose residues are exactly the prescribed boundary tuple and zero on every
other codimension-one divisor.  It does not choose an explicit rational-symbol
representative, so Galois-difference coordinates and the 14x26 tensor remain
blocked.
"""
import hashlib,json,runpy
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE_SCRIPT=HERE/'materialize_order2_first_residue_functions.py'
ORDER4_SCRIPT=HERE/'certify_order2_quotient_raw_order4_bockstein.py'
BASE_JSON=HERE/'order2-first-residue-function-liftability.json'
ORDER4_JSON=HERE/'order2-quotient-raw-order4-bockstein.json'
OUT=HERE/'mixed-order-global-gersten-lift-existence-by-purity.json'
EXPECTED_BASE='85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312'
EXPECTED_ORDER4='085ad52c1eb1cf8069fcac9a0814250428288cc5d517a036670ae529c36eb88a'


def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def locked(path,expected):
    x=json.load(open(path)); h=x.pop('canonical_sha256')
    if h!=expected or sha(x)!=expected: raise SystemExit(f'source lock moved: {path.name}')
    x['canonical_sha256']=h; return x

def bits_from_hex(h,n):
    z=int(h,16); return [(z>>j)&1 for j in range(n)]
def comp_id(j): return f'SIDE_{j+1:03d}' if j<24 else f'EXC_{j-23:03d}'

# Reproduce both exact producers.  The order4 producer itself re-runs BASE, but
# we retain the first namespace because it exposes the frozen 144-edge order.
ns=runpy.run_path(str(BASE_SCRIPT))
runpy.run_path(str(ORDER4_SCRIPT))
base=locked(BASE_JSON,EXPECTED_BASE); order4=locked(ORDER4_JSON,EXPECTED_ORDER4)
edges=ns['edges']
if len(edges)!=144 or any(a>=24 or b<24 for a,b in edges): raise SystemExit('144 side->exceptional edge order moved')

# 17 raw-order2 tuples: divisor mod 2 consists exactly of the selected crossing
# points; denominator degree is even, so infinity has coefficient 0 mod 2.
raw2_records=[]
for sr in base['source_basis']:
    if not sr['raw_order2_first_residue_function_liftable']: continue
    name=sr['source_basis_name']; v=bits_from_hex(sr['crossing_vector_f2_144_hex_le'],144)
    pkgs={p['component_id']:p for p in sr['component_first_residue_functions']}
    appearances={e:[] for e,b in enumerate(v) if b}
    for j in range(72):
        expected=[e for e,(a,b) in enumerate(edges) if v[e] and (a==j or b==j)]
        p=pkgs.get(comp_id(j))
        if not expected:
            if p is not None: raise SystemExit(f'{name} unexpected nontrivial package {comp_id(j)}')
            continue
        if p is None: raise SystemExit(f'{name} missing package {comp_id(j)}')
        if int(p['even_degree'])%2: raise SystemExit(f'{name} odd infinity pole degree at {comp_id(j)}')
        got=sorted(int(x.split('_')[1])-1 for x in p['selected_edge_ids'])
        if got!=expected: raise SystemExit(f'{name} crossing divisor mismatch at {comp_id(j)}')
        for e in got: appearances[e].append(j)
    for e,ends in appearances.items():
        if sorted(ends)!=sorted(edges[e]): raise SystemExit(f'{name} edge {e+1} not present at both endpoints')
    raw2_records.append({'source_basis_name':name,'order':2,'selected_crossing_count':sum(v),'all_crossing_second_residues_cancel_mod_order':True,'all_infinity_pole_coefficients_zero_mod_order':True})
if len(raw2_records)!=17: raise SystemExit('17 raw-order2 source count moved')

# 9 raw-order4 tuples: producer freezes oriented coefficient -r on side and +r
# on exceptional.  Their sum is 0 mod 4 at every crossing; denominator degree
# is divisible by 4, so infinity also contributes zero.
raw4_records=[]
order4_rows=order4['quotient_to_raw_bockstein']['nine_source_records']
for sr in order4_rows:
    name=sr['source_basis_name']; z=int(sr['raw_z4_crossing_vector_2bit_hex_le'],16)
    raw=[(z>>(2*e))&3 for e in range(144)]
    pkgs={p['component_id']:p for p in sr['component_order4_first_residue_functions']}
    seen={}
    for j in range(72):
        p=pkgs.get(comp_id(j)); expected=[]
        for e,(a,b) in enumerate(edges):
            r=raw[e]
            c=(-r)%4 if j==a else (r%4 if j==b else 0)
            if c: expected.append((e,c))
        if not expected:
            if p is not None: raise SystemExit(f'{name} unexpected order4 package {comp_id(j)}')
            continue
        if p is None: raise SystemExit(f'{name} missing order4 package {comp_id(j)}')
        if int(p['denominator_exponent_d'])%4: raise SystemExit(f'{name} nonzero infinity residue mod4 at {comp_id(j)}')
        got=sorted((int(f['edge_id'].split('_')[1])-1,int(f['z4_divisor_coefficient'])%4) for f in p['selected_crossing_factors'])
        if got!=expected: raise SystemExit(f'{name} signed crossing divisor mismatch at {comp_id(j)}')
        for e,c in got: seen.setdefault(e,[]).append((j,c))
    for e,r in enumerate(raw):
        if r==0:
            if e in seen: raise SystemExit(f'{name} zero edge unexpectedly present {e+1}')
            continue
        a,b=edges[e]; got=sorted(seen.get(e,[]))
        want=sorted([(a,(-r)%4),(b,r%4)])
        if got!=want or sum(c for _,c in got)%4:
            raise SystemExit(f'{name} order4 second residue failed at edge {e+1}')
    raw4_records.append({'source_basis_name':name,'order':4,'odd_crossing_entry_count':int(sr['raw_odd_crossing_entry_count']),'all_crossing_second_residues_cancel_mod_order':True,'all_infinity_pole_coefficients_zero_mod_order':True})
if len(raw4_records)!=9: raise SystemExit('9 raw-order4 source count moved')

cert={
 'schema':'STAGE33_07_MIXED_ORDER_GLOBAL_GERSTEN_LIFT_EXISTENCE_BY_PURITY_V1',
 'source_locks':{'order2_first_residue_liftability_sha256':EXPECTED_BASE,'full_order4_bockstein_sha256':EXPECTED_ORDER4},
 'field':'L=Q(i,sqrt(2))','surface':'smooth regular compactification S_L; char 0; 2 and 4 invertible; mu_4 subset L',
 'gersten_exactness_adapter':{
   'complex':'Br(K)[n] -> direct_sum_{D in S^(1)} H^1(k(D),Z/n) -> direct_sum_{x in S^(2)} H^0(k(x),Z/n(-1))',
   'use':'extend each prescribed 72-boundary residue tuple by zero on every other codimension-one divisor; exactness at the middle term gives a global function-field Brauer n-torsion lift',
   'explicit_symbol_representative_chosen':False,
 },
 'source_records':raw2_records+raw4_records,
 'exact_counts':{'source_count':26,'raw_order2_sources':17,'raw_order4_sources':9,'boundary_components':72,'crossings':144},
 'exact_checks':{
   'all_17_order2_component_divisors_match_the_frozen_crossing_vectors':True,
   'all_17_order2_crossing_second_residues_cancel_pairwise_mod2':True,
   'all_17_order2_infinity_poles_have_even_degree':True,
   'all_9_order4_signed_component_divisors_match_the_frozen_raw_Z4_vectors':True,
   'all_9_order4_crossing_second_residues_cancel_as_minus_r_plus_r_mod4':True,
   'all_9_order4_infinity_poles_have_degree_divisible_by4':True,
   'all_26_boundary_tuples_extended_by_zero_are_in_the_full_codim2_Gersten_kernel':True,
   'global_geometric_Gersten_lift_existence_follows_for_all_26':True,
 },
 'constructive_progress':{
   'global_geometric_Gersten_lift_existence_certified_count':26,
   'global_geometric_Gersten_explicit_representatives_materialized_count':0,
   'offboundary_residue_vanishing_for_the_abstract_Gersten_preimages':'BUILT_IN_BY_ZERO_EXTENSION_AND_EXACTNESS',
   'explicit_boundary_uniformizer_atlas_retained_but_not_promoted_to_global_lifts':True,
   'cc_ct_actions_on_chosen_global_representatives_computed':False,
   'proper_Br2_difference_coordinates_computed':False,
   'project_14x26_L_squareclass_tensor_materialized':False,
   'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False,
 },
 'new_smallest_exact_kernel':'R33-BR2A-26-GERSTEN-LIFT-CHOICE-GALOIS-EXTENSION-CLASS-IN-PROPER-BR2',
 'next_exact_leaf':'L33-07-COMPUTE-GALOIS-EXTENSION-CLASS-OF-26-GERSTEN-LIFT-TORSOR-WITHOUT-REQUIRING-RATIONAL-SYMBOL-REPRESENTATIVES',
 'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
}
cert['canonical_sha256']=sha(cert); OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'global_Gersten_lift_existence':'26/26','explicit_representatives':'0/26','certificate_sha256':cert['canonical_sha256'],'next_exact_leaf':cert['next_exact_leaf']},indent=2,sort_keys=True))