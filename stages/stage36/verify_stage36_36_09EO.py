#!/usr/bin/env python3
import hashlib,json,math,subprocess
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EH='stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-preflight.json'
EJ='stages/stage36/36-09EJ/bounded-rho-sel2-exact-computation-preflight.json'
EK='stages/stage36/36-09EK/rho-sel2-literal-orbit-closure-preflight.json'
EL='stages/stage36/36-09EL/rho-square-legendre-symbolic-sel2-matrix-preflight.json'
EM='stages/stage36/36-09EM/rho-odd-prime-local-kummer-branch-preflight.json'
EN='stages/stage36/36-09EN/rho-dyadic-local-kummer-branch-preflight.json'
SOURCE='stages/stage36/36-09EO/rho-point-search-free-sel2-evaluator-source-lock.md'
CERT='stages/stage36/36-09EO/rho-point-search-free-sel2-evaluator-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EH:'d95bf71f3cbed1d3fd12eaa0d235d2aa83539d37',
 EJ:'7ff288962132cae21f30a3c7b05ee1e5b5680c91',
 EK:'f6af11a0f7fd8a303531b2a587b7446c382a84c5',
 EL:'192ff96c8b17db331cefd019c0b70c7b4a6f6bc9',
 EM:'6307dcbfcd0cdfcf1e9ebba80d9408a88e5809d6',
 EN:'344759ef8e003e8e37f1f22a046fa0bfcb8131f3',
 SOURCE:'81fd2354e95a8e27ba7978b87612daf9ac9c452c',
 CERT:'bb76c05c7549ebb243a193376691138d8e01a7fb',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
eh=load(EH);ej=load(EJ);ek=load(EK);el=load(EL);em=load(EM);en=load(EN);c=load(CERT)
assert eh['rank_and_torsion_criterion']['sel2_dimension_condition']==2
assert eh['fixed_p_consequence']['retained_physical_receiver_sector_empty_under_conditions'] is True
assert ej['exact_result']['sel2_dimension_distribution']=={'2':14,'3':14,'4':30,'5':4}
assert ek['receiver_consequence']['expanded_registry_count']==16
assert el['symbolic_sel2_matrix']['dimension_formula']=='dim_F2 Sel^2(E_rho,p/Q)=2|G|-rank_F2 M_Sel2(a,b)'
assert em['scope_firewalls']['odd_prime_local_kummer_branch_formula_complete'] is True
assert en['combined_local_closure']['all_required_local_kummer_branch_formulas_complete'] is True

# ---------- F2 linear algebra ----------
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
def rank(vs):return len(rref(vs))
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
  for i,p in reversed(list(enumerate(piv))):
   z=0
   for j in free:z^=a[i][j]&x[j]
   x[p]=z
  out.append(tuple(x))
 return out

# ---------- arithmetic / squareclasses ----------
def vpint(n,p):
 assert n!=0
 n=abs(n);z=0
 while n%p==0:z+=1;n//=p
 return z
def pf(n):
 n=abs(n);out=[]
 if n<2:return out
 if n%2==0:
  out.append(2)
  while n%2==0:n//=2
 q=3
 while q*q<=n:
  if n%q==0:
   out.append(q)
   while n%q==0:n//=q
  q+=2
 if n>1:out.append(n)
 return out
def scodd(n,p):
 z=vpint(n,p);u=n//(p**z);um=u%p
 return (z&1,0 if pow(um,(p-1)//2,p)==1 else 1)
def sc2(n):
 z=vpint(n,2);u=(n//(2**z))%8
 nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u]
 return (z&1,)+nm
def scloc(g,v):
 if v=='infinity':return (1 if g<0 else 0,)
 if v==2:return sc2(g)
 return scodd(g,v)

REAL=((0,1),)
W2_SHALLOW=((0,0,1,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
W2_DEEP=((0,0,0,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
ODD={
 ('D',None):((0,0,1,0),(0,0,0,1)),
 ('P',1):((1,0,1,0),(0,1,0,1)),
 ('P',7):((0,1,0,0),(0,0,0,1)),
 ('Q',1):((1,0,0,0),(0,1,0,0)),
 ('Q',7):((0,1,0,0),(0,0,0,1)),
}
assert tuple(map(tuple,en['local_formulas']['real']['basis']))==REAL
assert tuple(map(tuple,en['local_formulas']['shallow']['basis']))==W2_SHALLOW
assert tuple(map(tuple,en['local_formulas']['deep']['basis']))==W2_DEEP

def sel2_closed(a,b):
 N=a*a-b*b;d=a*b;P=N+2*d;Q=N-2*d;D=P*P-Q*Q
 S=sorted(set([2]+pf(P)+pf(Q)+pf(D)))
 G=[-1]+S;m=len(G);ambient=2*m;constraints=[]
 for v in ['infinity']+S:
  if v=='infinity':W=REAL;dl=1
  elif v==2:
   g=math.gcd(abs(P),abs(Q));r=0 if g==1 else 1
   A=P//(2**r);B=Q//(2**r);depth=vpint(A*A-B*B,2)
   assert depth>=4
   W=W2_SHALLOW if depth==4 else W2_DEEP;dl=3
  else:
   if P%v==0:key=('P',v%8)
   elif Q%v==0:key=('Q',v%8)
   else:
    assert D%v==0 and P%v and Q%v
    key=('D',None)
   assert key in ODD,(a,b,v,key)
   W=ODD[key];dl=2
  orth=nullspace(W,2*dl);loc=[scloc(g,v) for g in G]
  for z in orth:
   z1=z[:dl];z2=z[dl:];row=[0]*ambient
   for j,lg in enumerate(loc):
    row[j]=sum(x*y for x,y in zip(z1,lg))&1
    row[m+j]=sum(x*y for x,y in zip(z2,lg))&1
   constraints.append(tuple(row))
 cr=rank(constraints)
 return S,ambient,cr,ambient-cr

# Replay original EJ domain with no local point search.
pairs10=[(a,b) for a in range(1,11) for b in range(1,11) if a!=b and math.gcd(a,b)==1]
res10=[(a,b,*sel2_closed(a,b)) for a,b in pairs10]
d10=Counter(x[-1] for x in res10)
assert d10==Counter({4:30,2:14,3:14,5:4}),d10
rows2_10=[[a,b] for a,b,*rest in res10 if rest[-1]==2]
assert rows2_10==ej['exact_result']['sel2_dimension_2_rows']

# Exact 50-box evaluation.
pairs50=[(a,b) for a in range(1,51) for b in range(1,51) if a!=b and math.gcd(a,b)==1]
assert len(pairs50)==1546
rows=[];dims=Counter();dim2=[]
for a,b in pairs50:
 S,ambient,cr,dim=sel2_closed(a,b);dims[dim]+=1
 if dim==2:dim2.append([a,b])
 rows.append((a,b,';'.join(map(str,S)),ambient,cr,dim))
assert dims==Counter({5:554,4:500,6:280,3:136,7:52,2:24}),dims
expected_dim2=[[1,2],[1,3],[1,5],[2,1],[2,3],[2,7],[2,9],[3,1],[3,2],[3,47],[5,1],[5,9],[6,43],[7,2],[7,11],[9,2],[9,5],[11,7],[22,25],[25,22],[37,49],[43,6],[47,3],[49,37]]
assert dim2==expected_dim2
csv=''.join(f'{a},{b},{S},{ambient},{cr},{dim}\n' for a,b,S,ambient,cr,dim in rows)
digest=hashlib.sha256(csv.encode()).hexdigest()
assert digest=='875b813e8af97b34a7fb6d3dab70abb17bc88102beb5523efc751a72352133e7'
assert c['diagnostic_50_box']['row_digest_sha256']==digest
assert c['diagnostic_50_box']['sel2_dimension_2_rows']==expected_dim2
assert c['diagnostic_50_box']['sel2_dimension_distribution']=={'2':24,'3':136,'4':500,'5':554,'6':280,'7':52}

# Exact literal/rho orbit algebra.
def pq(a,b):
 N=a*a-b*b;d=a*b
 return N+2*d,N-2*d
def cp(p):return (p+1)/(p-1)
def orbit(p):
 z=cp(p)
 return tuple(sorted({abs(p),abs(1/p),abs(z),abs(1/z)}))
seeds=[Fraction(2),Fraction(1,5),Fraction(2,7),Fraction(2,9),Fraction(3,47),Fraction(6,43)]
expected_orbits=[tuple(Fraction(s) for s in xs) for xs in c['rho_orbit_structure']['six_dim2_orbits']]
for p,exp in zip(seeds,expected_orbits):assert orbit(p)==tuple(sorted(exp)),(p,orbit(p),exp)
# Inversion and c-action formulas before primitive reduction.
for a,b in [(3,47),(6,43),(7,11),(22,25)]:
 P,Q=pq(a,b);Pi,Qi=pq(b,a);Pc,Qc=pq(a+b,a-b)
 assert (Pi,Qi)==(-Q,-P)
 assert (Pc,Qc)==(2*P,-2*Q)

# EH no4 condition and rational 3-torsion witnesses on new seeds.
def rat_square(q):
 q=Fraction(q)
 if q<0:return False
 return math.isqrt(q.numerator)**2==q.numerator and math.isqrt(q.denominator)**2==q.denominator
def no4(a,b):
 h=Fraction(a*a-b*b,a*b)
 return (not rat_square(8*h)) and (not rat_square(-8*h))
def count_mod(a,b,l):
 P,Q=pq(a,b);roots=[0,(P*P)%l,(Q*Q)%l]
 assert len(set(roots))==3,(a,b,l,roots)
 total=1
 for x in range(l):
  rhs=x*(x-roots[1])*(x-roots[2])%l
  if rhs==0:total+=1
  elif pow(rhs,(l-1)//2,l)==1:total+=2
 return total
for a,b,l,n in [(3,47,13,16),(6,43,5,8)]:
 assert sel2_closed(a,b)[-1]==2
 assert no4(a,b)
 assert count_mod(a,b,l)==n
 assert n%3!=0 and l!=3
# Directly verify all eight new orbit members retain Sel2=2 and no4.
new8=[[3,47],[22,25],[25,22],[47,3],[6,43],[37,49],[49,37],[43,6]]
for a,b in new8:
 assert sel2_closed(a,b)[-1]==2
 assert no4(a,b)
assert c['new_orbit_EH_checks']['seed_3_47']=={'sel2_dimension':2,'plus_minus_8h_nonsquare':True,'good_reduction_prime':13,'finite_field_order':16,'rational_3_torsion_zero':True}
assert c['new_orbit_EH_checks']['seed_6_43']=={'sel2_dimension':2,'plus_minus_8h_nonsquare':True,'good_reduction_prime':5,'finite_field_order':8,'rational_3_torsion_zero':True}
cc=c['criterion_consumption']
assert cc['previous_fixed_parameter_registry_count']==16
assert cc['new_excluded_parameter_count']==8
assert cc['expanded_fixed_parameter_registry_count']==24
assert len(set(cc['expanded_fixed_parameter_registry']))==24
assert cc['each_new_fixed_parameter_receiver_sector_empty'] is True
assert c['route_result']['next_leaf']=='36-09EP_RHO_SEL2_RANK_CRITERION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09EO verified: closed local-formula Sel2 evaluator reproduces EJ, gives exact 50-box distribution 2:24/3:136/4:500/5:554/6:280/7:52, and two new EH-qualified four-point orbits add eight fixed-p exclusions. No exhaustive-ledger/full receiver/endpoint credit.')
