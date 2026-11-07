# tally of the light smoothness check (mksx.py jobs sx1_/sx2_*)
import re, glob, collections
gen = collections.defaultdict(set); bad = []; ok = 0
for f in sorted(glob.glob('sx[12]_*.out')):
    t = open(f).read(); tag = re.match(r'sx[12]_(.*)_\d+\.out', f).group(1)
    yd = re.search(r'YDEG (\d+)', t); so = re.search(r'SINGOFF dim (-?\d+)\s+deg (\d+)', t)
    se = [m for m in re.findall(r'SINGE node (\d+)\s+chart (\d+).*?sing dim (-?\d+)\s+sing length (\d+)', t) if m[2] != '-1']
    err = [w for w in ('error', 'ERROR', '?') if w in t]
    if 'DONE' not in t or err or not yd or not so:
        bad.append((f, 'INCOMPLETE', err, t.strip().splitlines()[-1:])); continue
    gen[f[:3] + tag].add(int(yd.group(1)))
    if so.group(1) != '-1' or se:
        bad.append((f, 'SINGULAR', so.groups(), se)); continue
    ok += 1
print('smooth', ok, ' not smooth / incomplete', len(bad))
for b in bad: print(' ', b)
print('Y degrees per family:', {k: sorted(v) for k, v in gen.items()})
