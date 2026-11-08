# Are the 8 k=4 (2,2) hits pullbacks (x, y) -> (x^2, y^2) of the k=8 Moebius graphs of E06?  t = rho^2 maps
# B_k4 = mu_8 onto {+-1, +-i} and rho = 0, inf onto t = 0, inf (labels: B_u -> {+-i} = a, B_v -> {+-1} = b).
import itertools
P = 10009; I = 6706; assert I * I % P == P - 1
B8 = [None, 0, 1, P - 1, I, P - I]; TY8 = [0, 0, 1, 1, 2, 2]          # inf, 0 (e), 1, -1 (b), i, -i (a)
def mob(m, t):
    a, b, c, d = m
    if t is None: return None if c == 0 else a * pow(c, P - 2, P) % P
    num, den = (a * t + b) % P, (c * t + d) % P
    return None if den == 0 else num * pow(den, P - 2, P) % P
# all Moebius maps sending 3 distinct points of B8 to 3 points of B8 (as E06), dedupe, and |Delta|
def through(p, q):  # Moebius sending p[0..2] -> q[0..2]; use cross-ratio construction via linear solve
    rows = []
    for s, t in zip(p, q):
        # (a s + b) - t (c s + d) = 0 ; infinity handled
        if s is None and t is None: rows.append([0, 0, 1, 0, 'cz'])  # c*? : a/c = inf -> c = 0
        elif s is None: rows.append([1, 0, -t % P, 0])
        elif t is None: rows.append([0, 0, s, 1])
        else: rows.append([s, 1, (-t * s) % P, (-t) % P])
    rows = [r[:4] if r[-1] != 'cz' else [0, 0, 1, 0] for r in rows]
    M = [r[:] for r in rows]; piv = []; rk = 0
    for c in range(4):
        k = next((i for i in range(rk, 3) if M[i][c] % P), None)
        if k is None: continue
        M[rk], M[k] = M[k], M[rk]; f = pow(M[rk][c], P - 2, P); M[rk] = [v * f % P for v in M[rk]]
        for i in range(3):
            if i != rk and M[i][c] % P: g = M[i][c]; M[i] = [(x - g * y) % P for x, y in zip(M[i], M[rk])]
        piv.append(c); rk += 1
    if rk != 3: return None
    fr = [c for c in range(4) if c not in piv][0]; v = [0] * 4; v[fr] = 1
    for i, c in enumerate(piv): v[c] = (-M[i][fr]) % P
    if (v[0] * v[3] - v[1] * v[2]) % P == 0: return None
    f = pow(next(x for x in v if x), P - 2, P); return tuple(x * f % P for x in v)
maps = set()
for p in itertools.permutations(range(6), 3):
    if p != tuple(sorted(p)): continue
    for q in itertools.permutations(range(6), 3):
        m = through([B8[i] for i in p], [B8[i] for i in q])
        if m: maps.add(m)
def delta(m):
    img = {}
    for k in range(6):
        t = mob(m, B8[k]); img[k] = next((i for i in range(6) if B8[i] == t), -1)
    D = 0
    for chi in range(3):
        A = {k for k in range(6) if TY8[k] == chi}; Bm = {k for k in range(6) if img[k] >= 0 and TY8[img[k]] == chi}
        D |= 0
    # |Delta| = sum over chi |B_chi symmetric-difference T^{-1} B_chi|, union over chi
    S = set()
    for chi in range(3):
        A = {B8[k] for k in range(6) if TY8[k] == chi}
        pre = {B8[k] for k in range(6) if img[k] >= 0 and TY8[img[k]] == chi}
        # T^{-1}B_chi may contain non-B points
        Tinv = set()
        for k in range(6):
            if TY8[k] == chi:
                # preimage of B8[k] under m: solve
                a, b, c, d = m; inv = (d, (-b) % P, (-c) % P, a); Tinv.add(mob(inv, B8[k]))
        S |= A ^ Tinv
    return len(S)
good = sorted(m for m in maps if delta(m) <= 4)
print('Moebius maps through 3 points', len(maps), ' |Delta|<=4:', len(good), [delta(m) for m in good].count(0), 'with Delta empty')
for m in good:
    a, b, c, d = m   # graph Y (cX + d) - (aX + b) = 0, X = x^2, Y = y^2  -> c x^2 y^2 + d y^2 - a x^2 - b
    print('T', m, 'Delta', delta(m), ' W: %d x2y2 + %d y2 + %d x2 + %d' % (c, d, (-a) % P, (-b) % P))
