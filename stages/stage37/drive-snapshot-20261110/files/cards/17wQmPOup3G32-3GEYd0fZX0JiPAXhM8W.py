from math import gcd,isqrt
from collections import defaultdict
from pathlib import Path
import json

# Integer circles only: these are a larger algebraic test locus, not endpoints.
circles=defaultdict(set)
for m in range(2,72):
 for n in range(1,m):
  d=m*m+n*n
  if d>5000 or gcd(m,n)!=1 or (m-n)%2==0:continue
  a=m*m-n*n;b=2*m*n
  for scale in range(1,5000//d+1):
   R=scale*d
   if R%2:circles[R].update(((scale*a,scale*b),(scale*b,scale*a)))
counts=defaultdict(int);examples={};reconstruction=0
for R,cs in circles.items():
 cs=sorted(cs)
 for j,(e1,f1) in enumerate(cs):
  h1=gcd(e1,R)
  for e2,f2 in cs[j+1:]:
   h2=gcd(e2,R)
   if gcd(h1,h2)!=1:continue
   k=h1*h2;assert R%k==0
   c=[];phi=[];u=[]
   for sign in (1,-1):
    q=e1*e2+sign*f1*f2;p=f1*e2-sign*e1*f2
    den=R*R//gcd(q,p)
    assert den%k==0
    root=isqrt(den//k);assert root*root==den//k
    c.append(den);u.append(root);phi.append(k*root)
    assert R%(k*root)==0
    N=k*root;assert N*N%k==0 and N*N//k==den
    reconstruction+=1
   assert gcd(u[0],u[1])==1 and u[0]*u[1]==R//k
   assert c[0]*c[1]==R*R and gcd(c[0],c[1])==k
   assert gcd(phi[0],phi[1])==k and phi[0]*phi[1]==k*R
   label='unit_pair' if k==1 else ('one_nonunit' if min(h1,h2)==1 else 'two_nonunit')
   counts[label]+=1
   if label not in examples:examples[label]={'R':R,'edges':[e1,e2],'diagonals':[f1,f2],'contents':[h1,h2],'kappa':k,'pair_denominators':c,'roots':u,'Phi':phi}
# A concrete pair showing square denominator need not survive non-unit content.
R=65;e1=25;f1=60;e2=39;f2=52;k=65
cp=[R*R//gcd(e1*e2+t*f1*f2,f1*e2-t*e1*f2) for t in (1,-1)]
assert cp==[65,65] and isqrt(cp[0])**2!=cp[0]
out={'card':'M3-T11-195','coprime_content_circle_pairs':dict(counts),'signed_denominator_reconstruction_checks':reconstruction,'examples':examples,'non_square_example':{'R':65,'contents':[5,13],'denominators':cp},'physical_endpoints':0,'independent_audit':False,'status':'PASS'}
Path('M3-T11-195-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
