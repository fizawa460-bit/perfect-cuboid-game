"""Half-twists of two finite branch points of B (among 1, i, -1, -i) as paths for mono.track, and their predicted
action on monodromy tuples.  Point a runs along an arc of radius 1-d, point b along radius 1+d (or the other way),
so the two pass each other once: a half-twist.  Afterwards the critical-point blocks of a and b are exchanged so
the cover is again in mono.System's labelling."""
import numpy as np
from mono import track, homB
ANG = {2: 0.0, 4: np.pi / 2, 3: np.pi, 5: 3 * np.pi / 2}       # B index -> angle on the unit circle
def path(a, b, side, m=12, d=0.15):
    """list of W (6,2) from B0 to B0 with the points labelled a,b exchanged.  side=+1: a inside; side=-1: a outside."""
    B0 = homB(); ta, tb = ANG[a], ANG[b]
    dt = (tb - ta + np.pi) % (2 * np.pi) - np.pi                  # signed short angle a -> b
    Ws = []
    for k in range(m + 1):
        s = k / m; W = B0.copy()
        bump = np.sin(np.pi * s)                                     # radial offset, 0 at both ends
        W[a, 0] = (1 - side * d * bump) * np.exp(1j * (ta + s * dt))
        W[b, 0] = (1 + side * d * bump) * np.exp(1j * (tb - s * dt))
        Ws.append(W)
    Ws[-1] = B0.copy(); Ws[-1][[a, b]] = B0[[b, a]]           # positions exchanged
    return Ws
def run(S, U, a, b, side, careful=False):
    Ws = path(a, b, side); ok = np.ones(len(U), bool)
    kw = dict(h0=0.002, hmin=1e-12, dmax=1e-2) if careful else {}
    for Wa, Wb in zip(Ws[:-1], Ws[1:]):
        U, o, _ = track(S, U, Wa, Wb, **kw); ok &= o
    # exchange critical-point blocks of a and b (prof[a] == prof[b] required)
    ys = S.ys; ia = np.nonzero(ys == a)[0]; ib = np.nonzero(ys == b)[0]
    assert len(ia) == len(ib) and ia.min() >= 3 and ib.min() >= 3
    off = 2 * S.n + 2 - 3; U = U.copy(); tmp = U[:, off + ia].copy(); U[:, off + ia] = U[:, off + ib]; U[:, off + ib] = tmp
    return U, ok
def comp(g, h):  # x -> g[h[x]]
    return tuple(g[h[x]] for x in range(len(g)))
def predict(t, a, b, form):
    t = list(t); ga, gb = t[a], t[b]
    if form == 'A': t[a], t[b] = gb, comp(gb, comp(ga, gb))
    elif form == 'B': t[a], t[b] = comp(ga, comp(gb, ga)), ga
    elif form == 'S': t[a], t[b] = gb, ga
    return tuple(t)
