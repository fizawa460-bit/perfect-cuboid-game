"""Run after compiling/running verify158.cpp; finite diagnostics, not an asymptotic proof."""
import csv,json,math,hashlib
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
rows=[{k:int(v) for k,v in r.items()} for r in csv.DictReader(Path('M3-T11-158-census.tsv').open(),delimiter='\t')]
primes=[3,7,11,19,23,31,43,47,59,67,71,79,83,103]
selected=[7,19,23,31,43,47,59,67,71,79,83,103]
def chi(t,p):
 r=pow(t%p,(p-1)//2,p)
 return -1 if r==p-1 else r
for r in rows:
 x,y,z,t=(r[k] for k in ['X','Y','Z','T'])
 assert x%2 and y<z and y%4==0 and z%4==0
 assert math.gcd(x,math.gcd(y,z))==1 and t==x*x+y*y+z*z and t<=10**12
 assert all(r[d]**2==a*a+b*b for d,a,b in [('Dxy',x,y),('Dxz',x,z),('Dyz',y,z)])
 a=r['Dxy']-y;b=r['Dxz']-z
 assert a<x and b<x and x*x%a==0 and x*x%b==0
 assert 4*x*x+(x*x//a-a)**2+(x*x//b-b)**2==4*t
 assert all(chi(t,p) in [-1,1] for p in primes)
 assert chi(t,3)==chi(t,11)==1
 sf=r['squarefree_T'];q=math.isqrt(t//sf)
 assert sf*q*q==t
assert len(rows)==len({(r['X'],r['Y'],r['Z']) for r in rows})==219
snapshots=[]
for B in [1000,10000,100000,1000000]:
 pop=[r for r in rows if r['T']<=B*B];N=len(pop)
 nus=Counter(r['T'] for r in pop);sd=Counter(r['squarefree_T'] for r in pop)
 assert not any(t%2==0 for t in nus)
 # Sparse exact total variation: include both zero boundaries.
 tv=sum(abs(nus.get(t+1,0)-nus.get(t,0)) for t in set(nus)|{n-1 for n in nus})
 assert tv==2*N
 W={f'{p},{q}':sum(chi(r['T'],p)*chi(r['T'],q) for r in pop) for p,q in combinations(selected,2)}
 k=len(selected);sq=sum(sum(chi(r['T'],p) for p in selected)**2 for r in pop)
 assert sq==k*N+2*sum(W.values())
 passcount=sum(all(chi(r['T'],p)==1 for p in selected) for r in pop)
 P=sum(r['squarefree_T']==1 for r in pop)
 assert P<=passcount and k*k*passcount<=sq
 snapshots.append({'B':B,'M3':N,'endpoint_count_finite_only':P,'terminal_variation':tv,'distinct_terminal_values':len(nus),'distinct_terminal_squareclasses':len(sd),'squareclass_collision_energy':sum(v*v for v in sd.values()),'max_squareclass_occupancy':max(sd.values()),'selected_primes':selected,'one_prime_means':{str(p):str(Fraction(sum(chi(r['T'],p) for r in pop),N)) for p in selected},'pair_W':W,'pair_C':{pq:str(Fraction(w,N)) for pq,w in W.items()},'all_selected_prime_pass_count':passcount,'157_second_moment_upper_fraction':str(Fraction(sq,k*k*N))})
out={'status':'PASS','scope':'Complete primitive Euler bricks with sqrt(T)<=1000000, X unique odd, Y<Z; two independent face enumerations matched. No infinite-height inference.','initial_integer_overflow_guard_corrected_before_final_census':True,'sha256_census':hashlib.sha256(Path('M3-T11-158-census.tsv').read_bytes()).hexdigest(),'snapshots':snapshots}
Path('verify158-result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'snapshots':[{k:s[k] for k in ['B','M3','squareclass_collision_energy','max_squareclass_occupancy','all_selected_prime_pass_count','157_second_moment_upper_fraction']} for s in snapshots]},indent=2))
