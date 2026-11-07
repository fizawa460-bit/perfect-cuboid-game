import sys,os,glob,re
ARGS=sys.argv[1:]
g={}; sys.argv=['x']
exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], g)
CURVES=g['CURVES']
def known_tail():
    t='list MA = minAssGTZ(Bp); int ia; int found; ideal KK;\n'
    t+='ideal RB = std(radical(Bp)); "RADICAL degree", mult(RB), " scheme degree", mult(Bp);\n'
    t+='list KL;\n'
    for k in range(1,93):
        t+=f'KL[{k}] = satur(std(S + ideal({",".join(CURVES[k-1])})), MX);\n'
    t+='int kk;\nfor (ia = 1; ia <= size(MA); ia++) { ideal QA = std(MA[ia]); if (dim(QA) == 2) { found = 0;\n'
    t+='  for (kk = 1; kk <= 92 && found == 0; kk++) { KK = KL[kk]; if (mult(KK) == mult(QA)) { if (size(reduce(QA, std(KK))) == 0 && size(reduce(KK, QA)) == 0) { found = kk; } } }\n'
    t+='  "KCOMP degree", mult(QA), " known", found; } kill QA; }\n"KDONE";\nquit;\n'
    return t
T=known_tail(); names=[]
for f in ARGS:
    s=open(f).read(); key='list MA = minAssGTZ(Bp);'
    n='k_'+os.path.basename(f)[:-5]
    open('cgk/'+n+'.sing','w',newline='\n').write(s[:s.index(key)]+T); names.append(n)
open('cgk/jobs.txt','a',newline='\n').write('\n'.join(names)+'\n'); print(len(names))
