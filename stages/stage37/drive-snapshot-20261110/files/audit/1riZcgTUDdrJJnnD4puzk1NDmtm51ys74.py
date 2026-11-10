from fractions import Fraction
from pathlib import Path
import json
from math import isqrt,gcd

def local(p):
 chi=[0]*p
 for a in range(1,p):chi[a]=1 if pow(a,(p-1)//2,p)==1 else -1
 roots=[1+x for x in chi]
 total=trace=boundary=states=0
 triples=((1,b,c) for b in range(p) for c in range(p))
 def consume(a,b,c):
  nonlocal total,trace,boundary,states
  aa,bb,cc=a*a%p,b*b%p,c*c%p
  w=roots[(aa+bb)%p]*roots[(aa+cc)%p]*roots[(bb+cc)%p]
  if not w:return
  t=(aa+bb+cc)%p
  assert t!=0
  states+=1;total+=w;trace+=w*chi[t]
  if not a*b*c:boundary+=w
 for t in triples:consume(*t)
 for c in range(p):consume(0,1,c)
 consume(0,0,1)
 return dict(p=p,projective_K3_points=total,terminal_trace=trace,bias=str(Fraction(trace,total)),zero_terminal_points=0,edge_boundary_points=boundary,edge_residue_states=states)

primes=[3,7,11,19,23,31,43,47,59,67,71,79,83,103]
rows=[local(p) for p in primes]
# Independent exact CRT product-state moments, including nonzero local bias.
moments=[]
for k in [1,2,3,5,8,13]:
 a=[Fraction(r['terminal_trace'],r['projective_K3_points']) for r in rows[1:k+1]]
 total=Fraction(k)+sum(2*a[i]*a[j] for i in range(k) for j in range(i+1,k))
 moments.append(dict(k=k,crt_second_moment_bound=str(total/(k*k)),bias_aware=True))
# Half of objects have every chi=+1, half every chi=-1.
# Single marginals vanish but pair correlations are1; endpoint-compatible mass stays1/2.
counterexample=dict(single_marginal=0,pair_correlation=1,all_plus_mass='1/2',second_moment_bound=1)
assert rows[0]['terminal_trace']==rows[0]['projective_K3_points']
examples=[]
for x,y,z in [(117,44,240),(85,132,720),(693,140,480)]:
 assert gcd(x,gcd(y,z))==1
 assert all(isqrt(t)**2==t for t in [x*x+y*y,x*x+z*z,y*y+z*z])
 a=isqrt(x*x+y*y)-y;b=isqrt(x*x+z*z)-z
 assert x*x%a==0 and x*x%b==0
 k=4*x*x+(x*x//a-a)**2+(x*x//b-b)**2
 assert k==4*(x*x+y*y+z*z)
 assert all(k%p!=0 for p in primes)
 assert all(pow(k%p,(p-1)//2,p)==1 for p in [3,11])
 examples.append(dict(odd_edge=x,even_edges=[y,z],divisors=[a,b],integer_kernel=k))
out=dict(status='PASS',local_projective_enumeration=rows,crt_moment_examples=moments,single_marginals_counterexample=counterexample,physical_integer_kernel_examples=examples,physical_M3_equidistribution_proved=False,global_counting_credit=0)
Path('/workspace/scratch/a5e20b2bdfbe/verify157-result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
