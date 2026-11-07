import os,sys,re
src=open('cnc/mk.py').read()
T=src.split("T=r'''")[1].split("'''")[0]
T=T.replace('"COMPS", nq,','DCURVES\n"COMPS", nq,',1)
names=[]
for f in sys.argv[1:]:
    s=open(f).read(); key='list MA = minAssGTZ(Bp);'
    gs=re.search(r'ideal Dc = std\(intersect\(([^)]*)\)\)', s).group(1).split(',')
    dc=''
    for g in gs:
        dc+=('ideal BBn = std(S + ideal(NN)); ideal BBg = std(S + ideal(F0 + 7*F1)); '
             f'int exn = (mult(BBn) - mult(satx(BBn, {g}))) div mult({g}); int exg = (mult(BBg) - mult(satx(BBg, {g}))) div mult({g}); '
             f'if (exn > exg) {{ nq++; QL[nq] = {g}; QM[nq] = exn - exg; "  D-curve {g} excess", exn - exg; }} kill BBn; kill BBg; kill exn; kill exg;\n')
    n='nc_'+os.path.basename(f)[:-5]
    open('cnc/'+n+'.sing','w',newline='\n').write(s[:s.index(key)]+T.replace('DCURVES',dc)); names.append(n)
open('cnc/jobs2.txt','w',newline='\n').write('\n'.join(names)+'\n'); print(len(names))
