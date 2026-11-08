import sys,json,math,time
from pathlib import Path
from fractions import Fraction as Q
from flint import fmpz_poly,fmpq_poly,fmpq_mat,fmpz_mat,fmpq
from formal_jacobi import lift,series,v2,PARENT
import local2_arithmetic as L
import numpy as np
import argparse
ROOT=Path(__file__).resolve().parent
aparser=argparse.ArgumentParser();aparser.add_argument('--q8',type=Path,required=True);aparser.add_argument('--output-dir',type=Path,required=True);args=aparser.parse_args()
q=json.loads(args.q8.read_text());N=q['N'];start=time.monotonic();args.output_dir.mkdir(parents=True,exist_ok=True)
if N<192:raise ValueError('192+ input bits required for RR squareclass certificate')
P=N-4;MOD=1<<P;FP=fmpz_poly(L.F);ONE=[1]+[0]*35;UV=[0,1]+[0]*34;TH=[-3,2]+[0]*34
def rmul(a,b,prec=P):
 mod=1<<prec;aa=fmpz_poly([int(a[i])<<(11-i//3)for i in range(36)]);bb=fmpz_poly([int(b[i])<<(11-i//3)for i in range(36)]);cc=aa*bb%FP
 return [((int(cc[i])<<(i//3))//(1<<22))%mod for i in range(36)]
def add(a,b):return[(x+y)%MOD for x,y in zip(a,b)]
def sub(a,b):return[(x-y)%MOD for x,y in zip(a,b)]
def scale(a,n):return[(x*n)%MOD for x in a]
def power(a,n):
 r=ONE
 while n:
  if n&1:r=rmul(r,a)
  a=rmul(a,a);n>>=1
 return r
def inv1(a):
 r=ONE
 for _ in range(P.bit_length()+1):r=rmul(r,sub(scale(ONE,2),rmul(a,r)))
 if rmul(a,r)!=ONE:raise ArithmeticError('inverse')
 return r
def evalX(cs,prec=P):
 t=fmpz_poly([-3,2]);p=fmpz_poly([])
 for c in cs[::-1]:p=(p*t+int(c))%FP
 return[(int(p[i])<<(i//3))%(1<<prec)for i in range(36)]
th17=power(TH,17)
# Work two extra bits before dividing by four.
ap=evalX(q['a_coefficients'],P+2)
def rmulp(a,b):return rmul(a,b,P+2)
z=ONE
thp=TH
for _ in range(17):z=rmulp(z,TH)
inv=ONE
for _ in range((P+2).bit_length()+1):inv=rmulp(inv,[(2*ONE[i]-x)%(1<<(P+2))for i,x in enumerate(rmulp(z,inv))])
alpha=rmulp(ap,inv);la=[(-x)%(1<<(P+2))for x in alpha]
if any((la[i]-ONE[i])%4 for i in range(36)):raise ArithmeticError('lambda-alpha not 1mod4')
gg=[((la[i]-ONE[i])//4)%MOD for i in range(36)]
tau=json.loads((ROOT/'parents/torsion_frame_P512.json').read_text())['tau_basis_mod2P'];w=[int(x)%MOD for x in tau];w=add(w,add(UV,rmul(UV,UV)))
for _ in range(P.bit_length()+2):w=sub(w,rmul(sub(add(rmul(w,w),w),gg),inv1(add(ONE,scale(w,2)))))
if sub(add(rmul(w,w),w),gg)!=[0]*36:raise ArithmeticError('AS square root')
sqrt=add(ONE,scale(w,2));r=rmul(th17,sqrt)
rr=[]
for k in range(36):rr.append(sum(Q(r[j]*math.comb(j,k)*3**(j-k),1<<(j+j//3))for j in range(k,36)))
h=json.loads((PARENT/'parents/rank6.json').read_text())['h2_coefficients_ascending'];HP=fmpq_poly(h);rp=fmpq_poly([fmpq(str(x))for x in rr]);ap=fmpq_poly(q['a_coefficients']);ud=fmpq_poly([0]*17+[int(x)for x in q['a_coefficients']])
def remainder(poly,div):return poly%div
udz=fmpz_poly([int(x)for x in ud.coeffs()]);mn=1<<N
AA=json.loads((PARENT/'parents/rank6.json').read_text())['A_coefficients_ascending'];BB=json.loads((PARENT/'parents/rank6.json').read_text())['B_coefficients_ascending']
def red(poly):return fmpz_poly([int(z)%mn for z in (poly%udz).coeffs()])
def pmul(a,b):return red(a*b)
apoly=red(fmpz_poly(AA));bp=red(fmpz_poly([z//2 for z in BB]));cc=red(fmpz_poly([0,1])*bp*bp)
def pinv(a):
 inv=[1]
 for k in range(1,34):inv.append(-sum(int(a[j])*inv[k-j]for j in range(1,k+1))%2)
 r=fmpz_poly(inv)
 for _ in range(N.bit_length()+3):r=pmul(r,red(2-pmul(a,r)))
 if pmul(a,r)!=fmpz_poly([1]):raise ArithmeticError('quotient-ring inverse')
 return r
zz=fmpz_poly([])
for _ in range(N.bit_length()+2):zz=red(zz-pmul(red(zz*zz+apoly*zz+cc),pinv(red(apoly+2*zz))))
if red(zz*zz+apoly*zz+cc)!=fmpz_poly([]):raise ArithmeticError('positive divisor branch')
vd=fmpq_poly(red(apoly+2*zz))
cols=[]
for j in range(18):
 pj=(rp*fmpq_poly([0]*j+[1]))%HP
 rem=pj%ud;cols.append([pj[35]]+[rem[i]for i in range(34)])
for j in range(17):
 rem=(-vd*fmpq_poly([0]*j+[1]))%ud;cols.append([0]+[rem[i]for i in range(34)])
rows=[[cols[j][i]for j in list(range(17))+list(range(18,35))]for i in range(35)];rhs=[-cols[17][i]for i in range(35)]
E=N-50
def padiclift(q,prec):
 q=Q(str(q));dd=v2(q.denominator)
 return Q((q.numerator*pow(q.denominator>>dd,-1,1<<(prec+dd)))%(1<<(prec+dd)),1<<dd)
rows=[[padiclift(x,E)for x in row]for row in rows];rhs=[padiclift(x,E)for x in rhs]
# All entries have dyadic denominators. Scale all equations uniformly.
den=max((Q(str(x)).denominator.bit_length()-1 for row in rows for x in row),default=0);fac=1<<den
ints=[[int(Q(str(x))*fac)for x in row]for row in rows];rhsint=[int(Q(str(x))*fac)for x in rhs]
best=None
for omitted in range(35):
 mat=fmpz_mat([row for i,row in enumerate(ints)if i!=omitted]);det=int(mat.det())
 if det and(best is None or v2(abs(det))<best[0]):best=(v2(abs(det)),omitted,mat)
valdet,omitted,mat=best;ids=[i for i in range(35)if i!=omitted]
print(json.dumps({'N':N,'ringP':P,'denominator_bits':den,'det_integer_v2':valdet,'omitted':omitted,'seconds':time.monotonic()-start}),flush=True)
sol=fmpq_mat(mat).solve(fmpq_mat([[rhsint[i]]for i in ids]));solq=[Q(str(sol[i,0]))for i in range(34)]
exact_sol=solq[:]
def vq(q):
 q=Q(str(q));return 10**9 if not q else v2(abs(q.numerator))-v2(q.denominator)
res=[sum(Q(str(rows[i][j]))*solq[j]for j in range(34))-Q(str(rhs[i]))for i in range(35)]
mi=fmpq_mat(mat).inv()*fac;mininv=min(vq(mi[i,j])for i in range(34)for j in range(34));minsol=min(map(vq,solq));solerr=E+mininv+min(0,minsol)
denSol=math.lcm(*(v.denominator for v in exact_sol));numSol=[int(v*denSol)for v in exact_sol]
inverse_shift=max(0,-mininv);inverse_int=[[int(padiclift(mi[i,j],128)*(1<<inverse_shift))for j in range(34)]for i in range(34)]
print(json.dumps({'matrix_entry_error':E,'inverse_minval':mininv,'solution_minval':minsol,'certified_solution_error':solerr,'omitted_residual_v2':min(map(vq,res))}),flush=True)
if E+mininv<1 or solerr<16:raise ArithmeticError('insufficient solve precision')
solq=[padiclift(z,solerr)for z in solq]
ff=fmpq_poly([fmpq(str(z))for z in solq[:17]]+[1]);bb=fmpq_poly([fmpq(str(z))for z in solq[17:]]);aa=(rp*ff)%HP;identity=aa*aa-HP*bb*bb+ud*ff*ff
print(json.dumps({'residual_v2':min(map(vq,res)),'norm_identity_v2':min(map(vq,identity.coeffs())),'min_f_v2':min(map(vq,ff.coeffs())),'min_b_v2':min(map(vq,bb.coeffs())),'seconds':time.monotonic()-start}),flush=True)
# Convert the prospective half's numerator at theta to an integral unit,
# allowing a rational scalar power of 2 and a square power of u.
fx=fmpq_poly([])
for z in ff.coeffs()[::-1]:fx=(fx*fmpq_poly([-3,2])+z)%fmpq_poly(L.F)
raw=[Q(str(fx[i]))/(1<<0) for i in range(36)]
gcd,bezF,bezb=ff.xgcd(bb)
if gcd!=fmpq_poly([1]):raise ArithmeticError('RR support gcd')
inter={'N':N,'ring_precision':P,'r_theta':[str(x)for x in rr],'sqrt_basis_mod2P':sqrt,'uD':[str(x)for x in ud.coeffs()],'vD':[str(x)for x in vd.coeffs()],'F16':[str(x)for x in ff.coeffs()],'b':[str(x)for x in bb.coeffs()],'a':[str(x)for x in aa.coeffs()],'matrix_denominator_power':den,'chosen_omitted_row':omitted,'matrix_determinant_v2':valdet,'matrix_entry_error_bits':E,'inverse_minval':mininv,'solution_minval':minsol,'solution_error_bits':solerr,'linear_residual_v2':min(map(vq,res)),'norm_identity_v2':min(map(vq,identity.coeffs())), 'matrix_all_scaled_integer_rows':ints,'matrix_all_scaled_integer_rhs':rhsint,'solution_exact_common_denominator':str(denSol),'solution_exact_numerators':list(map(str,numSol)),'inverse_dyadic_shift':inverse_shift,'inverse_scaled_integer_matrix':inverse_int,'bezout_F':[str(padiclift(z,128))for z in bezF.coeffs()],'bezout_b':[str(padiclift(z,128))for z in bezb.coeffs()]}
(args.output_dir/('sixteenth_intermediate_P'+str(N)+'.json')).write_text(json.dumps(inter))
def divideU(a,prec):
 m=1<<prec;newm=m//2
 if prec<2:raise ArithmeticError('uniformizer precision exhausted')
 aa=[int(c)%m for c in a]
 if any(aa[3*k]&1 for k in range(12)):raise ArithmeticError('not uniformly u-divisible')
 final=[-L.F[k]*(1<<(k//3))//(1<<11)for k in range(36)]
 b35=(aa[0]//2)*pow((final[0]//2)%newm,-1,newm)%newm;b=[]
 for k in range(1,36):
  v=(aa[k]-final[k]*b35)%m
  if k%3==0:
   if v%2:raise ArithmeticError('uniformizer division parity')
   v//=2
  b.append(v%newm)
 return b+[b35],prec-1
needed=max(0,max(-vq(z)for z in raw));ss=needed+(needed%2)
W=64;wm=1<<W
unit=[int(z*(1<<(ss+i//3)))%wm for i,z in enumerate(raw)]
def residue(a):return sum((int(a[3*k])&1)<<k for k in range(12))
tt=[0]*36;tt[3]=1;ti=list(map(int,L.lift(L.r_inv(residue(tt)))))
for _ in range(W.bit_length()+3):ti=rmul(ti,[(2*ONE[i]-v)%wm for i,v in enumerate(rmul(tt,ti,W))],W)
if rmul(tt,ti,W)!=ONE:raise ArithmeticError('t inverse')
def pwr(a,n,prec):
 z=ONE
 for _ in range(n):z=rmul(z,a,prec)
 return z
e12=json.loads((ROOT/'parents/torsion_frame_P512.json').read_text())['torsion0']['idempotent_basis_mod2P'];ee=[[v%wm for v in e12],[(ONE[i]-e12[i])%wm for i in range(36)]];parts=[];vals=[];precs=[]
for e in ee:
 z=rmul(e,unit,W);vv=min(v2(x)for x in z)
 z=[x>>vv for x in z];prec=W-vv;z=rmul(z,pwr(ti,vv,prec),prec);rrr=0
 while not residue(z):z,prec=divideU(z,prec);rrr+=1
 if rrr>2:raise ArithmeticError('residual uniformizer valuation')
 parts.append(z);vals.append(3*vv+rrr);precs.append(prec)
if vals[0]%2!=vals[1]%2:raise ArithmeticError('component parity mismatch')
extra=vals[0]%2
if extra:
 parts=[rmul(z,ti,p)for z,p in zip(parts,precs)];ss+=1;vals=[v+3 for v in vals]
prec=min(precs)
unit=[sum(z[i]for z in parts)%256 for i in range(36)]
removed=vals
if prec<8:raise ArithmeticError('not enough class precision')
L.MOD=256;L.PREC=8;ch=L.unit_class(np.array([z%256 for z in unit],dtype=np.int64));L.MOD=65536;L.PREC=16
print(json.dumps({'half_fake_character_hex':hex(ch),'scalar2_power':ss,'u_removed':removed,'class_precision':prec,'seconds':time.monotonic()-start}),flush=True)
out=dict(inter,half_fake_character_hex=hex(ch),normalized_half_unit_mod256=[z%256 for z in unit],scalar2_power=ss,u_removed=removed,seconds=time.monotonic()-start)
(args.output_dir/('sixteenth_P'+str(N)+'.json')).write_text(json.dumps(out,indent=2))
