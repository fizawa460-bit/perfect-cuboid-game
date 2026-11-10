import sys,json,time,hashlib
from pathlib import Path
DATA=Path(__file__).resolve().parent
BASE=DATA.parent/'row393'
(DATA/'rerun').mkdir(exist_ok=True)
if not __debug__: raise RuntimeError("Run certification/discovery scripts without Python -O")
from math import gcd
from flint import fmpz_poly,fmpz
sys.path.insert(0,str((BASE/'parent392'/'parent391'/'parent390'/'parent389'/'parent388'/'parent381')))
import verify_units381 as v
import verify_row380 as v380
sys.path.insert(0,str(DATA.parent/'wave2'))
from prime_certificates import certify, certificates, verify
v380.is_prime=certify
sys.path.insert(0,str(DATA.parent/'wave3'))
from arbitrary_precision import activate
activate(v,v380,certify)
if (DATA/'prime_certificates.json').exists():
 saved=json.loads((DATA/'prime_certificates.json').read_text());verify(saved);certificates.update({int(k):r for k,r in saved.items()})
O=DATA;d=json.loads((BASE/'discovery/scan_basis.json').read_text());zk=[(fmpz_poly(h),den) for h,den in zip(d['basis_numerators'],d['basis_denominators'])]
files=sorted(DATA.glob('*_terms.jsonl'))
old=json.loads((BASE/'parent392/parent391/parent390/parent389/parent388/profiles388.json').read_text())+sum((json.loads(p.read_text()) for p in [BASE/'parent392/parent391/parent390/parent389/new_relations389.json',BASE/'parent392/parent391/parent390/new_relations390.json',BASE/'parent392/parent391/new_relations391.json',BASE/'parent392/new_relations392.json',BASE/'new_relations393.json',DATA.parent/'new394/new_relations394.json',DATA.parent/'wave2/new_relations_wave2.json',DATA.parent/'wave3/new_relations_wave3.json',DATA.parent/'wave4/new_relations_wave4.json',DATA.parent/'wave5/new_relations_wave5.json']),[]);oldkeys={tuple(r['coefficients']) for r in old if 'coefficients' in r}|{tuple(-x for x in r['coefficients']) for r in old if 'coefficients' in r}
for name in ['principal_witnesses.json','new_relations.json']:
 for r in json.loads((BASE/'parent392/parent391/parent390/parent389/parent388/parent381'/name).read_text()):
  oldkeys.add(tuple(r['coefficients']));oldkeys.add(tuple(-x for x in r['coefficients']))
rows=[];seen=set();start=time.perf_counter();counts={'raw_terms':0,'unique_numerators':0,'old_numerators':0,'large_prime_skips':0,'dyadic_precision_skips':0,'two_only_skips':0};cache_path=O/'harvest_cache_wave6.json';cache=json.loads(cache_path.read_text()) if cache_path.exists() else {}
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
  r={'coefficients':list(map(int,h)),'odd_factorization':fs,'search_terms':terms,'search_file':file.name,'search_target':c['target'],'search_trial':c['trial'],'search_power':c.get('power',1),'discovery_method':c.get('method','dense80_triples32_quadruples'),'search_anchor':c.get('anchor')}
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
(O/'new_relations_wave6.json').write_text(json.dumps(rows,separators=(',',':')))
counts.update({'accepted_new_numerators':len(rows),'file_count':len(files),'seconds':round(time.perf_counter()-start,1)})
(O/'harvest_summary_wave6.json').write_text(json.dumps(counts,indent=2)+'\n');print(counts,flush=True)

verify(certificates)
(DATA/'prime_certificates.json').write_text(json.dumps(certificates,indent=2)+'\n')
