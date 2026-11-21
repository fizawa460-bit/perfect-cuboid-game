"""Merge split runs of one profile (mono_par with OWN=r/K, DELTA_OUT, NBASE) back into one checkpoint.

usage: python3 merge9.py base_ckpt.pkl out_ckpt.pkl delta_0.pkl [delta_1.pkl ...]

Every split run starts from the same base checkpoint (same L, fixed points and coordinates), so the covers in the
deltas are in the same coordinates and can simply be appended; duplicates (by canonical monodromy tuple) are dropped.
The merged checkpoint resumes like any other (plain mono_par, or another split round)."""
import sys, os, pickle
import numpy as np
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fastmono-20261119')
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import monodromy as md

def main():
    base, out, deltas = sys.argv[1], sys.argv[2], sys.argv[3:]
    d = pickle.load(open(base, 'rb')); nb = len(d['sols'])
    seen = set(md.canon(t)[0] for t in d['TT'])
    sols = [d['sols']]; TT = list(d['TT']); IS = list(d['ISREP']); CF = list(d['CONF']); REJ = list(d['REJ'])
    for fn in deltas:
        e = pickle.load(open(fn, 'rb'))
        assert e['nbase'] == nb, f'{fn}: made from a base of {e["nbase"]} covers, this base has {nb}'
        keep = []
        for k, t in enumerate(e['TT']):
            c = md.canon(t)[0]
            if c in seen: continue
            seen.add(c); keep.append(k); TT.append(t); IS.append(e['ISREP'][k]); CF.append(e['CONF'][k])
        if keep: sols.append(np.asarray(e['sols'])[keep])
        REJ += list(e['REJ'][len(d['REJ']):]) if len(e['REJ']) >= len(d['REJ']) else list(e['REJ'])
        print(f'{fn}: {len(e["TT"])} covers, {len(keep)} new', flush=True)
    d['sols'] = np.concatenate(sols); d['TT'] = TT; d['ISREP'] = IS; d['CONF'] = CF; d['REJ'] = REJ
    pickle.dump(d, open(out + '.tmp', 'wb')); os.replace(out + '.tmp', out)
    print(f'merged: {nb} -> {len(TT)} covers -> {out}', flush=True)

if __name__ == '__main__': main()
