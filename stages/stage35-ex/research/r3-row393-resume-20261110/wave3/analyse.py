"""Exact parity relations; does not certify generation of the full class group."""
import json,sys,time
from pathlib import Path
if not __debug__:raise RuntimeError('Do not run with -O')
OUT=Path(__file__).resolve().parent;BASE=OUT.parent/'row393';P=BASE/'parent392/parent391/parent390/parent389/parent388'
sys.path.insert(0,str(P/'parent381'));from verify_row380 import prime_factors
import verify_row380 as v380
sys.path.insert(0,str(OUT.parent/'wave2'))
from prime_certificates import certify
import verify_units381 as v
from arbitrary_precision import activate
activate(v,v380,certify)
v380.is_prime=certify
parents=[P/'profiles388.json',P.parent/'new_relations389.json',P.parent.parent/'new_relations390.json',P.parent.parent.parent/'new_relations391.json',BASE/'parent392/new_relations392.json',BASE/'new_relations393.json',OUT.parent/'new394/new_relations394.json',OUT.parent/'wave2/new_relations_wave2.json']
old=sum((json.loads(p.read_text()) for p in parents),[]);new=json.loads((OUT/'new_relations_wave3.json').read_text());factors={int(p):d for p,d in json.loads((OUT.parent/'wave2/factorizations_wave2.json').read_text()).items()}
oldp=set(factors);start=time.perf_counter()
for p in sorted({p for row in new for p,e in row['odd_factorization']}-oldp):
 _,ff=prime_factors(p);ff=sorted(ff,key=lambda a:a[2]);factors[p]=[[g.degree() for g,e,j in ff],[e for g,e,j in ff]]
ps=sorted(factors);labels=[(2,0),(2,1)]+[(p,j) for p,(ds,es) in sorted(factors.items()) for j in range(len(ds))];ix={t:i for i,t in enumerate(labels)}
oldrows=[{(p,j):e for p,j,e in row['valuations']} for row in old];rats=[{(p,j):e for j,e in enumerate(factors[p][1])} for p in ps];newrows=[{(p,j):e for p,j,e in row['valuations']} for row in new];rows=oldrows+rats+newrows
piv={};base_n=len(oldrows)+len(rats)
def vec(row):return sum((e&1)<<ix[p] for p,e in row.items())
def add(v,i):
 c=1<<i
 while v:
  k=v.bit_length()-1
  if k not in piv:piv[k]=(v,c);return True
  w,d=piv[k];v^=w;c^=d
 return False
def reduce(v,basis):
 c=0
 for k in sorted(basis,reverse=True):
  if v>>k&1:v^=basis[k][0];c^=basis[k][1]
 return v,c
for i,row in enumerate(rows[:base_n]):add(vec(row),i)
oldrank=len(piv);oldbasis=piv.copy()
fb=[(2,0,128)]+[(p,j,p**d) for p,(ds,es) in sorted(factors.items()) for j,d in enumerate(ds) if p**d<=6768];fb.sort(key=lambda a:(a[2],a[0],a[1]))
def fb_status(basis):
 fbpi={};zeros=[];rem=[]
 for a in fb:
  v,c=reduce(1<<ix[a[:2]],basis)
  if not v:zeros.append(a)
  while v:
   k=v.bit_length()-1
   if k not in fbpi:fbpi[k]=v;rem.append(a);break
   v^=fbpi[k]
 return zeros,rem
oldzero,oldrem=fb_status(oldbasis);assert len(fb)==878 and len(oldzero)==628 and len(oldrem)==180
ind=[]
for j,row in enumerate(newrows):
 if add(vec(row),base_n+j):ind.append(j)
zeros,rem=fb_status(piv);witnesses=[]
for a in zeros:
 if a in oldzero:continue
 v,c=reduce(1<<ix[a[:2]],piv);assert v==0
 used=[i for i in range(len(rows)) if c>>i&1];vals={}
 for i in used:
  for key,e in rows[i].items():vals[key]=vals.get(key,0)+e
 assert [t for t,e in sorted(vals.items()) if e&1]==[a[:2]]
 witnesses.append(dict(prime_ideal=a,old_generator_indices=[i for i in used if i<len(old)],rational_primes=[ps[i-len(old)] for i in used if len(old)<=i<base_n],new_generator_indices=[i-base_n for i in used if i>=base_n],half_ideal_factors=[[p,j,(e-int((p,j)==a[:2]))//2] for (p,j),e in sorted(vals.items()) if (e-int((p,j)==a[:2]))//2]))
results=dict(new_exact_generators=len(new),new_independent_principal_relations=len(ind),new_rational_prime_support=len(set(factors)-oldp),old_formal_dimension=180,new_formal_dimension=len(rem),old_individually_zero=628,new_individually_zero=len(zeros),new_zero_count=len(witnesses),p827_zero=(827,0,827) in zeros,remaining_first=rem[:5],old_plus_new_rational_rank=oldrank,new_rank=len(piv),classgroup_generation='NOT_CERTIFIED',c_Cl='UNDETERMINED',unconditional_signed_exclusions=0)
json.dump(results,open(OUT/'results_wave3.json','w'),indent=2);json.dump(dict(witnesses=witnesses,independent_new_indices=ind,remaining_formal_basis=rem),open(OUT/'certificate_wave3.json','w'),indent=2);json.dump(factors,open(OUT/'factorizations_wave3.json','w'))
print(json.dumps(results,indent=2));print('seconds',time.perf_counter()-start)
