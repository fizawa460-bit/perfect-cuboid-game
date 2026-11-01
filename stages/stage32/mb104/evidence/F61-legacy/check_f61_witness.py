#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
P,R,C=97,896,1464

def trim(a):
    while a and not a[-1]: a.pop()
    return a
def rem(a,b):
    a=trim(a[:]);b=trim(b[:])
    while a and len(a)>=len(b):
        f=a[-1]*pow(b[-1],-1,P)%P;k=len(a)-len(b)
        for j,x in enumerate(b):a[k+j]=(a[k+j]-f*x)%P
        trim(a)
    return a
def gcd(a,b):
    a,b=trim(a[:]),trim(b[:])
    while b:a,b=b,rem(a,b)
    return a
def dot(a,b):return sum(x*y for x,y in zip(a,b))%P
def main():
    raw=(ROOT/'A97.bin').read_bytes();lead=(ROOT/'leading97.bin').read_bytes()
    ev=(ROOT/'evaluations97.bin').read_bytes();sample=(ROOT/'samples97.bin').read_bytes()
    rows=[raw[i*C:(i+1)*C] for i in range(R)]
    leadrows=[lead[i*C:(i+1)*C] for i in range(14*17)]
    good=[]
    for k in range(len(sample)//C):
        x=sample[k*C:(k+1)*C]
        assert all(dot(row,x)==0 for row in rows)
        assert dot(ev[:C],x)==1 and dot(ev[C:],x)
        forms=[[dot(row,x) for row in leadrows[n*17:(n+1)*17]] for n in range(14)]
        if all(f[-1] and len(gcd(f,[(j*f[j])%P for j in range(1,17)]))==1 for f in forms):
            good.append((k,x,forms))
            for old_k,old_x,old_forms in good[:-1]:
                if all(len(gcd(f,g))==1 for f,g in zip(forms,old_forms)):
                    result={'prime':P,'matrix_shape':[R,C],
                            'rank':int((ROOT/'rank97.txt').read_text().split()[0]),
                            'witness_indices':[old_k,k],
                            'witnesses':[list(old_x),list(x)],
                            'leading_forms':[old_forms,forms],
                            'all_896_constraints':True,'all_14_squarefree':True,
                            'all_14_pairwise_coprime':True,
                            'omitted_values':[[dot(ev[:C],y),dot(ev[C:],y)] for y in (old_x,x)],
                            'characteristic_zero_lift':'NOT_YET_ESTABLISHED'}
                    (ROOT/'witness97.json').write_text(json.dumps(result,indent=2)+'\n')
                    print(json.dumps({key:result[key] for key in ('prime','matrix_shape','rank','witness_indices','all_14_squarefree','all_14_pairwise_coprime','omitted_values','characteristic_zero_lift')}))
                    return
    raise SystemExit('No suitable pair among the bounded 32 samples')
if __name__=='__main__':main()
