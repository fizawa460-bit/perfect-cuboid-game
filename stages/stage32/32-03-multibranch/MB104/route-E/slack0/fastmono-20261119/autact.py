"""Action of Stab(prof) in Aut(B) x <conj> on monodromy tuples, learned once from numerically computed images.

For a symmetry s with branch-point permutation pi, the image cover sX has tuple
    t'[pi(y)] = h . (e_y t[y] e_y^-1) . h^-1      (e_y = product of letters w_y of the old tuple, h global)
learn() finds the shortest words w_y on sample covers (w for y=0 is () since h absorbs one conjugation), and
apply() then gives the image class of any cover without numerical root following.  Used to name images
whose numerical monodromy fails (covers with almost-coincident critical points)."""
import itertools, numpy as np
from common import AUT
import monodromy as md

def sym_list(prof):
    """the same order as closure.images: (conj, M, total permutation y -> pi(y))"""
    out = []
    for conj in (0, 1):
        cperm = (0, 1, 2, 3, 5, 4) if conj else (0, 1, 2, 3, 4, 5)
        for M, perm in AUT:
            t2 = [0] * 6
            for y in range(6): t2[perm[cperm[y]]] = prof[y]
            if tuple(t2) != tuple(prof): continue
            out.append((conj, M, tuple(perm[cperm[y]] for y in range(6))))
    return out

def image_cover(x, an, n, conj, M, pi):
    """same transformation as closure.images, for one symmetry"""
    p, q = x[:n + 1], x[n + 1:]
    cj = lambda z: None if z is None else complex(z).conjugate()
    pp, qq = (p.conj(), q.conj()) if conj else (p, q)
    anc = {y: ([cj(z) for z in an[y][0]], [cj(z) for z in an[y][1]]) if conj else an[y] for y in range(6)}
    p2 = M[0, 0] * pp + M[0, 1] * qq; q2 = M[1, 0] * pp + M[1, 1] * qq
    return np.concatenate([p2, q2]), {pi[y]: anc[y] for y in range(6)}

def _words(L):
    out = [()]
    for l in range(1, L + 1):
        for w in itertools.product(range(6), repeat=l):
            if all(w[i] != w[i + 1] for i in range(l - 1)): out.append(w)
    return out

def comp(g, h): return tuple(g[h[x]] for x in range(len(g)))
def ev(t, w):
    g = tuple(range(len(t[0])))
    for i in w: g = comp(g, t[i])
    return g
def conj(t, w, x):
    e = ev(t, w); ei = [0] * len(e)
    for i, v in enumerate(e): ei[v] = i
    return comp(e, comp(x, tuple(ei)))

def apply(t, rule):
    pi, words = rule; s = [None] * 6
    for y in range(6): s[pi[y]] = conj(t, words[y], t[y])
    return tuple(s)

def learn(T, T2, pi, n, L=4):
    """T, T2: lists of tuples (covers and their images). returns words per y, or None"""
    H = np.array(list(itertools.permutations(range(n)))); Hinv = np.argsort(H, 1)
    def conj_all(g, idx):  # h g h^-1 for h in H[idx]
        return np.take_along_axis(H[idx], np.asarray(g)[Hinv[idx]], 1)
    cand = [np.nonzero((conj_all(t[0], np.arange(len(H))) == np.asarray(t2[pi[0]])).all(1))[0] for t, t2 in zip(T, T2)]
    words = {0: ()}
    for y in range(1, 6):
        found = None
        for w in _words(L):
            newc = []
            for t, t2, c in zip(T, T2, cand):
                g = conj(t, w, t[y]); m = (conj_all(g, c) == np.asarray(t2[pi[y]])).all(1)
                if not m.any(): break
                newc.append(c[m])
            else:
                found = w; cand = newc; break
        if found is None: return None
        words[y] = found
    return [words[y] for y in range(6)]
