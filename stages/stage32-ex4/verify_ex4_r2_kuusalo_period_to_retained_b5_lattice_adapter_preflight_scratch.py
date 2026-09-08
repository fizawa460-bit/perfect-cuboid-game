#!/usr/bin/env python3
import json, hashlib
from collections import Counter, deque, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "stages/stage32-ex4/ex4-r2-kuusalo-period-to-retained-b5-lattice-adapter-preflight-scratch.json"
R1 = ROOT / "stages/stage32-ex4/ex4-r1-kuusalo-branch-labelled-h1-reentry-scratch.json"
ROSATI = ROOT / "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-principal-rosati-lock.json"

data = json.loads(ART.read_text())
r1 = json.loads(R1.read_text())
rosati = json.loads(ROSATI.read_text())

def canonical_sha(obj):
    d = dict(obj)
    d.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

assert canonical_sha(data) == data["canonical_sha256_without_this_field"]
assert data["status"].startswith("SCRATCH_REPLAYABLE_")
assert r1["canonical_sha256_without_this_field"] == data["source_locks"]["r1"]["canonical_sha256"]
assert rosati["canonical_sha256_without_this_field"] == data["retained_principal_lattice"]["source_lock"]["canonical_sha256"]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mt(A): return [list(x) for x in zip(*A)]
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mneg(A): return [[-x for x in row] for row in A]
def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def key(A): return tuple(x for row in A for x in row)
def mv(A,v): return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
def powm(A,n):
    R=eye(len(A)); X=A
    while n:
        if n&1: R=mm(R,X)
        X=mm(X,X); n//=2
    return R

def inv_int(A):
    n=len(A)
    aug=[[Fraction(A[i][j]) for j in range(n)] + [Fraction(1 if i==j else 0) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if aug[i][c])
        aug[c],aug[p]=aug[p],aug[c]
        z=aug[c][c]
        aug[c]=[x/z for x in aug[c]]
        for i in range(n):
            if i==c: continue
            z=aug[i][c]
            if z:
                aug[i]=[aug[i][j]-z*aug[c][j] for j in range(2*n)]
    out=[[aug[i][n+j] for j in range(n)] for i in range(n)]
    assert all(x.denominator==1 for row in out for x in row)
    return [[int(x) for x in row] for row in out]

J=[[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]]
E=data["retained_principal_lattice"]["riemann_form"]
U=data["retained_principal_lattice"]["darboux_change_columns_raw_basis"]
Uinv=inv_int(U)
assert mm(mm(mt(U),E),U)==J

def q(a=0,b=0): return (Fraction(a),Fraction(b))
def qa(x,y): return (x[0]+y[0],x[1]+y[1])
def qn(x): return (-x[0],-x[1])
def qs(x,y): return qa(x,qn(y))
def qm(x,y): return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def qi(x):
    den=x[0]*x[0]+2*x[1]*x[1]
    assert den
    return (x[0]/den,-x[1]/den)
Q0=q()
def sumq(xs):
    z=Q0
    for x in xs: z=qa(z,x)
    return z
def qmi(A): return [[q(x) for x in row] for row in A]
def qmm(A,B):
    return [[sumq([qm(A[i][k],B[k][j]) for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]
def qma(A,B): return [[qa(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def qeq(A,B): return A==B

r=q(0,1)
tauR=[[q(Fraction(1,2),Fraction(1,2)), q(Fraction(-1,2),0)],
      [q(Fraction(-1,2),0), q(Fraction(-1,2),Fraction(1,2))]]
tauK=[[q(Fraction(1,3),Fraction(2,3)), q(Fraction(-2,3),Fraction(-1,3))],
      [q(Fraction(-2,3),Fraction(-1,3)), q(Fraction(1,3),Fraction(2,3))]]

Praw=[[q(1),q(0),r,q(0)],[q(0),q(1),q(0),r]]
Pstd=qmm(Praw,qmi(U))
OA=[row[:2] for row in Pstd]
OB=[row[2:] for row in Pstd]
assert qeq(qmm(OA,tauR),OB)

def blocks(G):
    return ([row[:2] for row in G[:2]],[row[2:] for row in G[:2]],
            [row[:2] for row in G[2:]],[row[2:] for row in G[2:]])

def period_maps(G,t1,t2):
    A,B,C,D=blocks(G)
    left=qmm(qma(qmi(A),qmm(t1,qmi(C))),t2)
    right=qma(qmi(B),qmm(t1,qmi(D)))
    return qeq(left,right)

S=data["retained_g12"]["raw_generators"]["S"]
T=data["retained_g12"]["raw_generators"]["T"]
assert mm(mm(mt(S),E),S)==E
assert mm(mm(mt(T),E),T)==E
Sstd=mm(mm(Uinv,S),U)
Tstd=mm(mm(Uinv,T),U)
assert mm(mm(mt(Sstd),J),Sstd)==J
assert mm(mm(mt(Tstd),J),Tstd)==J
assert period_maps(Sstd,tauR,tauR)
assert period_maps(Tstd,tauR,tauR)

def generate_group(gens):
    I=eye(4); seen={key(I):I}; dq=deque([I])
    while dq:
        X=dq.popleft()
        for G in gens:
            Y=mm(X,G); ky=key(Y)
            if ky not in seen:
                seen[ky]=Y; dq.append(Y)
    return seen

std_group=generate_group([Sstd,Tstd])
raw_group=generate_group([S,T])
assert len(std_group)==48
assert len(raw_group)==48

G0=data["period_adapter_convention"]["seed_symplectic_adapter_G0"]
assert mm(mm(mt(G0),J),G0)==J
assert period_maps(G0,tauR,tauK)

adapters=[mm(H,G0) for H in std_group.values()]
assert len({key(G) for G in adapters})==48
assert all(mm(mm(mt(G),J),G)==J for G in adapters)
assert all(period_maps(G,tauR,tauK) for G in adapters)

delta=data["delta0inf_transport"]["kuusalo_coordinate_mod2"]
line_map={(0,0,1,0):"L1",(0,0,0,1):"L2",(0,0,1,1):"L3"}
def transport_delta(G):
    return tuple(x&1 for x in mv(mm(U,G),delta))
counts=Counter(line_map.get(transport_delta(G),"OTHER") for G in adapters)
assert counts==Counter({"L1":16,"L2":16,"L3":16})
assert "OTHER" not in counts

M1=data["kuusalo_period"]["f1_h1_matrix"]
assert mm(mm(mt(M1),J),M1)==J
assert powm(M1,4)==mneg(eye(4))
assert powm(M1,8)==eye(4)

def conj_raw(G):
    return mm(mm(mm(mm(U,G),M1),inv_int(G)),Uinv)

induced=[conj_raw(G) for G in adapters]
uniq={key(M):M for M in induced}
assert len(uniq)==6
assert all(key(M) in raw_group for M in uniq.values())

Tinv=inv_int(T)
Araw=mm(S,Tinv)
conjclass={}
for H in raw_group.values():
    M=mm(mm(H,Araw),inv_int(H))
    conjclass[key(M)]=M
assert len(conjclass)==6
assert set(uniq)==set(conjclass)

mult=Counter(key(M) for M in induced)
assert set(mult.values())=={8}

element_lines=defaultdict(set)
for G,M in zip(adapters,induced):
    v=transport_delta(G)
    assert tuple(x&1 for x in mv(M,list(v)))==v
    element_lines[key(M)].add(line_map[v])
assert all(len(s)==1 for s in element_lines.values())
per_line=Counter(next(iter(s)) for s in element_lines.values())
assert per_line==Counter({"L1":2,"L2":2,"L3":2})

literal=[G for G,M in zip(adapters,induced) if M==Araw]
assert len(literal)==8
assert {transport_delta(G) for G in literal}=={(0,0,0,1)}

M2=data["kuusalo_period"]["f2_h1_matrix_reserved_next"]
assert mm(mm(mt(M2),J),M2)==J
assert powm(M2,3)==eye(4)

assert data["delta0inf_transport"]["line_counts_across_48_adapters"]=={"L1":16,"L2":16,"L3":16}
assert data["transported_B9_order8_action"]["distinct_target_elements"]==6
assert data["transported_B9_order8_action"]["adapter_multiplicity_per_target_element"]==8
assert data["transported_B9_order8_action"]["target_class_elements_per_fixed_W_line"]=={"L1":2,"L2":2,"L3":2}
assert data["transported_B9_order8_action"]["literal_A_equals_S_Tinverse"]["compatible_adapter_count"]==8
assert data["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert data["decision"]["absolute_Q602_residue_identified"] is False
assert data["decision"]["Q602_excluded"] is False
assert data["decision"]["O210_excluded"] is False
assert data["decision"]["stage32_main_credit"] is False

print("Stage32EX4 R2 Kuusalo period adapter preflight: PASS")
print("period_adapters=48 delta_lines=L1:16,L2:16,L3:16")
print("transported_f1_targets=6=conjugacy_class(S*T^-1), multiplicity=8 each")
print("literal_STinverse_adapters=8 -> L2 -> conditional residue 97")
print("absolute_marking=false Q602_excluded=false O210_excluded=false stage32_main_credit=false")
