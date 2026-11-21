"""Write cov_/full_/rej_/extra_ files from a mono_par/mono_dir checkpoint, with the analyse loop on NP processes.
usage: python3 export9.py ckpt_dir_<n>_<tag>.pkl n t1,..,t6 [NP]   (writes next to the checkpoint)"""
import sys, os, pickle, multiprocessing as mp
sys.argv, _a = sys.argv[:1] + ['9', '1,1,1,1,1,1'], sys.argv   # mono_par imports parse nothing at import time
import mono_par
sys.argv = _a
ck, n, prof = sys.argv[1], int(sys.argv[2]), tuple(int(x) for x in sys.argv[3].split(','))
NP = int(sys.argv[4]) if len(sys.argv) > 4 else 4
d = pickle.load(open(ck, 'rb'))
os.chdir(os.path.dirname(os.path.abspath(ck)))
with mp.get_context('fork').Pool(NP) as P:
    k, N = mono_par.export_par({'sols': list(d['sols']), 'TT': d['TT'], 'CONF': d['CONF'], 'REJ': d['REJ'], 'L': d['L'], 'fixed': d['fixed']}, n, prof, P)
print(f'wrote cov ({k} covers passing analyse) and full ({N})', flush=True)
