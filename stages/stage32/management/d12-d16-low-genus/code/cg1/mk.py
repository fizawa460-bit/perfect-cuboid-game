import sys, os, json
sys.path.insert(0, os.path.abspath('fasth0'))
import script_v2 as SV

TAIL=open('cg/mk.py').read().split("TAIL='''")[1].split("'''")[0]
H=json.load(open('fasth0/d16v2f_h0.json')); C=json.load(open('fasth0/d16v2f_cont.json'))
red=[k for k,v in C.items() if v]
lim=int(sys.argv[1]) if len(sys.argv)>1 else None
names=[]
for k in red[:lim]:
    m,h,D=H[k]; s=SV.script(D,m)
    key='"base locus outside D\'s curves'
    s=s[:s.index(key)]+'if (dim(Bp) != 2) { "residual not a curve"; quit; }\n'+TAIL
    n=f'c1_{k}'; open(f'cg1/{n}.sing','w',newline='\n').write(s); names.append(n)
open('cg1/jobs.txt','w',newline='\n').write('\n'.join(names)+'\n'); print(len(names))
