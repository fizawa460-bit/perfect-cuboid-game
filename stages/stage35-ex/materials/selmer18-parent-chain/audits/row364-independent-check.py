import json, pathlib, time, math, hashlib, zipfile
from fractions import Fraction
base=pathlib.Path(__file__).resolve().parent / 'math'
load=lambda a:json.loads((base/a).read_text())
C=load('parents/global_cover.json');D=load('parents/local2.json');O=load('parents/local_odd_images.json');U=load('parents/full_units.json')['units'];cert=load('local_membership_certificate.json');L=load('parents/local_dimensions.json');V=load('parents/V_polynomial_source.json')['V_minimal_polynomial_ascending']
assert len(U)==19 and len(V)==37
K=[int(x,16)for x in cert['residual_masks_hex']];assert len(K)==2

def spanrank(vec):
 b={}
 for v in vec:
  while v:
   k=v.bit_length()-1
   if k not in b:b[k]=v;break
   v^=b[k]
 return len(b)
def XOR(m,arr):
 z=0
 for j,v in enumerate(arr):
  if m>>j&1:z^=v
 return z

# Independent exact modular finite-field ring arithmetic:
# Determine quadratic character of u mod irreducible factor f by repeated polynomial squaring,
# rather than Euclidean resultants (author's algorithm).
def trim(a):
 while a and a[-1]==0:a.pop()
 return a

def red(a,f,p):
 a=a[:]; n=len(f)-1
 for i in range(len(a)-1,n-1,-1):
  c=a[i]
  if c:
   for j in range(n):a[i-n+j]=(a[i-n+j]-c*f[j])%p
 return (a[:n]+[0]*n)[:n]
def fm(a,b,f,p):
 n=len(f)-1;c=[0]*(2*n-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:c[i+j]=(c[i+j]+x*y)%p
 return red(c,f,p)
def fpow(a,e,f,p):
 n=len(f)-1;o=[1]+[0]*(n-1)
 while e:
  if e&1:o=fm(o,a,f,p)
  e>>=1
  if e:a=fm(a,a,f,p)
 return o

def unitpoly(u,p):
 q=[Fraction(x)for x in u['coefficients_V']];return [int((x.numerator%p)*pow(x.denominator,-1,p)%p)for x in q]

results=[];st=time.monotonic();checks=0
# independent full GF(2) linear combinations against local frame and scalar
old6=[int(x,16)for x in C['old6_MW_fake_coordinate_masks_hex']]
assert spanrank(old6)==6 and spanrank(old6+K)==8
rows=[int(x,16) for x in C['full_candidate_rows_hex']]
for m in old6+K:
 assert all(((m&r).bit_count()%2)==0 for r in rows)
checks+=len(rows)*8
# local2: independent bits linear algebra in GF(2)
cols=[int(x,16)for x in C['full19_dyadic_character_columns_hex']]
loccols=[int(x.get('unit_squareclass_hex',x.get('unit_character_hex',x.get('character_hex'))),16) for x in D['selected_fake_basis']]+[int(D['scalar_minus1_character_hex'],16)]
assert spanrank(loccols)==19
for m,record in zip(K,cert['dyadic_candidate_images']):
 assert XOR(m,cols)==XOR(int(record['local_expression_mask'],16),loccols)==int(record['characters'],16)
 checks+=1
# exact algebraic real signs by rational interval, independent implementation
ints=[(Fraction(n,1<<bits),Fraction(m,1<<bits)) for n,m,bits in cert['V_real_root_dyadic_intervals']]
def horner_intervals(q,lo,hi):
 a=b=Fraction(0)
 for z in reversed(q):
  x=[a*lo,a*hi,b*lo,b*hi];a=min(x)+z;b=max(x)+z
 return a,b
sigs=[]
for u in U:
 q=[Fraction(v) for v in u['coefficients_V']]
 sig=[]
 for a,b in ints:
  low,high=horner_intervals(q,a,b)
  assert high<0 or low>0
  sig.append(int(high<0));checks+=1
 sigs.append(sig)
assert sigs==cert['real_unit_sign_columns']
for m in K:assert [sum(sigs[i][j] for i in range(19) if m>>i&1)%2 for j in range(4)]==[0]*4
# check all 19 norm+-1 stored and candidates product +1
for m in K: assert math.prod(U[i]['norm'] for i in range(19) if m>>i&1)==1
print('Independent REAL dyadic F2 passed',time.monotonic()-st,flush=True)
# All 5 primes x all 19 units x all residue factor rings independently through powering.
for place, old in zip(cert['odd_places'],O['odd_bad_primes']):
 p=place['p'];assert p==old['p'];fs=place['V_factors'];pred=[]
 ups=[unitpoly(u,p) for u in U]
 for f in fs:
  n=len(f)-1
  f=[int(x)%p for x in f]
  exp=(pow(p,n)-1)//2
  bits=[]
  for u in ups:
   v=red(u+[0]*(max(0,len(f)-1-len(u))),f,p)
   power=fpow(v,exp,f,p)
   if power[0]==1 and all(x==0 for x in power[1:]):bits.append(0)
   elif power[0]==p-1 and all(x==0 for x in power[1:]):bits.append(1)
   else:raise AssertionError(('not squarecharacter',p,n,power[:4]))
  pred.append(bits)
 chars=[sum(pred[j][i]<<j for j in range(len(fs))) for i in range(19)]
 assert chars==[int(x,16) for x in place['unit_character_columns_hex']],('odd all unit chars differ',p)
 gens=[int(x,16) for x in place['local_generator_character_columns_hex']]
 for m,record in zip(K,place['candidate_images']):
  v=XOR(m,chars)
  assert v==int(record['characters'],16)==XOR(int(record['local_expression_mask'],16),gens)
 results.append({'prime':p,'factor_degrees':[len(f)-1 for f in fs],'candidate_character':[hex(XOR(m,chars))for m in K]})
 checks+=19*len(fs)+2
 print('verified odd residue place',p,'factor degrees',results[-1]['factor_degrees'],'t=',round(time.monotonic()-st,2),flush=True)
# Independent check codimension and pairing branch implications (conditional, not c calculation).
assert spanrank(old6+K)-spanrank(old6)==2
assert all(U[i]['norm'] in[-1,1] for i in range(19))
report={'result':'PASS_INDEPENDENT_LOCAL_RINGS_AND_CHARACTER_MEMBERSHIP','algorithm':'finite-field multiplicative character via exponent (p^f-1)/2 mod irreducible factor; not via author Euclidean resultants','checks':checks,'real_signs':True,'dyadic_linear_membership':True,'global_candidate_rank':8,'candidate_real_signs':'both all positive','odd_places':results,'elapsed_seconds':round(time.monotonic()-st,3)}
(base.parent/'independent_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False))
