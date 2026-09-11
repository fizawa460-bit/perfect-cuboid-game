#!/usr/bin/env python3
import json,math,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EO='stages/stage36/36-09EO/rho-point-search-free-sel2-evaluator-preflight.json'
EL='stages/stage36/36-09EL/rho-square-legendre-symbolic-sel2-matrix-preflight.json'
EM='stages/stage36/36-09EM/rho-odd-prime-local-kummer-branch-preflight.json'
EN='stages/stage36/36-09EN/rho-dyadic-local-kummer-branch-preflight.json'
SOURCE='stages/stage36/36-09EP/rho-sel2-support-rank-criterion-source-lock.md'
CERT='stages/stage36/36-09EP/rho-sel2-support-rank-criterion-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={EO:'bb76c05c7549ebb243a193376691138d8e01a7fb',EL:'192ff96c8b17db331cefd019c0b70c7b4a6f6bc9',EM:'6307dcbfcd0cdfcf1e9ebba80d9408a88e5809d6',EN:'344759ef8e003e8e37f1f22a046fa0bfcb8131f3',SOURCE:'cef2f0eaecd6d428821859a520d71042291c3744',CERT:'4e3f103a3711220f1d5f6475f1fcff345b31ae7a'}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
eo=load(EO);el=load(EL);em=load(EM);en=load(EN);c=load(CERT)
assert eo['diagnostic_50_box']['ordered_parameter_count']==1546
assert el['symbolic_sel2_matrix']['dimension_formula']=='dim_F2 Sel^2(E_rho,p/Q)=2|G|-rank_F2 M_Sel2(a,b)'
assert em['scope_firewalls']['odd_prime_local_kummer_branch_formula_complete'] is True
assert en['combined_local_closure']['all_required_local_kummer_branch_formulas_complete'] is True

# F2 linear algebra.
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

# Arithmetic helpers.
def vp(n,p):
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
def legbit(a,q):return 0 if pow(a%q,(q-1)//2,q)==1 else 1
def scodd(n,q):
 z=vp(n,q);u=n//(q**z)
 return (z&1,legbit(u,q))
def sc2(n):
 z=vp(n,2);u=(n//(2**z))%8
 nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u]
 return (z&1,)+nm

REAL=((0,1),)
W2S=((0,0,1,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
W2D=((0,0,0,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
ODD={('D',None):((0,0,1,0),(0,0,0,1)),('P',1):((1,0,1,0),(0,1,0,1)),('P',7):((0,1,0,0),(0,0,0,1)),('Q',1):((1,0,0,0),(0,1,0,0)),('Q',7):((0,1,0,0),(0,0,0,1))}

def datum(a,b):
 N=a*a-b*b;d=a*b;P=N+2*d;Q=N-2*d;D=P*P-Q*Q
 SP=sorted(q for q in pf(P) if q!=2);SQ=sorted(q for q in pf(Q) if q!=2)
 SD=sorted(q for q in pf(D) if q!=2 and P%q and Q%q)
 assert not (set(SP)&set(SQ) or set(SP)&set(SD) or set(SQ)&set(SD))
 odd=sorted(SP+SQ+SD)
 labels={q:('P' if q in SP else ('Q' if q in SQ else 'D')) for q in odd}
 g=math.gcd(abs(P),abs(Q));r=0 if g==1 else 1;A=P//(2**r);B=Q//(2**r)
 eps='shallow' if vp(A*A-B*B,2)==4 else 'deep'
 return P,Q,odd,labels,eps

def W_for(v,labels,eps):
 if v=='infinity':return REAL,1
 if v==2:return (W2S if eps=='shallow' else W2D),3
 typ=labels[v];key=(typ,v%8) if typ in ('P','Q') else ('D',None)
 return ODD[key],2

def matrix_direct(a,b):
 P,Q,odd,labels,eps=datum(a,b);G=[-1,2]+odd;ambient=2*len(G);rows=[]
 for v in ['infinity',2]+odd:
  W,dl=W_for(v,labels,eps);orth=nullspace(W,2*dl);loc=[]
  for g in G:
   if v=='infinity':bits=(1 if g<0 else 0,)
   elif v==2:bits=sc2(g)
   else:bits=scodd(g,v)
   loc.append(bits)
  for z in orth:
   z1=z[:dl];z2=z[dl:];row=[0]*ambient
   for j,bits in enumerate(loc):
    row[j]=sum(x*y for x,y in zip(z1,bits))&1
    row[len(G)+j]=sum(x*y for x,y in zip(z2,bits))&1
   rows.append(tuple(row))
 return tuple(rows),G,labels,eps

def support_loc(g,v):
 # Construct squareclass bits solely from the labelled radical datum.
 if v=='infinity':return (1 if g==-1 else 0,)
 if v==2:
  if g==-1:return (0,1,0)
  if g==2:return (1,0,0)
  r=g%8
  return {1:(0,0,0),3:(0,1,1),5:(0,0,1),7:(0,1,0)}[r]
 # odd v
 if g==v:return (1,0)
 if g==-1:return (0,1 if v%4==3 else 0)
 if g==2:return (0,1 if v%8 in (3,5) else 0)
 return (0,legbit(g,v))

def matrix_support(a,b):
 P,Q,odd,labels,eps=datum(a,b);G=[-1,2]+odd;ambient=2*len(G);rows=[]
 for v in ['infinity',2]+odd:
  W,dl=W_for(v,labels,eps);orth=nullspace(W,2*dl);loc=[support_loc(g,v) for g in G]
  for z in orth:
   z1=z[:dl];z2=z[dl:];row=[0]*ambient
   for j,bits in enumerate(loc):
    row[j]=sum(x*y for x,y in zip(z1,bits))&1
    row[len(G)+j]=sum(x*y for x,y in zip(z2,bits))&1
   rows.append(tuple(row))
 return tuple(rows),G,labels,eps

# Exact replay: entrywise matrix equality on all EO 50-box rows.
count=0;dim2=0
for a in range(1,51):
 for b in range(1,51):
  if a==b or math.gcd(a,b)!=1:continue
  md,Gd,ld,ed=matrix_direct(a,b);ms,Gs,ls,es=matrix_support(a,b)
  assert Gd==Gs and ld==ls and ed==es
  assert md==ms,(a,b)
  n=len(Gs);dim=2*n-rank(ms)
  assert dim>=2
  if dim==2:
   dim2+=1
   assert rank(ms)==2*n-2
  else:
   assert rank(ms)!=2*n-2
  count+=1
assert count==1546 and dim2==24,(count,dim2)

sr=c['support_matrix']
assert sr['entrywise_equal_to_EL_EO_matrix_in_canonical_order'] is True
assert sr['sel2_dimension_formula']=='dim_F2 Sel^2(E_rho,p/Q)=2n-rank_F2 M_R(R(a,b))'
assert sr['sel2_dimension_2_criterion']=='rank_F2 M_R(R(a,b))=2n-2'
assert sr['criterion_necessary_and_sufficient'] is True
assert c['exponent_erasure']['valuation_exponents_not_needed'] is True
assert c['exponent_erasure']['labelled_radical_support_plus_quadratic_reciprocity_sufficient'] is True
assert c['exact_replay']=={'domain':'EO ordered primitive 1..50 box','row_count':1546,'support_matrix_matches_EO_rank_on_all_rows':True,'support_matrix_matches_EO_sel2_dimension_on_all_rows':True,'sel2_dimension_2_row_count':24}
assert c['route_result']['next_leaf']=='36-09EQ_RHO_LEGENDRE_GRAPH_MAXIMAL_RANK_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09EP verified: labelled radical support, mod-8 data, dyadic branch, and pairwise Legendre symbols reconstruct the Sel2 matrix entrywise on all 1546 EO rows; Sel2_dim=2 iff support matrix rank is 2n-2. Exponents are irrelevant; no new receiver/endpoint credit.')
