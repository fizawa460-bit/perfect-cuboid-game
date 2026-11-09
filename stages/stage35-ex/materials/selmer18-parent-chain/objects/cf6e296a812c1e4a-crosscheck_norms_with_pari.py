"""Optional independent backend for ALL saved generator and unit norms.
No class group, BNF, GRH or floating-point conclusion is used.
"""
from pathlib import Path
import json,sys,os,time
R=Path(__file__).resolve().parent
if os.environ.get('STAGE35EX_DEPS'):sys.path.insert(0,os.environ['STAGE35EX_DEPS'])
from cypari2 import Pari
p=Pari();p.allocatemem(268435456)
parent=json.loads((R/'parents/row359_three_units.json').read_text());F=p.Polrev(parent['V_minimal_polynomial_ascending']);x=p('x');basis=[(x-1)**j/p(2)**(j//3)for j in range(36)];nf=p.nfinit([F,basis]);start=time.monotonic();count=0
pr=json.loads((R/'principal_prime_generators.json').read_text())
for r in pr['records']:
 a=p.Polrev(r['numerator'])/r['denominator']
 if p.nfeltnorm(nf,a)!=r['norm']:raise ArithmeticError('PARI prime-generator norm mismatch')
 count+=1
un=json.loads((R/'full_unit_basis_definitions.json').read_text())
for u in un['units']:
 a=p.Polrev([p(z)for z in u['coefficients_V']])
 if p.nfeltnorm(nf,a)!=u['norm']:raise ArithmeticError('PARI unit norm mismatch')
 count+=1
out={'status':'PASS_EXACT_PARI_BACKEND_CROSSCHECK','prime_generators':len(pr['records']),'ordinary_units':len(un['units']),'norm_identities':count,'bnfinit_used':False,'GRH_used':False,'whole_MW_U_constructed':False,'independent_mathematical_audit':'PENDING_NOT_RUN','seconds':round(time.monotonic()-start,3)}
(R/'PARI_NORM_CROSSCHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
