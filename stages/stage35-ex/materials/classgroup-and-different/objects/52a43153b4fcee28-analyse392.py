import json,sys,time
from pathlib import Path
DATA=Path(__file__).resolve().parent
(DATA/'rerun').mkdir(exist_ok=True)
sys.path.insert(0,str((DATA.parent/'parent391'/'parent390'/'parent389'/'parent388')))
from verify_row388 import binary_basis,integer_basis,valuation_sum,parity_mask
sys.path.insert(0,str((DATA.parent/'parent391'/'parent390'/'parent389'/'parent388'/'parent381')))
from verify_row380 import prime_factors
P=(DATA.parent/'parent391'/'parent390'/'parent389'/'parent388');O=(DATA/'rerun')
profiles=json.loads((P/'profiles388.json').read_text())+json.loads(((DATA.parent/'parent391'/'parent390'/'parent389')/'new_relations389.json').read_text())+json.loads(((DATA.parent/'parent391'/'parent390')/'new_relations390.json').read_text())+json.loads(((DATA.parent/'parent391')/'new_relations391.json').read_text());new=json.loads((O/'new_relations392.json').read_text());factors={int(p):d for p,d in json.loads(((DATA.parent/'parent391')/'factorizations391.json').read_text()).items()};old_n=len(profiles)
psnew={p for r in new for p,e in r['odd_factorization']}-factors.keys();start=time.perf_counter()
for count,p in enumerate(sorted(psnew)):
 _,ff=prime_factors(p);ff=sorted(ff,key=lambda a:a[2]);factors[p]=[[g.degree() for g,e,j in ff],[e for g,e,j in ff]]
 if count%100==99:print('new decompositions',count+1,round(time.perf_counter()-start,1),flush=True)
(O/'all_factorizations392.json').write_text(json.dumps(factors,separators=(',',':')))
ps=sorted(factors);labels=[(2,0),(2,1)]+[(p,j) for p,(ds,es) in sorted(factors.items()) for j in range(len(ds))];ix={p:i for i,p in enumerate(labels)}
oldrows=[{(p,j):e for p,j,e in r['valuations']} for r in profiles];rationalrows=[{(p,j):e for j,e in enumerate(factors[p][1])} for p in ps]
newrows=[{(p,j):e for p,j,e in r['valuations']} for r in new];rows=oldrows+rationalrows+newrows
vec=lambda row:sum((e&1)<<ix[p] for p,e in row.items())
base_n=len(oldrows)+len(rationalrows)
piv={};ind=[]
def add(v,index):
 c=1<<index
 while v:
  k=v.bit_length()-1
  if k not in piv:piv[k]=(v,c);return True
  w,d=piv[k];v^=w;c^=d
 return False
for i,row in enumerate(rows[:base_n]):add(vec(row),i)
base_piv=dict(piv)
def reduce(v,basis):
 c=0
 for k in sorted(basis,reverse=True):
  if v>>k&1:v^=basis[k][0];c^=basis[k][1]
 return v,c
fb=[(2,0,128)]+[(p,j,p**d) for p,(ds,es) in sorted(factors.items()) for j,d in enumerate(ds) if p**d<=6768];fb.sort(key=lambda a:(a[2],a[0],a[1]))
oldzeros=[a for a in fb if not reduce(1<<ix[a[:2]],base_piv)[0]];oldrank=len(binary_basis([reduce(1<<ix[a[:2]],base_piv)[0] for a in fb])[0]);assert len(fb)==878 and len(oldzeros)==595 and oldrank==222
for i,row in enumerate(newrows):
 if add(vec(row),base_n+i):ind.append(i)
zeros=[];remaining=[];witnesses=[];fbpiv={}
for a in fb:
 v,c=reduce(1<<ix[a[:2]],piv)
 if not v:
  zeros.append(a)
  if a not in oldzeros:
   used=[i for i in range(len(rows)) if c>>i&1];value=valuation_sum([(i,1) for i in used],rows)
   assert sorted(p for p,e in value.items() if e&1)==[a[:2]]
   half={p:(e-int(p==a[:2]))//2 for p,e in value.items()};assert all(e>=0 for e in half.values())
   witnesses.append({'prime_ideal':list(a),'old_generator_indices':[i for i in used if i<old_n],
     'rational_primes':[ps[i-old_n] for i in used if old_n<=i<base_n],
     'new_generator_indices':[i-base_n for i in used if i>=base_n],
     'half_ideal_factors':[[p,j,e] for (p,j),e in sorted(half.items()) if e]})
 while v:
  k=v.bit_length()-1
  if k not in fbpiv:fbpiv[k]=v;remaining.append(a);break
  v^=fbpiv[k]
print('binary result','new_rows',len(new),'independent',len(ind),'zero',len(zeros),'FB rank',len(fbpiv),'newzero',len(witnesses),flush=True)
bq,kernel=integer_basis(rows);r2=len(piv);rQ=len(bq)
print('integer','rankQ',rQ,'rank2',r2,'kernel',len(kernel),'pivots',sorted({abs(v[k]) for k,(v,c) in bq.items()}),flush=True)
cert={'new_zero_witnesses':witnesses,'independent_new_relation_indices':ind,'integer_kernel':kernel,
      'remaining_formal_basis':[list(a) for a in remaining],'zero_prime_ideals':[list(a) for a in zeros]}
(O/'relation_certificate392.json').write_text(json.dumps(cert,separators=(',',':')))
res={'new_exact_generators':len(new),'new_independent_principal_relation_dimension':len(ind),
     'support_rational_primes':len(ps),'new_prime_decompositions':len(psnew),'finite_factorbase_bound':6768,'finite_factorbase_size':878,
     'old_individually_zero':595,'new_individually_zero':len(zeros),'newly_certified_zero_count':len(witnesses),
     'old_formal_span_dimension':222,'new_formal_span_dimension':len(fbpiv),'formal_dimension_drop':222-len(fbpiv),
     'first_remaining_formal_direction':list(remaining[0]) if remaining else None,
     'integer_matrix_rows':len(rows),'integer_matrix_columns':len(labels),'rank_Q':rQ,'rank_F2':r2,'integer_kernel_dimension':len(kernel),
     'integer_kernel_mod2_rank':len(binary_basis([parity_mask(k) for k in kernel])[0]),
     'all_integer_pivots_are_units':all(abs(v[k])==1 for k,(v,c) in bq.items()),
     'p827_j0_zero':any(a[:2]==(827,0) for a in zeros),
     'classgroup_mod2_generation':'NOT_CERTIFIED','c_Cl':'UNDETERMINED','qstar':'UNDETERMINED','new_unconditional_signed_exclusion':0}
(O/'results392.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2),flush=True)
