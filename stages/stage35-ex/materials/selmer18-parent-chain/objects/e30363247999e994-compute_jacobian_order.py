import json,time,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'_deps'))
from cypari2 import Pari
P=Path(__file__).resolve().parents[1]
source=P.parent/'r307_next_20261105/math/parents/rank6_divisors.json'
h=json.loads(source.read_text())['h2_coefficients_ascending']
pari=Pari();pari.allocatemem(536870912)
t=time.monotonic();f=pari.Polrev(h)
print('starting exact hyperellcharpoly, genus17, p163',flush=True)
c=pari.hyperellcharpoly(f*pari.Mod(1,163))
coeff=[int(c.polcoef(i))for i in range(35)];N=int(c(1))
out={'prime':163,'genus':17,'algorithm':'PARI hyperellcharpoly; untrusted discovery until independent certification','pari_version':str(pari('version()')),'characteristic_polynomial_ascending':coeff,'Jacobian_order':N,'order_mod163':N%163,'seconds':time.monotonic()-t}
(P/'exploratory/JACOBIAN_ORDER163_DISCOVERY.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out),flush=True)
