import glob, os, re, json, collections
src = open('gph2/analyze.py', encoding='utf-8').read().split('names = sorted(')[0]
ns = {}; exec(src, ns)
def load(name):
    t = open(f'm16/{name}.out').read()
    comps = {}
    for m in re.finditer(r'^COMP\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)', t, re.M):
        ia, dg, mu, ge = map(int, m.groups()); comps[('C', ia)] = dict(deg=dg, m=mu, g=max(0, ge))
    nodes = {}
    for m in re.finditer(r'^NODE\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+comps\s*([\d ]*)$', t, re.M):
        jj, pd, e, lok = map(int, m.groups()[:4]); nodes[jj] = dict(e=e, lok=lok, comps=[int(x) for x in m.group(5).split()], pdeg=pd)
    cross = []
    for m in re.finditer(r'^CROSS\s+(\d+)\s+(\d+)\s+pdeg\s+(\d+)\s+len\s+(\d+)\s+on\s+([\d ]*?)\s+basept\s+(\d)', t, re.M):
        a, b, pd, ln = map(int, m.groups()[:4]); cross.append(dict(a=a, b=b, pdeg=pd, len=ln, on=[int(x) for x in m.group(5).split()], bp=int(m.group(6))))
    badc = {int(a): v for a, v in re.findall(r'^BADC\s+(\d+)\s+(\S+)', t, re.M)}
    bade = {int(a): v for a, v in re.findall(r'^BADE\s+(\d+)\s+(\S+)', t, re.M)}
    badx = [m.groups() for m in re.finditer(r'^BADX\s+(\d+)\s+(\d+)\s+(\d+)\s+(base|pt)\s+(\S+)(?:\s+(\S+))?', t, re.M)]
    return comps, nodes, cross, badc, bade, badx
ns['load'] = load
C = collections.Counter(); rows = []
for f in sorted(glob.glob('m16/m_*.out')):
    nm = os.path.basename(f)[:-4]; t = open(f).read()
    if 'END' not in t:
        st = 'NOMEMBER' if 'NO-UNIQUE-MEMBER' in t else 'UNFINISHED'; C[st] += 1; rows.append((nm, st, None)); continue
    sg = int(re.search(r'SIGMAG\s+(-?\d+)', t).group(1)); hh = int(re.search(r'^HH\s+(\d+)', t, re.M).group(1))
    if sg >= 2: C['LEMMA-G'] += 1; rows.append((nm, 'LEMMA-G', sg)); continue
    r = ns['analyze'](nm)
    val = r['perdir'].get('B', r['perdir']['generic']) if hh == 2 else r['worst']
    if hh >= 4: st = 'WEB'
    elif r['flags']: st = 'FLAG'
    else: st = 'OK' if val >= 2 else 'LOW'
    C[st] += 1; rows.append((nm, st, val, r['allgood'], r['flags'][:3]))
print(dict(C))
for r in rows:
    if r[1] not in ('LEMMA-G', 'OK'): print(r)
json.dump(rows, open('m16/an.json', 'w'), default=str)
