#!/usr/bin/env python3
import itertools, json, math, pathlib

def variance(vals):
    m=sum(vals)/len(vals)
    return m*(1-m),m

def influences(vals,r):
    out=[]
    for j in range(r):
        flips=0
        for idx in range(1<<r):
            if vals[idx]!=vals[idx^(1<<j)]: flips+=1
        out.append(flips/(1<<r))
    return out

checks=0
for r in range(1,9):
    # structured Boolean stress family: thresholds/parities/cylinders/singletons
    funcs=[]
    funcs.append([1 if bin(i).count('1')>=max(1,(r+1)//2) else 0 for i in range(1<<r)])
    funcs.append([bin(i).count('1')%2 for i in range(1<<r)])
    funcs.append([1 if i==0 else 0 for i in range(1<<r)])
    funcs.append([1 if (i&1)==0 else 0 for i in range(1<<r)])
    for vals in funcs:
        v,m=variance(vals); inf=influences(vals,r)
        assert v <= 0.25*sum(inf)+1e-12
        if 0<m<1:
            assert max(inf) + 1e-12 >= 4*v/r
        checks+=1
p=pathlib.Path('stages/stage14/data/14-t96/influence_frozen.json')
data=json.loads(p.read_text())
data.update({'boolean_rank_max':8,'poincare_checks':checks,'max_influence_pigeonhole_checks':checks})
p.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
print('t96 influence audit OK',checks)
