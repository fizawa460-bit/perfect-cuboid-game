#!/usr/bin/env python3
import json,math,runpy,subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EP='stages/stage36/36-09EP/rho-sel2-support-rank-criterion-preflight.json'
EY='stages/stage36/36-09EY/rho-radical-refinement-rank-compression-preflight.json'
EZ='stages/stage36/36-09EZ/rho-core-nullity-controlled-radical-search-preflight.json'
EZV='stages/stage36/verify_stage36_36_09EZ.py'
EXV='stages/stage36/verify_stage36_36_09EX.py'
EH='stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-preflight.json'
EK='stages/stage36/36-09EK/rho-sel2-literal-orbit-closure-preflight.json'
SOURCE='stages/stage36/36-09FA/rho-residual-core-partial-legendre-chart-source-lock.md'
CERT='stages/stage36/36-09FA/rho-residual-core-partial-legendre-chart-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EP:'4e3f103a3711220f1d5f6475f1fcff345b31ae7a',
 EY:'dbad704b6e05eb0a08ff33b1794436cab7f94fc6',
 EZ:'873eef8d82b89ecefe3e331b3038df9bff18fec0',
 EZV:'3a79a0b663727d57c2f2a6ec849e5bfc82af6188',
 EXV:'3adbd3fe00b2e4c85261862f8e949a5c8af09c03',
 EH:'d95bf71f3cbed1d3fd12eaa0d235d2aa83539d37',
 EK:'f6af11a0f7fd8a303531b2a587b7446c382a84c5',
 SOURCE:'de142ff3bf00298d39bb683c39e15fc415f2beae',
 CERT:'499ac146f0d453a7a7abee565e4dcfb4aec982ed',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)

ep=load(EP);ey=load(EY);ez=load(EZ);eh=load(EH);ek=load(EK);c=load(CERT)
assert ep['support_matrix']['criterion_necessary_and_sufficient'] is True
assert ey['leaf_core_theorem']['sel2_identity']=='dim_F2 Sel^2(E_rho,p/Q)=nullity_F2(H)'
assert ez['registry_impact']['provisional_count']==192
assert eh['rational_4torsion_test']['order4_iff']=='8h in Q^2 or -8h in Q^2'
assert ek['literal_orbit_theorem']['positive_literal_orbit_complete'] is True
assert c['entry_authority']['v286_exact_head']=='5c2224442466ad5990866018cfc1f92deb048c62'
assert c['entry_authority']['v286_exact_head_ci']=='34414312546/102675622532'
assert c['entry_authority']['36_09FA_entry_allowed'] is True

exns=runpy.run_path(str(ROOT/EXV)); ezns=runpy.run_path(str(ROOT/EZV))
rank=exns['rank'];matrix_from_pattern=exns['matrix_from_pattern'];legbit=exns['legbit']
factor=ezns['factor'];is_prime=ezns['is_prime']
previous=set(ezns['prev'])|set(ezns['seen']); assert len(previous)==192

def rref(vs):
 rows=[list(map(int,v)) for v in vs if any(v)]
 if not rows:return ()
 n=len(rows[0]);rr=0
 for j in range(n):
  q=next((i for i in range(rr,len(rows)) if rows[i][j]),None)
  if q is None:continue
  rows[rr],rows[q]=rows[q],rows[rr]
  for i in range(len(rows)):
   if i!=rr and rows[i][j]:rows[i]=[x^y for x,y in zip(rows[i],rows[rr])]
  rr+=1
  if rr==len(rows):break
 return tuple(tuple(x) for x in rows[:rr])
def nullspace(rows,n):
 a=[list(map(int,r)) for r in rows if any(r)];piv=[];rr=0
 for j in range(n):
  q=next((i for i in range(rr,len(a)) if a[i][j]),None)
  if q is None:continue
  a[rr],a[q]=a[q],a[rr]
  for i in range(len(a)):
   if i!=rr and a[i][j]:a[i]=[x^y for x,y in zip(a[i],a[rr])]
  piv.append(j);rr+=1
  if rr==len(a):break
 free=[j for j in range(n) if j not in piv];out=[]
 for f in free:
  x=[0]*n;x[f]=1
  for i,p in reversed(list(enumerate(piv))):x[p]=sum(a[i][j]&x[j] for j in free)&1
  out.append(tuple(x))
 return out

REAL=((0,1),)
W2S=((0,0,1,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
ODD={('D',None):((0,0,1,0),(0,0,0,1)),('P',1):((1,0,1,0),(0,1,0,1)),('P',7):((0,1,0,0),(0,0,0,1)),('Q',1):((1,0,0,0),(0,1,0,0)),('Q',7):((0,1,0,0),(0,0,0,1))}
ZERO=(0,0);ONE=(0,1)
def exxor(a,b):return (a[0]^b[0],a[1]^b[1])
def exsum(ts):
 z=ZERO
 for t in ts:z=exxor(z,t)
 return z
ATTRS=[('D',3),('D',3),('D',5),('D',7),('P',1),('P',1),('P',7),('Q',1),('Q',7),('Q',7)]
def symbolic_matrix():
 pairs={};v=0
 for i in range(len(ATTRS)):
  for j in range(i+1,len(ATTRS)):pairs[(i,j)]=v;v+=1
 def L(i,j):
  if i==j:return ZERO
  if i<j:return (1<<pairs[(i,j)],0)
  rec=1 if ATTRS[i][1] in (3,7) and ATTRS[j][1] in (3,7) else 0
  return (1<<pairs[(j,i)],rec)
 G=[-1,2]+list(range(len(ATTRS)));rows=[]
 def add(W,dl,loc):
  for z in nullspace(W,2*dl):
   z1=z[:dl];z2=z[dl:];row=[ZERO]*(2*len(G))
   for j,bits in enumerate(loc):
    row[j]=exsum(bits[k] for k,x in enumerate(z1) if x)
    row[len(G)+j]=exsum(bits[k] for k,x in enumerate(z2) if x)
   rows.append(row)
 add(REAL,1,[[ONE],[ZERO]]+[[ZERO]]*len(ATTRS))
 q2=[[ZERO,ONE,ZERO],[ONE,ZERO,ZERO]]+[[ZERO,ONE if m8 in (3,7) else ZERO,ONE if m8 in (3,5) else ZERO] for _,m8 in ATTRS]
 add(W2S,3,q2)
 for i,(lab,m8) in enumerate(ATTRS):
  key=(lab,m8) if lab in ('P','Q') else ('D',None)
  loc=[[ZERO,ONE if m8 in (3,7) else ZERO],[ZERO,ONE if m8 in (3,5) else ZERO]]
  for j in range(len(ATTRS)):loc.append([ONE,ZERO] if i==j else [ZERO,L(i,j)])
  add(ODD[key],2,loc)
 return rows,pairs
SM,PAIRS=symbolic_matrix(); assert len(PAIRS)==45 and len(SM)==24 and len(SM[0])==24

def ev(e,a):
 mask,z=e
 for k,b in enumerate(a):
  if b and ((mask>>k)&1):z^=1
 return z
def eval_matrix(a):return [[ev(e,a) for e in row] for row in SM]
def assignment(primes):
 out=[0]*45
 for (i,j),k in PAIRS.items():out[k]=legbit(primes[j],primes[i])
 return out

def peel(A):
 A=[list(r) for r in A];rids=list(range(len(A)));cids=list(range(len(A[0])));trace=[]
 while A and A[0]:
  nr=len(A);nc=len(A[0]);pick=None;typ=None
  for i in range(nr):
   js=[j for j in range(nc) if A[i][j]]
   if len(js)==1:pick=(i,js[0]);typ='row';break
  if pick is None:
   for j in range(nc):
    ii=[i for i in range(nr) if A[i][j]]
    if len(ii)==1:pick=(ii[0],j);typ='col';break
  if pick is None:break
  i,j=pick;trace.append((typ,rids[i],cids[j]))
  A=[[A[r][q] for q in range(nc) if q!=j] for r in range(nr) if r!=i]
  rids.pop(i);cids.pop(j)
 return trace,A,rids,cids

def leaf_equation_rref(trace):
 rids=list(range(24));cids=list(range(24));eq=[]
 for typ,rid,cid in trace:
  if typ=='row':
   for cj in cids:eq.append((SM[rid][cj],1 if cj==cid else 0))
  else:
   for ri in rids:eq.append((SM[ri][cid],1 if ri==rid else 0))
  rids.remove(rid);cids.remove(cid)
 for ri in rids:
  for cj in cids:eq.append((SM[ri][cj],0))
 mat=[]
 for (mask,const),target in eq:
  rhs=const^target
  if mask==0:assert rhs==0
  else:mat.append(tuple((mask>>k)&1 for k in range(45))+(rhs,))
 return rref(mat)

def expected_chart(rows):
 out=[]
 for i,j,rhs in rows:
  v=[0]*46;v[PAIRS[(i,j)]]=1;v[-1]=rhs;out.append(tuple(v))
 return rref(out)
CHART_A=[(0,4,1),(0,5,0),(1,4,0),(1,5,0),(1,7,1),(2,5,1)]
CHART_B=[(0,4,1),(0,5,0),(1,5,1),(3,4,0),(3,5,0),(3,6,0),(3,7,1),(3,8,0),(3,9,0)]

def prime_support(u,fm=None):
 K=729;b=2*u+K;q=4*u+K;s=(8*u*u-K*K)//7;t=(8*u*u+8*K*u+K*K)//41
 vals={'u':u,'b':b,'q':q,'s':s,'t':t}
 if fm is None:ff={k:factor(v,[]) for k,v in vals.items()}
 else:
  ff={k:[] for k in vals}
  for k,d in fm.items():
   z=1
   for ps,e in d.items():
    p=int(ps);assert is_prime(p);ff[k]+=[p]*e;z*=p**e
   assert z==vals[k],(u,k,z,vals[k])
 SD=sorted({3}|{p for k in ('u','b','q') for p in ff[k]});SP=sorted({7}|set(ff['s']));SQ=sorted({41}|set(ff['t']))
 assert not(set(SD)&set(SP) or set(SD)&set(SQ) or set(SP)&set(SQ))
 D3=[p for p in SD if p%8==3];D5=[p for p in SD if p%8==5];D7=[p for p in SD if p%8==7]
 P1=sorted(p for p in SP if p%8==1);P7=[p for p in SP if p%8==7]
 Q1=[p for p in SQ if p%8==1];Q7=sorted(p for p in SQ if p%8==7)
 assert D3[0]==3 and len(D3)==2 and len(D5)==len(D7)==1
 assert len(P1)==2 and P7==[7] and Q1==[41] and len(Q7)==2
 return [3,D3[1],D5[0],D7[0],P1[0],P1[1],7,41,Q7[0],Q7[1]],vals

def chart_ok(primes,chart):
 a=assignment(primes)
 return all(a[PAIRS[(i,j)]]==rhs for i,j,rhs in chart)
def numeric_object(primes):
 L=[[0 if i==j else legbit(primes[j],primes[i]) for j in range(10)] for i in range(10)]
 return {'eps':'shallow','vertices':[[a,b] for a,b in ATTRS],'legendre_bits':L}
def psi3_coeffs(a,b):
 N=a*a-b*b;M=a*a+b*b;d=a*b
 return [-64*N*N*d*d*(M**4+4*N*N*d*d),-192*N*N*d*d*M*M,-96*N*N*d*d,4*M*M,3]
def has_root_mod(coeffs,q):
 for x in range(q):
  y=0
  for z in reversed(coeffs):y=(y*x+z)%q
  if y==0:return True
 return False

pA,_=prime_support(22885787);AA=eval_matrix(assignment(pA));trA,HA,_,_=peel(AA)
pB,_=prime_support(35456387);AB=eval_matrix(assignment(pB));trB,HB,_,_=peel(AB)
assert len(trA)==len(trB)==22 and HA==HB==[[0,0],[0,0]]
assert leaf_equation_rref(trA)==expected_chart(CHART_A)
assert leaf_equation_rref(trB)==expected_chart(CHART_B)
ca=c['partial_legendre_charts']['A'];cb=c['partial_legendre_charts']['B']
assert ca['independent_condition_count']==6 and ca['free_reciprocity_bit_count']==39
assert cb['independent_condition_count']==9 and cb['free_reciprocity_bit_count']==36

ueh=c['uniform_EH_on_progression'];assert ueh['no4_condition_uniform'] and ueh['no3_condition_uniform']
assert not has_root_mod([4,0,4,0,3],5)

new=set()
for row in c['arithmetic_realizations']:
 u=row['u'];j=row['j'];assert u==17627+34440*j and u%3==2 and u%8==3 and u%5==2
 primes,vals=prime_support(u,row['factorization'])
 a=2*u;b=2*u+729;q=4*u+729
 assert math.gcd(u,b)==math.gcd(u,q)==math.gcd(b,q)==1
 assert math.isqrt(u)**2!=u and math.isqrt(u*b*q)**2!=u*b*q
 assert [z%5 for z in psi3_coeffs(a,b)]==[4,0,4,0,3] and not has_root_mod(psi3_coeffs(a,b),5)
 chosen=CHART_A if row['chart']=='A' else CHART_B
 assert chart_ok(primes,chosen)
 obj=numeric_object(primes);M,n=matrix_from_pattern(obj);r=rank(M)
 assert eval_matrix(assignment(primes))==[list(x) for x in M]
 tr,H,_,_=peel(M);rh=rank(H)
 assert (n,r,len(tr),len(H),rh,len(H)-rh)==(12,22,22,2,0,2)
 orbit={Fraction(a,b),Fraction(b,a),Fraction(729,q),Fraction(q,729)}
 assert orbit=={Fraction(x) for x in row['literal_orbit']}
 assert not(orbit&previous) and not(orbit&new);new.update(orbit)

assert len(new)==16 and len(previous|new)==208
ri=c['registry_impact'];assert ri=={'previous_count':192,'new_orbits':4,'new_parameters':16,'disjoint':True,'provisional_count':208,'exact_sufficient_template_count_unchanged':17,'partial_legendre_chart_count':2}
th=c['symbolic_theorem'];assert th['chart_A_or_B_implies_rank_2n_minus_2'] and th['chart_A_or_B_implies_sel2_dimension_2']
assert th['all_unlisted_reciprocity_bits_are_dont_care'] is True
assert th['charts_are_claimed_necessary'] is False and th['charts_exhaust_coarse_support_type'] is False
assert c['route_result']['next_leaf']=='36-09FB_RHO_PARTIAL_LEGENDRE_CHART_ARITHMETIC_REALIZATION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for key,val in c['scope_firewalls'].items():assert val is False,(key,val)
print('36-09FA verified: one fixed coarse support type has two exact partial-Legendre leaf charts of codimension 6 and 9 (39/36 reciprocity bits free); four new EH-clean literal orbits are disjoint from registry 192, giving provisional 208. No infinitude/classification/parent receiver/endpoint credit.')
