"""32R-75: the 2-Gamma families of the d=16 net D-check (32R-72), redone with Lemma G.
For each (job, line Q) from n16/fam/h_<job>.out (A: contains (m+1)Gamma), build
  famg/f_<job>_<k>.sing : generic member of the pencil I(D + Gamma) (components, genera, bad directions; m16 tail)
  famg/c_<job>_<k>.sing : critical scheme of the pencil off base locus and nodes, fibre factors (famc tail)
Header = the D-check preamble of n16/d_<job>.sing (same decomposition, same random basis FL, seed 2718)."""
import re, glob, os, json
NL = '\n'
ftail = open('fam/f_28246_121.sing').read(); ftail = ftail[ftail.index('// find the member(s) in J'):]
ctail = open('famc/c_28246_121.sing').read(); ctail = ctail[ctail.index('string TAG'):]; ctail = ctail[ctail.index(NL) + 1:]
fams = {}
for f in sorted(glob.glob('n16/fam/h_*.out')):
    job = os.path.basename(f)[2:-4]
    if job.startswith('27685s'): continue          # mu = 16 class: M7
    cur = None
    for line in open(f):
        m = re.match(r'== family (\S+) (G\d+) m=(\d) Q=(.*)', line)
        if m: cur = (m.group(2), int(m.group(3)), m.group(4).strip()); continue
        if cur and 'contains (m+1)Gamma' in line:
            fams.setdefault((job, cur[2]), [])
            if (cur[0], cur[1]) not in fams[(job, cur[2])]: fams[(job, cur[2])].append((cur[0], cur[1]))
jobs = []; meta = {}
cnt = {}
for (job, q), gl in fams.items():
    k = cnt.get(job, 0); cnt[job] = k + 1
    src = open(f'n16/d_{job}.sing').read()
    i = src.index('list FL; for (kk = 1; kk <= HH;'); head = src[:src.index(NL, i) + 1]
    mult = {}
    for mm in re.finditer(r'ideal (G\d+)(p*) = ', head):
        mult[mm.group(1)] = max(mult.get(mm.group(1), 1), 1 + len(mm.group(2)))
    kk = head.index('ideal Iall = '); names = re.findall(r'(G\d+)p*', head[kk:head.index(NL, kk)])
    h = head + 'ideal NODES = std(S + minor(jacob(S), 4));' + NL
    h += 'ideal Dc = std(' + (('intersect(' + ','.join(names) + ')') if len(names) > 1 else names[0]) + ');' + NL
    h += 'list DL; intvec DLc;' + NL + ''.join(f'DL[{i+1}] = {n}; DLc[{i+1}] = {mult[n]};' + NL for i, n in enumerate(names))
    h += 'proc ordP(poly F, ideal P) { int k = 0; int mm2; for (mm2 = 1; mm2 <= 6; mm2++) { if (size(reduce(F, satur(std(S + P^mm2), MX))) == 0) { k = mm2; } else { break; } } return(k); }' + NL
    J = ' ideal J = ideal(1);'
    for g, m in gl:
        J += f' J = intersect(J, satur(satur(std(S + {g}^{mult[g] + 1}), NODES), MX));'
    h += J + ' J = std(J); ideal J1 = J;' + NL
    tag = f'{job}_{k}'
    meta[tag] = {'job': job, 'Q': q, 'Gammas': gl}
    open(f'famg/f_{tag}.sing', 'w', newline=NL).write(h + f'string TAG = "{tag}";' + NL + ftail)
    open(f'famg/c_{tag}.sing', 'w', newline=NL).write(h + f'string TAG = "{tag}";' + NL + ctail)
    jobs += [f'f_{tag}', f'c_{tag}']
open('famg/jobs.txt', 'w', newline=NL).write(NL.join(jobs) + NL)
json.dump(meta, open('famg/meta.json', 'w'), indent=1)
print(len(meta), 'families'); [print(t, v['Gammas'], v['Q']) for t, v in meta.items()]
