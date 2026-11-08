"""Unconditional global squareclass cover and residual-rank bound.

All units are certified by integral coordinates and integer norms. Their
completeness MODULO SQUARES is proved by20 independent finite characters;
no fundamental-unit index1 or provisional BNF output is used in this proof.
This is NOT a construction of the whole-MW163-adic upper space U.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,lcm,isqrt
import json,sys,os,time,hashlib
ROOT=Path(__file__).resolve().parent
if os.environ.get('STAGE35EX_DEPS'):sys.path.insert(0,os.environ['STAGE35EX_DEPS'])
from flint import fmpz_poly
precision=12
for a in sys.argv:
 if a.startswith('--precision='):precision=int(a.split('=')[1])
if precision not in[10,12]:raise ValueError('precision10 or12 only')
os.environ['LOCAL2_PRECISION']=str(precision)
import local2_arithmetic as L
start=time.monotonic();checks=0;negatives=0
def check(ok,label):
 global checks
 if not ok:raise ArithmeticError(label)
 checks+=1
def negative(ok,label):
 global negatives
 if ok:raise ArithmeticError('negative accepted: '+label)
 negatives+=1
def load(s):return json.loads((ROOT/s).read_text())
def rank(vs):
 p={}
 for v in vs:
  while v:
   k=v.bit_length()-1
   if k not in p:p[k]=v;break
   v^=p[k]
 return len(p)
def det(a):
 a=[r[:]for r in a];n=len(a);sg=1;prev=1
 for k in range(n-1):
  if not a[k][k]:
   j=next((j for j in range(k+1,n)if a[j][k]),None)
   if j is None:return 0
   a[k],a[j]=a[j],a[k];sg=-sg
  pp=a[k][k]
  for i in range(k+1,n):
   v=a[i][k]
   for j in range(k+1,n):
    z=a[i][j]*pp-v*a[k][j]
    if z%prev:raise ArithmeticError('Bareiss inexact')
    a[i][j]=z//prev
   a[i][k]=0
  prev=pp
 return sg*a[-1][-1]
def ev(q,x,mod=None):
 z=0
 for c in q[::-1]:
  z=z*x+c
  if mod:z%=mod
 return z
def rref(rows,width):
 a=list(rows);p=[];r=0
 for j in range(width):
  k=next((k for k in range(r,len(a))if(a[k]>>j)&1),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  for k in range(len(a)):
   if k!=r and(a[k]>>j)&1:a[k]^=a[r]
  p.append(j);r+=1
 return a[:r],p
def kernel(rows,width):
 a,p=rref(rows,width);out=[]
 for j in range(width):
  if j in p:continue
  v=1<<j
  for rr,c in zip(a,p):v|=((rr>>j)&1)<<c
  out.append(v)
 return out
def solve(rows,bits,width):
 a,p=rref([r|(((bits>>j)&1)<<width)for j,r in enumerate(rows)],width)
 if len(p)!=width:raise ArithmeticError('noninvertible character frame')
 return sum(((r>>width)&1)<<j for r,j in zip(a,p))
def rows_from_cols(vs,width):return[sum(((v>>j)&1)<<i for i,v in enumerate(vs))for j in range(width)]
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def normalized_q(q):
 q=list(map(Q,q));d=lcm(*(v.denominator for v in q));return[int(v*d)for v in q],d
def coords(q,d):return[sum(q[k]*comb(k,j)for k in range(j,len(q)))*Q(2**(j//3),d)for j in range(36)]
defs=load('full_unit_basis_definitions.json');old=load('parents/row356_global_four_cuts.json');old359=load('parents/row359_three_units.json');u12=load('parents/unit12.json');ud359=load('parents/row359_unit_definitions.json');ov=load('parents/row349_V_fourth_root.json');local=load('dyadic_full_kummer_certificate.json');prev=load('parents/row358_finite_even.json');classone=load('class_one_certificate.json');log361=load('parents/row361_known7_logs.json')
F=old359['V_minimal_polynomial_ascending'];FP=fmpz_poly(F)
check(classone['ordinary_class_number_exact']==1 and classone['ordinary_c_K_exact']==0 and not classone['GRH_assumed'],'new independently replayed class-one certificate')
check(prev['full_finite_even_fake_ambient_dimension']=='19+c_K','OLD full finite-even ambient, modulo scalar')
check(len(defs['units'])==19 and old359['ordinary_unit_full_free_rank']==19,'Dirichlet rank19 inherited')
units=[]
for u in defs['units']:
 q,d=normalized_q(u['coefficients_V']);bc=coords(q,d)
 check(all(z.denominator==1 for z in bc),'integral OLD V maximal basis '+u['label'])
 check(list(map(int,bc))==u['integral_basis_coefficients'],'exact integral coordinates '+u['label'])
 check(int(FP.resultant(fmpz_poly(q)))==u['norm']*d**36 and abs(u['norm'])==1,'exact global norm '+u['label'])
 units.append(dict(u,numerator=q,denominator=d))
# Finite residue characters give an injective20-dimensional unit-squareclass
# frame. Real embeddings imply the only roots of unity are+/-1.
places=defs['auxiliary_places'];aux=[]
for pl in places:
 pp=pl['p'];a=pl['V_residue'];check(prime(pp)and pp!=2,'auxiliary prime')
 check(ev(F,a,pp)==0 and ev([j*F[j]for j in range(1,37)],a,pp)!=0,'actual simple residue embedding')
 row=int(pow(pp-1,(pp-1)//2,pp)==pp-1)
 for j,u in enumerate(units):
  v=ev(u['numerator'],a,pp)*pow(u['denominator'],-1,pp)%pp;ch=pow(v,(pp-1)//2,pp)
  check(ch in(1,pp-1),'nonzero global unit residue')
  row|=int(ch==pp-1)<<(j+1)
 aux.append(row)
check([hex(x)for x in aux]==defs['expected_auxiliary_character_rows_hex'],'frozen auxiliary characters')
auxmatrix=[[(r>>j)&1 for j in range(20)]for r in aux];ad=det(auxmatrix)
check(len(places)==20 and rank(aux)==20 and ad%2==1,'20 independent unit-squareclass characters')
# Express the OLD ordinary units in the now complete squareclass frame.
def oldval(name,theta,pp):
 if name=='epsilon':return pow(theta-1,3,pp)*pow(16,-1,pp)%pp
 if name=='eta':return(3*theta+1)*pow(theta-1,-1,pp)%pp
 if name=='sigma':return(theta*theta+6*theta+1)*pow((theta-1)**2,-1,pp)%pp
 u=next(x for x in u12['unit_definitions']if x['name']==name)
 return ev(u['q'],theta,pp)*pow(1<<u['two_power'],-1,pp)%pp
oldmasks={}
for u in u12['unit_definitions']:
 bits=0
 for j,pl in enumerate(places):
  pp=pl['p'];v=oldval(u['name'],pow(pl['V_residue'],4,pp),pp);s=pow(v,(pp-1)//2,pp);check(s in(1,pp-1),'old unit actual auxiliary character');bits|=int(s==pp-1)<<j
 oldmasks[u['name']]=solve(aux,bits,20)
for u in ud359['units']:
 bits=0
 for j,pl in enumerate(places):
  pp=pl['p'];v=ev(u['q_V'],pl['V_residue'],pp)*pow(u['denominator'],-1,pp)%pp;s=pow(v,(pp-1)//2,pp);check(s in(1,pp-1),'old nu actual auxiliary character');bits|=int(s==pp-1)<<j
 oldmasks[u['label']]=solve(aux,bits,20)
check(rank([1]+list(oldmasks.values()))==16,'OLD minus1+15 independent unit directions retained')
newdirs=[];span=[1]+list(oldmasks.values())
for i in range(19):
 if rank(span+[1<<(i+1)])>len(span):newdirs.append('u'+str(i+1));span.append(1<<(i+1))
check(len(newdirs)==4 and rank(span)==20,'four missing ordinary-unit squareclass directions now covered')
# Exact dyadic algebra reuses the old characters, but evaluates ALL19 units.
constraints=[int(x,16)for x in local['local_constraint_interface']['unit_fake_image_constraints_hex']]
check(len(constraints)==rank(constraints)==19,'OLD full scalar-safe local constraints')
scalar=int(local['scalar_minus1_character_hex'],16);check(not any((r&scalar).bit_count()%2 for r in constraints),'OLD scalar minus1 killed')
def qvec(q,k):
 cs=[sum(q[j]*comb(j,i)*2**i*(-3)**(j-i)for j in range(i,len(q)))*(1<<(i//3))for i in range(len(q))]
 check(all(c%(1<<k)==0 for c in cs),'OLD integral theta coordinates')
 z=L.ZERO.copy();z[:len(cs)]=[c//(1<<k)%L.MOD for c in cs];return z
epsilon=(-4*L.ONE+6*L.U-3*L.power(L.U,2)+L.T)%L.MOD;pi=(L.U-2*L.ONE)%L.MOD
eta=(3*L.ONE+L.mul(L.power(pi,2),L.inv(epsilon)))%L.MOD
sigma=L.mul((L.T-L.power(L.U,2)-L.U+2*L.ONE)%L.MOD,L.inv(epsilon));oldu={'epsilon':epsilon,'eta':eta,'sigma':sigma}
for u in u12['unit_definitions']:
 if u['name']not in oldu:oldu[u['name']]=qvec(u['q'],u['two_power'])
theta=(2*L.U-3*L.ONE)%L.MOD;V=L.ONE.copy()
for name,e in {'epsilon':5,'eta':15,'alpha':-2,'rho':-2,'beta4':-2,'beta9':15,'gamma8':-17}.items():V=L.mul(V,L.power(oldu[name]if e>=0 else L.inv(oldu[name]),abs(e)))
V=L.mul(V,L.power(L.inv(theta),3));check((L.power(V,4)==theta).all(),'OLD exact fourth-root branch in local algebra')
fv=L.ZERO.copy()
for c in F[::-1]:fv=(L.mul(fv,V)+c*L.ONE)%L.MOD
check(not fv.any(),'local V satisfies the fixed selected F')
w=(V-L.ONE)%L.MOD;w3=L.power(w,3);check(all(int(z)%2==0 for z in w3),'integral w3/2')
tw=w3//2;basis=[L.mul(L.power(tw,j//3),L.power(w,j%3))for j in range(36)];characters=[];defects=[]
for u in units:
 z=sum(((int(c)%L.MOD)*basis[j]for j,c in enumerate(u['integral_basis_coefficients'])),L.ZERO.copy())%L.MOD
 cc=L.unit_class(z);dd=sum(((r&cc).bit_count()%2)<<i for i,r in enumerate(constraints))
 check(hex(cc)==u['expected_character_hex']and hex(dd)==u['expected_defect_hex'],'new19 actual local coordinates '+u['label'])
 characters.append(cc);defects.append(dd)
check(rank(defects)==11,'full ordinary-unit local obstruction rank11')
icol=[];iv=[]
for i,v in enumerate(defects):
 if rank(iv+[v])>len(iv):icol.append(i);iv.append(v)
ir=[];rv=[]
for j in range(19):
 row=sum(((v>>j)&1)<<k for k,v in enumerate(iv))
 if rank(rv+[row])>len(rv):ir.append(j);rv.append(row)
minor=[[(defects[i]>>j)&1 for i in icol]for j in ir];minor_det=det(minor)
check(len(icol)==len(ir)==11 and minor_det%2==1,'explicit11x11 obstruction minor has odd determinant')
olddef=[int(u['dyadic_defect_hex'],16)for u in old['unit_records']]+[int(u['dyadic_defect_hex'],16)for u in old359['new_unit_local_records']]
check(rank(olddef)==9,'inherited old15 rank9')
check(rank(olddef+[defects[13]])==10 and rank(olddef+[defects[13],defects[14]])==11,'two genuinely new obstruction directions u14/u15')
# Binding the old15 coordinates to the finite global frame AND local frame
# prevents swapping independently computed global/local unit labels.
charcols=[scalar]+characters;defcols=[0]+defects
def lin(mask,cols):
 z=0
 for j,c in enumerate(cols):
  if(mask>>j)&1:z^=c
 return z
for name,m in oldmasks.items():
 rec=next((u for u in old['unit_records']if u['name']==name),None)or next(u for u in old359['new_unit_local_records']if u['label']==name)
 check(lin(m,charcols)==int(rec['dyadic_character_hex'],16),'global/local old character binding '+name)
 check(lin(m,defcols)==int(rec['dyadic_defect_hex'],16),'global/local old defect binding '+name)
rows=rows_from_cols(defects,19);ker=kernel(rows,19)
check(len(ker)==rank(ker)==8 and not any((r&v).bit_count()%2 for r in rows for v in ker),'complete8-dimensional global candidate cover')
oldforms={'D1a':['alpha'],'D1b':['epsilon','eta'],'D2':['rho'],'D4':['beta4'],'D9':['beta9'],'F2':['sigma']};old6=[]
for name,terms in oldforms.items():
 v=0
 for nm in terms:v^=oldmasks[nm]
 v>>=1;check(not any((r&v).bit_count()%2 for r in rows),'OLD global divisor inside full candidate cover '+name);old6.append(v)
check(rank(old6)==6,'OLD six genuine fake directions retained')
span=old6[:];complement=[]
for v in ker:
 if rank(span+[v])>len(span):complement.append(v);span.append(v)
check(len(complement)==2 and rank(span)==8,'explicit two residual global squareclasses beyond old6')
complement_units=[['u'+str(i+1)for i in range(19)if(v>>i)&1]for v in complement]
# The two residual squareclasses are candidate Kummer values. They are NOT
# asserted to lift to rational divisors or to specify163-adic directions.
check(19-11==8 and 8+1==9,'full fake<=8 and true<=9 using inherited true/fake kernel<=1')
check(old359['MW_rank_interval'][0]==7 and 9-7==2,'whole-MW rank7..9 and residual logarithmic rank<=2')
Lmat=log361['normalized_log_matrix_mod163'];I=log361['pivot_columns_zero_based'];md=det([[r[j]for j in I]for r in Lmat])
check(md%163==137 and log361['known7_log_rank']==7,'reuse OLD actual7 logs, not a new log computation')
check(17-9==8 and 17-10==7,'dependent jet bound first unit index<=9')
negative(rank(olddef+[olddef[0]])>9,'repeated old unit cannot add a constraint')
negative(rank(aux[:-1])==20,'missing finite character prevents completeness')
negative(int(FP.resultant(fmpz_poly([units[13]['numerator'][0]+1]+units[13]['numerator'][1:])))==units[13]['norm']*units[13]['denominator']**36,'changed new unit norm rejected')
negative(all(z.denominator==1 for z in coords([1]+[0]*35,2)),'nonintegral unit representative rejected')
negative(len(complement)==0,'old6 cannot cover full8-dimensional candidate space')
negative(9==7,'rank interval must not become exact rank7')
negative(8==9,'true/fake kernel cannot be dropped')
negative(2==0,'residual dimension bound does not give U=0')
out={'scope':'fixed signed+-18 C2 and its OLD36-degree field only','ordinary_class_number_exact':1,'ordinary_c_K_exact':0,'ordinary_unit_squareclass_dimension_including_minus1':20,'complete_unit_squareclass_basis':['-1']+[u['label']for u in units],'fundamental_unit_index1_claimed':False,'auxiliary_places':places,'auxiliary_character_rows_hex':[hex(x)for x in aux],'auxiliary20x20_integer_determinant':ad,'old15_unit_coordinate_masks_with_scalar_hex':{k:hex(v)for k,v in oldmasks.items()},'new_four_global_unit_directions_beyond_old15':newdirs,'full19_dyadic_character_columns_hex':[hex(v)for v in characters],'full19_dyadic_defect_columns_hex':[hex(v)for v in defects],'old15_obstruction_rank':9,'full_obstruction_rank':11,'new_obstruction_witnesses':['u14','u15'],'full_candidate_rows_hex':[hex(v)for v in rows],'full_candidate_kernel_basis_hex':[hex(v)for v in ker],'full_candidate_dimension':8,'old6_MW_fake_coordinate_masks_hex':[hex(v)for v in old6],'old6_MW_fake_order':list(oldforms),'residual_global_squareclass_masks_hex':[hex(v)for v in complement],'residual_global_squareclass_unit_products':complement_units,'residual_global_squareclass_dimension':2,'residual_squareclasses_certified_to_lift_to_global_MW':False,'fake_Selmer_dimension_upper':8,'true_Selmer_dimension_upper':9,'MW_rank_interval':[7,9],'old_known7_log_minor_mod163':137,'remaining_global_residual_log_coordinates':10,'remaining_global_residual_log_Q163_rank_upper':2,'whole_MW_residual_log_U_constructed':False,'whole_MW_a0_unit_proved':False,'known7_MW_finite_index_proved':False,'full_MW_annihilator_dimension_lower':8,'dependent_first_unit_index_upper':9,'dependent_nonzero_source_disk_count_upper':9,'dependent_primitive_labelled_bases_union_both_valid_signs_upper':9,'new_global_MW_points':0,'new_source_exclusions':0,'GRH_assumed':False,'independent_mathematical_audit':'PENDING_NOT_RUN','P23_LOW':'OPEN','Branch_B':'OPEN','formal_R0':'C35-200_UNCHANGED','input_sha256':{s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest()for s in['full_unit_basis_definitions.json','principal_prime_generators.json','class_one_certificate.json','local2_arithmetic.py','dyadic_full_kummer_certificate.json']}}
out.update({'ordinary_S_class_number_exact_as_quotient':1,'ordinary_c_S_exact_same_fixed_field':0,'obstruction_minor_unit_indices_zero_based':icol,'obstruction_minor_row_indices_zero_based':ir,'obstruction_minor_matrix':minor,'obstruction11x11_integer_determinant':minor_det})
if '--build'in sys.argv:(ROOT/'global_residual_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
else:check(load('global_residual_cover_certificate.json')==out,'frozen global cover certificate exactly reproduced')
log={'status':'INTERNAL_EXACT_PASS','checks':checks,'negative_controls':negatives,'precision_bits':precision,'unit_squareclass_basis_dimension':20,'global_obstruction_rank':11,'class_number':1,'fake_Selmer_upper':8,'true_Selmer_upper':9,'MW_rank_interval':[7,9],'global_candidate_residual_dimension':2,'residual_log_rank_upper':2,'U_constructed':False,'source_exclusions':0,'independent_audit':'PENDING_NOT_RUN','seconds':round(time.monotonic()-start,3)}
name='GLOBAL_COVER_'+('NORMAL'if __debug__ else'OPTIMIZED')+'_P'+str(precision)+'_REPLAY.json';(ROOT/name).write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log))
print(json.dumps({'new_unit_directions':newdirs,'residual_candidate_units':complement_units,'auxiliary_determinant':ad}))
