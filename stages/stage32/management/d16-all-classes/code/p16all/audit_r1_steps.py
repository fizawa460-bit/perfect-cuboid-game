"""Generators used for the answers to the D16-ALL-CLASSES audit round 1 (2026-11-09), as run in the session (each was
first run inline; collected here in function form).  Run from stoll/:  python p16all/audit_r1_steps.py <step>
  rf    : (b) member jobs for every fibre removed whole by the v6 critical tail ('critical curve fibre (removed whole)'),
          Lemma G by components (p16all/rf/rf_<i>_<t>_<u>.sing)
  c0    : (e) print c0 = order of the generic member at the node / curve vs D_k for all 441 scan entries (p16all/c0/)
  idc   : (d) identify every component of the low members (cg_sx, rf, nr) with a known curve (p16all/idc/); the m16
          tail defines an int b1 that shadows the ring variable b1, so 'kill b1;' precedes the known-curve ideals
  sbw   : stage2b members of quadratic factors computed as ONE member over F_p(w) (minpoly = the factor), fast tail
  lgs   : fast Lemma G (known curves removed) for stage2b members without a fast bound >= 2
The (f) check inserted into every T7 job is the block '// audit (f)' visible in p16all/t7/t7_*.sing: F0 and F0 + 7F1
have exactly the D multiplicities DLc along every D-curve, and NN != F0.  The T7 generators for rf / sb members and the
nc generators are mkt7.py / mknc.py with the source and target folders changed (rft7, sbt7, rfnc, sbnc); the
decomposition is plan decs[t] (rf) or decs[0] (sb, whose pencil basis is that of c_<i>_0)."""
import sys, re, glob, os, json

step = sys.argv[1] if len(sys.argv) > 1 else ''


def cg():
    return open("p16all/mkcg.py").read().split("CG = '''")[1].split("'''")[0]


def lg_parts():
    T = open('gfast/tail_fast_v2.sing').read()
    src = open('d16all/mklg.py').read()
    PRE = src.split("PRE = '''")[1].split("'''")[0].replace('\\\\"', '\\"')
    k = T.index("if (size(Fq) != 1")
    k = T.index("\n", k) + 1
    FACT = ('list FFR = factorize(Fp[1]); if (size(FFR[1]) - 1 >= 2 || FFR[2][size(FFR[1])] >= 2) '
            '{ "LG-REMAINDER-REDUCIBLE plane factors", size(FFR[1]) - 1; quit; } "LG-REMAINDER-INTEGRAL";\n')
    lg = open('d16all/h1/lg_6.sing').read()
    qdefs = '\n'.join(l for l in lg.split('\n') if l.startswith('ideal Q') and '= std(S + ideal(' in l)
    return qdefs, PRE, T[:k] + FACT + T[k:]


def dcpart(D):
    cids = sorted(int(x) for x in D if int(x) <= 92)
    if len(cids) > 1:
        return "intersect(" + ",".join(f"G{x}" for x in cids) + ")"
    return f"G{cids[0]}" if cids else "ideal(1)"


if step == 'rf':
    P = json.load(open('p16all/plan.json'))
    os.makedirs('p16all/rf', exist_ok=True)
    MAPF = {}
    for f in sorted(glob.glob('p16all/c_*.out')):
        nm = os.path.basename(f)[:-4]
        _, i, t = nm.split('_')
        t = int(t)
        for fc in re.findall(r'critical curve fibre \(removed whole\): u([+-]\d+)', open(f).read()):
            root = (-int(fc)) % 10009
            src = open(f'p16all/c_{i}_{t}.sing').read()
            kk = src.index('system("random", ')
            pre = src[:kk] + src[kk:].split('\n', 1)[0] + '\n'
            body = pre + f"ideal Dc = std({dcpart(P[i]['decs'][t][1])});\npoly NN = F0 - ({root}) * F1;\n"
            body += ('ideal B = std(S + ideal(NN)); def LL = sat(B, Dc); ideal Bp; if (typeof(LL) == "list") '
                     '{ Bp = std(LL[1]); } else { Bp = std(LL); } kill LL;\n')
            body += f'"removed-fibre member u = {root}; residual dim", dim(Bp), " degree", mult(Bp);\n'
            body += 'LIB "primdec.lib"; LIB "normal.lib";\n' + cg()
            n = f'rf_{i}_{t}_{root}'
            open(f'p16all/rf/{n}.sing', 'w', newline='\n').write(body)
            MAPF[n] = (i, t, root)
    open('p16all/rf/jobs.txt', 'w', newline='\n').write('\n'.join(sorted(MAPF)) + '\n')
    json.dump(MAPF, open('p16all/rf/map.json', 'w'))
elif step == 'c0':
    SC = json.load(open('p16all/scan.json'))
    os.makedirs('p16all/c0', exist_ok=True)
    L = [l.split(chr(9)) for l in open('//wsl.localhost/Ubuntu/root/j16all_new_h0pos.txt').read().split(chr(10))[:-1]]
    rows = []
    for idx, (h, res) in SC.items():
        D = {int(a): int(b) for a, b in (q.split(':') for q in L[int(idx)][2].split()[2].split(','))}
        for k, hh in res:
            n = f'm_{idx}_{k}'
            s = open(f'p16all/nr/{n}.sing').read()
            a = s.index('int c0 = ')
            b = s.index(';', a) + 1
            extra = f'\n"C0", c0, " Dk", {D.get(k, 0)}, " cap", {int(hh == "cap")};\nquit;\n'
            open(f'p16all/c0/{n}.sing', 'w', newline='\n').write(s[:b] + extra)
            rows.append(n)
    open('p16all/c0/jobs.txt', 'w', newline='\n').write('\n'.join(rows) + '\n')
elif step == 'idc':
    qdefs, _, _ = lg_parts()
    os.makedirs('p16all/idc', exist_ok=True)
    ID = qdefs + '''
LIB "primdec.lib";
list MAi = minAssGTZ(Bp); int ia2; int kq2; int nunk = 0; int ncomp = 0;
for (ia2 = 1; ia2 <= size(MAi); ia2++) { ideal QAi = std(MAi[ia2]); if (dim(QAi) == 2) { ncomp++; int hitk = 0;
  for (kq2 = 1; kq2 <= 92; kq2++) { execute("if (hitk == 0) { if (size(reduce(Q" + string(kq2) + ", QAi)) == 0 && mult(std(Q" + string(kq2) + ")) == mult(QAi)) { hitk = " + string(kq2) + "; } }"); }
  "IDCOMP", ia2, " degree", mult(QAi), " known", hitk; if (hitk == 0) { nunk++; } kill hitk; } kill QAi; }
"IDENT components", ncomp, " unknown", nunk; if (nunk == 0) { "ID-ALL-KNOWN"; } else { "ID-HAS-UNKNOWN"; }
quit;
'''
    jobs = []
    for f in sorted(glob.glob('p16all/cg_sx_*.out')) + sorted(glob.glob('p16all/rf/rf_*.out')):
        m = re.search(r'GENUS-SUM (-?\d+)', open(f).read())
        if not m or int(m.group(1)) >= 2:
            continue
        s = open(f[:-4] + '.sing').read()
        k = s.index('LIB "primdec.lib"; LIB "normal.lib";')
        n = 'id_' + os.path.basename(f)[:-4]
        open(f'p16all/idc/{n}.sing', 'w', newline='\n').write(s[:k] + ID)
        jobs.append(n)
    for f in sorted(glob.glob('p16all/nr/m_*.out')):
        if 'END' not in open(f).read():
            continue
        s = open(f[:-4] + '.sing').read()
        key = 'ideal B = std(S + ideal(NN)); ideal Bp = satur(B, Dc);'
        k = s.index(key) + len(key)
        n = 'id_' + os.path.basename(f)[:-4]
        open(f'p16all/idc/{n}.sing', 'w', newline='\n').write(s[:k] + '\nkill b1;\n' + ID)
        jobs.append(n)
    open('p16all/idc/jobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n')
elif step == 'sbw':
    FAST = open("gfast/tail_fast_v2.sing").read()
    jobs = []
    for f in sorted(glob.glob('p16all/sb_*.sing')):
        s = open(f).read()
        m = re.search(r'poly qq = ([^;]*);', s)
        if not m or not re.search(r'u\^([2-9]|\d\d)', m.group(1)):
            continue
        pre = s[:s.index('ring RQ = 10009,(u),dp;')]
        body = pre + 'poly NN = F0 - ww * F1;\n'
        body += ('ideal B = std(S + ideal(NN)); def LL = sat(B, Dc); ideal Bp; if (typeof(LL) == "list") '
                 '{ Bp = std(LL[1]); } else { Bp = std(LL); } kill LL;\n')
        body += '"special member over F_p(w): residual dim", dim(Bp), " degree", mult(Bp), " expected 16";\n'
        body += 'if (mult(Bp) < 16) { "MEMBER-REDUCIBLE (contains a D-curve)"; quit; }\nif (dim(Bp) != 2) { "MEMBER-NOT-CURVE"; quit; }\n' + FAST
        fac = m.group(1).replace('u', 'ww')
        body = re.sub(r"ring (\w+) = 10009,(\([^)]*\)),dp;",
                      lambda mm: f"ring {mm.group(1)} = (10009,ww),{mm.group(2)},dp; minpoly = {fac};", body)
        n = 'sbw_' + os.path.basename(f)[3:-5]
        open(f'p16all/{n}.sing', 'w', newline='\n').write(body)
        jobs.append(n)
    open('p16all/sbwjobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n')
elif step == 'lgs':
    qdefs, PRE, TAIL = lg_parts()
    jobs = []
    for f in sorted(glob.glob('p16all/sb_*.out')):
        t = open(f).read()
        b = os.path.basename(f)[3:-4]
        if os.path.exists(f'p16all/sbw_{b}.sing'):
            continue
        mg = re.search(r"FASTGENUS (?:lower bound )?(-?\d+)", t)
        mk = re.search(r"k (\d+)\s+residual", t)
        if mg and mk and int(mk.group(1)) == 1 and int(mg.group(1)) >= 2 and 'REDUCIBLE' not in t:
            continue
        s = open(f[:-4] + '.sing').read()
        kk = s.index('if (mult(Bp) < 16 * kq)')
        open(f'p16all/lgs_{b}.sing', 'w', newline='\n').write(s[:kk] + qdefs + '\n' + PRE + TAIL + '\nquit;\n')
        jobs.append('lgs_' + b)
    open('p16all/lgsjobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n')
else:
    print(__doc__)
