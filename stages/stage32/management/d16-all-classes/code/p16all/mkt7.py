"""T7 data for the pencil members that failed the normal-crossings check (p16all/nc/*.out without NC-OK): the sx member
script up to the member ideal, plus the setup expected by m16/tail.sing (HH = 2, FL = (F0, F1), NODES, the D-curve
list DL / DLc of the decomposition used, ordP), then m16/tail.sing from its '// direction basis' block on (the member
NN is given, so the member search of the tail is skipped).  usage (from stoll/): python p16all/mkt7.py"""
import json, glob, os
MAP = json.load(open('p16all/sxmap.json'))
TAIL = open('m16/tail.sing').read(); TAIL = TAIL[TAIL.index('// direction basis'):]
bad = [os.path.basename(f)[6:-4] for f in sorted(glob.glob('p16all/nc/nc_cg_sx_*.out')) if 'NC-OK' not in open(f).read()]
for nm in bad:
    s = open(f'p16all/{nm}.sing').read(); k = s.index('ideal B = std(S + ideal(NN));')
    i, t, m, D = MAP[nm]; cids = sorted(int(c) for c in D if int(c) <= 92)
    add = 'int HH = 2; list FL; FL[1] = F0; FL[2] = F1; int kk; int js; string TAG = "%s";\n' % nm
    add += 'ideal NODES = std(S + minor(jacob(S), 4));\n'
    add += 'list DL; intvec DLc;\n' + ''.join(f'DL[{n+1}] = G{c}; DLc[{n+1}] = {D[str(c)]};\n' for n, c in enumerate(cids))
    add += 'proc ordP(poly F, ideal P) { int k = 0; int mm2; for (mm2 = 1; mm2 <= 6; mm2++) { if (size(reduce(F, satur(std(S + P^mm2), MX))) == 0) { k = mm2; } else { break; } } return(k); }\n'
    add += 'LIB "primdec.lib"; LIB "normal.lib";\n'
    open(f'p16all/t7/t7_{nm}.sing', 'w', newline='\n').write(s[:k] + add + TAIL)
open('p16all/t7/jobs.txt', 'w', newline='\n').write('\n'.join('t7_' + n for n in bad) + '\n')
print(len(bad))
