"""32R-69 fast exact h0 (char p = 10009) of |m K - D| from precomputed degree-m parts of the component ideals
(fasth0/spaces.txt, made by precompute.sing): (I(D))_m = ∩ (I_comp)_m, so
  dim (I(D))_m = N_m - rank(stacked annihilators),  h0 = dim (I(D))_m - dim S_m   (identical to the Singular sweep)."""
import re, numpy as np
P = 10009
NM = {1: 7, 2: 28, 3: 84}
def _rref_null(B):
    """basis of {a : B a = 0} over F_p (B: r x N int)"""
    B = B.copy() % P; r, N = B.shape; piv = []; row = 0
    for col in range(N):
        if row >= r: break
        nz = np.nonzero(B[row:, col])[0]
        if len(nz) == 0: continue
        k = row + nz[0]; B[[row, k]] = B[[k, row]]
        B[row] = B[row] * pow(int(B[row, col]), P - 2, P) % P
        others = np.nonzero(B[:, col])[0]; others = others[others != row]
        if len(others): B[others] = (B[others] - np.outer(B[others, col], B[row])) % P
        piv.append(col); row += 1
    free = [c for c in range(N) if c not in piv]
    A = np.zeros((len(free), N), dtype=np.int64)
    for t, f in enumerate(free):
        A[t, f] = 1
        for i, pc in enumerate(piv): A[t, pc] = (-B[i, f]) % P
    return A
def rank_mod(M):
    M = M.copy() % P; r, N = M.shape; row = 0
    for col in range(N):
        if row >= r: break
        nz = np.nonzero(M[row:, col])[0]
        if len(nz) == 0: continue
        k = row + nz[0]; M[[row, k]] = M[[k, row]]
        M[row] = M[row] * pow(int(M[row, col]), P - 2, P) % P
        below = row + 1 + np.nonzero(M[row + 1:, col])[0]
        if len(below): M[below] = (M[below] - np.outer(M[below, col], M[row])) % P
        row += 1
    return row
ANN, DIMS = {}, {}
for line in open(__file__.replace("fasth0v2.py", "spaces_v2.txt")):
    t = line.split(); name, m, nc, nr = t[0], int(t[1]), int(t[2]), int(t[3])
    if nc == 0:
        ANN[(name, m)] = np.eye(NM[m], dtype=np.int64); DIMS[(name, m)] = 0; continue   # 32R-69f: (I)_m = 0 (was: no constraint)
    vals = np.array([int(v) for v in t[4:]], dtype=np.int64).reshape(nc, nr)   # rows = generators, cols = monomials
    assert nr == NM[m]
    ANN[(name, m)] = _rref_null(vals); DIMS[(name, m)] = NM[m] - ANN[(name, m)].shape[0]
def h0(m, comps):
    """comps: list of component names like 'C17_1', 'N95_2'"""
    if not comps: return NM[m] - DIMS[("S", m)]
    M = np.concatenate([ANN[(c, m)] for c in comps])
    return NM[m] - rank_mod(M) - DIMS[("S", m)]
def comps_from_sing(path):
    s = open(path).read()
    m = int(re.search(r"int mm = (\d+);", s).group(1))
    parts = re.search(r"ideal Iall = (?:intersect\()?([^;)]*)\)?; Iall", s).group(1).split(",")
    out = []
    for p_ in parts:
        p_ = p_.strip()
        if p_.startswith("G"):
            k = int(re.match(r"G(\d+)", p_).group(1))
            if p_.endswith("p"):
                c = int(re.search(rf"sat\(std\(S \+ G{k}\^(\d+)\)", s).group(1))
            else: c = 1
            out.append(f"C{k}_{c}")
        else:
            k = int(p_[1:]); c = int(re.search(rf"ideal N{k} = std\(S \+ ideal\([^;]*\)\^(\d+)\);", s).group(1))
            out.append(f"N{k}_{c}")
    return m, out

# 32R-69c: v2 spaces (correct saturations; curve multiplicities 1..4, node powers 1..3)
_SB = {}
def _sbasis(m):
    if m not in _SB:
        A = ANN[("S", m)]; _SB[m] = _rref_null(A) if A.shape[0] else np.eye(NM[m], dtype=np.int64)   # basis of S_m
    return _SB[m]
def member_form(m, comps):
    """a form F in (I(D))_m not in S_m (for h0 >= 1), or None"""
    M = np.concatenate([ANN[(c, m)] for c in comps]) if comps else np.zeros((0, NM[m]), dtype=np.int64)
    Kb = _rref_null(M) if M.shape[0] else np.eye(NM[m], dtype=np.int64)
    Sb = _sbasis(m); rs = rank_mod(Sb) if Sb.shape[0] else 0
    for v in Kb:
        if rank_mod(np.vstack([Sb, v[None, :]])) > rs: return v
    return None
def contained_curves(m, comps):
    """known curves Γ (1..92) contained in the member: F in V(Γ, c_Γ + 1)"""
    F = member_form(m, comps)
    if F is None: return None
    mult = {}
    for c in comps:
        if c.startswith("C"): k, cc = c[1:].split("_"); mult[int(k)] = int(cc)
    out = []
    for k in range(1, 93):
        c1 = mult.get(k, 0) + 1
        if c1 > 4: continue
        if not (ANN[(f"C{k}_{c1}", m)].dot(F) % P).any(): out.append(k)
    return out
