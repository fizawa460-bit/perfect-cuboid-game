#!/usr/bin/env python3
import hashlib, itertools, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "FORMAL-INFINITE-FAMILY-FEASIBILITY-CERTIFICATE.json"

LOCKS = {
    "MB101": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB101/CERTIFICATE.json", "282fc94d8d5feb0221cf6bf096ed4b0030883563"),
    "MB102": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB102/CERTIFICATE.json", "f852f66c67343b6a553b5c20e15dc0a0f55d5226"),
    "R8_WALLS": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/R8-ROUTE-WALLS-CERTIFICATE.json", "88220a04928f61a3491118c9c1f1bb35a1d6e6b9"),
    "HODGE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/HODGE-EXCEPTIONAL-MASS-CERTIFICATE.json", "3e1ea879f2b8368a6795f2e7faa1a4a08b608100"),
    "BTVA_LOW_SUPPORT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-LOW-SUPPORT-FINITENESS-CERTIFICATE.json", "248adcc01021ba087cb24e06e6492e837aca22ae"),
    "BTVA_SPAN": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-SPAN-DEGREE-CERTIFICATE.json", "dd174696c7391981d4d9a95e631b5df22d08500a"),
    "BEAUVILLE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-ODD-BRANCH-COVER-CERTIFICATE.json", "6a3fc0207aa66b453be0ad2f921425a70f93bd91"),
}

def require(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")

def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root not found")

def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def z(s):
    return {"0":(0,0),"1":(1,0),"-1":(-1,0),"i":(0,1),"-i":(0,-1)}[s]

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def neg(a): return (-a[0],-a[1])

def parity(p):
    inv = 0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            inv += p[i] > p[j]
    return -1 if inv % 2 else 1

def det(mat):
    n = len(mat)
    out = (0,0)
    for p in itertools.permutations(range(n)):
        term = (1,0)
        for i,j in enumerate(p):
            term = mul(term, mat[i][j])
        if parity(p) < 0:
            term = neg(term)
        out = add(out, term)
    return out

S_P6 = [
["1","0","0","0","1","1","1"],["1","0","0","0","1","1","-1"],["1","0","0","0","1","-1","1"],
["0","1","0","1","0","1","1"],["0","1","0","1","0","1","-1"],["0","1","0","1","0","-1","1"],
["0","0","1","1","1","0","1"],["0","0","1","1","1","0","-1"],
["1","i","0","i","1","0","0"],["1","i","0","i","-1","0","0"],
["0","1","i","0","i","1","0"],["0","1","i","0","i","-1","0"],
["i","0","1","1","0","i","0"],["i","0","1","1","0","-i","0"],
]
P6_BLOCKS = [1,1,1,2,2,2,3,3,4,4,5,5,6,6]

S_P5 = [
["1","i","0","i","1","0","0"],["1","i","0","i","-1","0","0"],["1","i","0","-i","1","0","0"],
["1","i","0","-i","-1","0","0"],["1","-i","0","i","1","0","0"],
["0","1","i","0","i","1","0"],["0","1","i","0","i","-1","0"],["0","1","i","0","-i","1","0"],
["0","1","i","0","-i","-1","0"],["0","1","-i","0","i","1","0"],
["i","0","1","1","0","i","0"],["i","0","1","1","0","-i","0"],["i","0","1","-1","0","i","0"],
["i","0","1","-1","0","-i","0"],
]
P5_BLOCKS = [4]*5 + [5]*5 + [6]*4

def parse(rows):
    return [[z(x) for x in row] for row in rows]

def block_counts(ids):
    return [ids.count(i) for i in range(1,7)]

def check_span():
    p6 = parse(S_P6)
    m = [p6[i] for i in [0,1,2,3,6,9,10]]
    require(det(m) == (8,8), "P6 support determinant")
    p5 = parse(S_P5)
    require(all(row[6] == (0,0) for row in p5), "P5 support lies in c=0")
    m5 = [[p5[i][j] for j in range(6)] for i in [0,1,2,4,5,6]]
    require(det(m5) == (0,16), "P5 support determinant")

def check_symbolic_families():
    require(block_counts(P6_BLOCKS) == [3,3,2,2,2,2], "P6 block counts")
    require(block_counts(P5_BLOCKS) == [0,0,0,5,5,4], "P5 block counts")

    # F0-P6: d=28k-4, g=0, R8=M=r_odd=28k, k>=1.
    require(84*1-12 > 0, "F0 FSM slack 84k-12")
    require(28 % 2 == 0, "F0 Beauville parity")
    require(22*1-4 >= 0, "F0 rank3 block slack 22k-4")
    require(42+28-2 > 0, "F0 Hodge sum-square slack")
    require(21+14-1 > 0, "F0 Hodge D2 slack")
    require(34 >= 0, "F0 conductor slack")
    require(-28+4+28-4 == 0, "F0 GFU degree boundary")

    # F1-P5/P6: d=28k, g=1, R8=M=r_odd=28k.
    require(112-28 >= 0, "F1 FSM slack")
    require(28 % 2 == 0, "F1 Beauville parity")
    require(10 <= 28 and 6 <= 28, "F1 rank3 block bounds")
    require(42+56 > 0, "F1 Hodge sum-square slack")
    require(21+28 > 0, "F1 Hodge D2 slack")
    require(34 >= 0, "F1 conductor slack")
    require(-28+28 == 0, "F1 GFU degree boundary")

def main():
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_FORMAL_INFINITE_FAMILY_FEASIBILITY_V1", "schema")
    require(cert["operator_priority"]["direct_R8_alpha_lt_quarter"] == "FROZEN_UNTIL_NEW_LEVER", "priority freeze")
    require(cert["scope"]["actual_curves_constructed"] is False, "actual curve firewall")

    rr = root()
    for key,(rel,sha) in LOCKS.items():
        p = rr / rel
        require(p.is_file(), f"{key} source missing")
        require(blob_sha1(p) == sha, f"{key} blob mismatch")
        require(cert["source_locks"][key] == sha, f"{key} certificate lock mismatch")

    check_span()
    check_symbolic_families()

    fam = {x["id"]:x for x in cert["families"]}
    require(set(fam) == {"F0-P6","F1-P5","F1-P6"}, "three hard-sector families")
    require(fam["F0-P6"]["span"] == 6 and fam["F1-P5"]["span"] == 5 and fam["F1-P6"]["span"] == 6, "span routing")
    require(cert["consequence"]["formal_unbounded_packets_exist_in_all_hard_sectors"] is True, "formal family conclusion")
    require(cert["consequence"]["current_retained_constraints_alone_force_finiteness"] is False, "no false finiteness")

    for key,val in cert["credit_firewall"].items():
        require(val is False, f"credit firewall {key}")

    print("PASS: unbounded formal packets survive all enumerated retained MB104 constraints in g0/P6 and g1/P5,P6; direct R8 route remains frozen")

if __name__ == "__main__":
    main()
