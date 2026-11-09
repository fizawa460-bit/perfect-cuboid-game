"""Independent exact identities for the NEW dyadic frame and torsion arithmetic.

No PARI calls. General descent, Neron-model and Selmer-Chabauty arguments
are supplied by the mathematical report; row365 is not independently audited.
"""
import os,sys,json,math,copy
from pathlib import Path
from fractions import Fraction as Q
from flint import fmpz_poly,fmpq_poly,fmpq
import numpy as np
ROOT=Path(__file__).resolve().parent
os.environ['LOCAL2_PRECISION']='16'
import local2_arithmetic as L
load=lambda s:json.loads((ROOT/s).read_text())
checks=0;negatives=0
def check(ok,label):
 global checks
 if not ok:raise ArithmeticError(label)
 checks+=1
def reject(ok,label):
 global negatives
 if ok:raise ArithmeticError('negative accepted: '+label)
 negatives+=1
def rank(vs):
 piv={}
 for v in vs:
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=v;break
   v^=piv[k]
 return len(piv)
def lin(m,cols):
 z=0
 for i,c in enumerate(cols):
  if m>>i&1:z^=c
 return z
def kernel(rows,width):
 a=list(rows);r=0;p=[]
 for j in range(width):
  k=next((k for k in range(r,len(a))if(a[k]>>j)&1),None)
  if k is None:continue
  a[k],a[r]=a[r],a[k]
  for k in range(len(a)):
   if k!=r and(a[k]>>j)&1:a[k]^=a[r]
  p.append(j);r+=1
 return[(1<<j)^sum(((a[i]>>j)&1)<<c for i,c in enumerate(p))for j in range(width)if j not in p]
def determinant(a):
 a=[r[:]for r in a];prev=1;sgn=1
 for k in range(len(a)-1):
  if not a[k][k]:
   j=next((j for j in range(k+1,len(a))if a[j][k]),None)
   if j is None:return 0
   a[j],a[k]=a[k],a[j];sgn=-sgn
  pp=a[k][k]
  for i in range(k+1,len(a)):
   v=a[i][k]
   for j in range(k+1,len(a)):
    z=a[i][j]*pp-v*a[k][j]
    if z%prev:raise ArithmeticError('inexact Bareiss')
    a[i][j]=z//prev
   a[i][k]=0
  prev=pp
 return sgn*a[-1][-1]
def rowminor(cols,width):
 selected=[];vs=[]
 for j in range(width):
  row=sum(((c>>j)&1)<<i for i,c in enumerate(cols))
  if rank(vs+[row])>len(vs):selected.append(j);vs.append(row)
  if len(selected)==len(cols):break
 return selected,[[(cols[i]>>j)&1 for i in range(len(cols))]for j in selected]
def solve(cols,v):
 piv={}
 for i,c in enumerate(cols):
  m=1<<i
  while c:
   k=c.bit_length()-1
   if k not in piv:piv[k]=(c,m);break
   w,n=piv[k];c^=w;m^=n
 m=0
 while v:
  k=v.bit_length()-1
  if k not in piv:return None
  w,n=piv[k];v^=w;m^=n
 return m
def vp(q):
 q=Q(str(q))
 if not q:return 10**9
 return((abs(q.numerator)&-abs(q.numerator)).bit_length()-1)-((q.denominator&-q.denominator).bit_length()-1)
# Quadratic coefficient field: a^2+a+1=0. Polynomials are pairs in Q[x].
def fq(cs):return fmpq_poly([fmpq(str(v))for v in cs])
def pol(data):return tuple(fq([v[k]for v in data])for k in[0,1])
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def scale(a,c):return(a[0]*c,a[1]*c)
def power(a,n):
 z=(fmpq_poly([1]),fmpq_poly([]))
 for _ in range(n):z=mul(z,a)
 return z
def minvp(a):return min((vp(v)for q in a for v in q.coeffs()),default=10**9)
def congruent(a,b,n,label):check(minvp(sub(a,b))>=n,label)

C=load('parents/global_cover.json');D=load('parents/local2.json');T=load('torsion_frame_P512.json')
check(T['precision']==512 and T['endpoint_absolute_precision_bits']>=128
 and len(T['factor18'])==19 and T['factor18'][-1]==['1','0']
 and len(T['torsion0']['factor12'])==13 and T['torsion0']['factor12'][-1]==['1','0']
 and len(T['torsion0']['factor24'])==25 and T['torsion0']['factor24'][-1]==['1','0']
 and len(T['initial']['u'])==36 and T['initial']['u'][-1]==['1','0']
 and all(len(s['new_u'])==s['new_degree']+1 and s['new_u'][-1]==['1','0'] and len(s['new_v'])<=s['new_degree'] for s in T['stages']),
 'precision, factor degrees, exact monic and remainder conventions')
FP=fmpz_poly(L.F);P=T['precision'];MOD=1<<P;ONE=[1]+[0]*35
def imul(a,b):
 aa=fmpz_poly([int(a[i])<<(11-i//3)for i in range(36)]);bb=fmpz_poly([int(b[i])<<(11-i//3)for i in range(36)]);cc=(aa*bb)%FP;out=[]
 for i in range(36):
  z=int(cc[i])<<(i//3);check(z%(1<<22)==0,'integral maximal-basis product');out.append((z>>22)%MOD)
 return out
tau=T['tau_basis_mod2P'];check(all((a+b+c)%MOD==0 for a,b,c in zip(imul(tau,tau),tau,ONE)),'unramified quadratic root')
check(L.residue(np.array([v%65536 for v in tau],dtype=np.int64))==T['residue_root'],'root labeling in residue algebra')
e=T['torsion0']['idempotent_basis_mod2P'];check(imul(e,e)==e,'degree12 projector idempotent')
F=(fmpq_poly(L.F),fmpq_poly([]));f=pol(T['factor18']);fc=pol(T['conjugate_factor18']);q12=pol(T['torsion0']['factor12']);q24=pol(T['torsion0']['factor24'])
congruent(mul(f,fc),F,480,'unramified conjugate branch partition')
congruent(fc,(f[0]-f[1],-f[1]),480,'coefficient conjugation')
congruent(mul(q12,q24),F,480,'degree12/24 Q2 branch partition')
# Match projector traces to the claimed factors through exact Newton identities.
tr=[36]
for k in range(1,36):tr.append(-sum(L.F[36-j]*tr[k-j]for j in range(1,k))-k*L.F[36-k])
bt=[tr[i]//(1<<(i//3))for i in range(36)]
check(all(tr[i]%(1<<(i//3))==0 for i in range(36)),'integral basis traces')
check(sum(e[i]*bt[i]for i in range(36))%MOD==12,'projector trace12')
check(sum(tau[i]*bt[i]for i in range(36))%MOD==(-18)%MOD,'unramified eigenspaces both dimension18')
# The branch factors are tied to the frozen projectors, rather than merely
# being arbitrary conjugate factors of F. Trace operations preserve 512 bits.
def trace(z):return sum(z[i]*bt[i]for i in range(36))%MOD
def constpair(c,d=0):return(fq([c]),fq([d]))
def newton_check(factor,sums,label):
 deg=int(factor[0].degree());cc=[constpair(factor[0][deg-j],factor[1][deg-j])for j in range(deg+1)]
 for k in range(1,deg+1):
  rr=scale(cc[k],k)
  for j in range(1,k+1):rr=add(rr,mul(cc[k-j],sums[j-1]))
  check(minvp(rr)>=480,label+' Newton trace '+str(k))
z=[0,1]+[0]*34;s12=[];s24=[];s18=[]
for k in range(1,25):
 t=trace(z);te=trace(imul(e,z));tt=trace(imul(tau,z))
 if k<=12:s12.append(constpair(te))
 s24.append(constpair(t-te))
 if k<=18:s18.append(constpair(Q(t-tt,3),-Q(2*tt+t,3)))
 z=imul(z,[0,1]+[0]*34)
newton_check(q12,s12,'factor12');newton_check(q24,s24,'factor24');newton_check(f,s18,'factor18')
# Independent coefficient error bounds. These are balls about the frozen
# rational centers, not a second use of PARI's reported precision.
INF=10**9
def degree(a):return max(int(a[0].degree()),int(a[1].degree()))
def cv(a,i):return min(vp(a[0][i]),vp(a[1][i]))
def coefvals(a,n=None):return[cv(a,i)for i in range((degree(a)+1)if n is None else n)]
def erradd(a,b,n):return[min(a[i]if i<len(a)else INF,b[i]if i<len(b)else INF)for i in range(n)]
def errconv(a,b,n):return[min((a[j]+b[i-j]for j in range(len(a))if 0<=i-j<len(b)),default=INF)for i in range(n)]
def errmul(a,ea,b,eb,n):return erradd(erradd(errconv(ea,coefvals(b),n),errconv(coefvals(a),eb,n),n),errconv(ea,eb,n),n)
def diverr(er,divisor,ed):
 # Long division by a monic polynomial. Leading coefficient is exactly 1.
 d=degree(divisor);er=er[:];eq=[INF]*max(0,len(er)-d)
 for j in range(len(er)-1,d-1,-1):
  qerr=er[j];eq[j-d]=qerr
  for k in range(d):er[j-d+k]=min(er[j-d+k],qerr+min(cv(divisor,k),ed[k]))
  er[j]=INF
 return eq,er[:d]
ef=[480-vp(math.factorial(18))]*18+[INF]
# Verify every frozen RR identity by rational polynomial arithmetic.
initial=T['initial'];u=pol(initial['u']);v=pol(initial['v']);z=(fq([Q(-3,2),1]),fmpq_poly([]));ys=[Q(s)for s in initial['y_series']]
congruent(u,mul(f,power(z,17)),200,'initial degree35 divisor')
interp=(fmpq_poly([]),fmpq_poly([]))
for j,c in enumerate(initial['interpolation_coefficients']):interp=add(interp,mul(pol([c]),power(z,j)))
congruent(v,mul(f,interp),200,'initial support on branch partition')
check(ys[0]==Q(1,262144),'exact positive P0 y value in u chart')
ft=[];eft=[]
for k in range(17):
 fc0=[]
 for fp in f:
  fc0.append(sum(Q(str(fp[j]))*math.comb(j,k)*Q(3,2)**(j-k)for j in range(k,19)))
 ft.append(constpair(*fc0));eft.append(min(ef[j]+vp(math.comb(j,k)*Q(3,2)**(j-k))for j in range(k,19)))
 fy=sum(Q(L.F[j])*math.comb(j,k)*Q(3,2)**(j-k)for j in range(k,37))
 check(sum(ys[j]*ys[k-j]for j in range(k+1))==fy,'exact Taylor square-root coefficient')
ss=[pol([c])for c in initial['interpolation_coefficients']];es=[]
check(eft[0]>cv(ft[0],0),'Taylor denominator valuation certified')
for k in range(17):
 rr=constpair(ys[k])
 for j in range(k+1):rr=sub(rr,mul(ft[j],ss[k-j]))
 ev=min(minvp(rr),min(eft[j]+cv(ss[k-j],0)for j in range(k+1)),min((min(cv(ft[j],0),eft[j])+es[k-j]for j in range(1,k+1)),default=INF))-cv(ft[0],0)
 es.append(ev)
esi=[min(es[j]+vp(math.comb(j,k)*(-Q(3,2))**(j-k))for j in range(k,17))for k in range(17)]
eu=errconv(ef,coefvals(power(z,17)),36)
eu=erradd(eu,coefvals(sub(u,mul(f,power(z,17))),36),36);eu[-1]=INF
ev=errmul(f,ef,interp,esi,35)
ev=erradd(ev,coefvals(sub(v,mul(f,interp)),35),35)
ball_stages=[{'degree':35,'u_error_min':min(eu),'v_error_min':min(ev)}]
for k in range(17):
 val=(fmpq_poly([]),fmpq_poly([]))
 vals=[]
 for q in v:
  vals.append(sum(Q(str(q[j]))*math.comb(j,k)*Q(3,2)**(j-k)for j in range(k,int(q.degree())+1)))
 check(vp(vals[0]-ys[k])>=200 and vp(vals[1])>=200,'initial P0 multiplicity condition')
rr_min=10**9
for step in T['stages']:
 uu=pol(step['new_u']);vv=pol(step['new_v']);lc=pol([step['scale']]);quo=pol(step['v_quotient'])
 err1=sub(sub(F,mul(v,v)),mul(lc,mul(u,uu)));err2=sub(sub(neg(v),vv),mul(quo,uu));rr_min=min(rr_min,minvp(err1),minvp(err2))
 check(minvp(err1)>=160,'RR norm identity');check(minvp(err2)>=160,'RR involution/remainder identity')
 check(step['new_degree']==step['old_degree']-2,'balanced even-degree RR degree count')
 nn=max(37,2*(len(ev)-1)+1);qn=mul(lc,uu)
 en=erradd([w+1 for w in errconv(coefvals(v),ev,nn)],errconv(ev,ev,nn),nn)
 er=erradd(erradd(en,errconv(eu,coefvals(qn),nn),nn),coefvals(err1,nn),nn)
 eq,_=diverr(er,u,eu);ld=degree(uu);el=eq[ld];vl=cv(lc,0)
 check(el>vl,'RR nonzero leading coefficient with certified valuation')
 euu=[min(eq[i]-vl,cv(qn,i)+el-2*vl)for i in range(ld)]+[INF]
 nv=max(len(ev)-1,degree(mul(quo,uu)),degree(vv))+1
 erv=erradd(erradd(ev,errconv(euu,coefvals(quo),nv),nv),coefvals(err2,nv),nv)
 _,evv=diverr(erv,uu,euu)
 eu,ev=euu,evv;u,v=uu,vv
 ball_stages.append({'degree':ld,'u_error_min':min(eu),'v_error_min':min(ev)})
check(min(eu)>=16,'independent endpoint coefficient ball is sufficient for unit class')
check(len(T['stages'])==9 and u[0].degree()==17,'final effective degree17')
check(minvp((fmpq_poly([]),u[1]))>=128 and minvp((fmpq_poly([]),v[1]))>=128,'endpoint descends to Q2')
end=[Q(c)for c in T['u_endpoint_rational_ascending']]
congruent(u,(fq(end),fmpq_poly([])),128,'bound endpoint rational representative')
# Compute NEW torsion squareclasses in the inherited exact local unit model.
e16=np.array([x%65536 for x in e],dtype=np.int64)
def modq(q,n):
 q=Q(q);d=q.denominator.bit_length()-1
 if q.denominator!=1<<d:raise ArithmeticError('dyadic denominator required')
 return (q.numerator%(1<<(n+d)))//(1<<d)
q12c=[modq(c[0],16)for c in T['torsion0']['factor12']];q24c=[modq(c[0],16)for c in T['torsion0']['factor24']]
a=(-L.mul(e16,L.eval_u(q24c)))%65536;b=L.mul((L.ONE-e16)%65536,L.eval_u(q12c))
check(all(int(z)%256==0 for z in a)and all(int(z)%16==0 for z in b),'torsion0 square component valuations')
unit0=(a//256+b//16)%256;check(list(map(int,unit0))==T['torsion0']['unit_basis_mod256'],'torsion0 normalized unit')
z=L.ZERO.copy()
for i,c in enumerate(end):
 c=c*(1<<(3+i//3));check(c.denominator==1,'torsion1 integral basis normalization');z[i]=int(c)%65536
prec=16
for _ in range(6):z,prec=L.divide_u(z,prec)
unit1=z%256;check(prec>=8 and list(map(int,unit1))==T['torsion1']['unit_basis_mod256'],'torsion1 removal of U^6 square')
L.MOD=256;L.PREC=8
t0=L.unit_class(unit0);t1=L.unit_class(unit1)
check(hex(t0)==T['torsion0']['character_hex']=='0x62afd2803','torsion0 squareclass')
check(hex(t1)==T['torsion1']['character_hex']=='0x30fb7e2ed8','torsion1 squareclass')
scalar=int(D['scalar_minus1_character_hex'],16);cols=[int(s,16)for s in C['full19_dyadic_character_columns_hex']]
check(rank([scalar]+cols)==20,'NEW injective complete unit-squareclass localization')
mr,mm=rowminor([scalar]+cols,38);det20=determinant(mm);check(len(mr)==20 and det20%2==1,'explicit odd unit20 minor')
G=[lin(int(s,16),cols)for s in C['old6_MW_fake_coordinate_masks_hex']];K=[lin(int(s,16),cols)for s in C['residual_global_squareclass_masks_hex']];H=[scalar]+G+K
check(rank(H)==9 and rank(H+[t0,t1])==11,'NEW transverse global Selmer fake image and entire local torsion image')
ir,im=rowminor(H+[t0,t1],38);det11=determinant(im);check(len(ir)==11 and det11%2==1,'explicit transverse11 minor')
localcols=[int(t['character_hex'],16)for t in D['selected_fake_basis']]+[scalar]
tw=[solve(localcols,c)for c in[t0,t1]];check(all(v is not None for v in tw),'torsion belongs to actual complete local Jacobian image')
oldw=[1<<j for j in range(6)]+[1<<18];kap=[int('1cdee',16),int('24809',16)];Htrue=oldw+kap
for j,c in enumerate(G):check((solve(localcols,c)&((1<<18)-1))==1<<j,'known6 genuine coordinate projection')
for j,c in enumerate(K):check((solve(localcols,c)&((1<<18)-1))==kap[j],'residual genuine coordinate projection')
check(rank(Htrue)==9,'whole genuine Selmer localization rank9')
ann=kernel(Htrue,19);check(len(ann)==rank(ann)==10 and all(not((a&v).bit_count()%2)for a in ann for v in Htrue),'ten exact local19 membership constraints')
check(rank([scalar]+G+[t0,t1])==9,'q(G) fake image dimension8 modulo scalar')
check(rank([scalar]+G+K+[t0,t1])==11,'q(G) and Selmer intersect only known7, including genuine infinity kernel')
# Source coordinate and smooth AS chart used by the mathematical proof.
R=load('parents/rank6.json');A=R['A_coefficients_ascending'];B=R['B_coefficients_ascending'];h=R['h2_coefficients_ascending'];ax=fmpz_poly(A);bx=fmpz_poly(B)
check(fmpz_poly(h)==ax*ax-fmpz_poly([0,1])*bx*bx and all(c%4==0 for c in B),'exact AS chart with 4|B')
check(A[0]==1 and(A[0]%2)==1,'smooth source chart at (X,Z)=(0,0)')
reject(rank([scalar]+cols[:-1])==20,'missing global unit cannot certify injection')
reject(rank(H+[t0,t0])==11,'one local torsion repeated')
reject(rank(H+[t0,K[0]])==11,'Selmer vector is not a transverse torsion direction')
reject(minvp(sub(u,(fq([end[0]+1]+end[1:]),fmpq_poly([]))))>=128,'changed endpoint divisor')
reject(L.unit_class((unit1+L.ONE)%256)==t1,'changed normalized torsion unit')
reject(det20%2==0,'singular unit frame')
reject(rank(oldw+kap[:1])==9,'one residual class omitted')
out={'scope':'fixed signed18 C2 only','internal_status':'EXACT_PASS','checks':checks,'negative_controls':negatives,'unit_localization_rank':20,'unit_minor_rows':mr,'unit20_integer_determinant':det20,'transverse_rank_including_scalar':11,'transverse_minor_rows':ir,'transverse11_integer_determinant':det11,'torsion_characters_hex':list(map(hex,[t0,t1,t0^t1])),'torsion_local_word_masks_with_scalar_hex':list(map(hex,tw)),'true_global_selmer_localization_dimension':9,'true_local_dimension':19,'true_Selmer_localization_injective':True,'H2_true_columns_hex':list(map(hex,Htrue)),'H2_annihilator_rows_hex':list(map(hex,ann)),'local_2primary_torsion_exponent_by_report':2,'whole_MW_global_local_2power_divisibility_by_report':True,'source_global_2power_divisor_exponent_lower':'2*v2(A_source)-2 >= 2','q_known7_intersection_Selmer_exact_known7':True,'RR_independent_identity_v2_lower':rr_min,'independent_factor18_coefficient_error_bits':min(ef),'independent_RR_coefficient_balls':ball_stages,'independent_endpoint_coefficient_error_bits':min(eu),'MW_rank_interval':[7,9],'CT_entry_computed':False,'whole_MW_p163_U_constructed':False,'new_source_exclusions':0,'independent_mathematical_audit':'PENDING_NOT_RUN'}
out.update({'unit20_columns_hex':list(map(hex,[scalar]+cols)),'unit20_minor_matrix':mm,'Hfake_with_scalar_columns_hex':list(map(hex,H)),'transverse11_columns_hex':list(map(hex,H+[t0,t1])),'transverse11_minor_matrix':im})
if '--build'in sys.argv:(ROOT/'dyadic_transversality_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
else:check(load('dyadic_transversality_certificate.json')==out,'frozen NEW certificate reproduced')
print(json.dumps({k:v for k,v in out.items()if not isinstance(v,list)}))
