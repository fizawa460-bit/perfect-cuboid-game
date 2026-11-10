#!/usr/bin/env python3
import csv,math,json,hashlib,pathlib
LIMIT=10**6
sieve=bytearray(b'\1')*(LIMIT+1);sieve[:2]=b'\0\0'
for p in range(2,math.isqrt(LIMIT)+1):
 if sieve[p]:sieve[p*p::p]=b'\0'*(((LIMIT-p*p)//p)+1)
primes=[p for p in range(2,LIMIT+1) if sieve[p]]
def factor(n):
 out={}
 for p in primes:
  if p*p>n:break
  if n%p==0:
   k=0
   while n%p==0:n//=p;k+=1
   out[p]=k
 if n>1:out[n]=out.get(n,0)+1
 return out
def val(n,p):
 k=0
 while n%p==0:n//=p;k+=1
 return k

def sqrtmod(n,p):
 n%=p
 assert pow(n,(p-1)//2,p)==1
 if p%4==3:return pow(n,(p+1)//4,p)
 q=p-1;s=0
 while q%2==0:q//=2;s+=1
 z=2
 while pow(z,(p-1)//2,p)!=p-1:z+=1
 c=pow(z,q,p);x=pow(n,(q+1)//2,p);t=pow(n,q,p);m=s
 while t!=1:
  i=1;u=t*t%p
  while u!=1:u=u*u%p;i+=1
  b=pow(c,1<<(m-i-1),p);x=x*b%p;t=t*b*b%p;c=b*b%p;m=i
 return x

def local_odd(F,p):
 t=val(F,p);u=F//p**t
 return t%2==0 and pow(u%p,(p-1)//2,p)==1

def local2(F):
 t=val(F,2);return t%2==0 and (F//2**t)%8==1
rows=[{k:int(v) for k,v in r.items()} for r in csv.DictReader(open('M3-T11-207-raw-census.tsv'),delimiter='\t')]
records=[];branchrootchecks=0;checks=0;branch={'s<r':0,'s>r':0,'s=r':0};badR=[];allR=[];rootchecks=0;residual_examples=[]
for row in rows:
 e=[row['a'],row['b'],row['c']];R=row['R'];eligible=[i for i in range(3) if math.isqrt(R*R-e[i]**2)**2==R*R-e[i]**2]
 assert len(eligible)==2
 i,j=eligible;k=3-i-j;a=e[k];c=math.gcd(R,e[i])*math.gcd(R,e[j]);F=R*R-a*a
 h=math.gcd(R,a);epsilon=2 if a%2 else 1
 A=(R-a)//(epsilon*h);B=(R+a)//(epsilon*h)
 assert A>0 and B>A and math.gcd(A,B)==1 and F==(epsilon*h)**2*A*B
 branchbad=[]
 for p in factor(c):
  eta=pow((a//h)*pow(epsilon,-1,p)%p,(p-1)//2,p)
  assert pow(A,(p-1)//2,p)==pow(B,(p-1)//2,p)==eta
  if eta!=1:branchbad.append(p)
 assert c==row['c_raw_max'] and math.gcd(c,a)==math.gcd(c,F)==1
 rf=factor(R);cf=factor(c);ff=factor(F);kap=math.prod(p for p,t in ff.items() if t%2);sq=math.isqrt(F//kap)
 assert sq*sq*kap==F and kap>1
 assert R%2 and all(p%4==1 for p in rf)
 localbad=[];equal=[]
 for p,r in rf.items():
  s=val(a,p);name='s<r' if s<r else 's>r' if s>r else 's=r';branch[name]+=1
  okay=local_odd(F,p)
  if s!=r:assert okay
  else:equal.append(p)
  if not okay:localbad.append(p);assert s==r
  if kap%p==0:assert s==r
  checks+=1
 for p in cf:
  if p not in branchbad:
   for target in [A,B]:
    xx=sqrtmod(target,p);mm=p
    for ee in range(1,7):
     assert (xx*xx-target)%mm==0
     branchrootchecks+=1
     tt=((target-xx*xx)//mm)*pow(2*xx,-1,p)%p
     xx+=tt*mm;mm*=p
  assert p%4==1 and kap%p and pow(kap,(p-1)//2,p)==1
  x=sqrtmod(F,p);mod=p
  for exponent in range(1,7):
   assert (x*x-F)%mod==0 and math.gcd(x,p)==1
   rootchecks+=1
   t=((F-x*x)//mod)*pow(2*x,-1,p)%p
   x+=t*mod;mod*=p
  assert (x*x-F)%mod==0
 fa=factor(A);fb=factor(B);ka=math.prod(p for p,t in fa.items() if t%2);kb=math.prod(p for p,t in fb.items() if t%2)
 assert ka*kb==kap and math.gcd(ka,kb)==1
 for pp in rf:
  assert local_odd(A,pp)==(ka%pp!=0 and pow(ka,(pp-1)//2,pp)==1)
  assert local_odd(B,pp)==(kb%pp!=0 and pow(kb,(pp-1)//2,pp)==1)
 assert local2(A)==(ka%2==1 and ka%8==1) and local2(B)==(kb%2==1 and kb%8==1)
 branchRbad=[p for p in rf if not local_odd(A,p) or not local_odd(B,p)]
 branch2=local2(A) and local2(B)
 rec=dict(minus_kernel=ka,plus_kernel=kb,branch_conductor_obstructions=branchRbad,branch_local2_square=branch2,edges=e,R=R,shared_edge=a,c_chart=c,missing_square=F,primitive_content=h,parity_divisor=epsilon,coprime_minus=A,coprime_plus=B,branch_character_obstructions=branchbad,kappa=kap,kernel_square_multiplier=sq,conductor_primes=list(rf),saturated_shared_primes=equal,conductor_local_obstructions=localbad,local2_square=local2(F))
 records.append(rec)
 if localbad:badR.append(rec)
 else:allR.append(rec)
 if not localbad and local2(F):residual_examples.append(rec)
spectrum=[]
for bound in [1000,10000,100000,1000000]:
 for num,den in [(3,16),(5,24),(11,48)]:
  ss=[r for r in records if r['R']<=bound and r['c_chart']**den>bound**num]
  bb=[r for r in ss if not r['branch_character_obstructions']]
  cc=[r for r in bb if not r['conductor_local_obstructions'] and r['local2_square']]
  spectrum.append(dict(B=bound,exponent=f'{num}/{den}',chart_tail=len(ss),coupled_branch_content_mask=len(bb),plus_2_and_conductor_F_mask=len(cc),full_2R_branch_mask=sum(not r['branch_conductor_obstructions'] and r['branch_local2_square'] for r in ss)))
summary=dict(card='M3-T11-208',scope='raw local-saturation/support theorem; no asymptotic tail estimate',raw_records=len(records),records_passing_full_2R_branch_mask=sum(not r['branch_conductor_obstructions'] and r['branch_local2_square'] for r in records),full_2R_branch_survivor_examples=[r for r in records if not r['branch_conductor_obstructions'] and r['branch_local2_square']][:3],records_passing_coupled_branch_content_mask=sum(not r['branch_character_obstructions'] for r in records),coupled_branch_obstruction_examples=[r for r in records if r['branch_character_obstructions']][:3],threshold_spectrum=spectrum,all_records_global_missing_face_nonsquare=True,conductor_prime_checks=checks,depth_branch_counts=branch,content_prime_power_root_checks=rootchecks,accepted_coprime_branch_prime_power_root_checks=branchrootchecks,Hensel_orders='1 through6 checked, theorem all positive orders',records_with_conductor_local_obstruction=len(badR),records_locally_square_at_all_conductor_primes=len(allR),records_locally_square_at_2_and_all_conductor_primes=len(residual_examples),example=next(r for r in records if r['edges']==[104,153,672]),saturated_obstruction_examples=badR[:3],fresh_obstruction_examples=residual_examples[:3],source_census_sha256=hashlib.sha256(pathlib.Path('M3-T11-207-raw-census.tsv').read_bytes()).hexdigest(),script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
pathlib.Path('M3-T11-208-verification.json').write_text(json.dumps(dict(summary=summary,records=records),indent=2)+'\n')
print(json.dumps(summary,indent=2))
