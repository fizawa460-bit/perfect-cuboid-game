#!/usr/bin/env python3
"""Network-free exact verifier for the Stage33-12 Kc transcendental lattice isometry checkpoint."""
from fractions import Fraction
from math import gcd, lcm
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
PIC=HERE/'j2-semantic-kc-picard-basis.json'
DISC=HERE/'j2-semantic-kc-discriminant-2torsion-target.json'
OUT=HERE/'j2-kc-transcendental-lattice-isometry.json'

def csha(d):
    d=dict(d); d.pop('canonical_sha256',None)
    return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def gram(c):
    g17=c['gram17']; inc=c['incidence17x12']; triple=c['semantic_exceptional_indices_0based']
    g=[r[:] + [inc[i][j] for j in triple] for i,r in enumerate(g17)]
    for a,j in enumerate(triple):
        row=[inc[i][j] for i in range(17)]+[0,0,0]; row[17+a]=-2; g.append(row)
    return g

def det_bareiss(A):
    m=[r[:] for r in A]; n=len(m); sign=1; prev=1
    for k in range(n-1):
        if m[k][k]==0:
            p=next((i for i in range(k+1,n) if m[i][k]),None)
            if p is None:return 0
            m[k],m[p]=m[p],m[k]; sign=-sign
        piv=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n): m[i][j]=(m[i][j]*piv-m[i][k]*m[k][j])//prev
        prev=piv
        for i in range(k+1,n):m[i][k]=0
        for j in range(k+1,n):m[k][j]=0
    return sign*m[-1][-1]

def parsev(v): return [Fraction(x) for x in v]
def mod1(x): return x % 1
def mod2(x): return x % 2

def pair(A,v,w):
    return sum(v[i]*A[i][j]*w[j] for i in range(len(v)) for j in range(len(w)))
def order(v):
    return lcm(*[x.denominator for x in v])
def addmod(a,b,ka=1,kb=1):
    return tuple(mod1(ka*x+kb*y) for x,y in zip(a,b))

def reduced_candidates():
    out=[]
    for a in range(1,33):
        for c in range(a,33):
            for b in range(-a,a+1):
                if 4*a*c-b*b==32:
                    M=[[2*a,b],[b,2*c]]
                    d1=0
                    for x in (2*a,b,b,2*c): d1=gcd(d1,abs(x))
                    d2=32//d1
                    out.append((M,f'Z/{d1} direct_sum Z/{d2}'))
    return out

def main():
    p=json.loads(PIC.read_text()); d=json.loads(DISC.read_text()); o=json.loads(OUT.read_text())
    assert p['canonical_sha256']==o['source_locks']['semantic_picard_basis_canonical_sha256']==csha(p)
    assert d['canonical_sha256']==o['source_locks']['semantic_discriminant_target_canonical_sha256']==csha(d)
    A=gram(p); assert det_bareiss(A)==-32
    assert p['picK_abs_discriminant']==32 and p['semantic_basis_index_in_picK']==1
    assert d['picK_discriminant_group']=='Z/4 direct_sum Z/8'

    got=[]
    for M,gp in reduced_candidates():
        got.append({'gram':M,'discriminant_group':gp,'compatible':gp=='Z/4 direct_sum Z/8'})
    assert got==o['gauss_reduced_even_positive_binary_det32_candidates']
    assert [x['gram'] for x in got if x['compatible']]==[[[4,0],[0,8]]]

    W=o['explicit_discriminant_anti_isometry_witness']; x,y=map(parsev,W['NS_images_semantic_fractional_coordinates'])
    assert order(x)==4 and order(y)==8 and W['NS_orders']==[4,8]
    assert mod2(pair(A,x,x))==Fraction(7,4)
    assert mod2(pair(A,y,y))==Fraction(15,8)
    assert mod1(pair(A,x,y))==0
    assert W['NS_q']==['7/4','15/8'] and W['NS_cross_mod_Z']=='0'
    H={addmod(x,y,a,b) for a in range(4) for b in range(8)}
    assert len(H)==32==W['generated_subgroup_size']
    assert W['T_q']==['1/4','1/8'] and W['T_cross']=='0'
    assert mod2(Fraction(1,4)+Fraction(7,4))==0
    assert mod2(Fraction(1,8)+Fraction(15,8))==0

    assert o['transcendental_lattice_isometry_gram']==[[4,0],[0,8]]
    assert o['transcendental_lattice_isometry_class_materialized'] is True
    assert o['transcendental_marking_materialized'] is False
    assert o['named_j2_mod2_functional_materialized'] is False
    assert o['j2_semantic_candidate_count_after_certificate']==3
    assert o['stage33_12_closed_exact'] is False and o['stage33_13_released'] is False
    for k in ('theorem_credit','receiver_credit','endpoint_credit','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
        assert o[k] is False
    assert o['canonical_sha256']==csha(o)
    print(json.dumps({'status':'PASS_EXACT','T_gram':[[4,0],[0,8]],'anti_isometry_subgroup_size':32,'canonical_sha256':o['canonical_sha256']},sort_keys=True))

if __name__=='__main__': main()
