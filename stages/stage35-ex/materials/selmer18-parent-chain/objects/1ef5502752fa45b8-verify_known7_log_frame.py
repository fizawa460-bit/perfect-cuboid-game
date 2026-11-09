"""Independent stdlib finite-ring/local-integral check and optional group replay.

This certifies a logarithm frame for the OLD SEVEN classes only. It refuses
to promote the resulting a0=1 differential to a whole-MW annihilator.
"""
from pathlib import Path
from fractions import Fraction
import argparse,copy,json,math,hashlib,subprocess,sys,time,tempfile
ROOT=Path(__file__).resolve().parent;checks=0
def require(ok,label):
 global checks
 checks+=1
 if not ok:raise ValueError(label)
def load(n):return json.loads((ROOT/n).read_text())
def tr(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def padd(a,b,p):return tr([((a[i]if i<len(a)else 0)+(b[i]if i<len(b)else 0))%p for i in range(max(len(a),len(b)))])
def pmul(a,b,p):
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%p
 return tr(z)
def pdiv(a,b,p):
 a=tr(a);b=tr(b);q=[0]*max(1,len(a)-len(b)+1);inv=pow(b[-1],-1,p)
 while a!=[0]and len(a)>=len(b):
  i=len(a)-len(b);z=a[-1]*inv%p;q[i]=z
  for j,y in enumerate(b):a[i+j]=(a[i+j]-z*y)%p
  a=tr(a)
 return tr(q),a
def pinverse(a,b,p):
 r0,r1=tr(b),tr(a);s0,s1=[0],[1]
 while r1!=[0]:
  q,r=pdiv(r0,r1,p);r0,r1=r1,r;s0,s1=s1,padd(s0,[-x for x in pmul(q,s1,p)],p)
 require(len(r0)==1 and r0[0]!=0,'finite-field unit for coefficient inverse')
 s=[x*pow(r0[0],-1,p)%p for x in s0];return pdiv(s,b,p)[1]
class Ring:
 def __init__(self,p,k,T):self.p=p;self.k=k;self.m=p**k;self.T=T;self.zero=(0,)*6;self.one=(1,0,0,0,0,0)
 def scalar(self,v):return (v%self.m,0,0,0,0,0)
 def elem(self,v):return tuple((v[i]if i<len(v)else 0)%self.m for i in range(6))
 def add(self,a,b):return tuple((x+y)%self.m for x,y in zip(a,b))
 def neg(self,a):return tuple(-x%self.m for x in a)
 def sub(self,a,b):return self.add(a,self.neg(b))
 def scale(self,a,n):return tuple(x*n%self.m for x in a)
 def mul(self,a,b):
  z=[0]*11
  for i,x in enumerate(a):
   for j,y in enumerate(b):z[i+j]+=x*y
  for i in range(10,5,-1):
   v=z[i]%self.m
   for j in range(6):z[i-6+j]-=v*self.T[j]
  return tuple(x%self.m for x in z[:6])
 def power(self,a,n):
  z=self.one
  while n:
   if n&1:z=self.mul(z,a)
   a=self.mul(a,a);n//=2
  return z
 def inverse(self,a):
  bb=pinverse([x%self.p for x in a],[x%self.p for x in self.T],self.p);b=self.elem(bb)
  for _ in range(self.k.bit_length()+1):b=self.mul(b,self.sub(self.scalar(2),self.mul(a,b)))
  require(self.mul(a,b)==self.one,'independent coefficient Hensel inverse')
  return b
 def eval(self,c,a):
  z=self.zero
  for x in reversed(c):z=self.add(self.mul(z,a),self.scalar(x))
  return z
 def sqrtseries(self,h,a,y,n):
  powers=[self.one]
  for _ in range(len(h)):powers.append(self.mul(powers[-1],a))
  hh=[]
  for i in range(n):
   z=self.zero
   for j in range(i,len(h)):z=self.add(z,self.scale(powers[j-i],h[j]*math.comb(j,i)))
   hh.append(z)
  out=[y];inverse=self.inverse(self.scale(y,2))
  for i in range(1,n):
   z=hh[i]
   for j in range(1,i):z=self.sub(z,self.mul(out[j],out[i-j]))
   out.append(self.mul(z,inverse))
  return out
def determinant(a):
 a=[r[:]for r in a];sgn=1;prev=1
 for k in range(len(a)-1):
  i=next((i for i in range(k,len(a))if a[i][k]),None)
  if i is None:return 0
  if i!=k:a[i],a[k]=a[k],a[i];sgn=-sgn
  pivot=a[k][k]
  for i in range(k+1,len(a)):
   for j in range(k+1,len(a)):a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])//prev
   a[i][k]=0
  prev=pivot
 return sgn*a[-1][-1]
def solve(a,b,power,p=163):
 z=[r[:]+[v]for r,v in zip(a,b)];n=len(z)
 for j in range(n):
  i=next(i for i in range(j,n)if z[i][j]%p);z[j],z[i]=z[i],z[j];inv=pow(z[j][j],-1,power);z[j]=[v*inv%power for v in z[j]]
  for i in range(n):
   if i!=j:
    s=z[i][j];z[i]=[(x-s*y)%power for x,y in zip(z[i],z[j])]
 return [r[-1]for r in z]
def guard(d):
 require(d['scope']=='KNOWN_SEVEN_MW_CLASSES_ONLY','scope of partial annihilator')
 require(d['known7_log_rank']==7 and d['known7_annihilator_dimension']==10,'partial frame dimensions')
 require(d['whole_MW_log_upper_certified'] is False and d['whole_MW_annihilator_constructed'] is False,'unknown whole-MW directions not discarded')
 require(d['a0_unit_for_known7'] is True and d['a0_unit_for_whole_MW'] is False,'a0 unit is scoped to known7')
 require(d['known7_MW_finite_index_proved'] is False,'partial subgroup not whole MW')
 require(d['new_global_MW_points']==0 and d['source_exclusions_new']==0,'no new point or source exclusion credit')
 require(d['new_independent_mathematical_audit']=='PENDING_NOT_RUN','no automatic independent audit')
 require(d['auxiliary_local_chart_points_are_global_MW'] is False,'local chart is not global MW data')
def build(primary_override=None):
 p=163;k=6;mod=p**5;primary=primary_override if primary_override is not None else load('KNOWN7_LOGS_P6_EXT0_CHART0_ANN1.json');parent=load('parents/rank6_divisors.json');h=parent['h2_coefficients_ascending']
 def imul(a,b):
  z=[0]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):z[i+j]+=x*y
  return z
 A=parent['A_coefficients_ascending'];B=parent['B_coefficients_ascending'];AA=imul(A,A);BB=[0]+imul(B,B)
 require(h==[AA[i]-(BB[i]if i<len(BB)else 0)for i in range(len(AA))],'exact inherited h2=A2-XB2')
 factors=parent['B_factors_coefficients_ascending'];product=[parent['B_factorization_constant']]
 for f in factors:product=imul(product,f)
 require(product==B,'exact global divisor support factors B')
 names=['D1a','D1b','D2','D4','D9','F2','D_inf'];require(primary['class_order']==names,'canonical old7 classes')
 L=[r['normalized_log_vector']for r in primary['results']]
 for n in ['KNOWN7_LOGS_P6_EXT1_CHART2_ANN1.json','KNOWN7_LOGS_P8_EXT0_CHART1_ANN2.json']:
  q=load(n)
  for i in range(7):
   require(q['results'][i]['name']==names[i],'cross-run class')
   for a,b in zip(L[i],q['results'][i]['normalized_log_vector']):require((a-b)%mod==0,'extension/chart/precision/scalar cross check')
 # An independently implemented finite-ring reconstruction of the local integrals.
 R=Ring(p,k,primary['extension_modulus_ascending']);alpha=R.elem(primary['branch_root_alpha_mod_pK'])
 require(R.eval(h,alpha)==R.zero,'branch root in same curve')
 points=[(R.elem(a),R.elem(y))for a,y in zip(primary['chart_local_original_x_field_coordinates'],primary['chart_local_y_field_coordinates'])];local=[]
 for i,(a,y)in enumerate(points):
  require(R.mul(y,y)==R.eval(h,a),'chart point curve equation')
  for b,z in points[:i]:require(any(v%p for v in R.sub(a,b)),'distinct chart abscissas modulo163')
  ys=R.sqrtseries(h,a,y,k-1);inv=R.inverse(y);b=[R.inverse(R.scale(y,2))]
  for m in range(1,k-1):
   z=R.zero
   for q in range(1,m+1):z=R.add(z,R.mul(ys[q],b[m-q]))
   b.append(R.neg(R.mul(z,inv)))
  powers=[R.one]
  for _ in range(17):powers.append(R.mul(powers[-1],a))
  prim=[]
  for j in range(17):
   row=[]
   for m in range(k-1):
    z=R.zero
    for q in range(min(m,j)+1):z=R.add(z,R.scale(R.mul(powers[j-q],b[m-q]),math.comb(j,q)))
    row.append(R.scale(z,pow(m+1,-1,R.m)))
   prim.append(row)
  local.append(prim)
 N=primary['annihilating_integer_N'];require(N%p!=0,'normalizing N prime to163')
 for rec in primary['results']:
  sums=[R.zero]*17
  for s,((a,y),xx,yy,dd)in enumerate(zip(points,rec['chart_endpoints_original_x_mod_pK'],rec['chart_endpoints_original_y_mod_pK'],rec['chart_deltas_field_coordinates'])):
   xx=R.elem(xx);yy=R.elem(yy);delta=R.elem(dd)
   require(R.sub(xx,a)==delta,'recorded endpoint difference')
   require(all(v%p==0 for v in delta),'endpoint same local disk')
   require(all(v%p==0 for v in R.sub(yy,y)),'endpoint same y branch')
   require(R.mul(yy,yy)==R.eval(h,xx),'endpoint curve equation')
   powers=[delta]
   for _ in range(k-2):powers.append(R.mul(powers[-1],delta))
   for j in range(17):
    for m in range(k-1):sums[j]=R.add(sums[j],R.mul(local[s][j][m],powers[m]))
  for j,z in enumerate(sums):
   require(list(z)==rec['raw_integral_sum_field_coordinates'][j],'independent local integral sum')
   require(all(v%p==0 for v in z),'raw sum divisible163')
   zz=[v//p*pow(N,-1,mod)%mod for v in z]
   require(not any(zz[1:]),'normalized logarithm descends to Q163')
   require(zz[0]==L[names.index(rec['name'])][j],'normalized coordinate equals primary')
 I=list(range(1,8));J=[0]+list(range(8,17));minor=[[r[j]%p for j in I]for r in L];det=determinant(minor)
 require(det%p!=0,'unit 7x7 log minor excluding column0')
 AI=[[r[j]for j in I]for r in L];basis=[]
 for free in J:
  vals=solve(AI,[-r[free]%mod for r in L],mod);w=[0]*17;w[free]=1
  for j,v in zip(I,vals):w[j]=v
  for row in L:require(sum(a*b for a,b in zip(row,w))%mod==0,'partial annihilator coordinate')
  basis.append(w)
 # Independent tiny integral at P0; this local point is NOT global MW input.
 tiny=load('KNOWN7_LOGS_P6_EXT1_CHART1_ANN1.json')['results'][0]['normalized_log_vector'];ys=[Fraction(1)]
 for n in range(1,k-1):ys.append(Fraction(h[n]-sum(ys[j]*ys[n-j]for j in range(1,n)),2))
 bb=[Fraction(1,2)]
 for n in range(1,k-1):bb.append(-sum(ys[j]*bb[n-j]for j in range(1,n+1)))
 for j in range(17):
  q=sum((bb[m-j]*Fraction(p**m,m+1)for m in range(j,k-1)),Fraction(0));require(tiny[j]==q.numerator*pow(q.denominator,-1,mod)%mod,'direct tiny integral normalization calibration')
 high=load('KNOWN7_LOGS_P8_EXT0_CHART1_ANN2.json');hh={r['name']:r['normalized_log_vector']for r in high['results']}
 for j in range(17):require((35*hh['P0_MINUS'][j]-4*sum(hh[n][j]for n in names[:5])-hh['D_inf'][j])%(p**7)==0,'global principal-divisor relation calibration')
 d={'run_id':'R3-20261105-C2-P163-CONCRETE-KNOWN7-LOG-FRAME','scope':'KNOWN_SEVEN_MW_CLASSES_ONLY','prime':p,'normalized_log_definition':'log(D)/163 in holomorphic basis X^j dX/(2Y), j0..16','normalized_log_precision':5,'class_order':names,'normalized_log_matrix_mod163power5':L,'normalized_log_matrix_mod163':[[v%p for v in r]for r in L],'pivot_columns_zero_based':I,'free_columns_zero_based':J,'minor_mod163':minor,'minor_integer_determinant':det,'minor_determinant_mod163':det%p,'known7_log_rank':7,'known7_log_lattice_saturated_in_Z163_17':True,'known7_annihilator_dimension':10,'partial_annihilator_basis_mod163power5':basis,'partial_annihilator_a0_one_mod163': [v%p for v in basis[0]],'exact_partial_coefficient_definition':'a0=1; aI=-L_I^{-1} L_0 using the EXACT seven normalized logarithms; remaining a8..16=0. Other basis vectors are defined analogously for free columns0,8..16.','a0_unit_for_known7':True,'a0_unit_for_whole_MW':False,'whole_MW_log_upper_certified':False,'whole_MW_annihilator_constructed':False,'known7_MW_finite_index_proved':False,'remaining_global_residual_log_coordinates':10,'remaining_global_residual_log_Q163_rank_upper':7,'inherited_MW_rank_interval':[7,14],'inherited_row360_source_base_bound':14,'new_global_MW_points':0,'auxiliary_local_chart_points_are_global_MW':False,'source_exclusions_new':0,'new_independent_mathematical_audit':'PENDING_NOT_RUN','P23_LOW':'OPEN','Branch_B':'OPEN','formal_R0':'C35-200_UNCHANGED','new_scope':'Actual old7 logarithms, unit minor and concrete partial annihilator frame. No full-MW coverage; no recredit of old MW lower/upper/unit/classgroup/source disk results.','input_SHA256':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest()for n in ['parents/rank6_divisors.json','KNOWN7_LOGS_P6_EXT0_CHART0_ANN1.json','KNOWN7_LOGS_P6_EXT1_CHART2_ANN1.json','KNOWN7_LOGS_P8_EXT0_CHART1_ANN2.json','KNOWN7_LOGS_P6_EXT1_CHART1_ANN1.json']}}
 guard(d);return d
def negatives(d):
 bad=[('scope','WHOLE_MW'),('known7_log_rank',14),('whole_MW_log_upper_certified',True),('a0_unit_for_whole_MW',True),('known7_MW_finite_index_proved',True),('new_global_MW_points',1),('source_exclusions_new',1),('auxiliary_local_chart_points_are_global_MW',True)]
 for k,v in bad:
  z=copy.deepcopy(d);z[k]=v
  try:guard(z)
  except ValueError:continue
  raise RuntimeError('scope negative accepted: '+k)
 primary=load('KNOWN7_LOGS_P6_EXT0_CHART0_ANN1.json')
 for fault in ['log','endpoint','normalizer']:
  z=copy.deepcopy(primary)
  if fault=='log':z['results'][0]['normalized_log_vector'][0]+=1
  elif fault=='endpoint':z['results'][0]['chart_endpoints_original_y_mod_pK'][0][0]+=1
  else:z['annihilating_integer_N']+=1
  try:build(z)
  except ValueError:continue
  raise RuntimeError('arithmetic fault accepted: '+fault)
 return len(bad)+3
def main():
 global checks
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--replay',action='store_true');ap.add_argument('--log');args=ap.parse_args();start=time.monotonic()
 d=build();count=checks;negative=negatives(d);checks=count;dest=ROOT/'known7_log_frame_certificate.json'
 if args.write:dest.write_text(json.dumps(d,indent=2)+'\n')
 else:require(d==json.loads(dest.read_text()),'frozen log-frame certificate')
 if args.replay:
  with tempfile.TemporaryDirectory(prefix='r307_log_replay_')as folder:
   cmd=[sys.executable,str(ROOT/'compute_known7_logs.py'),'--precision','6','--output-dir',folder];r=subprocess.run(cmd,capture_output=True,text=True)
   if r.returncode:raise RuntimeError(r.stdout+r.stderr)
   replay=json.loads((Path(folder)/'KNOWN7_LOGS_P6_EXT0_CHART0_ANN1.json').read_text())
   require([z['normalized_log_vector']for z in replay['results']]==d['normalized_log_matrix_mod163power5'],'complete scalar-chain/local-integral replay')
 out={'status':'INTERNAL_EXACT_PASS_KNOWN7_ONLY','checks':checks,'negative_scope_controls':negative,'full_group_algorithm_replayed':args.replay,'known7_log_rank':7,'partial_minor_mod163':d['minor_determinant_mod163'],'partial_a0':1,'whole_MW_coverage':False,'source_exclusions':0,'independent_mathematical_audit':'PENDING_NOT_RUN','seconds':round(time.monotonic()-start,3)}
 if args.log:(ROOT/args.log).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out))
if __name__=='__main__':main()
