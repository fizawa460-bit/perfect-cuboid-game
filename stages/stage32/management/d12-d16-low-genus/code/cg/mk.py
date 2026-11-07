import glob,os,sys
TAIL='''list MA = minAssGTZ(Bp); int ia; int GS = 0; int GL;
for (ia = 1; ia <= size(MA); ia++) { ideal QA = std(MA[ia]); if (dim(QA) == 2) { intvec HQ = hilbPoly(QA); int paq = 1 - HQ[1];
  if (mult(QA) <= 2 || paq <= 0) { GL = 0; } else { GL = genus(QA); }
  "COMP degree", mult(QA), " pa", paq, " genus", GL; if (GL > 0) { GS = GS + GL; } kill HQ; kill paq; } kill QA; }
"GENUS-SUM", GS;
quit;
'''
names=[]
for f in sorted(glob.glob('p16/scx_*.sing')):
    s=open(f).read(); key='list MA = minAssGTZ(Bp);'
    if key not in s: print('skip',f); continue
    n='cg_'+os.path.basename(f)[4:-5]
    open('cg/'+n+'.sing','w').write(s[:s.index(key)]+TAIL); names.append(n)
open('cg/jobs.txt','w').write('\n'.join(names)+'\n'); print(len(names))
