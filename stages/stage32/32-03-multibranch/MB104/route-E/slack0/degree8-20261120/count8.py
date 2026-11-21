"""Check the degree-8 list: per profile, the weighted number of covers sum 1/|Aut| in L5_8_<profile>.pkl (build5 output)
must equal the Hurwitz number in hurwitz8.txt.   usage: python3 count8.py dir"""
import sys, glob, pickle
D = sys.argv[1] if len(sys.argv) > 1 else '.'
H = {}
for l in open(__file__.rsplit('/', 1)[0] + '/hurwitz8.txt' if '/' in __file__ else 'hurwitz8.txt'):
    p, c = l.split(); H[p.replace(',', '')] = float(c)
N = W = bad = 0
for fn in sorted(glob.glob(f'{D}/L5_8_*.pkl')):
    t = fn.rsplit('L5_8_', 1)[1][:-4]; d = pickle.load(open(fn, 'rb'))
    w = sum(1 / a for a in d['aut']); N += len(d['aut']); W += w
    if abs(w - H[t]) > 1e-9: bad += 1; print('MISMATCH', t, w, H[t])
print(f'profiles {len(H)}, covers {N}, weighted {W}, Hurwitz total {sum(H.values())}, mismatches {bad}')
