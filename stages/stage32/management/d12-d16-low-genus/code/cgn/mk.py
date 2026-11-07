import glob,os,re
TAIL=open('cg/mk.py').read().split("TAIL='''")[1].split("'''")[0]
names=[]
for o in sorted(glob.glob('n16/r_*.out')+glob.glob('n16/rl_*.out')+glob.glob('n16/dm/dm_*.out')+glob.glob('n16/dm/rd_*.out')):
    t=open(o,errors='replace').read()
    if not re.search(r'RESIDUAL-REDUCIBLE|RESIDUAL-NONREDUCED|MEMBER-REDUCIBLE|MEMBER-NONREDUCED',t): continue
    s=open(o[:-4]+'.sing').read(); key='if (mult(Bp) < 16)'
    if key not in s: print('nokey',o); continue
    n='gn_'+os.path.basename(o)[:-4]
    open('cgn/'+n+'.sing','w',newline='\n').write(s[:s.index(key)]+TAIL); names.append(n)
open('cgn/jobs.txt','w',newline='\n').write('\n'.join(names)+'\n'); print(len(names))
