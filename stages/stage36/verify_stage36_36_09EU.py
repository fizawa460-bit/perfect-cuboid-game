#!/usr/bin/env python3
import itertools,json,math,subprocess
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EP='stages/stage36/36-09EP/rho-sel2-support-rank-criterion-preflight.json'
ES='stages/stage36/36-09ES/rho-legendre-pattern-classification-preflight.json'
ET='stages/stage36/36-09ET/rho-template-realization-nearmiss-expansion-preflight.json'
SOURCE='stages/stage36/36-09EU/rho-t6-profile-legendre-rigidity-source-lock.md'
CERT='stages/stage36/36-09EU/rho-t6-profile-legendre-rigidity-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EP:'4e3f103a3711220f1d5f6475f1fcff345b31ae7a',
 ES:'1a464aaffb328dc5068cda2e6f3a5073bc9d7f69',
 ET:'6130e12a668c66fa181b1e9a6be17c9219257002',
 SOURCE:'f3bbc98b642c6cc1a4417288344a490f20e39d79',
 CERT:'0507f5a19cc3baf44553e7b9bdd0e689bd5ec5d7'}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
ep=load(EP);es=load(ES);et=load(ET);c=load(CERT)
assert c['entry_authority']['v274_exact_head']=='317e9eb47c5e69fd2c6c1810e1689b7bd24391cb'
assert c['entry_authority']['v274_promotion_ci']=='34362605141/102503133358'
assert c['entry_authority']['36_09EU_entry_allowed'] is True
assert ep['support_matrix']['criterion_necessary_and_sufficient'] is True
assert es['abstract_matrix_theorem']['global_in_parameter_not_box_restricted'] is True
assert et['template_library_impact']['expanded_exact_template_count']==9
assert et['new_fixed_parameter_exclusions']['expanded_registry_count']==36

# F2 linear algebra.
def rref(vs):
 rows=[list(map(int,v)) for v in vs if any(v)]
 if not rows:return []
 n=len(rows[0]);rr=0
 for j in range(n):
  q=next((i for i in range(rr,len(rows)) if rows[i][j]),None)
  if q is None:continue
  rows[rr],rows[q]=rows[q],rows[rr]
  for i in range(len(rows)):
   if i!=rr and rows[i][j]:rows[i]=[x^y for x,y in zip(rows[i],rows[rr])]
  rr+=1
  if rr==len(rows):break
 return rows[:rr]
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

def det3(A):
 # sign disappears in F2
 z=0
 for s in itertools.permutations(range(3)):
  t=1
  for i in range(3):t&=A[i][s[i]]
  z^=t
 return z

# Polynomial ring over F2 represented by sets of squarefree monomial masks.
# Boolean specializations satisfy x^2=x, sufficient for symbolic replay of all
# Legendre-bit assignments.
ZERO=frozenset();ONE=frozenset({0})
def var(i):return frozenset({1<<i})
def add(a,b):return a.symmetric_difference(b)
def mul(a,b):
 out=set()
 for x in a:
  for y in b:
   z=x|y
   if z in out:out.remove(z)
   else:out.add(z)
 return frozenset(out)

def isone(a):return a==ONE

REAL=((0,1),)
W2S=((0,0,1,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
ODD={('D',None):((0,0,1,0),(0,0,0,1)),('P',1):((1,0,1,0),(0,1,0,1)),('P',7):((0,1,0,0),(0,0,0,1)),('Q',1):((1,0,0,0),(0,1,0,0)),('Q',7):((0,1,0,0),(0,0,0,1))}
attrs=[('D',3),('D',3),('D',5),('D',7),('P',1),('P',7),('Q',1),('Q',1)]
mods=[x[1] for x in attrs];pairs=[(i,j) for i in range(8) for j in range(i+1,8)];pidx={p:i for i,p in enumerate(pairs)}

def L(i,j):
 if i==j:return ZERO
 if i<j:return var(pidx[(i,j)])
 x=var(pidx[(j,i)])
 return add(x,ONE) if mods[i]%4==3 and mods[j]%4==3 else x

def symbolic_matrix():
 rows=[]
 def addplace(W,dl,loc):
  for z in nullspace(W,2*dl):
   z1=z[:dl];z2=z[dl:];row=[ZERO]*20
   for j,bits in enumerate(loc):
    a=ZERO;b=ZERO
    for q,w in zip(z1,bits):
     if q:a=add(a,w)
    for q,w in zip(z2,bits):
     if q:b=add(b,w)
    row[j]=a;row[10+j]=b
   rows.append(row)
 addplace(REAL,1,[(ONE,),(ZERO,)]+[(ZERO,)]*8)
 q2map={1:(0,0,0),3:(0,1,1),5:(0,0,1),7:(0,1,0)}
 q2=[tuple(ONE if v else ZERO for v in (0,1,0)),tuple(ONE if v else ZERO for v in (1,0,0))]
 q2 += [tuple(ONE if v else ZERO for v in q2map[m]) for m in mods]
 addplace(W2S,3,q2)
 for i,(lab,m8) in enumerate(attrs):
  key=(lab,m8) if lab in ('P','Q') else ('D',None)
  loc=[(ZERO,ONE if m8 in (3,7) else ZERO),(ZERO,ONE if m8 in (3,5) else ZERO)]
  loc += [(ONE,ZERO) if i==j else (ZERO,L(i,j)) for j in range(8)]
  addplace(ODD[key],2,loc)
 return rows

def constant_reduce(A):
 A=[row[:] for row in A];piv=[];rl=list(range(20));cl=list(range(20))
 while A and A[0]:
  pos=next(((i,j) for i,row in enumerate(A) for j,e in enumerate(row) if isone(e)),None)
  if pos is None:break
  i,j=pos;A[0],A[i]=A[i],A[0];rl[0],rl[i]=rl[i],rl[0]
  for row in A:row[0],row[j]=row[j],row[0]
  cl[0],cl[j]=cl[j],cl[0]
  for r in range(1,len(A)):
   f=A[r][0]
   if f:A[r]=[add(x,mul(f,y)) for x,y in zip(A[r],A[0])]
  for cc in range(1,len(A[0])):
   f=A[0][cc]
   if f:
    for r in range(len(A)):A[r][cc]=add(A[r][cc],mul(f,A[r][0]))
  piv.append((rl[0],cl[0]))
  A=[row[1:] for row in A[1:]];rl=rl[1:];cl=cl[1:]
 return A,piv,rl,cl

S=symbolic_matrix();R,piv,rl,cl=constant_reduce(S)
assert len(S)==20 and all(len(x)==20 for x in S)
assert len(piv)==12 and len(R)==8 and len(R[0])==8
assert sum(all(not x for x in row) for row in R)==1
assert sum(all(not R[i][j] for i in range(8)) for j in range(8))==1

# Delete the unique zero row/column. Constant pivoting preserves rank but the
# residual row order is not the semantic D0,D1,D2,D3,P,Q1,Q0 order. Relabel
# only the rows by the exact deterministic residual-label permutation before
# checking the alternating block form.
zr=next(i for i,row in enumerate(R) if all(not x for x in row))
zc=next(j for j in range(8) if all(not R[i][j] for i in range(8)))
K0=[[R[i][j] for j in range(8) if j!=zc] for i in range(8) if i!=zr]
rowperm=[0,3,2,5,1,6,4]
K=[K0[i] for i in rowperm]
assert len(K)==7 and all(len(x)==7 for x in K)
assert all(not K[i][i] for i in range(7))
assert all(K[i][j]==K[j][i] for i in range(7) for j in range(7))
B=[[K[i][j] for j in range(4,7)] for i in range(4)]
assert all(not K[i][j] for i in range(4) for j in range(4))
assert not K[5][6] and not K[6][5]
# B must be exactly the 12 D-to-{P,Q1,Q0} upper Legendre variables.
expected_B=[[L(i,j) for j in (4,7,6)] for i in range(4)]
assert B==expected_B

# Principal 6x6 Pfaffians: four are 3x3 B minors, three vanish.
def pf(A):
 n=len(A)
 if n==0:return ONE
 out=ZERO
 for j in range(1,n):
  idx=[q for q in range(n) if q not in (0,j)]
  sub=[[A[r][cc] for cc in idx] for r in idx]
  out=add(out,mul(A[0][j],pf(sub)))
 return out
pfs=[]
for k in range(7):
 idx=[i for i in range(7) if i!=k];sub=[[K[r][cc] for cc in idx] for r in idx];pfs.append(pf(sub))
for k in range(4):
 rows=[i for i in range(4) if i!=k]
 d=ZERO
 for s in itertools.permutations(range(3)):
  t=ONE
  for i,r in enumerate(rows):t=mul(t,B[r][s[i]])
  d=add(d,t)
 assert pfs[k]==d
assert pfs[4:]==[ZERO,ZERO,ZERO]

# Arithmetic replay of T6/T7/T8/T9 and the two rank-16 controls.
def factor(n):
 n=abs(n);out=[]
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

def oriented_B(a,b):
 N=a*a-b*b;d=a*b;P=N+2*d;Q=N-2*d;D=P*P-Q*Q
 SP=sorted(q for q in factor(P) if q!=2);SQ=sorted(q for q in factor(Q) if q!=2)
 SD=sorted(q for q in factor(D) if q!=2 and P%q and Q%q)
 odd=sorted(SP+SQ+SD);labs={q:('P' if q in SP else ('Q' if q in SQ else 'D')) for q in odd}
 verts=[(q,labs[q],q%8) for q in odd];leg={(q,r):legbit(r,q) for q in odd for r in odd if q!=r}
 best=None
 for swap in (False,True):
  lm={'P':'Q','Q':'P','D':'D'} if swap else {'P':'P','Q':'Q','D':'D'}
  if sorted((lm[l],m) for _,l,m in verts)!=sorted(attrs):continue
  groups=defaultdict(list)
  for q,l,m in verts:groups[(lm[l],m)].append(q)
  keys=sorted(groups)
  for choice in itertools.product(*[list(itertools.permutations(groups[k])) for k in keys]):
   order=[]
   for key,ch in zip(keys,choice):order.extend(ch)
   mat=[[0 if i==j else leg[(order[i],order[j])] for j in range(8)] for i in range(8)]
   enc=''.join(map(str,sum(mat,[])))
   if best is None or enc<best[0]:best=(enc,mat)
 assert best is not None
 mat=best[1]
 return [[mat[i][j] for j in (4,7,6)] for i in range(4)]

replay={x['id']:x for x in c['ET_pattern_replay']}
seeds={'T6':(3,47),'T7':(1,277),'T8':(1,333),'T9':(134,863),'N1':(1,1323),'N2':(81,317)}
for ident,seed in seeds.items():
 bb=oriented_B(*seed);row=replay[ident]
 assert bb==row['B']
 rb=rank(bb);assert rb==row['B_rank']
 assert (rb==3)==(row['sel2_dimension']==2)
 ds=[]
 for k in range(4):ds.append(det3([bb[i] for i in range(4) if i!=k]))
 assert (any(ds))==(rb==3)

th=c['pfaffian_rank_theorem'];sr=c['symbolic_reduction']
assert sr['constant_pivot_count']==12 and sr['essential_core_alternating'] is True
assert sr['B_shape']==[4,3] and sr['P7_bits_survive_rank_problem'] is False and sr['Q1_Q1_bit_survives_rank_problem'] is False
assert th['core_rank_six_iff_B_rank_three'] is True
assert th['support_matrix_rank_18_iff_B_rank_3'] is True
assert th['sel2_dimension_2_iff_B_rank_3'] is True
assert th['criterion_necessary_and_sufficient_on_fixed_coarse_profile'] is True
assert th['criterion_global_not_box_restricted'] is True
assert c['route_result']['next_leaf']=='36-09EV_RHO_T6_PROFILE_RANK3_REALIZATION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09EU verified: fixed T6 coarse profile support matrix reduces by 12 constant pivots to a 7x7 alternating core; Sel2_dim=2 iff the 4x3 D-to-{P1,Q1,Q1} Legendre matrix B has rank 3. T6/T7/T8/T9 pass, both ET negative controls fail. No new fixed-p/receiver/endpoint credit.')
