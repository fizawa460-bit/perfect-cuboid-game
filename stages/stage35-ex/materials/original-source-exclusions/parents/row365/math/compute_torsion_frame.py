import os,sys,json,time,math,argparse
from pathlib import Path
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT));os.environ['LOCAL2_PRECISION']='16'
import local2_arithmetic as L
from cypari2 import Pari
from flint import fmpz_poly
ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=256);ap.add_argument('--root-index',type=int,default=0);ap.add_argument('--output-dir',type=Path,required=True);args=ap.parse_args()
P=args.precision;start=time.monotonic();p=Pari();p.allocatemem(1073741824)
x=p('x');a=p('a');unit=1+p('O(2^'+str(P)+')');F=p.Polrev(L.F,x);U=p.Mod(x,F)
roots=[i for i in range(1<<12)if(L.r_mul(i,i)^i^1)==0]
r=roots[args.root_index]
MOD=1<<P;FP=fmpz_poly(L.F);ONE=[1]+[0]*35;UV=[0,1]+[0]*34
def rmul(a,b):
 aa=fmpz_poly([int(a[i])<<(11-i//3)for i in range(36)]);bb=fmpz_poly([int(b[i])<<(11-i//3)for i in range(36)])
 cc=(aa*bb)%FP;out=[]
 for i in range(36):
  z=int(cc[i])<< (i//3)
  if z%(1<<22):raise ArithmeticError('ring integral product')
  out.append((z>>22)%MOD)
 return out
def rsub(a,b):return[(x-y)%MOD for x,y in zip(a,b)]
def radd(a,b):return[(x+y)%MOD for x,y in zip(a,b)]
def rscale(a,n):return[(x*n)%MOD for x in a]
def rinv1(a):
 b=ONE[:]
 for _ in range(P.bit_length()+1):b=rmul(b,rsub(rscale(ONE,2),rmul(a,b)))
 if rmul(a,b)!=ONE:raise ArithmeticError('unit inverse')
 return b
tau=[int(i%3==0 and(r>>(i//3))&1)for i in range(36)]
def minv(poly):
 if poly==0:return P
 return min(v2(poly.polcoef(i))for i in range(max(0,int(poly.poldegree()))+1))
def v2(c):
 v=p.valuation(c,2)
 return P if v.type()=='t_INFINITY'else int(v)
print(json.dumps({'stage':'seed','roots':roots,'selected':r,'precision':P}),flush=True)
for i in range(P.bit_length()+3):tau=rsub(tau,rmul(radd(radd(rmul(tau,tau),tau),ONE),rinv1(radd(rscale(tau,2),ONE))))
if any(radd(radd(rmul(tau,tau),tau),ONE)):raise ArithmeticError('tau root')
terr=P;print(json.dumps({'stage':'unram_root','equation_v2':terr,'seconds':time.monotonic()-start}),flush=True)
# Trace of a polynomial representative, using Newton sums of exact F.
tr=[36]
for k in range(1,36):tr.append(-sum(L.F[36-j]*tr[k-j]for j in range(1,k))-k*L.F[36-k])
bt=[]
for i in range(36):
 if tr[i]%(1<<(i//3)):raise ArithmeticError('integral trace')
 bt.append(tr[i]//(1<<(i//3)))
def trace(z):return (sum(int(z[i])*bt[i]for i in range(36))%MOD)*unit
def pack(c):
 q=p.lift(c);return[str(q.polcoef(0).lift()),str(q.polcoef(1).lift())]
def packpoly(q):return[pack(q.polcoef(i))for i in range(max(0,int(q.poldegree()))+1)]
def charpoly(ss,d):
 cc=[1]
 for k in range(1,d+1):cc.append(-sum(cc[k-j]*ss[j-1]for j in range(1,k+1))/k)
 return p.Polrev(cc[::-1],x)
g4,g8=L.FACTORS;eb=L.pgf_mul(g8,L.pgf_inv(L.pgf_mod(g8,g4),g4),L.R);eid=[int(i%3==0 and(eb>>(i//3))&1)for i in range(36)]
for _ in range(P.bit_length()+3):eid=rsub(rscale(rmul(eid,eid),3),rscale(rmul(rmul(eid,eid),eid),2))
if rmul(eid,eid)!=eid:raise ArithmeticError('idempotent')
ei2=rsub(ONE,eid);tr12=[];tr24=[];zp=UV
for k in range(1,25):
 if k<=12:tr12.append(trace(rmul(eid,zp)))
 tr24.append(trace(rmul(ei2,zp)));zp=rmul(zp,UV)
q12=charpoly(tr12,12);q24=charpoly(tr24,24)
qfq=[[int(q.polcoef(i).lift())%65536 for i in range(int(q.poldegree())+1)]for q in[q12,q24]]
import numpy as np
ee=np.array([v%65536 for v in eid],dtype=np.int64)
aa0=(-L.mul(ee,L.eval_u(qfq[1])))%65536;bb0=L.mul((L.ONE-ee)%65536,L.eval_u(qfq[0]))
if any(int(v)%256 for v in aa0)or any(int(v)%16 for v in bb0):raise ArithmeticError('torsion0 component valuation')
unit0=(aa0//256+bb0//16)%256;L.MOD=256;L.PREC=8;ch0=L.unit_class(unit0);L.MOD=65536;L.PREC=16
t0={'idempotent_residue_binary':eb,'idempotent_basis_mod2P':eid,'factor12':packpoly(q12),'factor24':packpoly(q24),'factor_product_v2':minv(q12*q24-F),'component_square_two_powers':[8,4],'unit_basis_mod256':list(map(int,unit0)),'character_hex':hex(ch0)}
aa=p.Mod(a,a*a+a+1);ab=-1-aa;delta=aa-ab
ts=[];z=UV
for k in range(1,19):
 ts.append((trace(rmul(tau,z))-ab*trace(z))/delta);z=rmul(z,UV)
cs=[aa*0+1]
for k in range(1,19):cs.append(-sum(cs[k-j]*ts[j-1]for j in range(1,k+1))/k)
f=p.Polrev(cs[::-1],x)
def conjugate(z):
 q=p.lift(z);return q.polcoef(0)+q.polcoef(1)*ab
fc=p.Polrev([conjugate(f.polcoef(i))for i in range(19)],x)
err=minv(f*fc-F);print(json.dumps({'stage':'factor18','product_v2':err,'seconds':time.monotonic()-start}),flush=True)
u0=p('3/2');y0=p('1/262144');ys=[y0]
for k in range(1,17):
 h=sum(L.F[j]*math.comb(j,k)*u0**(j-k)for j in range(k,37))
 ys.append((h-sum(ys[j]*ys[k-j]for j in range(1,k)))/(2*y0))
fs=[sum(f.polcoef(j)*math.comb(j,k)*u0**(j-k)for j in range(k,19))for k in range(17)]
ss=[]
for k in range(17):ss.append((ys[k]-sum(fs[j]*ss[k-j]for j in range(1,k+1)))/fs[0])
v=f*sum(ss[k]*(x-u0)**k for k in range(17));u=f*(x-u0)**17
initial={'u':packpoly(u),'v':packpoly(v),'interpolation_coefficients':list(map(pack,ss)),'y_series':list(map(str,ys))};stages=[]
while int(u.poldegree())>17:
 num=F-v*v;div=p.divrem(num,u);rr=minv(div[1]);uu=div[0];scale=uu.pollead();uu=uu/scale;quo=p.divrem(-v,uu)[0];vv=(-v)%uu
 rec={'old_degree':int(u.poldegree()),'new_degree':int(uu.poldegree()),'division_remainder_v2':rr,'scale':pack(scale),'new_u':packpoly(uu),'new_v':packpoly(vv),'v_quotient':packpoly(quo)}
 stages.append(rec);print(json.dumps({'stage':'reduce','old_degree':rec['old_degree'],'new_degree':rec['new_degree']}),flush=True);u,v=uu,vv
ue=[];ve=[];omega_v=10**6;endpoint_precision=P
for q,out in [(u,ue),(v,ve)]:
 for i in range(max(0,int(q.poldegree()))+1):
  c=q.polcoef(i);cl=p.lift(c);omega_v=min(omega_v,v2(cl.polcoef(1)));endpoint_precision=min(endpoint_precision,v2(cl.polcoef(0)-cl.polcoef(0).lift()));out.append(str(cl.polcoef(0).lift()))
raw0=[Q(z)for z in ue];z=L.ZERO.copy()
for i,c in enumerate(raw0):
 c=c*(1<<(3+i//3))
 if c.denominator!=1:raise ArithmeticError('T1 integral normalization')
 z[i]=int(c)%65536
prec=16
for _ in range(6):z,prec=L.divide_u(z,prec)
L.MOD=256;L.PREC=8;ch1=L.unit_class(z%256);L.MOD=65536;L.PREC=16
out={'precision':P,'root_index':args.root_index,'residue_root':r,'tau_basis_mod2P':tau,'unram_equation_v2':terr,'factor18':packpoly(f),'conjugate_factor18':packpoly(fc),'factor_product_v2':err,'initial':initial,'stages':stages,'endpoint_degree':int(u.poldegree()),'omega_component_v2':omega_v,'endpoint_absolute_precision_bits':endpoint_precision,'u_endpoint_rational_ascending':ue,'v_endpoint_rational_ascending':ve,'torsion0':t0,'torsion1':{'scalar_two_power':3,'U_square_power':6,'unit_basis_mod256':list(map(int,z%256)),'character_hex':hex(ch1)},'seconds':time.monotonic()-start}
args.output_dir.mkdir(parents=True,exist_ok=True)
(args.output_dir/('TORSION1_P'+str(P)+'_R'+str(args.root_index)+'.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict({k:out[k]for k in ['precision','residue_root','omega_component_v2','endpoint_absolute_precision_bits','seconds']},torsion0=hex(ch0),torsion1=hex(ch1))),flush=True)
