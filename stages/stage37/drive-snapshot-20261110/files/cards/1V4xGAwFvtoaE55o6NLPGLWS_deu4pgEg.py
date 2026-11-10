import math,json,collections
from pathlib import Path
height=100000; gap_bound=500
triples=set()
for m in range(2,math.isqrt(height)+1):
 for n in range(1,m):
  c=m*m+n*n
  if c>height or math.gcd(m,n)!=1 or (m-n)%2==0:continue
  a,b=sorted((m*m-n*n,2*m*n));triples.add((a,b,c))
scaled=0
for a,b,c in triples:
 d=b-a;w=a+b
 assert d>0 and d%2==1 and w*w-2*c*c==-d*d
 assert math.gcd(w,d)==math.gcd(w,c)==1
 assert math.gcd(a+b,c)==math.gcd(a-b,c)==math.gcd(a+b,a-b)==1
 for scale in (1,3):
  R=c*scale;g=R**3//c;U=g*b;V=g*a
  assert math.gcd(abs(U+V),R**3)==g
  assert math.gcd(abs(U-V),R**3)==g
  assert math.gcd(abs(U+V),abs(U-V))==g
  assert abs(abs(U)-abs(V))//g==d
  scaled+=1

def omega(v):
 p=2;count=0
 while p*p<=v:
  if v%p==0:
   count+=1
   while v%p==0:v//=p
  p+=1
 return count+(v>1)
seeds={};from_pell=set()
for d in range(1,gap_bound+1,2):
 arr=[]
 for c in range(1,3*d+1):
  w2=2*c*c-d*d
  if w2<=0:continue
  w=math.isqrt(w2)
  if w*w!=w2 or w%2==0 or c%2==0 or math.gcd(w,d)!=1:continue
  if 3*w-4*c>0:continue
  arr.append((w,c))
 assert len(arr)<=2**omega(d)
 seeds[d]=arr
 for w,c in arr:
  while c<=height:
   if w>d:
    a,b=(w-d)//2,(w+d)//2
    assert a>0 and math.gcd(a,b)==1 and a*a+b*b==c*c
    from_pell.add((a,b,c))
   w,c=3*w+4*c,2*w+3*c
expected={t for t in triples if t[1]-t[0]<=gap_bound}
assert expected==from_pell
# Reduce every small-gap Euclid label to an actual listed seed.
for a,b,c in expected:
 d=b-a;w=a+b
 while 3*w-4*c>0:w,c=3*w-4*c,3*c-2*w
 assert (w,c) in seeds[d]
# A fixed gap does not bound the phase hypotenuse.
w,c=1,1;seq=[]
for _ in range(10):
 w,c=3*w+4*c,2*w+3*c
 seq.append(((w-1)//2,(w+1)//2,c))
 assert w*w-2*c*c==-1
out={'card':'M3-T11-188','status':'PASS','primitive_phase_triangles_c_le':height,'primitive_phase_triangles_checked':len(triples),'scaled_integer_gcd_checks':scaled,'gap_bound':gap_bound,'primitive_pell_seeds':sum(map(len,seeds.values())),'complete_euclid_pell_match':len(expected),'gap_one_labels_first_last':[seq[0],seq[-1]],'physical_endpoints_enumerated':0,'scope':'Primitive conic/Pell directions and scaled norm labels only; no physical occupancy or asymptotic verification.'}
Path('M3-T11-188-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
