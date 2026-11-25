"""Mini L7 files for resolving the distributed (9,9) run: the query covers that a table machine reported as hits or
deferred candidates (search7 QMODE, res99_<X>.pkl), cut out of the owner's L7 with their 60-digit points, so that the
table machine can rerun just these queries in full mode (verification with both 60-digit sides, birationality).

usage: python3 mkmini9.py res99_X.pkl LOCDIR OUTDIR      -> OUTDIR/L7_9_<tag>.pkl (+ _z/_inf/_pq/_crit/_hp.npy)
for every tag of res99_X.pkl's hits and deferred list that LOCDIR holds; prints the tags written and the tags needed.
Every mini row is its own orbit (orbG = orbA = arange), so search7 takes each one as a query."""
import sys, os, glob, pickle, numpy as np

def needed(res):
    R = pickle.load(open(res, 'rb')); need = {}
    for h in R['hits']: need.setdefault(str(h[1]), set()).add(int(h[2]))
    for x in R['deferred']: need.setdefault(str(x[1]), set()).add(int(x[2]))
    return {t: sorted(v) for t, v in need.items()}

def main():
    res, loc, out = sys.argv[1:4]; os.makedirs(out, exist_ok=True); need = needed(res)
    print('needed', ' '.join(f'{t}:{len(v)}' for t, v in sorted(need.items())), flush=True)
    for t, rows in sorted(need.items()):
        pre = f'{loc}/L7_9_{t}'
        if not os.path.exists(pre + '.pkl'): continue
        d = pickle.load(open(pre + '.pkl', 'rb')); N = d['N']; rows = np.array(rows, np.int64); k = len(rows)
        m = {}
        for key, v in d.items():
            if isinstance(v, np.ndarray) and v.ndim >= 1 and len(v) == N and key not in ('oddy', 'crity'): m[key] = v[rows]
            else: m[key] = v
        m['N'] = k; m['orbG'] = np.arange(k); m['orbA'] = np.arange(k); m['mini_orig'] = rows
        for s in ('z', 'inf', 'pq', 'crit', 'hp'):
            np.save(f'{out}/L7_9_{t}_{s}.npy', np.asarray(np.load(f'{pre}_{s}.npy', mmap_mode='r')[rows]))
        pickle.dump(m, open(f'{out}/L7_9_{t}.pkl.tmp', 'wb')); os.replace(f'{out}/L7_9_{t}.pkl.tmp', f'{out}/L7_9_{t}.pkl')
        open(f'{out}/L7_9_{t}.done', 'w').write(f'{k}\n'); print('wrote', t, k, flush=True)

if __name__ == '__main__': main()
