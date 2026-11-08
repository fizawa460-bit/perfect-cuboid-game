"""Exact global witness restrictions for fixed C2; not a full global basis.
Uses audited row355 local coordinates and locked historical global units.
No assert statements: normal and -O enforce identical mathematical checks.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,sys,hashlib,time
import local2_arithmetic as L
sys.path.insert(0,str(L.ROOT/'parents'))
import verify_odd_bad_rational_kummer_stdlib as ODD

ROOT=Path(__file__).resolve().parent
P=ROOT/'parents/PARENT_ROW352_INFINITY_RANK7'
UC=json.loads((P/'unit12_certificate.json').read_text())
REAL=json.loads((P/'row350_certificate.json').read_text())
CERT=json.loads((ROOT/'dyadic_full_kummer_certificate.json').read_text())
OLD6=json.loads((ROOT/'parents/signed18_genus17_rank6_certificate.json').read_text())
ODDC=json.loads((ROOT/'parents/r3_07_odd_bad_local_images_certificate.json').read_text())
DIMS=json.loads((ROOT/'parents/signed18_c2_true_local_kummer_dimensions_certificate.json').read_text())
GLOB=json.loads((P/'signed18_c2_global_sunits_preflight_certificate.json').read_text())
BRIDGE=json.loads((P/'true_fake_bridge_351_certificate.json').read_text())
start=time.time();checks=0;negatives=0

def check(ok,label):
 global checks
 if not ok:raise RuntimeError(label)
 checks+=1

def negative(ok,label):
 global negatives
 if ok:raise RuntimeError('unrejected negative control: '+label)
 negatives+=1

def rr(xs):
 # Pure Python highest-pivot rank, independent of the arithmetic module.
 piv={}
 for a in xs:
  x=int(a)
  for k in sorted(piv,reverse=True):
   if (x>>k)&1:x^=piv[k]
  if x:piv[x.bit_length()-1]=x
 return len(piv)

def annihilator(xs,width):
 a=[[(v>>i)&1 for i in range(width)]for v in xs];r=0;piv=[]
 for j in range(width):
  k=next((k for k in range(r,len(a))if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  for k in range(len(a)):
   if k!=r and a[k][j]:a[k]=[x^y for x,y in zip(a[k],a[r])]
  piv.append(j);r+=1
 out=[]
 for j in range(width):
  if j not in piv:
   x=1<<j
   for k,c in enumerate(piv):x|=a[k][j]<<c
   out.append(x)
 check(rr(out)+rr(xs)==width,'annihilator rank-nullity')
 check(not any((h&v).bit_count()%2 for h in out for v in xs),'annihilator orthogonality')
 return out

def poly_mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def det(M):
 a=[row[:]for row in M];n=len(a);sign=1;prev=1
 if not n:return 1
 for k in range(n-1):
  if not a[k][k]:
   j=next((j for j in range(k+1,n)if a[j][k]),None)
   if j is None:return 0
   a[k],a[j]=a[j],a[k];sign=-sign
  piv=a[k][k]
  for i in range(k+1,n):
   v=a[i][k]
   for j in range(k+1,n):
    num=a[i][j]*piv-v*a[k][j]
    if num%prev:raise RuntimeError('nonexact Bareiss division')
    a[i][j]=num//prev
   a[i][k]=0
  prev=piv
 return sign*a[-1][-1]

def resultant(f,g):
 m=len(f)-1;n=len(g)-1
 if not n:return g[0]**m
 a=[[0]*(m+n)for _ in range(m+n)]
 for i in range(n):a[i][i:i+m+1]=list(reversed(f))
 for i in range(m):a[n+i][i:i+n+1]=list(reversed(g))
 return det(a)

def rational_definition(d):
 n=d['name']
 if n=='epsilon':return poly_mul(poly_mul([-1,1],[-1,1]),[-1,1]),[16]
 if n=='eta':return [1,3],[-1,1]
 if n=='sigma':return [1,6,1],poly_mul([-1,1],[-1,1])
 return d['q'],[1<<d['two_power']]

def qvec(q,k):
 cc=[sum(q[j]*comb(j,i)*2**i*(-3)**(j-i)for j in range(i,len(q)))*(1<<(i//3))for i in range(len(q))]
 check(all(c%(1<<k)==0 for c in cc),'integral maximal-order coordinates')
 a=L.ZERO.copy();a[:len(cc)]=[c//(1<<k)%L.MOD for c in cc];return a

def ev(q,x):
 a=Q(0)
 for c in reversed(q):a=a*x+c
 return a

def interval(q,l,r):
 lo=hi=Q(q[-1])
 for c in reversed(q[:-1]):
  z=[lo*l,lo*r,hi*l,hi*r];lo=min(z)+c;hi=max(z)+c
 return lo,hi

intervals=[(Q(*l),Q(*r))for l,r in REAL['rational_root_intervals']]

def sign_q(q,l,r):
 for _ in range(80):
  lo,hi=interval(q,l,r)
  if lo>0 or hi<0:return int(hi<0)
  mid=(l+r)/2
  if ev(L.H,l)*ev(L.H,mid)<0:r=mid
  else:l=mid
 raise RuntimeError('unresolved rational interval sign')

check(L.PREC==8,'frozen audited precision8')
check(L.H==UC['h2_coefficients_ascending']==OLD6['h2_coefficients_ascending']==REAL['h2_coefficients_ascending'],'same fixed h2')
for fn,sha in UC['parent_sha256'].items():check(hashlib.sha256((P/fn).read_bytes()).hexdigest()==sha,'unit parent SHA')
for fn,sha in CERT['parent_sha256'].items():check(hashlib.sha256((ROOT/'parents'/fn).read_bytes()).hexdigest()==sha,'local parent SHA')
check(GLOB['fake_ambient_dim_expression']=='34+c_S','full symbolic ambient bound inherited')
check(REAL['fake_real_and_square_norm_dimension_upper_expression']=='31+c_S','old norm-real upper inherited')
check(BRIDGE['H1_J2_to_H1_M_kernel_F2_dimension']==1,'true to fake kernel1 inherited')
for l,r in intervals:check(l<r and ev(L.H,l)*ev(L.H,r)<0,'locked real root isolator')

pi=(L.U-2*L.ONE)%L.MOD
epsilon=(-4*L.ONE+6*L.U-3*L.power(L.U,2)+L.T)%L.MOD
check(L.np.array_equal(L.power(pi,3),2*epsilon%L.MOD),'pi^3=2epsilon')
eta=(3*L.ONE+L.mul(L.power(pi,2),L.inv(epsilon)))%L.MOD
sigma=L.mul((L.T-L.power(L.U,2)-L.U+2*L.ONE)%L.MOD,L.inv(epsilon))
# Exact polynomial numerators make the two division-free identities unambiguous.
check(poly_mul([3],[-4,6,-3,Q(1,2)])==[-12,18,-9,Q(3,2)],'eta exact numerator first term')
eta_n=[-8,14,-8,Q(3,2)] # (3u-4)*pi^2/2 = 3epsilon+pi^2
check([3*x+y for x,y in zip([-4,6,-3,Q(1,2)],[4,-4,1,0])]==eta_n,'eta exact rational identity')
check(poly_mul([-2,1],[-2,0,1])==[4,-2,-2,1],'sigma numerator pi*(u^2-2)')
constraints=[int(x,16)for x in CERT['local_constraint_interface']['unit_fake_image_constraints_hex']]
check(len(constraints)==rr(constraints)==19,'audited19 unit constraints')
chars=[int(CERT['scalar_minus1_character_hex'],16)]+[int(r['character_hex'],16)for r in CERT['selected_fake_basis']]
check(rr(chars)==19 and not any((h&v).bit_count()%2 for h in constraints for v in chars),'complete local subspace and constraints')

records=[];vectors={}
for d in UC['unit_definitions']:
 n=d['name'];num,den=rational_definition(d)
 nn,nd=resultant(L.H,num),resultant(L.H,den)
 check(nd!=0 and nn==d['norm']*nd,'exact global unit norm '+n)
 a={'epsilon':epsilon,'eta':eta,'sigma':sigma}.get(n)
 if a is None:a=qvec(d['q'],d['two_power'])
 check(all(L.pgf_mod(L.residue(a),f)!=0 for f in L.FACTORS),'unit at both dyadic factors '+n)
 c=L.unit_class(a);vectors[n]=a
 bs=[sign_q(num,l,r)^sign_q(den,l,r)for l,r in intervals]
 check((sum(bs)%2)==int(d['norm']==-1),'norm and real signs '+n)
 defect=sum(((h&c).bit_count()%2)<<j for j,h in enumerate(constraints))
 records.append({'name':n,'norm':d['norm'],'unit_basis_mod256':list(map(int,a)),'dyadic_character_hex':hex(c),'dyadic_defect_hex':hex(defect),'real_sign_bits':bs,'norm_sign_and_first_real_pair':[int(d['norm']==-1),bs[0]^bs[1]]})
byname={r['name']:r for r in records};names=[r['name']for r in records]
q2cols=[int(r['dyadic_defect_hex'],16)for r in records]
q2rows=[sum(((x>>j)&1)<<i for i,x in enumerate(q2cols))for j in range(19)]
oldrows=[sum(r['norm_sign_and_first_real_pair'][j]<<i for i,r in enumerate(records))for j in range(2)]
check(rr(q2cols)==rr(q2rows)==6,'rank6 on known12 global units')
check(rr(oldrows)==2 and rr(oldrows+q2rows)==6,'4 additional constraints on old norm-real kernel')

# Binding the six old genuine images directly to their original G(theta).
old_records={r['old_class']:r for r in CERT['selected_fake_basis']if r['kind']=='old_global_divisor'}
old_unit_masks=[]
identity_units={'D1a':['alpha'],'D1b':['epsilon','eta'],'D2':['rho'],'D4':['beta4'],'D9':['beta9'],'F2':['sigma']}
for n,g in zip(OLD6['class_order'],OLD6['class_G_coefficients_ascending']):
 if n=='D1b':
  check(g==[1,3],'old D1b input')
  a=(3*L.T-2*L.power(L.U,2))%L.MOD
  check(poly_mul([0,0,Q(1,4)],[-8,6])==[0,0,-2,Q(3,2)],'D1b square normalization exact')
 elif n=='F2':
  check(g==[1,6,1],'old F2 input')
  a=L.mul((L.T-L.U)%L.MOD,L.inv(L.T))
  check([sum(g[j]*comb(j,i)*2**i*(-3)**(j-i)for j in range(i,len(g)))for i in range(len(g))]==[-8,0,4],'F2 G(theta) exact transform')
 else:
  cc=[sum(g[j]*comb(j,i)*2**i*(-3)**(j-i)for j in range(i,len(g)))*(1<<(i//3))for i in range(len(g))]
  den=min(abs(c)&-abs(c)for c in cc if c)
  a=L.ZERO.copy();a[:len(cc)]=[c//den%L.MOD for c in cc]
 check(list(map(int,a))==old_records[n]['unit_basis_mod256'],'old G bound to stored unit '+n)
 c=L.unit_class(a);mask=0;uc=0
 for nm in identity_units[n]:mask^=1<<names.index(nm);uc^=int(byname[nm]['dyadic_character_hex'],16)
 check((uc^c)in (0,int(CERT['scalar_minus1_character_hex'],16)),'old divisor unit product up to scalar '+n)
 old_unit_masks.append(mask)
 check(not any((mask&row).bit_count()%2 for row in q2rows),'old genuine class in Q2 kernel')
check(rr(old_unit_masks)==6,'six old divisor coefficient masks independent')
check(rr(annihilator(q2rows,12)+old_unit_masks)==6,'known unit Q2 kernel exactly old6 span')

# All five odd places: unit residue map, modulo the audited full image+scalar.
odd_data=[];all_odd_rows=[]
for item,loc in zip(ODDC['odd_bad_primes'],DIMS['local_primes_odd']):
 p=item['p'];check(p==loc['p'],'odd place order')
 fs=[f['coefficients_ascending_mod_p']for f in loc['factors']]
 bcols=[sum(bit<<j for j,bit in enumerate(b))for b in item['unit_residue_quadratic_character_bits']]
 scalar=sum(bit<<j for j,bit in enumerate(item['rational_scalar_bit_vector']))
 if item['additional_local_point_X4']:
  bcols.append(sum(bit<<j for j,bit in enumerate(item['additional_local_point_X4']['quadratic_character_bits'])))
 ann=annihilator(bcols+[scalar],len(fs));cs=[]
 for d in UC['unit_definitions']:
  num,den=rational_definition(d);bits=[]
  for f in fs:
   nr=ODD.resultant(f,num,p);dr=ODD.resultant(f,den,p)
   check(nr==ODD.field_norm_by_matrix(f,num,p) and dr==ODD.field_norm_by_matrix(f,den,p),'odd resultant/matrix norm '+d['name'])
   check(nr%p!=0 and dr%p!=0,'odd residue unit')
   v=nr*pow(dr,-1,p)%p;leg=pow(v,(p-1)//2,p)
   check(leg in (1,p-1),'odd Legendre')
   bits.append(int(leg==p-1))
  cs.append(sum(bit<<j for j,bit in enumerate(bits)))
 rows=[sum(((a&c).bit_count()%2)<<i for i,c in enumerate(cs))for a in ann]
 check(not any((m&r).bit_count()%2 for m in old_unit_masks for r in rows),'old global images satisfy odd local conditions')
 all_odd_rows+=rows
 odd_data.append({'p':p,'unit_residue_characters_hex':[hex(c)for c in cs],'annihilators_hex':[hex(a)for a in ann],'constraint_rows_on_12units_hex':[hex(r)for r in rows],'restricted_rank':rr(rows)})
check(rr(q2rows+all_odd_rows+oldrows)==6,'odd+real add no rank on this already exhausted known subgroup')

witness_names=[['epsilon','gamma8','gamma6'],['gamma8','gamma12'],['tau3'],['epsilon','upsilon3']]
witnesses=[]
for w in witness_names:
 mask=sum(1<<names.index(n)for n in w);a=L.ONE.copy();xc=0;xd=0
 for n in w:
  a=L.mul(a,vectors[n]);xc^=int(byname[n]['dyadic_character_hex'],16);xd^=int(byname[n]['dyadic_defect_hex'],16)
 check(L.unit_class(a)==xc,'product characteristic linearity')
 check(all(not((mask&r).bit_count()%2)for r in oldrows),'witness belongs to global norm-real candidate')
 check(sum(((h&xc).bit_count()%2)<<j for j,h in enumerate(constraints))==xd,'product defect')
 witnesses.append({'unit_product':w,'unit_exponent_mask_hex':hex(mask),'dyadic_character_hex':hex(xc),'dyadic_defect_hex':hex(xd),'global_norm':1,'real_pair_conditions_zero':True})
wcols=[int(w['dyadic_defect_hex'],16)for w in witnesses]
check(rr(wcols)==4,'four independent global defect witnesses')
selected=[];minorrows=[]
for j in range(19):
 row=sum(((c>>j)&1)<<i for i,c in enumerate(wcols))
 if rr(minorrows+[row])>len(minorrows):selected.append(j);minorrows.append(row)
 if len(selected)==4:break
minor=[[(c>>j)&1 for c in wcols]for j in selected]
check(det(minor)%2==1,'explicit4x4 minor odd determinant')
for i in range(4):negative(rr(wcols[:i]+wcols[i+1:])==4,'a witness is required')
negative(rr([wcols[0],wcols[1],wcols[2],wcols[2]])==4,'duplicated witness not accepted')
# Direct combinatorial strengthening recommended by row355 audit.
fixed=anti=0
for m in range(1<<12):
 x=[(m>>i)&1 for i in range(12)];y=[0]*12
 for cy in [list(range(4)),list(range(4,12))]:
  for i,j in enumerate(cy):y[cy[(i+1)%len(cy)]]=x[j]
 if x==y or all(a!=b for a,b in zip(x,y)):
  check(3*sum(x)%2==0,'even parity including complement-swapped branch subsets')
  if x==y:fixed+=1
  else:anti+=1
check((fixed,anti)==(4,4),'fixed+complement invariant subset enumeration')

parents=['dyadic_full_kummer_certificate.json','parents/r3_07_odd_bad_local_images_certificate.json','parents/signed18_genus17_rank6_certificate.json','parents/PARENT_ROW352_INFINITY_RANK7/unit12_certificate.json','parents/PARENT_ROW352_INFINITY_RANK7/row350_certificate.json','parents/PARENT_ROW352_INFINITY_RANK7/true_fake_bridge_351_certificate.json','parents/PARENT_ROW352_INFINITY_RANK7/signed18_c2_global_sunits_preflight_certificate.json']
out={'run_id':'R3-20261104-SIGNED18-C2-GLOBAL-LOCAL-RESTRICTION-FOUR-NEW-CUTS','scope':'fixed C2 only; known global subspace is NOT full global upper','unit_order':names,'unit_records':records,'dyadic_constraint_rows_on_12units_hex':[hex(x)for x in q2rows],'old_norm_real_rows_hex':[hex(x)for x in oldrows],'known_unit_local_defect_rank':6,'old_norm_real_rank_on_units':2,'additional_independent_global_restrictions':4,'old_six_kernel_unit_masks_hex':[hex(x)for x in old_unit_masks],'kernel_of_all_current_local_conditions_on_known_units':'exactly span of old six genuine global fake divisor images','odd_places':odd_data,'witnesses':witnesses,'witness_minor_constraint_indices_zero_based':selected,'witness_minor_matrix':minor,'witness_minor_integer_determinant':det(minor),'previous_full_fake_candidate_bound':'31+c_S','new_full_fake_candidate_bound_after_local2':'27+c_S','true_selmer_to_fake_kernel_bound':1,'new_true_Selmer_upper':'28+c_S','new_MW_rank_upper':'28+c_S','c_S':'UNKNOWN','numeric_global_Selmer_upper16_proved':False,'full_global_squareclass_basis_constructed':False,'full_global_restriction_rank_computed':False,'global_restriction_rank_on_old_norm_real_candidate_lower_bound':4,'remaining_sufficient_global_restriction_rank_for_target16':'at least 12+c0 more, after proving c_S<=c0','rank_lower_retained':7,'new_global_MW_generators':0,'new_source_exclusions':0,'P23_LOW':'OPEN','Branch_B':'OPEN','R0_formal':'C35-200_UNCHANGED','independent_math_audit_this_new_result':'PENDING_NOT_RUN','row355_audit_adopted':'PASS_SCOPED; fixed local result only','parent_SHA256':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest()for n in parents}}
certpath=ROOT/'global_local_restriction_certificate.json'
if '--write' in sys.argv:certpath.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
else:check(json.loads(certpath.read_text())==out,'frozen new certificate matches exact recomputation')
log={'status':'PASS_INTERNAL_EXACT_NOT_INDEPENDENT_MATH_AUDIT','checks':checks,'negative_controls':negatives,'known_unit_dyadic_defect_rank':6,'old_norm_real_rank':2,'additional_global_restriction_rank_lower_bound':4,'all_known_local_conditions_rank':6,'minor_rows_zero_based':selected,'minor_matrix':minor,'minor_integer_determinant':det(minor),'fake_upper':'27+c_S','true_upper':'28+c_S','c_S_unknown':True,'numeric_upper16':False,'source_exclusions':0,'elapsed_seconds':round(time.time()-start,3)}
target=ROOT/('GLOBAL_RESTRICTION_OPTIMIZED_REPLAY.json'if not __debug__ else 'GLOBAL_RESTRICTION_NORMAL_REPLAY.json')
target.write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log))
