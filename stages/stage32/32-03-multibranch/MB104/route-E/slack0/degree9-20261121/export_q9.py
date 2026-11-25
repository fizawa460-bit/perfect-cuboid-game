"""Query-only file of one profile for the distributed (9,9) run of search7: the odd points of the orbit
representatives (one cover per Aut(B) x <conj> orbit, as search6/search7 take queries), small enough for the shared
folder (about 380 bytes per representative).

usage: python3 export_q9.py n tag D out.npz          (D holds L7_<n>_<tag>.pkl and its _z / _inf arrays)

The file holds: n, prof, oddy, crity, orig (row of each representative in the L7 file), Z, INF, aut.  search7 loads
a directory of such files (qry_<n>_<tag>.npz) as its query side: queries = all rows; the 60-digit points, p, q and
the critical points stay on the owner machine (a candidate that needs them is deferred, see search7 DEFER)."""
import sys, os, pickle, numpy as np

def main():
    n, tag, D, out = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
    pre = f'{D}/L7_{n}_{tag}'; d = pickle.load(open(pre + '.pkl', 'rb'))
    o = np.asarray(d['orbG']); N = len(o)
    first = np.full(o.max() + 1, -1, np.int64)
    for i in range(N - 1, -1, -1): first[o[i]] = i
    reps = np.nonzero(first[o] == np.arange(N))[0]
    Z = np.load(pre + '_z.npy', mmap_mode='r'); INF = np.load(pre + '_inf.npy', mmap_mode='r')
    np.savez(out + '.tmp.npz', n=n, prof=np.array(d['prof']), oddy=np.asarray(d['oddy']), crity=np.asarray(d['crity']),
             orig=reps.astype(np.int64), Z=np.asarray(Z[reps]), INF=np.asarray(INF[reps]), aut=np.asarray(d['aut'])[reps])
    os.replace(out + '.tmp.npz', out)
    print(f'{tag}: {N} covers, {len(reps)} representatives -> {out} ({os.path.getsize(out) / 1e6:.1f} MB)', flush=True)

if __name__ == '__main__': main()
