"""Exact replay; independent root lifting and determinant interpolation controls.
Requires NumPy only. Does not certify global Selmer, MW, or source exclusion.
"""
from local2_arithmetic import *
from tame_local_points import Tame,irreducible,image_unit
from local2_constraints import build_constraints,norm_unit_mod8
from fractions import Fraction
from math import comb,factorial
import hashlib,random,time,sys

checks=0;negatives=0
def check(ok,label):
 global checks
 if not ok:raise RuntimeError(label)
 checks+=1
def negative(ok,label):
 global negatives
 if ok:raise RuntimeError('unrejected '+label)
 negatives+=1
def bits(a):return sum((int(c)&1)<<i for i,c in enumerate(a))
def unbits(a):return np.array([(a>>i)&1 for i in range(36)],dtype=np.int64)

def solve_cols(cols,target):
 piv={};kernel=[]
 for i,c in enumerate(cols):
  v=c;w=1<<i
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=(v,w);break
   v^=piv[k][0];w^=piv[k][1]
  if not v:kernel.append(w)
 v=target;w=0
 while v:
  k=v.bit_length()-1
  if k not in piv:return None,kernel,len(piv)
  v^=piv[k][0];w^=piv[k][1]
 return w,kernel,len(piv)

EYE=[unbits(1<<j)for j in range(36)]
SQ=[bits(mul(e,e))for e in EYE]
_,SQUARE_KERNEL,SQUARE_RANK=solve_cols(SQ,0)
check(SQUARE_RANK==24 and len(SQUARE_KERNEL)==12,'mod2 square map')
for k in SQUARE_KERNEL:check(bits(mul(unbits(k),unbits(k)))==0,'Frobenius kernel')
for i,k in enumerate(SQUARE_KERNEL):
 for l in SQUARE_KERNEL[:i]:check(not np.any((2*mul(unbits(k),unbits(l)))%4),'linear mod4 adjustment')

def square_via_independent_lifting(a):
 """r mod2 -> mod4 -> mod8; uses no unit filtration coordinates."""
 aa=a%8;y,_,_=solve_cols(SQ,bits(aa))
 if y is None:return False
 yy=unbits(y);ysq=mul(yy,yy)%8
 delta=(aa-ysq)%4
 check(not np.any(delta%2),'initial square parity')
 adj=[]
 for k in SQUARE_KERNEL:
  kk=unbits(k);v=(2*mul(yy,kk)+mul(kk,kk))%4
  check(not np.any(v%2),'kernel square even')
  adj.append(bits(v//2))
 c,_,r=solve_cols(adj,bits(delta//2))
 check(r==12,'mod4 adjustment rank')
 if c is None:return False
 for i,k in enumerate(SQUARE_KERNEL):
  if(c>>i)&1:y^=k
 yy=unbits(y);ysq=mul(yy,yy)%8
 delta=(aa-ysq)%8
 check(not np.any(delta%4),'square mod4')
 columns=[bits((mul(e,e)+mul(yy,e))%2)for e in EYE]
 c,_,r=solve_cols(columns,bits(delta//4))
 check(r==34,'Artin Schreier rank34')
 if c is None:return False
 rr=(yy+2*unbits(c))%8
 check(np.array_equal(mul(rr,rr)%8,aa),'square mod8 root')
 return True

def bareiss(m):
 a=[list(map(int,r))for r in m];n=len(a);last=1;sgn=1
 for k in range(n-1):
  if not a[k][k]:
   j=next((i for i in range(k+1,n)if a[i][k]),None)
   if j is None:return 0
   a[k],a[j]=a[j],a[k];sgn=-sgn
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=a[i][j]*pivot-a[i][k]*a[k][j]
    if num%last:raise RuntimeError('Bareiss nonexact')
    a[i][j]=num//last
   a[i][k]=0
  last=pivot
 return sgn*a[-1][-1]

def charpoly_by_determinants(E,a):
 """n+1 exact determinants + Newton interpolation, no matrix-power traces."""
 mat=np.einsum('i,ijk->kj',a,E.tab,optimize=False)%E.mod;n=E.n
 values=[bareiss([[(t if i==j else 0)-int(mat[i,j])for j in range(n)]for i in range(n)])for t in range(n+1)]
 differences=[]
 while values:
  differences.append(values[0]);values=[b-a for a,b in zip(values,values[1:])]
 out=[Fraction(0)]*(n+1);falling=[1]
 for k,d in enumerate(differences):
  for j,c in enumerate(falling):out[j]+=Fraction(d*c,factorial(k))
  new=[0]*(len(falling)+1)
  for j,c in enumerate(falling):new[j]-=k*c;new[j+1]+=c
  falling=new
 check(all(c.denominator==1 for c in out),'det polynomial integrality')
 return[int(c)%E.mod for c in out]

def k_mul_by_polynomial_quotient(a,b):
 """Independent quotient arithmetic over exact rational polynomials."""
 aa=[Fraction(int(c),1<<(i//3))for i,c in enumerate(a)]
 bb=[Fraction(int(c),1<<(i//3))for i,c in enumerate(b)]
 cc=[Fraction(0)]*71
 for i,x in enumerate(aa):
  for j,y in enumerate(bb):cc[i+j]+=x*y
 for k in range(70,35,-1):
  c=cc[k]
  for j in range(36):cc[k-36+j]-=c*F[j]
 out=[]
 for i,c in enumerate(cc[:36]):
  c*=1<<(i//3);check(c.denominator==1,'independent ring integrality');out.append(int(c)%MOD)
 return np.array(out,dtype=np.int64)

start=time.time();cert=json.loads((ROOT/'dyadic_full_kummer_certificate.json').read_text())
for name,sha in cert['parent_sha256'].items():check(hashlib.sha256((ROOT/'parents'/name).read_bytes()).hexdigest()==sha,'parent SHA '+name)
check(H==cert['h2_coefficients_ascending'],'h2 lock')
check(F==cert['F_u_coefficients_ascending'],'F lock')
check(pgf_mul(FACTORS[0],FACTORS[1],1<<13)==R,'residual factorization')
for f in FACTORS:check(irreducible(f),'residual irreducibility')
# Independent Horner polynomial composition h2(2u-3).
hh=[0]
for c in reversed(H):
 nn=[0]*(len(hh)+1)
 for i,z in enumerate(hh):nn[i]-=3*z;nn[i+1]+=2*z
 nn[0]+=c;hh=nn
while len(hh)>37 and hh[-1]==0:hh.pop()
check(hh==[c*2**36 for c in F],'Horner composition')
zz=[0]*19;zz[18]=1;zz[15]=2;zz[16]=2
sq=[0]*37
for i,a in enumerate(zz):
 for j,b in enumerate(zz):sq[i+j]+=a*b
check(all((a-b)%8==0 for a,b in zip(F,sq)),'unramified unit square Hensel identity')
check([bin(f)for f in FACTORS]==['0b11111','0b111111001'],'residual fields exact')

rng=random.Random(35520261104)
for trial in range(8):
 a=np.array([rng.randrange(MOD)for i in range(36)],dtype=np.int64)
 b=np.array([rng.randrange(MOD)for i in range(36)],dtype=np.int64)
 check(np.array_equal(mul(a,b),k_mul_by_polynomial_quotient(a,b)),'independent ring multiplication')

unitbasis=[]
for level in (1,3,5):
 for k in range(12):
  a=GEN[(level,k)];c=unit_class(a)
  check(c==1<<((level//2)*12+k),'filtration basis coordinate')
  check(not square_via_independent_lifting(a),'independent nonsquare basis')
  unitbasis.append(c)
for k in range(12):
 a=(ONE+mul(power(U,6),lift(1<<k)))%MOD
 c=unit_class(a);unitbasis.append(c)
 check((c==0)==square_via_independent_lifting(a),'top-layer independent square test')
check(rank(unitbasis)==38,'unit squareclass dimension38')
check(square_via_independent_lifting(5*ONE),'rational5 square in both even residue fields')
negative(square_via_independent_lifting((-ONE)%MOD),'minus1 is not square')

for i in range(32):
 def randunit():
  while True:
   a=np.array([rng.randrange(MOD)for j in range(36)],dtype=np.int64)
   if all(pgf_mod(residue(a),f)for f in FACTORS):return a
 a=randunit();b=randunit()
 check(unit_class(mul(a,b))==unit_class(a)^unit_class(b),'character product law')
 check(unit_class(mul(a,a))==0,'square character zero')
 if i<8:check(square_via_independent_lifting(mul(a,a)),'independent random square')
 if i<8:check((unit_class(a)==0)==square_via_independent_lifting(a),'independent random square decision')

chars=[int(cert['scalar_minus1_character_hex'],16)];tame_count=0;unram_count=0;old_count=0
for r in cert['selected_fake_basis']:
 a=np.array(r['unit_basis_mod256'],dtype=np.int64)
 check(unit_class(a)==int(r['character_hex'],16),'basis image character '+r['label'])
 check(norm_unit_mod8(a)==1,'each actual divisor image has square norm')
 if r['kind']=='unramified_unit_point':
  g=r['poly_u'];binary=sum((c&1)<<i for i,c in enumerate(g))
  check(irreducible(binary),'unramified minimal polynomial')
  check(g[-1]==1 and g[0]&1,'unramified unit point')
  check(np.array_equal(eval_u(g),a),'unramified norm image');unram_count+=1
 elif r['kind']=='tame_e3_point':
  m=r['m_binary'];f=r['f'];check(irreducible(m),'tame residue field irreducibility')
  check(f==pgf_deg(m),'tame field degree')
  check(pgf_mod(R,m)!=0,'unit y residue')
  derivative=sum(((i*((R>>i)&1))&1)<<(i-1)for i in range(1,13))
  check(pgf_mod(derivative,m)!=0,'Hensel derivative unit')
  E=Tame(m,r['field_precision']);y=np.array(r['y_basis_mod'],dtype=np.int64);u=np.array(r['u_basis_mod'],dtype=np.int64)
  # Divide by pi with one bit of loss, then verify the root to that precision.
  nn=E.n;mm=E.mod;newmod=mm//2
  check(all(int(u[3*k])%2==0 for k in range(f)),'u divisible by pi')
  last=(-int(u[0])//2)%newmod
  z=[]
  for k in range(1,nn):
   final=-2*E.mc[k//3] if k%3==0 else 0
   numerator=(int(u[k])-final*last)%mm
   if k%3==0:
    check(numerator%2==0,'pi division parity');numerator//=2
   z.append(numerator%newmod)
  z.append(last);z=np.array(z,dtype=np.int64)
  check(E.res(z)==1,'Hensel initial root')
  err=(E.peval(E.G,z)-E.mul(y,y))%newmod
  check(not np.any(err),'certified Hensel approximation')
  g=charpoly_by_determinants(E,u)
  check(g==r['norm_poly_mod'],'independent determinant norm polynomial')
  check(np.array_equal(image_unit(g,f),a),'normalized norm class')
  check(E.prec-1-f>=PREC,'precision after rational norm scaling')
  tame_count+=1
 else:old_count+=1
 chars.append(int(r['character_hex'],16))
check(rank(chars)==19,'fake basis independent modulo scalar')
for i in range(1,len(chars)):negative(rank(chars[:i]+chars[i+1:])==19,'basis member removable')
# A deliberately damaged character matrix must lose one dimension.
damaged=chars.copy();damaged[-1]=damaged[-2]
negative(rank(damaged)==19,'duplicated character mistaken as full basis')
check(old_count==6 and unram_count==3 and tame_count==9,'basis source counts')
interface=build_constraints(cert)
check(interface==cert['local_constraint_interface'],'constraint interface exact')
constraints=[int(h,16)for h in interface['unit_fake_image_constraints_hex']]
check(rank(constraints)==19,'orthogonal constraint rank19')
for h in constraints:
 for c in chars:check((h&c).bit_count()%2==0,'annihilator matrix')
normrows=[int(h,16)for h in interface['unit_norm_characters_hex']]
check(rank(constraints+normrows)==19 and rank(normrows)==2,'norm rows already within constraints')
check(cert['local_fake_Kummer_image_dimension']==18 and cert['local_true_Kummer_JQ2_mod2_dimension']==19,'new exact dimensions')
check(cert['new_original_signed_source_exclusions']==0 and not cert['global_Selmer_dim16_proved'],'claim boundaries')

out={'status':'PASS_INTERNAL_EXACT_REPLAY_NOT_INDEPENDENT_MATH_AUDIT','checks':checks,'negative_controls':negatives,
 'unit_coordinates':38,'independent_frobenius_square_rank':24,'mod4_adjustment_rank':12,'mod8_Artin_Schreier_rank':34,
 'rank_including_scalar_minus1':19,'fake_local_image_dim':18,'true_local_image_dim':19,
 'basis_old_global_divisors':6,'basis_new_unramified_local_divisors':unram_count,'basis_new_tame_local_divisors':tame_count,
 'independent_norm_polynomial_method':'n+1 integer Bareiss determinants and exact rational interpolation, versus discovery matrix-power Newton traces',
 'independent_square_test':'mod2/mod4/mod8 root lifting, no filtration-coordinate use',
 'unit_constraint_rank':19,'norm_constraint_rank':2,'extra_local_constraints_after_norm':18,'global_independent_codimension_computed':False,
 'new_global_MW_rank':False,'global_Selmer_bound16':False,'source_exclusions':0,'elapsed_seconds':round(time.time()-start,3)}
target=Path(sys.argv[1])if len(sys.argv)>1 else ROOT/'LOCAL2_EXACT_REPLAY_RESULT.json'
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
