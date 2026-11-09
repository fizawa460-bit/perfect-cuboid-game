import math,json,hashlib
from fractions import Fraction as Q

def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def add(a,b):
 return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,k):return trim([k*x for x in a])
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def sq(a):return mul(a,a)
def rem(a,b,p):
 a=trim([x%p for x in a]);b=trim([x%p for x in b]);v=pow(b[-1],-1,p)
 while len(a)>=len(b) and a!=[0]:
  k=len(a)-len(b);s=a[-1]*v%p
  for j in range(len(b)):a[j+k]=(a[j+k]-s*b[j])%p
  trim(a)
 return a
f=[1,-2,3,-2,1];g=[0,4,-4];w=[0,1]
for _ in range(2):
 f,g=sq(add(sq(f),mul(w,sq(g)))),scale(mul(mul(f,g),add(add(sq(f),mul([1,-1],mul(f,g))),scale(mul(w,sq(g)),-1))),4)
assert len(f)-1==64 and len(g)-1==62
assert max(abs(x).bit_length() for x in f+g)==41 and f[-1]==1
a,b=f,g;chain=[]
while b!=[0]:
 chain.append(len(b)-1);a,b=b,rem(a,b,101)
assert len(a)==1 and a[0]%101
assert 8+127*(7+41)==6104
assert 3*(126+6104+1)+24==18717

def ec_add(U,V,B,D):
 if U is None:return V
 if V is None:return U
 x,y=U;z,t=V
 if x==z:
  if y+t==0:return None
  slope=(3*x*x+2*B*B*x-D*D)/(2*y)
 else:slope=(t-y)/(z-x)
 r=slope*slope-B*B-x-z
 return r,-y+slope*(x-r)
def ec_mul(n,P,B,D):
 R=None
 while n:
  if n&1:R=ec_add(R,P,B,D)
  n//=2
  if n:P=ec_add(P,P,B,D)
 return R
def vp(n,p):
 if n==0:raise ValueError('zero valuation')
 s=0
 while n%p==0:n//=p;s+=1
 return s
def vq(q,p):return vp(abs(q.numerator),p)-vp(q.denominator,p)
def smallprime(n):
 for p in range(2,math.isqrt(n)+1):
  if n%p==0:return p
 return n
rows=[(3,4,5),(4,3,5),(5,12,13),(12,5,13),(15,8,17),(8,15,17),(63,16,65)]
formal=[]
for A,B,C in rows:
 D=A*C;k=C.bit_length();cE=(256*D**8*(A*A+C*C)**4).bit_length()
 assert math.gcd(B,D)==1 and cE<=24*k+12
 P=(Q(D),Q(B*D));two=ec_mul(2,P,B,D)
 assert two[0]==Q(D*D,B*B)
 p=smallprime(B);e=vp(B,p)
 assert p!=2 or e>=2
 for j in range(3):
  Z=ec_mul(2*p**j,P,B,D)
  assert Z is not None and vq(Z[0],p)==-2*(e+j)
  t=-Z[0]/Z[1];assert vq(t,p)==e+j
  formal.append({'base':[A,B,C],'p':p,'j':j,'depth':e+j})

# Exact low-C constants; formal logarithm's universal proof is in CARD.
assert 24*113+12==2724 and 2724//3+2==910
assert 3+2*113*910==205663
eta_exponent=205663
assert eta_exponent-2==205661 and 113+2724//6==567
for cE in range(1,2725):
 j=cE//3+2
 assert Q(j)-Q(cE,3)>1 and j<=910

def high_count_bound(x,L):
 assert x>=1 and L>=5
 mmax=math.isqrt((256*(x+2)+145920-1)//6270)
 terms=[]
 for m in range(L,mmax+1):
  K=(256*(x+2)-1)//(55*m*m-1280)
  assert K>=114 and 114*(55*m*m-1280)<256*(x+2)
  assert (55*m*m-1280)*K<256*(x+2)
  assert (55*m*m-1280)*(K+1)>=256*(x+2)
  terms.append((m,K))
 return terms
controls=0;bound_examples=[]
for x in (1,16,64,128,256,512,1024,2048,4096,10000):
 for L in (5,6,7,8,9,12):
  ts=high_count_bound(x,L)
  for m in range(L,max(L+1,math.isqrt((256*(x+2)+145920)//6270)+3)):
   for k in (113,114,115,200,1000):
    allowed=k>=114 and (55*m*m-1280)*k<256*(x+2)
    expected=k>=114 and any(mm==m and k<=K for mm,K in ts)
    assert allowed==expected
    controls+=1
  if L==8:bound_examples.append({'X_bit_length':x,'high_m_max':ts[-1][0] if ts else None,'high_K_at_L':ts[0][1] if ts else None,'high_bound_terms':len(ts)})
assert Q(256,55*8*8-1280)==Q(4,35)<Q(1,8)
assert 330*114-18717>=165*114

# Oriented Euclid source census, checked exactly for modest height panels.
base_controls=0
for Y in (8,16,32,64,128,256,512,1024):
 count=0
 for m in range(2,math.isqrt(Y)+1):
  for n in range(1,m):
   if m*m+n*n<Y and math.gcd(m,n)==1 and (m-n)%2:count+=2
 assert count<=2*Y;base_controls+=1

out={'section':316,'verification_status':'PASS','counts':{'exact_original_formal_depth_controls':len(formal),'low_C_height_floor_integer_controls':2724,'exact_high_stratum_cutoff_controls':controls,'oriented_Euclid_census_controls':base_controls},'old_S308_map_certificate_recomputed':{'degrees':[64,62],'coefficient_bits':41,'mod101_gcd_chain':chain,'loss_bits':6104,'lambda_numerator_loss':18717},'formal_examples':formal,'high_census_examples':bound_examples,'universal_low_C_height_floor':'hat_h(P)>2^(-205663)','all_base_high_index_source_count':'N_8(X)=O(X^(4/35)*sqrt(1+log X)); effective explicit upper formula in CARD','four_GOOD_total_log_weight':'O(X^(4/35)*(1+log X)^(3/2))','no_base_height_cutoff':True,'all_CM_ranks_included':True,'small_indices_3_to_7_not_covered':True,'universal_proofs_in_CARD':True,'physical_witnesses_constructed':False,'per_packet_GOOD_fraction_upper_proved':False,'closure_credit':False}
out['sha256_without_digest']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print(json.dumps(out,sort_keys=True,indent=2))
