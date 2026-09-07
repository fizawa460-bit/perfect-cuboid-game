#!/usr/bin/env python3
from __future__ import annotations

import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
N_PATH = HERE / "post1648n-canonical-period-marked-ppav-torsor-obstruction.json"
O_PATH = HERE / "post1648o-b9-zero-translation-conjugacy-nonpruning.json"
Q_PATH = HERE / "post1648q-full-torus-translation-conjugacy-nonpruning.json"

EXPECTED_N_CANON = "060d940626cd59b00efb67db7f27914e6a440c92968600a3d82a208d5a5d76ba"
EXPECTED_N_BLOB = "0ee05f679c7706113feed2c217e08a95b3bd6f06"
EXPECTED_O_CANON = "6ad188aaf14aa9998ac27efc5737e79666b300cdccf2312d9c2b250f8e8a02ef"
EXPECTED_O_BLOB = "3636be221c73fa2ec023ee0a6238f2e857089562"
EXPECTED_Q_CANON = "9d7cec0d381e4524873be1dd1837e55fb99b1f38ec384ac79cface5bfe26af18"

def canonical(obj):
    body=dict(obj)
    body.pop("canonical_sha256_without_this_field",None)
    raw=json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def blob(path):
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def eye():
    return [[1 if i==j else 0 for j in range(4)] for i in range(4)]

def neg(A):
    return [[-x for x in row] for row in A]

def det4(M):
    import itertools
    total=0
    for p in itertools.permutations(range(4)):
        inv=sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])
        term=1
        for i in range(4):
            term*=M[i][p[i]]
        total+=(-1 if inv%2 else 1)*term
    return total

def powm(A,n):
    out=eye()
    for _ in range(n):
        out=mm(out,A)
    return out

def real_matrix(entries):
    alpha,beta,gamma,delta=entries
    aa,ab=alpha; ba,bb=beta; ca,cb=gamma; da,db=delta
    return [
        [aa,ba,-2*ab,-2*bb],
        [ca,da,-2*cb,-2*db],
        [ab,bb,aa,ba],
        [cb,db,ca,da],
    ]

def word_matrix(word,S,T):
    out=eye()
    for tok in word.split("*"):
        out=mm(out,S if tok=="S" else T)
    return out

def main():
    n=json.loads(N_PATH.read_text())
    o=json.loads(O_PATH.read_text())
    q=json.loads(Q_PATH.read_text())
    assert canonical(n)==EXPECTED_N_CANON==n["canonical_sha256_without_this_field"]
    assert blob(N_PATH)==EXPECTED_N_BLOB
    assert canonical(o)==EXPECTED_O_CANON==o["canonical_sha256_without_this_field"]
    assert blob(O_PATH)==EXPECTED_O_BLOB
    assert canonical(q)==EXPECTED_Q_CANON==q["canonical_sha256_without_this_field"]

    mu=q["source_B9_full_homology"]["mu1_coordinate_matrix"]
    cyc=n["source_marking"]["mu1_cycle_action_matrix"]
    assert mu==[list(row) for row in zip(*cyc)]
    I=eye()
    assert det4([[I[i][j]-mu[i][j] for j in range(4)] for i in range(4)])==2
    assert powm(mu,4)==neg(I)
    assert powm(mu,8)==I

    S=real_matrix(((1,0),(1,1),(0,0),(-1,0)))
    T=real_matrix(((1,0),(1,0),(-1,0),(0,0)))
    words={w for ws in n["exact_enumeration"]["short_target_words_by_fixed_line"].values() for w in ws}
    assert len(words)==6
    for w in words:
        A=word_matrix(w,S,T)
        assert det4([[I[i][j]-A[i][j] for j in range(4)] for i in range(4)])==2
        assert powm(A,4)==neg(I)
        assert powm(A,8)==I

    full=q["full_torus_argument"]
    assert full["all_six_retained_B9_linear_images_det_I_minus_A"]==2
    assert full["I_minus_A_surjective_for_all_six"] is True
    assert full["affine_translation_can_select_a_W_line"] is False
    assert o["finite_mod2_translation_audit"]["all_candidate_translations_in_image_I_minus_A"] is True
    assert o["finite_mod2_translation_audit"]["solutions_per_candidate"]==2

    dec=q["decision"]
    assert dec["full_lattice_affine_translation_breaks_ppav_torsor_ambiguity"] is False
    assert dec["absolute_delta0inf_retained_W_line_identified"] is False
    assert dec["survivors_current_credit"]==[73,97,235]
    assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
    assert q["firewalls"]["scratch_result_promoted_to_MAIN_authority"] is False

    print("POST1648Q_FULL_TORUS_TRANSLATION_CONJUGACY_NONPRUNING_COMPLETE")
    print("det_I_minus_mu1=2; I_minus_A_isogeny_surjective_for_all_six=true")
    print("affine_translation_marking_selector=false")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")

if __name__=="__main__":
    main()
