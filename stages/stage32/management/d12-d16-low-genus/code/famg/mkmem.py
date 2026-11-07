import json, re
spec = json.load(open('famg/special.json')); R = json.load(open('famg/milp2.json'))
SKIP = {'28246_0_0', '28246_2_0', '28255_0_1', '28255_1_0', '28255_2_0', '27988_0_0', '27988_1_0'}
xs = open('famd/x_28246_121.sing').read()
KL = {int(k): v for k, v in re.findall(r'KL\[(\d+)\] = (satur\(std\(S \+ ideal\([^;]*\)\), MX\));', xs)}
ordp = 'proc ordP(poly F, ideal P) { int k = 0; int mm2; for (mm2 = 1; mm2 <= 6; mm2++) { if (size(reduce(F, satur(std(S + P^mm2), MX))) == 0) { k = mm2; } else { break; } } return(k); }\n'
jobs = []
for tag, v in spec.items():
    if tag in SKIP: continue
    f = open(f'famg/f_{tag}.sing').read()
    a = f.index('system("random", 9137); number rr = random(1, 9999);')
    b = f.index('ideal R1;', a)
    for u in v['1']:
        s = f[:a] + 'poly NN = 0; for (kk = 1; kk <= HH; kk++) { NN = NN + (number(v1[kk]) - ' + u + ' * number(v2[kk])) * FL[kk]; }\n' + f[b:]
        n = f's1_{tag}_{u}'; open(f'famg/{n}.sing', 'w', newline='\n').write(s); jobs.append(n)
    # rep 2
    r = open(f'famg/r_{tag}.sing').read(); head = r[:r.index('ideal BL = ')]
    D2 = {int(k): c for k, c in R[tag]['alt']['D2'].items()}; cur = sorted(k for k in D2 if k <= 92)
    h = head + 'ideal NODES = std(S + minor(jacob(S), 4)); int HH = 2; list FL; FL[1] = F0; FL[2] = F1; int kk; int ii;\n'
    h += 'ideal Dc = std(' + ('intersect(' + ','.join(f'G{c}' for c in cur) + ')' if len(cur) > 1 else f'G{cur[0]}') + ');\n'
    h += 'list DL; intvec DLc;\n' + ''.join(f'DL[{i+1}] = G{c}; DLc[{i+1}] = {D2[c]};\n' for i, c in enumerate(cur)) + ordp
    t = f[b:]
    for u in v['2']:
        s = h + f'poly NN = F0 - {u} * F1; ideal J1 = std(S); int js;\n' + t
        n = f's2_{tag}_{u}'; open(f'famg/{n}.sing', 'w', newline='\n').write(s); jobs.append(n)
open('famg/sjobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n'); print(len(jobs))
