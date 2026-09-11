#!/usr/bin/env python3
import json,math,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EP='stages/stage36/36-09EP/rho-sel2-support-rank-criterion-preflight.json'
EP_SOURCE='stages/stage36/36-09EP/rho-sel2-support-rank-criterion-source-lock.md'
SOURCE='stages/stage36/36-09EQ/rho-legendre-graph-leaf-pivot-source-lock.md'
CERT='stages/stage36/36-09EQ/rho-legendre-graph-leaf-pivot-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EP:'4e3f103a3711220f1d5f6475f1fcff345b31ae7a',
 EP_SOURCE:'cef2f0eaecd6d428821859a520d71042291c3744',
 SOURCE:'08ff42c1670a8dddffbbe9b9d81ef31934437af4',
 CERT:'ff4f8215b5e607c278b01f65aa858a5f038e0b35',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
ep=load(EP);c=load(CERT)
assert ep['support_matrix']['sel2_dimension_2_criterion']=='rank_F2 M_R(R(a,b))=2n-2'
assert ep['support_matrix']['criterion_necessary_and_sufficient'] is True
assert ep['exponent_erasure']['valuation_exponents_not_needed'] is True

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

# Arithmetic / labelled radical Legendre datum, copied independently from EP formulas.
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

REAL=((0,1),)
W2S=((0,0,1,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
W2D=((0,0,0,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
ODD={
 ('D',None):((0,0,1,0),(0,0,0,1)),
 ('P',1):((1,0,1,0),(0,1,0,1)),
 ('P',7):((0,1,0,0),(0,0,0,1)),
 ('Q',1):((1,0,0,0),(0,1,0,0)),
 ('Q',7):((0,1,0,0),(0,0,0,1)),
}

def datum(a,b):
 N=a*a-b*b;d=a*b;P=N+2*d;Q=N-2*d;D=P*P-Q*Q
 SP=sorted(q for q in pf(P) if q!=2);SQ=sorted(q for q in pf(Q) if q!=2)
 SD=sorted(q for q in pf(D) if q!=2 and P%q and Q%q)
 assert not (set(SP)&set(SQ) or set(SP)&set(SD) or set(SQ)&set(SD))
 odd=sorted(SP+SQ+SD)
 labels={q:('P' if q in SP else ('Q' if q in SQ else 'D')) for q in odd}
 g=math.gcd(abs(P),abs(Q));r=0 if g==1 else 1;A=P//(2**r);B=Q//(2**r)
 eps='shallow' if vp(A*A-B*B,2)==4 else 'deep'
 return odd,labels,eps

def W_for(v,labels,eps):
 if v=='infinity':return REAL,1
 if v==2:return (W2S if eps=='shallow' else W2D),3
 typ=labels[v];key=(typ,v%8) if typ in ('P','Q') else ('D',None)
 return ODD[key],2

def support_loc(g,v):
 if v=='infinity':return (1 if g==-1 else 0,)
 if v==2:
  if g==-1:return (0,1,0)
  if g==2:return (1,0,0)
  return {1:(0,0,0),3:(0,1,1),5:(0,0,1),7:(0,1,0)}[g%8]
 if g==v:return (1,0)
 if g==-1:return (0,1 if v%4==3 else 0)
 if g==2:return (0,1 if v%8 in (3,5) else 0)
 return (0,legbit(g,v))

def matrix_support(a,b):
 odd,labels,eps=datum(a,b);G=[-1,2]+odd;ambient=2*len(G);rows=[]
 for v in ['infinity',2]+odd:
  W,dl=W_for(v,labels,eps);orth=nullspace(W,2*dl);loc=[support_loc(g,v) for g in G]
  for z in orth:
   z1=z[:dl];z2=z[dl:];row=[0]*ambient
   for j,bits in enumerate(loc):
    row[j]=sum(x*y for x,y in zip(z1,bits))&1
    row[len(G)+j]=sum(x*y for x,y in zip(z2,bits))&1
   rows.append(tuple(row))
 return tuple(rows),G

# Deterministic graph peeling. Record enough data to replay leaf legality.
def peel(rows):
 if not rows:return [],[],[]
 R=set(range(len(rows)));C=set(range(len(rows[0])));seq=[]
 while True:
  chosen=None
  for i in sorted(R):
   js=[j for j in C if rows[i][j]]
   if len(js)==1:
    chosen=(i,js[0],'row');break
  if chosen is None:
   for j in sorted(C):
    ii=[i for i in R if rows[i][j]]
    if len(ii)==1:
     chosen=(ii[0],j,'column');break
  if chosen is None:break
  i,j,kind=chosen;seq.append((i,j,kind));R.remove(i);C.remove(j)
 return seq,sorted(R),sorted(C)

def pivot_minor(rows,seq):
 rr=[x[0] for x in seq];cc=[x[1] for x in seq]
 return [[rows[i][j] for j in cc] for i in rr]

expected20=[[1,2],[1,3],[1,5],[2,1],[2,3],[2,7],[2,9],[3,1],[3,2],[5,1],[5,9],[6,43],[7,2],[7,11],[9,2],[9,5],[11,7],[37,49],[43,6],[49,37]]
leaf_rows=[];dim2_rows=[];false_positive=[]
for a in range(1,51):
 for b in range(1,51):
  if a==b or math.gcd(a,b)!=1:continue
  M,G=matrix_support(a,b);n=len(G);rk=rank(M);dim=2*n-rk
  if dim==2:dim2_rows.append([a,b])
  seq,R,C=peel(M)
  if len(seq)>=2*n-2:
   # The first target pivots are themselves a legal certificate. Their selected minor must be full rank.
   target=seq[:2*n-2]
   pm=pivot_minor(M,target)
   assert len(pm)==2*n-2 and all(len(r)==2*n-2 for r in pm)
   assert rank(pm)==2*n-2,(a,b,'pivot minor not full rank')
   assert rk==2*n-2 and dim==2,(a,b,rk,dim)
   leaf_rows.append([a,b])
   if dim!=2:false_positive.append([a,b])
assert len(dim2_rows)==24
assert leaf_rows==expected20,(leaf_rows,expected20)
assert false_positive==[]
assert c['deterministic_replay']['row_count']==1546
assert c['deterministic_replay']['leaf_certified_row_count']==20
assert c['deterministic_replay']['leaf_certified_rows']==expected20
assert c['deterministic_replay']['false_positive_count']==0

# Exact nonnecessity orbit and residual-core diagnostics.
bad=[[3,47],[22,25],[25,22],[47,3]]
counts=[];resdiag=[]
for a,b in bad:
 M,G=matrix_support(a,b);assert len(G)==10;assert rank(M)==18;assert 2*len(G)-rank(M)==2
 seq,R,C=peel(M);counts.append(len(seq))
 sub=[[M[i][j] for j in C] for i in R]
 resdiag.append((len(R),len(C),rank(sub)))
assert counts==[12,12,10,10],counts
assert resdiag==[(8,8,6),(8,8,6),(10,10,8),(10,10,8)],resdiag
nw=c['nonnecessity_witness']
assert nw['rows']==bad and nw['n']==10 and nw['exact_rank']==18 and nw['exact_sel2_dimension']==2
assert nw['deterministic_leaf_pivot_counts']==counts
assert nw['leaf_criterion_not_necessary'] is True

lp=c['leaf_pivot_criterion']
assert lp['target_pivot_count']=='2n-2'
assert lp['sufficient_for_nonzero_2n_minus_2_minor'] is True
assert lp['sufficient_for_rank_2n_minus_2'] is True
assert lp['sufficient_for_Sel2_dimension_2'] is True
assert lp['criterion_is_claimed_necessary'] is False
assert c['route_result']['next_leaf']=='36-09ER_RHO_LEGENDRE_CORE_PARITY_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09EQ verified: a deficiency-two leaf-pivot certificate gives a full-rank (2n-2)-minor and hence Sel2_dim=2. Deterministic Legendre-graph peeling certifies 20/24 exact max-rank rows (five orbits) in the EO box with zero false positives; O(3/47) is the exact cyclic-core nonnecessity witness. No new receiver/endpoint credit.')
