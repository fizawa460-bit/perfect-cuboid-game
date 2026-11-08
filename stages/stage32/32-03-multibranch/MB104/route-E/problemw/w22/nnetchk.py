import sys, pickle, importlib.util
P=int(sys.argv[1]); I=int(sys.argv[2]); sys.argv=['pwfam.py',str(P),str(I),'0','/dev/null']
spec=importlib.util.spec_from_file_location('pwfam','pwfam.py'); pf=importlib.util.module_from_spec(spec); spec.loader.exec_module(pf)
sys.argv=['pwfam.py',str(P),str(I),'1','/dev/null']; spec=importlib.util.spec_from_file_location('pn','pwfam.py'); pn=importlib.util.module_from_spec(spec); spec.loader.exec_module(pn)
hits,nnet=pickle.load(open(f'slack0_{P}.pkl','rb'))
out=[f'ring r={P},(X0,X1,Y0,Y1),dp; poly g; int c=0; int u=0;']
for e in nnet:
    if isinstance(e[0],str): tag,S=e; m=pn if tag=='D' else pf; ns=m.nullspace((m.BASE if tag=='D' else [])+[m.R[p] for p in S])
    else: S=e; ns=pf.nullspace([pf.R[p] for p in S])
    g='gcd('*(len(ns)-1)+pf.polystr(ns[0])+''.join(','+pf.polystr(v)+')' for v in ns[1:])
    out.append(f'g={g}; if (deg(g)>0) {{c++;}} else {{u++; "NOCOMMON {e}";}}')
out.append('"families",'+str(len(nnet))+'," common factor",c," no common factor",u; quit;')
open(f'nnet_{P}.sing','w').write('\n'.join(out))
