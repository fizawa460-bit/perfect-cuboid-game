import json,sys,time
from pathlib import Path
from math import lcm,gcd
import numpy as np
from flint import fmpz_mat,fmpz_poly,fmpz
from cypari2 import Pari
HERE=Path(__file__).resolve().parent;ROOT=HERE/'rerun';ROOT.mkdir(exist_ok=True);parent=HERE
p=Pari();z=p((parent/'embed_basis.txt').read_text());basis=[]
for a in z:
 cs=list(a.Vecrev()) if a.type()=='t_POL' else [a];d=lcm(*(int(t.denominator()) for t in cs));basis.append((fmpz_poly([int(t*d) for t in cs]),d))
embed=np.array(json.loads((parent/'embeddings.json').read_text()));embed=embed[...,0]+1j*embed[...,1]
assert embed.shape==(105,56)
q=349;rho=178
res=[int(h(rho))%q*pow(d,-1,q)%q for h,d in basis]
pivot=next(i for i,x in enumerate(res) if x)
M=np.eye(105,dtype=np.int64);M[pivot,pivot]=q
for i,r in enumerate(res):
 if i==pivot:continue
 a=r*pow(res[pivot],-1,q)%q
 if a>q//2:a-=q
 M[i,pivot]=-a
assert all(sum(int(c)*r for c,r in zip(row,res))%q==0 for row in M)
Iembed=M@embed;R=np.column_stack((Iembed[:,:7].real,np.sqrt(2)*Iembed[:,7:].real,np.sqrt(2)*Iembed[:,7:].imag))
left,right=np.triu_indices(105,1)
rng=np.random.default_rng(389349);seen=set();rows=[];start=time.perf_counter()
output=(ROOT/'target349_terms.jsonl').open('w')
for it in range(int(sys.argv[1])):
 width=[1.1,2.2,3.5,5.5,8.5,12.5][it%6]
 scales=np.zeros(56) if it%3==0 else rng.uniform(-width,width,56)
 if it%3==0:
  choose=rng.choice(56,size=int(rng.integers(2,16)),replace=False);scales[choose]=rng.uniform(-width,width,len(choose))
 w=2.0**np.concatenate((scales,scales[7:]));floating=R*w*1e9
 assert np.max(np.abs(floating))<9e18
 _,U=fmpz_mat(np.round(floating).astype(np.int64).tolist()).lll(transform=True,delta=0.99)
 Ulist=U.tolist();assert max(abs(int(x)) for row in Ulist for x in row)<2**40
 C=np.array(Ulist,dtype=np.int64)@M;B=C@embed
 def accept(vals,coef):
  a=np.abs(vals);ns=a[:,:7].prod(1)*np.square(a[:,7:].prod(1))
  for j in np.flatnonzero((ns>1.1)&(ns<2e15)):
   c=tuple(map(int,coef(j)))
   if c in seen or tuple(-v for v in c) in seen:continue
   seen.add(c);output.write(json.dumps({'approx_abs_norm':float(ns[j]),'terms':[[i,v] for i,v in enumerate(c) if v]},separators=(',',':'))+'\n')
 accept(B,lambda i:C[i])
 for s in [-1,1]:accept(B[left]+s*B[right],lambda i:C[left[i]]+s*C[right[i]])
 output.flush();print('scan',it+1,'candidates',len(seen),'seconds',round(time.perf_counter()-start,1),flush=True)
output.close()
(ROOT/'scan_basis.json').write_text(json.dumps({'basis_numerators':[[int(c) for c in h] for h,d in basis],'basis_denominators':[d for h,d in basis],'prime':q,'rho':rho,'basis_residues':res,'ideal_coordinate_basis':M.tolist()},separators=(',',':')))
