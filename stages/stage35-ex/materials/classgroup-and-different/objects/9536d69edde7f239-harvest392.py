import sys,json,time,hashlib
from pathlib import Path
DATA=Path(__file__).resolve().parent
(DATA/'rerun').mkdir(exist_ok=True)
from math import gcd
from flint import fmpz_poly,fmpz
sys.path.insert(0,str((DATA.parent/'parent391'/'parent390'/'parent389'/'parent388'/'parent381')))
import verify_units381 as v
O=(DATA/'rerun');d=json.loads((DATA/'scan_basis.json').read_text());zk=[(fmpz_poly(h),den) for h,den in zip(d['basis_numerators'],d['basis_denominators'])]
files=sorted(DATA.glob('shard*_terms.jsonl'))
old=json.loads(((DATA.parent/'parent391'/'parent390'/'parent389'/'parent388'/'parent381')/'principal_witnesses.json').read_text())+json.loads(((DATA.parent/'parent391'/'parent390'/'parent389'/'parent388'/'parent381')/'new_relations.json').read_text())+json.loads(((DATA.parent/'parent391'/'parent390'/'parent389')/'new_relations389.json').read_text())+json.loads(((DATA.parent/'parent391'/'parent390')/'new_relations390.json').read_text())+json.loads(((DATA.parent/'parent391')/'new_relations391.json').read_text());oldkeys={tuple(r['coefficients']) for r in old}|{tuple(-x for x in r['coefficients']) for r in old}
rows=[];seen=set();start=time.perf_counter();counts={'raw_terms':0,'unique_numerators':0,'old_numerators':0,'large_prime_skips':0,'dyadic_precision_skips':0,'two_only_skips':0};cache_path=O/'harvest_cache392.json';cache=json.loads(cache_path.read_text()) if cache_path.exists() else {}
for file in files:
 for line in file.read_text().splitlines():
  try:c=json.loads(line)
  except json.JSONDecodeError:continue
  counts['raw_terms']+=1;terms=c['terms'];den=max(zk[j][1] for j,e in terms)
  h=sum((e*(den//zk[j][1])*zk[j][0] for j,e in terms),fmpz_poly());cont=gcd(*map(int,h));h=h//cont
  if h[h.degree()]<0:h=-h
  key=tuple(map(int,h))
  if key in seen:continue
  seen.add(key);counts['unique_numerators']+=1
  if key in oldkeys:counts['old_numerators']+=1;continue
  digest=hashlib.sha256(json.dumps(key,separators=(',',':')).encode()).hexdigest()
  if digest in cache:
   r=cache[digest]
   if isinstance(r,str):counts[r]+=1;continue
   rows.append(r);continue
  norm=abs(int(v.G.resultant(h)));odd=norm//(norm&-norm)
  if odd==1:counts['two_only_skips']+=1;cache[digest]='two_only_skips';continue
  fs=[[int(p),int(e)] for p,e in fmpz(odd).factor()]
  if max(p for p,e in fs)>10**9:counts['large_prime_skips']+=1;cache[digest]='large_prime_skips';continue
  r={'coefficients':list(map(int,h)),'odd_factorization':fs,'search_terms':terms,'search_file':file.name,'search_target':c['target'],'search_trial':c['trial'],'search_power':c.get('power',1),'discovery_method':c.get('method','dense60_triples24_quadruples')}
  out=v.full_profile(r)
  if out is None:counts['dyadic_precision_skips']+=1;cache[digest]='dyadic_precision_skips';continue
  vs,code,positive_h=out;k=min(vs.get((2,0),0),vs.get((2,1),0))//3
  for i,a in enumerate(h(v.X+1)):assert int(a)%2**max(0,k-i//3)==0
  assert norm%2**(105*k)==0
  for j in [0,1]:
   val=vs.get((2,j),0)-3*k
   if val:vs[2,j]=val
   else:vs.pop((2,j),None)
  r.update({'denominator_exponent':k,'absolute_norm':norm//2**(105*k),'mod2_labels':[[p,j] for (p,j),e in sorted(vs.items()) if p!=2 and e&1],
   'valuations':[[p,j,e] for (p,j),e in sorted(vs.items()) if e],'local_unit_code':hex(code),'norm_sign':1 if positive_h==h else -1})
  rows.append(r);cache[digest]=r
  if len(rows)%100==0:print('accepted',len(rows),'unique',len(seen),'seconds',round(time.perf_counter()-start,1),flush=True)
 print('file',file.name,'accepted',len(rows),'seconds',round(time.perf_counter()-start,1),flush=True)
 cache_path.write_text(json.dumps(cache,separators=(',',':')))
(O/'new_relations392.json').write_text(json.dumps(rows,separators=(',',':')))
counts.update({'accepted_new_numerators':len(rows),'file_count':len(files),'seconds':round(time.perf_counter()-start,1)})
(O/'harvest_summary392.json').write_text(json.dumps(counts,indent=2)+'\n');print(counts,flush=True)
