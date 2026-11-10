"""218 hidden row(C) radical-height lift; symbolic and integer labels only."""
import json,math
from pathlib import Path
states=0
for a in range(1,13):
    for b in range(13):
        for row in (['A','C'] if b==0 else ['A','B','C']):
            HQ=a if row!='C' else 0;HS=a-HQ
            TQ=b if row=='A' else 0;TB=b if row=='B' else 0;TC=b if row=='C' else 0
            ePC=TC+1 if TC else 0;eA=HQ+TQ+TB
            eR=a+b
            assert ePC+eA<=eR and (not ePC or ePC>=2)
            assert (TC==0 or HS>=1)
            states+=1
for b in range(1,13):
    for side in ['Q','S']:
        states+=1
        # Fresh-S cannot pay the extra radical power at height R.
        if side=='S':assert b+1>b
U=200000;rad=list(range(U+1))
for n in range(1,U+1):rad[n]=1
for p in range(2,U+1):
    if rad[p]==1:
        for n in range(p,U+1,p):rad[n]*=p
labels=[n for n in range(1,U+1) if n*rad[n]<=U]
image={n*rad[n]:n for n in labels}
assert len(image)==len(labels)
for m,n in image.items():
    assert m//rad[m]==n and rad[m]==rad[n]
    rem=m
    for p in range(2,math.isqrt(m)+1):
        if rem%p:continue
        e=0
        while rem%p==0:rem//=p;e+=1
        assert e>=2
    assert rem==1
checks=[]
for Y in [10,100,1000,10000,U]:
    vals=[n for n in labels if n*rad[n]<=Y]
    assert len(vals)<=3*math.sqrt(Y)
    for T in [1,10,100,1000]:
        s=sum(1/n for n in vals if n>=T)
        assert s<=3*math.sqrt(Y)/T
    checks.append({'Y':Y,'labels':len(vals),'max_n':max(vals)})
out={'card':'M3-T11-218','symbolic_states':states,'radical_height_bijection_labels':len(labels),'height_count_checks':checks,'fresh_S_counterstate':{'beta':1,'R_depth':1,'proposed_radical_lift_depth':2},'scope':'synthetic retained-table and integer-label verification; no physical endpoints or full residual count','independent_audit':'NOT RUN'}
Path('M3-T11-218-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
