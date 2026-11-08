"""Independent exact-mod243 Coleman disk test from independent C35-08 basepoint logs.
Underlying source E26 and F8 exact Mumford polynomials; no Claude Coleman routines.
"""
from c35_08_independent_lambda import F,P,N,M,K,FT,qm,vpint,le,lam,root,Y1
from math import comb
P5=3**5
l=[(z//3)%M for z in [v*pow(26,-1,M)%M for v in le]]
r=[(z//3)%M for z in lam]
print('L/3', [x%729 for x in l], 'Lam/3', [x%729 for x in r])
# g(t)=ft(root+t)/ft(root) and inverse square root; exact integer modular recurrence
f0=0
for c in FT[::-1]:f0=(f0*root+c)%M
assert f0%3==1
fi=pow(f0,-1,M);inv2=pow(2,-1,M)
g=[sum(FT[j]*comb(j,k)*pow(root,j-k,M) for j in range(k,len(FT)))*fi%M for k in range(7)]
assert g[0]==1
sqrt=[1]
for k in range(1,7):
    sqrt.append((g[k]-sum(sqrt[j]*sqrt[k-j] for j in range(1,k)))*inv2%M)
inv=[1]
for k in range(1,7):
    inv.append(-sum(sqrt[j]*inv[k-j] for j in range(1,k+1))%M)
ci=[]
for i in range(3):
    h=[]
    for n in range(6):
        # (root+z)^i*g(z)^-1/2 times 1/(2Y1)
        q=sum(comb(i,j)*pow(root,i-j,M)*inv[n-j] for j in range(min(n,i)+1))
        h.append(q*pow(2*Y1,-1,M)%M)
    ci.append(h)
A=[(l[1]*r[0]-l[0]*r[1])%P5]
B=[(l[2]*r[0]-l[0]*r[2])%P5]
for m in range(1,7):
    coef=qm(F(3**(m-1),m),P5)
    A.append((l[1]*ci[0][m-1]-l[0]*ci[1][m-1])*coef%P5)
    B.append((l[2]*ci[0][m-1]-l[0]*ci[2][m-1])*coef%P5)
print('A polynomial mod243',A)
print('B polynomial mod243',B)
assert A==[173,172,126,18,108,81,81]
assert B==[103,74,120,132,162,81,81]
def ev(c,x):
    a=0
    for y in c[::-1]:a=(a*x+y)%P5
    return a
ar=[t for t in range(P5) if ev(A,t)==0]
br=[t for t in range(P5) if ev(B,t)==0]
assert ar==[106] and br==[187]
print('A roots',ar,'B roots',br,'B(106)',ev(B,106),'A(187)',ev(A,187))
print('PASS_INDEPENDENT_MOD243_TWO_FUNCTION_DISK_NO_COMMON_ROOT')
