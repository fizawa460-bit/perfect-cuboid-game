#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name('j2-naive-cv-branch-to-e2-kummer-rejection.json')
c=json.loads(p.read_text())

# Low-degree-first polynomial helpers over Z[t].
def add(a,b):
 n=max(len(a),len(b)); o=[0]*n
 for i in range(n): o[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
 while len(o)>1 and o[-1]==0:o.pop()
 return o
def sub(a,b):
 n=max(len(a),len(b)); o=[0]*n
 for i in range(n): o[i]=(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
 while len(o)>1 and o[-1]==0:o.pop()
 return o
def mul(a,b):
 o=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b): o[i+j]+=x*y
 while len(o)>1 and o[-1]==0:o.pop()
 return o
def scale(a,k): return [k*x for x in a]

one=[1]; t=[0,1]; t2=[0,0,1]; t4=[0,0,0,0,1]
H=add(sub(t4,scale(t2,4)),one)
c0=add(H,one)
t2m1=sub(t2,one)
Dplus=sub(sub(t2,scale(t,2)),one)

# beta+beta'=-H/t^2 and beta*beta'=1 imply
# (t^2 beta+c)(t^2 beta'+c)=t^4-cH+c^2=2(t^2-1)^2.
lhs=add(sub(t4,mul(c0,H)),mul(c0,c0))
rhs=scale(mul(t2m1,t2m1),2)
assert lhs==rhs

# Including ell's prefactor gives 32/Dplus^2, hence squareclass 2.
assert c['naive_partition_character_test']['reciprocal_pair_product']=='32/(t^2-2*t-1)^2'
assert c['naive_partition_character_test']['resulting_naive_split_E2_character_triple']==['1','2','2']
assert c['geometric_base_change_test']['naive_H1_E2_class_geometrically_trivial'] is True
assert c['geometric_base_change_test']['named_J2_geometrically_nontrivial'] is True
assert c['exact_conclusion']['previous_full_E2_kummer_from_hilbert90_route_rejected'] is True
assert c['j2_marked_brauer_coordinate_selected'] is False
assert c['stage33_12_closed_exact'] is False
assert c['stage33_13_released'] is False
print('PASS j2 naive CV branch-to-E2 Kummer rejection')
