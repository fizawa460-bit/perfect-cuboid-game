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
def run(S, U, a, b, side, careful=False, d=0.15):
    Ws = path(a, b, side, d=d); ok = np.ones(len(U), bool)
    kw = dict(h0=0.002, hmin=1e-12, dmax=1e-2) if careful else {}
    for Wa, Wb in zip(Ws[:-1], Ws[1:]):
        U, o, _ = track(S, U, Wa, Wb, **kw); ok &= o
    return relabel(S, U, a, b), ok
def relabel(S, U, a, b):
    """exchange the critical-point blocks of a and b (prof[a] == prof[b] required)"""
    # exchange critical-point blocks of a and b (prof[a] == prof[b] required)
    ys = S.ys; ia = np.nonzero(ys == a)[0]; ib = np.nonzero(ys == b)[0]
    assert len(ia) == len(ib) and ia.min() >= 3 and ib.min() >= 3
    off = 2 * S.n + 2 - 3; U = np.array(U).copy(); tmp = U[:, off + ia].copy(); U[:, off + ia] = U[:, off + ib]; U[:, off + ib] = tmp
    return U
    return U, ok
def comp(g, h):  # x -> g[h[x]]
    return tuple(g[h[x]] for x in range(len(g)))
def predict(t, a, b, form):
    t = list(t); ga, gb = t[a], t[b]
    if form == 'A': t[a], t[b] = gb, comp(gb, comp(ga, gb))
    elif form == 'B': t[a], t[b] = comp(ga, comp(gb, ga)), ga
    elif form == 'S': t[a], t[b] = gb, ga
    return tuple(t)

def path_full(a, b, side, m=12, d=0.15):
    """full twist (pure braid): the half-twist path(a, b, side) followed by the same geometric half-twist again,
    so both points end where they started (no relabelling; works for any profile).  The point at a's position
    always runs on the inner arc for side=+1, so the positional formula is the half-twist formula applied twice."""
    B0 = homB(); ta, tb = ANG[a], ANG[b]
    dt = (tb - ta + np.pi) % (2 * np.pi) - np.pi
    Ws = path(a, b, side, m, d)
    for k in range(1, m + 1):
        s = k / m; W = B0.copy(); bump = np.sin(np.pi * s)
        W[a, 0] = (1 + side * d * bump) * np.exp(1j * (tb - s * dt))
        W[b, 0] = (1 - side * d * bump) * np.exp(1j * (ta + s * dt))
        Ws.append(W)
    Ws[-1] = B0.copy()
    return Ws
def run_full(S, U, a, b, side, careful=False, d=0.15):
    Ws = path_full(a, b, side, d=d); ok = np.ones(len(U), bool)
    kw = dict(h0=0.002, hmin=1e-12, dmax=1e-2) if careful else {}
    for Wa, Wb in zip(Ws[:-1], Ws[1:]):
        U, o, _ = track(S, U, Wa, Wb, **kw); ok &= o
    return U, ok

FINV = {0: 0j, 2: 1 + 0j, 3: -1 + 0j, 4: 1j, 5: -1j}
def path_loop(a, b, r=0.3, m=10, sense=+1):
    """pure braid: point a goes straight towards b, runs once around b on a circle of radius r (sense +1 =
    counter-clockwise), and comes back the same way."""
    B0 = homB(); va, vb = FINV[a], FINV[b]; e = vb + r * (va - vb) / abs(va - vb)
    pts = [va + (e - va) * k / m for k in range(m + 1)]
    ang0 = np.angle(e - vb); pts += [vb + r * np.exp(1j * (ang0 + sense * 2 * np.pi * k / (2 * m))) for k in range(1, 2 * m + 1)]
    pts += [e + (va - e) * k / m for k in range(1, m + 1)]
    Ws = []
    for z in pts:
        W = B0.copy(); W[a, 0] = z; Ws.append(W)
    Ws[-1] = B0.copy(); return Ws
def run_path(S, U, Ws, careful=False):
    ok = np.ones(len(U), bool); kw = dict(h0=0.002, hmin=1e-12, dmax=1e-2) if careful else {}
    for Wa, Wb in zip(Ws[:-1], Ws[1:]):
        U, o, _ = track(S, U, Wa, Wb, **kw); ok &= o
    return U, ok
