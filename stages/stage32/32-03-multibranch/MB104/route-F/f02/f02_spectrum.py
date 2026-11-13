"""Route F, trial F-02: slack-0 mismatch spectrum including degree 4 (floating-point measurement, not a theorem).

Same quantities as F-01 (route-F/f01): |Omega| = |O1| + |O2| - 2j - h for p1 (degree a) and p2 = q o T (degree b).
Difference: only Moebius maps T with c >= 4 coincidences are enumerated, found by matching cross-ratios.
- For each q, the cross-ratios of all ordered quadruples of O_q go into a KD-tree (chordal embedding).
- Each unordered source quadruple of O1, in a fixed order, is looked up there.
- Every T with c >= 4 coincidences is found (from each of its C(c,4) coincident quadruples) and deduplicated by
  a numeric key.
Pairs with c <= 3 have |Omega| >= |O1| + |O2| - 6. This is reported as the bound for the part not enumerated.

Birationality: the degree of (p1, p2) onto its image is the number of points in a generic fibre of p1 with the same
p2-value. It is computed at two generic points. (This also catches a common factor of p1 and p2; E11's test
"p2 constant on fibres of p1" covers only the case p2 = r o p1.)

Cross-check mode: bidegrees (1,2), (2,2), (2,3), (3,3) must reproduce the F-01 values of omega_min and the
birational low counts.

usage: python -I -O f02_spectrum.py 2x4 3x4 4x4   (degree-4 maps from maps4.json; process pool, resumable via spec{a}x{b}.jsonl)
"""
import itertools, json, sys, time, os
from collections import Counter
from math import comb
import numpy as np
from scipy.spatial import cKDTree
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "f01"))
import f01_mismatch_spectrum as F1   # map construction for degrees 1-3, map_data, peval, roots_hom, nrm

mp.mp.dps = 50


def maps_deg4():
    data = json.load(open(os.path.join(HERE, "maps4.json")))
    sys.path.insert(0, HERE)
    import build_maps as BM
    return [([BM.parse_c(c) for c in d["P"]], [BM.parse_c(c) for c in d["Q"]]) for d in data]


def maps_of_degree(n):
    return maps_deg4() if n == 4 else F1.maps_of_degree(n)


def cr(p):
    """cross-ratio of 4 homogeneous points (rows of p, shape (...,4,2)), as a chordal point in R^3"""
    def d(i, j): return p[..., i, 0] * p[..., j, 1] - p[..., i, 1] * p[..., j, 0]
    num = d(0, 2) * d(1, 3); den = d(0, 3) * d(1, 2)
    # chordal embedding of num/den without dividing: (2 Re(n conj d), 2 Im(n conj d), |n|^2 - |d|^2) / (|n|^2 + |d|^2)
    w = num * np.conj(den); s = np.abs(num)**2 + np.abs(den)**2
    return np.stack([2 * w.real / s, 2 * w.imag / s, (np.abs(num)**2 - np.abs(den)**2) / s], axis=-1)


def frame(p0, p1, p2):
    M = np.stack([p0, p1], axis=-1)
    co = np.linalg.solve(M, p2[..., None])[..., 0]
    return M * co[..., None, :]


def bir_degree(a, Pa, Qa, Pb, Qb, T):
    """number of points in a generic fibre of p1 with the same value of q o T as the base point"""
    if a == 1: return 1
    degs = []
    for z0 in (np.array([0.4127 + 0.2291j, 1]), np.array([-1.37 + 0.61j, 1])):
        z0 = F1.nrm(z0)
        y0 = F1.peval(Pa, Qa, z0)
        fib = F1.roots_hom([y0[1] * Pa[m] - y0[0] * Qa[m] for m in range(a + 1)])
        w0 = F1.peval(Pb, Qb, F1.nrm(T @ z0))
        imgs = [F1.peval(Pb, Qb, F1.nrm(T @ v)) for v in fib]
        degs.append(sum(1 for w in imgs if abs(w0[0] * w[1] - w0[1] * w[0]) < 1e-8))
    return max(degs)


def tkey(T):
    def aff(v):
        v = T @ v
        return "inf" if abs(v[1]) < 1e-9 * abs(v[0]) else (round((v[0] / v[1]).real, 6), round((v[0] / v[1]).imag, 6))
    return (aff(np.array([0, 1])), aff(np.array([1, 1])), aff(np.array([1, 0])))


TOL = 1e-8; RAD = 1e-7
AMB = (1e-12, 1e-6)      # cross values in this band are recorded as borderline
SPECV = "v2"             # resume-file version (v2 adds the borderline list "amb")


from math import gcd
CUT = {(1, 2): 10, (2, 2): 12, (2, 3): 14, (3, 3): 16, (2, 4): 16, (3, 4): 18, (4, 4): 13}   # (4,4) lowered 18 -> 13 on 2026-11-13 after omega=12 was found (resume-compatible, see spectrum)


_W = {}


def _init(a, b):
    """per-worker data: the maps and O-sets of both degrees (trees are built per chunk)"""
    A_maps, B_maps = maps_of_degree(a), maps_of_degree(b)
    _W.update(a=a, b=b, A_maps=A_maps, B_maps=B_maps,
              A_dat=[F1.map_data(P, Q) for P, Q in A_maps], B_dat=[F1.map_data(P, Q) for P, Q in B_maps])


def _chunk(ibs):
    """all p1 against the q maps with indices ibs; returns partial histogram data"""
    a, b = _W["a"], _W["b"]; cut = CUT[(a, b)]
    A_maps, B_maps, A_dat, B_dat = _W["A_maps"], _W["B_maps"], _W["A_dat"], _W["B_dat"]
    nA, nB = 2 * a + 4, 2 * b + 4
    assert all(len(d) == nA for d in A_dat) and all(len(B_dat[ib]) == nB for ib in ibs), "O-set sizes"
    tq = np.array(list(itertools.permutations(range(nB), 4)))
    sq = np.array(list(itertools.combinations(range(nA), 4)))
    trees = {}
    for ib in ibs:
        Oq = B_dat[ib]; Xq = np.array([p for p, _ in Oq])
        trees[ib] = (Xq, np.array([l for _, l in Oq]), cKDTree(cr(Xq[tq])))
    untested = Counter(); low = []; GAP = [0.0, 1.0]; cand = 0; amb = []
    for ia, O1 in enumerate(A_dat):
        X1 = np.array([p for p, _ in O1]); L1 = np.array([l for _, l in O1])
        S = cr(X1[sq])
        for ib in ibs:
            Xq, Lq, tree = trees[ib]
            hits = tree.query_ball_point(S, RAD)
            seen = {}
            for si, lst in enumerate(hits):
                for ti in lst:
                    s = sq[si]; t = tq[ti]
                    T = frame(Xq[t[0]], Xq[t[1]], Xq[t[2]]) @ np.linalg.inv(frame(X1[s[0]], X1[s[1]], X1[s[2]]))
                    T = T / np.linalg.norm(T)
                    k = tkey(T)
                    if k in seen: continue
                    cand += 1
                    O2 = (np.linalg.inv(T) @ Xq.T).T; O2 = O2 / np.linalg.norm(O2, axis=1, keepdims=True)
                    cross = np.abs(X1[:, None, 0] * O2[None, :, 1] - X1[:, None, 1] * O2[None, :, 0])
                    co = cross < TOL
                    if co.any(): GAP[0] = max(GAP[0], float(cross[co].max()))
                    if (~co).any(): GAP[1] = min(GAP[1], float(cross[~co].min()))
                    same = L1[:, None] == Lq[None, :]
                    j = int((co & same).sum()); h = int((co & ~same).sum())
                    seen[k] = (nA + nB - 2 * j - h, j, h, T)
                    if ((cross > AMB[0]) & (cross < AMB[1])).any():     # borderline: rechecked in high precision (recheck_amb.py)
                        amb.append((ia, ib, [int(x) for x in s], [int(x) for x in t], nA + nB - 2 * j - h, j, h))
            for k, (om, j, h, T) in seen.items():
                if j + h < 4: continue      # a cross-ratio match must come from >= 4 coincidences
                if gcd(a, b) == 1: bd = 1
                elif om <= cut: bd = bir_degree(a, *A_maps[ia], *B_maps[ib], T)
                else: untested[om] += 1; continue
                low.append((om, j, h, bd))
    return dict(ibs=list(ibs), untested=dict(untested), low=low, gap=GAP, cand=cand, amb=amb)


def spectrum(a, b, workers=None, chunk=None):
    """same result as the serial version; the q maps are split into chunks run on a process pool.
    Each finished chunk is appended to spec{a}x{b}.jsonl, so an interrupted run resumes."""
    from multiprocessing import Pool
    cut = CUT[(a, b)]
    t0 = time.time()
    _init(a, b)
    nA, nB = 2 * a + 4, 2 * b + 4
    nMa, nMb = len(_W["A_maps"]), len(_W["B_maps"])
    workers = workers or max(1, (os.cpu_count() or 2) - 1)
    chunk = chunk or max(1, nMb // (30 * workers))     # small chunks: an interruption loses at most one chunk per worker
    chunks = [tuple(range(i, min(i + chunk, nMb))) for i in range(0, nMb, chunk)]
    path = os.path.join(HERE, f"spec{a}x{b}{SPECV}.jsonl")
    done = []
    if os.path.exists(path):
        done = [json.loads(l) for l in open(path) if l.strip()]
    have = {tuple(d["ibs"]) for d in done}
    todo = [c for c in chunks if c not in have]
    if not {tuple(d["ibs"]) for d in done} <= set(chunks):    # explicit check: python -O drops asserts
        raise SystemExit(f"{path} comes from a different chunking; pass the old chunk size or remove the file")
    print(f"  ({a},{b}) {len(chunks)} chunks, {len(todo)} to do, {workers} workers", file=sys.stderr, flush=True)
    if todo:
        with Pool(workers, initializer=_init, initargs=(a, b)) as pool, open(path, "a") as f:
            for r in pool.imap_unordered(_chunk, todo):
                f.write(json.dumps(r) + chr(10)); f.flush(); done.append(r)
                print(f"  ({a},{b}) chunk {len(done)}/{len(chunks)}  {time.time() - t0:.0f}s", file=sys.stderr, flush=True)
    untested = Counter(); low = []; GAP = [0.0, 1.0]; cand = 0
    for r in done:
        untested.update({int(k): v for k, v in r["untested"].items()})
        for x in r["low"]:            # chunks computed with a higher cut: entries above the current cut count as untested
            if x[0] > cut and gcd(a, b) != 1: untested[x[0]] += 1
            else: low.append(tuple(x))
        GAP[0] = max(GAP[0], r["gap"][0]); GAP[1] = min(GAP[1], r["gap"][1]); cand += r["cand"]
    amb = [x for r in done for x in r.get("amb", [])]
    with open(os.path.join(HERE, f"amb{a}x{b}.json"), "w") as f: json.dump(amb, f)
    bir = Counter(v[0] for v in low if v[3] == 1)
    nonb = Counter(v[0] for v in low if v[3] != 1)
    om_bir = min(bir) if bir else None
    ext = Counter((v[1], v[2]) for v in low if v[3] == 1 and v[0] == om_bir)
    return dict(bidegree=[a, b], maps=[nMa, nMb], O=[nA, nB],
                bound_for_c_le_3=nA + nB - 6, distinct_T_c_ge_4=len(low), candidates=cand,
                birational_by_omega=dict(sorted(bir.items())), nonbirational_by_omega=dict(sorted(nonb.items())),
                omega_untested_above_cut=dict(sorted(untested.items())), cut=cut, omega_min_birational=om_bir, max_2j_plus_h_birational=(nA + nB - om_bir) if om_bir is not None else None,
                extremal_jh=sorted([list(k), v] for k, v in ext.items()), gap=GAP, borderline_T=len(amb), seconds=round(time.time() - t0, 1))


def cut_check(a, b): return CUT[(a, b)]


# F-01 values (f01.out): omega_min over birational pairs, and birational counts at omega <= cut
F01 = {(1, 2): (6, {6: 96}), (2, 2): (6, {6: 192, 7: 384, 8: 6720}), (2, 3): (10, {}), (3, 3): (10, {10: 384})}
# serial run of this script (f02_serial_2x4_3x4.out): the parallel version must reproduce these lines exactly
SERIAL = {}
_sp = os.path.join(HERE, "f02_serial_2x4_3x4.out")
if os.path.exists(_sp):
    for _l in open(_sp):
        if _l.startswith("{"):
            _d = json.loads(_l); _d.pop("seconds"); SERIAL[tuple(_d["bidegree"])] = _d

if __name__ == "__main__":
    todo = [tuple(int(x) for x in s.split("x")) for s in sys.argv[1:]]
    ok = True
    for a, b in todo:
        res = spectrum(a, b)
        print(json.dumps(res)); sys.stdout.flush()
        if res["omega_min_birational"] is None or res["omega_min_birational"] > cut_check(a, b):
            print(f"  ({a},{b}) WARNING: no birational T at or below the cut; omega_min not determined"); ok = False
        if not (res["gap"][0] < 1e-10 and res["gap"][1] > 1e-6):
            print(f"  ({a},{b}) WARNING: separation gap"); ok = False
        if (a, b) in SERIAL:
            mine = json.loads(json.dumps(res)); mine.pop("seconds"); mine.pop("borderline_T")
            good = mine == SERIAL[(a, b)]
            print(f"  ({a},{b}) cross-check with the serial run: {'ok' if good else 'MISMATCH'}"); ok &= good
        if (a, b) in F01:
            om, lowc = F01[(a, b)]
            cut = max(lowc) if lowc else om
            mine = {k: v for k, v in res["birational_by_omega"].items() if k <= cut}
            # (2,3): F-01 found no T with c >= 3 below 10; here omega_min must be 10 too
            good = res["omega_min_birational"] == om and (mine == lowc or not lowc)
            print(f"  ({a},{b}) cross-check with F-01: omega_min {res['omega_min_birational']} vs {om}, low {mine} vs {lowc}:",
                  "ok" if good else "MISMATCH"); ok &= good
    print("PASS" if ok else "FAIL")
    if not ok: raise SystemExit(1)
