"""32R-70 lattice decomposition search: find c in {0..3}^140 with c.Cm = v without MILP.
c = c0 + t.Kb (Kb: LLL-reduced integer kernel basis of Cm), start near the LP point, then local search
with short kernel moves to remove box violations. Falls back to MILP when it fails (caller)."""
import numpy as np, flint, os, pickle
HERE = os.path.dirname(os.path.abspath(__file__))
def setup(Cm):
    path = os.path.join(HERE, "latdec_cache.pkl")
    if os.path.exists(path):
        D = pickle.load(open(path, "rb"))
        if np.array_equal(D["Cm"], Cm): return D
    n, r = Cm.shape
    M = flint.fmpz_mat([[int(v) for v in Cm[i]] + [1 if j == i else 0 for j in range(n)] for i in range(n)])
    H = M.hnf()
    H = np.array([[int(H[i, j]) for j in range(r + n)] for i in range(n)], dtype=object)
    rows = [i for i in range(n) if any(H[i, :r])]
    ker = [i for i in range(n) if not any(H[i, :r])]
    H64 = H[rows, :r]; U64 = H[rows, r:]; K = H[ker, r:]
    assert (np.array(H64, dtype=np.int64) == np.array(U64, dtype=np.int64).dot(Cm)).all()
    Kl = flint.fmpz_mat([[int(v) for v in row] for row in K]).lll()
    Kb = np.array([[int(Kl[i, j]) for j in range(n)] for i in range(Kl.nrows())], dtype=np.int64)
    assert not Kb.dot(Cm).any()
    # move set: basis rows and short combinations
    mv = [k for k in Kb]
    for i in range(len(Kb)):
        for j in range(i + 1, len(Kb)):
            for s in (1, -1):
                w = Kb[i] + s * Kb[j]
                if np.abs(w).sum() <= 6: mv.append(w)
    mv = np.array(mv, dtype=np.int64); mv = np.vstack([mv, -mv])
    D = {"Cm": Cm, "H64": np.array(H64, dtype=np.int64), "U64": np.array(U64, dtype=np.int64), "Kb": Kb,
         "Kpinv": np.linalg.pinv(Kb.astype(float)), "MV": mv, "piv": [next(j for j in range(r) if H64[i, j]) for i in range(len(rows))]}
    pickle.dump(D, open(path, "wb")); return D
def particular(D, v):
    """integer y with y.H64 = v (H64 row echelon), c0 = y.U64; None if v not in the lattice"""
    H = D["H64"]; y = np.zeros(H.shape[0], dtype=np.int64); res = v.astype(np.int64).copy()
    for i, p in enumerate(D["piv"]):
        if res[p] % H[i, p]: return None
        y[i] = res[p] // H[i, p]; res = res - y[i] * H[i]
    if res.any(): return None
    return y.dot(D["U64"])
def viol(c): return np.maximum(-c, 0).sum(-1) + np.maximum(c - 3, 0).sum(-1)
def search(D, v, start, rng, iters=400):
    c0 = particular(D, v)
    if c0 is None: return None
    t = np.round((start - c0).dot(D["Kpinv"])).astype(np.int64)
    c = c0 + t.dot(D["Kb"]); MV = D["MV"]; best = viol(c)
    for it in range(iters):
        if best == 0: return c
        cand = viol(c[None, :] + MV); k = int(cand.argmin())
        if cand[k] < best: c = c + MV[k]; best = cand[k]
        else:   # plateau: random move among the non-worsening ones, else random kick
            ok = np.nonzero(cand <= best)[0]
            k = int(rng.choice(ok)) if len(ok) else int(rng.integers(len(MV)))
            c = c + MV[k]; best = viol(c)
    return c if best == 0 else None
