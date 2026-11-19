"""Write a finished mono_dir checkpoint in speedup mono.py's output format, for fast40/build_all.py.

cov_<n>_<prof>.pkl / rej_<n>_<prof>.pkl hold only the covers that pass analyse() in double precision; build_all
refines them at 40 digits and regenerates the Aut(B) images itself, which brings back the covers with almost
coincident critical points as exact images (every Aut(B) orbit has such a member; checked by orbitcover.py for
2,2,2,2,2,2).  The complete list (all classes, tuples, flags) goes to full_<n>_<prof>.pkl.
usage: python3 export.py ckpt_dir_<n>_<prof>.pkl n t1,..,t6"""
import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md
from mono import System, analyse, analyse_loose
from covers import fingerprint

def export(d, n, prof, outdir='.'):
    S = System(n, prof, d['fixed'], d['L']); tag = f'{n}_{"".join(map(str, prof))}'
    covs = []; keep = []
    for i, u in enumerate(d['sols']):
        p, q, cc = S.unpack(u[None])
        an = analyse(p[0], q[0], n, prof, cc[0], list(S.ys)) or analyse_loose(p[0], q[0], n, prof, cc[0], list(S.ys))
        if an is None: continue
        keep.append(i); covs.append((np.concatenate([p[0], q[0]]), md.canon(d['TT'][i])[1]))
    sols = np.array(d['sols'])
    pickle.dump({'sols': sols[keep], 'ys': S.ys, 'REJ': d['REJ'], 'L': d['L'], 'fixed': d['fixed']},
                open(os.path.join(outdir, f'rej_{tag}.pkl'), 'wb'))
    pickle.dump({'n': n, 'prof': prof, 'covers': covs}, open(os.path.join(outdir, f'cov_{tag}.pkl'), 'wb'))
    pickle.dump({'sols': sols, 'ys': S.ys, 'L': d['L'], 'fixed': d['fixed'], 'tuples': d['TT'],
                 'confirmed': d['CONF'], 'in_cov_file': keep}, open(os.path.join(outdir, f'full_{tag}.pkl'), 'wb'))
    return len(keep), len(sols)

if __name__ == '__main__':
    d = pickle.load(open(sys.argv[1], 'rb')); n = int(sys.argv[2]); prof = tuple(int(x) for x in sys.argv[3].split(','))
    k, N = export(d, n, prof, os.path.dirname(os.path.abspath(sys.argv[1])))
    print(f'cov file: {k} covers that pass analyse (of {N}); full list: {N}')
