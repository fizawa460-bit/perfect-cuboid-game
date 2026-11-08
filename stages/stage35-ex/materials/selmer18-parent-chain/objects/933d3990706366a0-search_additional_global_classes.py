from pathlib import Path
import json,sys,time,math
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'_deps'))
from cypari2 import Pari
p=Pari();p.allocatemem(268435456);x=p('x')
d=json.loads((R/'math/parents/rank6_divisors.json').read_text());A=p.Polrev(d['A_coefficients_ascending']);B=p.Polrev(d['B_coefficients_ascending']);h=p.Polrev(d['h2_coefficients_ascending'])
known=[p.Polrev(c)for c in d['class_G_coefficients_ascending']]+[p.Polrev(d['intersection_degree16_coefficients_ascending']),x]
known=[f/f.pollead()for f in known];cases=[]
for den in range(1,17):
 for num in range(1,121):
  if math.gcd(num,den)==1:cases.append((0,num,den))
for den in range(1,5):
 for slope in [-3,-2,-1,1,2,3]:
  for intercept in range(-12,13):
   if math.gcd(math.gcd(abs(slope),abs(intercept)),den)==1:cases.append((slope,intercept,den))
start=time.monotonic();novel=[];hist={};tests=0
for aa,bb,den in cases:
 ell=aa*x+bb;H=2*den*ell*A+(den*den*x+ell*ell)*B
 if B*H!=((den*A+ell*B)**2-den*den*h):raise RuntimeError('global graph identity')
 fac=H.factor();unknown=[]
 for f,e in zip(fac[0],fac[1]):
  f=f/f.pollead()
  if not any(f==z for z in known):unknown.append((f,int(e)))
 tests+=1;hist[len(unknown)]=hist.get(len(unknown),0)+1
 if len(unknown)>=2:
  rec={'slope':aa,'intercept':bb,'denominator':den,'unknown_factors':[{'degree':int(f.poldegree()),'coefficients_ascending':[str(f.polcoef(j))for j in range(int(f.poldegree())+1)],'multiplicity':e}for f,e in unknown]};novel.append(rec);print(json.dumps(rec),flush=True)
out={'scope':'bounded necessary search for additional global MW classes, not a completeness proof','tests':tests,'cases_with_N_unknown_support_factors':hist,'potentially_productive_cases':novel,'single_unknown_factor_relation':'principal divisor of Y-(A+ell*B/den) expresses its class over Q as a combination of the old seven, using old infinity/P0minus relations; no new independent direction','new_independent_global_MW_classes_certified':0,'seconds':round(time.monotonic()-start,3)}
(R/'exploratory/ADDITIONAL_GLOBAL_CLASS_SEARCH.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'done':True,'tests':tests,'histogram':hist,'potential_cases':len(novel),'seconds':out['seconds']}))
