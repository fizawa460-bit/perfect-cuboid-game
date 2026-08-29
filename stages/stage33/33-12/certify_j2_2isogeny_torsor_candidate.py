#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parent
p=ROOT/'j2-2isogeny-torsor-candidate.json'
cert=json.loads(p.read_text(encoding='utf-8'))
t=sp.symbols('t')
H=t**4-4*t**2+1
q=t**4-6*t**2+1
Dp=t**2-2*t-1
Dm=t**2+2*t-1
D=(t**2-1)**2*q
assert sp.expand(q-Dp*Dm)==0
assert sp.expand(H**2-D-4*t**4)==0
# For E:y^2=x(x^2+a x+b), quotient by (0,0) is
# Ehat:y^2=x(x^2-2a x+(a^2-4b)); here a=-2H,b=D.
a=-2*H;b=D
assert sp.expand(-2*a-4*H)==0
assert sp.expand(a**2-4*b-16*t**4)==0
# Standard 2-isogeny homogeneous-space template with d=Dp.
assert sp.simplify(D/Dp-(t**2-1)**2*Dm)==0
assert cert['candidate_torsor_equation']=="N^2=Dplus*U^4-2*H*U^2*V^2+(t^2-1)^2*Dminus*V^4"
assert cert['named_j2_identification_certified'] is False
assert cert['candidate_count_after']==3
assert cert['route_status']=='BLOCKED_NEW_PATTERN_ISOLATED'
claimed=cert.pop('canonical_sha256')
canonical=json.dumps(cert,sort_keys=True,separators=(',',':')).encode()
actual=hashlib.sha256(canonical).hexdigest()
assert actual==claimed,(actual,claimed)
print('PASS',claimed)
