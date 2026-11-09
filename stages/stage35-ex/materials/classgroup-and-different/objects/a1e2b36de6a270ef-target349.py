import sys,json,time
from pathlib import Path
from math import lcm,gcd
from cypari2 import Pari
from flint import fmpz_poly
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'parent381'))
from verify_row380 import G
p=Pari();p.allocatemem(160000000,2000000000);p.set_real_precision(75);p.setrand(388)
x=p('x');poly=p.Polrev(list(map(int,G)));basis=[(x-1)**i/2**(i//3) for i in range(105)]
bad=[2,199,11385628289870903,83743632872646893,278122000170586522903289,128315161223632986986799118753,14758359995285977308443723270301431340936632015367331820639800963]
t=time.perf_counter();nf=p.nfinit([poly,basis,bad]);print('nf',round(time.perf_counter()-t,1),flush=True)
Ps=[I for I in p.idealprimedec(nf,349,1) if p.idealval(nf,x-178,I)>0];assert len(Ps)==1
res=[]
for exp in [9,11,13,17,21]:
 I=p.idealpow(nf,Ps[0],exp)
 for style in range(3):
  direction=([0]*56 if style==0 else [((i*7+exp)%5) if style==1 else (6 if i in [0,7,23,48] else 0) for i in range(56)])
  J,c=p.idealred(nf,[I,1],direction)
  n=int(p.idealnorm(nf,J));a=p.nfbasistoalg(nf,c).lift();cs=list(a.Vecrev()) if a.type()=='t_POL' else [a];d=lcm(*(int(z.denominator()) for z in cs));h=[int(z*d) for z in cs];cont=gcd(*h);h=[z//cont for z in h]
  res.append({'prime':349,'label':2,'rho_residue':178,'exponent':exp,'style':style,'reduced_ideal_norm':n,'coefficients':h})
  print('reduction',exp,style,n,round(time.perf_counter()-t,1),flush=True)
  Path(__file__).with_name('target349_candidates.json').write_text(json.dumps(res,separators=(',',':')))
