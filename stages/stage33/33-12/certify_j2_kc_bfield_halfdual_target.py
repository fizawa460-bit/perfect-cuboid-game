#!/usr/bin/env python3
"""Verify the exact marked Br(Kc)[2] half-dual target for T(Kc)=diag(4,8)."""
from fractions import Fraction
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent
SRC=H/'j2-kc-transcendental-lattice-isometry.json'
OUT=H/'j2-kc-bfield-halfdual-target.json'
SRC_SHA='b7f2bcfa29c01731ea2f10d22db898ad57317f140b547f91e3d3a27a0faf1010'
OUT_SHA='28180fae13a24e4d06018703aff574db801486fa6130e83c6b6db215c32b1fdb'
def sh(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def canonical_ok(p,expected):
 o=json.loads(p.read_text()); got=o.pop('canonical_sha256'); assert got==expected==sh(o); return json.loads(p.read_text())
s=canonical_ok(SRC,SRC_SHA); o=canonical_ok(OUT,OUT_SHA)
G=s['transcendental_lattice_isometry_gram']; assert G==[[4,0],[0,8]]
assert o['marked_transcendental_lattice']['gram']==G
assert o['marked_transcendental_lattice']['dual_basis']==['t1/4','t2/8']
# Br[2]=Hom(T,Z/2)=(1/2 T*)/T*.  In coordinates relative to t1,t2,
# beta1=t1/8 and beta2=t2/16 pair to 1/2 with t1,t2 respectively.
breps=[(Fraction(1,8),Fraction(0)),(Fraction(0),Fraction(1,16))]
for j,b in enumerate(breps):
 vals=[]
 for k in range(2):
  pair=sum(b[r]*G[r][k] for r in range(2))
  assert pair.denominator in (1,2)
  vals.append(int((2*pair)%2))
 assert vals==o['brauer_2torsion_target']['marked_basis'][j]['functional_on_t_basis']
# 2*B lies in T* for every basis B, while B itself does not.
dual=[(Fraction(1,4),0),(0,Fraction(1,8))]
for b,d in zip(breps,dual): assert tuple(2*x for x in b)==d and b!=d
assert o['brauer_2torsion_target']['nonzero_candidates']==[
 {'functional_on_t_basis':[1,0],'label':'beta1'},
 {'functional_on_t_basis':[0,1],'label':'beta2'},
 {'functional_on_t_basis':[1,1],'label':'beta1+beta2'}]
# A_T[2]=(T*/T)[2] is a different quotient; verify its three nonzero reps and q values.
areps=[(Fraction(1,2),0),(0,Fraction(1,2)),(Fraction(1,2),Fraction(1,2))]
q=[]
for a in areps:
 qa=sum(a[r]*G[r][c]*a[c] for r in range(2) for c in range(2))
 q.append(str(int(qa%2)))
assert q==o['discriminant_2torsion_comparison']['quadratic_values_mod_2']==['1','0','1']
assert o['discriminant_2torsion_comparison']['same_quotient_as_Br2'] is False
assert o['exact_consequence']['named_j2_brauer_coordinate_materialized'] is False
assert o['exact_consequence']['two_cycle_evaluations_always_determine_nonzero_class'] is True
assert all(v is False for v in o['firewalls'].values())
print('STAGE33_12_J2_KC_BFIELD_HALFDUAL_TARGET=PASS_EXACT')
print('BR2_MARKED_BASIS=beta1:t1/8,beta2:t2/16')
print('NONZERO_FUNCTIONALS=[1,0],[0,1],[1,1]')
print('CERTIFICATE_SHA256='+OUT_SHA)
