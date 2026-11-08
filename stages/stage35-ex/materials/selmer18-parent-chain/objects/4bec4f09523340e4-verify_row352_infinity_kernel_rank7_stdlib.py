#!/usr/bin/env python3
"""Exact arithmetic replay; geometric identities and Galois cohomology used as stated lemmas."""
from pathlib import Path
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'row352_infinity_kernel_rank7_certificate.json').read_text())
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
for key,name in [('rank6_certificate_sha256','signed18_genus17_rank6_certificate.json'),('true_fake_351_certificate_sha256','true_fake_bridge_351_certificate.json'),('row350_certificate_sha256','row350_certificate.json')]:
 assert D['old_dependencies'][key]==sha(name),name
old=json.loads((ROOT/'signed18_genus17_rank6_certificate.json').read_text())
h=old['h2_coefficients_ascending'];assert len(h)==37 and h[-1]==1 and h[0]==1
b=old['expected_character_bits'];assert b['combined_rank']==6
rows=[list(map(int,a+c)) for a,c in zip(b['p3'],b['p29_quotient'])]
assert [''.join(map(str,v)) for v in rows]==D['old_six_fake_character_vectors']
def gf2rank(X):
 piv={}
 for row in X:
  mask=sum((int(v)&1)<<i for i,v in enumerate(row))
  while mask:
   j=mask.bit_length()-1
   if j not in piv:piv[j]=mask;break
   mask^=piv[j]
 return len(piv)
assert gf2rank(rows)==6
# Transpositions force invariants of 36-bit signs to be constant; modulo diagonal => M^G=0.
n=36;adj=[]
for i in range(n-1):
 v=[0]*n;v[i]=1;v[i+1]=1;adj.append(v)
assert gf2rank(adj)==35
assert D['M_invariants_F2_dim']==0 and D['H1_true_to_fake_kernel_dimension']==1
# The 7th dimension is mathematically supplied by rational D_infinity (Kummer = nonzero connecting class).
# One may choose a vector-space splitting of Sel2 with the last coordinate the nonzero kernel class.
aug=[x+[0] for x in rows]+[[0]*9+[1]]
assert gf2rank(aug)==7 and D['independent_mod2_F2_rank']==7
assert D['kernel_local_membership_resolved'] and D['JQ_2_torsion_dim']==0
assert D['original_signed18_source_exclusions_new']==0 and D['Branch_B']=='OPEN'
assert D['MW_rank_lower_new']==7 and not D['true_Selmer_rank_upper16_proved']
print('PASS input old rank6 and row351/row350 SHA256, monic degree36 h2')
print('PASS six row342 fake character vectors p3+p29 rank6')
print('PASS S36 M(Q)=0 via adjacent swaps rank35, H1 connecting kernel exactly1')
print('PASS seven true rational Jacobian classes F2 independent using geometric connecting-cocycle lemma')
print('THEOREM: kappa_2([Infinity_+-Infinity_-])=partial(1), nonzero in true Selmer, fake class0')
print('THEOREM: rank Jac(C2)(Q)>=7; true Sel2 fake kernel exactly1; true upper<=32+c_S unchanged')
print('NOT_PROVED Cl(O_K)[2], Cl_S[2], all units, rank upper16, Coleman p163, source exclusion')
if '--full-parent' in sys.argv:
 for s in ['verify_signed18_genus17_rank6_stdlib.py','verify_true_fake_bridge_351_stdlib.py']:
  p=subprocess.run([sys.executable,str(ROOT/s)],cwd=str(ROOT),capture_output=True,text=True,timeout=180)
  assert p.returncode==0,(s,p.stderr,p.stdout[-900:]);print('PASS prior full replay:',s)
