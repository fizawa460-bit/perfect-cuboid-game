#!/usr/bin/env python3
from pathlib import Path
from flint import fmpz_poly,fmpz_mat
import json
HERE=Path(__file__).resolve().parent
read=lambda name:json.loads((HERE/name).read_text())
c=read('different392.json')
curve=read('parent391/parent390/parent389/parent388/parent381/curve_C29.json')
X=fmpz_poly([0,1]);A=fmpz_poly(curve['A_star_ascending']);B=fmpz_poly(curve['B_star_ascending']);G=A(-X*X)+X*B(-X*X);H=G(X+1)
assert abs(int(G.resultant(G.derivative())))==c['derivative_norm_abs']
R=fmpz_poly([1]);coeff=[]
for m in range(311):coeff.append(int(R[104]));R=R*X%H
assert coeff==c['trace_coefficients_m0_to310']
C=[]
for i in range(105):
    row=[]
    for j in range(105):
        d=2**(i//3+j//3);a=coeff[i+j+102];assert a%d==0;row.append(a//d)
    C.append(row)
assert C==c['scaled_trace_matrix'] and int(fmpz_mat(C).det())==1
assert abs(int(H[0]))==2**35
print('PASS exact derivative resultant, all trace entries, FLINT determinant 1')
