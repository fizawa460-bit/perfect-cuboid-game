"""32R-74 analyzer v2: g(C_0) >= 1 + sum_{certified vertices} g + E_cert - V_cert   (bad tubes contribute >= 0).
Vertices: pieces of the components of M_p (cyclic covers for multiple components; c components each of genus g').
Edges: certified annuli at crossings (gcd(m, m') of them). A crossing is certified when b(Q) != 0 in the direction."""
import re, math, itertools, collections, json, glob, os, sys
REFINE = False
LOOP = False   # 32R-76: the loop lemma merges components like the hub model; off (the RH hub model replaces it)
HUB = True
HUBRH = 'MINMH'   # 32R-76 (independent audit): hub weight -min(m, h) (g_H = 0) / 0 (g_H >= 1); True: m*(g_H-1); False: old -1 (invalid)
HUBLOG = []
CFGLOG = {}
KCOMP = True   # 32R-76: count connected components of the certified subgraph
ASSUME1 = ()   # diagnostic only: hub multiplicities treated as one component
CERT1 = set()   # 32R-76: hubs proved to carry all certified edges on one component (e3h/), set per member by the caller
COLLIDE = True   # 32R-75 (audit round 2): free zeros of B|_v on a multiple sheet may coincide


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        return [[]]
    out = []
    for k in range(min(n, mx), 0, -1):
        for p in partitions(n - k, k):
            out.append([k] + p)
    return out


def parse(t):
    comps = {}
    for m in re.finditer(r'^COMP\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)', t, re.M):
        ia, dg, mu, ge = map(int, m.groups())
        comps[('C', ia)] = dict(deg=dg, m=mu, g=max(0, ge))
    nodes = {}
    for m in re.finditer(r'^NODE\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+comps\s*([\d ]*)$', t, re.M):
        jj, pd, e, lok = map(int, m.groups()[:4])
        nodes[jj] = dict(e=e, lok=lok, comps=[int(x) for x in m.group(5).split()], pdeg=pd)
    cross = []
    for m in re.finditer(r'^CROSS\s+(\d+)\s+(\d+)\s+pdeg\s+(\d+)\s+len\s+(\d+)\s+on\s+([\d ]*?)\s+basept\s+(\d)', t, re.M):
        a, b, pd, ln = map(int, m.groups()[:4])
        cross.append(dict(a=a, b=b, pdeg=pd, len=ln, on=[int(x) for x in m.group(5).split()], bp=int(m.group(6))))
    badc = {int(a): v for a, v in re.findall(r'^BADC\s+(\d+)\s+(\S+)', t, re.M)}
    bade = {int(a): v for a, v in re.findall(r'^BADE\s+(\d+)\s+(\S+)', t, re.M)}
    badx = {}
    cnt = collections.Counter()
    for m in re.finditer(r'^BADX\s+(\d+)\s+(\d+)\s+(\d+)\s+(base|pt)\s+(\S+)(?:\s+(\S+))?', t, re.M):
        a, b = int(m.group(1)), int(m.group(2))
        s = set(m.group(5).split(',')) | (set(m.group(6).split(',')) if m.group(6) else set())
        badx[(a, b, cnt[(a, b)])] = s - {'NONE'}
        cnt[(a, b)] += 1
    badn = {}
    for m in re.finditer(r'^BADN\s+(\d+)\s+(\d+)\s+(\S+)', t, re.M):
        badn[('N', int(m.group(1)), int(m.group(2)))] = set(m.group(3).split(',')) - {'NONE'}
    badx.update(badn)
    return comps, nodes, cross, badc, bade, badx


def cover(m, gbase, ords):
    """cyclic m-cover v^m = f of a genus-gbase curve; ords = nonzero orders of f. Returns (components, genus each)."""
    c = math.gcd(m, *ords) if ords else m
    d = m // c
    r = sum(d - math.gcd(d, o // c) for o in ords)
    return c, (2 + d * (2 * gbase - 2) + r) // 2


def analyze(t, pencil=False, multi=False):
    comps, nodes, cross, badc, bade, badx = parse(t)
    flags = []
    V = dict(comps)
    for jj, nd in nodes.items():
        if nd['e'] > 0:
            V[('E', jj)] = dict(deg=0, m=nd['e'], g=0)
        if nd['pdeg'] != 1:
            flags.append(f'node pdeg {jj}')
        if nd['lok'] != 1 and nd['e'] > 0:
            flags.append(f'node tangency {jj}')
    inc = []
    for jj, nd in nodes.items():
        if nd['e'] > 0:
            for c in nd['comps']:
                inc.append(dict(u=('E', jj), w=('C', c), key=('N', jj, c)))
    cc = collections.Counter()
    for cr in cross:
        if len(cr['on']) > 2:
            flags.append(f'triple {cr["on"]}')
        if cr['len'] != 1 or cr['pdeg'] != 1:
            flags.append(f'crossing {cr["a"]},{cr["b"]} len {cr["len"]} pdeg {cr["pdeg"]}')
        k = (cr['a'], cr['b'], cc[(cr['a'], cr['b'])])
        cc[(cr['a'], cr['b'])] += 1
        inc.append(dict(u=('C', cr['a']), w=('C', cr['b']), key=k))
    xg = {}
    for v, d in V.items():
        if v[0] == 'C':
            s = d['m'] * (2 * d['g'] - 2 - d['deg']) + sum(nd['e'] for nd in nodes.values() if v[1] in nd['comps'])
            for cr in cross:
                if v[1] == cr['a']:
                    s += V[('C', cr['b'])]['m'] * cr['len']
                if v[1] == cr['b']:
                    s += V[('C', cr['a'])]['m'] * cr['len']
        else:
            nd = nodes[v[1]]
            s = -2 * nd['e'] + sum(V[('C', c)]['m'] for c in nd['comps'])
        xg[v] = s
    if any(s < 0 for s in xg.values()):
        flags.append('negative x.Gamma')
    triv = [v for v in V if xg[v] == 0]
    sheets = [v for v in V if xg[v] > 0]
    par = {v: v for v in triv}

    def f(v):
        while par[v] != v:
            par[v] = par[par[v]]
            v = par[v]
        return v
    for e in inc:
        if e['u'] in par and e['w'] in par:
            par[f(e['u'])] = f(e['w'])

    def badset(v):
        return set((badc if v[0] == 'C' else bade).get(v[1], 'NONE').split(',')) - {'NONE'}
    cfg = {}
    for v in triv:
        cfg.setdefault(f(v), []).append(v)
    cbad = {}
    for r, mem in cfg.items():
        bs = [badset(v) for v in mem]
        u = set().union(*bs)
        if (not multi) and (len(u) > 1 or (u and any(not b for b in bs))):
            flags.append(f'config dirs {sorted(u)}')
        for v in mem:
            cbad[v] = u
    for v in sheets:
        cbad[v] = badset(v)

    def vbad(x, lam):
        return lam in cbad[x] or 'ALL' in cbad[x]

    def ok_edge_dir(e, lam):
        u, w = e['u'], e['w']
        for x in (u, w):
            if x in par and vbad(x, lam):
                return False
        if u in par or w in par:
            return True        # touches a good x-trivial configuration: b is a nonzero constant there
        if e['key'] is None or (e['key'][0] == 'N' and e['key'] not in badx):
            return False       # E-sheet / curve-sheet incidence at a node: direction not computed
        bs = badx.get(e['key'], {'*'})
        return not ('*' in bs or 'ALL' in bs or lam in bs)
    dirs = set()
    for v in V:
        dirs |= cbad[v]
    for b in badx.values():
        dirs |= b
    dirs -= {'ALL', '*'}
    cands = ['B'] if pencil else (sorted(dirs) + ['generic'])

    def bound(lam):
        return max(bound_core(lam, False), bound_core(lam, True) if HUB else -99)

    def bound_core(lam, hub):
        vert = {}
        removed = set()
        for v, d in V.items():
            mu = d['m']
            if vbad(v, lam):
                # hub model: multiplicity-1 pieces of a bad configuration stay good (W vanishes on Z, mu != 0);
                # a multiple component of a bad configuration is one hub vertex of genus >= 0
                if hub and v in par:
                    vert[v] = (1, d['g']) if mu == 1 else ('HUB',)
                else:
                    vert[v] = None
                continue
            incid = [i for i, e in enumerate(inc) if v in (e['u'], e['w'])]
            nb = {i: (inc[i]['w'] if inc[i]['u'] == v else inc[i]['u']) for i in incid}
            if mu == 1:
                vert[v] = (1, d['g'])
                continue
            if xg[v] == 0:
                vert[v] = cover(mu, d['g'], [V[nb[i]]['m'] for i in incid])
                continue
            # multiple sheet: s = B|_v has xg[v] zeros; forced at incidences with bad configurations, rest worst case
            forced = [i for i in incid if nb[i] in par and vbad(nb[i], lam)]
            rest = xg[v] - len(forced)
            if rest < 0:
                vert[v] = None
                continue
            best = None
            for combo in itertools.combinations_with_replacement(incid + ['free'], rest):
                sz = collections.Counter(combo)
                for i in forced:
                    sz[i] += 1
                # 32R-75: free zeros (off the incidences) may collide with each other -> all partitions
                for part in (partitions(sz['free']) if COLLIDE else [[1] * sz['free']]):
                    o2 = [sz[i] - V[nb[i]]['m'] for i in incid] + list(part)
                    o2 = [abs(o) for o in o2 if o != 0]
                    c, gp = cover(mu, d['g'], o2)
                    lost = sum(math.gcd(mu, V[nb[i]]['m']) for i in incid if sz[i] > 0)
                    score = c * gp - c - lost
                    if best is None or score < best[0]:
                        best = (score, c, gp, [i for i in incid if sz[i] > 0])
            vert[v] = (best[1], best[2])
            removed |= set(best[3])
        tot = 0 if KCOMP else 1
        EL = []
        if hub:
            for v, vv in vert.items():
                if vv == ('HUB',):
                    vert[v] = (V[v]['m'], V[v]['g']) if HUBRH else (1, 0)
            # hub edges: hub x multiplicity-1 neighbour (connector lemma); mult-1(bad Z) x mult-1 (W in (y) or (xy))
            hubset = {v for v in V if v in par and vbad(v, lam) and V[v]['m'] > 1}
            badset = {v for v in V if v in par and vbad(v, lam)}
            hcount = {}
            for i, e in enumerate(inc):
                u, w = e['u'], e['w']
                if not (vert.get(u) and vert.get(w)):
                    continue
                if (u in badset or w in badset):
                    mu_u, mu_w = V[u]['m'], V[w]['m']
                    if (u in hubset and mu_w == 1) or (w in hubset and mu_u == 1) or (mu_u == 1 and mu_w == 1):
                        tot += 1
                        EL.append((u, w))
                        for x in (u, w):
                            if x in hubset:
                                hcount[x] = hcount.get(x, 0) + 1
            # 32R-76: components of the cover over a hub H carrying no certified edge are left out of the subgraph;
            # each remaining component has genus >= g(H), so the hub weight is -min(m, h) (g(H) = 0) or >= 0 (g(H) >= 1)
            if HUBRH == 'MINMH':
                for v in hubset:
                    if vert.get(v):
                        h = hcount.get(v, 0)
                        vert[v] = (min(V[v]['m'], h), 0) if V[v]['g'] == 0 else (1, 1)
                        if (V[v]['m'] in ASSUME1 or v in CERT1) and V[v]['g'] == 0:
                            vert[v] = (1, 0)
                        HUBLOG.append((lam, v, V[v]['m'], V[v]['g'], h, [ (e['u'] if e['w'] == v else e['w']) for e in inc if v in (e['u'], e['w']) and V[e['w'] if e['u'] == v else e['u']]['m'] == 1 and vert.get(e['w'] if e['u'] == v else e['u'])]))
            # hubs with no multiplicity-1 neighbour are dropped again
            for v in hubset:
                if not any(((e['u'] == v and V[e['w']]['m'] == 1 and vert.get(e['w'])) or (e['w'] == v and V[e['u']]['m'] == 1 and vert.get(e['u']))) for e in inc):
                    vert[v] = None
        if LOOP and not hub:
            # loop lemma: a bad configuration Z contributes >= b1 of the graph on its components whose edges are the
            # incidences with at least one multiplicity-1 endpoint (multiple components act as hubs)
            done = set()
            for v in V:
                if v in par and vbad(v, lam):
                    r0 = f(v)
                    if r0 in done:
                        continue
                    done.add(r0)
                    memb = [x for x in V if x in par and f(x) == r0]
                    ms = set(memb)
                    ne = sum(1 for e in inc if e['u'] in ms and e['w'] in ms and (V[e['u']]['m'] == 1 or V[e['w']]['m'] == 1))
                    # number of connected components of that graph
                    pp = {x: x for x in memb}
                    def ff(x):
                        while pp[x] != x:
                            pp[x] = pp[pp[x]]
                            x = pp[x]
                        return x
                    for e in inc:
                        if e['u'] in ms and e['w'] in ms and (V[e['u']]['m'] == 1 or V[e['w']]['m'] == 1):
                            pp[ff(e['u'])] = ff(e['w'])
                    ncomp = len({ff(x) for x in memb})
                    tot += max(0, ne - len(memb) + ncomp)
        for v, vv in vert.items():
            if vv:
                tot += vv[0] * vv[1] - vv[0]
        for i, e in enumerate(inc):
            if i in removed:
                continue
            okd = ok_edge_dir(e, lam)
            if REFINE and not okd and vert[e['u']] and vert[e['w']]:
                bz = [x for x in (e['u'], e['w']) if x in par and vbad(x, lam)]
                if bz and V[e['u']]['m'] == 1 and V[e['w']]['m'] == 1:
                    other = [x for x in (e['u'], e['w']) if x not in bz]
                    # both in the bad configuration, or bad-config component x sheet: B_lead vanishes on Z only, b = mu != 0
                    if not other or (other[0] not in par):
                        okd = True if (not other or e['key'] is None or True) else okd
            if vert[e['u']] and vert[e['w']] and okd:
                tot += math.gcd(V[e['u']]['m'], V[e['w']]['m'])
                EL.append((e['u'], e['w']))
        if KCOMP:
            # 32R-76: g >= sum g_v + b1(G') and b1 = E - V + (number of connected components of G')
            pk = {v: v for v, vv in vert.items() if vv}
            def fk(x):
                while pk[x] != x:
                    pk[x] = pk[pk[x]]
                    x = pk[x]
                return x
            for u, w in EL:
                if u in pk and w in pk:
                    pk[fk(u)] = fk(w)
            tot += max(1, len({fk(v) for v in pk}))
        return tot
    CFGLOG.clear(); CFGLOG.update(dict(V=V, cfg=cfg, inc=inc, cbad=cbad))
    res = {lam: bound(lam) for lam in cands}
    return dict(worst=min(res.values()), allgood=bound('__none__'), perdir=res, flags=flags, sheets=len(sheets))


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'nets':
        for fn in sorted(glob.glob('gph/g_*.out')):
            nm = os.path.basename(fn)[2:-4]
            t = open(fn).read() + open(f'gph2/h_{nm}.out').read()
            r = analyze(t)
            print(nm, r['allgood'], r['worst'], r['flags'][:2])
    elif mode == 'm16':
        C = collections.Counter()
        rows = []
        for fn in sorted(glob.glob('m16/m_*.out')):
            nm = os.path.basename(fn)[:-4]
            t = open(fn).read()
            if 'END' not in t:
                st = 'NOMEMBER' if 'NO-UNIQUE-MEMBER' in t else 'UNFINISHED'
                C[st] += 1
                rows.append((nm, st))
                continue
            sg = int(re.search(r'SIGMAG\s+(-?\d+)', t).group(1))
            hh = int(re.search(r'^HH\s+(\d+)', t, re.M).group(1))
            if sg >= 2:
                C['LEMMA-G'] += 1
                rows.append((nm, 'LEMMA-G', sg))
                continue
            if hh >= 4:
                C['WEB'] += 1
                rows.append((nm, 'WEB'))
                continue
            r = analyze(t, pencil=(hh == 2))
            st = 'FLAG' if r['flags'] else ('OK' if r['worst'] >= 2 else 'LOW')
            C[st] += 1
            rows.append((nm, st, r['worst'], r['allgood'], r['flags'][:3]))
        print(dict(C))
        for r in rows:
            if r[1] in ('FLAG', 'LOW', 'UNFINISHED'):
                print(r)
        json.dump(rows, open('m16/an2.json', 'w'), default=str)
