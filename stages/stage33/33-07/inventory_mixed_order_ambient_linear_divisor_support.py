#!/usr/bin/env python3
"""Inventory the finite ambient-linear carrier envelope behind the 26 mixed-order
boundary-function packages.

This does not multiply the component packages into a global Gersten lift.  It
only canonicalizes every ambient linear numerator/pole form already certified
on the 24 side and 48 exceptional components, records where it occurs, and
checks its incidence with the 48 frozen nodes.  The result is the exact finite
carrier list on which the next off-boundary codimension-one residue analysis
must operate.
"""
import hashlib,json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
SIDE=HERE/'mixed-order-side-ambient-function-lifts.json'
EXC=HERE/'mixed-order-exceptional-ambient-tangent-function-lifts.json'
OUT=HERE/'mixed-order-ambient-linear-divisor-support.json'
SIDE_SHA='2f137842fffbabe7fa9f91879f379e0662803204d6753c342fc31f6dfe12fa6d'
EXC_SHA='a9d5ceb66625dfa561db61a3afc95388bf5a8371fb81905988991514a765d397'
COORDS=['a1','a2','a3','b1','b2','b3','c']

def canonsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(path,sha):
    x=json.load(open(path)); assert x['canonical_sha256']==sha
    body=dict(x); body.pop('canonical_sha256'); assert canonsha(body)==sha
    return x

def z(z): return (Fraction(int(z[0]),int(z[1])),Fraction(int(z[2]),int(z[3])))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def inv(x):
    d=x[0]*x[0]+x[1]*x[1]; assert d
    return (x[0]/d,-x[1]/d)
def enc(x): return [x[0].numerator,x[0].denominator,x[1].numerator,x[1].denominator]
def vec(v): return [z(x) for x in v]
def norm(v):
    v=vec(v); p=next((x for x in v if x!=(0,0)),None); assert p is not None
    q=inv(p); return tuple(tuple(enc(mul(q,x))) for x in v)
def key(v): return json.dumps(norm(v),separators=(',',':'))
def dot(v,p):
    s=(Fraction(0),Fraction(0))
    for a,b in zip(vec(v),vec(p)): s=add(s,mul(a,b))
    return s

def den_side(pkg): return pkg['D_coefficients_L_basis']
def den_exc(pkg): return pkg['ambient_projection_R0_R1_coefficients_L_basis'][1]

side=load(SIDE,SIDE_SHA); exc=load(EXC,EXC_SHA)
assert side['ambient_coordinate_order']==COORDS and exc['ambient_coordinate_order']==COORDS
nodes={m['exceptional_id']:m['node_point_ambient_P6_L_basis'] for m in exc['exceptional_ambient_projection_models']}
assert len(nodes)==48

by_source={f'A2_{i:02d}':[] for i in range(1,27)}
all_forms={}

def add_occ(source,order,component,kind,multiplicity,v,edge=None):
    k=key(v); n=norm(v)
    zeros=[eid for eid,p in nodes.items() if dot(n,p)==(0,0)]
    occ={'source_basis_name':source,'raw_order':order,'component_id':component,'kind':kind,
         'signed_multiplicity':int(multiplicity),'canonical_linear_form_L_basis':[list(x) for x in n],
         'vanishing_exceptional_node_count':len(zeros),'vanishing_exceptional_node_ids':zeros}
    if edge is not None: occ['edge_id']=edge
    by_source[source].append(occ)
    row=all_forms.setdefault(k,{'canonical_linear_form_L_basis':[list(x) for x in n],'occurrences':0,
                                'sources':set(),'components':set(),'numerator_occurrences':0,'denominator_occurrences':0,
                                'vanishing_exceptional_node_ids':zeros})
    assert row['vanishing_exceptional_node_ids']==zeros
    row['occurrences']+=1; row['sources'].add(source); row['components'].add(component)
    row['numerator_occurrences']+=kind=='numerator'; row['denominator_occurrences']+=kind=='denominator'

for sr in side['source_ambient_side_lifts']:
    source=sr['source_basis_name']; order=int(sr['raw_order'])
    for pkg in sr['side_ambient_function_lifts']:
        for f in pkg['numerator_factors']:
            add_occ(source,order,pkg['component_id'],'numerator',f['exponent'],f['ambient_linear_factor_coefficients_L_basis'],f['edge_id'])
        add_occ(source,order,pkg['component_id'],'denominator',-int(pkg['denominator']['exponent']),den_side(pkg))
for sr in exc['source_ambient_exceptional_lifts']:
    source=sr['source_basis_name']; order=int(sr['raw_order'])
    for pkg in sr['exceptional_ambient_tangent_function_lifts']:
        for f in pkg['numerator_factors']:
            add_occ(source,order,pkg['component_id'],'numerator',f['exponent'],f['ambient_tangent_linear_factor_coefficients_L_basis'],f['edge_id'])
        add_occ(source,order,pkg['component_id'],'denominator',-int(pkg['denominator']['exponent']),den_exc(pkg))

rows=[]
for k,row in all_forms.items():
    row['sources']=sorted(row['sources'],key=lambda s:int(s.split('_')[1]))
    row['components']=sorted(row['components'])
    row['source_count']=len(row['sources']); row['component_count']=len(row['components'])
    rows.append(row)
rows.sort(key=lambda r:json.dumps(r['canonical_linear_form_L_basis'],separators=(',',':')))
source_summary=[]
for s,occs in by_source.items():
    orders={o['raw_order'] for o in occs}; assert len(orders)==1
    source_summary.append({'source_basis_name':s,'raw_order':next(iter(orders)),
        'linear_form_occurrence_count':len(occs),'distinct_projective_linear_form_count':len({json.dumps(o['canonical_linear_form_L_basis'],separators=(',',':')) for o in occs}),
        'components_with_ambient_function_package':len({o['component_id'] for o in occs}),
        'numerator_occurrence_count':sum(o['kind']=='numerator' for o in occs),
        'denominator_occurrence_count':sum(o['kind']=='denominator' for o in occs)})
assert len(source_summary)==26

cert={'schema':'STAGE33_07_MIXED_ORDER_AMBIENT_LINEAR_DIVISOR_SUPPORT_V1',
 'source_locks':{'side_ambient_lifts_sha256':SIDE_SHA,'exceptional_ambient_lifts_sha256':EXC_SHA},
 'scope':'finite ambient-linear carrier envelope only; no global Gersten lift or off-boundary residue vanishing is inferred',
 'ambient_coordinate_order':COORDS,'source_count':26,'raw_order_partition':{'2':17,'4':9},
 'distinct_projective_ambient_linear_forms':len(rows),'total_linear_form_occurrences':sum(r['occurrences'] for r in rows),
 'source_summary':source_summary,'ambient_linear_form_inventory':rows,
 'exact_checks':{'all_26_sources_present':True,'all_occurring_forms_projectively_canonicalized_over_Qi':True,
                 'all_forms_tested_on_all_48_frozen_nodes':True,'side_and_exceptional_denominators_included':True,
                 'no_global_lift_credit_from_carrier_inventory':True},
 'constructive_progress':{'all_72_boundary_component_function_packages_ambientized':True,
    'ambient_linear_carrier_inventory_materialized':True,'global_geometric_Gersten_lifts_materialized_count':0,
    'off_boundary_codimension1_residue_certificates_materialized_count':0,'project_14x26_L_squareclass_tensor_materialized':False,
    'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False},
 'new_smallest_exact_kernel':'R33-BR2A-AMBIENT-LINEAR-CARRIERS-26-GLOBAL-GERSTEN-OFF-BOUNDARY-RESIDUE-CANCELLATION',
 'next_exact_leaf':'L33-07-FACTOR-AMBIENT-LINEAR-CARRIER-SECTIONS-ON-SURFACE-AND-SEPARATE-BOUNDARY-VS-OFF-BOUNDARY-COMPONENTS',
 'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False}
cert['canonical_sha256']=canonsha(cert); OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'sources':26,'distinct_projective_ambient_linear_forms':len(rows),
 'total_linear_form_occurrences':cert['total_linear_form_occurrences'],'global_Gersten_lifts':'0/26',
 'certificate_sha256':cert['canonical_sha256'],'next_exact_leaf':cert['next_exact_leaf']},indent=2,sort_keys=True))
