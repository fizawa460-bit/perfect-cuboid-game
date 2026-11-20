# E25 audit (section 4): for a Mobius U, |B ∩ U(B)| is never 5, so |B Δ U(B)| ∈ {0} ∪ [4, inf).
# Exact arithmetic in Q(i) (pairs of Fractions). Every U with |B∩U(B)| >= 3 sends some ordered triple of B
# into B, so the 120 x 120 ordered-triple pairs cover all of them; the rest have |B Δ U(B)| >= 8.
import itertools
from fractions import Fraction as Fr
class G:
    __slots__=('r','i')
    def __init__(s,r,i=0): s.r=Fr(r); s.i=Fr(i)
    def __add__(s,o): return G(s.r+o.r,s.i+o.i)
    def __sub__(s,o): return G(s.r-o.r,s.i-o.i)
    def __mul__(s,o): return G(s.r*o.r-s.i*o.i,s.r*o.i+s.i*o.r)
    def inv(s): d=s.r*s.r+s.i*s.i; return G(s.r/d,-s.i/d)
    def __truediv__(s,o): return s*o.inv()
    def z(s): return s.r==0 and s.i==0
O,ONE=G(0),G(1)
H=[(O,ONE),(ONE,O),(ONE,ONE),(G(-1),ONE),(G(0,1),ONE),(G(0,-1),ONE)]   # 0, inf, 1, -1, i, -i
def frame(p):
    (a0,a1),(b0,b1),(c0,c1)=p
    det=a0*b1-b0*a1; l0=(c0*b1-b0*c1)/det; l1=(a0*c1-c0*a1)/det
    return [[a0*l0,b0*l1],[a1*l0,b1*l1]]
def mul(A,B): return [[A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]],
                      [A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def inv(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d,(O-A[0][1])/d],[(O-A[1][0])/d,A[0][0]/d]]
def same(u,v): return (u[0]*v[1]-u[1]*v[0]).z()
hist={}
for tx in itertools.permutations(range(6),3):
    Fx=inv(frame([H[k] for k in tx]))
    for ty in itertools.permutations(range(6),3):
        M=mul(frame([H[k] for k in ty]),Fx)
        c=0
        for z in H:
            w=(M[0][0]*z[0]+M[0][1]*z[1],M[1][0]*z[0]+M[1][1]*z[1])
            if any(same(w,v) for v in H): c+=1
        hist[c]=hist.get(c,0)+1
print('|B ∩ U(B)| over all triple-determined U (counted with multiplicity):',dict(sorted(hist.items())))
print('PASS' if 5 not in hist else 'FAIL', ': |B∩U(B)|=5 never occurs')
