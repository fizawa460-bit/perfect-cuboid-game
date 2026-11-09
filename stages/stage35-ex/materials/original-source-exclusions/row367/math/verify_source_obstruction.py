"""Exact frozen-certificate checks for row367. General proofs are in REPORT.md.
No PARI. The formal logs use independent inverse-square-root series and
companion-matrix traces, rather than the generating AS/Newton-sum routines.
"""
import os,json,sys,math
from pathlib import Path
from fractions import Fraction as Q
from flint import fmpz_poly,fmpq_poly,fmpq,fmpz_mat
import numpy as np
ROOT=Path(__file__).resolve().parent
os.environ['LOCAL2_PRECISION']='16'
import local2_arithmetic as L
from independent_formal_check import check_point,fast_inverse_y
checks=0;negatives=0
def ck(ok,label):
 global checks
 if not ok:raise ArithmeticError(label)
 checks+=1
def reject(ok,label):
 global negatives
 if ok:raise ArithmeticError('negative accepted: '+label)
 negatives+=1
def load(s):return json.loads((ROOT/s).read_text())
def v2(n):return (abs(n)&-abs(n)).bit_length()-1 if n else 10**9
def vp(z):
 q=Q(str(z));return v2(q.numerator)-v2(q.denominator)if q else 10**9
def poly(cs):return fmpq_poly([fmpq(str(x))for x in cs])
def minvp(p):return min(map(vp,p.coeffs()),default=10**9)
def plift(z,n):
 z=Q(str(z));d=v2(z.denominator);m=1<<(n+d)
 return Q(z.numerator*pow(z.denominator>>d,-1,m)%m,1<<d)
def rank(vs):
 p={}
 for v in vs:
  while v:
   k=v.bit_length()-1
   if k not in p:p[k]=v;break
   v^=p[k]
 return len(p)
def kernel(vs,width):
 rows=vs[:];r=0;ps=[]
 for j in range(width):
  k=next((i for i in range(r,len(rows))if rows[i]>>j&1),None)
  if k is None:continue
  rows[r],rows[k]=rows[k],rows[r]
  for i in range(len(rows)):
   if i!=r and rows[i]>>j&1:rows[i]^=rows[r]
  ps.append(j);r+=1
 return[(1<<j)^sum(((rows[i]>>j)&1)<<k for i,k in enumerate(ps))for j in range(width)if j not in ps]
def minor(cols,width):
 rs=[];rr=[]
 for j in range(width):
  r=sum(((c>>j)&1)<<i for i,c in enumerate(cols))
  if rank(rr+[r])>len(rr):rs.append(j);rr.append(r)
  if len(rr)==len(cols):break
 mat=[[(c>>j)&1 for c in cols]for j in rs]
 return rs,mat,int(fmpz_mat(mat).det())
D=load('parents/rank6.json');Q4=load('q4_P32.json');Q8=load('q8_P256.json');R=load('sixteenth_P256.json');parent=load('parents/dyadic_transversality_certificate.json')
A=D['A_coefficients_ascending'];B=D['B_coefficients_ascending'];h=D['h2_coefficients_ascending'];HP=poly(h)
ck(HP==poly(A)**2-poly([0,1])*poly(B)**2 and all(x%4==0 for x in B),'same source curve and smooth AS chart')
ck(all(A[i]%2==int(i in[0,2,16,18])for i in range(19)),'A mod2=(X+1)^18, derivative even')
formal=[]
for q in[Q4,Q8]:
 info=check_point(q);formal.append(info);ck(info['actual_17_logs_recomputed']and info['tail_v2_lower']>=q['N'],'actual formal division and analytic tail')
 ck(q['a_coefficients'][-1]==1 and all(x%q['scale']==0 for x in q['a_coefficients'][:-1]),'formal divisor integral and monic')
ck(Q8['N']==256 and Q8['initial_bits_hex']=='0x808b','full 8-division frozen input')
c=fast_inverse_y(40,32)
Tcols=[sum((c[i-j-1]%2)<<j for j in range(i))for i in range(1,18)]
Mcols=[sum((((c[i-j-1]if i>j else 0)+(c[2*i-j-1]if 2*i>j else 0))%2)<<j for j in range(17))for i in range(1,18)]
ck(rank(Tcols)==rank(Mcols)==17,'Hensel Jacobian and mod2 root matrix both full rank')
def comb(word,cols):
 r=0
 for i,c0 in enumerate(cols):
  if word>>i&1:r^=c0
 return r
ck(comb(0x808b,Mcols)==1,'uniform odd tangent initial root')
fp=fmpz_poly(L.F)
def rmul(a,b,n):
 aa=fmpz_poly([int(a[i])<<(11-i//3)for i in range(36)]);bb=fmpz_poly([int(b[i])<<(11-i//3)for i in range(36)]);cc=aa*bb%fp;out=[]
 for i in range(36):
  z=int(cc[i])<<(i//3);ck(z%(1<<22)==0,'integral maximal-order product');out.append((z>>22)%(1<<n))
 return out
ONE=[1]+[0]*35;U=[0,1]+[0]*34;TH=[-3,2]+[0]*34
def rpower(a,n,prec):
 r=ONE
 while n:
  if n&1:r=rmul(r,a,prec)
  a=rmul(a,a,prec);n>>=1
 return r
def evalX(cs,n):
 p=fmpz_poly([]);theta=fmpz_poly([-3,2])
 for z in cs[::-1]:p=(p*theta+int(z))%fp
 return[(int(p[i])<<(i//3))%(1<<n)for i in range(36)]
# Inverse theta is exact, since h(0)=1. This also avoids Newton inversion.
thinv=evalX([-int(x)for x in h[1:]],260)
ck(rmul(TH,thinv,260)==ONE,'exact theta inverse')
P=R['ring_precision'];mod=1<<P
alpha8=rmul(evalX(Q8['a_coefficients'],P),rpower(thinv,17,P),P)
sqrt=R['sqrt_basis_mod2P'];sq=rmul(sqrt,sqrt,P)
ck(all((sq[i]+alpha8[i])%mod==0 for i in range(36)),'norm-compatible square root of -alpha8')
tau=load('parents/torsion_frame_P512.json')['tau_basis_mod2P']
tr=[36]
for k in range(1,36):tr.append(-sum(L.F[36-j]*tr[k-j]for j in range(1,k))-k*L.F[36-k])
bt=[tr[j]//(1<<(j//3))for j in range(36)]
ck(sum(tau[i]*bt[i]for i in range(36))%(1<<32)==(-18)%(1<<32),'unramified-root trace parity')
ck(bt[1]%2==bt[2]%2==0,'nilpotent u,u2 have even trace')
ck([x%8 for x in alpha8]==[3,4]+[0]*34,'8-division alpha modulo8')
u2=rmul(U,U,8);w=[(tau[i]+U[i]+u2[i])%8 for i in range(36)];z0=[(ONE[i]+2*w[i])%8 for i in range(36)];sq0=rmul(z0,z0,8)
ck(all((sq0[i]+alpha8[i])%8==0 for i in range(36)),'explicit square witness and full-kernel sign')
ck(sum(w[i]*bt[i]for i in range(36))%2==0,'square-root norm is 1 mod4')
for c0 in[0,1]:
 for d0 in[0,1]:
  ww=[(c0*tau[i]+d0*(U[i]+u2[i]))%8 for i in range(36)];ww2=rmul(ww,ww,8)
  ck(all((ww2[i]+ww[i]-c0*ONE[i]-d0*U[i])%2==0 for i in range(36)),'all scalar/nilpotent square-root witnesses')
  ck(sum(ww[i]*bt[i]for i in range(36))%2==0,'uniform true norm sign on entire even-coefficient chart')
a8=poly(Q8['a_coefficients']);uD=poly(R['uD']);vD=poly(R['vD']);F=poly(R['F16']);br=poly(R['b']);ar=poly(R['a']);rp=poly(R['r_theta'])
ck(uD==a8*poly([0]*17+[1]),'degree34 effective divisor E8+17P0')
ck(minvp((vD*vD-HP)%uD)>=256,'positive divisor branch norm')
ck(minvp((vD-poly(A))%uD)>=3,'positive branch Y=A mod8')
ck(minvp((rp*rp+uD)%HP)>=150,'RR square-root label in branch field')
def normmod4(v,u):
 n=int(u.degree());cols=[(v*poly([0]*j+[1]))%u for j in range(n)]
 mat=[[int(cols[j][i])%4 for j in range(n)]for i in range(n)]
 return int(fmpz_mat(mat).det())%4
ck(normmod4(vD,a8)==1,'true pair norm r8=1 mod4, not merely fake zero')
cols=[]
for j in range(18):
 pj=(rp*poly([0]*j+[1]))%HP;rem=pj%uD;cols.append([pj[35]]+[rem[k]for k in range(34)])
for j in range(17):
 rem=(-vD*poly([0]*j+[1]))%uD;cols.append([0]+[rem[k]for k in range(34)])
unknowns=list(range(17))+list(range(18,35));den=R['matrix_denominator_power'];fac=1<<den;E=R['matrix_entry_error_bits']
rows=[[int(plift(cols[j][i],E)*fac)for j in unknowns]for i in range(35)];rhs=[int(plift(-cols[17][i],E)*fac)for i in range(35)]
ck(rows==R['matrix_all_scaled_integer_rows']and rhs==R['matrix_all_scaled_integer_rhs'],'all RR linear equations independently assembled')
ids=[i for i in range(35)if i!=R['chosen_omitted_row']];mi=[rows[i]for i in ids];Vi=R['inverse_scaled_integer_matrix'];si=R['inverse_dyadic_shift'];level=den+si+64
for i in range(34):
 for j in range(34):ck((sum(mi[i][k]*Vi[k][j]for k in range(34))-(1<<(den+si)if i==j else 0))%(1<<level)==0,'dyadic inverse witness')
ds=int(R['solution_exact_common_denominator']);nums=list(map(int,R['solution_exact_numerators']))
for i in ids:ck(sum(rows[i][j]*nums[j]for j in range(34))==rhs[i]*ds,'exact selected RR solve with integers')
xexact=[Q(n,ds)for n in nums];xmin=min(map(vp,xexact));invmin=-si
err=E+invmin+min(0,xmin)
ck(E==206 and invmin==-37 and xmin==-22 and err==147,'independent matrix perturbation bound')
xfrozen=[Q(str(F[j]))for j in range(17)]+[Q(str(br[j]))for j in range(17)]
for x,y in zip(xexact,xfrozen):ck(vp(x-y)>=err,'true RR solution coefficient ball')
ck(min(vp(Q(sum(rows[i][j]*nums[j]for j in range(34))-rhs[i]*ds,ds*fac))for i in range(35))>=184,'remaining exact-kernel compatibility residual')
ck(F.degree()==17 and F[17]==1 and all(vp(z)>=0 for z in F.coeffs()),'monic integral effective half divisor')
ck(int(F[0])%2==1 and all(int(x)%2==0 for x in uD.coeffs()[:-1]),'half divisor is disjoint from E8 and P0 modulo2')
ck(minvp((ar-rp*F)%HP)>=80 and minvp((ar-br*vD)%uD)>=80,'RR support constraints')
ck(minvp(ar*ar-HP*br*br+uD*F*F)>=64,'full RR norm identity residual')
s=poly(R['bezout_F']);t=poly(R['bezout_b'])
ck(minvp(s*F+t*br-1)>=80 and min(minvp(s),minvp(t))+err>0,'stable coprimality, genuine doubled divisor')
# Independent unit normalization: exact inverse of t=u^3/2 as rational polynomials.
fu=poly(L.F);iu=-poly(L.F[1:])/L.F[0];ti=(2*iu*iu*iu)%fu
tin=[]
for j in range(36):
 q=Q(str(ti[j]))*(1<<(j//3));ck(vp(q)>=0,'integral inverse t');tin.append(int(plift(q,45)))
fvals=evalX([int(z)for z in F.coeffs()],64)
ck(all(x%(1<<19)==0 for x in fvals),'half branch value divisible by 2^19')
nf=[x>>19 for x in fvals];un=rmul(nf,rpower(tin,20,45),45)
ck([x%256 for x in un]==R['normalized_half_unit_mod256'],'unit=2F(theta)/u^60 independently reproduced')
L.MOD=256;L.PREC=8
actual=L.unit_class(np.array([x%256 for x in un],dtype=np.int64));theta17=L.unit_class(np.array([x%256 for x in rpower(TH,17,8)],dtype=np.int64))
ck(theta17==0,'P0 denominator theta^17 is square')
ck(hex(actual)==R['half_fake_character_hex']=='0x3101d39ed8','actual16-half local character')
H=[int(x,16)for x in parent['transverse11_columns_hex']]
ck(rank(H)==11 and rank(H+[actual])==12,'source normalized16-half is OUTSIDE whole Selmer plus full torsion')
rs,matrix,det=minor(H+[actual],38);ck(det%2==1,'explicit source-obstruction12 minor')
ann=kernel(H,38);rho=next(r for r in ann if(r&actual).bit_count()%2)
ck(all((rho&c0).bit_count()%2==0 for c0 in H)and(rho&actual).bit_count()%2==1,'dual scalar-safe separation witness')
# The uniform source bridge is proved in REPORT.md; check its exact constants.
ck(all(m*(k-1)-v2(k)>=3 for m in[4,6,8,10]for k in range(2,100)),'normalized higher terms begin in8Z2')
ck(all((s0*s0-1)%8==0 for s0 in range(1,32,2)),'all odd-square residue classes')
reject(normmod4(-vD,a8)==1,'wrong true norm sign cannot be ignored')
reject(rank(H+[H[0]])==12,'Selmer vector cannot certify exclusion')
reject(all((rho&c0).bit_count()%2==0 for c0 in H+[actual]),'obstruction class cannot enter accepted upper space')
reject(err-19<8,'insufficient normalized-unit precision')
reject((3-1)%8==0,'nonsquare odd unit cannot use source bridge')
reject(rank(H[:-1])==11,'one torsion generator missing')
out={'scope':'fixed signed +/-18 C2 and original square X, v2X>=4 ONLY','internal_status':'EXACT_PROOF_PASS','new_independent_audit':'PENDING_NOT_RUN','parent_latest_audit':'ROW366_PASS','checks':checks,'negative_controls':negatives,'formal_logs':formal,'beta4_true19_hex':'0x0','beta8_true19_hex':'0x0','local_source_division_exponent':'v2(X), all v2(X)>=4','RR_working_bits':252,'RR_matrix_entry_error_bits':206,'RR_inverse_minval':-37,'RR_solution_minval':-22,'RR_true_coefficient_error_bits':147,'RR_norm_identity_residual_at_least':64,'half_normalization':'2F(theta)/u^60','normalized_unit_verified_bits':45,'actual16_half_fake_character_hex':hex(actual),'Hfake_plus_scalar_plus_full_torsion_rank':11,'augmented_rank':12,'source_minor_rows':rs,'source_minor_matrix':matrix,'source_minor_integer_determinant':det,'scalar_safe_separator_hex':hex(rho),'source_original_signed18_exclusion':'PROVED_INTERNAL_AUDIT_PENDING_BY_REPORT','new_absolute_indices_excluded_internal':[18],'new_signed_indices_excluded_internal':[-18,18],'all_LOW_closed':False,'BranchB_closed':False,'MW_rank_interval':[7,9],'CT_computed':False,'whole_MW_p163_U_constructed':False,'whole_q_X2_inclusion_proved':False,'n4_Gamma_le5_proved':False}
if '--build'in sys.argv:(ROOT/'source_obstruction_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
else:ck(load('source_obstruction_certificate.json')==out,'frozen source certificate reproduced')
print(json.dumps({k:v for k,v in out.items()if not isinstance(v,list)}))
