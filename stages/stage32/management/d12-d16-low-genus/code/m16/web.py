import re, glob, os, random, sys, collections, json
sys.path.insert(0, 'm16'); import an2
P = 10009
def parse_k(s):
    if s == 'NNOUT': return None
    m = re.match(r'K(\d+)((?::[^:]+)*)$', s); d = int(m.group(1))
    vecs = [tuple(int(x) % P for x in v.split(',')) for v in m.group(2).split(':')[1:]]
    return d, vecs
def rank(vs):
    M = [list(v) for v in vs]; r = 0; n = 3
    for c in range(n):
        piv = next((i for i in range(r, len(M)) if M[i][c] % P), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]; inv = pow(M[r][c], P - 2, P)
        M[r] = [x * inv % P for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]: M[i] = [(a - M[i][c] * b) % P for a, b in zip(M[i], M[r])]
        r += 1
    return r
def inspace(t, sp):
    d, vecs = sp
    if d == 3: return True
    if d == 0: return False
    return rank(vecs + [t]) == rank(vecs)
def cross(a, b): return ((a[1]*b[2]-a[2]*b[1]) % P, (a[2]*b[0]-a[0]*b[2]) % P, (a[0]*b[1]-a[1]*b[0]) % P)
def run(fn):
    t = open(fn).read()
    vals = re.findall(r'^(BADC|BADE)\s+(\d+)\s+(\S+)', t, re.M) + [(None, None, v) for v in re.findall(r'^BADN\s+\d+\s+\d+\s+(\S+)', t, re.M)] + [(None, None, v) for v in re.findall(r'^BADX\s+\d+\s+\d+\s+\d+\s+(?:base|pt)\s+(\S+)', t, re.M)] \
         + [(None, None, v) for v in re.findall(r'^BADX\s+\d+\s+\d+\s+\d+\s+base\s+\S+\s+(\S+)', t, re.M)]
    spaces = {}
    for _, _, v in vals:
        if v not in spaces: spaces[v] = parse_k(v)
    if any(s is None for s in spaces.values()): return None, 'NNOUT'
    lines = [s for s in spaces.values() if s[0] == 2]; pts = [s for s in spaces.values() if s[0] == 1]
    rnd = random.Random(7)
    cands = [tuple(rnd.randrange(P) for _ in range(3))]
    cands += [s[1][0] for s in pts]
    normals = []
    for d, vecs in lines:
        nrm = cross(vecs[0], vecs[1]); normals.append(nrm)
        a, b = rnd.randrange(P), rnd.randrange(P); cands.append(tuple((a * x + b * y) % P for x, y in zip(*vecs)))
    for i in range(len(normals)):
        for j in range(i + 1, len(normals)):
            c = cross(normals[i], normals[j])
            if any(c): cands.append(c)
    cands = list(dict.fromkeys(cands))
    lab = {c: f'w{k}' for k, c in enumerate(cands)}
    def lbl(v):
        sp = spaces[v]
        if sp[0] == 3: return 'ALL'
        bad = [lab[c] for c in cands if inspace(c, sp)]
        return ','.join(bad) if bad else 'NONE'
    t = re.sub(r'^(BADN\s+\d+)(\s+\d+\s+)(\S+)', lambda m: m.group(1) + m.group(2) + m.group(3), t, flags=re.M)
    t2 = re.sub(r'^(BADC|BADE)(\s+\d+\s+)(\S+)', lambda m: m.group(1) + m.group(2) + lbl(m.group(3)), t, flags=re.M)
    def subx(m):
        rest = m.group(2).split()
        return m.group(1) + ' ' + ' '.join(lbl(x) for x in rest)
    t2 = re.sub(r'^(BADX\s+\d+\s+\d+\s+\d+\s+(?:base|pt))\s+(.*)$', subx, t2, flags=re.M)
    t2 = re.sub(r'^(BADN\s+\d+\s+\d+)\s+(\S+)$', lambda m: m.group(1) + ' ' + lbl(m.group(2)), t2, flags=re.M)
    return t2, len(cands)
C = collections.Counter(); out = []
for fn in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else 'm16/w_*.out')):
    nm = os.path.basename(fn)[:-4]
    t2, nc = run(fn)
    if t2 is None: C['NNOUT'] += 1; out.append((nm, 'NNOUT')); continue
    if 'END' not in t2: C['UNFIN'] += 1; out.append((nm, 'UNFIN')); continue
    r = an2.analyze(t2, multi=True)
    st = 'FLAG' if r['flags'] else ('OK' if r['worst'] >= 2 else 'LOW')
    C[st] += 1; out.append((nm, st, r['worst'], r['allgood'], nc, r['flags'][:2]))
print(dict(C))
for o in out:
    if o[1] != 'OK': print(o)
json.dump(out, open('m16/web.json', 'w'))
