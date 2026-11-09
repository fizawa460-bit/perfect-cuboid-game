import glob,re,json
from collections import Counter
res={};C=Counter();bad=[]
for f in sorted(glob.glob("sb_*.out")):
    t=open(f,errors="replace").read(); nm=f[:-4]
    if "time" not in t: C["running"]+=1; continue
    mk=re.search(r"k (\d+)\s+residual dim (-?\d+)\s+degree (\d+)\s+expected (\d+)",t)
    mg=re.search(r"FASTGENUS (?:lower bound )?(-?\d+)",t)
    if "REDUCIBLE" in t: st="reducible"
    elif mk and mg:
        k=int(mk.group(1)); B=int(mg.group(1)); g=-(-(B+k-1)//k)
        st="g>=2" if g>=2 else "OPEN-lowg"
        if int(mk.group(3))!=int(mk.group(4)): st+="-degmismatch"
    else: st="OPEN-other"
    C[st]+=1; res[nm]=st
    if st!="g>=2": bad.append(nm)
print(C); print(bad[:40]); json.dump(res,open("sb_tally.json","w"))
