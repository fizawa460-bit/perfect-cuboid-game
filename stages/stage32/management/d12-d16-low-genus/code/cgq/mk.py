import sys,os,re
ARGS=sys.argv[1:]
g={}; sys.argv=['x']
exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], g)
CURVES=g['CURVES']
t='"residual degree", mult(Bp);\nlist KL;\n'
for k in range(1,93):
    t+=f'KL[{k}] = satur(std(S + ideal({",".join(CURVES[k-1])})), MX);\n'
t+='ideal Q = Bp; int kk; def LQ;\n'
t+='for (kk = 1; kk <= 92; kk++) { if (size(reduce(Bp, std(KL[kk]))) == 0) { LQ = sat(Q, KL[kk]); if (typeof(LQ) == "list") { Q = std(LQ[1]); } else { Q = std(LQ); } kill LQ; def LQ; "CONTAINS", kk, " deg", mult(std(KL[kk])), " left dim", dim(Q), " deg", mult(Q); } }\n'
t+='if (dim(Q) <= 1) { "ALLKNOWN"; } else { "UNKNOWN-REMAINS degree", mult(Q); }\nquit;\n'
names=[]
for f in ARGS:
    s=open(f).read(); key='list MA = minAssGTZ(Bp);'
    n='q_'+os.path.basename(f)[:-5]
    open('cgq/'+n+'.sing','w',newline='\n').write(s[:s.index(key)]+t); names.append(n)
open('cgq/jobs.txt','w',newline='\n').write('\n'.join(names)+'\n'); print(len(names))
