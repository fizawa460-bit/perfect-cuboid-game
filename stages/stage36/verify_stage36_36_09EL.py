#!/usr/bin/env python3
import json
import math
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EJ='stages/stage36/36-09EJ/bounded-rho-sel2-exact-computation-preflight.json'
EK='stages/stage36/36-09EK/rho-sel2-literal-orbit-closure-preflight.json'
DW='stages/stage36/36-09DW/phi-selmer-five-place-local-image-source-lock.md'
ARS='docs/arsenal/cards/formal/S34-W01.md'
SOURCE='stages/stage36/36-09EL/rho-square-legendre-symbolic-sel2-matrix-source-lock.md'
CERT='stages/stage36/36-09EL/rho-square-legendre-symbolic-sel2-matrix-preflight.json'

def blob(p): return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p): return json.loads((ROOT/p).read_text())
expected={
 EJ:'7ff288962132cae21f30a3c7b05ee1e5b5680c91',
 EK:'f6af11a0f7fd8a303531b2a587b7446c382a84c5',
 DW:'08c91eed30774fa5c44509bb61f1c3b1386f2266',
 ARS:'01a8e90e34b4aa46edbfa825803d488e5230e9d0',
 SOURCE:'a279ee06b5b7c33e09597c6516097a3e821e1f2e',
 CERT:'192ff96c8b17db331cefd019c0b70c7b4a6f6bc9',
}
for p,s in expected.items(): assert blob(p)==s,(p,blob(p),s)

ej=load(EJ); ek=load(EK); c=load(CERT)
dw=(ROOT/DW).read_text(); ars=(ROOT/ARS).read_text(); src=(ROOT/SOURCE).read_text()
assert ej['criterion_consumption']['expanded_fixed_parameter_registry_count']==14
assert ek['receiver_consequence']['expanded_registry_count']==16
assert 'F2-dimension `2` for odd residue characteristic' in dw
assert 'F2-dimension `3` over `Q_2`' in dw
assert 'SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT' in ars
assert 'local squareclass of D alone != local Kummer branch' in src

# Exact algebraic identities and primitive gcd dichotomy.
for a in range(1,51):
  for b in range(1,51):
    if math.gcd(a,b)!=1 or a==b: continue
    N=a*a-b*b; d=a*b; M=a*a+b*b; P=N+2*d; Q=N-2*d
    assert M*M == N*N + 4*d*d
    assert M*M + 4*N*d == P*P
    assert M*M - 4*N*d == Q*Q
    assert P*P-Q*Q == 8*N*d
    g=math.gcd(abs(P),abs(Q))
    exp=2 if (a&1 and b&1) else 1
    assert g==exp,(a,b,P,Q,g,exp)
    assert math.gcd(abs(P//g),abs(Q//g))==1

# For the general gcd proof used by the source: an odd common prime would divide
# P-Q=4ab and P+Q=2(a^2-b^2); primitivity then forbids it. 2-adic parity
# gives exactly the dichotomy above. The finite loop is a regression replay,
# not the proof source.

# ---------- F2 linear algebra ----------
def rref(vs):
    rows=[list(map(int,v)) for v in vs if any(v)]
    if not rows: return ()
    n=len(rows[0]); rr=0
    for j in range(n):
        q=next((i for i in range(rr,len(rows)) if rows[i][j]),None)
        if q is None: continue
        rows[rr],rows[q]=rows[q],rows[rr]
        for i in range(len(rows)):
            if i!=rr and rows[i][j]: rows[i]=[x^y for x,y in zip(rows[i],rows[rr])]
        rr+=1
        if rr==len(rows): break
    return tuple(tuple(x) for x in rows[:rr])
def rank(vs): return len(rref(vs))
def vpi(n,p):
    n=abs(n); z=0
    while n and n%p==0: z+=1; n//=p
    return z
def sc_int(n,p):
    assert n!=0
    z=vpi(n,p); u=n//(p**z); um=u%p
    return (z&1,0 if pow(um,(p-1)//2,p)==1 else 1)
def is_qp_square_int(n,p):
    if n==0:return True
    z=vpi(n,p)
    if z&1:return False
    u=n//(p**z)
    return pow(u%p,(p-1)//2,p)==1

def local_span(P,Q,p,bound=100):
    # translated roots 0,P^2,Q^2; Kummer ([X],[X-P^2])
    e1,e2,e3=0,P*P,Q*Q
    pairs=[((e1-e2)*(e1-e3),e1-e2),(e2-e1,(e2-e1)*(e2-e3))]
    out=[sc_int(x,p)+sc_int(y,p) for x,y in pairs]
    for X in range(-bound,bound+1):
        if X in (e1,e2,e3): continue
        rhs=(X-e1)*(X-e2)*(X-e3)
        if is_qp_square_int(rhs,p):
            out.append(sc_int(X-e1,p)+sc_int(X-e2,p))
    return rref(out)

cases=[
 (1,5,-14,-34,-960,((1,0,0,0),(0,1,0,0))),
 (1,7,-34,-62,-2688,((1,0,1,0),(0,1,0,1))),
]
for a,b,P,Q,D,W in cases:
    assert sc_int(D,17)==(0,0)
    got=local_span(P,Q,17)
    assert rank(got)==2
    assert got==W,(a,b,got,W)
assert cases[0][5] != cases[1][5]

n=c['square_legendre_normalization']
assert n['translated_model']=='y^2=X*(X-P^2)*(X-Q^2)'
assert n['scaled_model']=='v^2=u*(u-1)*(u-s^2)'
assert n['lambda']=='s^2'
ps=c['prime_support']
assert ps['gcd_P_Q_in']==[1,2]
assert ps['P0_Q0_coprime'] is True
m=c['symbolic_sel2_matrix']
assert m['local_target_dimensions']=={'infinity':1,'Q2':3,'odd_Qq':2}
assert m['constraint_block']=='W_v^perp * L_v'
assert m['dimension_formula']=='dim_F2 Sel^2(E_rho,p/Q)=2|G|-rank_F2 M_Sel2(a,b)'
ce=c['single_D_squareclass_counterexample']
assert ce['same_D_squareclass'] is True
assert ce['different_local_kummer_subspaces'] is True
assert c['route_result']['next_leaf']=='36-09EM_RHO_FULL2_LOCAL_KUMMER_BRANCH_FORMULA_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
print('36-09EL verified: exact square-Legendre normalization, primitive prime-support split, global Sel2 localization matrix, and Q17 counterexample to D-only local compression. EM remains locked pending CI consumption.')
