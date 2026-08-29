#!/usr/bin/env python3
"""Network-free exact verifier for the semantic Kc discriminant 2-torsion target."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
PIC=HERE/'j2-semantic-kc-picard-basis.json'
OUT=HERE/'j2-semantic-kc-discriminant-2torsion-target.json'
EXPECTED_PIC='c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0'

def csha(d):
    d=dict(d); d.pop('canonical_sha256',None)
    return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def gram(c):
    g17=c['gram17']; inc=c['incidence17x12']; triple=c['semantic_exceptional_indices_0based']
    g=[r[:] + [inc[i][j] for j in triple] for i,r in enumerate(g17)]
    for a,j in enumerate(triple):
        row=[inc[i][j] for i in range(17)]+[0,0,0]; row[17+a]=-2; g.append(row)
    return g

def rank_null_basis_mod2(A):
    a=[[x&1 for x in r] for r in A]; m=len(a); n=len(a[0]); r=0; piv=[]
    for col in range(n):
        p=next((i for i in range(r,m) if a[i][col]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for i in range(m):
            if i!=r and a[i][col]: a[i]=[x^y for x,y in zip(a[i],a[r])]
        piv.append(col); r+=1
    free=[j for j in range(n) if j not in piv]; basis=[]
    for f in free:
        x=[0]*n; x[f]=1
        for i,p in enumerate(piv): x[p]=a[i][f]
        basis.append(x)
    return r,basis

def mv(A,v): return [sum(a*b for a,b in zip(row,v)) for row in A]
def q(A,v): return sum(v[i]*A[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))

def main():
    p=json.loads(PIC.read_text()); o=json.loads(OUT.read_text())
    assert p['canonical_sha256']==EXPECTED_PIC==csha(p)
    A=gram(p); assert len(A)==20 and all(len(r)==20 for r in A)
    rank,basis=rank_null_basis_mod2(A); assert rank==18 and len(basis)==2
    expected=[x['numerator_mod2'] for x in o['semantic_half_lattice_basis']]
    assert basis==expected
    for rec,v in zip(o['semantic_half_lattice_basis'],basis):
        Av=mv(A,v); assert all(x%2==0 for x in Av)
        assert rec['pairing_vector_Gu_over_2']==[x//2 for x in Av]
        assert rec['self_pairing_numerator_vGv']==q(A,v)
        assert rec['quadratic_value_mod_2']==str((q(A,v)//4)%2)
    u1,u2=basis; us=[u1,u2,[a^b for a,b in zip(u1,u2)]]
    assert [x['numerator_mod2'] for x in o['nonzero_semantic_2torsion_candidates']]==us
    assert o['gram_mod2_rank']==18 and o['gram_mod2_nullity']==2
    assert o['discriminant_2torsion_dimension_f2']==2
    assert o['j2_coordinate_materialized'] is False
    assert o['stage33_12_closed_exact'] is False and o['stage33_13_released'] is False
    assert o['canonical_sha256']==csha(o)
    print(json.dumps({'status':'PASS_EXACT','rank_mod2':18,'nullity_mod2':2,'candidate_count':3,'canonical_sha256':o['canonical_sha256']},sort_keys=True))

if __name__=='__main__': main()
