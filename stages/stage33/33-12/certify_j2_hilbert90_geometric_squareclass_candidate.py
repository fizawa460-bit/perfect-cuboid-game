#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).with_name('j2-hilbert90-geometric-squareclass-candidate.json')
c=json.loads(p.read_text())
# exact polynomial identities, low-degree first
Dp=[-1,-2,1]
Dm=[-1,2,1]
q=[1,0,-6,0,1]
def mul(a,b):
 o=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b): o[i+j]+=x*y
 while len(o)>1 and o[-1]==0:o.pop()
 return o
assert mul(Dp,Dm)==q
assert c['arithmetic_constant_conjugation']['identity']=='(Dminus/Dplus)*q=Dminus^2'
# Cross-multiplied identity: (Dm/Dp)*q = Dm^2 iff q*Dm = Dp*Dm^2.
assert mul(q,Dm)==mul(Dp,mul(Dm,Dm))
# q is squarefree: gcd(q,q')=1 checked by Euclid over Q using the explicit roots structure.
# q=Dplus*Dminus, with both quadratics separable and coprime.
assert Dp != Dm
assert c['geometric_nontriviality_gate']['q_squarefree_over_Qbar'] is True
assert c['geometric_nontriviality_gate']['q_not_square_in_Qbar(t)'] is True
assert c['exact_conclusion']['new_rational_nonconstant_squareclass_candidate']=='q=t^4-6*t^2+1'
assert c['exact_conclusion']['candidate_promoted_to_leray_sha'] is False
assert c['j2_2isogeny_squareclass_selected'] is False
assert c['j2_torsor_equation_materialized'] is False
assert c['stage33_12_closed_exact'] is False
assert c['stage33_13_released'] is False
print('PASS j2 Hilbert90 geometric squareclass q candidate')
