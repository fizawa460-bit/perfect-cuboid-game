#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, json
from pathlib import Path
N=20
OK=(ast.Expression,ast.List,ast.Tuple,ast.Constant,ast.UnaryOp,ast.USub,ast.UAdd,ast.Load)

def parse_list(path,name):
    text=path.read_text(); k=text.find(name+':='); i=text.find('[',k); d=0; q=None; esc=False
    for j in range(i,len(text)):
        c=text[j]
        if q:
            if esc: esc=False
            elif c=='\\': esc=True
            elif c==q: q=None
            continue
        if c in "'\"": q=c
        elif c=='[': d+=1
        elif c==']':
            d-=1
            if d==0:
                tree=ast.parse(text[i:j+1],mode='eval')
                if any(not isinstance(x,OK) for x in ast.walk(tree)): raise ValueError(name)
                return ast.literal_eval(tree)
    raise KeyError(name)

def row(v,A): return [sum(v[i]*A[i][j] for i in range(N)) for j in range(N)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def I(): return [[int(i==j) for j in range(N)] for i in range(N)]
def dot(v,w,G): return sum(v[i]*G[i][j]*w[j] for i in range(N) for j in range(N))
def sset(vs): return {tuple(v) for v in vs}
def twice(label): return tuple((2*x)%4 for x in label)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',type=Path); ap.add_argument('identify',type=Path); ap.add_argument('--out',type=Path,required=True); a=ap.parse_args()
    s0=next(a.root.rglob('S0S3.txt')); bor=next(a.root.rglob('Borcherds.txt'))
    G=parse_list(s0,'GramS0'); Six=parse_list(bor,'SixFs'); Aut=parse_list(bor,'AutX0h0'); MW=parse_list(bor,'MWtorsigmaz'); Ts=parse_list(bor,'Tsigma'); inv=parse_list(bor,'iotasigmaz')
    raw=json.loads(a.identify.read_text()); fr=raw['fr']; refined=[]
    for n,c in enumerate(raw['candidates']):
        fs,M,corners=c['f_s'],c['M'],c['corner_roots']; cs=sset(corners)
        rb=[x for fib in Six[:2] for x in fib if tuple(x) not in cs and dot(M,x,G)==0]
        null4=[(i,v,l) for i,(v,l) in enumerate(MW) if dot(M,v,G)==0 and tuple(l) not in {(0,0),(0,2),(2,0),(2,2)}]
        doubles=sorted(set(twice(l) for _,_,l in null4)); boundary=list(doubles[0]) if len(doubles)==1 else None
        swaps=[]
        target=sset(v for _,v,_ in null4)
        for ai,A in enumerate(Aut):
            if row(fr,A)==fs and row(fs,A)==fr and row(M,A)==M and mm(A,A)==I() and sset(row(x,A) for x in corners)==cs and sset(row(x,A) for x in rb)==target:
                swaps.append(ai)
        deltas=[]
        for i,(v,l) in enumerate(MW):
            if tuple(l) not in {(0,2),(2,0),(2,2)}: continue
            D=mm(inv,Ts[i]); fixed=sum(row(x,D)==x for x in corners)
            deltas.append({'label':l,'index':i,'M_fixed':row(M,D)==M,'f_r_fixed':row(fr,D)==fr,'corner_fixed':fixed,'distinct_from_boundary':l!=boundary})
        deck=[d for d in deltas if d['M_fixed'] and d['f_r_fixed'] and d['corner_fixed']==4 and d['distinct_from_boundary']]
        passed=len(rb)==4 and len(null4)==4 and len(doubles)==1 and bool(swaps) and len(deck)==1
        refined.append({'raw_candidate_index':n,'f_s':fs,'M':M,'corners':corners,'r_boundary_roots':rb,'M_null_order4_sections':[v for _,v,_ in null4],
                        'M_null_order4_labels':[l for _,_,l in null4],'boundary_2torsion_label':boundary,'swap_indices':swaps,'delta_tests':deltas,'deck_candidates':deck,'pass':passed})
    passed=[x for x in refined if x['pass']]
    out={'raw_candidate_count':len(refined),'pass_count':len(passed),'candidates':refined}
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'raw':len(refined),'passed':len(passed),'summary':[{'index':x['raw_candidate_index'],'f_s':x['f_s'],'M':x['M'],'boundary':x['boundary_2torsion_label'],'deck':x['deck_candidates'][0]['label'],'swap_count':len(x['swap_indices'])} for x in passed]},indent=2))
if __name__=='__main__': main()
