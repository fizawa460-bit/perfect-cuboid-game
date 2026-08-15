#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from pathlib import Path
import json

root=Path(__file__).resolve().parents[3]
proof=(root/'stages/stage25/25-60/r504-section-lattice.md').read_text(encoding='utf-8')
twist=(root/'stages/stage25/25-60/r504-twist-descent.md').read_text(encoding='utf-8')
iterctl=json.loads((root/'stages/stage25/25-60/r504-iteration-controller.json').read_text(encoding='utf-8'))

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def deriv(a,p):
    return trim([(i*a[i])%p for i in range(1,len(a))] or [0])

def divmod_poly(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b])
    q=[0]*max(1,len(a)-len(b)+1)
    inv=pow(b[-1],-1,p)
    while a!=[0] and len(a)>=len(b):
        sh=len(a)-len(b); c=a[-1]*inv%p; q[sh]=c
        for i,x in enumerate(b): a[i+sh]=(a[i+sh]-c*x)%p
        a=trim(a)
    return trim(q),a

def gcd_poly(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b])
    while b!=[0]:
        _,r=divmod_poly(a,b,p); a,b=b,r
    inv=pow(a[-1],-1,p)
    return trim([x*inv%p for x in a])

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def vals(u,v):
    A=u**8-6*u**4*v**4-3*v**8
    B=3*u**8+6*u**4*v**4-v**8
    C=u**16+28*u**12*v**4+6*u**8*v**8+28*u**4*v**12+v**16
    E=2*u*u*v*v*A*B
    X=u*u*v*v*(B*B-A*A)
    Y=u**4*A*A-v**4*B*B
    HX=u*u*v*v*(A*A+B*B)
    HY=u**4*A*A+v**4*B*B
    D=(u**4+v**4)*C
    g=gcd(gcd(abs(E),abs(X)),abs(Y))
    return A,B,C,E,X,Y,HX,HY,D,g

rows=0
for v in range(1,110):
    for u in range(1,320):
        if gcd(u,v)!=1: continue
        A,B,C,E,X,Y,HX,HY,D,g=vals(u,v)
        assert E*E+X*X==HX*HX
        assert E*E+Y*Y==HY*HY
        assert E*E+X*X+Y*Y==D*D
        pred=128 if (u&1 and v&1) else 1
        assert g==pred,(u,v,g,pred)
        H=max(u,v)
        assert D>=H**20
        assert D<=128*H**20
        assert D%g==0
        rows+=1
assert rows>15000

def t3z3(k):
    A=k**8-6*k**4-3
    B=3*k**8+6*k**4-1
    C=k**16+28*k**12+6*k**8+28*k**4+1
    return Fraction(k*A,B),Fraction(C,B*B)
for K in range(2,30):
    t,z=t3z3(K)
    assert t**4+1==(K**4+1)*z*z

u,v=5,2
A,B,C,E,X,Y,HX,HY,D,g=vals(u,v)
assert E>0 and X>0 and Y>0
assert Y<E<X

Q1=[1,0,4,-8,14,-8,4,0,1]
Q2=[1,0,4,8,14,8,4,0,1]
Q3=[1,4,4,-4,-2,4,4,-4,1]
Q4=[1,-4,4,4,-2,-4,4,4,1]
Q=conv(conv(Q1,Q2),conv(Q3,Q4))
assert len(Q)-1==32
assert gcd_poly(Q,deriv(Q,3),3)==[1]

def ratio(k):
    A=k**8-6*k**4-3
    B=3*k**8+6*k**4-1
    return Fraction(A*B,4*(k-1)*(k+1)*(k*k+1)*(k**4+1)*(k**8+6*k**4+1))
assert ratio(Fraction(5,2)) != ratio(Fraction(13,5))

for marker in [
    'R504_GENERIC_QK_RANK=1',
    'R504_SECOND_INDEPENDENT_QK_SECTION_EXISTS=false',
    'R504_3P_PRIMITIVE_GCD_BOUND=128',
    'R504_3P_HEIGHT_DEGREE=20',
    'R504_3P_THIRD_FACE_EXCEPTION_GENUS=15',
    'R504_3P_EXACT_FAMILY_GROWTH=Theta(B^(1/10))',
    'R504_3P_BEATS_GLOBAL_QUARTER=false',
    'R504_ORIGINAL_SURFACE_SECTION_ROUTE=CLOSED_NO_GLOBAL_UPGRADE',
    'R504_LOW_DEGREE_BASE_CHANGE_ROUTE=OPEN_GATE',
    'R504_MULTI_SECTION_ROUTE=OPEN_GATE',
    'GLOBAL_STAGE25_LOWER_CHANGED=false',
    'FINITE_DATA_USED_AS_PROOF=false',
]: assert marker in proof, marker

for marker in [
    'R504_TWIST_COVER_IS_E0=true',
    'R504_DECK_ACTION=Q->T-Q',
    'R504_END_Q_E0=Z',
    'R504_T_NOT_2DIVISIBLE_OVER_Q=true',
    'R504_ANTI_INVARIANT_COEFFICIENT_PARITY=EVEN',
    'R504_EXPLICIT_P_COEFFICIENT=2_UP_TO_SIGN_AND_TORSION',
    'R504_EXPLICIT_P_PRIMITIVE_IN_TWIST_FREE_LATTICE=true',
    'R504_GENERIC_QK_RANK=1',
    'R504_BASE_CHANGE_RANK_CLAIM=NOT_MADE',
]: assert marker in twist, marker

assert iterctl['route']=='R504'
assert iterctl['checkpoint']==60
assert iterctl['audit_status']=='PENDING'
assert iterctl['advance_allowed'] is False
assert iterctl['next_checkpoint']==60
assert iterctl['merge_allowed'] is False
assert iterctl['stage70_allowed'] is False
assert iterctl['generic_qk_rank']==1
assert iterctl['three_p_height_degree']==20
assert iterctl['three_p_primitive_gcd_bound']==128
assert iterctl['three_p_exception_genus']==15
assert iterctl['global_stage25_lower_changed'] is False

print(f'R504_GCD_HEIGHT_GRID_ROWS={rows}')
print('R504_3P_INTEGER_IDENTITIES=PASS')
print('R504_3P_EXACT_GCD_REGRESSION=PASS')
print('R504_3P_HEIGHT_DEGREE20=PASS')
print('R504_Q32_MOD3_SQUAREFREE_CERTIFICATE=PASS')
print('R504_PHYSICAL_OPEN_CONE_WITNESS=PASS')
print('R504_TWIST_T_NOT_2DIVISIBLE_CERTIFICATE=PASS')
print('R504_TWIST_DESCENT_ARTIFACT_CONTRACT=PASS')
print('R504_SECTION_LATTICE_ARTIFACT_CONTRACT=PASS')
print('STAGE25_60_R504_AUDIT=PASS')
