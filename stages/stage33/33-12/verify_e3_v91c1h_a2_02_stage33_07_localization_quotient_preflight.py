#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; S33=H.parent; S07=S33/'33-07'
CERT=H/'e3-v91c1h-a2-02-stage33-07-localization-quotient-preflight.json'
V1G=H/'e3-v91c1g-a2-02-v4-naturality-fixed-subspace-preflight.json'
BR=S07/'proper-brauer2-from-discriminant.json'; IB=S07/'two-primary-residue-invariant-basis.json'
LOC=S07/'materialize_order2_localization_receiver.py'; BOC=S07/'certify_order2_quotient_raw_order4_bockstein.py'
EXPECTED='d05672463ce6340773b6a4394851398360cf58b03f544ea4c00ff0d345089be2'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
c=load(CERT,EXPECTED); g=load(V1G,'2a176993614fac6f4b1555855794642702f3eeb055d710b8f04ac5097e9fb370'); br=load(BR,'c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf'); ib=load(IB,'f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939')
assert c['entry_authority']['pr']==1649 and c['entry_authority']['hostile_audit_review']==5123633478 and c['entry_authority']['merge_commit']=='43f3f3b135a2f5664cb8cc736d6db0b37d7b79da'
assert g['proper14_fixed_subspace_test']['joint_v4_fixed_dimension_f2']==10 and g['proper14_fixed_subspace_test']['e3_target_mask_decimal']==20
assert br['proper_Br2_joint_v4_fixed_dimension_f2']==10 and br['full_absolute_localization_connecting_map_computed'] is False
assert ib['arithmetic_localization_connecting_map_computed'] is False and ib['absolute_H1_identified_with_finite_V4_H1'] is False
lt=LOC.read_text(); bt=BOC.read_text()
assert 'localization_extension_class_computed": False' in lt and 'localization_connecting_map_delta_loc_evaluated": False' in lt
assert 'project_14x26_L_squareclass_tensor_materialized": False' in bt and 'absolute_delta_loc_computed": False' in bt
r=c['stage33_07_route_audit']; assert r['localization_extension_class_computed'] is False and r['localization_connecting_map_delta_loc_evaluated'] is False and r['route_supplies_source_specific_marked_proper14_coordinate_for_A2_02'] is False
x=c['construction_result']; assert x['a2_02_marked_brauer_image_computed'] is False and x['a2_02_marked_brauer_image_equal_mask20'] is False and x['source_bound_marked_brauer_functional_materialized'] is False and x['e3_genuine_full_surface_h2_mu2_lift_materialized'] is False and x['e3_kummer_column_materialized'] is False
assert c['credit_firewall']['stage33_progress']=='6/11' and c['credit_firewall']['merge_allowed'] is False
print(json.dumps({'success':True,'marker':'V91C1H_STAGE33_07_LOCALIZATION_ROUTE_PREFLIGHT','certificate_sha256':EXPECTED,'next_exact_leaf':c['next_exact_leaf']},sort_keys=True))
