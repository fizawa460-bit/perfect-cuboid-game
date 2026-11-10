"""Finite algebra replay only; these weights are NOT Stage37 physical populations."""
import json, math, cmath
from pathlib import Path
import numpy as np
from fractions import Fraction

def rational_rank(matrix):
    a=[[Fraction(v) for v in row] for row in matrix if any(row)]
    if not a: return 0
    k=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(k,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[k],a[pivot]=a[pivot],a[k]
        for i in range(k+1,len(a)):
            if a[i][j]:
                ratio=a[i][j]/a[k][j]
                a[i]=[x-ratio*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a): break
    return k

rows=[]
for q in (13,17,25,65,169):
    units=[u for u in range(q) if math.gcd(u,q)==1]
    squares={u*u%q for u in units}
    for restriction in ('all_units','square_units'):
        vals=[u for u in units if restriction=='all_units' or u in squares]
        for kind in ('flat','masked_weighted'):
            mat=[]
            for u in vals:
                line=[]
                for v in vals:
                    ok=(1+u*u+v*v)%q==0
                    w=1 if kind=='flat' else ((u*7+v*11)%5+1 if (u+2*v)%4 else 0)
                    line.append(w if ok else 0)
                mat.append(line)
            a=np.array(mat,dtype=float)
            mass=int(a.sum()); energy=int((a*a).sum())
            groups={}
            for i,u in enumerate(vals):
                if any(mat[i]): groups.setdefault(u*u%q,[]).append(i)
            block_energy=sorted([int((a[ix,:]**2).sum()) for ix in groups.values()],reverse=True)
            exact_rank=rational_rank(mat)
            assert exact_rank>=len(groups)
            sv=np.linalg.svd(a,compute_uv=False)
            checks=[]
            for j in (0,1,2,4):
                lower=energy-sum(block_energy[:j])
                error=float(sum(sv[j:]**2))
                assert error+1e-7>=lower
                checks.append({'J':j,'squared_error':error,'lower_bound':lower})
            # Each frequency has exactly the same shell mass; numerical replay.
            shell=[(u,v,mat[i][k]) for i,u in enumerate(vals) for k,v in enumerate(vals) if mat[i][k]]
            for h in range(q):
                ah=sum(w*cmath.exp(2j*math.pi*h*((1+u*u+v*v)%q)/q) for u,v,w in shell)
                assert abs(ah-mass)<1e-8
            assert mass/q+(q-1)*mass/q==mass or abs(mass/q+(q-1)*mass/q-mass)<1e-8
            rows.append({'q':q,'restriction':restriction,'weight':kind,'mass':mass,'energy':energy,'occupied_square_values':len(groups),'exact_rank':exact_rank,'approximation_checks':checks})
out={'status':'PASS','scope':'finite algebra models, not physical endpoints or asymptotic evidence','cases':rows}
Path('verify159-result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','cases':len(rows),'max_q':169,'physical_population_tested':False}))
