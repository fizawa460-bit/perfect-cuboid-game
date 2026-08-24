#!/usr/bin/env python3
"""Scan several genuine Q_2 endpoint lifts for the pulled-back K_c J2 class."""
import hashlib
import json
import pathlib
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
MAGMA_URL='https://magma.maths.usyd.edu.au/xml/calculator.xml'
T=2
S_VALUES=[3,5,7,8,9,11,13]

def v2_unit(n):
    n=abs(int(n)); k=0
    while n and n%2==0:
        k+=1; n//=2
    return k,n

def q2_square(n):
    if n==0:return True
    k,u=v2_unit(n)
    return k%2==0 and u%8==1

points=[]
for s in S_VALUES:
    F=T*T*(1-s*s)**2+s*s*(1-T*T)**2
    D=(1-T*T)**2*(1-s*s)**2+4*F
    if not (q2_square(F) and q2_square(D)):
        raise SystemExit(f'candidate {(T,s)} lost Q2 endpoint lift')
    points.append({'t':T,'s':s,'w_squared':F,'space_diagonal_squared':D})

# At t=2 all evaluations lie in the same quartic branch number field, so the
# expensive local factorization above 2 is done once.
ss=','.join(map(str,S_VALUES))
code=f'''
Q := Rationals();
P<x> := PolynomialRing(Q);
f := x^4 + (1/4)*x^2 + 1;
assert IsIrreducible(f);
L<a> := NumberField(f);
OL := MaximalOrder(L);
ell := L!(-(16*a^2+8)/3);
fac := Factorization(2*OL);
printf "STAGE33_07_J2_SCAN_BEGIN\\n";
printf "PRIME_COUNT=%o\\n", #fac;
for s in [{ss}] do
  rhs := L!(s-a);
  hs := [ HilbertSymbol(ell, rhs, pp[1]) : pp in fac ];
  prod := &*hs;
  printf "S=%o HS=%o PRODUCT=%o\\n", s, hs, prod;
end for;
printf "STAGE33_07_J2_SCAN_END\\n";
'''
payload=urllib.parse.urlencode({'input':code}).encode()
req=urllib.request.Request(MAGMA_URL,data=payload,headers={
    'Content-Type':'application/x-www-form-urlencoded','Accept':'text/html, application/xml, application/xhtml+xml',
    'Referer':'https://magma.maths.usyd.edu.au/calc/','User-Agent':'perfect-cuboid-stage33/2.4'},method='POST')
with urllib.request.urlopen(req,timeout=180) as resp:
    raw=resp.read().decode('utf-8',errors='replace')
root=ET.fromstring(raw);lines=[]
for result in root.findall('.//results'):
    for line in result.findall('.//line'):lines.append(''.join(line.itertext()))
stdout='\n'.join(lines)+'\n'
(ROOT/'j2-q2-variation-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_J2_SCAN_END' not in stdout or any(b in stdout for b in ('Runtime error','Internal error','Assertion failed','User error')):
    print(stdout);raise SystemExit('J2 Q2 variation scan failed')
rows=[]
for m in re.finditer(r'^S=(\d+) HS=\[(.*?)\] PRODUCT=(-?\d+)$',stdout,re.M):
    s=int(m.group(1));hs=[int(x.strip()) for x in m.group(2).split(',') if x.strip()];prod=int(m.group(3))
    rows.append({'s':s,'hilbert_symbols':hs,'product':prod,'invariant':'1/2' if prod==-1 else '0'})
if [r['s'] for r in rows]!=S_VALUES or any(r['product'] not in (-1,1) for r in rows):
    print(stdout);raise SystemExit('incomplete J2 scan parse')
products={r['product'] for r in rows}
cert={
 'schema':'STAGE33_07_J2_ENDPOINT_Q2_VARIATION_SCAN_V1',
 'source_locks':{
   'stage33_05_j2':'stages/stage33/33-05/j2_arithmetic_descent.py',
   'stage33_07_nonzero_witness':'stages/stage33/33-07/probe_j2_endpoint_q2.py',
   'endpoint_equations':'c^2=e^2+x^2+y^2; e=(1-t^2)(1-s^2), x=2t(1-s^2), y=2s(1-t^2)',
   'local_corestriction_law':'inv_Q2(Cor A)=sum inv above 2',
 },
 'test_points':points,
 'evaluations':rows,
 'both_invariants_0_and_half_observed':products=={-1,1},
 'evaluation_nonconstant_on_endpoint_Q2_locus_certified':products=={-1,1},
 'what_this_alone_proves':'the pulled-back arithmetic J2 class is not a constant Br(Q) class if both invariants occur',
 'what_this_alone_does_not_prove':'boundary-unramifiedness/proper extension is certified separately before duplicate separation',
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(canonical).hexdigest()
(ROOT/'j2-endpoint-q2-variation.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps(cert,indent=2,sort_keys=True))
