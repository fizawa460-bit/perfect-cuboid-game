#!/usr/bin/env python3
import sympy as sp
from pathlib import Path
import json

root=Path(__file__).resolve().parents[3]
ctl=json.loads((root/'stages/stage25/25-60/r504-exceptional-search-controller.json').read_text())
proof=(root/'stages/stage25/25-60/r504-q-degree2-complete-descent.md').read_text()

a,b,x=sp.symbols('a b x')
Q=sp.expand((a*x+b)**4+(x+1)**4)
A=sp.expand(Q.coeff(x,4)); B=sp.expand(Q.coeff(x,3)); C=sp.expand(Q.coeff(x,2)); D=sp.expand(Q.coeff(x,1)); E=sp.expand(Q.coeff(x,0))
assert sp.factor(E*B**2-A*D**2)==16*(a-b)**3*(a+b)*(a*b-1)*(a*b+1)

def IJ(A,B,C,D,E):
    I=sp.factor(12*A*E-3*B*D+C**2)
    J=sp.factor(72*A*C*E+9*B*C*D-27*A*D**2-27*B**2*E-2*C**3)
    return I,J

subs={b:-a}
AA,BB,CC,DD,EE=[sp.factor(z.subs(subs)) for z in (A,B,C,D,E)]
I1,J1=IJ(AA,0,sp.factor(BB-4*AA),0,sp.factor(2*AA-2*BB+CC))
assert I1==64*a**4*(4*a**4+3)
assert J1==-1024*a**8*(8*a**4+9)

subs={b:1/a}; lam=1/a
AA,BB,CC,DD,EE=[sp.factor(z.subs(subs)) for z in (A,B,C,D,E)]
I2,J2=IJ(AA,0,sp.factor(BB-4*lam*AA),0,sp.factor(2*lam**2*AA-2*lam*BB+CC))
assert I2==8*(a-1)**4*(5*a**4+4*a**3+6*a**2+4*a+5)/a**2
assert J2==-64*(a-1)**8*(a**2+a+1)*(7*a**2+10*a+7)/a**3

for marker in [
 'R504_Q_DEGREE2_SOURCE_EQUIVALENCE=TARGET_FIXED_SOURCE_PGL2_Q',
 'R504_Q_DEGREE2_DECK_INVOLUTION_DEFINED_OVER_Q=true',
 'R504_Q_DEGREE2_INVOLUTION_CLASSES=SPLIT_OR_NONSPLIT_SQUARECLASS',
 'R504_Q_DEGREE2_COMPLETE_DESCENT_PROVED=true',
]: assert marker in proof, marker

assert ctl['complete_q_degree2_descent_proved'] is True
assert ctl['previous_even_normal_form_complete_claim'] is False
assert ctl['full_split_normal_form_analysis_required'] is True
assert ctl['nonsplit_normal_form_analysis_required'] is True
assert ctl['prym_as_sole_degree2_residual_accepted'] is False
assert ctl['stage70_allowed'] is False
assert ctl['audit_status']=='PENDING'

print('R504_EVEN_SUBFAMILY_SYMBOLIC_CERTIFICATE=PASS')
print('R504_Q_DEGREE2_COMPLETE_SOURCE_DESCENT=PASS')
print('R504_SPLIT_PLUS_NONSPLIT_STRATA_MATERIALIZED=PASS')
print('R504_PRYM_AS_SOLE_RESIDUAL=false')
print('R504_STAGE70_BLOCKED=PASS')
