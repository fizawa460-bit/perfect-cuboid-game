import numpy as np
from covers import *
def images(x,an,n,prof):
    """yield (x2, an2) for images of cover under Stab(prof) in Aut(B) x <conj>"""
    p,q=x[:n+1],x[n+1:]
    cj=lambda z: None if z is None else complex(z).conjugate()
    for conj in (0,1):
        pp,qq=(p.conj(),q.conj()) if conj else (p,q)
        cperm=(0,1,2,3,5,4) if conj else (0,1,2,3,4,5)
        anc={cperm[y]:([cj(z) for z in an[y][0]],[cj(z) for z in an[y][1]]) if conj else an[y] for y in range(6)}
        for M,perm in AUT:
            t2=[0]*6
            for y in range(6): t2[perm[cperm[y]]]=prof[y]
            if tuple(t2)!=tuple(prof): continue
            p2=M[0,0]*pp+M[0,1]*qq; q2=M[1,0]*pp+M[1,1]*qq
            an2={perm[y]:anc[y] for y in range(6)}
            yield np.concatenate([p2,q2]),an2
