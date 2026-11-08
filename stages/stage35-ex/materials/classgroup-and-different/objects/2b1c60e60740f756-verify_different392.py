#!/usr/bin/env python3
"""Pure Python exact trace-dual/different certificate; no numerical arithmetic."""
from pathlib import Path
from math import comb
import json,sys,hashlib
HERE=Path(__file__).resolve().parent

def det_bareiss(M):
    a=[r[:] for r in M];n=len(a);sign=1;previous=1
    for k in range(n-1):
        row=next(i for i in range(k,n) if a[i][k])
        if row!=k:a[k],a[row]=a[row],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            x=a[i][k]
            for j in range(k+1,n):
                v=a[i][j]*pivot-x*a[k][j]
                assert v%previous==0
                a[i][j]=v//previous
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

def main():
    cert=json.loads((HERE/'different392.json').read_text())
    curve=json.loads((HERE/'parent391'/'parent390'/'parent389'/'parent388'/'parent381'/'curve_C29.json').read_text())
    G=[0]*106
    for i,c in enumerate(curve['A_star_ascending']):G[2*i]=c*(-1)**i
    for i,c in enumerate(curve['B_star_ascending']):G[2*i+1]=c*(-1)**i
    assert G[105]==1
    H=[sum(G[j]*comb(j,i) for j in range(i,106)) for i in range(106)]
    assert H[0]==-2**35 and sum(i//3 for i in range(105))==1785
    # Coefficient of t^104 in t^m mod H(t), for m=0,...,310.
    rem=[1]+[0]*104;coeff=[]
    for m in range(311):
        coeff.append(rem[104]);lead=rem[104]
        rem=[-lead*H[0]]+[rem[j-1]-lead*H[j] for j in range(1,105)]
    assert coeff==cert['trace_coefficients_m0_to310']
    C=[]
    for i in range(105):
        row=[]
        for j in range(105):
            numerator=coeff[i+j+102];den=2**(i//3+j//3)
            assert numerator%den==0
            row.append(numerator//den)
        C.append(row)
    assert C==cert['scaled_trace_matrix']
    determinant=det_bareiss(C)
    assert determinant==cert['scaled_trace_det']==1
    # The trace-pairing matrix identifies delta^-1 O_K with the complete dual.
    D=cert['absolute_discriminant']
    assert cert['norm_t_abs']==2**35 and cert['index_of_power_order']==2**1785
    assert cert['derivative_norm_abs']==2**3570*D
    assert cert['derivative_norm_abs']==cert['norm_different_generator_abs']*cert['norm_t_abs']**102
    assert cert['norm_different_generator_abs']==D
    ext=json.loads((HERE/'different_extension392.json').read_text())
    raw=(HERE/'parent_row374_results.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()==ext['parent_row374_source_sha256']
    parent=json.loads(raw);p=ext['p'];assert p in parent['odd_discriminant_primes_all_exponent_one'] and p>10**9
    assert abs(int(parent['field_discriminant']))==D and D%p==0 and D%(p*p)!=0
    root=ext['double_root_of_G']
    def trim(a):
        while a and not a[-1]:a.pop()
        return a
    def remainder(a,b):
        a=trim([x%p for x in a]);b=trim([x%p for x in b]);inv=pow(b[-1],-1,p)
        while len(a)>=len(b):
            q=a[-1]*inv%p;shift=len(a)-len(b)
            for j,c in enumerate(b):a[shift+j]=(a[shift+j]-q*c)%p
            trim(a)
        return a
    A=[x%p for x in G];B=[i*G[i]%p for i in range(1,106)]
    while B:A,B=B,remainder(A,B)
    inv=pow(A[-1],-1,p);A=[c*inv%p for c in A]
    assert A==[(-root)%p,1]
    assert sum(c*pow(root,i,p*p) for i,c in enumerate(G))%(p*p)==p*ext['G_at_root_div_p_mod_p'] and ext['G_at_root_div_p_mod_p']%p!=0
    assert root%p!=1
    factors=json.loads((HERE/'factorizations392.json').read_text());assert max(map(int,factors))<=10**9
    profiles=json.loads((HERE/'new_relations392.json').read_text())
    assert all(q<=10**9 for row in profiles for q,e in row['odd_factorization'])
    print(json.dumps({'trace_matrix_size':105,'all_entries_integral':True,'scaled_trace_determinant':determinant,
        'codifferent':'((rho-1)^102/G_prime(rho))*O_K','different':'(G_prime(rho)/(rho-1)^102)*O_K',
        'ordinary_different_ideal_class_zero':True,'new_odd_valuation_coordinate_prime':p,'adjoining_different_preserves_closure_intersection_V':True,'no_classgroup_generation_conclusion':True},indent=2))
if __name__=='__main__':main()
