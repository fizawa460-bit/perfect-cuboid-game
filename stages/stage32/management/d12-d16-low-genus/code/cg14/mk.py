import sys, os, json
ARGS=sys.argv[1:]
sys.path.insert(0, os.path.abspath('fasth0'))
import script_v2 as SV
TAIL=open('cg/mk.py').read().split("TAIL='''")[1].split("'''")[0]
names=[]
for hf,cf,tag in [('d14v2_h0.json','d14v2_cont.json','v'),('d14fullf_h0.json','d14fullf_cont.json','f')]:
    H=json.load(open('fasth0/'+hf)); C=json.load(open('fasth0/'+cf))
    for k,v in C.items():
        if not v: continue
        m,h,D=H[k]; s=SV.script(D,m); key='"base locus outside D\'s curves'
        s=s[:s.index(key)]+'if (dim(Bp) != 2) { "residual not a curve"; quit; }\n'+TAIL
        n=f'c14{tag}_{k}'; open(f'cg14/{n}.sing','w',newline='\n').write(s); names.append(n)
open('cg14/jobs.txt','w',newline='\n').write('\n'.join(names)+'\n'); print(len(names))
