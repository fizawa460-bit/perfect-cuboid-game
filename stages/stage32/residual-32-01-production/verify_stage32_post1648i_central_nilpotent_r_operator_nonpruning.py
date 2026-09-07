#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648i-central-nilpotent-r-operator-nonpruning.json"
EXPECTED = "f42d3e56581b489ddb45fb6540a3ed74f29fde2142d7c12f9b6291b5b651687d"
I4 = (1,2,4,8)
ZERO4 = (0,0,0,0)


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    field = "canonical_sha256_without_this_field" if "canonical_sha256_without_this_field" in body else "canonical_sha256"
    claimed = body.pop(field)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def load_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file()
    assert blob_sha1(path) == lock["blob_sha1"]
    doc = json.loads(path.read_text())
    assert canonical(doc) == lock["canonical_sha256"]
    return doc


def from_rows(rows):
    return tuple(sum((int(x)&1)<<j for j,x in enumerate(row)) for row in rows)


def rows_list(A):
    return [[(A[i]>>j)&1 for j in range(4)] for i in range(4)]


def mat_vec(A, v: int) -> int:
    out=0
    for i,row in enumerate(A):
        if (row & v).bit_count() & 1:
            out |= 1<<i
    return out


def mat_mul(A,B):
    rows=[]
    for i in range(4):
        row=0
        for j in range(4):
            bit=0
            for k in range(4):
                bit ^= ((A[i]>>k)&1) & ((B[k]>>j)&1)
            row |= bit<<j
        rows.append(row)
    return tuple(rows)


def mat_transpose(A):
    return tuple(sum(((A[j]>>i)&1)<<j for j in range(4)) for i in range(4))


def mat_inv(A):
    rows=[A[i] | ((1<<i)<<4) for i in range(4)]
    for col in range(4):
        pivot=next((i for i in range(col,4) if (rows[i]>>col)&1),None)
        if pivot is None:
            return None
        rows[col],rows[pivot]=rows[pivot],rows[col]
        for i in range(4):
            if i!=col and ((rows[i]>>col)&1):
                rows[i]^=rows[col]
    return tuple((rows[i]>>4)&15 for i in range(4))


def close_group(gens):
    group={I4}
    stack=[I4]
    while stack:
        a=stack.pop()
        for g in gens:
            b=mat_mul(a,g)
            if b not in group:
                group.add(b); stack.append(b)
    return group


def kernel(A):
    return frozenset(v for v in range(16) if mat_vec(A,v)==0)


def image(A):
    return frozenset(mat_vec(A,v) for v in range(16))


def rank(A):
    rows=list(A); r=0
    for col in range(4):
        pivot=next((i for i in range(r,4) if (rows[i]>>col)&1),None)
        if pivot is None: continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        for i in range(4):
            if i!=r and ((rows[i]>>col)&1): rows[i]^=rows[r]
        r+=1
    return r


cert=json.loads(CERT_PATH.read_text())
assert canonical(cert)==EXPECTED
c=load_lock(cert["source_locks"]["post1648c"])
rosati=load_lock(cert["source_locks"]["principal_rosati"])

S2=from_rows(c["source_J2_model"]["phi2_matrix_f2"])
S6=from_rows(c["source_J2_model"]["phi6_matrix_f2"])
source_group=close_group([S2,S6])
assert len(source_group)==24

tg=c["target_J2_model"]["principal_generators_mod2"]
b1,b2,b3,b4=(from_rows(tg[x]) for x in ("b1","b2","b3","b4"))
target_group=close_group([b1,b2,b3,b4])
assert len(target_group)==24

source_W=frozenset({0,1,6,7})
target_W=frozenset({0,4,8,12})

source_cent=[]
target_cent=[]
for rows in itertools.product(range(16),repeat=4):
    A=tuple(rows)
    if all(mat_mul(A,g)==mat_mul(g,A) for g in source_group): source_cent.append(A)
    if all(mat_mul(A,g)==mat_mul(g,A) for g in target_group): target_cent.append(A)
assert len(source_cent)==4
assert len(target_cent)==4

source_special=[A for A in source_cent if A!=ZERO4 and mat_mul(A,A)==ZERO4 and rank(A)==2 and kernel(A)==source_W and image(A)==source_W]
target_special=[A for A in target_cent if A!=ZERO4 and mat_mul(A,A)==ZERO4 and rank(A)==2 and kernel(A)==target_W and image(A)==target_W]
assert len(source_special)==1
assert len(target_special)==1
Ns=source_special[0]
Nt=target_special[0]
assert rows_list(Ns)==cert["source_centralizer"]["operator_matrix_f2"]

# Scalar multiplication by r in basis (e1,e2,r*e1,r*e2): e1->r*e1, e2->r*e2, r*ei->0 mod 2.
rmod2=from_rows([[0,0,0,0],[0,0,0,0],[1,0,0,0],[0,1,0,0]])
assert Nt==rmod2
assert rows_list(rmod2)==cert["target_centralizer"]["scalar_r_mod2_matrix_in_basis_e1_e2_re1_re2"]
assert rosati["quadratic_order"]["relation"]=="r^2=-2"
assert rosati["principal_polarization"]["riemann_form_basis"]==["e1","e2","r*e1","r*e2"]

Esource=from_rows(c["source_J2_model"]["weil_form_matrix_f2"])
Etarget=from_rows(c["target_J2_model"]["riemann_form_matrix_f2"])
target_keys=set(target_group)
conjugacies=[]
for rows in itertools.product(range(16),repeat=4):
    P=tuple(rows)
    Pinv=mat_inv(P)
    if Pinv is None: continue
    if mat_mul(mat_mul(P,S2),Pinv) not in target_keys: continue
    if mat_mul(mat_mul(P,S6),Pinv) not in target_keys: continue
    if mat_mul(mat_mul(mat_transpose(P),Etarget),P)!=Esource: continue
    conjugacies.append((P,Pinv))
assert len(conjugacies)==48
maps_r=[P for P,Pinv in conjugacies if mat_mul(mat_mul(P,Ns),Pinv)==rmod2]
assert len(maps_r)==48

line_names={4:"L1",8:"L2",12:"L3"}
line_maps=set()
for P,_ in conjugacies:
    line_maps.add(tuple(line_names[mat_vec(P,z)] for z in (1,6,7)))
assert len(line_maps)==6
assert {m[2] for m in line_maps}=={"L1","L2","L3"}

assert cert["source_centralizer"]["centralizer_in_M4_F2_order"]==4
assert cert["target_centralizer"]["centralizer_in_M4_F2_order"]==4
assert cert["conjugacy_test"]["post1648c_symplectic_group_conjugacies"]==48
assert cert["conjugacy_test"]["conjugacies_mapping_source_operator_to_target_r"]==48
assert cert["conjugacy_test"]["pruning_count"]==0
assert cert["conjugacy_test"]["remaining_W_line_bijections"]==6
assert cert["decision"]["source_operator_promoted_to_geometric_sqrt_minus_2_endomorphism"] is False
assert cert["decision"]["survivors_current_credit"]==[73,97,235]
assert cert["decision"]["Q602_excluded"] is False and cert["decision"]["O210_excluded"] is False
assert not any(cert["firewalls"].values())

print("POST1648I_CENTRAL_NILPOTENT_R_OPERATOR_NONPRUNING_COMPLETE")
print(f"certificate_canonical={EXPECTED}")
print("source_centralizer=4 target_centralizer=4 unique_nilpotent_each=true")
print("symplectic_conjugacies=48 mapping_unique_source_N_to_target_r=48 pruning=0")
print("W_line_bijections=6 delta0inf_possible=L1,L2,L3")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
