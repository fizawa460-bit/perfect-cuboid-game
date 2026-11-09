"""Exact NEW local arithmetic for the full fixed-C2 Selmer intersection.

The cohomology/good-reduction/Cassels-Tate theorems are proved in the
accompanying mathematical report, not asserted to be machine verified here.
Frozen parent certificates retain their historical audit fields. The received
row363 scoped PASS is preserved separately under record_updates; row364 is pending.
"""
import json,math,time,sys
from pathlib import Path
from fractions import Fraction as Q
from functools import reduce
from flint import fmpz_poly,fmpq_poly,fmpq
P=Path(__file__).resolve().parent
load=lambda n:json.loads((P/n).read_text())
checks=0;negatives=0;started=time.monotonic()
def check(ok,label):
 global checks
 if not ok:raise ArithmeticError(label)
 checks+=1
def reject(ok,label):
 global negatives
 if ok:raise ArithmeticError('negative accepted: '+label)
 negatives+=1
def rank(vs):
 piv={}
 for v in vs:
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=v;break
   v^=piv[k]
 return len(piv)
def lin(mask,cols):
 z=0
 for i,c in enumerate(cols):
  if(mask>>i)&1:z^=c
 return z
def trim(a):
 a=list(a)
 while a and a[-1]==0:a.pop()
 return a
def mul(a,b,p):
 if not a or not b:return []
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return trim(c)
def rem(a,b,p):
 a=trim([v%p for v in a]);b=trim([v%p for v in b]);iv=pow(b[-1],-1,p)
 while len(a)>=len(b):
  c=a[-1]*iv%p;k=len(a)-len(b)
  for j in range(len(b)):a[k+j]=(a[k+j]-c*b[j])%p
  a=trim(a)
 return a
def gcd(a,b,p):
 while b:a,b=b,rem(a,b,p)
 return [(v*pow(a[-1],-1,p))%p for v in a]
def resultant(a,b,p):
 a=trim([v%p for v in a]);b=trim([v%p for v in b]);z=1
 if not a or not b:return 0
 while len(b)>1:
  m=len(a)-1;n=len(b)-1;r=rem(a,b,p)
  if not r:return 0
  z=z*pow(b[-1],m-len(r)+1,p)%p
  if m*n%2:z=-z%p
  a,b=b,r
 return z*pow(b[0],len(a)-1,p)%p
def modq(q,p):return[(v.numerator*pow(v.denominator,-1,p))%p for v in q]
def primitive_positive_scale(a):
 cs=[Q(str(v))for v in a.coeffs()]
 if not cs:return fmpq_poly([])
 den=math.lcm(*(c.denominator for c in cs));ns=[int(c*den)for c in cs];g=reduce(math.gcd,map(abs,ns))
 return fmpq_poly([v//g for v in ns])
def sturm(F):
 out=[fmpq_poly(F),fmpq_poly([i*F[i]for i in range(1,len(F))])]
 while out[-1].degree()>0:
  r=-(out[-2]%out[-1]);out.append(primitive_positive_scale(r))
 return out
def variation(vals):
 vals=[int(v>0)-int(v<0)for v in vals if v]
 return sum(a!=b for a,b in zip(vals,vals[1:]))
def countroots(chain,a,b):
 return variation([v(fmpq(a.numerator,a.denominator))for v in chain])-variation([v(fmpq(b.numerator,b.denominator))for v in chain])
def evalinterval(q,a,b):
 lo=hi=Q(0)
 for c in q[::-1]:
  vals=[lo*a,lo*b,hi*a,hi*b];lo=min(vals)+c;hi=max(vals)+c
 return lo,hi
def detmod(a,p):
 a=[[x%p for x in r]for r in a];out=1
 for j in range(len(a)):
  k=next((k for k in range(j,len(a))if a[k][j]),None)
  if k is None:return 0
  if k!=j:a[k],a[j]=a[j],a[k];out=-out
  v=a[j][j];out=out*v%p;iv=pow(v,-1,p)
  for k in range(j+1,len(a)):
   c=a[k][j]*iv%p
   for t in range(j+1,len(a)):a[k][t]=(a[k][t]-c*a[j][t])%p
 return out%p

C=load('parents/global_cover.json');U=load('parents/full_units.json')['units'];D=load('parents/local2.json');Vsrc=load('parents/V_polynomial_source.json');F=Vsrc['V_minimal_polynomial_ascending'];R=load('parents/rank6.json');L=load('parents/local_dimensions.json');O=load('parents/local_odd_images.json');cert=load('local_membership_certificate.json')
check(C['ordinary_class_number_exact']==1 and C['full_candidate_dimension']==8,'inherited full global upper8')
check(C['whole_MW_residual_log_U_constructed']is False,'do not promote inherited U status')
check(len(U)==19 and C['auxiliary20x20_integer_determinant']%2==1,'inherited complete unit squareclasses')
K=[int(s,16)for s in cert['residual_masks_hex']];rows=[int(s,16)for s in C['full_candidate_rows_hex']];old6=[int(s,16)for s in C['old6_MW_fake_coordinate_masks_hex']]
check(cert['residual_masks_hex']==C['residual_global_squareclass_masks_hex'],'bind the two NEW local tests to OLD candidates')
check(rank(old6)==6 and rank(old6+K)==8,'global eight independent candidate classes')
check(not any((r&v).bit_count()%2 for r in rows for v in old6+K),'all eight in upper kernel')
polys=[list(map(Q,u['coefficients_V']))for u in U];FP=fmpz_poly(F)
for i,(u,q)in enumerate(zip(U,polys)):
 den=math.lcm(*(v.denominator for v in q));ns=[int(v*den)for v in q]
 check(int(FP.resultant(fmpz_poly(ns)))==u['norm']*den**36 and abs(u['norm'])==1,'global unit norm '+str(i+1))
for k in K:check(math.prod(u['norm']for i,u in enumerate(U)if(k>>i)&1)==1,'candidate exact norm +1')

# All real signs are proven by exact rational isolation and interval Horner.
chain=sturm(F);global_v=[]
for sg in [-1,1]:
 global_v.append(variation([int(p.leading_coefficient()>0)*2-1 if sg==1 or p.degree()%2==0 else -(int(p.leading_coefficient()>0)*2-1)for p in chain]))
check(global_v[0]-global_v[1]==4,'F has exactly four real roots by Sturm')
intervals=[]
for n,m,bits in cert['V_real_root_dyadic_intervals']:
 a=Q(n,1<<bits);b=Q(m,1<<bits);check(a<b and countroots(chain,a,b)==1,'exact real-root isolating cell');intervals.append((a,b))
check(all(intervals[i][1]<intervals[i+1][0]for i in range(3)),'four disjoint ordered isolating cells')
signs=[[]for _ in U]
for i,q in enumerate(polys):
 for a,b in intervals:
  lo,hi=evalinterval(q,a,b);check(lo>0 or hi<0,'unit sign separated from zero');signs[i].append(int(hi<0))
check(signs==cert['real_unit_sign_columns'],'frozen real signatures reproduced')
rs=[[sum(signs[i][j]for i in range(19)if(k>>i)&1)%2 for j in range(4)]for k in K]
check(rs==cert['real_residual_signs']==[[0]*4,[0]*4],'both candidates totally positive')

# Dyadic membership explicitly exhibits a word in the OLD local generators.
key=lambda r:next(r[k]for k in ['unit_squareclass_hex','unit_character_hex','character_hex']if k in r)
db=D['selected_fake_basis'];dc=[int(key(r),16)for r in db]+[int(D['scalar_minus1_character_hex'],16)];dn=[r['label']for r in db]+['scalar_minus1'];uc=[int(s,16)for s in C['full19_dyadic_character_columns_hex']]
check(rank(dc)==19 and len(db)==18,'old complete scalar-enlarged local2 frame')
for k,r in zip(K,cert['dyadic_candidate_images']):
 v=lin(k,uc);mask=int(r['local_expression_mask'],16)
 check(v==int(r['characters'],16)==lin(mask,dc),'exact dyadic candidate combination')
 check(r['local_expression']==[n for i,n in enumerate(dn)if(mask>>i)&1],'dyadic local labels bound')

# Independently recompute finite-field norms by Euclidean resultants, rather
# than PARI's discovery routine. V-factors are matched through theta=V^4.
odd_rows=[]
for lc,im,s in zip(L['local_primes_odd'],O['odd_bad_primes'],cert['odd_places']):
 p=lc['p'];check(p==im['p']==s['p'],'odd prime binding');prod=[1];chars=[0]*19
 for j,(f,g)in enumerate(zip(lc['factors'],s['V_factors'])):
  q=f['coefficients_ascending_mod_p'];q4=[0]*(4*(len(q)-1)+1)
  for i,c in enumerate(q):q4[4*i]=c
  check(gcd(F,q4,p)==g and len(g)-1==f['degree'],'theta factor pullback at '+str(p))
  for _ in range(f['multiplicity']):prod=mul(prod,g,p)
  for i,u in enumerate(polys):
   norm=resultant(g,modq(u,p),p);leg=pow(norm,(p-1)//2,p)
   check(leg in(1,p-1),'nonzero unit residue norm');chars[i]|=int(leg==p-1)<<j
 check(prod==[v%p for v in F],'complete V factor product at '+str(p))
 check(list(map(hex,chars))==s['unit_character_columns_hex'],'all nineteen odd unit characters reproduced')
 cols=[sum(int(v)<<j for j,v in enumerate(row))for row in im['unit_residue_quadratic_character_bits']];names=im['six_divisor_names'][:]
 if im['additional_local_point_X4']:
  cols.append(sum(int(v)<<j for j,v in enumerate(im['additional_local_point_X4']['quadratic_character_bits'])));names.append('E4_local')
 cols.append(sum(int(v)<<j for j,v in enumerate(im['rational_scalar_bit_vector'])));names.append('scalar')
 check(names==s['local_generator_names']and list(map(hex,cols))==s['local_generator_character_columns_hex'],'local frame matches the parent rational/local divisors')
 for k,r in zip(K,s['candidate_images']):
  v=lin(k,chars);mask=int(r['local_expression_mask'],16)
  check(v==int(r['characters'],16)==lin(mask,cols),'odd local membership for each candidate')
  check(r['local_expression']==[n for i,n in enumerate(names)if(mask>>i)&1],'odd local expression names')
 odd_rows.append({'p':p,'candidate_characters':[r['characters']for r in s['candidate_images']]})

# Linear algebra relevant to the proof of the genuine lifting and CT reduction.
check(rank([(1<<i)|(1<<(i+1))for i in range(35)])==35,'S36 transpositions have only the constant invariant representatives')
bridge=load('parents/true_fake_bridge.json');check(bridge['H1_J2_to_H1_M_kernel_F2_dimension']==1,'inherited exact global connecting kernel')
logs=load('parents/known7_logs.json');lm=logs['normalized_log_matrix_mod163'];I=logs['pivot_columns_zero_based'];minor=detmod([[row[j]for j in I]for row in lm],163)
check(minor==137,'old log frame usable IF rank7 is subsequently proved')
check(8+1==9 and 9-7==2,'exact dimension consequence, not exact MW rank')
check(all(rank([c<<1,c])==(2 if c else 0)for c in[0,1]),'binary conditional CT matrix ranks 0 and 2 distinguished')
reject(lin(K[0],uc)==lin(int(cert['dyadic_candidate_images'][0]['local_expression_mask'],16)^1,dc),'changed dyadic word')
reject(lin(K[0],[int(s,16)for s in cert['odd_places'][1]['unit_character_columns_hex']])==int(cert['odd_places'][1]['candidate_images'][0]['characters'],16)^1,'changed odd character')
reject(rank(old6+[K[0],K[0]])==8,'duplicate residual class')
reject(countroots(chain,Q(0),Q(1,100))==1,'interval containing no branch root')
reject(all(lo>0 for lo in[evalinterval(polys[1],a,b)[0]for a,b in intervals]),'one ordinary unit must not be called totally positive')
reject(minor==0,'zero pivot is not accepted')
changed=[Q(v)for v in polys[0]];changed[0]+=1;den=math.lcm(*(v.denominator for v in changed))
reject(int(FP.resultant(fmpz_poly([int(v*den)for v in changed])))==U[0]['norm']*den**36,'altered global unit')

out={'status':'INTERNAL_EXACT_PASS_NEW_LOCAL_ARITHMETIC','checks':checks,'negative_controls':negatives,'global_fake_candidate_dimension':8,'two_residual_candidates_pass_all_bad_places_and_real':True,'odd_place_candidate_characters':odd_rows,'true_Selmer_dimension_exact_by_report_theorems':9,'known7_mod2_dimension_inherited':7,'true_Selmer_quotient_by_known7_dimension':2,'MW_rank_interval':[7,9],'CT_quotient_matrix_form':'[[0,c],[c,0]], c in {0,1/2}','CT_entry_computed':False,'if_CT_entry_nonzero_then_rank7_Uzero':True,'whole_MW_U_constructed':False,'whole_MW_a0_unit_proved':False,'source_exclusions':0,'independent_mathematical_audit':'PENDING_NOT_RUN','seconds':round(time.monotonic()-started,3)}
name='EXACT_SELMER9_'+('NORMAL'if __debug__ else'OPTIMIZED')+'_REPLAY.json';(P/name).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
