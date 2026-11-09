"""Fast Lemma G for 4 pencil member jobs without a cg result: the sx member, the 92 known-curve ideals Q1..Q92 (taken
from a d16all lg script), known curves removed by saturation, then tail_fast_v2 with a plane-image irreducibility check
(as d16all/mklg.py).  usage (from stoll/): python p16all/mklg.py"""
T = open('gfast/tail_fast_v2.sing').read()
src = open('d16all/mklg.py').read()
PRE = src.split("PRE = '''")[1].split("'''")[0].replace('\\\\"', '\\"')
k = T.index("if (size(Fq) != 1"); k = T.index("\n", k) + 1
FACT = 'list FFR = factorize(Fp[1]); if (size(FFR[1]) - 1 >= 2 || FFR[2][size(FFR[1])] >= 2) { "LG-REMAINDER-REDUCIBLE plane factors", size(FFR[1]) - 1; quit; } "LG-REMAINDER-INTEGRAL";\n'
TAIL = T[:k] + FACT + T[k:]
lg = open('d16all/h1/lg_6.sing').read()
qdefs = '\n'.join(l for l in lg.split('\n') if l.startswith('ideal Q') and '= std(S + ideal(' in l)
assert qdefs.count('ideal Q') == 92
J = ['sx_2652_4', 'sx_2707_4', 'sx_2707_8', 'sx_44_4']
for j in J:
    s = open(f'p16all/{j}.sing').read(); kk = s.index("if (mult(Bp) < ")
    open(f'p16all/lg_{j}.sing', 'w', newline='\n').write(s[:kk] + qdefs + '\n' + PRE + TAIL + '\nquit;\n')
open('p16all/lgjobs.txt', 'w', newline='\n').write('\n'.join('lg_' + j for j in J) + '\n')
