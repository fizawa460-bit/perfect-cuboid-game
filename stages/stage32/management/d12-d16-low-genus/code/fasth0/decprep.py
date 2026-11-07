"""32R-70: choose 64 of the 140 generators forming a Z-basis of Pic (B unimodular), so that
c_P = v.Binv - c_F.A  (A = Cm[F].Binv).  Writes decomp_tab.txt for decomp.c."""
import sys, os, numpy as np, flint
sys.argv = ["x"]
import judge_fast as J; J.init()
Cm = J.Cm.astype(np.int64); n, r = Cm.shape
rng = np.random.default_rng(0); best = None
order0 = sorted(range(n), key=lambda i: np.count_nonzero(Cm[i]))
for trial in range(200):
    order = order0 if trial == 0 else list(rng.permutation(n))
    P = []
    for i in order:
        if np.linalg.matrix_rank(Cm[P + [i]].astype(float)) > len(P): P.append(i)
        if len(P) == r: break
    d = flint.fmpz_mat([[int(v) for v in Cm[i]] for i in P]).det()
    if abs(int(d)) == 1:
        F = [i for i in range(n) if i not in P]
        B = flint.fmpz_mat([[int(v) for v in Cm[i]] for i in P]); Bi = B.inv()
        Binv = np.array([[int(Bi[i, j]) for j in range(r)] for i in range(r)], dtype=np.int64)
        A = Cm[F].dot(Binv); score = np.abs(A).sum()
        if best is None or score < best[0]: best = (score, P, F, Binv, A); print(trial, "score", score, "maxabs", np.abs(A).max(), "nnz", np.count_nonzero(A))
score, P, F, Binv, A = best
assert (np.eye(r, dtype=np.int64) == Cm[P].dot(Binv)).all()
with open("decomp_tab.txt", "w") as f:
    f.write(f"{n} {r}\n" + " ".join(map(str, P)) + "\n" + " ".join(map(str, F)) + "\n")
    for row in Binv: f.write(" ".join(map(str, row)) + "\n")
    for row in A: f.write(" ".join(map(str, row)) + "\n")
