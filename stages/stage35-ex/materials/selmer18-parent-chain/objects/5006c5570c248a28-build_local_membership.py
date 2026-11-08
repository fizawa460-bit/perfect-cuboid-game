import json
from pathlib import Path
from fractions import Fraction as Q
from cypari2 import Pari
P=Path('outputs/STAGE35EX_R3_07_EXACT_SELMER9_CT_REDUCTION_20261105/math')
load=lambda n:json.loads((P/'parents'/n).read_text())
pari=Pari();pari.allocatemem(268435456)
U=load('full_units.json')['units'];C=load('global_cover.json');D=load('local2.json');F=pari.Polrev(load('V_polynomial_source.json')['V_minimal_polynomial_ascending']);x=pari('x')
def lin(m,cols):
 z=0
 for i,c in enumerate(cols):
  if(m>>i)&1:z^=c
 return z
def solve(cols,target):
 piv={}
 for i,c in enumerate(cols):
  a=1<<i
  while c:
   k=c.bit_length()-1
   if k not in piv:piv[k]=(c,a);break
   v,b=piv[k];c^=v;a^=b
 a=0;c=target
 while c:
  k=c.bit_length()-1
  if k not in piv:return None
  v,b=piv[k];c^=v;a^=b
 return a
K=list(map(lambda s:int(s,16),C['residual_global_squareclass_masks_hex']))
real_roots=pari.polrootsreal(F,precision=1024);B=256;den=1<<B
intervals=[]
for r in real_roots:
 n=int(pari.floor(r*den));intervals.append([n,n+1,B])
out={'scope':'fixed C2 local membership for two global candidate squareclasses; not MW realization','V_real_root_dyadic_intervals':intervals,'real_unit_sign_columns':[],'residual_masks_hex':list(map(hex,K))}
for u in U:
 q=pari.Polrev([pari(c)for c in u['coefficients_V']]);out['real_unit_sign_columns'].append([int(pari.subst(q,'x',r)<0)for r in real_roots])
out['real_residual_signs']=[[sum(out['real_unit_sign_columns'][i][j]for i in range(19)if(m>>i)&1)%2 for j in range(4)]for m in K]
db=D['selected_fake_basis'];dnames=[u['label']for u in db]+['scalar_minus1'];dcols=[int(u['unit_squareclass_hex'],16)if 'unit_squareclass_hex'in u else int(u['unit_character_hex'],16)if 'unit_character_hex'in u else int(u['character_hex'],16)for u in db]+[int(D['scalar_minus1_character_hex'],16)]
uc=list(map(lambda s:int(s,16),C['full19_dyadic_character_columns_hex']));out['dyadic_candidate_images']=[]
for m in K:
 v=lin(m,uc);a=solve(dcols,v)
 if a is None:raise ArithmeticError('not in local2')
 out['dyadic_candidate_images'].append({'mask':hex(m),'characters':hex(v),'local_expression_mask':hex(a),'local_expression':[n for i,n in enumerate(dnames)if(a>>i)&1]})
out['odd_places']=[]
for lc,im in zip(load('local_dimensions.json')['local_primes_odd'],load('local_odd_images.json')['odd_bad_primes']):
 pp=lc['p'];Fp=F*pari.Mod(1,pp);vf=[];unitcols=[0]*19
 for j,f in enumerate(lc['factors']):
  g=pari.Polrev(f['coefficients_ascending_mod_p']);g=pari.gcd(Fp,pari.subst(g,'x',x**4)*pari.Mod(1,pp));g=g/g.pollead();vf.append([int(c)for c in pari.lift(g).Vec().python()[::-1]])
  if int(g.poldegree())!=f['degree']:raise ArithmeticError('factor map degree')
  for i,u in enumerate(U):
   q=pari.Polrev([pari(c)for c in u['coefficients_V']])*pari.Mod(1,pp);v=int(pari.lift(pari.polresultant(g,q)))%pp;s=pow(v,(pp-1)//2,pp)
   if s not in (1,pp-1):raise ArithmeticError('nonunit')
   unitcols[i]|=int(s==pp-1)<<j
 cols=[sum(int(b)<<j for j,b in enumerate(bits))for bits in im['unit_residue_quadratic_character_bits']];names=im['six_divisor_names'][:]
 if im['additional_local_point_X4']:
  cols.append(sum(int(b)<<j for j,b in enumerate(im['additional_local_point_X4']['quadratic_character_bits'])));names.append('E4_local')
 cols.append(sum(int(b)<<j for j,b in enumerate(im['rational_scalar_bit_vector'])));names.append('scalar')
 ks=[]
 for m in K:
  v=lin(m,unitcols);a=solve(cols,v)
  if a is None:raise ArithmeticError('not in local odd')
  ks.append({'mask':hex(m),'characters':hex(v),'local_expression_mask':hex(a),'local_expression':[n for i,n in enumerate(names)if(a>>i)&1]})
 out['odd_places'].append({'p':pp,'V_factors':vf,'unit_character_columns_hex':list(map(hex,unitcols)),'local_generator_names':names,'local_generator_character_columns_hex':list(map(hex,cols)),'candidate_images':ks})
(P/'local_membership_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'real_candidates':out['real_residual_signs'],'dyadic':out['dyadic_candidate_images'],'odd':[(s['p'],s['candidate_images'])for s in out['odd_places']]}))
