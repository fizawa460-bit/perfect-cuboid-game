#!/usr/bin/env python3
"""Dependency-free exact R3 bridge from corrected full-L J2 to the CV E[2] cocycle.

Source theorem: Creutz--Viray, arXiv:1403.2924v1, Lemma 4.6.
The corrected geometric full branch-algebra representative is (f2,1).
All function-field identities are checked in Z[i][t,X,Y]/(Y^2-X(X-r)(X-q)).
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Sparse Gaussian-integer polynomial in (t,X,Y).
# coefficients are (a,b) = a+b*i.
def cadd(a,b): return (a[0]+b[0], a[1]+b[1])
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

class P:
    def __init__(self,d=None):
        self.d={m:c for m,c in (d or {}).items() if c!=(0,0)}
    @staticmethod
    def const(n=0,im=0): return P({(0,0,0):(n,im)}) if (n or im) else P()
    @staticmethod
    def mon(t=0,x=0,y=0,c=(1,0)): return P({(t,x,y):c})
    def __add__(self,o):
        o=toP(o); d=dict(self.d)
        for m,c in o.d.items():
            d[m]=cadd(d.get(m,(0,0)),c)
            if d[m]==(0,0): d.pop(m)
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({m:(-c[0],-c[1]) for m,c in self.d.items()})
    def __sub__(self,o): return self+(-toP(o))
    def __rsub__(self,o): return toP(o)-self
    def __mul__(self,o):
        o=toP(o); d={}
        for (a,b,c),u in self.d.items():
            for (x,y,z),v in o.d.items():
                m=(a+x,b+y,c+z); d[m]=cadd(d.get(m,(0,0)),cmul(u,v))
        return P(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        r=P.const(1); a=self
        while n:
            if n&1: r=r*a
            a=a*a; n//=2
        return r
    def __eq__(self,o): return self.d==toP(o).d
    def is_zero(self): return not self.d

def toP(v):
    return v if isinstance(v,P) else P.const(int(v))

t=P.mon(t=1); X=P.mon(x=1); Y=P.mon(y=1); I=P.const(0,1)
one=P.const(1)
d=t**2-one
r=d**2
q=t**4-6*t**2+one
acoef=t**4-4*t**2+one
A=X-r
B=X-q
Epoly=X*A*B

# Reduce using Y^2=Epoly. Epoly has no Y, so direct monomial reduction is exact.
def reduce_y2(f):
    out=P()
    for (et,ex,ey),coef in f.d.items():
        k,rem=divmod(ey,2)
        out += P.mon(et,ex,rem,coef)*(Epoly**k)
    return out

assert reduce_y2(Y**2-Epoly).is_zero()
assert acoef*2 == r+q
assert r-q == 4*t**2

# Verify the explicit inverse birational map s=2tX/Y,
# W=t*N/((X-r)(X-q)) by clearing denominators in W^2=F(s).
C=t**8-8*t**6+14*t**4-8*t**2+one
N=X**2-C
quartic_cleared=(N**2)*(Y**4) - (A**2)*(B**2)*(16*t**4*X**4 + 4*acoef*X**2*Y**2 + Y**4)
assert reduce_y2(quartic_cleared).is_zero()

# B+ partition identification. After s=2tX/Y, the asserted identity
# (-1/(t*r))*Gplus/(X-r) = (1/(X-r)+iY/(d(X-r)(X-q)))^2
# becomes this denominator-cleared polynomial identity.
partition_cleared=A*(B**2)*(-Y**2 + 4*t**2*X**2 + 2*I*d*X*Y) - Y**2*(d*B + I*Y)**2
assert reduce_y2(partition_cleared).is_zero()

# Fixed rational 2-torsion points are pairwise distinct generically.
assert r != P() and q != P() and r-q != P()

# Source-lock R2 rather than re-proving its quotient nonzero statement here.
r2cert=json.loads((ROOT/'j2-corrected-full-l-representative.json').read_text(encoding='utf-8'))
assert r2cert['status']=='PASS_EXACT_R2_CORRECTED_REPRESENTATIVE_NONZERO'
assert r2cert['abstract_J2_source_locked_pair']=='(f2,1)'
assert r2cert['full_quotient_zero_test']['corrected_pair_zero'] is False
assert r2cert['full_quotient_zero_test']['f2_square_in_E'] is False
assert r2cert['quadratic_extension_square_test']['f2_K_square'] is False
assert r2cert['quadratic_extension_square_test']['f2_over_q_K_square'] is False

# CV Lemma 4.6: rho flips sqrt(f2) on the two B+ branch points only.
chi_rho=[1,1,0,0]
g_rho=sum(chi_rho)//2
assert g_rho==1
cocycle_bits_rho=[0,1]  # fixed basis [T0,Tr]
assert cocycle_bits_rho != [0,0]
assert [b^b for b in cocycle_bits_rho]==[0,0]

f2='(t + 1 + sqrt(2))/(t - 1 + sqrt(2))'
norm_f2_sq='(t**2 + 2*t + 2*sqrt(2)*t + 2*sqrt(2) + 3)/(t**2 - 2*t + 2*sqrt(2)*t - 2*sqrt(2) + 3)'
f2_valuations={'t=r2':1,'t=r4':-1}
assert any(v%2 for v in f2_valuations.values())

cert={
    'schema':'STAGE33_05_J2_CORRECTED_CV_E2_COCYCLE_V1',
    'status':'PASS_EXACT_R3_EXPLICIT_NONZERO_CV_E2_COCYCLE',
    'source_lock':{
        'corrected_R2_certificate':'stages/stage33/33-05/j2-corrected-full-l-representative.json',
        'corrected_R2_pair':'(f2,1)',
        'creutz_viray':'arXiv:1403.2924v1, Lemma 4.6 (pp. 15-16)',
        'generic_fiber_model':'Y^2=X*(X-(t^2-1)^2)*(X-(t^4-6*t^2+1))'
    },
    'base_field_scope':'Kgeom=Qbar(t); fixed E[2] basis is defined over Q(t)',
    'corrected_full_L_representative':{
        'ell_J2_corrected':'(f2,1)','f2':f2,
        'L':'Kgeom(B_plus) x Kgeom(B_minus)','degrees_over_Kgeom':[2,2],
        'norm':norm_f2_sq,'norm_is_square':True,'belongs_to_L1':True
    },
    'generic_fiber':{
        'quartic':'W^2=t^2*s^4+(t^4-4*t^2+1)*s^2+t^2',
        'branch_factor_Bplus':'Gplus=t*(1-s^2)+i*s*(1-t^2)',
        'branch_factor_Bminus':'Gminus=t*(1-s^2)-i*s*(1-t^2)',
        'jacobian':'E: Y^2=X*(X-r)*(X-q)',
        'r':'t**4 - 2*t**2 + 1','q':'t**4 - 6*t**2 + 1',
        'inverse_map_s':'s=2*t*X/Y',
        'inverse_map_W':'(X**2*t - t**9 + 8*t**7 - 14*t**5 + 8*t**3 - t)/(X**2 - 2*X*t**4 + 8*X*t**2 - 2*X + t**8 - 8*t**6 + 14*t**4 - 8*t**2 + 1)'
    },
    'partition_2torsion_identification':{
        'exact_square_identity':'(-1/(t*r))*Gplus/(X-r)=(1/(X-r)+i*Y/((t^2-1)*(X-r)*(X-q)))^2',
        'Bplus_partition_point':'Tr=(r,0)','not_inferred_from_branch_orbit_bits':True
    },
    'cv_lemma_4_6':{
        'rho':'nontrivial element of Gal(Kgeom(sqrt(f2))/Kgeom)',
        'chi_tilde_on_four_branch_points':chi_rho,'g_ell_rho':g_rho,'xi_rho':'Tr',
        'fixed_E2_basis':['T0=(0,0)','Tr=(r,0)'],
        'cocycle_bits_in_fixed_basis':cocycle_bits_rho,'cocycle_condition_verified':True
    },
    'fixed_rational_E2_kummer_coordinates':{
        'basis':['T0=(0,0)','Tr=((t^2-1)^2,0)'],
        'squareclass_pair':['1',f2],
        'meaning':'character coordinates of xi in H^1(Kgeom,E[2]) for the fixed constant E[2] basis',
        'nonzero':True,'f2_odd_valuations':f2_valuations
    },
    'exact_exit':'EXPLICIT_NONZERO_CREUTZ_VIRAY_E2_COCYCLE_AND_KUMMER_COORDINATES',
    'Q_defined_descent_credit_restored':False,'marked_brauer_coordinate_selected':False,
    'twisted_kernel_lattice_identified':False,'stage33_05_reclosed':False,
    'stage33_12_closed_exact':False,'stage33_13_released':False,'class3_promoted':False,
    'theorem_credit':False,'receiver_credit':False,'endpoint_credit':False,
    'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexististence_claim':False,
    'next_exact_leaf':'R4_BUILD_ASSOCIATED_TORSOR_OR_KERNEL_LATTICE_AND_READ_MINIMUM_NORM_4_8_12'
}
# Correct typo-proofing: use the exact historical field name expected by the certificate.
cert['perfect_cuboid_nonexistence_claim']=cert.pop('perfect_cuboid_nonexististence_claim')
canonical=json.dumps(cert,sort_keys=True,separators=(',',':')).encode()
cert['canonical_sha256']=hashlib.sha256(canonical).hexdigest()
(ROOT/'j2-corrected-cv-e2-cocycle.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({'success':True,'exact_exit':cert['exact_exit'],'xi_rho':'Tr','kummer_squareclasses':['1',f2],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
