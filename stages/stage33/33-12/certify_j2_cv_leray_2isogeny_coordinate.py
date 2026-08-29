#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
p=HERE/'j2-cv-leray-2isogeny-coordinate.json'
cert=json.loads(p.read_text(encoding='utf-8'))

# Dependency-free exact polynomial arithmetic in Z[t], low-degree first.
def add(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i in range(n): out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def scale(a,c): return [c*x for x in a]

t2=[0,0,1]
t4=[0,0,0,0,1]
one=[1]
H=add(add(t4,scale(t2,-4)),one)                       # t^4-4t^2+1
q=add(add(t4,scale(t2,-6)),one)                       # t^4-6t^2+1
Dp=add(add(t2,[ -1]),[0,-2])                          # t^2-2t-1
Dm=add(add(t2,[ -1]),[0, 2])                          # t^2+2t-1
t2m1=add(t2,[-1])
D=mul(mul(t2m1,t2m1),q)

assert mul(Dp,Dm)==q
assert sub(sub(mul(H,H),D),scale(t4,4))==[0]
# Full rational 2-torsion factorization:
# X*(X-(t^2-1)^2)*(X-q) expands to X*(X^2-2H*X+D).
r1=mul(t2m1,t2m1)
assert add(r1,q)==scale(H,2)
assert mul(r1,q)==D

# M/K norm. beta+beta'=-H/t^2, beta*beta'=1.
# c=t^4-4t^2+2=H+1 and
# Norm(t^2*beta+c)=t^4-c*H+c^2=2*(t^2-1)^2.
c=add(H,one)
norm_num=add(sub(t4,mul(c,H)),mul(c,c))
assert norm_num==scale(mul(t2m1,t2m1),2)
# ell has factor 4/((t^2-1)Dplus), hence Norm_M/K(ell)=16*norm_num/((t^2-1)^2 Dplus^2)=32/Dplus^2.
# Therefore its K-squareclass is exactly 2.

assert cert['cv_input']['ell_J2_in_M'] is True
assert cert['cv_input']['ell_J2_iota_invariant'] is True
assert cert['cv_input']['norm_M_over_K']=='32/(t^2-2*t-1)^2'
assert cert['cv_input']['norm_M_squareclass']=='2'
assert cert['partition_to_weierstrass']['T_iota_on_scaled_model']=='(U,V)=(0,0)'
assert cert['partition_to_weierstrass']['T_iota_on_polynomial_model']=='(X,Y)=(0,0)'
ex=cert['exact_conclusion']
assert ex['two_isogeny_kernel_membership_certified'] is True
assert ex['j2_2isogeny_squareclass_selected'] is True
assert ex['j2_2isogeny_squareclass']=='d=2'
assert ex['j2_torsor_equation_materialized'] is True
assert ex['marked_Brauer_functional_selected'] is False
assert cert['stage33_12_closed_exact'] is False
assert cert['stage33_13_released'] is False
claimed=cert.pop('canonical_sha256')
actual=hashlib.sha256(json.dumps(cert,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert claimed==actual,(claimed,actual)
assert claimed=='52a3e741fbe6158a2a9434c9797207f6e126fc7d9df2ab09a80d3edd5e005771'
print('PASS',claimed)
