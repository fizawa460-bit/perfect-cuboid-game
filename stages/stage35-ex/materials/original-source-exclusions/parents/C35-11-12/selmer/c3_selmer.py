"""Stage35EX C35-03: 2-Selmer group of J3 = Jac(C3'), C3': Y^2 = ft(u) = u*Q(u), Q(u) = P(-u),
P = t^6-5t^5-8t^4-5t^3-8t^2-5t-1. (C3': u -> -u of C3: Y^2 = -u P(u).)  genus 3, odd degree 7.

Descent map (Cassels/Schaefer, odd degree, monic):  J3(Q)/2 -> {(a, alpha) in Q*/Q*^2 x K*/K*^2 : a*N(alpha) in Q*^2},
point (u0,Y0) -> (u0, u0 + t)   [K = Q[t]/P, root of Q is T = -t, so u0 - T = u0 + t];
Weierstrass point u0 = 0 -> (Q(0), t) = (-1, t);  infinity -> 1.
Bad primes S = {2, 3461}, disc(ft) = 2^16*3461.  h_K odd (Minkowski + 2O = p^3), so K(S,2) = O_S^*/squares.
Selmer = alpha in K(S,2) (a := N(alpha)) whose localizations lie in the local images at inf, 2, 3461.
dim Sel = rank + dim J3(Q)[2] + dim Sha[2];  J3(Q)[2] = Z/2 (ft = u * irreducible sextic).
Pure Python (fractions).  Local images are spanned by images of Q_p-points; their dimension is
checked against the theoretical value dim J(Q_p)[2] + g*[p=2] (g=3), and dim J(R)[2] - g at inf."""
from fractions import Fraction as Fr
from itertools import product
import math, random, sys
sys.setrecursionlimit(10000)
import kfield as KF

N = 6
P = KF.P
p3 = 3461

# ---------- K arithmetic in basis coordinates (Fractions) ----------
def from_pow(pc):
    return KF.to_basis(pc)

def mul(x, y):
    return KF.mulb_fr(x, y)

def one():
    return [Fr(1)] + [Fr(0)] * (N - 1)

def mulmat(x):
    cols = [mul(x, [1 if k == j else 0 for k in range(N)]) for j in range(N)]
    return [[cols[j][i] for j in range(N)] for i in range(N)]

def inv(x):
    M = mulmat(x)
    return KF.solve(M, one())

def norm(x):
    return KF.det(mulmat(x))

def pw(x, k):
    r = one()
    if k < 0:
        x, k = inv(x), -k
    for _ in range(k):
        r = mul(r, x)
    return r

def to_pow(x):
    return KF.to_pow(x)

# ---------- global S-unit generators ----------
U1 = from_pow([Fr(-1, 4), Fr(-17, 4), Fr(-5, 4), Fr(-13, 4), Fr(-17, 4), Fr(3, 4)])
U2 = from_pow([Fr(13, 4), Fr(10), Fr(11, 4), Fr(8), Fr(33, 4), Fr(-3, 2)])
U3 = from_pow([Fr(-2), Fr(-35, 4), Fr(-3), Fr(-23, 4), Fr(-7), Fr(5, 4)])
MINUS1 = [Fr(-1)] + [Fr(0)] * 5
T_EL = from_pow([0, 1])          # the element t

def search_norm(targets, box=2):
    for c in product(range(-box, box + 1), repeat=N):
        if not any(c):
            continue
        x = [Fr(v) for v in c]
        n = norm(x)
        if n in targets:
            return x, n
    return None, None

# ---------- real places ----------
def real_roots():
    # P has exactly two real roots: near -1.1383 and 6.4045; refine by bisection
    def Pv(z):
        return sum(c * z ** i for i, c in enumerate(P))
    out = []
    for lo, hi in ((-1.5, -1.0), (6.0, 7.0)):
        for _ in range(200):
            mid = (lo + hi) / 2
            if (Pv(lo) < 0) == (Pv(mid) < 0):
                lo = mid
            else:
                hi = mid
        out.append((lo + hi) / 2)
    return out

RR = real_roots()

def sign_at(x, r):
    pc = to_pow(x)
    v = sum(float(c) * r ** i for i, c in enumerate(pc))
    assert abs(v) > 1e-9, "sign ambiguous"
    return 0 if v > 0 else 1

def vec_inf(a, alpha):
    return [0 if a > 0 else 1] + [sign_at(alpha, r) for r in RR]

# ---------- 2-adic: K (x) Q_2 is one field L (e=3, f=2) ----------
def v2(q):
    q = Fr(q)
    if q == 0:
        return 10 ** 9
    n, d = q.numerator, q.denominator
    a = 0
    while n % 2 == 0:
        n //= 2; a += 1
    while d % 2 == 0:
        d //= 2; a -= 1
    return a

PI2 = None          # global element with v_p = 1 at the unique prime above 2

def vP2(x):
    vn = v2(norm(x))
    assert vn % 2 == 0
    return vn // 2

def mod8(x):
    out = []
    for c in x:
        assert c.denominator % 2 == 1
        out.append(c.numerator * pow(c.denominator, -1, 8) % 8)
    return tuple(out)

def mul8(a, b):
    return tuple(KF.mulb(list(a), list(b), 8))

UNITS8, SQ8 = None, None

def build_2adic():
    global UNITS8, SQ8, BASIS_CLASSES
    allel = list(product(range(8), repeat=N))
    # unit iff norm odd; norm parity from O/2: element is unit iff not in the prime p
    # p/2O = nilradical of O/2O (2O = p^3)
    nil2 = set()
    for x in product(range(2), repeat=N):
        y = x
        for _ in range(3):
            y = tuple(KF.mulb(list(y), list(x), 2))
        if all(v == 0 for v in y) or all(v == 0 for v in tuple(KF.mulb(list(x), list(x), 2))) or True:
            pass
    # direct: unit iff N(x) odd
    def isunit(x):
        return norm([Fr(v) for v in x]).numerator % 2 == 1
    reps2 = [x for x in product(range(2), repeat=N) if isunit(x)]
    reps2 = set(reps2)
    UNITS8 = [x for x in allel if tuple(v % 2 for v in x) in reps2]
    SQ8 = set(mul8(x, x) for x in UNITS8)
    return len(UNITS8), len(SQ8)

def unit_class_basis():
    """greedy F2-basis of U/U^2 (U = (O/8)^*), dimension 7 expected"""
    basis = []
    span = {tuple([1] + [0] * (N - 1))}
    reps = [tuple([1] + [0] * (N - 1))]
    rnd = random.Random(1)
    pool = UNITS8[:]
    rnd.shuffle(pool)
    for x in pool:
        # x in span*SQ ?
        if any(mul8(x, s) in SQ8 for s in reps):
            continue
        basis.append(x)
        reps = reps + [mul8(x, s) for s in reps]
        if len(basis) == 8:
            break
    return basis, reps

def coords_unit2(u, basis):
    k = len(basis)
    for mask in range(1 << k):
        y = u
        for i in range(k):
            if mask >> i & 1:
                y = mul8(y, basis[i])
        if y in SQ8:
            return [(mask >> i) & 1 for i in range(k)]
    raise RuntimeError("no coordinates")

def vec_2(a, alpha, B2):
    a = Fr(a)
    va = v2(a)
    w = a / Fr(2) ** va
    w8 = w.numerator * pow(w.denominator, -1, 8) % 8
    qc = [va % 2, 0 if w8 % 4 == 1 else 1, 0 if w8 in (1, 7) else 1]
    v = vP2(alpha)
    unit = mul(alpha, pw(PI2, -v))
    return qc + [v % 2] + coords_unit2(mod8(unit), B2)

# ---------- 3461-adic ----------
def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)

PREC = 6
M3 = p3 ** PREC

def poly_divmod_mod(a, b, m):
    a = [c % m for c in a]
    inv_l = pow(b[-1], -1, m)
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        if a[-1] % m == 0:
            a.pop(); continue
        c = a[-1] * inv_l % m
        d = len(a) - len(b)
        q[d] = c
        for i, y in enumerate(b):
            a[i + d] = (a[i + d] - c * y) % m
        a.pop()
    while a and a[-1] % m == 0:
        a.pop()
    return q, a

def pmulm(a, b, m):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] = (r[i + j] + x * y) % m
    return r

def paddm(a, b, m):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % m for i in range(n)]

def pxgcd_p(a, b, p):
    r0, r1, s0, s1, t0, t1 = [c % p for c in a], [c % p for c in b], [1], [0], [0], [1]
    def trim(x):
        while len(x) > 1 and x[-1] % p == 0: x.pop()
        return x
    r0, r1 = trim(r0), trim(r1)
    while not (len(r1) == 1 and r1[0] % p == 0):
        q, r = poly_divmod_mod(r0, r1, p)
        r = r if r else [0]
        r0, r1 = r1, trim(r)
        s0, s1 = s1, trim(paddm(s0, [(-c) % p for c in pmulm(q, s1, p)], p))
        t0, t1 = t1, trim(paddm(t0, [(-c) % p for c in pmulm(q, t1, p)], p))
    c = pow(r0[-1], -1, p) if len(r0) == 1 else None
    assert len(r0) == 1, "not coprime"
    return [x * c % p for x in s0], [x * c % p for x in t0]

def hensel_split(f, g, h, p, k):
    """f = g h mod p, g,h monic coprime mod p -> lift to mod p^k (linear lifting)"""
    s, t = pxgcd_p(g, h, p)       # s g + t h = 1 mod p
    m = p
    for _ in range(k - 1):
        m2 = m * p
        e = paddm(f, [(-c) % m2 for c in pmulm(g, h, m2)], m2)
        e = [c // m for c in e]    # (f - gh)/m mod p
        # solve dg h + dh g = e mod p with deg dg < deg g, deg dh < deg h
        dh = poly_divmod_mod(pmulm(s, e, p), h, p)[1] or [0]
        dg = poly_divmod_mod(pmulm(t, e, p), g, p)[1] or [0]
        g = paddm(g, [c * m for c in dg], m2)
        h = paddm(h, [c * m for c in dh], m2)
        m = m2
    return g, h

def setup_3461():
    p = p3
    fp = [c % p for c in P]
    s0 = (-2342) % p
    # g0 = (t - s0)^2, h0 = P / g0 mod p
    g0 = pmulm([(-s0) % p, 1], [(-s0) % p, 1], p)
    h0, rem = poly_divmod_mod(fp, g0, p)
    assert not rem, rem
    ga, gb = hensel_split([c % M3 for c in P], g0, h0, p, PREC)
    # shift ga to z = t - s0: ga(z + s0)
    za = [0, 0, 0]
    # expand ga(t) with t = z + s0
    for i, c in enumerate(ga):
        for j in range(i + 1):
            za[j] = (za[j] + c * math.comb(i, j) * pow(s0, i - j, M3)) % M3
    c0, c1 = za[0], za[1]
    assert za[2] % M3 == 1
    assert c0 % p == 0 and c1 % p == 0 and c0 % (p * p) != 0, "not Eisenstein"
    rho = (c0 // p) * (-1) % p          # residue of varpi^2 / p  = -c0/p
    return dict(ga=ga, gb=gb, s0=s0, c0=c0, c1=c1, rho=rho)

def vp(q, p):
    q = Fr(q)
    if q == 0:
        return 10 ** 9
    n, d, a = q.numerator, q.denominator, 0
    while n % p == 0: n //= p; a += 1
    while d % p == 0: d //= p; a -= 1
    return a

def frac_mod(c, m):
    return c.numerator * pow(c.denominator, -1, m) % m

def vint(n, p):
    if n == 0: return 10 ** 9
    a = 0
    while n % p == 0: n //= p; a += 1
    return a

def class_3461(a, alpha, D):
    p = p3
    out = []
    va = vp(a, p)
    w = Fr(a) / Fr(p) ** va
    out += [va % 2, 0 if legendre(frac_mod(w, p), p) == 1 else 1]
    # scale alpha by p^k so its power coords are p-integral
    pc = to_pow(alpha)
    shift = -min(vp(c, p) for c in pc if c != 0)
    pc = [c * Fr(p) ** shift for c in pc]
    xi = [frac_mod(c, M3) for c in pc]
    # L_a : reduce mod ga, write in z = t - s0: A + B z
    r = poly_divmod_mod(xi, D["ga"], M3)[1] or [0]
    r = r + [0] * (2 - len(r))
    A = (r[0] + r[1] * D["s0"]) % M3
    Bc = r[1] % M3
    eA, eB = vint(A, p), vint(Bc, p)
    assert min(eA, eB) < PREC - 1, "precision"
    if 2 * eA < 2 * eB + 1:
        vL = 2 * eA
        res = (A // p ** eA) * pow(D["rho"], -eA, p) % p
    else:
        vL = 2 * eB + 1
        res = (Bc // p ** eB) * pow(D["rho"], -eB, p) % p
    vL += 2 * (-shift)                       # undo scaling: p = varpi^2 * unit(res rho^-1)
    res = res * pow(D["rho"], shift, p) % p  # p^-shift contributes rho^{shift} to residue
    out += [vL % 2, 0 if legendre(res, p) == 1 else 1]
    # L_b : unramified quartic
    rb = poly_divmod_mod(xi, D["gb"], M3)[1] or [0]
    eb = min(vint(c, p) for c in rb if c % M3 != 0)
    assert eb < PREC - 1
    ub = [(c // p ** eb) % p for c in rb]
    gbp = [c % p for c in D["gb"]]
    # quadratic character in F_p[t]/gb : u^((p^4-1)/2)
    e = (p ** 4 - 1) // 2
    res_b, base, ee = [1], ub, e
    while ee:
        if ee & 1:
            res_b = poly_divmod_mod(pmulm(res_b, base, p), gbp, p)[1] or [0]
        base = poly_divmod_mod(pmulm(base, base, p), gbp, p)[1] or [0]
        ee >>= 1
    res_b = res_b + [0] * (4 - len(res_b))
    chi_b = 0 if res_b[0] % p == 1 and all(c % p == 0 for c in res_b[1:]) else 1
    assert chi_b == 0 or (res_b[0] % p == p - 1 and all(c % p == 0 for c in res_b[1:]))
    vLb = eb - shift
    out += [vLb % 2, chi_b]
    return out

# ---------- F2 linear algebra ----------
def rref(rows):
    rows = [r[:] for r in rows]
    piv, R = [], []
    for r in rows:
        r = r[:]
        for (c, br) in zip(piv, R):
            if r[c]:
                r = [x ^ y for x, y in zip(r, br)]
        if any(r):
            c = r.index(1)
            # reduce existing
            R = [([x ^ y for x, y in zip(br, r)] if br[c] else br) for br in R]
            piv.append(c); R.append(r)
    return piv, R

def in_span(v, piv, R):
    v = v[:]
    for c, br in zip(piv, R):
        if v[c]:
            v = [x ^ y for x, y in zip(v, br)]
    return not any(v)

# ---------- sampling local points ----------
def ft(u):
    return u * sum(c * (-u) ** i for i, c in enumerate(P))

def is_sq_Q2(q):
    if q == 0: return False
    v = v2(q)
    if v % 2: return False
    w = Fr(q) / Fr(2) ** v
    return frac_mod(w, 8) == 1

def is_sq_Qp(q, p):
    if q == 0: return False
    v = vp(q, p)
    if v % 2: return False
    w = Fr(q) / Fr(p) ** v
    return legendre(frac_mod(w, p), p) == 1

def point_image(u0):
    if u0 == 0:
        return Fr(-1), T_EL
    return Fr(u0), [Fr(u0) + c if i == 0 else c for i, c in enumerate(T_EL)]

def sqrt2adic(w, K):
    """w odd integer, w = 1 mod 8: return s with s^2 = w mod 2^K"""
    s = 1
    for k in range(3, K):
        if (s * s - w) % (2 ** (k + 1)) != 0:
            s += 2 ** (k - 1)
    assert (s * s - w) % (2 ** K) == 0
    return s

def is_sq_Q2_approx(num_mod, val, K):
    """value = 2^val * unit, unit known mod 2^K (num_mod odd)"""
    return val % 2 == 0 and num_mod % 8 == 1

def sq_in_quadratic(A, B, m, K=60):
    """Is A + B*sqrt(m) a square in Q_2(sqrt m)? (m a non-square in Q_2, A,B rational)."""
    A, B = Fr(A), Fr(B)
    if B == 0:
        # A square in Q2, or A = m * square
        return is_sq_Q2(A) or is_sq_Q2(A / m)
    Nn = A * A - m * B * B
    if not is_sq_Q2(Nn):
        return False
    v = v2(Nn)
    val_n = v // 2
    E = max(0, -v2(A), -val_n) + 2                 # scale 2^E makes A*2^E and n*2^E integral
    KK = K + E + abs(val_n)
    w = Nn / Fr(2) ** v
    s = sqrt2adic(frac_mod(w, 2 ** KK), KK)        # sqrt(w) mod 2^(KK-1)
    for eps in (1, -1):
        # Xs = 2^E * (A + eps*n) = 2^(E+1) * X  (exact mod 2^KK)
        Xs = (frac_mod(A * Fr(2) ** E, 2 ** KK) + eps * (2 ** (val_n + E)) * s) % (2 ** KK)
        if Xs == 0:
            continue
        vx = vint(Xs, 2)
        if vx > KK - 6:
            continue                                # cancellation beyond precision: skip (never a false yes)
        unit = (Xs >> vx) % 8
        vX = vx - 1 - E
        if vX % 2 == 0 and unit == 1:
            return True
    return False

def quad_divisor_images(rnd, count):
    """images of Q2-rational degree-2 divisors with U(x) = (x - r)^2 - m irreducible over Q2"""
    out = []
    ms = [Fr(v) for v in (-1, 2, -2, 3, -3, 5, -5, 6, -6, 10, -10, 7, -7, 14, -14)]
    for _ in range(count):
        m = rnd.choice(ms) * Fr(rnd.randint(1, 30)) ** 2 * Fr(4) ** rnd.randint(-5, 5)
        if is_sq_Q2(m):
            continue
        r = Fr(rnd.randint(-200, 200)) * Fr(2) ** rnd.randint(-8, 6)
        # ft(r + sqrt m) = A + B sqrt m
        # expand polynomial in s = sqrt(m): (r + s)^k
        coeffs = [0] + [c * (-1) ** i for i, c in enumerate(P)]   # ft(u) = u*Q(u), Q(u)=P(-u)
        A = Fr(0); B = Fr(0)
        for k, c in enumerate(coeffs):
            if c == 0: continue
            for j in range(k + 1):
                term = Fr(c) * math.comb(k, j) * r ** (k - j)
                if j % 2 == 0:
                    A += term * m ** (j // 2)
                else:
                    B += term * m ** (j // 2)
        if not sq_in_quadratic(A, B, m):
            continue
        # divisor image: U(T) with U(x) = (x-r)^2 - m ; Q-comp U(0), K-comp U(-t)
        a = r * r - m
        if a == 0: continue
        mt = [-r, Fr(-1)]                     # -t - r in power coords: -r - t
        alpha = from_pow([(r * r - m), 2 * r, Fr(1)])     # (t + r)^2 - m = U(-t)
        out.append((a, alpha))
    return out

CUBICS = {  # monic U0 with Z_2[alpha] maximal: (coeffs low->high, kind)
    "x3+x+1": ([1, 1, 0, 1], "unram"),
    "x3-2": ([-2, 0, 0, 1], "eis"), "x3-6": ([-6, 0, 0, 1], "eis"),
    "x3-10": ([-10, 0, 0, 1], "eis"), "x3-14": ([-14, 0, 0, 1], "eis"),
    "x3+2x+2": ([2, 2, 0, 1], "eis"), "x3+2x2+2": ([2, 0, 2, 1], "eis"),
    "x3+2x2+2x+2": ([2, 2, 2, 1], "eis"),
}

def cub_mulmod(a, b, U0):
    r = [Fr(0)] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    for d in (4, 3):
        c = r[d]
        if c:
            for i in range(4):
                r[d - 3 + i] -= c * U0[i]
    return r[:3]

_SQ_CUB = {}
def cub_squares(name):
    if name not in _SQ_CUB:
        U0 = CUBICS[name][0]
        sq = set()
        for c in product(range(8), repeat=3):
            y = cub_mulmod([Fr(v) for v in c], [Fr(v) for v in c], U0)
            sq.add(tuple(int(v) % 8 for v in y))
        _SQ_CUB[name] = sq
    return _SQ_CUB[name]

def cub_val(x, kind):
    vs = [v2(c) for c in x]
    if kind == "unram":
        return min(vs)
    return min(3 * vs[0], 3 * vs[1] + 1, 3 * vs[2] + 2)

def sq_in_cubic(x, name):
    U0, kind = CUBICS[name]
    if all(c == 0 for c in x):
        return False
    v = cub_val(x, kind)
    if v % 2:
        return False
    if kind == "unram":
        y = [c / Fr(2) ** v for c in x]
    else:
        # divide by alpha^v using alpha^3 = -U0[0] - U0[1] alpha - U0[2] alpha^2 ; alpha^-1 exact
        ainv = KF.solve([[Fr(U0i) for U0i in row] for row in (
            # multiplication-by-alpha matrix columns: 1->alpha, alpha->alpha^2, alpha^2->alpha^3
            [0, 0, -U0[0]], [1, 0, -U0[1]], [0, 1, -U0[2]])], [Fr(1), Fr(0), Fr(0)])
        y = x[:]
        for _ in range(v):
            y = cub_mulmod(y, ainv, U0)
    assert all(c.denominator % 2 == 1 for c in y)
    ym = tuple(frac_mod(c, 8) for c in y)
    if all(c % 2 == 0 for c in ym) and kind == "unram":
        return False
    return ym in cub_squares(name)

def cubic_divisor_images(rnd, count):
    """Q2-rational degree-3 divisors: U(x) = lam^3 U0((x - r)/lam), U0 irreducible cubic over Q2.
    Rational iff ft(r + lam*alpha) is a square in Q2(alpha). Image = (-U(0), -U(-t))."""
    out = []
    coeffs = [0] + [c * (-1) ** i for i, c in enumerate(P)]   # ft(u) = u*Q(u)
    names = list(CUBICS)
    for _ in range(count):
        name = rnd.choice(names)
        U0 = CUBICS[name][0]
        r = Fr(rnd.randint(-300, 300)) * Fr(2) ** rnd.randint(-6, 6)
        lam = Fr(rnd.choice([1, 3, 5, 7, 9, 11, 13, 15])) * Fr(2) ** rnd.randint(-6, 6) * rnd.choice([1, -1])
        z = [r, lam, Fr(0)]                       # r + lam*alpha
        val = [Fr(0)] * 3
        zp = [Fr(1), Fr(0), Fr(0)]
        for c in coeffs:
            if c:
                val = [a + c * b for a, b in zip(val, zp)]
            zp = cub_mulmod(zp, z, U0)
        # scale by an even power of 2 (square) to clear 2-power denominators
        e = max(0, max(-v2(c) for c in val if c != 0))
        e += e % 2
        val = [c * Fr(2) ** e for c in val]
        try:
            ok = sq_in_cubic(val, name)
        except AssertionError:
            continue
        if not ok:
            continue
        # U(x) = lam^3 U0((x-r)/lam) = sum_i U0_i lam^(3-i) (x-r)^i
        def Uat_poly(shift_sign):
            # returns power-coords in t of U(-t) : x = -t
            res = [Fr(0)] * 4
            for i, ci in enumerate(U0):
                # (x - r)^i with x = -t : (-t - r)^i
                for j in range(i + 1):
                    res[j] += Fr(ci) * lam ** (3 - i) * math.comb(i, j) * (-1) ** j * (-r) ** (i - j)
            return res
        U0val = sum(Fr(ci) * lam ** (3 - i) * (-r) ** i for i, ci in enumerate(U0))   # U(0)
        if U0val == 0:
            continue
        alpha = from_pow([-c for c in Uat_poly(1)])
        out.append((-U0val, alpha))
    return out

def main():
    global PI2
    print("unit norms:", norm(U1), norm(U2), norm(U3))
    PI2, n2 = search_norm({Fr(4), Fr(-4)})
    print("generator of prime above 2:", PI2, "norm", n2)
    GA = [Fr(v) for v in (10, -2, -11, -8, -10, 2)]     # from find_ga.py (LLL); unique prime of norm 3461
    na = norm(GA)
    print("generator of degree-1 prime above 3461:", GA, "norm", na)
    assert PI2 is not None and GA is not None
    GB = mul([Fr(p3)] + [Fr(0)] * 5, pw(GA, -2))      # (3461) = pa^2 pb  =>  pb = 3461/ga^2
    print("norm of 3461/ga^2:", norm(GB), "= +-3461^4 ?", abs(norm(GB)) == p3 ** 4)
    gens = [("-1", MINUS1), ("u1", U1), ("u2", U2), ("u3", U3), ("pi2", PI2), ("ga", GA), ("gb", GB)]

    nU, nS = build_2adic()
    B2, _ = unit_class_basis()
    print("2-adic: |(O/8)^*| =", nU, "|squares| =", nS, "dim U/U^2 =", len(B2))
    D3 = setup_3461()

    def local_vec(place, a, alpha):
        if place == "inf": return vec_inf(a, alpha)
        if place == 2: return vec_2(a, alpha, B2)
        return class_3461(a, alpha, D3)

    # local images from points
    expected = {"inf": 1, 2: 4, p3: 2}
    images = {}
    rnd = random.Random(7)
    for place in ("inf", 2, p3):
        vecs = []
        cands = [Fr(0)]
        if place == "inf":
            cands += [Fr(-k, 10) for k in range(1, 64)] + [Fr(k, 10) for k in range(12, 80)]
        else:
            pp = 2 if place == 2 else p3
            for _ in range(4000):
                e = rnd.randint(-3, 3)
                num = rnd.randint(-10 ** 6, 10 ** 6)
                cands.append(Fr(num) * Fr(pp) ** e)
        for u0 in cands:
            y2 = ft(u0)
            ok = (y2 >= 0 if place == "inf" else (is_sq_Q2(y2) if place == 2 else is_sq_Qp(y2, p3))) if u0 != 0 else True
            if not ok or (u0 != 0 and y2 == 0):
                continue
            a, al = point_image(u0)
            try:
                vecs.append(local_vec(place, a, al))
            except AssertionError:
                continue
        if place == 2:
            nq = 0
            for (a, al) in quad_divisor_images(rnd, 6000):
                try:
                    vecs.append(local_vec(2, a, al)); nq += 1
                except AssertionError:
                    continue
            print("  2-adic: added", nq, "irreducible degree-2 divisor images")
            nc = 0
            for (a, al) in cubic_divisor_images(rnd, 3000):
                try:
                    vecs.append(local_vec(2, a, al)); nc += 1
                except AssertionError:
                    continue
            print("  2-adic: added", nc, "irreducible degree-3 divisor images")
        piv, R = rref(vecs)
        images[place] = (piv, R)
        print("place", place, "points used", len(vecs), "image dim", len(R), "expected", expected[place])

    # global Selmer
    gvecs = {}
    sel = []
    for mask in range(1 << len(gens)):
        al = one()
        for i, (nm, g) in enumerate(gens):
            if mask >> i & 1:
                al = mul(al, g)
        a = norm(al)
        ok = True
        for place in ("inf", 2, p3):
            v = local_vec(place, a, al)
            if not in_span(v, *images[place]):
                ok = False
                break
        if ok:
            sel.append([nm for i, (nm, g) in enumerate(gens) if mask >> i & 1])
    print("Selmer elements (as products of generators):", sel)
    d = int(round(math.log2(len(sel))))
    print("#Sel =", len(sel), "dim Sel^2 =", d, " => rank J3(Q) <= dim Sel - 1 =", d - 1)
    # torsion point sanity
    a0, t0 = point_image(Fr(0))
    print("torsion image (a,alpha)=(-1,t) in all local images:",
          all(in_span(local_vec(pl, a0, t0), *images[pl]) for pl in ("inf", 2, p3)))

if __name__ == "__main__":
    main()
