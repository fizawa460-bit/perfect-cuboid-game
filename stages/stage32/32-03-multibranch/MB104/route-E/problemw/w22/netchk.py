import sys, itertools, importlib.util
P=int(sys.argv[1]); I=int(sys.argv[2]); sys.argv=['pwfam.py',str(P),str(I),'0','/dev/null']
spec=importlib.util.spec_from_file_location('pwfam','pwfam.py'); pf=importlib.util.module_from_spec(spec); spec.loader.exec_module(pf)
M=[p for p in range(36) if pf.TY[p//6]==pf.TY[p%6]]
out=[f'ring r={P},(X0,X1,Y0,Y1),dp; poly g; int c=0;']
for S in itertools.combinations(M,7):
    ns=pf.nullspace([pf.R[p] for p in S])
    if len(ns)>2:
        out.append('g='+'gcd('*(len(ns)-1)+pf.polystr(ns[0])+''.join(','+pf.polystr(v)+')' for v in ns[1:])+'; if (deg(g)>0) {c++;} else {"NET-COPRIME";}')
out.append('"nets with common factor",c; quit;'); open('netchk.sing','w').write('\n'.join(out))
