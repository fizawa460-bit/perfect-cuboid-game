#!/usr/bin/env python3
"""Assemble the exact 26-source x 24 off-boundary-prime valuation tensor over
L=Q(i,sqrt(2)).

The 24 prime divisors are now source-locked:
* 12 genus-one strict-transform primes from b1=0,b2=0,b3=0 (4 each);
* 12 prime strict transforms of the quartic-norm carrier hyperplanes, proved
  prime after the six Kummer nonsquare tests remain irreducible over L.

For every one of the 240 nontrivial boundary first-residue function packages,
this leaf factors each numerator/pole ambient linear form through the frozen
33-carrier atlas and records its valuation on the 24 off-boundary primes.
The result is a sparse tensor

    m[source, offboundary_prime, boundary_component] in Z,

reduced modulo the source order (2 for 17 sources, 4 for 9 sources).

IMPORTANT: a nonzero tensor cell is only a *candidate* Gersten residue.  The
actual residue is the product of boundary uniformizer squareclasses raised to
these exponents.  Therefore this leaf does not claim residue nonvanishing and
does not promote any global Gersten lift.  Its purpose is to shrink the next
receiver to the exact 140 source-prime cells that need uniformizer-class
contraction; the other 484 of 624 cells vanish for valuation reasons alone.
"""
import hashlib,json
from collections import Counter,defaultdict
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
SIDE=HERE/'mixed-order-side-ambient-function-lifts.json'
EXC=HERE/'mixed-order-exceptional-ambient-tangent-function-lifts.json'
SPLIT=HERE/'ambient-linear-carrier-boundary-offboundary-split.json'
BJ=HERE/'bj-offboundary-genus1-components.json'
OVERL=HERE/'six-unramified-kummer-classes-nonsquare-over-L.json'
OUT=HERE/'offboundary-prime-valuation-tensor-26x24-over-L.json'
EXPECTED={
 SIDE.name:'2f137842fffbabe7fa9f91879f379e0662803204d6753c342fc31f6dfe12fa6d',
 EXC.name:'a9d5ceb66625dfa561db61a3afc95388bf5a8371fb81905988991514a765d397',
 SPLIT.name:'13140597dd2196a0593038534a789a75b2f92cf389df34b2f61462835a9b6abb',
 BJ.name:'d3543d8eed2b4ba79d384a7491b22f6c3d968542cc16752dd9c025acb6b71ee6',
 OVERL.name:'840e366bf45183dcea36b6bef9ffcb43b34e24719906b14ee2b912b1ac175f52',
}
COORDS=['a1','a2','a3','b1','b2','b3','c']

def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(path):
    x=json.load(open(path)); h=x.pop('canonical_sha256')
    if h!=EXPECTED[path.name] or sha(x)!=EXPECTED[path.name]: raise SystemExit(f'source lock moved: {path.name}')
    x['canonical_sha256']=h
    return x

def z(q):
    if isinstance(q,list): return (Fraction(int(q[0]),int(q[1])),Fraction(int(q[2]),int(q[3])))
    return q

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def inv(x):
    d=x[0]*x[0]+x[1]*x[1]
    if d==0: raise SystemExit('zero projective pivot')
    return (x[0]/d,-x[1]/d)
def enc(x): return [x[0].numerator,x[0].denominator,x[1].numerator,x[1].denominator]
def canon_vector(v):
    vals=[z(x) for x in v]; pivot=next((x for x in vals if x!=(0,0)),None)
    if pivot is None: raise SystemExit('zero ambient linear form')
    q=inv(pivot)
    return tuple(tuple(enc(mul(q,x))) for x in vals)
def sparse_to_vector(row):
    v=[(Fraction(0),Fraction(0)) for _ in COORDS]
    for e in row:
        v[COORDS.index(e['coordinate'])]=z(e['coefficient_Qi'])
    return v

def source_sort(s): return int(s.split('_')[1])
def component_sort(c): return (0 if c.startswith('SIDE_') else 1,int(c.split('_')[1]))

side,exc,split,bj,overL=map(load,(SIDE,EXC,SPLIT,BJ,OVERL))
if side['counts']['source_count']!=26 or exc['counts']['source_count']!=26: raise SystemExit('source count moved')
if side['counts']['nontrivial_source_side_function_count']!=120 or exc['counts']['nontrivial_source_exceptional_function_count']!=120:
    raise SystemExit('120+120 function-package prefix moved')
if overL['summary']['total_offboundary_carrier_prime_divisors_over_L']!=24:
    raise SystemExit('24-prime over-L inventory moved')
if overL['summary']['quartic_offboundary_prime_strict_transforms_over_L']!=12:
    raise SystemExit('quartic prime count moved')
if bj['hyperplane_decomposition']['total_genus1_prime_divisors']!=12:
    raise SystemExit('b_j prime count moved')

# Frozen 33 projective ambient-linear carriers.
carrier_by_key={}; carrier_by_index={}
for r in split['carrier_records']:
    k=canon_vector(sparse_to_vector(r['ambient_linear_form']))
    if k in carrier_by_key: raise SystemExit('duplicate projective carrier')
    carrier_by_key[k]=r; carrier_by_index[int(r['carrier_index_1based'])]=r
if len(carrier_by_key)!=33: raise SystemExit('33-carrier atlas moved')

# Expand the 15 off-boundary carrier hyperplanes to the exact 24 prime divisors.
prime_map=defaultdict(list); prime_records=[]
for br in bj['branch_records']:
    idx=int(br['carrier_index_1based']); sigma=int(br['sigma']); tau=int(br['tau'])
    pid=f'BJ_C{idx:02d}_S{sigma:+d}_T{tau:+d}'
    prime_map[idx].append(pid)
    prime_records.append({
      'prime_id':pid,'kind':'BJ_GENUS1','carrier_index_1based':idx,
      'carrier_hyperplane':br['carrier_hyperplane'],'sigma':sigma,'tau':tau,
      'field':'Q(i) subset L','degree':int(br['degree']),'genus':int(br['genus']),
      'prime_over_L':True,
    })
if len(prime_records)!=12 or sorted(len(v) for v in prime_map.values())!=[4,4,4]:
    raise SystemExit('b_j four-branch prime expansion moved')
quartic_indices=[]
for gr in overL['group_records']:
    gid=gr['group_id']
    if not gr['irreducible_over_L_t_y'] or gr['prime_components_per_carrier_over_L']!=1:
        raise SystemExit(f'quartic primality moved: {gid}')
    for idx in gr['carrier_indices_1based']:
        idx=int(idx); pid=f'QH_C{idx:02d}'
        if idx in prime_map: raise SystemExit('quartic carrier collided with b_j carrier')
        prime_map[idx]=[pid]; quartic_indices.append(idx)
        prime_records.append({
          'prime_id':pid,'kind':'QUARTIC_NORM_PRIME','carrier_index_1based':idx,
          'Kummer_group_id':gid,'field':'L=Q(i,sqrt(2))','prime_over_L':True,
          'base_normalization_genus':int(gr['base_normalization_genus']),
        })
if len(set(quartic_indices))!=12: raise SystemExit('12 quartic prime carriers moved')
prime_records.sort(key=lambda r:(0 if r['kind']=='BJ_GENUS1' else 1,r['carrier_index_1based'],r.get('sigma',0),r.get('tau',0)))
prime_ids=[r['prime_id'] for r in prime_records]
if len(prime_ids)!=24 or len(set(prime_ids))!=24: raise SystemExit('24-prime id inventory failed')

# Collect source/component/carrier valuations from the 240 boundary function packages.
sources={}
raw_occurrences=0; offboundary_carrier_occurrences=0

def ensure_source(name,order):
    d=sources.setdefault(name,{'raw_order':int(order),'components':defaultdict(Counter)})
    if d['raw_order']!=int(order): raise SystemExit(f'raw order mismatch {name}')
    return d

def add_factor(name,order,component,vec,multiplicity):
    global raw_occurrences,offboundary_carrier_occurrences
    d=ensure_source(name,order); k=canon_vector(vec)
    if k not in carrier_by_key: raise SystemExit(f'ambient factor escaped 33-carrier atlas: {name} {component}')
    row=carrier_by_key[k]; idx=int(row['carrier_index_1based'])
    d['components'][component][idx]+=int(multiplicity)
    raw_occurrences+=1
    if not row['boundary_only']: offboundary_carrier_occurrences+=1

for sr in side['source_ambient_side_lifts']:
    name=sr['source_basis_name']; order=int(sr['raw_order'])
    for pkg in sr['side_ambient_function_lifts']:
        comp=pkg['component_id']
        for f in pkg['numerator_factors']:
            add_factor(name,order,comp,[z(x) for x in f['ambient_linear_factor_coefficients_L_basis']],int(f['exponent']))
        add_factor(name,order,comp,[z(x) for x in pkg['D_coefficients_L_basis']],-int(pkg['denominator']['exponent']))
for sr in exc['source_ambient_exceptional_lifts']:
    name=sr['source_basis_name']; order=int(sr['raw_order'])
    for pkg in sr['exceptional_ambient_tangent_function_lifts']:
        comp=pkg['component_id']
        for f in pkg['numerator_factors']:
            add_factor(name,order,comp,[z(x) for x in f['ambient_tangent_linear_factor_coefficients_L_basis']],int(f['exponent']))
        add_factor(name,order,comp,[z(x) for x in pkg['ambient_projection_R0_R1_coefficients_L_basis'][1]],-int(pkg['denominator']['exponent']))

if len(sources)!=26: raise SystemExit('26-source union moved')
orders=Counter(d['raw_order'] for d in sources.values())
if orders!={2:17,4:9}: raise SystemExit(f'17+9 order partition moved: {orders}')
if raw_occurrences!=720: raise SystemExit(f'720 carrier occurrences moved: {raw_occurrences}')
if offboundary_carrier_occurrences!=190: raise SystemExit(f'190 offboundary carrier occurrences moved: {offboundary_carrier_occurrences}')

# Expand carrier valuations to prime valuations.  b_j carrier valuations repeat on
# all four strict-transform prime components; quartic carriers remain one-to-one.
tensor={}; sparse_entries=[]; source_summary=[]
nonzero_source_prime_cells=0; automatic_zero_cells=0; component_prime_entries=0
collapsed_nonzero_cells=0; collapsed_balanced_but_component_nonzero=0
order_cell_hist=Counter(); kind_cell_hist=Counter(); kind_entry_hist=Counter(); valuation_hist=Counter()
for name in sorted(sources,key=source_sort):
    d=sources[name]; n=d['raw_order']; by_prime={pid:Counter() for pid in prime_ids}
    for comp,cvals in d['components'].items():
        for idx,m in cvals.items():
            if idx not in prime_map or m==0: continue
            for pid in prime_map[idx]: by_prime[pid][comp]+=int(m)
    rows=[]; nz_cells=0; nz_entries=0
    for pid in prime_ids:
        vals=by_prime[pid]
        modrows=[]
        for comp,m in sorted(vals.items(),key=lambda kv:component_sort(kv[0])):
            if m==0: continue
            mod=m%n
            if mod:
                modrows.append({'boundary_component_id':comp,'valuation_integer':int(m),'valuation_mod_order':int(mod)})
                sparse_entries.append({'source_basis_name':name,'source_order':n,'offboundary_prime_id':pid,'boundary_component_id':comp,'valuation_integer':int(m),'valuation_mod_order':int(mod)})
                nz_entries+=1; component_prime_entries+=1; valuation_hist[f'order{n}_mod{mod}']+=1
        if modrows:
            nz_cells+=1; nonzero_source_prime_cells+=1; order_cell_hist[str(n)]+=1
            kind=next(r['kind'] for r in prime_records if r['prime_id']==pid)
            kind_cell_hist[f'order{n}_{kind}']+=1; kind_entry_hist[f'order{n}_{kind}']+=len(modrows)
            collapsed=sum(x['valuation_integer'] for x in modrows)%n
            if collapsed: collapsed_nonzero_cells+=1
            else: collapsed_balanced_but_component_nonzero+=1
            rows.append({'offboundary_prime_id':pid,'nonzero_boundary_component_valuations':modrows,'collapsed_integer_sum_mod_order':int(collapsed),'actual_Gersten_residue_status':'PENDING_BOUNDARY_UNIFORMIZER_CLASS_CONTRACTION'})
    automatic=24-nz_cells; automatic_zero_cells+=automatic
    source_summary.append({'source_basis_name':name,'source_order':n,'candidate_offboundary_prime_cells':nz_cells,'valuation_automatic_zero_prime_cells':automatic,'nonzero_component_prime_entries':nz_entries})
    tensor[name]={'source_order':n,'candidate_prime_records':rows}

if nonzero_source_prime_cells!=140 or automatic_zero_cells!=484: raise SystemExit(f'624-cell split moved: {nonzero_source_prime_cells}+{automatic_zero_cells}')
if component_prime_entries!=262: raise SystemExit(f'262 sparse tensor entries moved: {component_prime_entries}')
if order_cell_hist!=Counter({'2':122,'4':18}): raise SystemExit(f'order cell histogram moved: {order_cell_hist}')
if kind_cell_hist!=Counter({'order2_BJ_GENUS1':72,'order2_QUARTIC_NORM_PRIME':50,'order4_QUARTIC_NORM_PRIME':18}): raise SystemExit(f'prime-kind cell histogram moved: {kind_cell_hist}')
if kind_entry_hist!=Counter({'order2_BJ_GENUS1':96,'order2_QUARTIC_NORM_PRIME':94,'order4_QUARTIC_NORM_PRIME':72}): raise SystemExit(f'prime-kind entry histogram moved: {kind_entry_hist}')
if valuation_hist!=Counter({'order2_mod1':190,'order4_mod1':36,'order4_mod3':36}): raise SystemExit(f'valuation histogram moved: {valuation_hist}')
if collapsed_nonzero_cells!=70 or collapsed_balanced_but_component_nonzero!=70:
    raise SystemExit(f'collapsed diagnostic split moved: {collapsed_nonzero_cells}+{collapsed_balanced_but_component_nonzero}')

cert={
 'schema':'STAGE33_07_OFFBOUNDARY_PRIME_VALUATION_TENSOR_26X24_OVER_L_V1',
 'source_locks':{
   'side_ambient_lifts_sha256':EXPECTED[SIDE.name],'exceptional_ambient_lifts_sha256':EXPECTED[EXC.name],
   'carrier_boundary_offboundary_split_sha256':EXPECTED[SPLIT.name],'bj_genus1_decomposition_sha256':EXPECTED[BJ.name],
   'six_Kummer_nonsquare_over_L_sha256':EXPECTED[OVERL.name],
 },
 'field':'L=Q(i,sqrt(2))',
 'dimensions':{'source_count':26,'offboundary_prime_count':24,'source_prime_cell_count':624,'boundary_component_count':72},
 'prime_inventory':prime_records,
 'source_summary':source_summary,
 'sparse_valuation_tensor_entries':sparse_entries,
 'source_prime_tensor':tensor,
 'exact_counts':{
   'nontrivial_boundary_function_packages':240,
   'ambient_linear_carrier_occurrences_all':720,
   'offboundary_carrier_occurrences_before_prime_expansion':190,
   'offboundary_prime_expanded_component_entries_nonzero_mod_source_order':262,
   'source_prime_cells_nonzero_at_valuation_level':140,
   'source_prime_cells_automatic_zero_by_valuation':484,
   'order2_candidate_cells':122,'order4_candidate_cells':18,
   'order2_BJ_candidate_cells':72,'order2_quartic_candidate_cells':50,'order4_quartic_candidate_cells':18,
   'collapsed_integer_sum_nonzero_cells_diagnostic_only':70,
   'collapsed_integer_sum_zero_but_component_vector_nonzero_cells_diagnostic_only':70,
   'valuation_mod_order_histogram':dict(sorted(valuation_hist.items())),
 },
 'residue_firewall':{
   'valuation_zero_cell_rule':'if every boundary-component valuation is 0 modulo the source order, the off-boundary residue is automatically trivial for any choice of boundary uniformizers',
   'candidate_cell_rule':'a nonzero valuation vector does not imply a nonzero Gersten residue; it must be contracted with the restrictions of the 72 boundary uniformizers in k(E)^*/k(E)^{*n}',
   'collapsed_integer_sum_is_not_a_residue_test':True,
   'global_Gersten_lift_credit_from_this_leaf':False,
 },
 'exact_checks':{
   'all_720_ambient_factor_occurrences_match_the_frozen_33_carrier_atlas':True,
   'exact_offboundary_carrier_occurrence_count_is_190':True,
   '24_prime_inventory_over_L_is_12_BJ_plus_12_quartic':True,
   'all_three_bj_carriers_expand_to_four_prime_components':True,
   'all_twelve_quartic_carriers_expand_to_one_prime_over_L':True,
   '26_by_24_cell_split_is_exactly_140_candidate_plus_484_automatic_zero':True,
   'sparse_component_prime_tensor_has_262_nonzero_mod_order_entries':True,
   'order_partition_is_17_order2_plus_9_order4':True,
   'no_residue_nonvanishing_is_inferred_from_scalar_or_component_valuations_alone':True,
 },
 'constructive_progress':{
   'off_boundary_prime_divisor_decomposition_over_L_fully_closed':True,
   'off_boundary_carrier_prime_divisor_count_over_L':24,
   'offboundary_26x24_valuation_tensor_materialized':True,
   'offboundary_source_prime_cells_automatic_zero_by_valuation':484,
   'offboundary_source_prime_cells_requiring_uniformizer_contraction':140,
   'boundary_uniformizer_squareclass_matrix_on_24_primes_materialized':False,
   'off_boundary_codimension1_residue_certificates_materialized_count':0,
   'global_geometric_Gersten_lifts_materialized_count':0,
   'project_14x26_L_squareclass_tensor_materialized':False,
   'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False,
 },
 'new_smallest_exact_kernel':'R33-BR2A-140-OFFBOUNDARY-SOURCE-PRIME-RESIDUE-CELLS-BOUNDARY-UNIFORMIZER-SQUARECLASS-CONTRACTION',
 'next_exact_leaf':'L33-07-MATERIALIZE-72-BY-24-BOUNDARY-UNIFORMIZER-RESTRICTION-SQUARECLASSES-OVER-L-AND-CONTRACT-140-RESIDUE-CELLS',
 'stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
}
cert['canonical_sha256']=sha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({
 'success':True,'tensor_shape':'26x24x72 sparse','source_prime_cells':'140 candidate + 484 automatic-zero',
 'nonzero_sparse_entries':262,'candidate_cells_by_order':'122 order2 + 18 order4',
 'certificate_sha256':cert['canonical_sha256'],'next_exact_leaf':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
