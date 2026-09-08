#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "stages/stage32-ex4/ex4-05-lifted-krr-conjugator-cm-period-constraints-scratch.json"

def fail(msg: str) -> None:
    raise SystemExit(f"FAIL_STAGE32EX4_EX4_05_SCRATCH: {msg}")

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def canonical_hash(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def load_json(path: Path) -> tuple[dict, bytes]:
    data = path.read_bytes()
    return json.loads(data), data

a, araw = load_json(ART)
if canonical_hash(a) != a["canonical_sha256_without_this_field"]:
    fail("artifact canonical hash mismatch")

for lock in a["repo_source_locks"].values():
    p = ROOT / lock["path"]
    obj, raw = load_json(p)
    if git_blob_sha(raw) != lock["blob_sha1"]:
        fail(f"blob lock mismatch: {lock['path']}")
    if "canonical_sha256" in lock:
        got = obj.get("canonical_sha256_without_this_field")
        if got != lock["canonical_sha256"]:
            fail(f"canonical lock field mismatch: {lock['path']}")
        if canonical_hash(obj) != lock["canonical_sha256"]:
            fail(f"canonical recomputation mismatch: {lock['path']}")

K0 = (Fraction(0),) * 4
K1 = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))

def kadd(x, y):
    return tuple(x[j] + y[j] for j in range(4))

def kneg(x):
    return tuple(-v for v in x)

def kmul(x, y):
    out = [Fraction(0) for _ in range(4)]
    exps = [(0,0),(1,0),(0,1),(1,1)]
    idx = {(0,0):0,(1,0):1,(0,1):2,(1,1):3}
    for j, cx in enumerate(x):
        for k, cy in enumerate(y):
            es = exps[j][0] + exps[k][0]
            ei = exps[j][1] + exps[k][1]
            factor = Fraction(1)
            if es >= 2:
                factor *= 2
                es -= 2
            if ei >= 2:
                factor *= -1
                ei -= 2
            out[idx[(es,ei)]] += cx * cy * factor
    return tuple(out)

def frac(x):
    return Fraction(str(x))

def kcoeff(v):
    return tuple(frac(x) for x in v)

def m2mul(A, B):
    return (
        kadd(kmul(A[0],B[0]), kmul(A[1],B[2])),
        kadd(kmul(A[0],B[1]), kmul(A[1],B[3])),
        kadd(kmul(A[2],B[0]), kmul(A[3],B[2])),
        kadd(kmul(A[2],B[1]), kmul(A[3],B[3])),
    )

def m2eq(A, B):
    return all(x == y for x, y in zip(A, B))

src = a["exact_differential_intertwiner"]
phi2 = tuple(kcoeff(v) for row in src["source_phi2_matrix"] for v in row)
phi6 = tuple(kcoeff(v) for row in src["source_phi6_matrix"] for v in row)
Q0 = tuple(kcoeff(v) for row in src["Q0_normalized_q22_equals_1_field_coefficients"] for v in row)

one = K1
zero = K0
minus_one = kneg(one)
r = (Fraction(0),Fraction(0),Fraction(0),Fraction(1))
one_plus_r = kadd(one, r)
S4 = (one, one_plus_r, zero, minus_one)
Ti4 = (zero, minus_one, one, one)

if not m2eq(m2mul(phi2, Q0), m2mul(Q0, S4)):
    fail("phi2-Q0-S intertwiner identity failed")
if not m2eq(m2mul(phi6, Q0), m2mul(Q0, Ti4)):
    fail("phi6-Q0-Tinverse intertwiner identity failed")

detQ = kadd(kmul(Q0[0],Q0[3]), kneg(kmul(Q0[1],Q0[2])))
expected_det = (Fraction(2),Fraction(-1),Fraction(0),Fraction(0))
if detQ != expected_det:
    fail(f"det(Q0) mismatch: {detQ}")

if one_plus_r == zero:
    fail("1+r unexpectedly zero")
if src["projective_solution_dimension"] != 1:
    fail("artifact projective solution dimension regression")

Z0=(0,0); Z1=(1,0); Zm1=(-1,0); R=(0,1)
def zadd(x,y): return (x[0]+y[0], x[1]+y[1])
def zneg(x): return (-x[0],-x[1])
def zmul(x,y): return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def zmatmul(A,B):
    return (
        zadd(zmul(A[0],B[0]),zmul(A[1],B[2])),
        zadd(zmul(A[0],B[1]),zmul(A[1],B[3])),
        zadd(zmul(A[2],B[0]),zmul(A[3],B[2])),
        zadd(zmul(A[2],B[1]),zmul(A[3],B[3])),
    )
ZI=(Z1,Z0,Z0,Z1)
ZS=(Z1,zadd(Z1,R),Z0,Zm1)
ZT=(Z1,Z1,Zm1,Z0)

G={ZI}
q=deque([ZI])
while q:
    g=q.popleft()
    for h in (ZS,ZT):
        gh=zmatmul(g,h)
        if gh not in G:
            G.add(gh)
            q.append(gh)
if len(G) != 48:
    fail(f"target group order {len(G)} != 48")

def ztoK(z):
    return (Fraction(z[0]),Fraction(0),Fraction(0),Fraction(z[1]))
def mat_z_to_k(A):
    return tuple(ztoK(x) for x in A)

def zdet(A):
    return zadd(zmul(A[0],A[3]),zneg(zmul(A[1],A[2])))
def zinvunit(x):
    n=x[0]*x[0]+2*x[1]*x[1]
    if n != 1:
        fail(f"nonunit determinant {x}")
    return (x[0],-x[1])
def zinv(A):
    di=zinvunit(zdet(A))
    return (zmul(di,A[3]),zmul(di,zneg(A[1])),zmul(di,zneg(A[2])),zmul(di,A[0]))

for h in G:
    hi=zinv(h)
    hiK=mat_z_to_k(hi)
    Sh=zmatmul(zmatmul(h,ZS),hi)
    Tih=zmatmul(zmatmul(h,zinv(ZT)),hi)
    Qh=m2mul(Q0,hiK)
    if not m2eq(m2mul(phi2,Qh),m2mul(Qh,mat_z_to_k(Sh))):
        fail("lifted phi2 intertwiner family failed")
    if not m2eq(m2mul(phi6,Qh),m2mul(Qh,mat_z_to_k(Tih))):
        fail("lifted phi6 intertwiner family failed")

ZminusI=(Zm1,Z0,Z0,Zm1)
center=[g for g in G if zmatmul(g,ZS)==zmatmul(ZS,g) and zmatmul(g,ZT)==zmatmul(ZT,g)]
if set(center) != {ZI,ZminusI}:
    fail(f"center mismatch: {center}")
if a["lifted_target_inner_ambiguity"]["projective_inner_conjugator_count"] != len(G)//len(center):
    fail("projective inner conjugator count mismatch")

L1=(0,0,1,0); L2=(0,0,0,1); L3=(0,0,1,1)
lines=[L1,L2,L3]
def mod2_mat4(A):
    cols=[]
    basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    for v in basis:
        x1=(v[0],v[2]); x2=(v[1],v[3])
        y1=zadd(zmul(A[0],x1),zmul(A[1],x2))
        y2=zadd(zmul(A[2],x1),zmul(A[3],x2))
        cols.append((y1[0]%2,y2[0]%2,y1[1]%2,y2[1]%2))
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
def app4(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(4))%2 for i in range(4))

counts=Counter()
perms=Counter()
for h in G:
    M=mod2_mat4(h)
    image=app4(M,L2)
    if image not in lines:
        fail(f"W line escaped under unitary group: {image}")
    counts[image]+=1
    perm=tuple(lines.index(app4(M,L)) for L in lines)
    perms[perm]+=1

if counts != Counter({L1:16,L2:16,L3:16}):
    fail(f"L2 image counts mismatch: {counts}")
if len(perms) != 6 or set(perms.values()) != {8}:
    fail(f"W action not full S3 with multiplicity 8: {perms}")

rec=a["lifted_target_inner_ambiguity"]["images_of_seed_L2_under_48_markings"]
if rec != {"L1":16,"L2":16,"L3":16}:
    fail("artifact 48-marking W counts regression")
proj=a["lifted_target_inner_ambiguity"]["projective_pair_orbit_delta0inf_counts"]
if proj != {"L1":8,"L2":8,"L3":8}:
    fail("artifact projective W counts regression")

for k in ("absolute_W_line_identified","absolute_Q602_residue_identified","Q602_excluded","O210_excluded","stage32_main_credit"):
    if a["decision"][k] is not False:
        fail(f"forbidden decision credit raised: {k}")
for k,v in a["firewalls"].items():
    if v is not False:
        fail(f"firewall unexpectedly true: {k}")

if a["decision"]["next_leaf"] != "EX4-05B_FSM_THETA_LEVEL_HOMOLOGY_MARKING_PREFLIGHT":
    fail("next leaf regression")
if a["decision"]["retained_claim_dag_sync_performed"] is not False:
    fail("claim DAG sync unexpectedly asserted")

print("PASS_STAGE32EX4_EX4_05_SCRATCH_LIFTED_DIFFERENTIAL_PERIOD")
print("target_group_order=48 center_order=2 projective_inner_conjugators=24")
print("literal_Q0_det=2-sqrt2")
print("seed_L2_images=L1:16,L2:16,L3:16; projective_pair_orbit=8/8/8")
print("absolute_W_line=false absolute_Q602_residue=false")
print("next=EX4-05B_FSM_THETA_LEVEL_HOMOLOGY_MARKING_PREFLIGHT")
