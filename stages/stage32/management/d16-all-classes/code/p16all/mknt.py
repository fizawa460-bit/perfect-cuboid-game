"""Direct node version (R2 p16/nt_*.sing, 32R-69k) for the node jobs of p16all with 'NODE-OPEN: ramification not finite'
(n_1778_121_{1,2}, n_847_97_{1,2}).  The n_ job is kept up to its YF check (the moving part meets no fixed point); the
ramification step is replaced by the direct computation of the singular points of the members on E, taken verbatim from
lines 62- of R2's p16/nt_27522_122_1.sing (copied to code/p16all/R2_nt_template_27522_122_1.sing), with
cE = multiplicity of the node in decomposition 0 (the template's 'int cE = 1;'; the division by s^cE is checked by the
template, a failure prints NODE-OPEN).  usage (from stoll/): python p16all/mknt.py"""
import json, glob, re

plan = json.load(open('p16all/plan.json'))
TPL = open('p16/nt_27522_122_1.sing').read().split('\n')
tail = '\n'.join(TPL[61:])                     # lines 62- of the template
assert tail.startswith('int cE = 1;'), tail[:40]
jobs = []
for f in sorted(glob.glob('p16all/n_*.out')):
    if 'NODE-OPEN: ramification not finite' not in open(f).read():
        continue
    b = re.match(r'.*n_(\d+_\d+_\d)\.out$', f.replace('\\', '/')).group(1)
    i, k, ch = b.split('_')
    cE = plan[i]['decs'][0][1].get(k, 0)
    s = open(f'p16all/n_{b}.sing').read().split('\n')
    k61 = [n for n, l in enumerate(s) if l.startswith('ideal YF = std(YM + DF);')][0]
    open(f'p16all/nt_{b}.sing', 'w', newline='\n').write('\n'.join(s[:k61 + 1]) + '\n' + tail.replace('int cE = 1;', f'int cE = {cE};'))
    jobs.append(f'nt_{b}')
    print(b, 'cE', cE)
open('p16all/ntjobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n')
