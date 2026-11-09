"""Exact certificate for Cl(O_K)=1, using explicit principal primes.

Discovery may use bnfinit. Verification does not use bnfinit, bnfcertify,
GRH, floating point, an analytic class-number formula, or a unit index.
Needs python-flint solely for exact integer polynomial resultants.
The old maximal order and unconditional Weil explicit formula are parents.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,lcm,isqrt
import json,sys,time,hashlib,os
ROOT=Path(__file__).resolve().parent
if os.environ.get('STAGE35EX_DEPS'):sys.path.insert(0,os.environ['STAGE35EX_DEPS'])
from flint import fmpz_poly
start=time.monotonic();checks=0;negatives=0
def check(ok,label):
 global checks
 if not ok:raise ArithmeticError(label)
 checks+=1
def negative(ok,label):
 global negatives
 if ok:raise ArithmeticError('negative accepted: '+label)
 negatives+=1
def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def prem(a,b,p):
 a=trim([c%p for c in a]);b=trim([c%p for c in b]);iv=pow(b[-1],-1,p)
 while len(a)>=len(b)and a!=[0]:
  k=len(a)-len(b);v=a[-1]*iv%p
  for j,c in enumerate(b):a[k+j]=(a[k+j]-v*c)%p
  a=trim(a)
 return a
def gcdmod(a,b,p):
 while b!=[0]:a,b=b,prem(a,b,p)
 return [(z*pow(a[-1],-1,p))%p for z in a]
def mulmod(a,b,g,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return prem(c,g,p)
def powmod(a,n,g,p):
 z=[1]
 while n:
  if n&1:z=mulmod(z,a,g,p)
  a=mulmod(a,a,g,p);n>>=1
 return z
def irreducible(g,p):
 n=len(g)-1
 if n<1:return False
 if n==1:return True
 xp=[0,1]
 for k in range(1,n+1):
  xp=powmod(xp,p,g,p)
  if k<=n//2:
   z=xp+[0]*max(0,2-len(xp));z[1]=(z[1]-1)%p
   if len(gcdmod(g,trim(z),p))>1:return False
 return xp==[0,1]
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def coarse(x,upper=False):
 d=10**12;n=x.numerator*d//x.denominator
 if upper and Q(n,d)!=x:n+=1
 return Q(n,d)
def log_interval(x,terms=28):
 x=Q(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def series(y):
  z=(y-1)/(y+1);power=z;s=Q(0)
  for j in range(terms):s+=2*power/(2*j+1);power*=z*z
  return s,s+2*power/((2*terms+1)*(1-z*z))
 a,b=series(x);c,d=series(Q(2))
 return (a+k*c,b+k*d)if k>=0 else(a+k*d,b+k*c)
def atan_interval(x,terms=36):
 s=sum(((-1)**j*x**(2*j+1)/Q(2*j+1)for j in range(terms)),Q(0));v=(-1)**terms*x**(2*terms+1)/Q(2*terms+1)
 return min(s,s+v),max(s,s+v)
def exp_minus_lower(t):
 # Odd Taylor polynomial is a global lower bound by its integral remainder.
 term=Q(1);s=term
 for j in range(1,24):term*=(-t)/j;s+=term
 return coarse(s)
def pair(x):return[x.numerator,x.denominator]
def basis_coords(q,d):return[sum(q[k]*comb(k,j)for k in range(j,len(q)))*Q(2**(j//3),d)for j in range(36)]
def load(p):return json.loads(p.read_text())
parent=load(ROOT/'parents/row359_three_units.json');F=parent['V_minimal_polynomial_ascending'];FP=fmpz_poly(F)
order=load(ROOT/'parents/maximal_order.json');DK=parent['field_discriminant']
check(DK==(1<<24)*order['odd_discriminant_factor'],'old exact field discriminant')
check(order['global_maximal_order_established']and order['number_field_signature']==[4,16],'inherited maximal order and signature')
check(len(F)==37 and F[-1]==1 and F[0]==1,'same old V field')
if '--build'in sys.argv:
 raw=load(ROOT.parent/'exploratory/PRINCIPAL_PRIMES_30000_FROZEN.json');records=[]
 for u in raw['records']:
  cs=list(map(Q,u['generator_coefficients_V']));d=lcm(*(z.denominator for z in cs));q=[int(z*d)for z in cs];pp=u['rational_prime']
  G=gcdmod(F,[z%pp for z in q],pp)
  records.append({'p':pp,'f':u['residue_degree'],'norm':u['generator_norm'],'denominator':d,'numerator':q,'residue_factor_ascending':G})
 data={'scope':'explicit principal primes, not a complete small-prime enumeration','V_polynomial_ascending':F,'norm_bound':30000,'records':records,'bnf_or_GRH_used_in_proof':False}
 (ROOT/'principal_prime_generators.json').write_text(json.dumps(data,indent=2)+'\n')
else:data=load(ROOT/'principal_prime_generators.json')
check(data['V_polynomial_ascending']==F and data['bnf_or_GRH_used_in_proof']is False,'fixed input and unconditional proof flag')
seen=set();norms=[];normcounts={}
for r in data['records']:
 pp=r['p'];f=r['f'];q=r['numerator'];d=r['denominator'];G=r['residue_factor_ascending']
 check(prime(pp)and pp!=2,'odd rational prime')
 check(len(q)==36 and d>0 and d&(d-1)==0,'generator power-of-two denominator')
 bc=basis_coords(q,d);check(all(z.denominator==1 for z in bc),'generator integral in OLD maximal basis')
 result=int(FP.resultant(fmpz_poly(q)))
 check(result==r['norm']*d**36 and abs(r['norm'])==pp**f,'exact integer resultant certifies prime-power norm')
 check(gcdmod(F,[z%pp for z in q],pp)==G,'actual common residue factor')
 check(len(G)-1==f and irreducible(G,pp),'irreducible degree-f residue factor')
 # Since the power-order index is a power of2, this factor identifies a
 # prime of norm p^f; divisibility and equal norms show (alpha)=that prime.
 key=(pp,tuple(G));check(key not in seen,'distinct principal prime ideals')
 seen.add(key);norms.append(pp**f);normcounts[pp**f]=normcounts.get(pp**f,0)+1
check(len(norms)>=3000 and max(norms)<=30000,'finite explicit splitting-prime set')
aa,bb=atan_interval(Q(1,5));cc,dd=atan_interval(Q(1,239))
pi_lo=coarse(16*aa-4*dd);pi_hi=coarse(16*bb-4*cc,True)
N=8192;harm=sum((Q(1,j)for j in range(1,N+1)),Q(0));gamma_lo=coarse(harm-log_interval(N+1)[1])
M=100;zz=sum((Q(1,j**3)for j in range(1,M+1)),Q(0));zeta_hi=coarse(zz+Q(1,2*M*M),True)
log4pi_lo=coarse(log_interval(4*pi_lo)[0]);logD_hi=coarse(log_interval(DK)[1],True)
alpha=Q(1,100);moment=126*zeta_hi+4*pi_hi*pi_hi/3
base=36*(gamma_lo+log4pi_lo)+4-logD_hi-alpha*moment
terms=[];prime_sum=Q(0)
for q,multiplicity in sorted(normcounts.items()):
 lo,hi=log_interval(q);lo=coarse(lo);hi=coarse(hi,True)
 ex=exp_minus_lower(alpha*hi*hi);check(ex>0,'positive certified Gaussian value')
 contribution=coarse(4*lo*ex/Q(1+q));prime_sum+=multiplicity*contribution
 terms.append({'q':q,'multiplicity':multiplicity,'log_interval':[pair(lo),pair(hi)],'gaussian_lower':pair(ex),'prime_term_lower':pair(contribution)})
Delta=base+prime_sum
check(Delta>Q(179,10),'Hilbert class field gap exceeds17.9')
check(4*pi_hi/alpha<Q(71,2)**2,'Gaussian pole correction E<35.5')
check(2*Delta>Q(71,2),'all Hilbert class field degrees>=2 excluded')
check(2*Q(179,10)>Q(71,2),'coarse displayed constants suffice')
negative(int(FP.resultant(fmpz_poly([data['records'][0]['numerator'][0]+1]+data['records'][0]['numerator'][1:])))==data['records'][0]['norm']*data['records'][0]['denominator']**36,'changed generator norm')
negative(prime(289),'composite rational-prime control')
negative((data['records'][0]['p'],tuple(data['records'][0]['residue_factor_ascending']))not in seen,'repeated principal prime must not double count')
negative(base>Q(179,10),'principal splitting contributions cannot be omitted')
negative(Q(71,2)<2*Q(17),'weaker coarse gap17 does not certify class number1')
out={'scope':'fixed K=Q(V), V^4=theta only','field_degree':36,'signature':[4,16],'field_discriminant':DK,'principal_prime_count':len(norms),'norm_bound':max(norms),'alpha':pair(alpha),'Gaussian_function':'exp(-x^2/100)','prime_powers_used':[1],'archimedean_moment_upper':pair(coarse(moment,True)),'base_gap_lower':pair(coarse(base)),'principal_prime_term_lower':pair(coarse(prime_sum)),'Delta_lower':pair(coarse(Delta)),'display_coarse_Delta_strict_lower':[179,10],'pole_E_strict_upper':[71,2],'ordinary_class_number_exact':1,'ordinary_class_group':[],'ordinary_c_K_exact':0,'GRH_assumed':False,'bnfcertify_used_as_proof':False,'all_MW_residual_U_constructed':False,'new_independent_mathematical_audit':'PENDING_NOT_RUN','input_sha256':{'principal_prime_generators.json':hashlib.sha256((ROOT/'principal_prime_generators.json').read_bytes()).hexdigest()},'rational_prime_terms':terms}
if '--build'in sys.argv:(ROOT/'class_one_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
else:check(load(ROOT/'class_one_certificate.json')==out,'frozen analytic certificate matches exact replay')
log={'status':'INTERNAL_EXACT_PASS','checks':checks,'negative_controls':negatives,'class_number':1,'c_K':0,'principal_primes':len(norms),'Delta_lower':str(coarse(Delta)),'E_strict_upper':'35.5','GRH':False,'independent_audit':'PENDING_NOT_RUN','seconds':round(time.monotonic()-start,3)}
name='CLASS_ONE_'+('NORMAL'if __debug__ else'OPTIMIZED')+'_REPLAY.json';(ROOT/name).write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log))
