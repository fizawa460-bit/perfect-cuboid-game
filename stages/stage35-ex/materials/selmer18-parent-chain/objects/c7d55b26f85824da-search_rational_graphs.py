"""New bounded rational-graph family; no exhaustiveness or rank claim."""
from pathlib import Path
from itertools import product
from math import gcd
from functools import reduce
import json,sys,time
ROOT=Path(__file__).resolve().parents[1]
import os
if os.environ.get('STAGE35EX_DEPS'):sys.path.insert(0,os.environ['STAGE35EX_DEPS'])
from cypari2 import Pari
p=Pari();p.allocatemem(268435456);x=p('x')
d=json.loads((ROOT/'math/parents/rank6_divisors.json').read_text());A=p.Polrev(d['A_coefficients_ascending']);B=p.Polrev(d['B_coefficients_ascending']);h=p.Polrev(d['h2_coefficients_ascending'])
known=[p.Polrev(c)for c in d['class_G_coefficients_ascending']]+[x,p.Polrev(d['intersection_degree16_coefficients_ascending'])];known=[v/v.pollead()for v in known]
start=time.time();hits=[];cases=0;hist={};seen=set()
for deg,bound in [(1,4),(2,2)]:
 for cs in product(range(-bound,bound+1),repeat=deg+3):
  lc=list(cs[:deg+1]);dc=list(cs[deg+1:])
  if lc[-1]==0 or dc[-1]==0:continue
  if next((v for v in cs if v),0)<0 or reduce(gcd,cs)!=1:continue
  ell=p.Polrev(lc);den=p.Polrev(dc)
  if p.poldegree(p.gcd(ell,den))>0:continue
  H=2*den*ell*A+(den**2*x+ell**2)*B
  if B*H!=(den*A+ell*B)**2-den**2*h:raise RuntimeError('graph identity')
  fac=H.factor();unknown=[];cases+=1
  for f,e in zip(fac[0],fac[1]):
   g=f/f.pollead()
   if not any(g==k for k in known):unknown.append((g,int(e)))
  hist[len(unknown)]=hist.get(len(unknown),0)+1
  if len(unknown)<2:continue
  for g,mul in unknown:
   if not 1<=int(g.poldegree())<=17 or str(g)in seen:continue
   seen.add(str(g));v=p.lift(p.Mod(den*A+ell*B,g)/p.Mod(den,g))
   if p.lift(p.Mod(v*v-h,g))!=0:raise RuntimeError('candidate curve identity')
   rec={'ell_ascending':lc,'denominator_ascending':dc,'factor_degrees':[int(z.poldegree())for z,e in unknown],'u_ascending':[str(g.polcoef(j))for j in range(int(g.poldegree())+1)],'v_ascending':[str(v.polcoef(j))for j in range(max(0,int(v.poldegree()))+1)],'independence':'NOT_TESTED'};hits.append(rec);print(json.dumps(rec),flush=True)
 out={'scope':'new bounded rational graph family, no completeness proof','cases':cases,'last_ell_degree':deg,'coefficient_bound':bound,'unknown_factor_count_histogram':hist,'candidates':hits,'seconds':time.time()-start};(ROOT/'exploratory/RATIONAL_GRAPH_SEARCH.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='candidates'},flush=True)
