"""Request 6, exit (i): are the translate inequalities  sum_P m_P m_{gP} <= 2ab  (g in V4 x V4, g != e)
already implied by Lemma K (per graph), the fibre bounds and m >= 0 ?
We maximise the quadratic form over that polytope (random restarts, SLSQP).  Floating point, exploration only:
the answer is a real number compared with 2ab with a visible margin, no coincidence test is involved.
Run:  python -I translate_qp.py
"""
import itertools, numpy as np
from scipy.optimize import minimize
B=['0','inf','1','-1','i','-i']; lab={'0':'e','inf':'e','1':'b','-1':'b','i':'a','-i':'a'}
Z=[(x,y) for x in B for y in B if lab[x]==lab[y]]; idx={P:k for k,P in enumerate(Z)}
V4={'t':{'0':'0','inf':'inf','1':'1','-1':'-1','i':'i','-i':'-i'},
    '-t':{'0':'0','inf':'inf','1':'-1','-1':'1','i':'-i','-i':'i'},
    '1/t':{'0':'inf','inf':'0','1':'1','-1':'-1','i':'-i','-i':'i'},
    '-1/t':{'0':'inf','inf':'0','1':'-1','-1':'1','i':'i','-i':'-i'}}
graphs={g:[idx[(x,V4[g][x])] for x in B] for g in V4}       # 6 matched points on each Klein graph
for P in Z: assert sum(idx[P] in graphs[g] for g in V4)==2
def perm(g1,g2): return [idx[(V4[g1][x],V4[g2][y])] for (x,y) in Z]
def run(a,b,use_graph=True,trials=300,seed=1):
    rng=np.random.default_rng(seed); S=a+b
    cons=[]
    for x in B: cons.append([1.0 if P[0]==x else 0.0 for P in Z]+[a])       # column sums <= a
    for y in B: cons.append([1.0 if P[1]==y else 0.0 for P in Z]+[b])       # row sums <= b
    if use_graph:
        for g in V4: cons.append([1.0 if k in graphs[g] else 0.0 for k in range(12)]+[S])   # Lemma K per graph
    else: cons.append([1.0]*12+[2*S])                                                       # Lemma K summed
    A=np.array([c[:-1] for c in cons]); ub=np.array([c[-1] for c in cons])
    out={}
    for g1,g2 in itertools.product(V4,V4):
        if (g1,g2)==('t','t'): continue
        p=perm(g1,g2); best=0; arg=None
        f=lambda m: -sum(m[k]*m[p[k]] for k in range(12))
        for _ in range(trials):
            m0=rng.random(12)*min(a,b)/2
            r=minimize(f,m0,method='SLSQP',bounds=[(0,None)]*12,
                       constraints=[{'type':'ineq','fun':lambda m:ub-A@m}],options={'maxiter':200,'ftol':1e-12})
            if r.success and (ub-A@r.x).min()>-1e-8 and -r.fun>best: best=-r.fun; arg=r.x
        out[(g1,g2)]=(best,arg)
    worst=max(out.items(),key=lambda kv:kv[1][0])
    return worst
for a,b in ((1,1),(1,1.5),(1,1.9),(1,2.5)):
    for ug in (True,False):
        (g,(val,arg))=run(a,b,ug)
        print('a=%.1f b=%.1f  Lemma K %s : max over g of sum m_P m_gP = %.4f   2ab = %.4f   ratio %.4f   (g=%s, M=%.3f)'
              %(a,b,'per graph' if ug else 'summed   ',val,2*a*b,val/(2*a*b),g,arg.sum()))
# the uniform profile
for a,b in ((1,1),(1,1.5),(1,1.9)):
    S=a+b; print('uniform m_P = S/6 (M = 2S): sum = S^2/3 = %.4f  vs 2ab = %.4f'%(S*S/3,2*a*b))
