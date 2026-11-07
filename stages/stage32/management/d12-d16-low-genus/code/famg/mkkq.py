import glob, re, os
xs = open('famd/x_28246_121.sing').read()
KL = re.findall(r'(KL\[\d+\] = satur\(std\(S \+ ideal\([^;]*\)\), MX\);)', xs)
kdef = 'list KL;\n' + '\n'.join(KL) + '\n'
fs = []
for d in ('m16/m_*.out', 'm16/w_*.out', 'm16u/*.out', 'm2c/*.out', 'famc/*.out', 'famd/*.out', 'famg/s1_*.out', 'gph/g_*.out'):
    for fn in glob.glob(d):
        t = open(fn).read()
        if 'COMP ' not in t or 'END' not in t: continue
        m = re.search(r'SIGMAG\s+(-?\d+)', t)
        if m and int(m.group(1)) >= 2: continue
        if re.search(r'^COMP\s+\d+\s+4\s+\d+\s+1', t, re.M): fs.append(fn)
jobs = []
for fn in fs:
    s = open(fn[:-4] + '.sing').read(); k = s.index('"COMPS", nq;')
    inj = kdef + '''int iq4; int kq4; for (iq4 = 1; iq4 <= nq; iq4++) { if (mult(QL[iq4]) == 4) { string kn4 = "UNKNOWN";
  for (kq4 = 1; kq4 <= 92; kq4++) { if (size(reduce(KL[kq4], QL[iq4])) == 0 && size(reduce(QL[iq4], std(KL[kq4]))) == 0) { kn4 = "G" + string(kq4); } }
  "QUARTIC", iq4, kn4; kill kn4; } }
quit;
'''
    nm = '_'.join(os.path.normpath(fn[:-4]).split(os.sep))
    open(f'famg/kq/{nm}.sing', 'w', newline='\n').write(s[:k] + inj); jobs.append(nm)
open('famg/kq/jobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n'); print(len(jobs))
