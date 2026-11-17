"""checks9 / borel9.py -- exact checks for the Borel (Iwahori) lemma that makes cluster conjugators octahedral.

Lemma (Borel). Let x, y be elliptic involutions of Gamma_0 = PQ^1(P^2) with distinct fixed points, t = tr(x y)
(lifts in Q^1, x^2 = y^2 = -1), and let P be an odd prime of Z[sqrt2]. If the reductions of x and y mod P have a
common eigenline (equivalently: x, y lie in one Iwahori subgroup at P, i.e. both fix an edge of the Bruhat-Tits
tree at the vertex of Q_B), then t = +-2 mod P, i.e. P | t^2 - 4 = 4 m (m + 2) where t = +-(2 + 2m).
Hence a pair at distance l_min (t = 2 + 2 sqrt2, t^2 - 4 = 8 (1 + sqrt2)) lies in NO Iwahori at any odd P.

Part A (exact, Z[sqrt2]): the admissible distances d (2 cosh d = 2 + 2m, m in Z[sqrt2], conjugate of m in [-2, 0])
  up to cosh d <= CMAX, with the odd primes dividing N(m) N(m + 2).
Part B (exact, finite fields): for every residue field F_q of an odd prime of Z[sqrt2] with q <= QMAX, all X in
  SL_2(F_q) with X^2 = -I; for every pair: common eigenline  =>  tr(XY) = +-2 (and the converse for X != +-Y).
Part C (exact, the real group): the elliptic involutions of Gamma_0 found by route-E/e13/traces.py (word depth 9),
  reduced mod P through an explicit splitting Q_B / P Q_B = M_2(F_q) found by search, for every odd P with
  N(P) <= NMAX: (i) every involution has 2 eigenlines if -1 is a square in F_q and 0 otherwise; (ii) no pair with
  |tr| = 2 + 2 sqrt2 (adjacent) shares an eigenline; (iii) control: pairs whose t^2 - 4 is divisible by P do;
  (iv) labels: two involutions with the same label (class mod 2Q_B) have t = +-(2 + 2m) with m in 2Z[sqrt2], so an
  adjacent pair (m = sqrt2) always has two different labels.
usage (from the repository root):  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks9/borel9.py [NMAX=50 [DEPTH=9]]
  (Part C needs stages/.../MB104/route-E/e13/traces.py and filt.py; it is skipped with a note if they are absent.)
"""
import sys, os, math, itertools, io, contextlib, importlib.util
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
E13 = os.path.normpath(os.path.join(HERE, "..", "..", "..", "route-E", "e13"))
CMAX, QMAX = 400, 25
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 50          # Part C: odd primes P with N(P) <= NMAX
R2 = math.sqrt(2)
ok = True


def factor(n):
    n = abs(n); f = []; d = 2
    while d * d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1
    if n > 1: f.append(n)
    return f


# ---------------- Part A ----------------
print("Part A: admissible distances d with 2cosh d = 2 + 2m (m = x + y sqrt2, conj(m) in [-2, 0]), cosh d <= %d" % CMAX)
rows = []
for y in range(0, 200):
    for x in range(-int(2 + y * R2) - 1, int(y * R2) + 2):
        m = x + y * R2; mc = x - y * R2
        if m <= 0 or not (-2 - 1e-12 <= mc <= 1e-12) or 1 + m > CMAX: continue
        Nm, Nm2 = x * x - 2 * y * y, (x + 2) ** 2 - 2 * y * y
        odd = sorted(set(p for p in factor(Nm) + factor(Nm2) if p != 2))
        rows.append((math.acosh(1 + m), x, y, Nm, Nm2, odd))
rows.sort()
free = [r for r in rows if not r[5]]
for d, x, y, Nm, Nm2, odd in rows[:12]:
    print("  d = %.6f  m = %d + %d sqrt2  N(m) = %d  N(m+2) = %d  odd primes of N(t^2-4): %s" % (d, x, y, Nm, Nm2, odd or "none"))
print("  ... %d admissible distances up to cosh d <= %d; with no odd prime: %s" %
      (len(rows), CMAX, ["%.4f (m=%d+%dsqrt2)" % (r[0], r[1], r[2]) for r in free]))
lmin = math.acosh(1 + R2)
ok &= abs(rows[0][0] - lmin) < 1e-12 and not rows[0][5]
ok &= [r for r in rows if r[0] <= 1.6 + 1e-12] == rows[:1]
print("  smallest admissible distance = l_min = %.6f, no odd prime: %s; the only one <= 1.6: %s" %
      (lmin, not rows[0][5], [r for r in rows if r[0] <= 1.6] == rows[:1]))


# ---------------- finite fields F_q = F_p or F_p[s]/(s^2 - 2) ----------------
class Fq:
    def __init__(s, p, inert, r=None):
        s.p, s.inert, s.r = p, inert, r                       # r = sqrt2 mod p in the split case
        s.q = p * p if inert else p
    def el(s, x, y=0):                                        # x + y sqrt2
        return ((x % s.p, y % s.p) if s.inert else ((x + y * s.r) % s.p, 0))
    def add(s, a, b): return ((a[0] + b[0]) % s.p, (a[1] + b[1]) % s.p)
    def neg(s, a): return ((-a[0]) % s.p, (-a[1]) % s.p)
    def mul(s, a, b):
        if s.inert: return ((a[0] * b[0] + 2 * a[1] * b[1]) % s.p, (a[0] * b[1] + a[1] * b[0]) % s.p)
        return ((a[0] * b[0]) % s.p, 0)
    def all(s): return [(x, y) for x in range(s.p) for y in (range(s.p) if s.inert else [0])]
    def inv(s, a):
        if s.inert:
            n = (a[0] * a[0] - 2 * a[1] * a[1]) % s.p; ni = pow(n, s.p - 2, s.p)
            return ((a[0] * ni) % s.p, (-a[1] * ni) % s.p)
        return (pow(a[0], s.p - 2, s.p), 0)


def mm(F, X, Y):
    return [[F.add(F.mul(X[i][0], Y[0][j]), F.mul(X[i][1], Y[1][j])) for j in range(2)] for i in range(2)]


def lines(F):
    Z, O = F.el(0), F.el(1)
    return [(O, a) for a in F.all()] + [(Z, O)]


def eiglines(F, X, L):
    out = []
    for v in L:
        w = (F.add(F.mul(X[0][0], v[0]), F.mul(X[0][1], v[1])), F.add(F.mul(X[1][0], v[0]), F.mul(X[1][1], v[1])))
        if F.add(F.mul(w[0], v[1]), F.neg(F.mul(w[1], v[0]))) == F.el(0): out.append(v)
    return frozenset(out)


def residue_fields(qmax):
    out = []
    for p in range(3, 200, 2):
        if any(p % d == 0 for d in range(3, int(p ** 0.5) + 1, 2)): continue
        if p % 8 in (1, 7):
            if p > qmax: continue
            r = next(r for r in range(p) if (r * r - 2) % p == 0)
            out.append((p, Fq(p, False, r))); out.append((p, Fq(p, False, p - r)))
        elif p * p <= qmax:
            out.append((p, Fq(p, True)))
    return out


# ---------------- Part B ----------------
print("Part B: all X in SL2(F_q) with X^2 = -I, q <= %d; common eigenline => tr(XY) = +-2" % QMAX)
seen_q = set()
for p, F in residue_fields(QMAX):
    if (F.q, F.inert) in seen_q: continue
    seen_q.add((F.q, F.inert))
    Z, O = F.el(0), F.el(1); mone = F.neg(O); two = F.el(2); mtwo = F.neg(two)
    E = F.all(); L = lines(F)
    invs = []
    for a, b, c in itertools.product(E, E, E):              # X = [[a, b], [c, -a]], a^2 + bc = -1
        if F.add(F.mul(a, a), F.mul(b, c)) == mone: invs.append([[a, b], [c, F.neg(a)]])
    eig = [eiglines(F, X, L) for X in invs]
    sqm1 = any(F.mul(e, e) == mone for e in E)
    bad = conv_bad = 0; npairs = 0
    for i in range(len(invs)):
        for j in range(i + 1, len(invs)):
            X, Y = invs[i], invs[j]
            if all(F.add(X[r][c], Y[r][c]) == Z for r in range(2) for c in range(2)): continue   # Y = -X
            npairs += 1
            XY = mm(F, X, Y); t = F.add(XY[0][0], XY[1][1])
            common = bool(eig[i] & eig[j])
            if common and t not in (two, mtwo): bad += 1
            if sqm1 and (t in (two, mtwo)) and not common: conv_bad += 1
    nl = sorted({len(e) for e in eig})
    print("  q = %3d (%s): %d involutions, eigenlines per involution %s, -1 square: %s, pairs %d, "
          "violations %d, converse violations %d" % (F.q, "inert" if F.inert else "split", len(invs), nl, sqm1, npairs, bad, conv_bad))
    ok &= bad == 0 and conv_bad == 0 and nl == ([2] if sqm1 else [0])


# ---------------- Part C ----------------
def load(name, argv):
    spec = importlib.util.spec_from_file_location(name, os.path.join(E13, name + ".py"))
    m = importlib.util.module_from_spec(spec); old = sys.argv; sys.argv = [name + ".py"] + argv
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
    sys.argv = old
    return m


if not os.path.exists(os.path.join(E13, "traces.py")):
    print("Part C: skipped (route-E/e13/traces.py not found at %s)" % E13)
else:
    DEPTH = sys.argv[2] if len(sys.argv) > 2 else "9"
    T = load("traces", [DEPTH])
    invs = T.invs
    print("Part C: %d elliptic involutions of Gamma_0 from traces.py (depth %s)" % (len(invs), DEPTH))
    K = T.K
    def tval(u): return T.tr(u)
    pairs = []
    for x, y in itertools.combinations(invs, 2):
        t = tval(T.mul(x, y)); pairs.append((x, y, t))
    adj = [(x, y, t) for x, y, t in pairs if abs(abs(t.val()) - (2 + 2 * R2)) < 1e-9]
    print("  pairs %d, adjacent pairs (|tr| = 2 + 2 sqrt2) %d" % (len(pairs), len(adj)))
    ok &= len(adj) > 0
    # labels: same class mod 2Q_B  =>  t = -(2 + 4z), i.e. m in 2Z[sqrt2]; so adjacent pairs have different labels
    same = [(x, y, t) for x, y, t in pairs if T.mod2(x) == T.mod2(y)]
    def m_even(t):                      # |t| = 2 + 2m with m in 2Z[sqrt2]
        for sg in (1, -1):
            mx, my = sg * t.x - 2, sg * t.y
            if mx % 2 == 0 and my % 2 == 0 and (mx // 2) % 2 == 0 and (my // 2) % 2 == 0: return True
        return False
    adj_same = sum(1 for x, y, t in adj if T.mod2(x) == T.mod2(y))
    same_even = all(m_even(t) for x, y, t in same)
    print("  labels (classes mod 2Q_B): %d classes among the involutions; adjacent pairs with equal label %d; "
          "pairs with equal label %d, all with m in 2Z[sqrt2]: %s" % (len({T.mod2(x) for x in invs}), adj_same, len(same), same_even))
    ok &= adj_same == 0 and same_even and len({T.mod2(x) for x in invs}) == 3
    # splitting Q_B / P Q_B = M_2(F_q): A = image of alpha (alpha^2 - alpha + 1 = 0), search Bm for beta
    for p, F in residue_fields(NMAX):
        Z, O = F.el(0), F.el(1)
        def kred(c): return F.el(c.x, c.y)
        def I2(c): return [[c, Z], [Z, c]]
        def madd(X, Y): return [[F.add(X[i][j], Y[i][j]) for j in range(2)] for i in range(2)]
        def msc(c, X): return [[F.mul(c, X[i][j]) for j in range(2)] for i in range(2)]
        A = [[Z, F.neg(O)], [O, O]]                         # companion matrix of x^2 - x + 1
        def rel_ok(Bm):
            AB = mm(F, A, Bm); BA = mm(F, Bm, A)
            # beta * alpha in the basis (1, alpha, beta, alpha beta) from traces.py T[(2,1)]
            c = T.T[(2, 1)]
            rhs = madd(madd(I2(kred(c[0])), msc(kred(c[1]), A)), madd(msc(kred(c[2]), Bm), msc(kred(c[3]), AB)))
            BB = mm(F, Bm, Bm)
            beta_sq = madd(Bm, I2(F.neg(O)))                 # beta^2 = beta - 1
            return BA == rhs and BB == beta_sq
        E = F.all(); Bm = None
        for a, b in itertools.product(E, E):                 # Bm = [[a, b], [c, 1 - a]], det = 1
            d = F.add(O, F.neg(a))
            for c in E:
                if F.add(F.mul(a, d), F.neg(F.mul(b, c))) != O: continue
                cand = [[a, b], [c, d]]
                if rel_ok(cand): Bm = cand; break
            if Bm: break
        if Bm is None:
            print("  P over %d (q = %d): no splitting found" % (p, F.q)); ok = False; continue
        AB = mm(F, A, Bm)
        def red(u):
            return madd(madd(I2(kred(u[0])), msc(kred(u[1]), A)), madd(msc(kred(u[2]), Bm), msc(kred(u[3]), AB)))
        # check: the splitting is multiplicative on the basis (all 16 products)
        basis = [T.one, T.a, T.b, T.V(T.Z, T.Z, T.Z, T.O)]
        mult_ok = all(red(T.mul(u, v)) == mm(F, red(u), red(v)) for u in basis for v in basis)
        L = lines(F)
        eig = {T.key(x): eiglines(F, red(x), L) for x in invs}
        sqm1 = any(F.mul(e, e) == F.neg(O) for e in E)
        nl = sorted({len(e) for e in eig.values()})
        adj_common = sum(1 for x, y, t in adj if eig[T.key(x)] & eig[T.key(y)])
        # control pairs: P | t^2 - 4, x != +-y mod P
        ctrl = [(x, y) for x, y, t in pairs if F.mul(kred(t), kred(t)) == F.el(4)
                and not (eig[T.key(x)] == eig[T.key(y)] and red(x) in (red(y), [[F.neg(v) for v in r] for r in red(y)]))]
        ctrl_common = sum(1 for x, y in ctrl if eig[T.key(x)] & eig[T.key(y)])
        good = mult_ok and nl == ([2] if sqm1 else [0]) and adj_common == 0 and (not sqm1 or ctrl_common == len(ctrl))
        print("  P over %3d (q = %3d, %s): splitting multiplicative %s; eigenlines per involution %s (-1 square: %s); "
              "adjacent pairs sharing a line %d; control pairs (P | t^2-4) %d, sharing a line %d" %
              (p, F.q, "inert" if F.inert else "split", mult_ok, nl, sqm1, adj_common, len(ctrl), ctrl_common))
        ok &= good
print("PASS" if ok else "FAIL")
