"""E19 s.22.1: check of the Gauss-Bonnet identity (star) for U_r = {d(., anchors) >= r} in the hyperbolic plane.
Bounded components (holes inside a closed ring of anchors) are discs or have islands, and (star) summed over them reads
    A + coth(r) L = Psi + 2 pi (#islands - #components),     Psi = sum of corner angles.
A and L are computed exactly in polar coordinates around each anchor (Voronoi extent R_c(psi) of each ray:
    A = sum_c int (cosh R_c - cosh r)_+ dpsi,  L = sinh r * |{psi : R_c(psi) > r}|),
Psi from the corners computed exactly (intersection points of two r-circles outside all other balls), independently of A and L.
The check: n := (Psi - A - coth(r) L)/(2 pi) must be an integer (= #components - #islands; a grid count of pieces with
>= 40 pixels is printed for comparison).
Also checks the corner law phi = 2 arcsin(sinh(d/2)/sinh r) behind dphi/dr = -2 tan(phi/2) coth r.
usage: python3 -I gb22_check.py [seed]"""
import numpy as np, math, sys
from scipy import ndimage
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
rng = np.random.default_rng(seed)
R = 4.0
toE = lambda rho: math.tanh(rho / 2)
def mob(c, z): return (z + c) / (1 + np.conj(c) * z)
def mobinv(c, z): return (z - c) / (1 - np.conj(c) * z)
def hdist(z, w): return np.arccosh(1 + 2 * np.abs(z - w) ** 2 / ((1 - np.abs(z) ** 2) * (1 - np.abs(w) ** 2)))
ring = []
for rho in (R, R + 0.5):
    n = int(2 * math.pi * math.sinh(rho) / 0.4)
    ring += list(toE(rho) * np.exp(1j * (np.arange(n) * 2 * math.pi / n + rng.uniform(0, 1))))
inner = [toE(R * math.sqrt(rng.uniform(0, 1)) * 0.85) * np.exp(1j * rng.uniform(0, 2 * math.pi)) for _ in range(6)]
anch = np.array(ring + inner)
NPS = 6000
ps = np.linspace(0, 2 * math.pi, NPS, endpoint=False); dps = 2 * math.pi / NPS

def check(r):
    A = L = Psi = 0.0; law = 0.0; ncor = 0
    for ci, c in enumerate(anch):
        pts = mob(c, toE(r) * np.exp(1j * ps))
        near = anch[(hdist(c, anch) < 2 * r) & (np.arange(len(anch)) != ci)]
        pre = (hdist(pts[:, None], near[None, :]).min(1) >= r) & (np.abs(pts) < toE(R) * 0.999)
        if not pre.any(): continue
        others = np.delete(anch, ci)
        w = mobinv(c, others)                      # other anchors seen from c (c at 0)
        D = 2 * np.arctanh(np.abs(w)); th = np.angle(w)
        cosang = np.cos(ps[:, None] - th[None, :])
        num = (np.cosh(D) - 1) / np.sinh(D)
        with np.errstate(divide="ignore", invalid="ignore"):
            q = np.where(cosang > 0, num[None, :] / cosang, np.inf)
            ext = np.where(q < 1, np.arctanh(np.minimum(q, 1 - 1e-16)), np.inf)
        Rc = ext.min(1); kmin = ext.argmin(1)
        inside = np.abs(pts) < toE(R) * 0.999
        free = (Rc > r) & inside
        if not free.any(): continue
        assert np.all(np.isfinite(Rc[free])), "a hole ray escapes: ring not closed"
        A += np.sum(np.cosh(Rc[free]) - math.cosh(r)) * dps
        L += free.sum() * dps * math.sinh(r)
    # corners exactly: intersection points of two r-circles, not inside any other ball, inside the ring
    for ci, c in enumerate(anch):
        w = mobinv(c, anch); D = 2 * np.arctanh(np.minimum(np.abs(w), 1 - 1e-15))
        for k in np.where((D < 2 * r) & (np.arange(len(anch)) > ci))[0]:
            beta = math.acos(math.tanh(D[k] / 2) / math.tanh(r))
            for sgn in (1, -1):
                p = mob(c, toE(r) * np.exp(1j * (np.angle(w[k]) + sgn * beta)))
                if abs(p) >= toE(R) * 0.999: continue
                dd = hdist(p, anch); dd[ci] = dd[k] = np.inf
                if dd.min() < r: continue
                phi = abs(np.angle(mobinv(p, c) / mobinv(p, anch[k])))
                phi_law = 2 * math.asin(min(1.0, math.sinh(D[k] / 2) / math.sinh(r)))
                Psi += phi; ncor += 2; law = max(law, abs(phi - phi_law))
    # grid count of components and islands (only for the integer comparison)
    Mg = 900
    xs = np.linspace(-toE(R), toE(R), Mg); X, Y = np.meshgrid(xs, xs); Z = X + 1j * Y
    ins = np.abs(Z) < toE(R) * 0.98
    F = np.full(Z.shape, -1.0); idx = np.where(ins); zz = Z[idx]
    F[idx] = np.concatenate([hdist(zz[i:i + 4000, None], anch[None, :]).min(1) for i in range(0, len(zz), 4000)])
    lab, nc0 = ndimage.label(F >= r); labc, ncc = ndimage.label(F < r)
    sizes = ndimage.sum(np.ones_like(F), lab, range(1, nc0 + 1))
    nc = int((sizes >= 40).sum())            # the grid splits thin necks into pixel-size pieces; count real pieces only
    outer = set(np.unique(labc[~ins]))
    isl = len(set(range(1, ncc + 1)) - outer)
    n = (Psi - A - L / math.tanh(r)) / (2 * math.pi)
    print("r=%.2f corners=%d  A=%.4f L=%.4f Psi=%.4f  n=(Psi-A-coth L)/2pi=%.4f  grid: comps=%d islands=%d -> %d   corner law %.1e"
          % (r, ncor // 2, A, L, Psi, n, nc, isl, nc - isl, law))
    return n, nc - isl

print("seed", seed, " anchors", len(anch))
for r in (1.3, 1.6, 2.0, 2.4):
    check(r)
