import glob,os,re
TAIL=open('cg/mk.py').read().split("TAIL='''")[1].split("'''")[0]
names=[]
for o in sorted(glob.glob('p16/sx_*.out')):
    if 'MEMBER-REDUCIBLE (contains a D-curve)' not in open(o,errors='replace').read(): continue
    s=open(o[:-4]+'.sing').read(); key='if (mult(Bp) < 16)'
    n='cd_'+os.path.basename(o)[3:-4]
    open('cg/'+n+'.sing','w',newline='\n').write(s[:s.index(key)]+TAIL); names.append(n)
open('cg/jobs_sx.txt','w',newline='\n').write('\n'.join(names)+'\n'); print(len(names))
