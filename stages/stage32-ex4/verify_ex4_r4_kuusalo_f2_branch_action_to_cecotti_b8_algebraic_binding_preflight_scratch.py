#!/usr/bin/env python3
import hashlib, itertools, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = json.loads((ROOT / "stages/stage32-ex4/ex4-r4-kuusalo-f2-branch-action-to-cecotti-b8-algebraic-binding-preflight-scratch.json").read_text())
R3 = json.loads((ROOT / "stages/stage32-ex4/ex4-r3-kuusalo-second-generator-pair-preflight-scratch.json").read_text())
W = json.loads((ROOT / "stages/stage32/residual-32-01-production/post1505-o210-q4-x8-v4-torsor-plane-weierstrass-lock.json").read_text())

raw = dict(ART)
expected_hash = raw.pop("canonical_sha256_without_this_field")
canon = json.dumps(raw, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
assert hashlib.sha256(canon).hexdigest() == expected_hash == "0718f53281b215c668fbb7bb44b4b9c3e44a86cc64ba21dbcaaad4234f943679"
assert ART["prior_r3"]["canonical_sha256"] == R3["canonical_sha256_without_this_field"]
assert ART["source_locks"]["abstract_weierstrass"]["canonical_sha256"] == W["canonical_sha256_without_this_field"]

labels = ["infinity", "0", "+1", "+i", "-1", "-i"]
idx = {x:i for i,x in enumerate(labels)}
J = [[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]
M1 = [[x % 2 for x in row] for row in ART["source_convention"]["f1_h1_matrix"]]
M2 = [[x % 2 for x in row] for row in ART["source_convention"]["f2_h1_matrix"]]
d0 = tuple(ART["source_convention"]["source_delta0inf_coordinate_mod2"])
zero = (0,0,0,0)

def add(a,b): return tuple(x^y for x,y in zip(a,b))
def matvec(M,v): return tuple(sum(M[i][j]*v[j] for j in range(4)) % 2 for i in range(4))
def pairing(a,b):
    return sum(a[i]*J[i][j]*b[j] for i in range(4) for j in range(4)) % 2

def compose(p,q):
    # p o q
    return tuple(p[q[i]] for i in range(6))
def invperm(p):
    q=[0]*6
    for i,j in enumerate(p): q[j]=i
    return tuple(q)
def perm_order(p):
    cur=tuple(range(6))
    for n in range(1,25):
        cur=compose(p,cur)
        if cur==tuple(range(6)): return n
    raise AssertionError("order too large")

r = tuple(idx[x] for x in ["infinity","0","+i","-1","-i","+1"])
m = tuple(idx[x] for x in ["+i","-i","0","-1","infinity","+1"])
assert perm_order(r)==4
assert perm_order(m)==3

# Build all branch-to-J2 embeddings under R1 convention.
embeddings=[]
for bits in itertools.product([0,1], repeat=4):
    q1=tuple(bits)
    if q1==zero: continue
    emb={"infinity":zero, "0":d0, "+1":q1}
    emb["+i"] = matvec(M1, emb["+1"])
    emb["-1"] = matvec(M1, emb["+i"])
    emb["-i"] = matvec(M1, emb["-1"])
    # f1 quarter-turn must close.
    if matvec(M1, emb["-i"]) != emb["+1"]: continue
    vals=[emb[x] for x in labels]
    if len(set(vals)) != 6: continue
    noninf=[emb[x] for x in labels if x!="infinity"]
    if not all(pairing(a,b)==1 for a,b in itertools.combinations(noninf,2)): continue
    embeddings.append(emb)
assert len(embeddings)==8

# Pair-difference characterizes unordered Weierstrass pairs. Push differences by M2,
# then recover the unique permutation of six branch labels for each embedding.
def edge_map(emb):
    out={}
    for i in range(6):
        for j in range(i+1,6):
            out[add(emb[labels[i]],emb[labels[j]])]=(i,j)
    assert len(out)==15
    return out

perms=[]
for emb in embeddings:
    e2=edge_map(emb)
    pushed={}
    for i in range(6):
        for j in range(i+1,6):
            v=matvec(M2, add(emb[labels[i]],emb[labels[j]]))
            pushed[(i,j)] = tuple(sorted(e2[v]))
    found=[]
    for p in itertools.permutations(range(6)):
        ok=True
        for i in range(6):
            for j in range(i+1,6):
                if tuple(sorted((p[i],p[j]))) != pushed[(i,j)]:
                    ok=False; break
            if not ok: break
        if ok: found.append(tuple(p))
    assert len(found)==1
    perms.append(found[0])

counts=Counter(perms)
assert len(counts)==4
assert set(counts.values())=={2}

# The four exact candidates are the quarter-turn conjugates of Cecotti B.8.
conjs=[]
cur=tuple(range(6))
for k in range(4):
    rk=cur
    conjs.append(compose(compose(rk,m),invperm(rk)))
    cur=compose(r,cur)
assert set(counts)==set(conjs)
assert all(perm_order(p)==3 for p in conjs)
assert all(perm_order(compose(r,p))==2 for p in conjs)
assert m in counts

artifact_perms=[]
for row in ART["f2_branch_permutation_candidates"]:
    artifact_perms.append(tuple(idx[row["permutation"][x]] for x in labels))
    assert row["embedding_multiplicity"]==2
assert set(artifact_perms)==set(conjs)
assert sum(1 for row in ART["f2_branch_permutation_candidates"] if row["equals_literal_Cecotti_B8_reduced_map"])==1

assert ART["finite_weierstrass_embedding_reconstruction"]["compatible_full_branch_embeddings"]==8
assert ART["finite_weierstrass_embedding_reconstruction"]["distinct_f2_branch_permutations"]==4
assert ART["finite_weierstrass_embedding_reconstruction"]["multiplicity_per_distinct_f2_branch_permutation"]==2
assert ART["group_crosscheck"]["literal_B8_is_admissible_but_not_unique"] is True
assert ART["decision"]["literal_Kuusalo_f2_equals_Cecotti_B8_proved"] is False
assert ART["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert ART["decision"]["absolute_Q602_residue_identified"] is False
assert ART["decision"]["conditional_residue97_only"] is True
for k,v in ART["firewalls"].items():
    assert v is False, k

print("Stage32EX4 R4 finite branch-action preflight: PASS")
print("compatible branch->J2 embeddings=8")
print("distinct f2 branch permutations=4, multiplicity=2 each")
print("all four = r^k * B8 * r^-k, k=0..3")
print("literal B8 admissible but not source-selected; residue97 remains conditional")
