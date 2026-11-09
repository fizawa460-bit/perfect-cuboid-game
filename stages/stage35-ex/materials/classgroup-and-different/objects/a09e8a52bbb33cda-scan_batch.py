import json,sys,time
from pathlib import Path
from itertools import combinations
import numpy as np
from flint import fmpz_mat
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'parent388'/'parent381'))
from verify_row380 import prime_factors
HERE=Path(__file__).resolve().parent;O=HERE/'rerun';O.mkdir(exist_ok=True);data=json.loads((HERE/'scan_basis.json').read_text())
zk=list(zip(data['basis_numerators'],data['basis_denominators']))
E=np.array(json.loads((HERE/'embeddings.json').read_text()));E=E[...,0]+1j*E[...,1]
front=json.loads((HERE.parent/'parent388'/'frontier388.json').read_text())
targets=front['selected_prime_ideal_labels_and_norms'][1:1+int(sys.argv[1])]
seen=set();out=(O/'batch_terms.jsonl').open('w');start=time.perf_counter();left,right=np.triu_indices(105,1);abc=np.array(list(combinations(range(18),3))).T
saved_targets=[]
for ordinal,(q,j,N) in enumerate(targets):
 _,ff=prime_factors(q);g=next(g for g,e,k in ff if k==j)
 if g.degree()!=1:continue
 rho=-int(g[0])%q;res=[sum(c*pow(rho,i,q) for i,c in enumerate(h))%q*pow(d,-1,q)%q for h,d in zk]
 pivot=next(i for i,r in enumerate(res) if r);M=np.eye(105,dtype=np.int64);M[pivot,pivot]=q
 for i,r in enumerate(res):
  if i!=pivot:
   a=r*pow(res[pivot],-1,q)%q;M[i,pivot]=-(a-q if a>q//2 else a)
 assert all(sum(int(c)*r for c,r in zip(row,res))%q==0 for row in M)
 R=M@E;R=np.column_stack((R[:,:7].real,np.sqrt(2)*R[:,7:].real,np.sqrt(2)*R[:,7:].imag));rng=np.random.default_rng(3890000+q*17+j);before=len(seen)
 for it in range(18):
  width=[1.1,2.2,3.5,5.5,8.5,12.5][it%6]
  scales=np.zeros(56) if it%3==0 else rng.uniform(-width,width,56)
  if it%3==0:
   chosen=rng.choice(56,size=int(rng.integers(2,16)),replace=False);scales[chosen]=rng.uniform(-width,width,len(chosen))
  w=2.0**np.concatenate((scales,scales[7:]));A=R*w*1e9
  while np.max(np.abs(A))>2**60:A/=10
  _,U=fmpz_mat(np.round(A).astype(np.int64).tolist()).lll(transform=True,delta=0.99)
  z=U.tolist();assert max(abs(int(x)) for r in z for x in r)<2**40
  C=np.array(z,dtype=np.int64)@M;B=C@E
  def accept(vals,coeff):
   a=np.abs(vals);ns=a[:,:7].prod(1)*np.square(a[:,7:].prod(1))
   for k in np.flatnonzero((ns>1.1)&(ns<2e15)):
    row=list(map(int,coeff(k)));sgn=next(x for x in row if x);row=tuple(-x for x in row) if sgn<0 else tuple(row)
    if row in seen:continue
    seen.add(row);out.write(json.dumps({'target':[q,j,rho],'approx_abs_norm':float(ns[k]),'terms':[[i,c] for i,c in enumerate(row) if c]},separators=(',',':'))+'\n')
  accept(B,lambda k:C[k])
  for s in [-1,1]:accept(B[left]+s*B[right],lambda k:C[left[k]]+s*C[right[k]])
  if it%6==0:
   a,b,c=abc
   for s,t in [(1,1),(1,-1),(-1,1),(-1,-1)]:accept(B[a]+s*B[b]+t*B[c],lambda k:C[a[k]]+s*C[b[k]]+t*C[c[k]])
 out.flush();saved_targets.append([q,j,rho]);print('target',ordinal+1,q,j,rho,'new',len(seen)-before,'total',len(seen),'seconds',round(time.perf_counter()-start,1),flush=True)
 (O/'batch_targets.json').write_text(json.dumps(saved_targets))
out.close()
