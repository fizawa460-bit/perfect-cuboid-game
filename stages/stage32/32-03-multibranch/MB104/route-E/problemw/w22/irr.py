import sys
P=int(sys.argv[1]); files=sys.argv[2:]
out=[f'LIB "elim.lib"; ring r={P},(X0,X1,Y0,Y1),dp; list F; poly W;']
n=0
for fn in files:
    for l in open(fn):
        t=l.split()
        if not t or t[0]!='CURVE': continue
        d=dict(zip(t[1:t.index('w'):2],t[2:t.index('w'):2]))
        if int(d['om'])>4 or d['vline']=='1': continue
        w=t[t.index('w')+1:]
        terms=[f"{w[3*a+b]}*X0^{a}*X1^{2-a}*Y0^{b}*Y1^{2-b}" for a in range(3) for b in range(3) if w[3*a+b]!='0']
        out.append(f'W={"+".join(terms)}; F=factorize(W); "{fn} {n} {" ".join(k+"="+v for k,v in d.items())} nfac", size(F[1])-1, " mult", F[2];')
        n+=1
out.append('quit;'); open('irr.sing','w').write('\n'.join(out)); print(n,'curves')
