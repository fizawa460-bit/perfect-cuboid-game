"""32R-74: genus lower bound for C_0 near a net low member M_p via the specialization decomposition.
g(C_0) = sum_sheets g + sum_specials (g(Y_s) - c_s) + N - S + 1   (A2), with
 good special: config Z -> G_Z - 1 ; crossing -> -1 ;  bad special -> -ends (worst case: all discs)."""
import re, sys, glob, os, math, collections, json
def load(name):
    g = open(f'gph/g_{name}.out').read(); h = open(f'gph2/h_{name}.out').read()
    comps = {}; flags = []
    for m in re.finditer(r'^COMP\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)', g, re.M):
        ia, dg, mu, ge = map(int, m.groups()); comps[('C', ia)] = dict(deg=dg, m=mu, g=max(0, ge))
    nodes = {}
    for m in re.finditer(r'^NODE\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+comps\s+([\d ]*)$', g, re.M):
        jj, pd, e, lok = map(int, m.groups()[:4]); cs = [int(x) for x in m.group(5).split()]
        nodes[jj] = dict(e=e, lok=lok, comps=cs, pdeg=pd)
    cross = []
    for m in re.finditer(r'^CROSS\s+(\d+)\s+(\d+)\s+pdeg\s+(\d+)\s+len\s+(\d+)\s+on\s+([\d ]*?)\s+basept\s+(\d)', g, re.M):
        a, b, pd, ln = map(int, m.groups()[:4]); on = [int(x) for x in m.group(5).split()]; bp = int(m.group(6))
        cross.append(dict(a=a, b=b, pdeg=pd, len=ln, on=on, bp=bp))
    badc = {int(a): v for a, v in re.findall(r'^BADC\s+(\d+)\s+(\S+)', h, re.M)}
    bade = {int(a): v for a, v in re.findall(r'^BADE\s+(\d+)\s+(\S+)', h, re.M)}
    badx = []
    for m in re.finditer(r'^BADX\s+(\d+)\s+(\d+)\s+(\d+)\s+(base|pt)\s+(\S+)(?:\s+(\S+))?', h, re.M):
        badx.append(m.groups())
    return comps, nodes, cross, badc, bade, badx
def analyze(name):
    comps, nodes, cross, badc, bade, badx = load(name)
    flags = []
    V = dict(comps)
    for jj, nd in nodes.items():
        if nd['e'] > 0: V[('E', jj)] = dict(deg=0, m=nd['e'], g=0)
        if nd['pdeg'] != 1: flags.append(f'node {jj} pdeg {nd["pdeg"]}')
        if nd['lok'] != 1 and nd['e'] > 0: flags.append(f'node {jj} tangency')
    inc = []   # (u, v, len, special-point-key or None)
    for jj, nd in nodes.items():
        if nd['e'] > 0:
            for c in nd['comps']: inc.append((('E', jj), ('C', c), 1))
    xp = collections.Counter()
    for k, cr in enumerate(cross):
        if len(cr['on']) > 2: flags.append(f'triple point {cr["on"]}')
        if cr['pdeg'] != 1: flags.append(f'cross pdeg {cr["pdeg"]}')
        if cr['len'] != 1: flags.append(f'tangent crossing {cr["a"]},{cr["b"]}')
        inc.append((('C', cr['a']), ('C', cr['b']), cr['len'], k))
    # x.Gamma
    xg = {}
    for v, d in V.items():
        if v[0] == 'C':
            s = d['m'] * (2 * d['g'] - 2 - d['deg'])
            for jj, nd in nodes.items():
                if v[1] in nd['comps']: s += nd['e']
            for cr in cross:
                if v[1] == cr['a']: s += V[('C', cr['b'])]['m'] * cr['len']
                if v[1] == cr['b']: s += V[('C', cr['a'])]['m'] * cr['len']
        else:
            nd = nodes[v[1]]; s = -2 * nd['e'] + sum(V[('C', c)]['m'] for c in nd['comps'])
        xg[v] = s
    tot = sum(V[v]['m'] * xg[v] for v in V)
    if any(s < 0 for s in xg.values()): flags.append('negative x.Gamma')
    sheets = [v for v in V if xg[v] > 0]; triv = [v for v in V if xg[v] == 0]
    for v in sheets:
        if V[v]['m'] != 1: flags.append(f'multiple sheet {v}')
    # configs
    par = {v: v for v in triv}
    def f(v):
        while par[v] != v: par[v] = par[par[v]]; v = par[v]
        return v
    for t in inc:
        u, w = t[0], t[1]
        if u in par and w in par: par[f(u)] = f(w)
    cfg = collections.defaultdict(list)
    for v in triv: cfg[f(v)].append(v)
    def bad_of(v): return badc.get(v[1]) if v[0] == 'C' else bade.get(v[1])
    specials = []
    for r, mem in cfg.items():
        bds = {bad_of(v) for v in mem}
        if len(bds) != 1: flags.append(f'config {mem} bad dirs {bds}')
        bd = sorted(bds)[0]
        mset = set(mem)
        # pieces
        vert = {}; Eint = 0
        for v in mem:
            mu = V[v]['m']
            if mu == 1: vert[v] = V[v]['g']; continue
            if V[v]['g'] != 0: flags.append(f'multiple elliptic {v}')
            orders = []
            for t in inc:
                if t[0] == v: orders.append(V[t[1]]['m'] * t[2])
                elif t[1] == v: orders.append(V[t[0]]['m'] * t[2])
            c = math.gcd(mu, *orders) if orders else mu
            if c != 1: flags.append(f'split cover {v} m={mu} orders={orders}')
            gg = 1 - mu + sum(mu - math.gcd(mu, o) for o in orders) // 2
            vert[v] = gg
        ends = 0
        for t in inc:
            u, w = t[0], t[1]
            if u in mset and w in mset: Eint += math.gcd(V[u]['m'], V[w]['m'])
            elif (u in mset) != (w in mset): ends += 1
        b1 = Eint - len(vert) + 1
        G = sum(vert.values()) + b1
        specials.append(dict(kind='Z', mem=mem, bad={bd} - {'NONE'}, good=G - 1, ends=ends))
    # sheet-sheet incidences
    for t in inc:
        u, w = t[0], t[1]
        if u in sheets and w in sheets:
            if len(t) == 4:
                k = t[3]; bx = [b for b in badx if int(b[0]) == cross[k]['a'] and int(b[1]) == cross[k]['b']]
                bd = set()
                for b in bx: bd |= {b[4], b[5]} if b[3] == 'base' else {b[4]}
                bd -= {None, 'NONE'}
                if 'ALL' in bd or not bx: bd = {'*'}
            else:
                bd = {'*'}   # E-sheet / curve-sheet crossing: direction not computed -> always worst
            specials.append(dict(kind='X', mem=[u, w], bad=bd, good=-1, ends=2))
    N = sum(s['ends'] for s in specials); S = len(sheets)
    base = sum(V[v]['g'] for v in sheets) - S + N + 1
    dirs = set().union(*[s['bad'] for s in specials]) - {'*'}
    def bound(lam):
        return base + sum((-s['ends']) if ('*' in s['bad'] or lam in s['bad']) else s['good'] for s in specials)
    allgood = base + sum((-s['ends']) if '*' in s['bad'] else s['good'] for s in specials)
    res = {lam: bound(lam) for lam in dirs}; res['generic'] = bound(None)
    worst = min(res.values())
    return dict(xM=tot, name=name, sheets=len(sheets), specials=len(specials), N=N, allgood=allgood, worst=worst, flags=flags,
                perdir=res)
names = sorted(os.path.basename(f)[2:-4] for f in glob.glob('gph/g_*.out'))
out = []; C = collections.Counter()
for nm in names:
    r = analyze(nm); out.append(r)
    st = 'FLAG' if r['flags'] else ('OK' if r['worst'] >= 2 else 'LOW')
    C[st] += 1
    print(f"{nm:28s} x.M {r['xM']} sheets {r['sheets']} specials {r['specials']} allgood {r['allgood']:3d} worst {r['worst']:3d} {st} {';'.join(r['flags'])[:120]}")
print(dict(C))
json.dump(out, open('gph2/analysis.json', 'w'), indent=1, default=str)
