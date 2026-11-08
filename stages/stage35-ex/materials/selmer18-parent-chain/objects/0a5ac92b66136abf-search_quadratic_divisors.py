"""Finite discovery search only. Each hit carries an exact rational Mumford pair."""
from pathlib import Path
from math import gcd,isqrt
from fractions import Fraction as Q
import json,time
ROOT=Path(__file__).resolve().parents[1]
h=json.loads((ROOT/'math/parents/rank6_divisors.json').read_text())['h2_coefficients_ascending']
start=time.time();hits=[];tested=0
for a in range(1,9):
 scaled=[c*a**(36-j)for j,c in enumerate(h)]
 for b in range(-256,257):
  for c in range(-256,257):
   if not c or gcd(gcd(a,abs(b)),abs(c))!=1:continue
   disc=b*b-4*a*c
   if disc>=0 and isqrt(disc)**2==disc:continue
   r0=scaled[-1];r1=0
   for z in scaled[-2::-1]:r0,r1=z-a*c*r1,r0-b*r1
   norm=r0*r0-b*r0*r1+a*c*r1*r1;tested+=1
   if norm<0:continue
   nn=isqrt(norm)
   if nn*nn!=norm:continue
   for sn in [nn,-nn]if nn else[0]:
    val=2*r0-b*r1+2*sn
    if val<0:continue
    s=isqrt(val)
    if s*s!=val or not s:continue
    tv=Q(r1,s);sv=(Q(s)+b*tv)/2
    q=[sv/Q(a)**18,tv/Q(a)**17]
    # Direct check of v(x)^2=h(x) modulo u/a.
    hv0=Q(r0,a**36);hv1=Q(r1,a**35)
    if q[0]**2-Q(c,a)*q[1]**2!=hv0 or 2*q[0]*q[1]-Q(b,a)*q[1]**2!=hv1:raise RuntimeError('invalid square root')
    rec={'u_ascending':[c,b,a],'v_ascending':[str(z)for z in q],'support_degree':2,'discriminant':disc}
    if rec not in hits:hits.append(rec);print(json.dumps(rec),flush=True)
    break
 print(json.dumps({'a_done':a,'tested':tested,'hits':len(hits),'seconds':round(time.time()-start,3)}),flush=True)
 (ROOT/'exploratory/QUADRATIC_DIVISOR_SEARCH.json').write_text(json.dumps({'scope':'bounded search, no global completeness','a_max':a,'bc_bound':256,'tested':tested,'hits':hits,'seconds':time.time()-start},indent=2)+'\n')
