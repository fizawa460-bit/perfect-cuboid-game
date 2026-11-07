import json, re
ext = json.load(open('famg/ext.json'))
SKIP = {'28246_0_0', '28246_2_0', '28255_0_1', '28255_1_0', '28255_2_0', '27988_0_0', '27988_1_0', '34761_1_0', '34761_2_0'}
t = open('famd/ext117.sing').read()
tail = t[t.index('ideal NODES = std(S + minor(jacob(S), 4));\n// fixed part'):]
a = tail.index('list HF = '); b = tail.index('\n', a)
jobs = []
for tag, L in ext.items():
    if tag in SKIP: continue
    for rep in ('1', '2'):
        fs = sorted(set(re.sub(r'\bu\b', 's', fac) for r, kind, fac, ln in L if r == rep))
        if not fs: continue
        if rep == '1':
            s = open(f'famg/c_{tag}.sing').read(); head = s[:s.index('ideal BL = std(S + ideal(F0, F1));')]
        else:
            s = open(f'famg/s2_{tag}_' + '0'.join([]) if False else f'famg/r_{tag}.sing').read(); head = s[:s.index('ideal BL = ')]
            # rep-2 Dc = D2 curves (from the s2 member job header)
            import glob
            sj = sorted(glob.glob(f'famg/s2_{tag}_*.sing'))[0]; sh = open(sj).read()
            head = sh[:sh.index('poly NN = F0 - ')]
        tl = tail[:a] + 'list HF = ' + ', '.join(fs) + ';' + tail[b:]
        n = f'e{rep}_{tag}'; open(f'famg/{n}.sing', 'w', newline='\n').write(head + tl); jobs.append(n)
open('famg/ejobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n'); print(len(jobs), jobs)
