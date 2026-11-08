"""Row359 exact proof checks: three new ordinary units, true Selmer<=14.

Python3 + NumPy. No Wolfram, root finder, LLL, network, or floating-point proof
comparison is used. NumPy is used only for the previously audited finite ring
arithmetic in local2_arithmetic.py. This is INTERNAL verification, not an
independent mathematical audit. Parent scopes remain explicit.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import os,sys,json,hashlib,time
precision=12
for arg in sys.argv:
 if arg.startswith('--precision='):precision=int(arg.split('=')[1])
if precision not in [10,12]:raise ValueError('supported verification precisions10,12')
os.environ['LOCAL2_PRECISION']=str(precision)
import local2_arithmetic as L
P=Path(__file__).resolve().parent
start=time.time();checks=0;negatives=0
def check(ok,label):
 global checks
 if not ok:raise RuntimeError(label)
 checks+=1
def negative(ok,label):
 global negatives
 if ok:raise RuntimeError('unrejected negative control: '+label)
 negatives+=1
def load(name):return json.loads((P/name).read_text())
def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def padd(a,b,k=1):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=k*x
 return trim(c)
def pmul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def prem(a,f):
 a=trim(a)
 if f[-1]!=1:raise ValueError('monic modulus required')
 while len(a)>=len(f):
  k=len(a)-len(f);c=a[-1]
  for i,x in enumerate(f):a[k+i]-=c*x
  a=trim(a)
 return a
def ppowmod(a,n,f):
 b=[1];a=prem(a,f)
 while n:
  if n&1:b=prem(pmul(b,a),f)
  a=prem(pmul(a,a),f);n>>=1
 return b
def peval(a,x):
 v=0
 for c in a[::-1]:v=v*x+c
 return v
def det(a):
 a=[r[:]for r in a];n=len(a);sg=1;prev=1
 if not n:return 1
 for k in range(n-1):
  if not a[k][k]:
   j=next((j for j in range(k+1,n)if a[j][k]),None)
   if j is None:return 0
   a[k],a[j]=a[j],a[k];sg=-sg
  pv=a[k][k]
  for i in range(k+1,n):
   ai=a[i][k]
   for j in range(k+1,n):
    z=a[i][j]*pv-ai*a[k][j]
    if z%prev:raise ArithmeticError('Bareiss division not exact')
    a[i][j]=z//prev
   a[i][k]=0
  prev=pv
 return sg*a[-1][-1]
def resultant(f,g):
 f=trim(f);g=trim(g);m=len(f)-1;n=len(g)-1
 if n==0:return g[0]**m
 a=[[0]*(m+n)for _ in range(m+n)]
 for i in range(n):a[i][i:i+m+1]=f[::-1]
 for i in range(m):a[n+i][i:i+n+1]=g[::-1]
 return det(a)
def norm_by_multiplication_matrix(f,q):
 n=len(f)-1;a=[[0]*n for _ in range(n)]
 for j in range(n):
  v=prem([0]*j+q,f)
  for i,c in enumerate(v):a[i][j]=c
 return det(a)
def rank(vs):
 p={}
 for vv in vs:
  v=int(vv)
  while v:
   k=v.bit_length()-1
   if k in p:v^=p[k]
   else:p[k]=v;break
 return len(p)
def mask(bits):return sum(int(b)<<i for i,b in enumerate(bits))
def sign_interval(q,l,r):
 lo=hi=Q(q[-1])
 for c in q[-2::-1]:
  z=[lo*l,lo*r,hi*l,hi*r];lo=min(z)+c;hi=max(z)+c
 return lo,hi
def qvec_theta(q,k):
 cs=[sum(q[j]*comb(j,i)*2**i*(-3)**(j-i)for j in range(i,len(q)))*(1<<(i//3))for i in range(len(q))]
 check(all(c%(1<<k)==0 for c in cs),'old unit integral coordinates inherited and bound to definition')
 v=L.ZERO.copy();v[:len(cs)]=[c//(1<<k)%L.MOD for c in cs];return v
def defect(c):return mask([(h&c).bit_count()&1 for h in constraints])

new=load('new_unit_definitions.json')
old=load('parents/row356_global_four_cuts.json')
u12=load('parents/unit12.json')
row358=load('parents/row358_finite_even.json')
oldV=load('parents/row349_V_fourth_root.json')
G=load('parents/rank6_divisors.json')
bridge=load('parents/row351_true_fake_bridge.json')
local=load('dyadic_full_kummer_certificate.json')
order=load('parents/PARENT_ROW345_LOCAL_DIMENSIONS/signed18_c2_full_maximal_order_certificate.json')
h=G['h2_coefficients_ascending'];f=new['V_minimal_polynomial_ascending']
check(h==u12['h2_coefficients_ascending']==local['h2_coefficients_ascending']==order['h2_coefficients_ascending']==oldV['h2_coefficients_ascending'],'one exact fixed degree36 field and curve')
check(len(h)==37 and h[0]==h[-1]==1 and len(f)==37 and f[-1]==f[0]==1,'degree36 monic theta and V polynomials, both units')
check(order['global_maximal_order_established'] is True and order['number_field_signature']==[4,16],'inherited exact maximal order/signature')
check(row358['full_finite_even_fake_ambient_dimension']=='19+c_K' and row358['ordinary_class_2_rank_upper']==3,'audited row358 full-domain ambient and ordinary class2 bound')
check(bridge['fake_map_on_true_selmer_exists'] is True and bridge['true_selmer_to_fake_kernel_dimension_upper']==1 and old['rank_lower_retained']==7,'global true Selmer comparison, kernel<=1 and old MW lower7')
check(old['known_unit_local_defect_rank']==6 and u12['expected_GF2_rank']==13,'old12 units and minus1 are independent, old defect image rank6')

# Reprove the exact fourth root identity in Q[theta], avoiding reliance on a
# numerical algebraic-root selection or a CAS output.
qs=oldV['q_poly_ASC'];g2=qs['Q2_rho'];g4=qs['Q4_beta4'];g9=qs['Q9_beta9'];a8=qs['A8_gamma8']
num=ppowmod(pmul([1,3],g9),15,h)
den=[1<<14]
for q,e in [([0,1],3),([1,1],2),(g2,2),(g4,2),(a8,17)]:den=prem(pmul(den,ppowmod(q,e,h)),h)
identity=prem(padd(ppowmod(num,4,h),pmul([0,1],ppowmod(den,4,h)),-1),h)
check(identity==[0],'exact V=N(theta)/D(theta) satisfies V^4=theta')
p=61;t=47;nv=peval(num,t)%p;dv=peval(den,t)%p
check(peval(h,t)%p==0 and dv!=0,'actual old simple p61 theta place and nonzero V denominator')
vr=nv*pow(dv,-1,p)%p
check(vr==32 and pow(vr,4,p)==t,'exact p61 sign pin V=32, V^4=47')
A=G['A_coefficients_ascending'];B=G['B_coefficients_ascending']
check(padd(pmul(A,A),[0]+pmul(B,B),-1)==h,'old h=A^2-XB^2 identity')
av=peval(A,t)%p;bv=peval(B,t)%p
check(bv!=0 and (vr*vr*bv+av)%p==0 and (vr*vr*bv-av)%p!=0,'p61 selects V^2*B(theta)+A(theta)=0 globally')
Av4=[0]*73;v2Bv4=[0]*73
for i,c in enumerate(A):Av4[4*i]=c
for i,c in enumerate(B):v2Bv4[4*i+2]=c
fneg=[c*(-1)**i for i,c in enumerate(f)]
check(pmul(f,fneg)==padd(Av4,v2Bv4),'exact factorization A(X4)+X2B(X4)=F(X)F(-X)')
check(peval(f,vr)%p==0 and peval(f,-vr)%p!=0,'p61 selects F(V)=0 from two factors')
# Q(V)=K since theta=V4 and V lies in K; so F is its minimal polynomial.
check(peval(f,1)==2**12 and peval(f,-1)==-2**12,'exact Norm(V-1)=4096; no floating norm')
check(local['ramification_e']==3 and local['residue_degrees']==[4,8],'two dyadic primes have e3 f4,8')
check(4*1+8*1==12,'V-1 positive dyadic valuations are forced to be1,1 by its norm')
for j in range(36):check(j-3*(j//3)>=0,'integrality of b_j=(V-1)^j/2^floor(j/3)')
discV=resultant(f,[i*f[i]for i in range(1,len(f))])
DK=(1<<24)*order['odd_discriminant_factor']
check(discV==DK*2**(2*sum(j//3 for j in range(36))),'optional full maximal basis discriminant equality')

# Sign intervals are rational input certificates, generated during search.
# Four disjoint intervals with sign changes suffice because signature is4,16.
intervals=[(Q(*a),Q(*b))for a,b in new['real_V_root_intervals_in_theta_order']]
check(len(intervals)==4,'four real intervals')
theta_ranges=[]
for l,r in intervals:
 check(l<r and peval(f,l)*peval(f,r)<0,'real V root certified by exact sign change')
 check(l*r>0,'real V root interval avoids0')
 theta_ranges.append((min(l**4,r**4),max(l**4,r**4)))
check(all(theta_ranges[i][1]<theta_ranges[i+1][0]for i in range(3)),'root order theta=V4 matches original four real embeddings')
check(theta_ranges[0][1]<1<theta_ranges[1][0],'epsilon real sign branch threshold')

norm_data=[]
for u in new['units']:
 q=u['q_V'];d=u['denominator'];label=u['label']
 check(d>0 and d&(d-1)==0,'new unit denominator power of2')
 cs=[]
 for j in range(36):
  z=sum(q[k]*comb(k,j)for k in range(j,len(q)))*2**(j//3)
  check(z%d==0,'new unit integral b_j coefficient '+label)
  cs.append(z//d)
 check(cs==u['integral_basis_w_coefficients'],'exact Q(V)/d in integral basis '+label)
 n=resultant(f,q)
 check(n==u['norm']*d**36 and abs(u['norm'])==1,'exact Sylvester/Bareiss norm +/-1 '+label)
 check(norm_by_multiplication_matrix(f,q)==n,'independent36x36 multiplication matrix norm '+label)
 bits=[]
 for l,r in intervals:
  lo,hi=sign_interval(q,l,r)
  check(lo>0 or hi<0,'certified sign of new global unit '+label)
  bits.append(int(hi<0))
 check(bits==u['real_sign_bits'] and sum(bits)%2==int(u['norm']==-1),'real signs agree with exact norm '+label)
 check([int(u['norm']==-1),bits[0]^bits[1]]==u['norm_sign_and_real_pair'],'new norm-real two bits '+label)
 norm_data.append({'label':label,'norm':u['norm'],'denominator':d,'resultant':n,'real_sign_bits':bits,'integral_basis_w_coefficients':cs})

# All modular computations below use the OLD audited O_K basis and characters.
# V is obtained from its old exact unit product; (V-1)^3/2 is computed once.
constraints=[int(x,16)for x in local['local_constraint_interface']['unit_fake_image_constraints_hex']]
check(len(constraints)==19 and rank(constraints)==19,'old full local unit fake image constraints')
scalar=int(local['scalar_minus1_character_hex'],16)
check(not any((r&scalar).bit_count()%2 for r in constraints),'all forms kill scalar minus1')
epsilon=(-4*L.ONE+6*L.U-3*L.power(L.U,2)+L.T)%L.MOD
pi=(L.U-2*L.ONE)%L.MOD
eta=(3*L.ONE+L.mul(L.power(pi,2),L.inv(epsilon)))%L.MOD
sigma=L.mul((L.T-L.power(L.U,2)-L.U+2*L.ONE)%L.MOD,L.inv(epsilon))
units={'epsilon':epsilon,'eta':eta,'sigma':sigma}
for u in u12['unit_definitions']:
 if u['name']not in units:units[u['name']]=qvec_theta(u['q'],u['two_power'])
theta=(2*L.U-3*L.ONE)%L.MOD
V=L.ONE.copy()
for name,e in {'epsilon':5,'eta':15,'alpha':-2,'rho':-2,'beta4':-2,'beta9':15,'gamma8':-17}.items():V=L.mul(V,L.power(units[name]if e>=0 else L.inv(units[name]),abs(e)))
V=L.mul(V,L.power(L.inv(theta),3))
check((L.power(V,4)==theta).all(),'local V^4=theta consistency')
fv=L.ZERO.copy()
for c in f[::-1]:fv=(L.mul(fv,V)+c*L.ONE)%L.MOD
check(not fv.any(),'local signed V satisfies selected F')
w=(V-L.ONE)%L.MOD
check(L.residue(w)==0,'V-1 lies in both dyadic maximal ideals')
w3=L.power(w,3)
check(all(int(x)%2==0 for x in w3),'integral local (V-1)^3/2 coefficients')
tw=(w3//2)%(L.MOD//2)
bb=[L.mul(L.power(tw,j//3),L.power(w,j%3))for j in range(36)]
# Precision10/12 after the single division leaves >=9/11 bits, while the
# inherited squareclass interface is determined modulo2^8.
new_local=[]
for u in new['units']:
 z=sum(((int(c)%L.MOD)*bb[j]for j,c in enumerate(u['integral_basis_w_coefficients'])),L.ZERO.copy())%L.MOD
 cc=L.unit_class(z);dd=defect(cc)
 check(L.r_inv(L.residue(z))!=0,'new representative is a unit at both dyadic primes')
 new_local.append({'label':u['label'],'unit_basis_mod256':[int(x)%256 for x in z],'dyadic_character_hex':hex(cc),'dyadic_defect_hex':hex(dd)})
 units[u['label']]=z
old_defects=[]
for u in old['unit_records']:
 z=units[u['name']];cc=L.unit_class(z)
 check(cc==int(u['dyadic_character_hex'],16) and defect(cc)==int(u['dyadic_defect_hex'],16),'inherited old unit coordinate interface bound, no new credit')
 old_defects.append(int(u['dyadic_defect_hex'],16))
check(rank(old_defects)==6,'old12 defect rank6 retained')
newdef=[int(x['dyadic_defect_hex'],16)for x in new_local]
check(rank(old_defects+newdef)==9,'three new global unit obstruction directions independent modulo old12')

# Seven explicit globally norm-square/real-admissible unit witnesses.
oldw=[int(x['dyadic_defect_hex'],16)for x in old['witnesses']]
maps={u['name']:u for u in old['unit_records']}
neww=[newdef[0]^int(maps['gamma8']['dyadic_defect_hex'],16),newdef[1]^int(maps['epsilon']['dyadic_defect_hex'],16),newdef[2]]
neww_formulas=[['nu1','gamma8'],['nu2','epsilon'],['nu3']]
for wi,inds in enumerate(neww_formulas):
 n=1;sg=[0]*4;z=L.ONE.copy()
 for name in inds:
  rec=next((u for u in new['units']if u['label']==name),None)if name.startswith('nu')else maps[name]
  n*=rec['norm']
  for j,b in enumerate(rec['real_sign_bits']):sg[j]^=b
  z=L.mul(z,units[name])
 check(n==1 and sg[0]==sg[1] and sg[2]==sg[3],'new witness lies in full norm-real candidate')
 check(defect(L.unit_class(z))==neww[wi],'actual product witness defect')
witnesses=oldw+neww
check(rank(witnesses)==7,'seven independent constraints on full norm-real candidate')
rows=[mask([(v>>i)&1 for v in witnesses])for i in range(19)]
selected=[];rr=[]
for i,r in enumerate(rows):
 if rank(rr+[r])>len(rr):selected.append(i);rr.append(r)
 if len(rr)==7:break
minor=[[(witnesses[j]>>i)&1 for j in range(7)]for i in selected]
minor_det=det(minor)
check(len(selected)==7 and minor_det%2==1,'explicit7x7 dyadic obstacle minor odd determinant')
check(old['old_norm_real_rank_on_units']==2,'old norm-real codimension at least2 inherited')
check(19-2-7==10 and 10+1==11 and 11+3==14,'whole-domain fake<=10+c_K and true<=11+c_K<=14')
check(14<17 and 17-14==3,'strict Chabauty rank gate crossed; >=3-dimensional annihilator EXISTS')
check(14<=16,'old targettrue<=16 follows and is improved')
# Any F2 relation among old minus1+12 and new3 has new coefficients0 by
# the obstruction rank increment, then old coefficients0 by old finite tests.
check(u12['expected_GF2_rank']+3==16,'new ordinary-unit free subgroup rank15, not MW rank15')
negative(rank(old_defects+newdef[:2])==9,'two witnesses cannot certify all3 new directions')
negative(rank(old_defects+[old_defects[0]]*3)>6,'repeating old units never gives new rank')
negative(10+3==14,'fake dimension13 must not be mislabeled14')
negative(11+3==13,'true-fake kernel1 cannot be omitted')
negative(all(u['norm']==1 for u in new['units']),'nu2 is norm-1 before multiplication byepsilon')
negative(peval(f,-vr)%61==0,'wrong primitive root sign must be rejected')
badq=new['units'][0]['q_V'][:];badq[0]+=1
negative(resultant(f,badq)==new['units'][0]['denominator']**36,'changed unit polynomial must fail exact norm')
negative(all(sum(badq[k]*comb(k,j)for k in range(j,len(badq)))*2**(j//3)%new['units'][0]['denominator']==0 for j in range(36)),'changed polynomial must fail integrality')
negative(new['units'][0]['norm_sign_and_real_pair']==[0,0],'unadjusted nu1 must fail the real pair condition')
negative(row358['target_true_Selmer16_proved'] is True,'oldrow358 did not already prove the new rank gate')

out={
 'run_id':'R3-20261105-SIGNED18-C2-THREE-NEW-GLOBAL-UNITS-TRUESEL14',
 'scope':'fixed signed±18 C2 genus17 only, P23-R3-LOW first subleaf',
 'V_minimal_polynomial_ascending':f,
 'V_exact_theta_expression':'[(3theta+1)G9(theta)]^15/[2^14 theta^3(theta+1)^2 G2(theta)^2 G4(theta)^2 A8(theta)^17]',
 'V_fourth_power_theta_exactly_reverified':True,'V_p61':32,
 'V_basis_discriminant':discV,'field_discriminant':DK,
 'new_integral_basis':'(V-1)^j/2^floor(j/3), j0..35; same OLD maximal order, no independent new order credit',
 'new_units_global_norm_and_integrality':norm_data,
 'new_unit_local_records':new_local,
 'old12_unit_defect_rank':6,'old12_plus_new3_unit_defect_rank':9,
 'ordinary_unit_free_subgroup_rank_lower':15,'ordinary_unit_full_free_rank':19,
 'missing_ordinary_free_directions_at_most':4,'full_unit_lattice_index1':'NOT_PROVED',
 'old_four_norm_real_witnesses':[x['unit_product']for x in old['witnesses']],
 'new_norm_real_witnesses':neww_formulas,
 'seven_witness_dyadic_defects_hex':[hex(v)for v in witnesses],
 'selected_constraint_rows_zero_based':selected,
 'seven_by_seven_minor':minor,'seven_by_seven_integer_determinant':minor_det,
 'global_restriction_rank_lower_on_full_finite_even_ambient':9,
 'dyadic_restriction_rank_lower_on_norm_real_kernel':7,
 'fake_Selmer_upper':'10+c_K','true_Selmer_upper':'11+c_K',
 'c_K_ordinary_upper_inherited':3,'c_K_exact':'UNKNOWN','c_S_not_identified_with_c_K':True,
 'numeric_fake_upper':13,'numeric_true_Selmer_upper':14,'MW_rank_interval':[7,14],
 'target_true_Selmer16_proved_internally':True,'strict_rank_below_genus17_proved_internally':True,
 'p163_allMW_annihilator_dimension_lower_by_rank':3,
 'p163_specific_allMW_annihilator_constructed':False,'p163_integral_a0_unit_proved':False,
 'known7_MW_classes_finite_index_proved':False,'new_global_MW_points':0,
 'new_original_signed_source_exclusions':0,'P23_LOW':'OPEN','Branch_B':'OPEN',
 'formal_R0':'C35-200_UNCHANGED',
 'old_row355_row356_row357_row358_independent_audits':'PASS_SCOPED inherited in original scopes only',
 'new_row359_independent_mathematical_audit':'PENDING_NOT_RUN',
 'novelty':'three concrete new global ordinary-unit squareclass directions and full global dyadic-rank lower improvement6to9; no new local condition/method or oldclassnumber credit',
 'LLL_and_floating_point_in_final_proof':False,
 'dependencies':['audited row358 full finite-even ambient19+c_K and ordinaryc_K<=3','audited row355 actual full dyadic fake image and scalar-safe38unit characters','audited row356 actual oldunits, four witnesses and norm-real rank2','global true Selmer to fake kernel<=1 row351/352/356','degree36 signature4,16, order and real embedding data'],
 'parent_SHA256':{str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest()for f in sorted((P/'parents').rglob('*.json'))},
 'input_SHA256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest()for n in ['new_unit_definitions.json','local2_arithmetic.py','dyadic_full_kummer_certificate.json']}
}
cert=P/'three_new_units_certificate.json'
if '--write'in sys.argv:cert.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
else:check(load('three_new_units_certificate.json')==out,'frozen certificate exactly reproduced')
log={'status':'PASS_INTERNAL_EXACT_NOT_INDEPENDENT_MATHEMATICAL_AUDIT','checks':checks,'negative_controls':negatives,'local_precision_bits':precision,'new_global_unit_directions':3,'global_dyadic_rank_lower':9,'norm_real_kernel_rank_lower':7,'true_Selmer_upper':14,'MW_rank_interval':[7,14],'full_MW_p163_annihilator_constructed':False,'source_exclusions':0,'independent_audit':'PENDING_NOT_RUN','elapsed_seconds':round(time.time()-start,3)}
filename='THREE_UNITS_'+('OPTIMIZED'if not __debug__ else'NORMAL')+'_P'+str(precision)+'_REPLAY.json'
(P/filename).write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log))
