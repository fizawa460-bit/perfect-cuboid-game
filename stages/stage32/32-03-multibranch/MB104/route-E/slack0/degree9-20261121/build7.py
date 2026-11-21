"""Degree-n cover list for search6, memory-light (research code; one profile per call).

Same numbers as build5/build6 (60-digit refinement by hp_fast.refine_full / refine_extra, drift test, symmetry
images p, q -> M(p, q) (conjugated if needed) with odd and critical points carried over and relabelled), organised so
that a profile with millions of covers fits in memory:
  - the symmetry orbits (Stab(prof) in Aut(B) x <conj>, rule-named classes) are computed first;
  - a worker takes a chunk of orbits, refines ONE member per orbit (the next member if refinement or the drift test
    fails; the 80-digit regen start if mono_dir left one) and writes the rows of all members of the orbit as exact
    images of the refined one;
  - every chunk is saved (b7tmp_<n>_<tag>/c<k>.npz, resume after a restart) and the results are copied into
    fixed-width .npy files (memory-mapped by search6):
      L7_<n>_<tag>_pq.npy (N, 2n+2) complex128   P low->high, Q (double rounding of the 60-digit map)
      L7_<n>_<tag>_z.npy  (N, nodd) complex128   odd points, affine (value 0 where the point is infinity)
      L7_<n>_<tag>_inf.npy (N, nodd) bool        odd point is infinity
      L7_<n>_<tag>_crit.npy (N, 2n-2) complex128 critical points (labels crity)
      L7_<n>_<tag>_hp.npy (N, nodd, 2) S(DPS+12) 60-digit odd points as decimal strings (b'inf')
    and L7_<n>_<tag>.pkl: prof, oddy, crity, aut (N,), orbG (orbit id under Stab x <conj>), orbA (orbit id under
    Stab in Aut(B) only), kind (N,) int8 (0 refined from cov data, 1 from extra (polyroots), 2 regen, 3 image),
    src (N,) the refined cover each row was made from, res/mind of the refined source, syms.
  - Orbits where no member refines are listed in orphans_<n>_<tag>.txt and the run exits with code 3 (as build5).
Checks to run afterwards: count (sum 1/aut = Hurwitz number) and distinct (fingerprints) on the pq file.
usage: DPS=60 python3 build7.py n tag D [procs]"""
import os, sys, pickle, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build6 as B6
from build6 import md, autact, mp, DPS
SL = B6.SL

def orbits(F, prof, conj_too):
    RR = pickle.load(open(os.path.join(SL, 'fastmono-20261119', 'aut_rules_7_222222.pkl'), 'rb'))
    rkey = {(cj, pi): w for (cj, M, pi), (pi2, w) in zip(autact.sym_list(tuple(RR['prof'])), RR['rules'])}
    syms = autact.sym_list(prof); cls = [md.canon(t)[0] for t in F['tuples']]; cidx = {c: k for k, c in enumerate(cls)}
    N = len(cls); orb = np.full(N, -1, np.int64); members = []
    via = {}          # (j) -> (i, sym index) with class(j) = sym(class(i)), for i the first member of the orbit
    for i in range(N):
        if orb[i] >= 0: continue
        o = len(members); orb[i] = o; mem = [i]
        for k, (cj, M, pi) in enumerate(syms):
            if cj and not conj_too: continue
            j = cidx.get(md.canon(autact.apply(F['tuples'][i], (pi, rkey[(cj, pi)])))[0])
            if j is not None and orb[j] < 0: orb[j] = o; mem.append(j)
        members.append(mem)
    return orb, members, syms, rkey, cls, cidx

def image_row(Rj, sym, n, prof, oddy0):
    """build5's 'image of j' construction: the row of S(cover j) from the refined row of j"""
    cj, M, pi = sym
    pqj, oddj, sj, critj, ysj = Rj
    pp, qq = (pqj[:n + 1].conj(), pqj[n + 1:].conj()) if cj else (pqj[:n + 1], pqj[n + 1:])
    pq2 = np.concatenate([M[0, 0] * pp + M[0, 1] * qq, M[1, 0] * pp + M[1, 1] * qq])
    om = np.array([k for yq in range(6) for k in range(len(oddy0)) if pi[oddy0[k]] == yq])
    ysa = np.array(ysj); cm = np.array([k for yq in range(6) for k in range(len(ysa)) if pi[ysa[k]] == yq])
    odd2 = [oddj[k].conj() if cj else oddj[k] for k in om]
    def cs(x): return x if (x == b'inf' or not cj) else (x[0], x[1][1:] if x[1].startswith(b'-') else b'-' + x[1])
    s2 = [cs(sj[k]) for k in om]
    crit2 = np.array([critj[k] for k in cm]); crit2 = crit2.conj() if cj else crit2
    return pq2, odd2, s2, crit2, [pi[ysa[k]] for k in cm]

G = {}
def do_chunk(k):
    n, prof, F, covmap, members, chunks, syms, rkey, cls, cidx, oddy0, tmpd = (G[x] for x in
        ('n', 'prof', 'F', 'covmap', 'members', 'chunks', 'syms', 'rkey', 'cls', 'cidx', 'oddy0', 'tmpd'))
    fn = f'{tmpd}/c{k}.npz'
    if os.path.exists(fn): return fn
    rows_i = []; rows = []; kinds = []; srcs = []; resl = []; orphans = []
    for o in chunks[k]:
        mem = members[o]; ok = None
        order = sorted(mem, key=lambda x: (x not in F.get('regen', {}), x not in covmap, x))
        for i in order:
            r = B6.work((n, prof, F, covmap, [i]))[0]
            if r[8] == 'failed': continue
            if r[8] != 'regen':          # drift test (build5): critical points stay within 1e-5, points stay apart
                u = F['sols'][i]; c0 = np.array(list(F['fixed'][:3]) + list(u[2 * n + 2:]))
                dr = max(np.abs(r[4] - c).min() / (1 + abs(c)) for c in c0)
                if dr > 1e-5 or r[7] < 1e-10: continue
            elif r[7] < 1e-10: continue
            ok = (i, r); break
        if ok is None: orphans.append(o); continue
        i, r = ok; Ri = (r[1], r[2], r[3], r[4], r[5])
        kd = {'cov': 0, 'extra': 1, 'regen': 2}[r[8]]
        rows_i.append(i); rows.append(Ri); kinds.append(kd); srcs.append(i); resl.append((r[6], r[7]))
        for j in mem:
            if j == i: continue
            sym = None
            for (cj, M, pi) in syms:
                if md.canon(autact.apply(F['tuples'][i], (pi, rkey[(cj, pi)])))[0] == cls[j]: sym = (cj, M, pi); break
            if sym is None: orphans.append(o); continue      # cannot happen: j was put in the orbit by such a symmetry
            rows_i.append(j); rows.append(image_row(Ri, sym, n, prof, oddy0)); kinds.append(3); srcs.append(i); resl.append((r[6], r[7]))
    m = len(rows); nodd = len(oddy0)
    pq = np.array([x[0] for x in rows]) if m else np.zeros((0, 2 * n + 2), complex)
    z = np.zeros((m, nodd), complex); inf = np.zeros((m, nodd), bool)
    hp = np.empty((m, nodd, 2), dtype='S%d' % (DPS + 12))
    for a, x in enumerate(rows):
        for b, w in enumerate(x[1]):
            if abs(w[1]) < 1e-300: inf[a, b] = True
            else: z[a, b] = w[0] / w[1]
        for b, s in enumerate(x[2]): hp[a, b] = (b'inf', b'inf') if s == b'inf' else s
    crit = np.array([x[3] for x in rows]) if m else np.zeros((0, 2 * n - 2), complex)
    crity = np.array([x[4] for x in rows]) if m else np.zeros((0, 2 * n - 2), int)
    np.savez(fn + '.tmp.npz', i=np.array(rows_i, np.int64), pq=pq, z=z, inf=inf, hp=hp, crit=crit, crity=crity,
             kind=np.array(kinds, np.int8), src=np.array(srcs, np.int64), res=np.array(resl, float).reshape(-1, 2),
             orphans=np.array(orphans, np.int64))
    os.replace(fn + '.tmp.npz', fn); return fn

def main():
    n = int(sys.argv[1]); tag = sys.argv[2]; D = sys.argv[3]; NP = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    prof = tuple(int(c) for c in tag); t0 = time.time()
    F = pickle.load(open(f'{D}/full_{n}_{tag}.pkl', 'rb')); N = len(F['sols'])
    covmap = set(F['in_cov_file'])
    rgf = f'{D}/regen_{n}_{tag}.pkl'
    if os.path.exists(rgf): F['regen'] = {i: v for i, v in pickle.load(open(rgf, 'rb')).items() if v is not None}; print('80-digit starts for', sorted(F['regen']), flush=True)
    oddy0 = np.array([y for y in range(6) for _ in range(n - 2 * prof[y])])
    orbG, members, syms, rkey, cls, cidx = orbits(F, prof, True)
    orbA, _, _, _, _, _ = orbits(F, prof, False)
    print(f'{N} covers, {len(members)} orbits under Stab x <conj>, {orbA.max() + 1} under Stab in Aut(B); {time.time() - t0:.0f}s', flush=True)
    CH = int(os.environ.get('CHUNK', '300'))
    chunks = [list(range(k, min(k + CH, len(members)))) for k in range(0, len(members), CH)]
    tmpd = f'{D}/b7tmp_{n}_{tag}'; os.makedirs(tmpd, exist_ok=True)
    G.update(n=n, prof=prof, F=F, covmap=covmap, members=members, chunks=chunks, syms=syms, rkey=rkey, cls=cls, cidx=cidx, oddy0=oddy0, tmpd=tmpd)
    if NP > 1:
        import multiprocessing as _mp
        with _mp.get_context('fork').Pool(NP) as P: files = P.map(do_chunk, range(len(chunks)), chunksize=1)
    else: files = [do_chunk(k) for k in range(len(chunks))]
    t1 = time.time(); print(f'refined in {t1 - t0:.0f}s', flush=True)
    nodd = len(oddy0); pre = f'{D}/L7_{n}_{tag}'
    def mm(name, shape, dt): return np.lib.format.open_memmap(f'{pre}_{name}.npy.tmp', mode='w+', dtype=dt, shape=shape)
    PQ = mm('pq', (N, 2 * n + 2), complex); Z = mm('z', (N, nodd), complex); INF = mm('inf', (N, nodd), bool)
    CR = mm('crit', (N, 2 * n - 2), complex); HP = mm('hp', (N, nodd, 2), 'S%d' % (DPS + 12))
    kind = np.full(N, -1, np.int8); src = np.full(N, -1, np.int64); res = np.zeros((N, 2)); crity = None; orph = []
    for fn in files:
        d = np.load(fn); ii = d['i']
        if len(ii):
            PQ[ii] = d['pq']; Z[ii] = d['z']; INF[ii] = d['inf']; CR[ii] = d['crit']; HP[ii] = d['hp']
            kind[ii] = d['kind']; src[ii] = d['src']; res[ii] = d['res']
            cy = d['crity']
            if crity is None: crity = cy[0]
            assert (cy == crity).all()
        orph += list(d['orphans'])
    for a in (PQ, Z, INF, CR, HP): a.flush()
    del PQ, Z, INF, CR, HP
    if orph:
        bad = sorted({i for o in orph for i in members[o]})
        open(f'{D}/orphans_{n}_{tag}.txt', 'w').write(','.join(map(str, bad)) + '\n')
        print(f'{len(orph)} orbits without a refined cover ({len(bad)} covers) -> orphans file written', flush=True); sys.exit(3)
    assert (kind >= 0).all()
    for name in ('pq', 'z', 'inf', 'crit', 'hp'): os.replace(f'{pre}_{name}.npy.tmp', f'{pre}_{name}.npy')
    aut = np.array([md.canon(t)[1] for t in F['tuples']])
    pickle.dump({'n': n, 'prof': prof, 'oddy': oddy0, 'crity': crity, 'aut': aut, 'orbG': orbG, 'orbA': orbA, 'kind': kind,
                 'src': src, 'res': res, 'syms': [(cj, pi) for cj, M, pi in syms], 'N': N}, open(f'{pre}.pkl', 'wb'))
    print(f'n={n} prof={tag}: {N} covers, weighted {np.sum(1 / aut):.4f}; refined {int((kind < 3).sum())} '
          f'(cov {int((kind == 0).sum())}, extra {int((kind == 1).sum())}, regen {int((kind == 2).sum())}), images {int((kind == 3).sum())}; '
          f'worst residual {res[:, 0].max():.1e}, smallest point distance {res[:, 1].min():.1e}; {time.time() - t0:.0f}s', flush=True)

if __name__ == '__main__': main()
