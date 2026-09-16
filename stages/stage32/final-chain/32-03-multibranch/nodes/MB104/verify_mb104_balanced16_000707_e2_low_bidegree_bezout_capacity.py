#!/usr/bin/env python3
import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-LOW-BIDEGREE-BEZOUT-CAPACITY-CERTIFICATE.json"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-LOW-BIDEGREE-BEZOUT-CAPACITY.md",
        "60cd43c94b7d1ab2992f3cd502d1e49ac2c972e6",
    ),
    "JOINT_PAIR": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY.md",
        "53608cb51aa49ccde1603b1cb1d136ea497b2324",
    ),
    "RESIDUAL_NODE_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE-CERTIFICATE.json",
        "02c5c5b52ed18cc2850a01bab05c6dfac85a59f9",
    ),
    "PICARD_PARITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-DESCENT-PARITY-CERTIFICATE.json",
        "7621932b87a7558d473bc99a09b46bcb04a433a0",
    ),
    "ZERO_QUARTIC_TORSION": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ZERO-QUARTIC-TORSION-CONGRUENCES.md",
        "544ded0d132dcf4dca0a5a3d52925a88c8c461e2",
    ),
    "A1_ENERGY": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-A1-LIFT-ENERGY-IDENTITY.md",
        "3fb4152c35b88160f36730fac941f542566664a8",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def preflight(cert):
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "certificate/source-lock table mismatch")
    rr = root()
    for key, (rel, sha) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL: missing {key}: {rel}")
        got = blob_sha1(p)
        if got != sha:
            raise SystemExit(f"SOURCE_LOCK_FAIL: {key}: expected {sha}, got {got}")
    return rr


# Z[s,i], s^2=2, i^2=-1.  Every coefficient used below is an algebraic integer,
# so determinant/minor computations need no division.
Z0 = (0, 0, 0, 0)
Z1 = (1, 0, 0, 0)
S = (0, 1, 0, 0)
I = (0, 0, 1, 0)


def zadd(x, y):
    return (x[0]+y[0], x[1]+y[1], x[2]+y[2], x[3]+y[3])


def zneg(x):
    return (-x[0], -x[1], -x[2], -x[3])


def zsub(x, y):
    return zadd(x, zneg(y))


def zmul(x, y):
    a,b,c,d = x
    A,B,C,D = y
    return (
        a*A + 2*b*B - c*C - 2*d*D,
        a*B + b*A - c*D - d*C,
        a*C + 2*b*D + c*A + 2*d*B,
        a*D + b*C + c*B + d*A,
    )


def zscale(n, x):
    return (n*x[0], n*x[1], n*x[2], n*x[3])


def zdot(row, vec):
    out = Z0
    for a,b in zip(row, vec):
        out = zadd(out, zmul(a,b))
    return out


def det_dp(mat):
    n = len(mat)
    dp = {0: Z1}
    for r in range(n):
        nd = {}
        for mask, value in dp.items():
            for c in range(n):
                if mask & (1 << c):
                    continue
                inversions_added = sum(1 for j in range(c+1, n) if mask & (1 << j))
                term = zmul(value, mat[r][c])
                if inversions_added & 1:
                    term = zneg(term)
                nm = mask | (1 << c)
                nd[nm] = zadd(nd.get(nm, Z0), term)
        dp = nd
    return dp[(1 << n) - 1]


def minor(mat, rows, cols):
    return [[mat[r][c] for c in cols] for r in rows]


def null_basis_integral(mat, rank):
    m, n = len(mat), len(mat[0])
    chosen = None
    for rs in itertools.combinations(range(m), rank):
        for cs in itertools.combinations(range(n), rank):
            A = minor(mat, rs, cs)
            delta = det_dp(A)
            if delta != Z0:
                chosen = (rs, cs, A, delta)
                break
        if chosen:
            break
    req(chosen is not None, f"no nonzero rank-{rank} minor")
    rs, piv, A, delta = chosen
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        vec = [Z0] * n
        vec[f] = delta
        af = [mat[r][f] for r in rs]
        for jj, pc in enumerate(piv):
            repl = [row[:] for row in A]
            for rr in range(rank):
                repl[rr][jj] = af[rr]
            vec[pc] = zneg(det_dp(repl))
        for row in mat:
            req(zdot(row, vec) == Z0, "integral null basis does not annihilate full matrix")
        basis.append(vec)
    return basis


def resultant_quad(co):
    a,b,c,d,e,f = co
    return det_dp([
        [a,b,c,Z0],
        [Z0,a,b,c],
        [d,e,f,Z0],
        [Z0,d,e,f],
    ])


def irreducible_11(co):
    a,b,c,d = co
    return zsub(zmul(a,d), zmul(b,c)) != Z0


U = zadd(Z1, I)
V = zsub(Z1, I)
IS = zmul(I, S)
POINTS = [
    (S,S), (zneg(S),zneg(S)), (S,zneg(S)), (zneg(S),S),
    (IS,zneg(S)), (zneg(IS),S), (IS,S), (zneg(IS),zneg(S)),
    (U,V), (zneg(U),zneg(V)), (U,zneg(V)), (zneg(U),V),
    (U,zneg(U)), (zneg(U),U), (U,U), (zneg(U),zneg(U)),
]
LABELS = ["A+","A-","B+","B-","C+","C-","D+","D-","E+","E-","F+","F-","G+","G-","H+","H-"]
INDEX = {x:i for i,x in enumerate(LABELS)}


def row11(p):
    x,y = p
    return [zmul(x,y), x, y, Z1]


def row12(p):
    x,y = p
    y2 = zmul(y,y)
    return [zmul(x,y2), zmul(x,y), x, y2, y, Z1]


def row21(p):
    x,y = p
    x2 = zmul(x,x)
    return [zmul(x2,y), zmul(x,y), y, x2, x, Z1]


# Safe modular prefilter.  Full rank modulo p proves full rank in characteristic zero.
P = 41
SM = 17   # 17^2 = 2 mod 41
IM = 9    # 9^2 = -1 mod 41


def emb(z):
    a,b,c,d = z
    return (a + b*SM + c*IM + d*SM*IM) % P


POINTS_MOD = [(emb(x), emb(y)) for x,y in POINTS]


def row11m(p):
    x,y = p
    return [(x*y)%P, x, y, 1]


def row12m(p):
    x,y = p
    return [(x*y*y)%P, (x*y)%P, x, (y*y)%P, y, 1]


def row21m(p):
    x,y = p
    return [(x*x*y)%P, (x*y)%P, y, (x*x)%P, x, 1]


def rank_mod(mat):
    a = [row[:] for row in mat]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pr = next((rr for rr in range(r,m) if a[rr][c] % P), None)
        if pr is None:
            continue
        a[r], a[pr] = a[pr], a[r]
        inv = pow(a[r][c] % P, P-2, P)
        for rr in range(r+1,m):
            if not a[rr][c] % P:
                continue
            f = a[rr][c] * inv % P
            for j in range(c,n):
                a[rr][j] = (a[rr][j] - f*a[r][j]) % P
        r += 1
        if r == m:
            break
    return r


def support_of(rowfun, co):
    return tuple(i for i,p in enumerate(POINTS) if zdot(rowfun(p), co) == Z0)


def labels_of(support):
    return tuple(LABELS[i] for i in support)


def cert_supports(block):
    return {tuple(x) for x in block["supports"]}


def classify_11(cert):
    census = {4:0,3:0,2:0}
    irreducible = set()
    rank2_pencils = 0
    for ss in itertools.combinations(range(16), 4):
        mat = [row11(POINTS[i]) for i in ss]
        rk = rank_mod([row11m(POINTS_MOD[i]) for i in ss])
        census[rk] = census.get(rk,0) + 1
        if rk == 4:
            continue
        req(det_dp(mat) == Z0, "(1,1) modular rank drop but exact determinant nonzero")
        if rk == 3:
            co = null_basis_integral(mat, 3)[0]
            if irreducible_11(co):
                sup = support_of(row11, co)
                req(len(sup) == 4, "irreducible (1,1) support larger than four")
                irreducible.add(labels_of(sup))
        elif rk == 2:
            # Confirm exact rank is two, not a bad-prime rank-three drop.
            for rs in itertools.combinations(range(4),3):
                for cs in itertools.combinations(range(4),3):
                    req(det_dp(minor(mat,rs,cs)) == Z0, "(1,1) rank-two modular pencil has exact rank three")
            basis = null_basis_integral(mat, 2)
            req(len(basis) == 2, "(1,1) rank-two kernel dimension")
            # determinant is quadratic in a pencil parameter; three zeros make it identically zero.
            for t in (0,1,2):
                co = [zadd(basis[0][j], zscale(t,basis[1][j])) for j in range(4)]
                req(not irreducible_11(co), "rank-two (1,1) pencil contains irreducible member")
            rank2_pencils += 1
        else:
            raise SystemExit(f"FAIL: unexpected (1,1) rank {rk}")
    want = {int(k):v for k,v in cert["bidegree_11"]["rank_census"].items()}
    req(census == want, f"(1,1) rank census {census} != {want}")
    req(irreducible == cert_supports(cert["bidegree_11"]), "(1,1) irreducible support list mismatch")
    req(len(irreducible) == cert["bidegree_11"]["unique_irreducible_count"] == 32, "(1,1) irreducible count")
    req(rank2_pencils == 4 and cert["bidegree_11"]["rank2_pencils_with_irreducible_member"] == 0, "(1,1) rank-two pencil census")


def classify_12_like(cert, key, rowfun, rowfun_mod):
    census = {6:0,5:0,4:0}
    irreducible = set()
    rank4_pencils = 0
    for ss in itertools.combinations(range(16), 6):
        mat = [rowfun(POINTS[i]) for i in ss]
        rk = rank_mod([rowfun_mod(POINTS_MOD[i]) for i in ss])
        census[rk] = census.get(rk,0) + 1
        if rk == 6:
            continue
        req(det_dp(mat) == Z0, f"{key} modular rank drop but exact determinant nonzero")
        if rk == 5:
            co = null_basis_integral(mat, 5)[0]
            if resultant_quad(co) != Z0:
                sup = support_of(rowfun, co)
                req(len(sup) == 6, f"irreducible {key} support larger than six")
                irreducible.add(labels_of(sup))
        elif rk == 4:
            # Rule out exact rank five hidden by the chosen finite-field embedding.
            for rs in itertools.combinations(range(6),5):
                for cs in itertools.combinations(range(6),5):
                    req(det_dp(minor(mat,rs,cs)) == Z0, f"{key} rank-four modular pencil has exact rank five")
            basis = null_basis_integral(mat, 4)
            req(len(basis) == 2, f"{key} rank-four kernel dimension")
            # Resultant has degree <=4 on the pencil. Five exact zeros make it identically zero.
            for t in (0,1,2,3,4):
                co = [zadd(basis[0][j], zscale(t,basis[1][j])) for j in range(6)]
                req(resultant_quad(co) == Z0, f"{key} rank-four pencil contains irreducible member")
            rank4_pencils += 1
        else:
            raise SystemExit(f"FAIL: unexpected {key} rank {rk}")
    want = {int(k):v for k,v in cert[key]["rank_census"].items()}
    req(census == want, f"{key} rank census {census} != {want}")
    req(irreducible == cert_supports(cert[key]), f"{key} irreducible support list mismatch")
    req(len(irreducible) == cert[key]["rank5_unique_irreducible_count"] == 16, f"{key} irreducible count")
    req(rank4_pencils == 236, f"{key} rank-four pencil count")
    req(cert[key]["rank4_pencils_with_irreducible_member"] == 0, f"{key} certificate rank-four firewall")
    req(cert[key]["rank4_pencil_resultant_identically_zero"] is True, f"{key} resultant firewall")


def derive_fibres():
    vertical = {}
    horizontal = {}
    for idx,(x,y) in enumerate(POINTS):
        vertical.setdefault(x, []).append(LABELS[idx])
        horizontal.setdefault(y, []).append(LABELS[idx])
    groups = [tuple(v) for v in vertical.values()] + [tuple(v) for v in horizontal.values()]
    return {tuple(g) for g in groups}


def check_source_semantics(rr):
    residual = json.loads((rr / LOCKS["RESIDUAL_NODE_CERT"][0]).read_text())
    ex = residual["exact_residual_orbits"]
    req(ex["support_nodes"] == [0,1,2,3,8,9,10,11,24,25,26,32,33,34], "residual support nodes")
    req(ex["simultaneous_deck_action"] == "(r_z,r_w)->(-r_z,-r_w)", "residual simultaneous deck action")
    sat = residual["saturation_constraints"]
    req(sat["branches_per_supported_node"] == "8*l", "branch count semantics")
    req(sat["q0"] == "x0-x1+x2-x3-x24+x25-x26=-4*l", "Q0 saturation source")
    req(sat["q1"] == "x8+x9+x10+x11+x32+x33+x34=28*l", "Q1 saturation source")

    pic = json.loads((rr / LOCKS["PICARD_PARITY_CERT"][0]).read_text())
    req(pic["exact_result"]["membership_equation_rank"] == 14, "Picard parity rank")
    rows = pic["exact_result"]["equation_rows_l_then_support"]
    req(len(rows) == 14 and all(sum(r[1:]) == 1 and r[0] == 0 for r in rows), "Picard parity forces every x_j even")


def check_formal_survivor(cert):
    fw = cert["formal_survivor"]
    m, l = fw["m"], fw["l"]
    req(l == 2*m and (m,l) == (5,10), "formal survivor scale")
    nodes = fw["node_order"]
    x = dict(zip(nodes, fw["x"]))
    req(nodes == [0,1,2,3,8,9,10,11,24,25,26,32,33,34], "formal survivor node order")
    req(all(0 <= x[j] <= 8*l for j in nodes), "formal survivor branch bounds")
    req(all(x[j] % 2 == 0 for j in nodes), "formal survivor all-even Picard condition")
    req(x[0]-x[1]+x[2]-x[3]-x[24]+x[25]-x[26] == -4*l, "formal survivor Q0 saturation")
    req(x[8]+x[9]+x[10]+x[11]+x[32]+x[33]+x[34] == 28*l, "formal survivor Q1 saturation")
    req((x[24]+x[25]+x[26]) % 4 == 0, "formal survivor Q0 mod4")
    req((x[32]+x[33]+x[34]) % 4 == 0, "formal survivor Q1 mod4")
    b = [x[j]//2 - 4*m for j in nodes]
    req(b == fw["b"], "formal survivor centered vector")
    Q = sum(t*t for t in b)
    delta_same = 336*m*m + 112*m - 2*Q
    req(Q == fw["Q"] == 4480, "formal survivor energy")
    req(delta_same == fw["delta_same"] == 0, "formal survivor delta_same endpoint")

    w = {
        "A+":x[0]+x[2], "A-":16*l-x[0]-x[2],
        "B+":x[1]+x[3], "B-":16*l-x[1]-x[3],
        "C+":x[24]+x[26], "C-":16*l-x[24]-x[26],
        "D+":x[25], "D-":8*l-x[25],
        "E+":x[8]+x[10], "E-":16*l-x[8]-x[10],
        "F+":x[9]+x[11], "F-":16*l-x[9]-x[11],
        "G+":x[32]+x[34], "G-":16*l-x[32]-x[34],
        "H+":x[33], "H-":8*l-x[33],
    }
    req(sum(w.values()) == 112*l, "formal survivor total special mass")
    def mass(s): return sum(w[t] for t in s)
    fibres = cert["fibres"]["supports"]
    max_f = max(mass(s) for s in fibres)
    max11 = max(mass(s) for s in cert["bidegree_11"]["supports"])
    max12 = max(mass(s) for s in cert["bidegree_12"]["supports"])
    max21 = max(mass(s) for s in cert["bidegree_21"]["supports"])
    req(max_f == fw["max_fibre_mass"] == 28*l, "formal survivor fibre capacity")
    req(max11 == fw["max_11_mass"] == 546 and max11 <= 56*l, "formal survivor (1,1) capacity")
    req(max12 == fw["max_12_mass"] == 624 and max12 <= 84*l, "formal survivor (1,2) capacity")
    req(max21 == fw["max_21_mass"] == 632 and max21 <= 84*l, "formal survivor (2,1) capacity")
    req(fw["geometrically_realized"] is False, "formal survivor geometry firewall")


def main():
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_LOW_BIDEGREE_BEZOUT_CAPACITY_V1", "schema")
    rr = preflight(cert)
    check_source_semantics(rr)
    req(len(POINTS) == 16 and len(set(POINTS)) == 16, "sixteen distinct exact residual special points")
    req(derive_fibres() == cert_supports(cert["fibres"]), "special vertical/horizontal fibre list")
    classify_11(cert)
    classify_12_like(cert, "bidegree_12", row12, row12m)
    classify_12_like(cert, "bidegree_21", row21, row21m)
    check_formal_survivor(cert)
    req(cert["bezout"]["total_bidegree_ge_4_automatic"] is True, "high-bidegree exhaustion flag")
    req(cert["routing_consequence"]["raw_special_grid_bezout_exhausted"] is True, "route exhaustion flag")
    req(cert["routing_consequence"]["raw_special_grid_bezout_closes_e2"] is False, "e2 remains open")
    req(cert["credit_firewall"]["e2_closed"] is False, "e2 firewall")
    req(cert["credit_firewall"]["mb104_complete"] is False, "MB104 firewall")
    req(cert["credit_firewall"]["merge_authorized"] is False, "merge firewall")

    print("PASS STAGE32_MB104_000707_E2_LOW_BIDEGREE_BEZOUT_CAPACITY_V1")
    print("special_points=16; fibres=12")
    print("(1,1): rank 4/3/2 = 1432/384/4; irreducible four-point supports=32; rank2 pencils all reducible")
    print("(1,2): rank 6/5/4 = 4696/3076/236; irreducible six-point supports=16; rank4 pencils all reducible")
    print("(2,1): rank 6/5/4 = 4696/3076/236; irreducible six-point supports=16; rank4 pencils all reducible")
    print("formal endpoint survivor: m=5,l=10,delta_same=0 passes every raw low-bidegree capacity")
    print("e2 remains open; no credit; no merge")


if __name__ == "__main__":
    main()
