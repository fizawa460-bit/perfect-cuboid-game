#!/usr/bin/env python3
"""Enumerate the complete Stage14 split-root lattice for one Shimada labeling.
Requires PARI/GP for matkerint + Fincke-Pohst qfminim.
"""
from __future__ import annotations
import argparse, ast, json, shutil, subprocess
from pathlib import Path
N=20
OK=(ast.Expression,ast.List,ast.Tuple,ast.Constant,ast.UnaryOp,ast.USub,ast.UAdd,ast.Load)
def parse(path,name):
    t=path.read_text();k=t.find(name+':=');i=t.find('[',k);d=0;q=None;esc=False
    for j in range(i,len(t)):
        c=t[j]
        if q:
            if esc:esc=False
            elif c=='\\':esc=True
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
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def row(v,A):return [sum(v[i]*A[i][j] for i in range(N)) for j in range(N)]
def dot(v,w,G):return sum(v[i]*G[i][j]*w[j] for i in range(N) for j in range(N))
def gps(M):return '['+';'.join(','.join(str(x) for x in r) for r in M)+']'
def main():
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('refine',type=Path);ap.add_argument('equiv',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    if not shutil.which('gp'):raise RuntimeError('PARI/GP gp not found')
    eq=json.loads(a.equiv.read_text());assert eq['equivalent']
    rr=json.loads(a.refine.read_text());p=[x for x in rr['candidates'] if x['pass']][0]
    s0=next(a.root.rglob('S0S3.txt'));b=next(a.root.rglob('Borcherds.txt'))
    G=parse(s0,'GramS0');fr=parse(b,'fsigma');Ts=parse(b,'Tsigma');inv=parse(b,'iotasigmaz')
    M=p['M'];di=p['deck_candidates'][0]['index'];D=mm(inv,Ts[di])
    A=[r[:] for r in D]
    for i in range(N):A[i][i]+=1
    gp=f'''A={gps(A)}; G={gps(G)}; K=matkerint(A~); Q=-K~*G*K;\nprint("RANK=",matsize(K)[2]);\nfor(j=1,matsize(K)[2],print("K=",Vec(K[,j])));\nprint("DETQ=",matdet(Q));\nR=qfminim(Q,16); print("ENUMCOUNT=",R[1]); V=R[3];\nfor(j=1,matsize(V)[2],if(qfeval(Q,V[,j])==16,print("V=",Vec(V[,j]))));\n'''
    z=subprocess.run(['gp','-fq'],input=gp,text=True,capture_output=True,check=True).stdout.splitlines()
    rank=int(next(x.split('=',1)[1] for x in z if x.startswith('RANK=')))
    kb=[ast.literal_eval(x.split('=',1)[1]) for x in z if x.startswith('K=')]
    detq=int(next(x.split('=',1)[1] for x in z if x.startswith('DETQ=')))
    vv=[ast.literal_eval(x.split('=',1)[1]) for x in z if x.startswith('V=')]
    assert len(kb)==rank
    def xfrom(v):return [sum(kb[j][i]*v[j] for j in range(rank)) for i in range(N)]
    pairs=[]
    for v in vv:
        x=xfrom(v)
        if any((x[i]+M[i])%2 for i in range(N)):continue
        for sg in (1,-1):
            xs=[sg*y for y in x];C=[(M[i]+xs[i])//2 for i in range(N)]
            assert row(C,D)==[M[i]-C[i] for i in range(N)]
            assert dot(C,C,G)==-2 and dot(M,C,G)==4 and dot(fr,C,G)==2
        C=[(M[i]+x[i])//2 for i in range(N)];Cp=[M[i]-C[i] for i in range(N)]
        pairs.append({'C':C,'delta_C':Cp,'C2':-2,'M_C':4,'f_r_C':2,'pair_intersection':dot(C,Cp,G)})
    out={'representative_raw_candidate_index':p['raw_candidate_index'],'f_s':p['f_s'],'M':M,'deck_label':p['deck_candidates'][0]['label'],
         'anti_invariant_rank':rank,'positive_form_determinant':detq,'qfminim_norm_le_16_vector_count':int(next(x.split('=',1)[1] for x in z if x.startswith('ENUMCOUNT='))),
         'norm16_pair_representatives':len(vv),'parity_compatible_split_root_pairs':len(pairs),'split_root_pairs':pairs}
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('anti_invariant_rank','positive_form_determinant','norm16_pair_representatives','parity_compatible_split_root_pairs')},indent=2))
if __name__=='__main__':main()
