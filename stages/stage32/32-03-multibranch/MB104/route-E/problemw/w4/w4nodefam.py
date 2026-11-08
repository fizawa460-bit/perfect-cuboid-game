# pencils of w4node.out (node at (1,1) + >= 6 matched points, rank 7): |Omega(t)| at every event value of t
# (extra point: linear; fibre discriminant, node Hessian entries and discriminant: linear/quadratic) over F_p and
# F_p^2, at t = inf and at a generic t.  Hits (|Omega| <= 4, no fibre line) -> Singular gcd + factorization over F_p^2.
exec(open('w4node.py').read().split("N0 = 0 * 8")[0])
N0 = 0; base = [row(N0), drow(N0, 0), drow(N0, 1)]
NR = 11; assert pow(NR, (P - 1) // 2, P) == P - 1
def add(a, b): return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)
def sub(a, b): return ((a[0] - b[0]) % P, (a[1] - b[1]) % P)
def mul(a, b): return ((a[0] * b[0] + NR * a[1] * b[1]) % P, (a[0] * b[1] + a[1] * b[0]) % P)
def F(x): return (x % P, 0)
def isz(a): return a == (0, 0)
def inv2(a):
    n = (a[0] * a[0] - NR * a[1] * a[1]) % P; ni = pow(n, P - 2, P); return (a[0] * ni % P, (-a[1]) * ni % P)
def nullspace(rows):
    M = [r[:] for r in rows]; piv = []; rk = 0
    for c in range(9):
        k = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if k is None: continue
        M[rk], M[k] = M[k], M[rk]; f = pow(M[rk][c], P - 2, P); M[rk] = [v * f % P for v in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]: g = M[i][c]; M[i] = [(a - g * b) % P for a, b in zip(M[i], M[rk])]
        piv.append(c); rk += 1
    out = []
    for f in [c for c in range(9) if c not in piv]:
        v = [0] * 9; v[f] = 1
        for i, c in enumerate(piv): v[c] = (-M[i][f]) % P
        out.append(v)
    return out
ROWS = [row(p) for p in range(64)]
def lin(w, r):
    s = (0, 0)
    for a, b in zip(w, r): s = add(s, mul(a, F(b)))
    return s
def fibc(b, axis):  # coefficient vectors (over the 9 monomials) of the binary quadratic of the fibre
    x = xs[b]; q = [[0] * 9 for _ in range(3)]
    for c, (a, bb) in enumerate(MON):
        ex, ey = 2 - a, 2 - bb
        if axis == 0: q[ey][c] = pow(x, ex, P)
        else: q[ex][c] = pow(x, ey, P)
    return q
FIB = {(b, ax): fibc(b, ax) for b in range(8) for ax in (0, 1)}
HX = [[(2 - a) * (1 - a) % P if True else 0 for (a, b) in MON], [(2 - a) * (2 - b) % P for (a, b) in MON], [(2 - b) * (1 - b) % P for (a, b) in MON]]
def disc(q): return sub(mul(q[1], q[1]), mul(F(4), mul(q[0], q[2])))
def omega(w):
    fxx, fxy, fyy = [lin(w, r) for r in HX]
    trans = not isz(fxx) and not isz(fyy) and not isz(sub(mul(fxy, fxy), mul(fxx, fyy)))
    O1 = O2 = j = h = vl = 0; dq = {}
    for (b, ax), qc in FIB.items():
        q = [lin(w, r) for r in qc]
        if all(isz(c) for c in q): vl = 1; dq[(b, ax)] = False; continue
        d = not isz(disc(q)); dq[(b, ax)] = d
        if d or (b == 0 and trans):
            if ax == 0: O1 += 2
            else: O2 += 2
    if trans: j += 2
    for p in range(64):
        if p == N0 or not isz(lin(w, ROWS[p])): continue
        bx, by = divmod(p, 8)
        if dq[(bx, 0)] and dq[(by, 1)]:
            if TY[bx] == TY[by]: j += 1
            else: h += 1
    return O1 + O2 - 2 * j - h, vl
SQ = {}
def sqrtp(a):
    a %= P
    if a not in SQ: SQ[a] = next((x for x in range(P) if x * x % P == a), None)
    return SQ[a]
def roots_quad(a, b, c):
    a %= P; b %= P; c %= P
    if a == 0: return [] if b == 0 else [F(-c * pow(b, P - 2, P))]
    D = (b * b - 4 * a * c) % P; i2a = pow(2 * a, P - 2, P)
    if pow(D, (P - 1) // 2, P) in (0, 1): r = sqrtp(D); return [F((-b + r) * i2a), F((-b - r) * i2a)]
    u = sqrtp(D * pow(NR, P - 2, P)); return [((-b * i2a) % P, (u * i2a) % P), ((-b * i2a) % P, (-u * i2a) % P)]
def dot(r, w): return sum(a * b for a, b in zip(r, w)) % P
def qpoly(qa, qb):  # disc(qa + t qb) coefficients (t^2, t, 1)
    return (qb[1] * qb[1] - 4 * qb[0] * qb[2], 2 * qa[1] * qb[1] - 4 * (qa[0] * qb[2] + qb[0] * qa[2]), qa[1] * qa[1] - 4 * qa[0] * qa[2])
hits = []; gens = []; nf = 0
for l in open('w4node.out'):
    if not l.startswith('FAMILY'): continue
    pts = list(map(int, l.split()[4:])); nf += 1
    A, B = nullspace(base + [row(p) for p in pts]); k = len(gens); gens.append((A, B))
    ts = set()
    for p in range(64):
        a, b = dot(ROWS[p], A), dot(ROWS[p], B)
        if b: ts.add(F(-a * pow(b, P - 2, P)))
    for qc in FIB.values():
        qa = [dot(r, A) for r in qc]; qb = [dot(r, B) for r in qc]
        for r in roots_quad(*qpoly(qa, qb)): ts.add(r)
    ha = [dot(r, A) for r in HX]; hb = [dot(r, B) for r in HX]
    for i in (0, 2):
        if hb[i]: ts.add(F(-ha[i] * pow(hb[i], P - 2, P)))
    # fxy^2 - fxx fyy along the pencil
    c2 = hb[1] * hb[1] - hb[0] * hb[2]; c1 = 2 * ha[1] * hb[1] - ha[0] * hb[2] - hb[0] * ha[2]; c0 = ha[1] * ha[1] - ha[0] * ha[2]
    for r in roots_quad(c2, c1, c0): ts.add(r)
    cands = [([add(F(A[m]), mul(t, F(B[m]))) for m in range(9)], t) for t in ts] + [([F(B[m]) for m in range(9)], 'inf'), ([F(A[m] + 7 * B[m]) for m in range(9)], 'gen')]
    for w, t in cands:
        om, vl = omega(w)
        if om <= 4 and not vl: hits.append((k, t, om, w))
print('node families', nf, 'hits', len(hits), 'over F_p^2 only', sum(1 for h_ in hits if any(c[1] for c in h_[3])))
o = ['ring r=(10009,aa),(x,y),dp; minpoly=aa^2-11; list F; poly g; int irr=0;']
def ps(w): return '+'.join(f'({c[0]}+{c[1]}*aa)*x^{2-a}*y^{2-b}' for c, (a, b) in zip(w, MON) if c != (0, 0)) or '0'
for k, t, om, w in hits:
    A, B = gens[k]
    o.append(f'g=gcd({ps([F(v) for v in A])},{ps([F(v) for v in B])}); F=factorize({ps(w)}); if (deg(g)==0 && size(F[1])==2 && F[2][2]==1) {{ irr++; "IRRED fam {k} om {om}"; }}')
o.append('"irreducible hits", irr; quit;'); open('w4nodefam.sing', 'w').write('\n'.join(o))
