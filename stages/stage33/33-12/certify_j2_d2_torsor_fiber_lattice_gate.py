#!/usr/bin/env python3
import json, math
from pathlib import Path
p=Path(__file__).with_name('j2-d2-torsor-fiber-lattice-gate.json')
c=json.loads(p.read_text())
# low-degree-first integer polynomial arithmetic
def mul(a,b):
 o=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b): o[i+j]+=x*y
 while len(o)>1 and o[-1]==0:o.pop()
 return o
def sub(a,b):
 n=max(len(a),len(b));o=[0]*n
 for i in range(n):o[i]=(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
 while len(o)>1 and o[-1]==0:o.pop()
 return o
t2=[0,0,1]; one=[1]; t4=[0,0,0,0,1]
r1=mul(sub(t2,one),sub(t2,one))
q=[1,0,-6,0,1]
assert sub(r1,q)==[0,0,4]
# Delta/16=r1^2*q^2*(r1-q)^2, giving finite orders 4 at 0,+-1 and 2 at four simple q roots.
assert c['jacobian']['euler_sum']==24
assert c['jacobian']['root_rank']==16
assert c['jacobian']['root_discriminant']==4**4*2**4
# Rank-two kernel fingerprints and Smith invariants.
for key,expected in {'0,1':(128,4,32),'1,0':(128,8,16),'1,1':(128,4,32)}.items():
 G=c['lattice_gate']['candidate_kernel_lattices'][key]['reduced_gram']
 det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
 g=0
 for row in G:
  for x in row:g=math.gcd(g,abs(x))
 assert (det,g,det//g)==expected
assert c['lattice_gate']['marked_brauer_functional_selected'] is False
assert c['stage33_12_closed_exact'] is False
assert c['stage33_13_released'] is False
print('PASS j2 d=2 torsor fiber/lattice gate')
