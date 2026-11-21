"""Merge split runs of one profile (mono_par with OWN=r/K, DELTA_OUT, NBASE) back into one checkpoint.

usage: python3 merge9.py base_ckpt.pkl out_ckpt.pkl delta_0.pkl [delta_1.pkl ...]

Every split run starts from the same base checkpoint (same L, fixed points and coordinates), so the covers in the
deltas are in the same coordinates and can simply be appended; duplicates (by canonical monodromy tuple) are dropped.
Tuples may be stored as lists of tuples (old checkpoints) or int8 arrays (N, 6, n); the output uses int8 arrays.
The merged checkpoint resumes like any other (plain mono_par, or another split round)."""
import sys, os, pickle
import numpy as np
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fastmono-20261119')
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import monodromy as md

def as_arr(TT):
    return TT if isinstance(TT, np.ndarray) else np.array(TT, np.int8)

def key(row):
    return bytes([x for g in md.canon(tuple(map(tuple, row.tolist())))[0] for x in g])

def main():
    base, out, deltas = sys.argv[1], sys.argv[2], sys.argv[3:]
    d = pickle.load(open(base, 'rb')); nb = len(d['sols'])
    T0 = as_arr(d['TT']); seen = set(key(r) for r in T0)
    sols = [np.asarray(d['sols'])]; TT = [T0]; IS = list(d['ISREP']); CF = list(d['CONF']); REJ = list(d['REJ'])
    for fn in deltas:
        e = pickle.load(open(fn, 'rb'))
        assert e['nbase'] == nb, f'{fn}: made from a base of {e["nbase"]} covers, this base has {nb}'
        Te = as_arr(e['TT']); keep = []
        for k, r in enumerate(Te):
            c = key(r)
            if c in seen: continue
            seen.add(c); keep.append(k); IS.append(e['ISREP'][k]); CF.append(e['CONF'][k])
        if keep: sols.append(np.asarray(e['sols'])[keep]); TT.append(Te[keep])
        REJ += list(e['REJ'][len(d['REJ']):]) if len(e['REJ']) >= len(d['REJ']) else list(e['REJ'])
        print(f'{fn}: {len(Te)} covers, {len(keep)} new', flush=True)
        del e
    d['sols'] = np.concatenate(sols); d['TT'] = np.concatenate(TT); d['ISREP'] = IS; d['CONF'] = CF; d['REJ'] = REJ
    pickle.dump(d, open(out + '.tmp', 'wb')); os.replace(out + '.tmp', out)
    print(f'merged: {nb} -> {len(d["TT"])} covers -> {out}', flush=True)

if __name__ == '__main__': main()
