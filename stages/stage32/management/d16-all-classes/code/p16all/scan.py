"""R2 §4.5 non-reduced member scan (as m2/scan16.py) for the d16all new pencils: for every pencil without a fixed
component and every known curve / node k, h0_p(D + 2Γ_k) with the judge decomposition (m, D).  h0 > 0 means |x|
has a member containing Γ_k with multiplicity >= 2 (relative to D); 'cap' = multiplicity bound of the generator set."""
import sys, json
sys.path.insert(0, 'fasth0'); import fasth0v2 as F
L = [l.split(chr(9)) for l in open('//wsl.localhost/Ubuntu/root/j16all_new_h0pos.txt').read().split(chr(10))[:-1]]
fixed = {int(i) for i, k in json.load(open('p16all/fixed.json'))}
def names(D): return [f"C{k}_{c}" if k <= 92 else f"N{k}_{c}" for k, c in sorted(D.items()) if c > 0]
out = {}
for idx, t in enumerate(L):
    j = t[2].split()
    if j[1] != '2' or idx in fixed: continue
    m = int(j[0]); D = {int(a): int(b) for a, b in (q.split(':') for q in j[2].split(','))}
    res = []
    for k in range(1, 141):
        c = D.get(k, 0) + 2
        if c > (4 if k <= 92 else 3): res.append((k, 'cap')); continue
        D2 = dict(D); D2[k] = c; hh = F.h0(m, names(D2))
        if hh > 0: res.append((k, hh))
    out[idx] = (2, res)
    print(idx, [r for r in res], flush=True)
json.dump(out, open('p16all/scan.json', 'w'))
import collections
C = collections.Counter((sum(1 for r in res if r[1] != 'cap'), sum(1 for r in res if r[1] == 'cap')) for h, res in out.values())
print('pencils', len(out), 'hist (#h0>0, #cap):', sorted(C.items()))
