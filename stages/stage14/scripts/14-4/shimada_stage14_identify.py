#!/usr/bin/env python3
"""Identify Stage14's physical classes inside Shimada's level-4 NS basis.

Input is the unpacked official compdata directory.  The parser accepts the
Maple list assignments used in S0S3.txt/Borcherds.txt and never executes
arbitrary source code.
"""
from __future__ import annotations
import argparse, ast, json
from pathlib import Path

N=20

ALLOWED=(ast.Expression,ast.List,ast.Tuple,ast.Constant,ast.UnaryOp,ast.USub,ast.UAdd,ast.Load)

def safe_list_eval(expr:str):
    tree=ast.parse(expr,mode='eval')
    for n in ast.walk(tree):
        if not isinstance(n,ALLOWED):
            raise ValueError(f'unsupported syntax {type(n).__name__}')
        if isinstance(n,ast.Constant) and not isinstance(n.value,(int,str)):
            raise ValueError(f'unsupported constant {n.value!r}')
    return ast.literal_eval(tree)

def extract(path:Path,name:str):
    text=path.read_text(errors='strict')
    needle=name+':='
    i=text.find(needle)
    if i<0: raise KeyError(f'{name} not found in {path}')
    i=text.find('[',i+len(needle))
    if i<0: raise ValueError(f'{name}: list start missing')
    depth=0; quote=None; esc=False
    for j in range(i,len(text)):
        c=text[j]
        if quote:
            if esc: esc=False
            elif c=='\\': esc=True
            elif c==quote: quote=None
            continue
        if c in "'\"": quote=c
        elif c=='[': depth+=1
        elif c==']':
            depth-=1
            if depth==0:
                return safe_list_eval(text[i:j+1])
    raise ValueError(f'{name}: unterminated list')

def add(*vs): return [sum(x) for x in zip(*vs)]
def scale(a,v): return [a*x for x in v]
def sub(a,b): return [x-y for x,y in zip(a,b)]
def matmul_row(v,A): return [sum(v[i]*A[i][j] for i in range(N)) for j in range(N)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def dot(v,w,G): return sum(v[i]*G[i][j]*w[j] for i in range(N) for j in range(N))
def label2(label): return tuple((2*x)%4 for x in label)

def find_paths(root:Path):
    s=list(root.rglob('S0S3.txt')); b=list(root.rglob('Borcherds.txt'))
    if len(s)!=1 or len(b)!=1: raise RuntimeError(f'expected unique files; S0S3={s}, Borcherds={b}')
    return s[0],b[0]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',type=Path); ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args(); s0,bfile=find_paths(a.root)
    G=extract(s0,'GramS0'); L40=extract(s0,'L40vs')
    SixFs=extract(bfile,'SixFs'); fr=extract(bfile,'fsigma')
    AutH=extract(bfile,'AutX0h0'); MW=extract(bfile,'MWtorsigmaz')
    Ts=extract(bfile,'Tsigma'); inv=extract(bfile,'iotasigmaz')
    assert len(G)==N and all(len(r)==N for r in G)
    assert len(L40)==40 and len(SixFs)==6 and all(len(f)==4 for f in SixFs)
    assert len(AutH)==3840 and len(MW)==16 and len(Ts)==16
    orbit={tuple(matmul_row(fr,A)) for A in AutH}
    candidates=[]
    for fs_t in sorted(orbit):
        fs=list(fs_t)
        if fs==fr or dot(fs,fs,G)!=0 or dot(fr,fs,G)!=2: continue
        p0=[dot(fs,c,G) for c in SixFs[0]]; p1=[dot(fs,c,G) for c in SixFs[1]]
        if sorted(p0)!=[0,0,1,1] or sorted(p1)!=[0,0,1,1]: continue
        if min(dot(fs,c,G) for c in L40)<0: continue
        corners=[c for fib in SixFs[:2] for c in fib if dot(fs,c,G)==0]
        if len(corners)!=4: continue
        M=sub(add(scale(2,fr),scale(2,fs)), add(*corners))
        m40=[dot(M,c,G) for c in L40]
        cand={
          'f_s':fs,'corner_roots':corners,'M':M,
          'checks':{'M2':dot(M,M,G),'M_fr':dot(M,fr,G),'M_fs':dot(M,fs,G),
                    'M40_min':min(m40),'M40_zero_count':sum(x==0 for x in m40)},
          'M40_intersections':m40,
        }
        candidates.append(cand)
    # enrich any candidate satisfying the intrinsic Stage14 fingerprint
    for cand in candidates:
        M=cand['M']; corners=cand['corner_roots']
        mwrows=[]
        for idx,(v,label) in enumerate(MW):
            mwrows.append({'index':idx,'label':label,'vector':v,'M_degree':dot(M,v,G),'fr_degree':dot(fr,v,G)})
        null_labels=[r['label'] for r in mwrows if r['M_degree']==0]
        doubled=sorted(set(label2(x) for x in null_labels))
        order2=[r for r in mwrows if tuple(r['label']) in {(0,2),(2,0),(2,2)}]
        deltas=[]
        for r in order2:
            D=mm(inv,Ts[r['index']]) # row action: inversion then translation
            fixed_corners=sum(matmul_row(c,D)==c for c in corners)
            deltas.append({'index':r['index'],'label':r['label'],
                           'M_fixed':matmul_row(M,D)==M,
                           'fr_fixed':matmul_row(fr,D)==fr,
                           'fixed_corner_classes':fixed_corners,
                           'matrix':D})
        cand['mw_sections']=mwrows
        cand['M_null_torsion_labels']=null_labels
        cand['doubles_of_M_null_torsion_labels']=[list(x) for x in doubled]
        cand['order2_delta_tests']=deltas
        # exact tests among the distinguished 40 roots
        for d in deltas:
            D=d['matrix']; hits=[]
            for i,C in enumerate(L40):
                if dot(C,C,G)==-2 and dot(fr,C,G)==2 and dot(M,C,G)==4 and matmul_row(C,D)==sub(M,C):
                    hits.append(i+1)
            d['L40_split_hits_1based']=hits
            del d['matrix']
    result={
      'source_files':{'S0S3_bytes':s0.stat().st_size,'Borcherds_bytes':bfile.stat().st_size},
      'dimensions':{'GramS0':len(G),'L40vs':len(L40),'SixFs':len(SixFs),'AutX0h0':len(AutH),'MWtorsigmaz':len(MW),'Tsigma':len(Ts)},
      'fr':fr,'fr2':dot(fr,fr,G),'AutX0h0_fiber_orbit_size':len(orbit),
      'candidate_count':len(candidates),'candidates':candidates,
    }
    a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
