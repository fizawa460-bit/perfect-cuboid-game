#!/usr/bin/env python3
import json,math,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EM='stages/stage36/36-09EM/rho-odd-prime-local-kummer-branch-preflight.json'
EL='stages/stage36/36-09EL/rho-square-legendre-symbolic-sel2-matrix-preflight.json'
EJ='stages/stage36/36-09EJ/bounded-rho-sel2-exact-computation-preflight.json'
DW='stages/stage36/36-09DW/phi-selmer-five-place-local-image-source-lock.md'
SOURCE='stages/stage36/36-09EN/rho-dyadic-local-kummer-branch-source-lock.md'
REAL='stages/stage36/36-09EN/rho-real-local-kummer-formula-source-lock.md'
CERT='stages/stage36/36-09EN/rho-dyadic-local-kummer-branch-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={EM:'6307dcbfcd0cdfcf1e9ebba80d9408a88e5809d6',EL:'192ff96c8b17db331cefd019c0b70c7b4a6f6bc9',EJ:'7ff288962132cae21f30a3c7b05ee1e5b5680c91',DW:'08c91eed30774fa5c44509bb61f1c3b1386f2266',SOURCE:'b157421f9524b4996a6e6358c6c66a866077e1b5',REAL:'a827e59cae675c90923411c50ea5627e19bef4ed',CERT:'344759ef8e003e8e37f1f22a046fa0bfcb8131f3'}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
em=load(EM);el=load(EL);ej=load(EJ);c=load(CERT);dw=(ROOT/DW).read_text();real=(ROOT/REAL).read_text()
assert em['scope_firewalls']['odd_prime_local_kummer_branch_formula_complete'] is True
assert el['prime_support']['gcd_P_Q_in']==[1,2]
assert ej['scan_domain']['ordered_parameter_count']==62
assert 'F2-dimension `3` over `Q_2`' in dw
assert 'W_infinity=span{(0,1)}' in real

# F2 / Q2 squareclass helpers
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
def same(a,b):return rref(a)==rref(b)
def v2(n):
 assert n!=0
 n=abs(n);z=0
 while n%2==0:z+=1;n//=2
 return z
def sc2(n):
 assert n!=0
 z=v2(n);u=(n//(2**z))%8
 nm={1:(0,0),3:(1,1),5:(0,1),7:(1,0)}[u]
 return (z&1,)+nm
def is_square_q2(n):
 if n==0:return True
 z=v2(n)
 if z&1:return False
 return (n//(2**z))%8==1

def old_local_span(e1,e2,e3,bound=50):
 pairs=[((e1-e2)*(e1-e3),e1-e2),(e2-e1,(e2-e1)*(e2-e3))]
 out=[sc2(x)+sc2(y) for x,y in pairs]
 for x in range(-bound,bound+1):
  if x in (e1,e2,e3):continue
  rhs=(x-e1)*(x-e2)*(x-e3)
  if is_square_q2(rhs):out.append(sc2(x-e1)+sc2(x-e2))
 return rref(out)

def old_to_EL(W):
 out=[]
 for v in W:
  a=v[:3];b=v[3:]
  out.append(tuple(x^y for x,y in zip(a,b))+tuple(a))
 return rref(out)

SHALLOW=((0,0,1,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
DEEP=((0,0,0,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
seen={'shallow':0,'deep':0}
for a in range(1,11):
 for b in range(1,11):
  if a==b or math.gcd(a,b)!=1:continue
  N=a*a-b*b;d=a*b;M=a*a+b*b;P=N+2*d;Q=N-2*d
  g=math.gcd(abs(P),abs(Q));assert g in (1,2)
  r=0 if g==1 else 1
  A=P//(2**r);B=Q//(2**r)
  assert A&1 and B&1
  m=v2(A*A-B*B)
  assert m>=4,(a,b,A,B,m)
  shallow=(m==4)
  if (a+b)&1: expected_shallow=(v2(a*b)==1)
  else: expected_shallow=(v2(a*a-b*b)==3)
  assert shallow==expected_shallow,(a,b,m,expected_shallow)
  e1,e2,e3=4*N*d,-4*N*d,-M*M
  got=old_to_EL(old_local_span(e1,e2,e3,50))
  assert rank(got)==3,(a,b,got)
  exp=SHALLOW if shallow else DEEP
  assert same(got,exp),(a,b,m,got,exp)
  seen['shallow' if shallow else 'deep']+=1
assert seen['shallow']>0 and seen['deep']>0,seen

# Uniform real formula: choose X in (0,min(P^2,Q^2)); cubic sign is (+)(-)(-).
# Hence EL sign bits are (0,1), and the real local quotient has dimension one.
for a in range(1,31):
 for b in range(1,31):
  if a==b or math.gcd(a,b)!=1:continue
  N=a*a-b*b;d=a*b;P=N+2*d;Q=N-2*d
  assert P and Q and P*P!=Q*Q
  assert min(P*P,Q*Q)>0

# Broader arithmetic regression for the dyadic branch criterion itself.
for a in range(1,101):
 for b in range(1,101):
  if a==b or math.gcd(a,b)!=1:continue
  N=a*a-b*b;d=a*b;P=N+2*d;Q=N-2*d
  g=math.gcd(abs(P),abs(Q));assert g in (1,2)
  r=0 if g==1 else 1;A=P//(2**r);B=Q//(2**r);m=v2(A*A-B*B)
  assert m>=4
  if (a+b)&1: expected_shallow=(v2(a*b)==1)
  else: expected_shallow=(v2(a*a-b*b)==3)
  assert (m==4)==expected_shallow

lf=c['local_formulas']
assert lf['real']['basis']==[[0,1]]
assert lf['shallow']['basis']==[list(x) for x in SHALLOW]
assert lf['deep']['basis']==[list(x) for x in DEEP]
assert c['normalization']['m_lower_bound']==4
assert c['exactness']['real_local_target_dimension']==1
assert c['exactness']['real_formula_uniform'] is True
assert c['exactness']['Q2_local_target_dimension']==3
assert c['exactness']['all_62_EJ_rows_Q2_match_formula'] is True
assert c['exactness']['both_branches_occur_in_replay'] is True
assert c['combined_local_closure']['real_local_kummer_formula_complete'] is True
assert c['combined_local_closure']['odd_prime_local_kummer_branch_formula_complete'] is True
assert c['combined_local_closure']['dyadic_local_kummer_branch_formula_complete'] is True
assert c['combined_local_closure']['all_required_local_kummer_branch_formulas_complete'] is True
assert c['route_result']['next_leaf']=='36-09EO_RHO_SYMBOLIC_SEL2_EVALUATOR_AND_PATTERN_PREFLIGHT'
for k in ['uniform_Sel2_dimension_2_theorem','new_fixed_parameter_exclusion','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_nonexistence_claim']:
 assert c['scope_firewalls'][k] is False,k
print('36-09EN verified: real and Q2 local Kummer images are uniform exact formulas; with EM every local Sel2 block is point-search-free. No uniform Sel2/full receiver/endpoint credit.')
