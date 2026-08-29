#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
p=Path(__file__).with_name('j2-d2-geometric-nontriviality-rejection.json')
c=json.loads(p.read_text(encoding='utf-8'))
ex=c['exact_conclusion']
assert c['status']=='PASS_EXACT_REJECTION'
assert c['upstream_facts']['j2_geometric_nontrivial'] is True
assert c['upstream_facts']['j2_exact_order']==2
assert ex['d_equals_2_named_j2_torsor_rejected'] is True
assert ex['j2_2isogeny_squareclass_selected'] is False
assert ex['j2_torsor_equation_materialized'] is False
assert ex['j2_2isogeny_kernel_membership_certified'] is False
assert ex['partial_norm_squareclass_2_role']=='ARITHMETIC_DESCENT_DATUM_ONLY_NOT_FULL_LERAY_SHA_COORDINATE'
assert c['stage33_12_closed_exact'] is False
assert c['stage33_13_released'] is False
claimed=c.pop('canonical_sha256')
actual=hashlib.sha256(json.dumps(c,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert actual==claimed,(actual,claimed)
assert claimed=='8e128315159812ec709c79840bd46e213df3cb22512056478294c8f4fa637d78'
print('PASS j2 d=2 geometric nontriviality rejection')
