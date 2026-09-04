#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXPECTED_CANONICAL = "7ad84e3c0a567119933ee0941b3b125ebcdb80651973033e13dbf12b553bfc92"
EXPECTED_3 = [73,97,235]
EXPECTED_LINES = [(0,0,1,0),(0,0,0,1),(0,0,1,1)]


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body=dict(doc); body.pop("canonical_sha256_without_this_field",None)
    raw=json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json(lock: dict) -> dict:
    p=ROOT/lock["path"]
    assert p.is_file() and blob_sha1(p)==lock["blob_sha1"], p
    d=json.loads(p.read_text())
    if "canonical_sha256" in lock:
        assert canonical_sha256(d)==lock["canonical_sha256"], p
    return d

# Z[r], r^2=-2, represented as (a,b)=a+b*r.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def mm(A,B):
    return [[sum_pair(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sum_pair(xs):
    z=(0,0)
    for x in xs: z=add(z,x)
    return z
def ct(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]

def mod2_4(A):
    out=[[0]*4 for _ in range(4)]
    for j in range(4):
        c=[0,0]; d=[0,0]
        (c if j<2 else d)[j%2]=1
        oc=[0,0]; od=[0,0]
        for i in range(2):
            for k in range(2):
                a,b=A[i][k][0]&1,A[i][k][1]&1
                oc[i]^=a&c[k]
                od[i]^=(a&d[k])^(b&c[k])
        col=oc+od
        for i in range(4): out[i][j]=col[i]
    return out

def t4(bits: int):
    x=[(bits>>i)&1 for i in range(8)]
    A=[[(x[0],x[1]),(x[2],x[3])],[(x[4],x[5]),(x[6],x[7])]]
    return mod2_4(A)

def m4(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4))&1 for j in range(4)] for i in range(4)]
def inv4(A):
    X=[row[:] + [1 if i==j else 0 for j in range(4)] for i,row in enumerate(A)]
    r=0
    for c in range(4):
        p=next(i for i in range(r,4) if X[i][c]); X[r],X[p]=X[p],X[r]
        for i in range(4):
            if i!=r and X[i][c]: X[i]=[a^b for a,b in zip(X[i],X[r])]
        r+=1
    return [row[4:] for row in X]
def key(A): return tuple(tuple(r) for r in A)

def conj_residue(bits,g,decode): return decode[key(m4(m4(g,t4(bits)),inv4(g)))]
def mv(A,v): return tuple(sum(A[i][j]*v[j] for j in range(4))&1 for i in range(4))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",required=True); args=ap.parse_args()
    cert=json.loads((ROOT/args.check).read_text())
    assert cert["schema"]=="STAGE32_POST1505_O210_Q602_MARKED_W_LINE_GAUGE_ORBIT_V1"
    assert canonical_sha256(cert)==cert["canonical_sha256_without_this_field"]==EXPECTED_CANONICAL

    locks=cert["source_locks"]
    prev=load_json(locks["audited_weierstrass_transvection"])
    principal=load_json(locks["principal_rosati"])
    note=ROOT/locks["source_note"]["path"]
    assert note.is_file() and blob_sha1(note)==locks["source_note"]["blob_sha1"]
    assert locks["audited_weierstrass_transvection"]["hostile_reaudit_review"]==5102652713
    filt=prev["retained_residue_filter"]
    assert filt["surviving_residues_decimal"]==EXPECTED_3
    assert [tuple(x) for x in filt["image_lines_in_W"]]==EXPECTED_LINES
    assert cert["audited_input"]["residues_decimal"]==EXPECTED_3

    # Exact principal-unitary check for Cecotti B.1 generators b3,b4.
    H=[[(2,0),(1,1)],[(1,-1),(2,0)]]
    b3=[[(-1,0),(-1,0)],[(1,0),(0,0)]]
    b4=[[(1,0),(1,1)],[(0,0),(-1,0)]]
    assert principal["principal_polarization"]["hermitian_matrix"]==[["2","1+r"],["1-r","2"]]
    assert mm(mm(ct(b3),H),b3)==H
    assert mm(mm(ct(b4),H),b4)==H

    g3,g4=mod2_4(b3),mod2_4(b4)
    L1,L2,L3=EXPECTED_LINES
    assert [mv(g3,L1),mv(g3,L3),mv(g3,L2)]==[L3,L2,L1]
    assert [mv(g4,L1),mv(g4,L2),mv(g4,L3)]==[L1,L3,L2]

    decode={key(t4(bits)):bits for bits in range(256)}
    assert len(decode)==256
    c3={x:conj_residue(x,g3,decode) for x in EXPECTED_3}
    c4={x:conj_residue(x,g4,decode) for x in EXPECTED_3}
    assert c3=={73:235,97:73,235:97}
    assert c4=={73:73,97:235,235:97}
    assert cert["residue_conjugation"]["b3"]=={"73":235,"235":97,"97":73}
    assert cert["residue_conjugation"]["b4"]=={"73":73,"97":235,"235":97}

    # Generate the exact mod-2 group; it must act transitively on the three residues.
    I=[[1 if i==j else 0 for j in range(4)] for i in range(4)]
    seen={key(I)}; q=[I]
    while q:
        a=q.pop()
        for g in (g3,g4):
            z=m4(a,g); k=key(z)
            if k not in seen: seen.add(k); q.append(z)
    assert len(seen)==24
    orbit={conj_residue(73,[list(r) for r in g],decode) for g in seen}
    assert orbit==set(EXPECTED_3)

    # Canonical gauge L1 gives one representative, residue 73.
    g3sq=m4(g3,g3)
    assert conj_residue(97,g3,decode)==73 and mv(g3,L2)==L1
    assert conj_residue(235,g3sq,decode)==73 and mv(g3sq,L3)==L1
    norm=cert["marked_gauge_normalization"]
    assert norm["canonical_residue"]==73 and tuple(norm["canonical_line"])==L1
    assert norm["representative_count"]==1

    d=cert["decision"]; fw=cert["firewalls"]
    assert d["Q602_excluded"] is False and d["O210_excluded"] is False and d["O212_plus_authorized"] is False
    assert d["arithmetic_exclusion"] is False
    assert fw["absolute_delta0inf_retained_line_identified"] is False
    assert fw["two_residues_arithmetically_excluded"] is False
    assert fw["gauge_orbit_compression_only"] is True
    assert fw["heavy_compute_authorized"] is False and fw["receiver_credit"] is False and fw["theorem_credit"] is False
    print("PASS: Stage32 Q602 residues 73/97/235 are one exact principal-Bolza marked-gauge orbit; canonical representative 73; no arithmetic exclusion.")

if __name__=="__main__": main()
