# evaluate w4node.out CURVEPTS lines: W through the node rows at (1,1) and the listed points, |Omega| with the node
# correction (node fibres x = 1, y = 1 count 2 each if the node has branches transversal to both rulings, and the node
# gives 2 to j), keep |Omega| <= 4, write a Singular file (factorize over F_p^2 = F_p(sqrt 11)).
exec(open('w4node.py').read().split("N0 = 0 * 8")[0])
N0 = 0; base = [row(N0), drow(N0, 0), drow(N0, 1)]
def kernel(rows):
    M = [r[:] for r in rows]; piv = []; rk = 0
    for c in range(9):
        k = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if k is None: continue
        M[rk], M[k] = M[k], M[rk]; f = pow(M[rk][c], P - 2, P); M[rk] = [v * f % P for v in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]: g = M[i][c]; M[i] = [(a - g * b) % P for a, b in zip(M[i], M[rk])]
        piv.append(c); rk += 1
    fr = [c for c in range(9) if c not in piv]; assert len(fr) == 1
    v = [0] * 9; v[fr[0]] = 1
    for i, c in enumerate(piv): v[c] = (-M[i][fr[0]]) % P
    return v
def ev(w, p): return sum(a * b for a, b in zip(w, row(p))) % P
def fib(w, b, axis):   # binary quadratic coefficients
    x = xs[b]; q = [0, 0, 0]
    for c, (a, bb) in enumerate(MON):
        ex, ey = 2 - a, 2 - bb
        if axis == 0: q[ey] = (q[ey] + w[c] * pow(x, ex, P)) % P
        else: q[ex] = (q[ex] + w[c] * pow(x, ey, P)) % P
    return q
def disc(q): return (q[1] * q[1] - 4 * q[0] * q[2]) % P
def hess(w):  # second derivatives at (1,1) in the affine chart
    x = y = 1; fxx = fxy = fyy = 0
    for c, (a, b) in enumerate(MON):
        ex, ey = 2 - a, 2 - b
        fxx += w[c] * ex * (ex - 1); fyy += w[c] * ey * (ey - 1); fxy += w[c] * ex * ey
    return fxx % P, fxy % P, fyy % P
hits = []; n = 0
for l in open('w4node.out'):
    if not l.startswith('CURVEPTS'): continue
    pts = list(map(int, l.split()[1:])); n += 1
    w = kernel(base + [row(p) for p in pts])
    fxx, fxy, fyy = hess(w)
    trans = fxx != 0 and fyy != 0 and (fxy * fxy - fxx * fyy) % P != 0
    O1 = O2 = j = h = 0; vl = 0
    for b in range(8):
        for axis in (0, 1):
            q = fib(w, b, axis)
            if not any(q): vl = 1; continue
            if disc(q) or (b == 0 and trans): 
                if axis == 0: O1 += 2
                else: O2 += 2
    if trans: j += 2
    for p in range(64):
        if p == N0 or ev(w, p): continue
        bx, by = divmod(p, 8)
        qx, qy = fib(w, bx, 0), fib(w, by, 1)
        if any(qx) and any(qy) and disc(qx) and disc(qy):
            if TY[bx] == TY[by]: j += 1
            else: h += 1
    om = O1 + O2 - 2 * j - h
    if om <= 4 and not vl: hits.append((om, trans, w))
print('curves', n, 'hits |Omega|<=4', len(hits), 'transversal node', sum(1 for h_ in hits if h_[1]))
o = ['ring r=(10009,aa),(x,y),dp; minpoly=aa^2-11; list F;']
for k, (om, tr, w) in enumerate(hits):
    pol = '+'.join(f'{w[c]}*x^{2-a}*y^{2-b}' for c, (a, b) in enumerate(MON) if w[c])
    o.append(f'F=factorize({pol}); "H{k} om {om} trans {int(tr)} factors", size(F[1])-1;')
o.append('quit;'); open('w4node_eval.sing', 'w').write('\n'.join(o))
