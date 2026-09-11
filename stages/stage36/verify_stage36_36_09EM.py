#!/usr/bin/env python3
import json,math,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EL='stages/stage36/36-09EL/rho-square-legendre-symbolic-sel2-matrix-preflight.json'
EJ='stages/stage36/36-09EJ/bounded-rho-sel2-exact-computation-preflight.json'
DW='stages/stage36/36-09DW/phi-selmer-five-place-local-image-source-lock.md'
SOURCE='stages/stage36/36-09EM/rho-odd-prime-local-kummer-branch-source-lock.md'
CERT='stages/stage36/36-09EM/rho-odd-prime-local-kummer-branch-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={EL:'192ff96c8b17db331cefd019c0b70c7b4a6f6bc9',EJ:'7ff288962132cae21f30a3c7b05ee1e5b5680c91',DW:'08c91eed30774fa5c44509bb61f1c3b1386f2266',SOURCE:'7ce09723f733907a61de20ff72607154bf993d26',CERT:'6307dcbfcd0cdfcf1e9ebba80d9408a88e5809d6'}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
el=load(EL);ej=load(EJ);c=load(CERT);dw=(ROOT/DW).read_text()
assert el['square_legendre_normalization']['translated_model']=='y^2=X*(X-P^2)*(X-Q^2)'
assert el['prime_support']['gcd_P_Q_in']==[1,2]
assert ej['scan_domain']['ordered_parameter_count']==62
assert 'F2-dimension `2` for odd residue characteristic' in dw

# F2 helpers
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
def vpi(n,p):
 n=abs(n);z=0
 while n and n%p==0:z+=1;n//=p
 return z
def sc(n,p):
 assert n!=0
 z=vpi(n,p);u=n//(p**z);um=u%p
 return (z&1,0 if pow(um,(p-1)//2,p)==1 else 1)
def is_square_qp(n,p):
 if n==0:return True
 z=vpi(n,p)
 if z&1:return False
 return pow((n//(p**z))%p,(p-1)//2,p)==1

def pf(n):
 n=abs(n);out=[];q=2
 while q*q<=n:
  if n%q==0:
   out.append(q)
   while n%q==0:n//=q
  q=3 if q==2 else q+2
 if n>1:out.append(n)
 return out

def old_local_span(e1,e2,e3,p,bound=50):
 pairs=[((e1-e2)*(e1-e3),e1-e2),(e2-e1,(e2-e1)*(e2-e3))]
 out=[sc(x,p)+sc(y,p) for x,y in pairs]
 for x in range(-bound,bound+1):
  if x in (e1,e2,e3):continue
  rhs=(x-e1)*(x-e2)*(x-e3)
  if is_square_qp(rhs,p):out.append(sc(x-e1,p)+sc(x-e2,p))
 return rref(out)

def old_to_EL(W):
 # EJ old coordinates are ([x-4Nd],[x+4Nd]) = ([X-P^2],[X-Q^2]).
 # EL coordinates are ([X],[X-P^2]); product of all three coordinates is 1,
 # so [X]=old1+old2 and EL second=old1.
 out=[]
 for v in W:
  a=v[:2];b=v[2:]
  out.append(tuple(x^y for x,y in zip(a,b))+tuple(a))
 return rref(out)

FORM={
 ('D',None):((0,0,1,0),(0,0,0,1)),
 ('P',1):((1,0,1,0),(0,1,0,1)),
 ('P',7):((0,1,0,0),(0,0,0,1)),
 ('Q',1):((1,0,0,0),(0,1,0,0)),
 ('Q',7):((0,1,0,0),(0,0,0,1)),
}
counts={}
for a in range(1,11):
 for b in range(1,11):
  if a==b or math.gcd(a,b)!=1:continue
  N=a*a-b*b;d=a*b;M=a*a+b*b;P=N+2*d;Q=N-2*d;D=P*P-Q*Q
  assert math.gcd(abs(P),abs(Q)) in (1,2)
  e1,e2,e3=4*N*d,-4*N*d,-M*M
  for q in sorted(set(pf((e1-e2)*(e1-e3)*(e2-e3)))):
   if q==2:continue
   branch='P' if P%q==0 else ('Q' if Q%q==0 else 'D')
   if branch in ('P','Q'):
    assert q%8 in (1,7),(a,b,q,branch)
    key=(branch,q%8)
   else:
    assert D%q==0 and P%q and Q%q
    key=('D',None)
   got=old_to_EL(old_local_span(e1,e2,e3,q,50))
   assert rank(got)==2,(a,b,q,branch,got)
   assert same(got,FORM[key]),(a,b,q,branch,q%8,got,FORM[key])
   counts[key]=counts.get(key,0)+1

# All five branch formulas must occur in the exact bounded replay.
assert all(counts.get(k,0)>0 for k in FORM),counts
lf=c['local_formulas']
assert lf['D_branch']['basis']==[[0,0,1,0],[0,0,0,1]]
assert lf['P_branch_mod8_1']['basis']==[[1,0,1,0],[0,1,0,1]]
assert lf['P_branch_mod8_7']['basis']==[[0,1,0,0],[0,0,0,1]]
assert lf['Q_branch_mod8_1']['basis']==[[1,0,0,0],[0,1,0,0]]
assert lf['Q_branch_mod8_7']['basis']==[[0,1,0,0],[0,0,0,1]]
assert c['exactness']['odd_local_target_dimension']==2
assert c['exactness']['all_62_EJ_rows_all_odd_bad_places_match_formula'] is True
assert c['route_result']['next_leaf']=='36-09EN_RHO_DYADIC_LOCAL_KUMMER_BRANCH_FORMULA_PREFLIGHT'
assert c['scope_firewalls']['odd_prime_local_kummer_branch_formula_complete'] is True
assert c['scope_firewalls']['dyadic_local_kummer_branch_formula_complete'] is False
for k in ['uniform_Sel2_dimension_2_theorem','new_fixed_parameter_exclusion','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_nonexistence_claim']:
 assert c['scope_firewalls'][k] is False,k
print('36-09EM verified: every odd bad prime is P/Q/D branch and all exact EJ local images match the uniform five-case branch formula; dyadic local formula remains the sole local blocker.')
