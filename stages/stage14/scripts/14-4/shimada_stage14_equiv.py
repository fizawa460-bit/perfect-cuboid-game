#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, json
from pathlib import Path
N=20
OK=(ast.Expression,ast.List,ast.Tuple,ast.Constant,ast.UnaryOp,ast.USub,ast.UAdd,ast.Load)
def parse(path,name):
    t=path.read_text(); k=t.find(name+':='); i=t.find('[',k); d=0; q=None; esc=False
    for j in range(i,len(t)):
        c=t[j]
        if q:
            if esc: esc=False
            elif c=='\\': esc=True
            elif c==q:q=None
            continue
        if c in "'\"":q=c
        elif c=='[':d+=1
        elif c==']':
            d-=1
            if d==0:
                z=ast.parse(t[i:j+1],mode='eval')
                if any(not isinstance(x,OK) for x in ast.walk(z)):raise ValueError(name)
                return ast.literal_eval(z)
    raise KeyError(name)
def row(v,A):return [sum(v[i]*A[i][j] for i in range(N)) for j in range(N)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def sset(xs):return {tuple(x) for x in xs}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('refine',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    b=next(a.root.rglob('Borcherds.txt'));Aut=parse(b,'AutX0f');Ts=parse(b,'Tsigma');inv=parse(b,'iotasigmaz')
    r=json.loads(a.refine.read_text());p=[x for x in r['candidates'] if x['pass']]
    assert len(p)==2
    ds=[]
    for x in p:
        di=x['deck_candidates'][0]['index'];ds.append(mm(inv,Ts[di]))
    maps=[]
    for i,A in enumerate(Aut):
        if row(p[0]['f_s'],A)!=p[1]['f_s'] or row(p[0]['M'],A)!=p[1]['M']:continue
        if sset(row(x,A) for x in p[0]['corners'])!=sset(p[1]['corners']):continue
        if mm(A,ds[1])!=mm(ds[0],A):continue
        maps.append(i)
    out={'AutX0f_size':len(Aut),'passed_labelings':2,'equivalence_map_indices_0based':maps,'equivalent':bool(maps)}
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
