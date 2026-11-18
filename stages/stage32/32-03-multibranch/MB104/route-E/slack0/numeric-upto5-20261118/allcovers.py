import glob,pickle,sys
from covers import *
import hp
def rough(p,q,n,prof,crit,ysl):
    out={}
    for y in range(6):
        f=(BP[y][1]*p-BP[y][0]*q)[::-1]
        cs=[crit[k] for k in range(len(ysl)) if ysl[k]==y]
        assert len(cs)==prof[y]
        g=f.copy()
        for cc in cs:
            for _ in range(2): g,r=np.polydiv(g,np.array([1,-cc]))
        g=np.trim_zeros(np.where(np.abs(g)<1e-9*np.abs(g).max(),0,g),'f')
        deg=len(g)-1; ninf=n-2*len(cs)-deg
        out[y]=([complex(z) for z in np.roots(g)]+[None]*ninf, list(cs))
    return out
def load_reps(n):
    reps=[]
    if n==2:
        for y1,y2 in itertools.combinations(range(6),2):
            M=np.array([[BP[y2][0],BP[y1][0]],[BP[y2][1],BP[y1][1]]],complex)
            p=np.array([M[0,1],0,M[0,0]]); q=np.array([M[1,1],0,M[1,0]])
            an={}
            for y in range(6):
                if y in (y1,y2): an[y]=([],[0j] if y==y1 else [None]); continue
                w=np.linalg.solve(M,np.array(BP[y],complex)); s=np.sqrt(w[0]/w[1])
                an[y]=([s,-s],[])
            reps.append((p,q,an,2))
        return reps,reps
    out=[]
    for fn in sorted(glob.glob(f'cov_{n}_*.pkl'))+sorted(glob.glob(f'seed/cov_{n}_*.pkl')):
        d=pickle.load(open(fn,'rb')); prof=d['prof']
        ys=[y for y in range(6) for _ in range(prof[y])]
        for x,aut in d['covers']:
            p,q=x[:n+1],x[n+1:]
            # recover crit points: polish via analyse using roots of Wronskian
            W=np.polysub(np.polymul(np.polyder(p[::-1]),q[::-1]),np.polymul(p[::-1],np.polyder(q[::-1])))
            W=np.trim_zeros(np.where(np.abs(W)<1e-10*np.abs(W).max(),0,W),'f')
            cr=np.roots(W)
            assert len(cr)==2*n-2
            # assign crit to y
            crit=[];ysl=[]
            for c in cr:
                v=(np.polyval(p[::-1],c),np.polyval(q[::-1],c))
                k=min(range(6),key=lambda y:abs(v[0]*BP[y][1]-v[1]*BP[y][0])/(abs(v[0])+abs(v[1])))
                crit.append(c); ysl.append(k)
            # refine crit by Newton on W
            crit=[complex(polish(W,c)) for c in crit]
            an=analyse(p,q,n,prof,crit,ysl)
            if an is None:
                an=rough(p,q,n,prof,crit,ysl)
                an2,res,co,hpo=hp.refine(p,q,an,n,iters=15)
                co=np.array(co)
                an=analyse(co[:n+1],co[n+1:],n,prof,[z for y in range(6) for z in an2[y][1]],[y for y in range(6) for z in an2[y][1]])
                assert an is not None, fn
                p,q=co[:n+1],co[n+1:]
                print('  recovered one cover in',fn)
            an2,res,co,hpo=hp.refine(p,q,an,n)
            an2['hp']=hpo
            assert res<1e-25, (fn,res)
            # sanity: refined points close to old
            for y in range(6):
                for z1,z2 in zip(an[y][0],an2[y][0]):
                    assert (z1 is None)==(z2 is None) and (z1 is None or abs(z1-z2)<1e-3*(1+abs(z1))), (fn,z1,z2)
            co=np.array(co); out.append((co[:n+1],co[n+1:],an2,aut))
    return out,out
def dedupe(lst):
    """lst of (p,q,an,aut); dedupe by Mobius invariant"""
    keep=[]; inv=[]
    for c in lst:
        v=invariant(c[2]); inv.append(v)
    inv=np.array(inv); o=np.argsort(inv[:,0].real)
    used=np.zeros(len(lst),bool); out=[]
    r0=inv[o,0].real
    for a_ in range(len(o)):
        i=o[a_]
        if used[i]: continue
        used[i]=True; out.append(lst[i])
        b_=a_+1
        while b_<len(o) and r0[b_]-r0[a_]<1e-7*(1+abs(r0[a_])):
            j=o[b_]
            if not used[j] and np.abs(inv[j]-inv[i]).max()<1e-7*(1+np.abs(inv[i]).max()): used[j]=True
            b_+=1
    return out
def full(n):
    reps,_=load_reps(n)
    if n>2: reps=dedupe(reps)
    allc=[]
    for p,q,an,aut in reps:
        for M,perm in AUT:
            p2=M[0,0]*p+M[0,1]*q; q2=M[1,0]*p+M[1,1]*q
            an2={perm[y]:an[y] for y in range(6)}
            if 'hp' in an: an2['hp']={perm[y]:v for y,v in an['hp'].items()}
            allc.append((p2,q2,an2,aut))
    if n==2:
        d={}
        for c in allc:
            key=tuple(sorted(y for y in range(6) if c[2][y][1])); d.setdefault(key,c)
        return reps,list(d.values())
    return reps,dedupe(allc)
if __name__=='__main__':
    for n in map(int,sys.argv[1:]):
        reps,allc=full(n)
        print(n,'reps',len(reps),'all',len(allc),'weighted',sum(1/c[3] for c in allc))
        pickle.dump({'reps':reps,'all':allc},open(f'all_{n}.pkl','wb'))
