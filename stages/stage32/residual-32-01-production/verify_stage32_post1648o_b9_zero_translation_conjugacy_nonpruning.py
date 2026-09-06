#!/usr/bin/env python3
from __future__ import annotations

import hashlib, itertools, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648o-b9-zero-translation-conjugacy-nonpruning.json"
N_PATH = HERE / "post1648n-canonical-period-marked-ppav-torsor-obstruction.json"
D_PATH = HERE / "post1648d-deraux-affine-sixpoint-orbit-absolute-line-obstruction.json"

EXPECTED_CERT = "6ad188aaf14aa9998ac27efc5737e79666b300cdccf2312d9c2b250f8e8a02ef"
EXPECTED_N = "060d940626cd59b00efb67db7f27914e6a440c92968600a3d82a208d5a5d76ba"
EXPECTED_D = "598f3557d84423702be97a6fc942cf3254e68c57b3ccb1950f4d29c3fb3a69f0"
EXPECTED_N_BLOB = "0ee05f679c7706113feed2c217e08a95b3bd6f06"
EXPECTED_D_BLOB = "1ab58cba29ed94e0eaf7e646a8e6ed6a536dde41"


def canonical(obj):
    body = dict(obj); body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()).hexdigest()


def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) % 2 for j in range(4)] for i in range(4)]


def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(4)) % 2 for i in range(4)]


def ident():
    return [[1 if i==j else 0 for j in range(4)] for i in range(4)]


def key(A,t=None):
    q = tuple(x for row in A for x in row)
    return q if t is None else q + tuple(t)


def real_matrix(entries):
    alpha,beta,gamma,delta=entries
    aa,ab=alpha; ba,bb=beta; ca,cb=gamma; da,db=delta
    return [[aa,ba,-2*ab,-2*bb],[ca,da,-2*cb,-2*db],[ab,bb,aa,ba],[cb,db,ca,da]]


def mod2(A): return [[x%2 for x in row] for row in A]


def word_matrix(word,S,T):
    out=ident()
    for tok in word.split("*"):
        out=mm(out, S if tok=="S" else T)
    return out


def acomp(g,h):
    # h o g: x -> B(Ax+t)+u
    A,t=g; B,u=h
    return mm(B,A), [(x+y)%2 for x,y in zip(mv(B,t),u)]


def close_affine(gens):
    z=(ident(),[0,0,0,0]); seen={key(*z):z}; words={key(*z):"id"}; q=[z]
    while q:
        g=q.pop(0); w=words[key(*g)]
        for name,h in gens:
            y=acomp(g,h); k=key(*y)
            if k not in seen:
                seen[k]=y; words[k]=name if w=="id" else w+"*"+name; q.append(y)
    return seen,words


def translation_solutions(A,t):
    sols=[]
    for s in itertools.product((0,1), repeat=4):
        lhs=[(s[i]-mv(A,s)[i])%2 for i in range(4)]
        if lhs==t: sols.append(list(s))
    return sols


def main():
    cert=json.loads(CERT.read_text()); n=json.loads(N_PATH.read_text()); d=json.loads(D_PATH.read_text())
    assert canonical(cert)==EXPECTED_CERT==cert["canonical_sha256_without_this_field"]
    assert canonical(n)==EXPECTED_N==n["canonical_sha256_without_this_field"] and blob(N_PATH)==EXPECTED_N_BLOB
    assert canonical(d)==EXPECTED_D==d["canonical_sha256_without_this_field"] and blob(D_PATH)==EXPECTED_D_BLOB

    S=mod2(real_matrix(((1,0),(1,1),(0,0),(-1,0))))
    T=mod2(real_matrix(((1,0),(1,0),(-1,0),(0,0))))
    dg=d["target_deraux_affine_J2_model"]["deraux_generators_mod2"]
    gens=[]
    for name in ("R1","R2","R3"):
        gens.append((name,(dg[name]["linear"],dg[name]["translation"])))
    G,words=close_affine(gens)
    assert len(G)==24==d["target_deraux_affine_J2_model"]["generated_affine_group_order_mod2"]

    n_words=n["exact_enumeration"]["short_target_words_by_fixed_line"]
    expected_words={w for ws in n_words.values() for w in ws}
    assert len(expected_words)==6
    recs=cert["finite_mod2_translation_audit"]["candidates"]
    assert {r["retained_linear_word"] for r in recs}==expected_words

    lines={"L1":[0,0,1,0],"L2":[0,0,0,1],"L3":[0,0,1,1]}
    counts={k:0 for k in lines}
    for rec in recs:
        A=word_matrix(rec["retained_linear_word"],S,T)
        matches=[(g,words[k]) for k,g in G.items() if g[0]==A]
        assert len(matches)==1
        (A2,t),aword=matches[0]
        assert aword==rec["deraux_affine_word"]
        assert t==rec["translation_f2"]
        sols=translation_solutions(A,t)
        assert sols==rec["translation_conjugator_solutions_f2"] and len(sols)==2
        fixed=[name for name,v in lines.items() if mv(A,v)==v]
        assert fixed==[rec["fixed_W_line"]]
        counts[fixed[0]]+=1

    audit=cert["finite_mod2_translation_audit"]
    assert counts==audit["fixed_line_counts"]=={"L1":2,"L2":2,"L3":2}
    assert audit["all_candidate_translations_in_image_I_minus_A"] is True
    assert audit["possible_delta0inf_residues_decimal"]==[73,97,235]
    dec=cert["decision"]
    assert dec["B9_zero_translation_breaks_period_torsor_ambiguity"] is False
    assert dec["absolute_delta0inf_retained_W_line_identified"] is False
    assert dec["survivors_current_credit"]==[73,97,235]
    assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_MAIN_authority"] is False

    print("POST1648O_B9_ZERO_TRANSLATION_CONJUGACY_NONPRUNING_COMPLETE")
    print("six_linear_candidates_all_translation_conjugate_from_zero=true")
    print("translation_conjugator_solutions_per_candidate=2")
    print("fixed_line_counts=L1:2,L2:2,L3:2")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")

if __name__ == "__main__": main()
