"""Exact enumeration certificate via a quartic Hurwitz parameter; no point matching."""
import sympy as s,itertools,json
k,t=s.symbols('k t');I=s.I
B=[s.Integer(0),s.oo,s.Integer(1),-s.Integer(1),I,-I]
def h(z):return (s.Integer(1),s.Integer(0)) if z is s.oo else (z,s.Integer(1))
def det(u,v):return s.expand(u[0]*v[1]-u[1]*v[0])
P=t*t*((2*k-1)*t+2-3*k);Q=t-k
res=s.factor(s.resultant(P,Q,t));assert res==-2*k**2*(k-1)**2
# infinity has index2; remaining derivative roots 0,1,c.
assert s.factor(s.diff(P,t)*Q-P*s.diff(Q,t))==2*t*(t-1)*(2*k*t-3*k**2+2*k-t)
c=k*(3*k-2)/(2*k-1)
assert s.cancel(P.subs(t,c)/Q.subs(t,c))==s.cancel(k*(3*k-2)**3/(2*k-1))
rows=[]
for ids in itertools.combinations(range(6),4):
 A,C,D,E=[h(B[j]) for j in ids]
 # N(A)=0, N(C)=infinity, N(D)=1; lambda=N(E).
 z=s.cancel(det(E,A)*det(D,C)/(det(E,C)*det(D,A)))
 H=s.Poly(k*(3*k-2)**3-z*(2*k-1),k,extension=I)
 assert H.degree()==4 and s.gcd(H,H.diff()).degree()==0
 # Disallow degree drop, collisions, and denominator zero.
 bad=s.Poly(k*(k-1)*(2*k-1)*(3*k-2)*(3*k-1),k,extension=I)
 assert s.gcd(H,bad).degree()==0
 assert s.gcd(H,s.Poly(res,k,extension=I)).degree()==0
 rows.append({'critical_value_indices':ids,'cross_ratio':str(z),'quartic':str(H.as_expr()),'distinct_genuine_maps':4})
out={'status':'PASS_ENUMERATION_ONLY','degree2_count':15,'degree3_count':60,'base_field':'Q(i)','map_field':'Q(i)[k]/irreducible factor of listed quartic','rows':rows,'pair_matching_23_33':'NOT_RUN'}
print(json.dumps(out,indent=2));open('degree3_enumeration_result.json','w').write(json.dumps(out,indent=2))
