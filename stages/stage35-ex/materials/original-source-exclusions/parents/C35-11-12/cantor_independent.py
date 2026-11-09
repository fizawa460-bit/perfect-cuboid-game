import sympy as s,pickle
from pathlib import Path
x=s.Symbol('x'); Q=lambda a:s.Poly(a,x,domain=s.QQ)
f=Q(x**7+5*x**6-8*x**5+5*x**4-8*x**3+5*x**2-x)
O=(Q(1),Q(0))
def add(A,B):
 u,v=A;U,V=B
 a,b,d=s.gcdex(u,U); c,e,D=s.gcdex(d,v+V)
 h=(u*U).exquo(D*D);w=((c*a*u*V+c*b*U*v+e*(v*V+f)).exquo(D)).rem(h)
 while h.degree()>3:
  H=(f-w*w).exquo(h).monic();w=(-w).rem(H);h=H
 assert (w*w-f).rem(h).is_zero
 return h,w
D=(Q(x*x-x-1),Q(-4*x));T=(Q(x),Q(0))
def mul(n):
 a=O;b=D
 while n:
  if n&1:a=add(a,b)
  b=add(b,b);n//=2
 return a
for nm,A in [('E_26',mul(26)),('F_8',add(mul(8),T))]:
 # restricted loader: only Fraction globals allowed
 class Reader(pickle.Unpickler):
  def find_class(self,m,n):
   if (m,n)==('fractions','Fraction'):
    from fractions import Fraction
    return Fraction
   raise ValueError((m,n))
 with open(Path(__file__).parent/'coleman'/f'{nm}.pkl','rb') as h:u,v=Reader(h).load()
 U=Q(sum(s.Rational(c)*x**i for i,c in enumerate(u)));V=Q(sum(s.Rational(c)*x**i for i,c in enumerate(v)))
 assert A==(U,V),(nm,A,(U,V))
 print(nm,'INDEPENDENT_EXACT_CANTOR_MATCH')
