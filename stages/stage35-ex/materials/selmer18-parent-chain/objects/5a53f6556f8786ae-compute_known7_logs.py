"""Compute ACTUAL logarithms of old seven MW classes, not all-MW coverage.

The finite ring and local integrals are exact. No floating point is used.
The auxiliary N need only kill the seven reductions; this is checked by the
final Mumford divisor returning to the fixed local chart modulo163.
"""
from pathlib import Path
import argparse,json,sys,time,math,hashlib
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'_deps'))
from cypari2 import Pari

def run(k=6,extension=0,chart=0,selected=None,multiplier=1,output_dir=None):
 if not 2<=k<=160:raise ValueError('this integral truncation requires 2<=precision<=160')
 p=163;mod=p**k;start=time.monotonic();pari=Pari();pari.allocatemem(536870912)
 x=pari('x');t=pari('t');unit=pari.Mod(1,mod)
 source=json.loads((ROOT/'parents/rank6_divisors.json').read_text())
 h=source['h2_coefficients_ascending'];A=source['A_coefficients_ascending'];B=source['B_coefficients_ascending']
 Tlist=[[21,110,152,30,67,44,1],[93,152,73,73,47,92,1]]
 for line in (ROOT/'mumford_ring.gp').read_text().splitlines():
  if line.strip()and not line.lstrip().startswith('\\\\'):pari(line)
 for name in ['setring','cinv','pinv','mred','mdbl','madd','moffset','crtpoly']:
  if pari(name).type()!='t_CLOSURE':raise RuntimeError('GP function not loaded: '+name)
 pari('setring')(p,k,Tlist[extension])
 ci=pari('cinv');T=pari('RT');alpha=pari('RC')
 def evalpoly(c,a):
  z=0
  for v in reversed(c):z=z*a+v
  return z
 hp=[i*h[i]for i in range(1,len(h))]
 for _ in range(k.bit_length()+1):alpha-=evalpoly(h,alpha)*ci(evalpoly(hp,alpha))
 if evalpoly(h,alpha)!=0:raise RuntimeError('Hensel branch root failure')
 def reverse_shift(c,n):
  return pari.Polrev([sum(c[j]*math.comb(j,n-i)*alpha**(j-(n-i))for j in range(n-i,len(c)))for i in range(n+1)],x)
 oddfull=reverse_shift(h,36)
 f=pari.Polrev([oddfull.polcoef(i)for i in range(36)],x)
 if oddfull.polcoef(36)!=0 or int(f.poldegree())!=35:raise RuntimeError('odd model wrong degree')
 pari('setcurve')(f,17)
 # Coefficients of the exact local sqrt of f(u0+s), constant y0.
 def sqrtseries(coeffs,a,y0,n):
  ff=[sum(coeffs[j]*math.comb(j,i)*a**(j-i)for j in range(i,len(coeffs)))for i in range(n)]
  y=[y0]
  for i in range(1,n):y.append((ff[i]-sum(y[j]*y[i-j]for j in range(1,i)))*ci(2*y0))
  return y
 oddcoeff=[f.polcoef(i)for i in range(36)]
 u0=-ci(alpha);v0=u0**18
 if v0**2!=f(u0):raise RuntimeError('P0 odd-model point failure')
 Ypoly=reverse_shift(A,18);AB=A[:]
 for i,b in enumerate(B):AB[i]+=b
 Ypoly2=reverse_shift(AB,18)
 divisors=[]
 for name,c in zip(source['class_order'],source['class_G_coefficients_ascending']):
  d=len(c)-1;u=reverse_shift(c,d);u=u*ci(u.pollead())
  v=(Ypoly2 if name=='F2'else Ypoly)%u
  base=(x-u0)**d
  ys=sqrtseries(oddcoeff,u0,-v0,d)
  bv=sum(ys[i]*(x-u0)**i for i in range(d))
  vv=pari('crtpoly')(v,u,bv,base)
  D=pari('mred')([u*base,vv]);divisors.append((name,D))
 # I+ maps to (u,v)=(0,+1); I- is its hyperelliptic conjugate.
 Dinf=pari('mred')([x*x,1+f.polcoef(1)*x/2]);divisors.append(('D_inf',Dinf))
 if selected and 'P0_MINUS' in selected:
  ys=sqrtseries(oddcoeff,u0,-v0,2)
  divisors.append(('P0_MINUS',pari('mred')([(x-u0)**2,ys[0]+ys[1]*(x-u0)])))
 if selected and 'LOCAL_TINY163' in selected:
  aa=p;yy=unit
  for _ in range(k.bit_length()+1):yy=(yy+evalpoly(h,aa)*ci(yy))*ci(2)
  uu=ci(aa-alpha);vv=yy*uu**18
  base=x-u0;ug=x-uu;bv=-v0
  divisors.append(('LOCAL_TINY163',[[x-uu,vv],[x-u0,-v0]]))
 # A degree17 local chart over the UNRAMIFIED EXTENSION, not global MW points.
 # Using rational residue points makes intermediate CRT collisions common;
 # generic extension points avoid that chart defect without dividing by p.
 top=pari('top');tom=pari('tom');q=p**6;ab=top(alpha)
 odd=q-1;twopower=0
 while odd%2==0:odd//=2;twopower+=1
 nonsquare=next(ab+j for j in range(p)if (ab+j)**((q-1)//2)==-1)
 def finite_sqrt(a):
  c=nonsquare**odd;r=a**((odd+1)//2);tt=a**odd;mm=twopower
  while tt!=1:
   ii=1;ss=tt*tt
   while ss!=1:ss=ss*ss;ii+=1
   if ii>=mm:raise RuntimeError('finite sqrt Tonelli failure')
   bb=c**(2**(mm-ii-1));r*=bb;tt*=bb*bb;c=bb*bb;mm=ii
  if r*r!=a:raise RuntimeError('finite square root identity')
  return r
 candidates=[]
 for shift in range(1,p):
  a=alpha+shift;ha=evalpoly(h,a);res=top(ha)
  if res!=0 and res**((q-1)//2)==1:candidates.append((shift,a,ha,res))
 points=[]
 shifts=[]
 for shift,a,ha,res in candidates[chart:chart+17]:
  y=tom(finite_sqrt(res))
  for _ in range(k.bit_length()+1):y=(y+ha*ci(y))*ci(2)
  if y*y!=ha*unit:raise RuntimeError('local chart square root failure')
  points.append((a,y,ci(a-alpha)))
  shifts.append(shift)
 E=[pari(1),pari(0)]
 for a,y,u in points:E=pari('madd')(E,[x-u,y*u**18])
 if int(E[0].poldegree())!=17:raise RuntimeError('chart wrong degree')
 N=multiplier*json.loads((ROOT.parent/'exploratory/JACOBIAN_ORDER163_DISCOVERY.json').read_text())['Jacobian_order']
 def fieldvec(z):
  q=z.lift()
  return [int(q.polcoef(i).lift())%mod for i in range(6)]
 def ismodpzero(z):return all(v%p==0 for v in fieldvec(z))
 def ismodp_polyzero(z):return all(ismodpzero(z.polcoef(i))for i in range(max(0,int(z.poldegree()))+1))
 # Precompute first k-1 coefficients of each holomorphic primitive at E_i.
 local=[]
 for a,y,u in points:
  ys=sqrtseries(h,a,y,k-1);b=[ci(2*y)]
  for m in range(1,k-1):b.append(-sum(ys[j]*b[m-j]for j in range(1,m+1))*ci(y))
  prim=[]
  for j in range(17):
   prim.append([sum(math.comb(j,q)*a**(j-q)*b[m-q]for q in range(min(m,j)+1))*ci(m+1)for m in range(k-1)])
  local.append(prim)
 results=[]
 print(json.dumps({'stage':'start','precision':k,'extension':extension,'chart':chart,'N':N,'elapsed':round(time.monotonic()-start,2)}),flush=True)
 for name,D in divisors:
  if selected and name not in selected:continue
  began=time.monotonic();before=int(pari('COUNTER'))
  try:
   R=pari('mtinyoffset')(D[0],D[1],N,E)if name=='LOCAL_TINY163'else pari('moffset')(D,N,E)
  except Exception:
   print('failure step/op',pari('DBGSTEP'),pari('DBGOP'),flush=True)
   raise
  if not ismodp_polyzero(R[0]-E[0])or not ismodp_polyzero(R[1]-E[1]):raise RuntimeError('N does not return '+name+' to the chart modulo163')
  totals=[alpha*0 for _ in range(17)];deltas=[];endx=[];endy=[]
  for s,(a,y,u)in enumerate(points):
   root=u
   for _ in range(k.bit_length()+1):root-=R[0](root)*ci(R[0].deriv()(root))
   if R[0](root)!=0:raise RuntimeError('endpoint Hensel root')
   xx=alpha+ci(root);yy=R[1](root)*ci(root)**18;delta=xx-a
   if not ismodpzero(delta)or not ismodpzero(yy-y):raise RuntimeError('endpoint wrong disk/branch')
   if yy*yy!=evalpoly(h,xx):raise RuntimeError('endpoint original curve equation')
   deltas.append(fieldvec(delta));endx.append(fieldvec(xx));endy.append(fieldvec(yy))
   powers=[delta]
   for m in range(1,k-1):powers.append(powers[-1]*delta)
   for j in range(17):totals[j]+=sum(local[s][j][m]*powers[m]for m in range(k-1))
  modulus=p**(k-1);normal=[]
  for z in totals:
   vv=fieldvec(z)
   if any(v%p for v in vv):raise RuntimeError('sum is not p-integral')
   vv=[(v//p)*pow(N,-1,modulus)%modulus for v in vv]
   if any(vv[1:]):raise RuntimeError('logarithm did not descend to Q163')
   normal.append(vv[0])
  rec={'name':name,'normalized_log_modulus':modulus,'normalized_log_vector':normal,'raw_integral_sum_field_coordinates':[fieldvec(z)for z in totals],'chart_endpoints_original_x_mod_pK':endx,'chart_endpoints_original_y_mod_pK':endy,'chart_deltas_field_coordinates':deltas,'group_operations':int(pari('COUNTER'))-before,'seconds':round(time.monotonic()-began,4)}
  results.append(rec)
  print(json.dumps({'finished':name,'normal_log_mod163':[v%p for v in normal],'operations':rec['group_operations'],'seconds':rec['seconds']}),flush=True)
  out={'scope':'old seven MW classes ONLY; no whole-MW coverage','prime':p,'working_precision':k,'normalized_log_precision':k-1,'extension_factor_index':extension,'extension_modulus_ascending':Tlist[extension],'chart_index':chart,'chart_shift_values':shifts,'chart_local_original_x_field_coordinates':[fieldvec(a)for a,y,u in points],'auxiliary_chart_points_are_global_MW':False,'annihilating_integer_N':N,'N_is_needed_only_to_kill_each_input_reduction':True,'class_order':[z['name']for z in results],'results':results,'whole_MW_annihilator_constructed':False,'known7_finite_index_proved':False,'source_exclusions':0,'new_independent_mathematical_audit':'PENDING_NOT_RUN','seconds':time.monotonic()-start}
  out['annihilating_integer_multiplier']=multiplier
  out['branch_root_alpha_mod_pK']=fieldvec(alpha)
  out['chart_local_y_field_coordinates']=[fieldvec(y)for a,y,u in points]
  destination=Path(output_dir)if output_dir else ROOT;destination.mkdir(parents=True,exist_ok=True)
  dest=destination/f'KNOWN7_LOGS_P{k}_EXT{extension}_CHART{chart}_ANN{multiplier}.json';dest.write_text(json.dumps(out,indent=2)+'\n')
 return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=6);ap.add_argument('--extension',type=int,default=0);ap.add_argument('--chart',type=int,default=0);ap.add_argument('--classes',nargs='*');ap.add_argument('--multiplier',type=int,default=1);ap.add_argument('--output-dir');args=ap.parse_args()
 run(args.precision,args.extension,args.chart,args.classes,args.multiplier,args.output_dir)
