# 32R-93 k = 4, bidegree (2,2): W singular at a label-matched point of BxB.  The 32 matched points form one orbit under
# the label-compatible pairs (rho -> zeta rho, zeta/rho with zeta in mu_4, and both coordinates times zeta_8), so the
# node is put at (1,1).  A node with branches transversal to both rulings gives 2 to j; j >= 8 needs >= 6 further
# matched points (if a branch is tangent to a ruling, that point gives less to j and more points are needed).
# W: rows = W(1,1) = dW/dX0 = dW/dY0 = 0 (affine chart X0 = Y0 = 1 at (1,1): W, W_x, W_y), then >= 6 matched points.
# Rank 8 -> unique curve; rank 7 with >= 6 further points -> pencil, written as FAMILY lines for pw4fam-style analysis.
import sys, itertools
P = 10009; Z = 792
xs = [pow(Z, b, P) for b in range(8)]; TY = [0 if b % 2 else 1 for b in range(8)]
MON = [(a, b) for a in range(3) for b in range(3)]           # X0^a X1^(2-a) Y0^b Y1^(2-b) ; affine x = X1/X0, y = Y1/Y0
def row(p):
    bx, by = divmod(p, 8); x, y = xs[bx], xs[by]
    return [pow(x, 2 - a, P) * pow(y, 2 - b, P) % P for a, b in MON]
def drow(p, var):
    bx, by = divmod(p, 8); x, y = xs[bx], xs[by]; r = []
    for a, b in MON:
        ex, ey = 2 - a, 2 - b
        if var == 0: r.append(ex * pow(x, ex - 1, P) * pow(y, ey, P) % P if ex else 0)
        else: r.append(ey * pow(x, ex, P) * pow(y, ey - 1, P) % P if ey else 0)
    return r
def rank(rows):
    M = [r[:] for r in rows]; rk = 0
    for c in range(9):
        k = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if k is None: continue
        M[rk], M[k] = M[k], M[rk]; f = pow(M[rk][c], P - 2, P); M[rk] = [v * f % P for v in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]: g = M[i][c]; M[i] = [(a - g * b) % P for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk
N0 = 0 * 8 + 0                                        # (1,1)
MT = [p for p in range(64) if TY[p // 8] == TY[p % 8] and p != N0]
base = [row(N0), drow(N0, 0), drow(N0, 1)]
assert rank(base) == 3
out = open('w4node.out', 'w'); seen = set(); nc = nf = 0
def common(rows):
    return tuple(p for p in MT if rank(rows + [row(p)]) == rank(rows))
def dfs(rows, start, chosen):
    global nc, nf
    rk = rank(rows)
    if rk == 8:
        cm = common(rows)
        if len(cm) >= 6 and cm not in seen: seen.add(cm); nc += 1; out.write('CURVEPTS ' + ' '.join(map(str, cm)) + '\n')
        return
    if rk == 7:
        cm = common(rows)
        if len(cm) >= 6 and cm not in seen: seen.add(cm); nf += 1; out.write('FAMILY npts %d pts ' % len(cm) + ' '.join(map(str, cm)) + '\n')
    for k in range(start, len(MT)):
        r2 = rows + [row(MT[k])]
        if rank(r2) > rk: dfs(r2, k + 1, chosen + [MT[k]])
dfs(base, 0, [])
print('node at (1,1): curves', nc, 'families', nf)
