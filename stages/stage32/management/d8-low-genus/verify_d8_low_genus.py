#!/usr/bin/env python3
"""Stage32 D8-LOW-GENUS (research cycles 32R-20..23): exact checks for CONTRACT.md.

What this script ACTUALLY checks (sympy / integer arithmetic; Singular is NOT run here, see singular/run_all.sh):
  A. singular/tangency_{swap,id}.sing are reproduced byte-for-byte by singular/make_tangency_ideals.py.
  B. Every prime listed in singular/primes_{swap,id}.txt contains the tangency ideal T. Its members are:
       - the square locus {G^2 : G a (2,2) form through the 6 points}: for a SYMBOLIC G = sum a_k G_k, G^2 lies in L
         and makes every generator vanish identically in a; the map a -> G^2 has Jacobian rank len(a) (3 for swap,
         4 for id) at a rational point. The prime's dimension (= len(a)) is taken from Singular (primes_*.txt).
       - swap: two points, F = (x-y)(x+y)(xy-1)(xy+1) (contains x - y) and F = F*;
       - id: 16 primes on which x - y divides F (F(t,t) reduces to 0 modulo the prime).
     (That these primes are ALL the minimal primes of T is Singular's minAssGTZ, logged in primes_*.log.)
  C. F* = (x-y)^4 + (x^4-1)(y^4-1) = (x^2y^2-1)^2 - 4xy(x-y)^2.
     Its singular points are exactly the 6 points (±1,±1), (±i,±i), (0,inf), (inf,0), all with nonzero Hessian
     (ordinary nodes). With absolute irreducibility (Singular absFactorize, fstar.log) this gives genus 9-6 = 3.
  D. xy, (x^2-1)(y^2-1) and (x^2+1)(y^2+1) are squares on F* = 0: F* divides B_j^2 - 4(x-y)^2 g_j, and F* does not
     divide x - y.
  E. The 24 octahedral Moebius maps mu: for each, the rank r of <h_j(t)h_j(mu t)> mod squares, the number B of branch
     points, and the genus g of each component (2g-2 = 2^(r-1)(B-4)). Expected: rank 0 <-> class-preserving (4
     maps, conics), rank 1 (12 maps, g = 1), rank 2 (8 maps, g = 3).
  F. enumeration/certified_results.jsonl: every class reported by a split job is distinct and satisfies, in exact
     integer arithmetic, K.C = 8, F1.C = n1, e and Gamma49.C = v of its job, C^2 >= c2min, C.Gamma >= 0 for the 140
     known curves; there are 1830 of them, all with n1 = 4, in the stated (e, C^2, node pattern) counts.
  G. The result records are EXACTLY the generated job inventory of enumeration/run_certified.py (no missing, extra or
     duplicate job), all carry the producer id of the current producer files, and their fields match their job key;
     enumeration/PROVENANCE.json names the same producer id and the current certified_enum.c hash (the binary hash
     itself is reproduced by enumeration/reproduce_binary.sh, not by this script).
     Independently of the driver (rational nullspace, x_p = A^T (A A^T)^-1 t, column-lattice HNF), G recomputes:
     every CONGRUENCE_EMPTY claim (no integer solution of the slice equations), every EMPTY claim (R < 0), and for
     every BOUND job the intrinsic exact values f0_49, R, S49, which must equal the recorded witness and satisfy
     R >= 0, S49 >= 0, f0_49 <= 10 and (10 - f0_49)^2 >= R S49 (so Gamma49.C <= 10 on the slice); in every
     recomputed slice the form M = -N^T G N is checked positive definite by exact LDL^T pivots. COMPLETE split jobs are taken from
     the enumerator; their classes are checked in F.
NOT checked here (re-run separately): the enumeration itself (enumeration/run_certified.py, about 3 hours on 11 cores;
its pruning is rigorous by construction, see certified_enum.c and CONTRACT §2), the Singular decompositions
(singular/run_all.sh), any geometric statement, or the Hecke facts imported from #1842/#1843.
usage: PYTHONUTF8=1 python verify_d8_low_genus.py [REPO_ROOT]
"""
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from itertools import permutations
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[3]
sys.path.insert(0, str(HERE / "singular"))
import make_tangency_ideals as mti  # noqa: E402

QI = sp.QQ.algebraic_field(sp.I)
X, Y, T = sp.symbols("x y t")
x0, x1, y0, y1 = mti.x0, mti.x1, mti.y0, mti.y1
ok = True


def check(cond, msg):
    global ok
    print(("PASS " if cond else "FAIL ") + msg)
    ok &= bool(cond)


def affine(F):
    return sp.expand(F.subs({x0: X, x1: 1, y0: Y, y1: 1}))


# ---- A + B ---------------------------------------------------------------------------------------------------------
data = {}
for name, sigma in mti.SIGMAS.items():
    u, ns, vec, FL, tang = mti.build(sigma)
    txt = mti.singular_text(u, vec, tang).encode()
    check(txt == (HERE / "singular" / f"tangency_{name}.sing").read_bytes(), f"A {name}: tangency ideal reproduced (dim L = {len(u)})")
    data[name] = (sigma, u, FL, tang)

FSTAR = X**4 * Y**4 - 4 * X**3 * Y + 6 * X**2 * Y**2 - 4 * X * Y**3 + 1


def parse_primes(name, u):
    loc = {str(w): w for w in u}
    loc["I"] = sp.I
    out = []
    blocks = (HERE / "singular" / f"primes_{name}.txt").read_text().split("PRIME ")[1:]
    for b in blocks:
        head, body = b.split("\n", 1)
        d, deg = map(int, head.split())
        gens = [sp.expand(sp.sympify(g.replace("^", "**"), locals=loc)) for g in body.replace("\n", "").split(",") if g.strip()]
        out.append((d, deg, gens))
    return out


def reduces_to_zero(f, GB, u):
    return sp.reduced(sp.expand(f), GB, *u, order="grevlex", domain=QI)[1] == 0


def square_locus_dim(sigma):
    m2 = [x0**i * x1**(2 - i) * y0**j * y1**(2 - j) for i in range(3) for j in range(3)]
    g = sp.symbols("g0:9")
    G = sum(a * b for a, b in zip(g, m2))
    conds = [G.subs({x0: mti.CUSP[c][0], x1: mti.CUSP[c][1], y0: mti.CUSP[sigma[c]][0], y1: mti.CUSP[sigma[c]][1]}) for c in mti.CUSP]
    ns = sp.Matrix([[sp.diff(e, a) for a in g] for e in conds]).nullspace()
    return m2, ns


def coords_of(Fh, u, FL):
    """coordinates of a (4,4) form Fh in L (solve FL(u) = Fh)."""
    eqs = sp.Poly(sp.expand(FL - Fh), x0, x1, y0, y1).coeffs()
    s = sp.solve(eqs, u, dict=True)
    return s[0] if s else None


for name, (sigma, u, FL, tang) in data.items():
    primes = parse_primes(name, u)
    m2, nsG = square_locus_dim(sigma)
    kinds = Counter()
    for (d, deg, gens) in primes:
        GB = sp.groebner(gens, *u, order="grevlex", domain=QI)
        if not all(reduces_to_zero(tg, GB, u) for tg in tang):
            check(False, f"B {name}: a prime does not contain T"); continue
        if d == len(nsG):                                   # candidate square locus: UNIVERSAL symbolic check
            a = sp.symbols(f"a0:{len(nsG)}")
            coef = sum((a[k] * nsG[k] for k in range(len(nsG))), sp.zeros(9, 1))
            Gs = sp.expand(sum(coef[k] * m2[k] for k in range(9)) ** 2)
            eqs = sp.Poly(sp.expand(FL - Gs), x0, x1, y0, y1).coeffs()
            sol = sp.solve(eqs, u, dict=True)                  # u(a): coordinates of G^2 in L (polynomial in a)
            good = len(sol) == 1 and all(sp.expand(gg.subs(sol[0])) == 0 for gg in gens)
            # the parametrisation a -> G^2 has Jacobian rank len(a) at a rational point, so the closure of the
            # square locus has affine dimension len(a) = d; with the prime irreducible of dimension d, they coincide
            J = sp.Matrix([[sp.diff(sol[0][w], ak) for ak in a] for w in u]).subs({ak: k + 2 for k, ak in enumerate(a)})
            good &= J.rank() == len(a)
            kinds["square locus" if good else "UNEXPLAINED"] += 1
            continue
        if d == 1:                                          # a single projective point
            s = sp.solve(gens + [sum(u) - 1], u, dict=True) or sp.solve(gens + [u[-1] - 1], u, dict=True) or \
                [next(s_ for k in range(len(u)) for s_ in sp.solve(gens + [u[k] - 1], u, dict=True))]
            Fa = affine(sp.expand(FL.subs(s[0])))
            if sp.expand(Fa * FSTAR.coeff(X, 4).coeff(Y, 4) - FSTAR * Fa.coeff(X, 4).coeff(Y, 4)) == 0 and Fa != 0:
                kinds["F*"] += 1; continue
            fl = sp.factor_list(Fa, extension=sp.I)[1]
            if sp.rem(sp.Poly(Fa, X), sp.Poly(X - Y, X)).is_zero:
                kinds["contains x-y"] += 1
            elif len(fl) >= 2:
                kinds["reducible"] += 1
            else:
                kinds["UNEXPLAINED"] += 1
            continue
        # positive-dimensional, not the square locus: x - y | F on the component
        Fd = sp.Poly(sp.expand(FL.subs({x0: T, x1: 1, y0: T, y1: 1})), T).coeffs()
        kinds["contains x-y" if all(reduces_to_zero(c, GB, u) for c in Fd) else "UNEXPLAINED"] += 1
    expect = {"swap": Counter({"square locus": 1, "contains x-y": 1, "F*": 1}),
              "id": Counter({"square locus": 1, "contains x-y": 16})}[name]
    check(kinds == expect, f"B {name}: {len(primes)} primes classified as {dict(kinds)}")

# ---- C + D ---------------------------------------------------------------------------------------------------------
check(sp.expand(FSTAR - ((X - Y)**4 + (X**4 - 1) * (Y**4 - 1))) == 0, "C F* = (x-y)^4 + (x^4-1)(y^4-1)")
check(sp.expand(FSTAR - ((X**2 * Y**2 - 1)**2 - 4 * X * Y * (X - Y)**2)) == 0, "C F* = (x^2y^2-1)^2 - 4xy(x-y)^2")
Fx, Fy = sp.diff(FSTAR, X), sp.diff(FSTAR, Y)
GBs = sp.groebner([FSTAR, Fx, Fy], X, Y, order="lex", domain=QI)
check(GBs == sp.groebner([X - Y, Y**4 - 1], X, Y, order="lex", domain=QI), "C affine singular scheme of F* = (x - y, y^4 - 1): 4 reduced points")
nodes_ok = True
for c in (1, -1, sp.I, -sp.I):
    H = sp.hessian(FSTAR, (X, Y)).subs({X: c, Y: c})
    nodes_ok &= sp.simplify(H.det()) != 0
# chart x = 1/X (X = 0 is x = inf); and y = 1/Y
U, V = sp.symbols("U V")
Fxinf = sp.expand(U**4 * FSTAR.subs(X, 1 / U))
Fyinf = sp.expand(V**4 * FSTAR.subs(Y, 1 / V))
Fboth = sp.expand(U**4 * V**4 * FSTAR.subs({X: 1 / U, Y: 1 / V}))
s1 = sp.groebner([Fxinf, sp.diff(Fxinf, U), sp.diff(Fxinf, Y), U], U, Y, order="lex", domain=QI)
s2 = sp.groebner([Fyinf, sp.diff(Fyinf, X), sp.diff(Fyinf, V), V], X, V, order="lex", domain=QI)
s3 = sp.groebner([Fboth, U * V], U, V, order="lex", domain=QI)
nodes_ok &= list(s1.exprs) == [U, Y] and list(s2.exprs) == [X, V] and list(s3.exprs) == [1]
nodes_ok &= sp.hessian(Fxinf, (U, Y)).subs({U: 0, Y: 0}).det() != 0 and sp.hessian(Fyinf, (X, V)).subs({X: 0, V: 0}).det() != 0
check(nodes_ok, "C singular points of F* in P1xP1: exactly (±1,±1),(±i,±i),(inf,0),(0,inf), all ordinary nodes")
check(len(sp.factor_list(FSTAR, extension=sp.I)[1]) == 1, "C F* irreducible over Q(i) (absolute irreducibility: Singular log)")

I = sp.I
SQ = [  # elements 2(x-y) w + B_j of the component ideals (singular/fstar.log): w = -B_j / (2(x-y)), w^2 = g_j on F* = 0
    (X * Y, X**2 * Y**2 - 1),
    ((X**2 - 1) * (Y**2 - 1), I * X**3 * Y**3 - I * X**2 * Y**2 - 2 * I * X**2 + 3 * I * X * Y - 2 * I * Y**2 + I),
    ((X**2 + 1) * (Y**2 + 1), X**3 * Y**3 + X**2 * Y**2 - 2 * X**2 + 3 * X * Y - 2 * Y**2 - 1),
]
for j, (g, B) in enumerate(SQ, 1):
    r = sp.rem(sp.Poly(sp.expand(B**2 - 4 * (X - Y)**2 * g), X, Y, domain=QI), sp.Poly(FSTAR, X, Y, domain=QI))
    check(r.is_zero, f"D g_{j} is a square on F* = 0 (F* | B^2 - 4(x-y)^2 g)")
check(not sp.rem(sp.Poly(X - Y, X, Y), sp.Poly(FSTAR, X, Y)).is_zero, "D F* does not divide x - y")

# ---- E: octahedral graphs ------------------------------------------------------------------------------------------
PTS = [sp.oo, 0, 1, -1, I, -I]
CLASS = {sp.oo: 0, 0: 0, 1: 1, -1: 1, I: 2, -I: 2}


def mob(M, z):
    a, b, c, d = M
    if z == sp.oo:
        return sp.oo if c == 0 else sp.nsimplify(a / c)
    den = c * z + d
    return sp.oo if den == 0 else sp.nsimplify(sp.simplify((a * z + b) / den))


def mobius_through(src, dst):
    a, b, c, d = sp.symbols("a b c d")
    eqs = []
    for z, w in zip(src, dst):
        if z == sp.oo and w == sp.oo:
            eqs.append(c)
        elif z == sp.oo:
            eqs.append(a - w * c)
        elif w == sp.oo:
            eqs.append(c * z + d)
        else:
            eqs.append(a * z + b - w * (c * z + d))
    sol = sp.linsolve(eqs, [a, b, c, d])
    for s in sol:
        free = [v for v in (a, b, c, d) if any(e.has(v) for e in s)]
        vals = [e.subs({f: 1 for f in free}) for e in s]
        if sp.simplify(vals[0] * vals[3] - vals[1] * vals[2]) != 0:
            return tuple(sp.simplify(v) for v in vals)
    return None


octa = []
for img in permutations(PTS, 3):
    M = mobius_through(PTS[:3], img)
    if M and all(mob(M, z) in PTS for z in PTS) and len({mob(M, z) for z in PTS}) == 6:
        if not any(all(sp.simplify(mob(M, z) - mob(N, z)) == 0 if mob(M, z) != sp.oo else mob(N, z) == sp.oo for z in PTS) for N in octa):
            octa.append(M)
table = Counter()
for M in octa:
    # parity vectors over points of P1 of div(h_j(t) h_j(mu t)): zeros of h_j at class-j cusps, and at mu^-1(class-j cusps)
    vecs = []
    for j in range(3):
        par = Counter()
        for z in PTS:
            if CLASS[z] == j:
                par[z] += 1
            if CLASS[mob(M, z)] == j:
                par[z] += 1
        vecs.append(frozenset(z for z in par if par[z] % 2))
    span = {frozenset()}
    for v in vecs:
        span |= {s ^ v for s in span}
    r = {1: 0, 2: 1, 4: 2, 8: 3}[len(span)]
    branch = set().union(*span)
    B = len(branch)
    g = (2 ** (r - 1) * (B - 4) + 2) // 2 if r else 0
    cp = all(CLASS[mob(M, z)] == CLASS[z] for z in PTS)
    table[(r, B, g, cp)] += 1
check(len(octa) == 24 and table == Counter({(0, 0, 0, True): 4, (1, 4, 1, False): 12, (2, 6, 3, False): 8}),
      f"E octahedral graphs (rank, B, genus, class-preserving): {dict(table)}")

# ---- F: classes ----------------------------------------------------------------------------------------------------
try:
    import numpy as np
    sys.path.insert(0, str(REPO / "stages/stage32/residual-32-01-production"))
    from hperp_integral_adapter import HperpIntegralPairingAdapter

    def load_retained(path, name):
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.load()
    bundle = load_retained(REPO / "stages/stage33/33-07/picard_base_rows_retained.py", "b")
    marking = load_retained(REPO / "stages/stage33/33-07/stage32_picard_marking_retained.py", "m")
    ad = HperpIntegralPairingAdapter.from_retained(marking, bundle)
except Exception as exc:  # pragma: no cover
    ad = None
    check(False, f"F could not load the repository Picard data: {exc}")
if ad is not None:
    G = np.array([[int(v) for v in r] for r in bundle["picard_gram_64x64"]], dtype=object)
    P = np.array([[int(v) for v in r] for r in ad.pairing_matrix.tolist()], dtype=object)
    coords = [np.array([int(v) for v in ad.class_coordinates_in_retained_basis[i, :]], dtype=object) for i in range(140)]
    exc = P[92:].sum(axis=0)
    deg = (P[:92].sum(axis=0) + 5 * exc) // 19
    Fcls = {}
    for lbl in range(33, 45):
        pe = P.dot(coords[lbl - 1])
        Fcls[lbl] = tuple(2 * coords[lbl - 1] + sum(coords[k] for k in range(92, 140) if pe[k] > 0))
    F1 = sorted(set(Fcls.values()))[0]
    side = {lbl: ("V" if Fcls[lbl] == F1 else "H") for lbl in Fcls}
    F1row = np.array(F1, dtype=object).dot(G)
    gram140 = [P.dot(coords[i]) for i in range(140)]
    pair = {}
    for k in range(93, 141):
        met = [lbl for lbl in range(33, 45) if gram140[lbl - 1][k - 1] > 0]
        pair[k] = (next(lbl for lbl in met if side[lbl] == "V"), next(lbl for lbl in met if side[lbl] == "H"))
    check(Counter(Counter(pair.values()).values()) == Counter({4: 12}), "F 48 nodes = 12 cusp pairs x 4")
    results = [json.loads(line) for line in (HERE / "enumeration/certified_results.jsonl").read_text().splitlines() if line.strip()]
    cls = [(r, c) for r in results if r.get("fix") for c in r.get("classes", [])]
    pat = Counter()
    good = True
    for r, c in cls:
        x = np.array(c["x"], dtype=object)
        pr = P.dot(x)
        c2 = int(x.dot(G).dot(x))
        good &= (int(deg.dot(x)) == 8 and c2 == c["C2"] and c2 >= r["c2min"] and (pr >= 0).all()
                 and int(F1row.dot(x)) == r["n1"] and int(sum(pr[92:])) == r["e"] and int(pr[48]) == int(r["fix"].split("=")[1]))
        bd = {lbl: int(pr[lbl - 1]) for lbl in range(33, 45)}
        nd = defaultdict(list)
        for k in range(93, 141):
            if pr[k - 1] > 0:
                nd[pair[k]].append(int(pr[k - 1]))
        sumE_V = sum(v for lbl, v in bd.items() if side[lbl] == "V")
        good &= 2 * sumE_V + r["e"] == 6 * r["n1"]
        pat[(r["n1"], r["e"], c2, tuple(sorted(Counter(bd.values()).items())),
             tuple(sorted(Counter(tuple(sorted(m)) for m in nd.values()).items())),
             len({p_[0] for p_ in nd}), len({p_[1] for p_ in nd}))] += 1
    xs = [tuple(c["x"]) for _, c in cls]
    check(good and len(xs) == len(set(xs)) == 1830,
          f"F all {len(xs)} certified classes: distinct; K.C = 8, F1.C = n1, e, Gamma49.C = v of their job, C^2 >= c2min, "
          "C.Gamma >= 0 (140 curves), 2 sum_V C.E + e = 6 n1")
    # key: (n1, e, C^2, {C.E_c value: #lines}, {sorted m-list per cusp pair: #pairs}, #vertical lines met, #horizontal lines met)
    expect = Counter({
        (4, 12, -8, ((1, 12),), (((1, 1), 6),), 6, 6): 64,
        (4, 12, -4, ((1, 12),), (((1, 1), 6),), 6, 6): 32,
        (4, 8, -8, ((0, 4), (2, 8)), (((2, 2), 2),), 2, 2): 192,
        (4, 8, -8, ((0, 2), (1, 4), (2, 6)), (((2,), 2), ((2, 2), 1)), 3, 3): 384,
        (4, 8, -8, ((1, 8), (2, 4)), (((2,), 4),), 4, 4): 960,
        (4, 8, -4, ((1, 8), (2, 4)), (((1, 1), 4),), 4, 4): 192,
        (4, 8, 0, ((0, 4), (2, 8)), (((1, 1, 1, 1), 2),), 2, 2): 6})
    check(pat == expect, "F node patterns (n1, e, C2, C.E counts, m-lists per pair, #V, #H): "
          + "; ".join(f"{k} x{v}" for k, v in sorted(pat.items())))

# ---- G: certified job inventory, with INDEPENDENT recomputation of every exact slice claim -----------------------
# Independent of certified_driver.py: rational kernel via fmpz_mat.nullspace (not HNF + LLL), particular solution
# x_p = A^T (A A^T)^-1 t, and integer solvability via a row-HNF of the column lattice of A.
# The real-ellipsoid quantities are intrinsic (centre value of Gamma49, max x^2 - c2min, dual norm of Gamma49), so
# they must coincide exactly with the driver's witness, whatever basis the driver used.
from flint import fmpz_mat, fmpq_mat, fmpq  # noqa: E402
sys.path.insert(0, str(HERE / "enumeration"))
import run_certified  # noqa: E402
results = [json.loads(line) for line in (HERE / "enumeration/certified_results.jsonl").read_text().splitlines() if line.strip()]
keys = [r["job"] for r in results]
expected = {run_certified.key(j) for j in run_certified.inventory()}
pid = run_certified.producer_id()
okj = len(keys) == len(set(keys)) and set(keys) == expected and all(r.get("producer") == pid for r in results)
bad = []
if ad is not None:
    Gq = fmpq_mat([[fmpq(int(v)) for v in rw] for rw in G.tolist()])
    rowK, rowF1, rowE, row49 = ([int(v) for v in deg], [int(v) for v in F1row], [int(v) for v in exc], [int(v) for v in P[48]])
    cache = {}

    def slice_info(n1, e, c2min, v):
        kk = (n1, e, c2min, v)
        if kk in cache:
            return cache[kk]
        rows = [rowK, rowF1, rowE] + ([row49] if v is not None else [])
        t = [8, n1, e] + ([v] if v is not None else [])
        A = fmpz_mat(rows)
        H = fmpz_mat(A.transpose().tolist()).hnf()              # rows span the lattice A Z^64 (row vectors in Z^r)
        res = list(t)
        for i in range(H.nrows()):
            row = [int(H[i, j]) for j in range(H.ncols())]
            piv = next((j for j, x in enumerate(row) if x), None)
            if piv is None:
                continue
            if res[piv] % row[piv]:
                break
            q = res[piv] // row[piv]
            res = [rv - q * xv for rv, xv in zip(res, row)]
        solvable = all(x == 0 for x in res)
        Aq = fmpq_mat(A.tolist())
        xp = Aq.transpose() * (Aq * Aq.transpose()).inv() * fmpq_mat([[fmpq(x)] for x in t])
        X, nul = A.nullspace()
        N = fmpq_mat([[X[i, j] for j in range(nul)] for i in range(64)])
        M = -(N.transpose() * Gq * N)
        # independent positive-definiteness check of M (exact LDL^T pivots, all > 0)
        nn = M.nrows()
        Mw = [[M[i, j] for j in range(nn)] for i in range(nn)]
        pd = True
        for k in range(nn):
            pk_ = Mw[k][k]
            if not pk_ > 0:
                pd = False
                break
            for i in range(k + 1, nn):
                f_ = Mw[i][k] / pk_
                if f_ != 0:
                    for j in range(k + 1, nn):
                        Mw[i][j] -= f_ * Mw[k][j]
        bvec = N.transpose() * Gq * xp
        c = (xp.transpose() * Gq * xp)[0, 0]
        w = M.solve(bvec)
        R = c + (bvec.transpose() * w)[0, 0] - c2min
        l = fmpq_mat([[fmpq(x)] for x in row49])
        l0 = (l.transpose() * (xp + N * w))[0, 0]
        pv = N.transpose() * l
        S = (pv.transpose() * M.solve(pv))[0, 0]
        cache[kk] = (solvable, R, l0, S, pd)
        return cache[kk]

    for r in results:
        n1s, es, cs, vs = r["job"].split("|")
        n1, e, c2min = int(n1s), int(es), int(cs)
        v = None if vs == "BOUND" else int(vs)
        fields_ok = (r.get("d") == 8 and r.get("n1") == n1 and r.get("e") == e and r.get("c2min") == c2min
                     and r.get("fix") == (None if v is None else f"49={v}"))
        st = r["status"].split()[0]
        if not fields_ok:
            bad.append(r["job"] + " fields"); continue
        if st == "CONGRUENCE_EMPTY":
            if slice_info(n1, e, c2min, v)[0]:
                bad.append(r["job"] + " solvable")
        elif st == "EMPTY":
            si = slice_info(n1, e, c2min, v)
            if not (si[4] and si[1] < 0):
                bad.append(r["job"] + " R>=0")
        elif v is None:
            sol_, R, l0, S, pd = slice_info(n1, e, c2min, None)
            wit = r.get("witness", {})
            same = st == "BOUND" and wit.get("f0_49") == str(l0) and wit.get("R") == str(R) and wit.get("S49") == str(S)
            if not (same and pd and R >= 0 and S >= 0 and l0 <= 10 and (10 - l0) ** 2 >= R * S):
                bad.append(r["job"] + " bound")
        elif st != "COMPLETE":
            bad.append(r["job"] + " status")
else:
    okj = False
prov = json.loads((HERE / "enumeration/PROVENANCE.json").read_text())
import hashlib  # noqa: E402
prov_ok = (prov["producer_id_in_records"] == pid
           and prov["certified_enum_c_sha256"] == hashlib.sha256((HERE / "enumeration/certified_enum.c").read_bytes()).hexdigest())
if not prov_ok:
    bad.append("PROVENANCE.json inconsistent with the current producer files")
okj &= not bad
check(okj, f"G inventory: {len(keys)} result records = exactly the {len(expected)} generated jobs, all from the current "
      "producer files; record fields match their job key; M positive definite; every CONGRUENCE_EMPTY / EMPTY claim and every BOUND witness "
      "(Gamma49.C <= 10 on the real ellipsoid) independently recomputed in exact arithmetic; split jobs COMPLETE otherwise"
      + (f"; bad: {bad[:5]}" if bad else ""))

print("ALL PASS" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
