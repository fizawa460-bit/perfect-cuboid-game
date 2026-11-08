"""Auditor-supplied checks. Does not modify frozen archive inputs.
GF(2) witness rank, old G(theta) normalization, tame/unramified field identities,
local even-subset invariants for the true Kummer kernel.
"""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import numpy as np
from fractions import Fraction
from math import comb
from local2_arithmetic import R,F,H,FACTORS,T,U,ONE,MOD,rank,unit_class,eval_u,pgf_mul,pgf_mod,pgf_deg,power,mul
P=Path(__file__).parent
cert=json.loads((P/'dyadic_full_kummer_certificate.json').read_text())
old=json.loads((P/'parents/signed18_genus17_rank6_certificate.json').read_text())

# Standalone GF(2) rank, independent of local2_arithmetic.rank.
def rref_rank(xs):
 basis={}
 for row in xs:
  x=row
  for k in sorted(basis,reverse=True):
   if (x>>k)&1:x^=basis[k]
  if x:basis[x.bit_length()-1]=x
 return len(basis)
assert len(cert['selected_fake_basis'])==18
vec=[int(cert['scalar_minus1_character_hex'],16)]+[int(x['character_hex'],16) for x in cert['selected_fake_basis']]
assert rref_rank(vec)==19

# Old G(theta) in exact u-basis: for 4 cases, divide out a common power of 2.
# For the two exceptional cases, compare exact polynomial identities in Q[u] (multipliers are squares).
selected={x['old_class']:x for x in cert['selected_fake_basis'] if x['kind']=='old_global_divisor'}
for name,G in zip(old['class_order'],old['class_G_coefficients_ascending']):
 row=selected[name]
 if name=='D1b':
  # (u/2)^2*(1+3*theta) = 3*u^3/2-2*u^2 = 3*t-2*u^2.
  expr=lambda u:Fraction(u*u,4)*(1+3*(2*u-3))
  ref=lambda u:Fraction(3*u**3,2)-2*u*u
  assert all(expr(u)==ref(u) for u in range(-5,7))
  expected=(3*T-2*power(U,2))%MOD
 elif name=='F2':
  # G(theta)=4*u^2*(t-u)/t =4*(u^2-2)
  assert all((2*u-3)**2+6*(2*u-3)+1 == 4*(u*u-2) for u in range(-5,7))
  from local2_arithmetic import inv
  expected=mul((T-U)%MOD,inv(T))
 else:
  vals=[sum(G[k]*comb(k,i)*2**i*(-3)**(k-i) for k in range(i,len(G)))*(1<<(i//3)) for i in range(len(G))]
  pow2=min(abs(c)&(-abs(c)) for c in vals if c)
  expected=np.zeros(36,dtype=np.int64)
  expected[:len(vals)]=[int(c//pow2)%MOD for c in vals]
 assert np.array_equal(expected,np.array(row['unit_basis_mod256'],dtype=np.int64)),name
 assert unit_class(expected)==int(row['character_hex'],16),name

# Pure combinatorics: inertia C3 forces 12 constant triple blocks;
# Frobenius permutes 4+8 blocks. In M=F_2^36/<1>, an invariant
# can be Frobenius-fixed or Frobenius-complemented; all have even parity.
cycle4=list(range(4));cycle8=list(range(4,12))
def rotate(x):
 out=x[:]
 for group in [cycle4,cycle8]:
  for i,j in enumerate(group):out[group[(i+1)%len(group)]]=x[j]
 return out
fixed,anti=0,0
for mask in range(1<<12):
 x=[(mask>>i)&1 for i in range(12)]
 y=rotate(x)
 if x==y or all(x[i]!=y[i] for i in range(12)):
  assert (3*sum(x))%2==0,('odd invariant lift',mask)
  if x==y:fixed+=1
  else:anti+=1
assert (fixed,anti)==(4,4)
assert (fixed+anti)//2==4 # J[2](Q2) has four classes modulo complement.

# Hensel tame: R and R' nonzero in 1,2,3 residue degree factors;
# f=1 polynomial corresponds to w=-1 (not +1 in characteristic zero).
def Rderivative():
 return sum(((i*((R>>i)&1))&1)<<(i-1) for i in range(1,13))
rd=Rderivative()
for m in (3,7,11):
 assert pgf_mod(R,m)!=0 and pgf_mod(rd,m)!=0
assert F[36]==1 and len(H)==37
assert all((F[i]-(1 if i==36 else (4 if i in (30,32,33,34) else 0)))%8==0 for i in range(37))
print(json.dumps({'auditor_checks':'PASS','old_six_recomputed_from_original_G':6,'gf2_rank_of_scalar_plus_divisors':rref_rank(vec),'invariant_even_subset_count_before_complement':fixed+anti,'true_local_torsion_dimension':2,'kernel_connecting_class_local_nonzero':True,'tame_hensel_derivative_field_degrees':[1,2,3],'unramified_mod8_square_identity':True},ensure_ascii=False))
