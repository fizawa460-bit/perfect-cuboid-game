"""Lemma G by components for the lg jobs whose remainder was reducible (the 14 non-reduced classes 666..679): the lg
script up to 'Bp = RR;' (known curves removed), then minAssGTZ + normal.lib genus of each component (as cg/).
usage (from stoll/): python d16all/mkrr.py   (reads d16all/h1/lg_open.txt from tally_lg.py)"""
CG = open("p16all/mkcg.py").read().split("CG = '''")[1].split("'''")[0]
jobs = [l.split()[0] for l in open('d16all/h1/lg_open.txt') if 'remainder-reducible' in l]
for j in jobs:
    s = open(f'd16all/h1/{j}.sing').read()
    k = s.index('Bp = RR; kill RR;'); k = s.index('\n', k) + 1
    open(f'd16all/h1/rr_{j[3:]}.sing', 'w', newline='\n').write(s[:k] + 'LIB "primdec.lib"; LIB "normal.lib";\n' + CG)
open('d16all/h1/rrjobs.txt', 'w', newline='\n').write('\n'.join('rr_' + j[3:] for j in jobs) + '\n')
print(len(jobs))
