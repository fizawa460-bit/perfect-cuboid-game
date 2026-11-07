import sys, json
sys.path.insert(0,'fasth0'); import fasth0v2 as F
H=json.load(open('fasth0/d16v2f_h0.json')); FX=json.load(open('fasth0/d16_fix.json'))
def names(D): return [f"C{k}_{c}" if k<=92 else f"N{k}_{c}" for k,c in sorted(D.items()) if c>0]
out={}; tot=0; cnt={}
for idx,(m,h,D) in H.items():
    if h is None or h<2 or FX.get(idx): continue
    D={int(k):v for k,v in D.items()}
    res=[]
    for k in range(1,141):
        c=D.get(k,0)+2
        if c>(4 if k<=92 else 3): res.append((k,'cap')); continue
        D2=dict(D); D2[k]=c; hh=F.h0(m,names(D2))
        if hh>0: res.append((k,hh))
    out[idx]=(h,res); tot+=1
json.dump(out,open('m2/scan16.json','w'))
import collections
C=collections.Counter()
for idx,(h,res) in out.items():
    C[(h, sum(1 for r in res if r[1]!='cap'), max([r[1] for r in res if r[1]!='cap'] or [0]), sum(1 for r in res if r[1]=='cap'))]+=1
print('reps', tot); print(sorted(C.items()))
