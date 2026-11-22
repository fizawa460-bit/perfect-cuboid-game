"""Small backup of one profile's degree-9 cover list, enough to rebuild L7 with build7 (PACK mode) in hours, not a day.

usage: python3 pack9.py n tag D out.npz          (D holds full_<n>_<tag>.pkl, L7_<n>_<tag>.pkl and maybe regen_<n>_<tag>.pkl)

Keeps the monodromy tuples of all covers (int8), and for each orbit only the member that build7 refined: its index,
its double-precision position (the full_ row), whether it was in the cov file, and its 80-digit regen start if any.
The images, the orbits and the 60-digit points are recomputed by build7 from these (PACK=out.npz, see build7.py).
About 54 bytes per cover plus 530 bytes per orbit (232333: about 0.6 GB instead of 13 GB of L7)."""
import sys, os, pickle, numpy as np

def main():
    n, tag, D, out = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
    F = pickle.load(open(f'{D}/full_{n}_{tag}.pkl', 'rb')); L = pickle.load(open(f'{D}/L7_{n}_{tag}.pkl', 'rb'))
    N = len(F['sols']); assert L['N'] == N
    reps = np.flatnonzero(L['kind'] < 3); assert (L['src'][reps] == reps).all()
    TT = F['tuples'] if isinstance(F['tuples'], np.ndarray) else np.array(F['tuples'], np.int8)
    inc = np.zeros(N, bool); inc[np.asarray(F['in_cov_file'], np.int64)] = True
    rgf = f'{D}/regen_{n}_{tag}.pkl'
    rg = pickle.load(open(rgf, 'rb')) if os.path.exists(rgf) else {}
    rg = {int(i): v for i, v in rg.items() if v is not None and L['kind'][i] == 2}
    np.savez_compressed(out + '.tmp.npz', n=n, tag=tag, N=N, tuples=TT.astype(np.int8), reps=reps.astype(np.int64),
                        sols=np.asarray(F['sols'])[reps], incov=inc[reps], kind=L['kind'][reps].astype(np.int8),
                        meta=np.frombuffer(pickle.dumps({k: v for k, v in F.items() if k not in ('sols', 'tuples', 'confirmed', 'in_cov_file')}), np.uint8),
                        regen=np.frombuffer(pickle.dumps(rg), np.uint8),
                        check=np.array([L['orbG'].max() + 1, L['orbA'].max() + 1, np.sum(1 / L['aut'])]))
    os.replace(out + '.tmp.npz', out)
    print(f'{tag}: {N} covers, {len(reps)} refined, {len(rg)} regen -> {out} ({os.path.getsize(out) / 1e6:.1f} MB)', flush=True)

if __name__ == '__main__': main()
