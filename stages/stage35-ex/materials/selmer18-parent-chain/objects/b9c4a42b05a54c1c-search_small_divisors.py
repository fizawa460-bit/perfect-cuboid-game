"""Bounded low-degree divisor discovery, with exact square roots for hits."""
from pathlib import Path
from itertools import product
from math import isqrt
import json,sys,time
ROOT=Path(__file__).resolve().parents[1]
import os
if os.environ.get('STAGE35EX_DEPS'):sys.path.insert(0,os.environ['STAGE35EX_DEPS'])
from flint import fmpz_poly
from cypari2 import Pari
p=Pari();p.allocatemem(268435456)
hcs=json.loads((ROOT/'math/parents/rank6_divisors.json').read_text())['h2_coefficients_ascending']
h=fmpz_poly(hcs);hp=p.Polrev(hcs);square=p('(n,z)->{my(s);if(nfeltissquare(n,z,&s),[1,nfbasistoalg(n,s)],[0])}')
start=time.time();hits=[];tested=0;norm_hits=0
for degree,bound in [(3,30),(4,12)]:
 for low in product(range(-bound,bound+1),repeat=degree):
  cs=list(low)+[1]
  if cs[0]==0 or sum(c*(-1)**i for i,c in enumerate(cs))==0 or sum(c*(-1)**i*3**(degree-i)for i,c in enumerate(cs))==0:continue
  u=fmpz_poly(cs);norm=int(u.resultant(h));tested+=1
  if norm<0:continue
  s=isqrt(norm)
  if s*s!=norm:continue
  norm_hits+=1;content,fac=u.factor()
  if len(fac)!=1 or fac[0][1]!=1 or fac[0][0].degree()!=degree:continue
  up=p.Polrev(cs);nf=p.nfinit(up);ss=square(nf,p.Mod(hp,up))
  if not ss[0]:continue
  v=p.lift(ss[1]);vc=[str(v.polcoef(j))for j in range(degree)]
  if p.lift(p.Mod(v*v-hp,up))!=0:raise RuntimeError('false square root')
  rec={'degree':degree,'u_ascending':cs,'v_ascending':vc};hits.append(rec);print(json.dumps(rec),flush=True)
 out={'scope':'bounded divisor search, not a completeness proof','last_degree':degree,'bound':bound,'tested':tested,'square_norm_candidates':norm_hits,'hits':hits,'seconds':time.time()-start}
 (ROOT/'exploratory/SMALL_DIVISOR_SEARCH.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='hits'},flush=True)
