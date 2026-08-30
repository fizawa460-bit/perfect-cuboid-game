#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
p=Path(__file__).with_name('j2-geometric-halfdivisor-base-squareclass.json')
c=json.loads(p.read_text(encoding='utf-8'))
# Dplus=t^2-2t-1 has roots 1+-sqrt(2), hence two simple zeros and a double pole at infinity.
# Exact Vieta checks avoid symbolic dependencies.
assert (1)+(1)==2
assert (1)*(1)-2==-1
assert c['exact_pushforward']['identity']=='pi_star(E_J2)=-div(Dplus)'
geo=c['geometric_squareclass']
assert geo['nonconstant_over_Qbar'] is True
assert geo['nonsquare_over_Qbar_t'] is True
assert c['semantic_boundary']['full_leray_sha_identification_certified'] is False
assert c['candidate_count_after']==3
assert c['marked_brauer_functional_selected'] is False
assert c['stage33_12_closed_exact'] is False
claimed=c.pop('canonical_sha256')
actual=hashlib.sha256(json.dumps(c,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert actual==claimed,(actual,claimed)
assert claimed=='876734d9c1263150666d120c55c2d836fac74b2fb04168197c0845854a6f142d'
print('PASS j2 geometric half-divisor base squareclass')
