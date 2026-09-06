#!/usr/bin/env python3
"""Verify V91C1I: audited A2_02 localization zero is not a marked proper14 coordinate."""
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
CERT=HERE/'e3-v91c1i-a2-02-audited-localization-zero-fingerprint.json'
H=HERE/'e3-v91c1h-a2-02-stage33-07-localization-quotient-preflight.json'
G11=S33/'33-11g'/'stage33-11g-hostile-audit-exact-exit-certificate.json'
F11=S33/'33-11f'/'stage33-11f-26-column-exact-closure-certificate.json'
EXPECTED={H:'d05672463ce6340773b6a4394851398360cf58b03f544ea4c00ff0d345089be2',G11:'233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e',F11:'c7ba9a5a4a9475830e62276292abcdb89deb729a6aecab2c0b6f48a71a65f6e4'}

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,expected=None):
    o=json.loads(p.read_text())
    b=dict(o); claimed=b.pop('canonical_sha256')
    assert csha(b)==claimed
    if expected: assert claimed==expected
    return o

for p,h in EXPECTED.items(): load(p,h)
f=load(F11); g=load(G11); c=load(CERT,'241112a8dceaae61027b803438f3dd5b34f3f85387b95c02b6d490666011213c')
assert g['exact_result']['arithmetic_localization_connecting_map']=='COMPUTED_EXACT_ZERO_MAP'
assert g['exact_result']['connecting_columns_exact_audited']=='26/26'
assert g['exact_result']['unresolved_connecting_columns']==0
r=next(x for x in g['independent_replay']['columns'] if x['source_basis_name']=='A2_02')
assert r['column_1based']==2 and r['audited_status']=='ZERO_EXACT_AUDITED'
assert r['transport_kind']=='DIRECT_EXACT_GENERATOR'
fr=next(x for x in f['columns'] if x['source_basis_name']=='A2_02')
assert fr['absolute_receiver_value']==c['audited_localization_fact']['a2_02_absolute_receiver_value']
assert f['absolute_receiver']['coefficient_module']=='K=Br(Sbar)[2], dim_F2=14'
assert c['type_separation']['localization_output_type']=='ABSOLUTE_H1_CONNECTING_OBSTRUCTION_CLASS'
assert c['type_separation']['desired_marking_output_type']=='MARKED_GEOMETRIC_Br(Sbar)[2]_PROPER14_COORDINATE'
assert c['type_separation']['zero_localization_obstruction_identifies_marked_geometric_brauer_coordinate'] is False
assert c['type_separation']['zero_map_is_injective_on_26_source_directions'] is False
assert c['exact_consequence']['a2_02_marked_brauer_image_computed'] is False
assert c['exact_consequence']['a2_02_marked_brauer_image_equal_mask20'] is False
assert c['batch_continuation']['combined_hostile_audit_pending'] is True
assert c['batch_continuation']['audit_pass_credit'] is False
assert c['credit_firewall']['stage33_progress']=='6/11'
assert c['credit_firewall']['merge_allowed'] is False
print(json.dumps({'success':True,'certificate_sha256':c['canonical_sha256'],'a2_02_localization':'ZERO_EXACT_AUDITED','marked_proper14_image_computed':False,'stage33_progress':'6/11'},sort_keys=True))
