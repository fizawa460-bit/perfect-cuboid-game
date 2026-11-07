"""32R-74 R4: exact integer data for splitenum9x (exact Fincke-Pohst + exact CS pruning).
usage: python gen_exact.py d INPUTFILE OUT
Recomputes the LDL^T data from the lattice (same coordinates as split_reps.py), checks it against the float
data in INPUTFILE, and writes integer data."""
import sys, math
from fractions import Fraction as Fr
d = int(sys.argv[1]); INP = sys.argv[2]; OUT = sys.argv[3]
sys.argv = ['x', str(d)]
src = open('split_reps.py', encoding='utf-8').read()
exec(src[:src.index('Mf = ')])
n = 15
M = [[Fr(int((-A2r[i, j]).p), int((-A2r[i, j]).q)) for j in range(n)] for i in range(n)]
D = [None] * n; U = [[Fr(0)] * n for _ in range(n)]
for i in range(n):
    D[i] = M[i][i] - sum(U[k][i] ** 2 * D[k] for k in range(i)); U[i][i] = Fr(1)
    for j in range(i + 1, n): U[i][j] = (M[i][j] - sum(U[k][i] * U[k][j] * D[k] for k in range(i))) / D[i]
cen = [Fr(int(wsr[i, 0].p), int(wsr[i, 0].q)) for i in range(n)]
Rq = Fr(int(R.p), int(R.q))
# float input
tok = open(INP).read().split()
pos = 0
def nxt():
    global pos; pos += 1; return tok[pos - 1]
n_ = int(nxt()); nb = int(nxt()); Rf = float(nxt())
Df = [float(nxt()) for _ in range(n)]; Uf = [[float(nxt()) for _ in range(n)] for _ in range(n)]; cf = [float(nxt()) for _ in range(n)]
assert n_ == n
z0_ = [nxt() for _ in range(16)]; [nxt() for _ in range(n * 16)]; [nxt() for _ in range(256)]; [nxt() for _ in range(3)]
[nxt() for _ in range(48)]; [nxt() for _ in range(n * 48)]
bq0 = [int(nxt()) for _ in range(nb)]; BQ = [[int(nxt()) for _ in range(nb)] for _ in range(n)]
err = max([abs(float(D[i]) - Df[i]) for i in range(n)] + [abs(float(U[i][j]) - Uf[i][j]) for i in range(n) for j in range(n)]
          + [abs(float(cen[i]) - cf[i]) for i in range(n)] + [abs(float(Rq) - Rf) / max(1, abs(Rf))])
assert err < 1e-6, err
print('float/exact max deviation', err)
L = math.lcm(*[U[i][j].denominator for i in range(n) for j in range(n)], *[c.denominator for c in cen])
DD = math.lcm(*[x.denominator for x in D])
K = DD * L ** 4
RemTop = Rq * K; assert RemTop.denominator == 1
out = [f"{L} {DD} {int(RemTop)}", " ".join(str(int(DD * D[i])) for i in range(n))]
out += [" ".join(str(int(L * U[i][j])) for j in range(n)) for i in range(n)]
assert all((L * c).denominator == 1 for c in cen)
out.append(" ".join(str(int(L * c)) for c in cen))
mx = 0
for i in range(1, n + 1):
    for q in range(nb):
        l = [Fr(BQ[k][q]) for k in range(i)]
        u = [Fr(0)] * i
        for k in range(i): u[k] = l[k] - sum(U[j][k] * u[j] for j in range(k))
        S = sum(u[k] ** 2 / D[k] for k in range(i))
        alpha = sum(l[k] * cen[k] for k in range(i))
        gam = [sum(u[k] * U[k][j] for k in range(i)) for j in range(i, n)]
        G = math.lcm(alpha.denominator, *[g.denominator for g in gam]) if gam else alpha.denominator
        out.append(" ".join([str(G), str(int(alpha * G)), str(S.numerator), str(S.denominator)] + [str(int(g * G)) for g in gam]))
        mx = max(mx, G, S.numerator, S.denominator, *[abs(int(g * G)) for g in gam])
open(OUT, 'w', newline='\n').write("\n".join(out) + "\n")
print('L', L, 'DD', DD, 'RemTop', RemTop, 'max CS int', mx)
