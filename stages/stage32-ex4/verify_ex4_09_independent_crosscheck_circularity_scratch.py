#!/usr/bin/env python3
import hashlib
import itertools
import json
import subprocess
from collections import Counter, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ARTIFACT = HERE / "ex4-09-independent-crosscheck-circularity-audit-scratch.json"

ZERO=(0,0); ONE=(1,0); MONE=(-1,0); R=(0,1)
def radd(x,y): return (x[0]+y[0],x[1]+y[1])
def rneg(x): return (-x[0],-x[1])
def rmul(x,y):
    return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def mmul(A,B):
    return tuple(tuple(radd(rmul(A[i][0],B[0][j]),rmul(A[i][1],B[1][j]))
                       for j in range(2)) for i in range(2))
I=((ONE,ZERO),(ZERO,ONE))
S=((ONE,radd(ONE,R)),(ZERO,MONE))
T=((ONE,ONE),(MONE,ZERO))
def det(A): return radd(rmul(A[0][0],A[1][1]),rneg(rmul(A[0][1],A[1][0])))
def minv(A):
    d=det(A)
    assert d in (ONE,MONE)
    dinv=d
    adj=((A[1][1],rneg(A[0][1])),(rneg(A[1][0]),A[0][0]))
    return tuple(tuple(rmul(dinv,adj[i][j]) for j in range(2)) for i in range(2))
TINV=minv(T)

def generate_group():
    gens=(S,T,minv(S),TINV)
    seen={I}; q=deque([I])
    while q:
        g=q.popleft()
        for a in gens:
            h=mmul(g,a)
            if h not in seen:
                seen.add(h); q.append(h)
    return seen

L1=(0,0,1,0); L2=(0,0,0,1); L3=(0,0,1,1); LINES=(L1,L2,L3)
def mod2_mat4(A):
    ar=[[A[i][j][0]&1 for j in range(2)] for i in range(2)]
    br=[[A[i][j][1]&1 for j in range(2)] for i in range(2)]
    M=[[0]*4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            M[i][j]=ar[i][j]
            M[i+2][j]=br[i][j]
            M[i+2][j+2]=ar[i][j]
    return tuple(tuple(row) for row in M)
def act4(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(4))&1 for i in range(4))
def line_perm(A):
    imgs=tuple(act4(mod2_mat4(A),v) for v in LINES)
    assert set(imgs)==set(LINES)
    return tuple(LINES.index(x) for x in imgs)
def conj(h,a): return mmul(mmul(h,a),minv(h))

def canonical_sha256(data):
    d=dict(data)
    expected=d.pop("canonical_sha256_without_this_field")
    got=hashlib.sha256(json.dumps(d,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
    assert got==expected,(got,expected)
    return got

def git_blob_sha(path):
    return subprocess.check_output(["git","-C",str(ROOT),"hash-object",str(path)],text=True).strip()

def check_locks(data):
    for item in data["source_locks"].values():
        path=ROOT/item["path"]
        assert path.exists(),item["path"]
        assert git_blob_sha(path)==item["blob_sha1"],item["path"]
        if "canonical_sha256" in item and path.suffix==".json":
            obj=json.loads(path.read_text())
            assert obj.get("canonical_sha256_without_this_field")==item["canonical_sha256"],item["path"]

def equivariant_bijections(target_phi2,target_phi6):
    source_phi2=(0,2,1)
    source_phi6=(2,0,1)
    out=[]
    for f in itertools.permutations(range(3)):
        if all(f[source_phi2[i]]==target_phi2[f[i]] and f[source_phi6[i]]==target_phi6[f[i]]
               for i in range(3)):
            out.append(f)
    return out

def main():
    data=json.loads(ARTIFACT.read_text())
    canonical_sha256(data)
    check_locks(data)

    G=generate_group()
    assert len(G)==48
    perms=Counter(line_perm(g) for g in G)
    assert len(perms)==6 and set(perms.values())=={8}

    pair_classes={}
    for h in G:
        pair=(conj(h,S),conj(h,TINV))
        pair_classes.setdefault(pair,[]).append(h)
    assert len(pair_classes)==24
    assert set(len(v) for v in pair_classes.values())=={2}

    # Independent source-Z to target-W enumeration. Decimal Q602 residue labels
    # are intentionally absent from this computation.
    bijection_counts=Counter()
    delta_counts=Counter()
    representatives=[]
    for pair,hs in pair_classes.items():
        representatives.append(hs[0])
        p2=line_perm(pair[0]); p6=line_perm(pair[1])
        eq=equivariant_bijections(p2,p6)
        assert len(eq)==1
        f=eq[0]
        bijection_counts[f]+=1
        delta_counts[f[2]]+=1
    assert len(bijection_counts)==6
    assert set(bijection_counts.values())=={4}
    assert delta_counts==Counter({0:8,1:8,2:8})

    # Gauge/seed independence: any of the three W lines has the same 8/8/8
    # projective orbit among the 24 pair classes.
    seed_counts={}
    for i,name in enumerate(("seed_L1","seed_L2","seed_L3")):
        c=Counter(line_perm(h)[i] for h in representatives)
        assert c==Counter({0:8,1:8,2:8})
        seed_counts[name]={"L1":c[0],"L2":c[1],"L3":c[2]}
    assert seed_counts==data["independent_replay"]["seed_line_invariance"]

    replay=data["independent_replay"]
    assert replay["G_order"]==48
    assert replay["W_action_image_order"]==6
    assert replay["projective_pair_classes"]==24
    assert replay["source_to_W_bijections"]==6
    assert replay["bijection_multiplicity"]==4
    assert replay["delta0inf_line_counts"]=={"L1":8,"L2":8,"L3":8}

    for name,check in data["circularity_checks"].items():
        assert check["result"]=="PASS",name

    assert data["dependency_direction"]["forbidden_feedback_absent"] is True
    assert data["terminal_input_assessment"]["roadmap_exit"]=="TERMINAL_CERTIFICATE_INPUTS_INDEPENDENT"
    assert data["terminal_input_assessment"]["result"]=="PASS_CANDIDATE"

    dec=data["decision"]
    assert dec["result"]=="EX4_09_TERMINAL_CERTIFICATE_INPUTS_INDEPENDENT_CANDIDATE"
    assert dec["next_leaf"]=="EX4-10_BOUNDED_TERMINAL_DECISION_CERTIFICATE_ASSEMBLY"
    for key in ("absolute_W_line_identified","absolute_Q602_residue_identified","Q602_excluded","O210_excluded","stage32_main_credit"):
        assert dec[key] is False

    # No Stage33 artifact is allowed to become an EX4-09 source lock.
    assert all("/stage33/" not in item["path"] for item in data["source_locks"].values())

    print(json.dumps({
        "artifact":ARTIFACT.name,
        "canonical_sha256":data["canonical_sha256_without_this_field"],
        "G_order":len(G),
        "projective_pair_classes":len(pair_classes),
        "distinct_source_to_W_bijections":len(bijection_counts),
        "delta0inf_line_counts":{"L1":delta_counts[0],"L2":delta_counts[1],"L3":delta_counts[2]},
        "seed_line_invariance":seed_counts,
        "circularity_checks":"PASS",
        "result":dec["result"]
    },indent=2))

if __name__=="__main__":
    main()
