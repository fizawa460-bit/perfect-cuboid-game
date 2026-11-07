import re,os,json
from collections import Counter
C=Counter(); res={}
for nm in open("sxjobs_new.txt").read().split():
    f=nm+".out"
    if not os.path.exists(f): C["pending"]+=1; continue
    t=open(f,errors="replace").read()
    if "time" not in t: C["running"]+=1; continue
    mg=re.search(r"FASTGENUS (?:lower bound )?(-?\d+)",t)
    if "DUPLICATE" in t: st="duplicate"
    elif "REDUCIBLE" in t: st="reducible"
    elif re.search(r"^time 7[12]\d\d",t,re.M): st="OPEN-timeout"
    elif mg: st="g>=2" if int(mg.group(1))>=2 else "OPEN-lowg"
    else: st="OPEN-other"
    C[st]+=1; res[nm]=st
print(C); json.dump(res,open("sx_tally.json","w"))
print([k for k,v in res.items() if v.startswith("OPEN")][:40])
