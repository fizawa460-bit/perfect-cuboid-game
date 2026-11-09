import json,sys,time
from pathlib import Path
DATA=Path(__file__).resolve().parent
(DATA/'rerun').mkdir(exist_ok=True)
from itertools import combinations,product
import numpy as np
from flint import fmpz_mat
sys.path.insert(0,str((DATA.parent/'parent391'/'parent390'/'parent389'/'parent388'/'parent381')))
from verify_row380 import prime_factors
HERE=DATA;O=(DATA/'rerun');data=json.loads((HERE/'scan_basis.json').read_text())
zk=list(zip(data['basis_numerators'],data['basis_denominators']))
E=np.array(json.loads((HERE/'embeddings.json').read_text()));E=E[...,0]+1j*E[...,1]
front=json.loads(((DATA.parent/'parent391')/'relation_certificate391.json').read_text())
start_idx,end_idx=int(sys.argv[1]),int(sys.argv[2]);prefix=f'shard{start_idx}_{end_idx}'
targets=front['remaining_formal_basis'][start_idx:end_idx]
seen=set();out=(O/(prefix+'_terms.jsonl')).open('w');start=time.perf_counter();left,right=np.triu_indices(105,1);abc=np.array(list(combinations(range(60),3))).T
quad=np.array(list(combinations(range(24),4))).T
saved_targets=[]
for ordinal,(q,j,N) in enumerate(targets):
 target_label=j
 _,ff=prime_factors(q);g=next(g for g,e,k in ff if k==j)
 f=g.degree();rho=-int(g[0])%q if f==1 else list(map(int,g))
 from flint import nmod_poly
 residues=[]
 for h,d in zk:
  r=nmod_poly([c*pow(d,-1,q)%q for c in h],q)%g
  residues.append([int(r[k]) for k in range(f)])
 piv={};selected=[]
 for i,col in enumerate(residues):
  v=col[:]
  for k,w in sorted(piv.items()):
   c=v[k]
   if c:v=[(a-c*b)%q for a,b in zip(v,w)]
  if any(v):
   k=next(k for k,c in enumerate(v) if c);inv=pow(v[k],-1,q);piv[k]=[c*inv%q for c in v];selected.append(i)
  if len(selected)==f:break
 assert len(selected)==f
 # Invert the selected f by f residue-column matrix.
 A=[[residues[selected[j]][i] for j in range(f)]+[int(i==j) for j in range(f)] for i in range(f)]
 for j in range(f):
  k=next(k for k in range(j,f) if A[k][j]);A[j],A[k]=A[k],A[j]
  inv=pow(A[j][j],-1,q);A[j]=[x*inv%q for x in A[j]]
  for k in range(f):
   if k!=j:
    c=A[k][j];A[k]=[(a-c*b)%q for a,b in zip(A[k],A[j])]
 Binv=[row[f:] for row in A]
 M=np.eye(105,dtype=np.int64)
 for i in range(105):
  if i in selected:M[i,i]=q;continue
  coeff=[sum(a*b for a,b in zip(row,residues[i]))%q for row in Binv]
  for k,c in zip(selected,coeff):M[i,k]=-(c-q if c>q//2 else c)
 assert all(all(sum(int(c)*residues[i][k] for i,c in enumerate(row))%q==0 for k in range(f)) for row in M)
 j=target_label
 R=M@E;R=np.column_stack((R[:,:7].real,np.sqrt(2)*R[:,7:].real,np.sqrt(2)*R[:,7:].imag));rng=np.random.default_rng(3920000+q*43+j);before=len(seen)
 for it in range(8):
  width=[0.0,1.1,2.3,4.7,7.9,12.1,3.7,8.3][it]
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
   for k in np.flatnonzero((ns>1.1)&(ns<2e17)):
    row=list(map(int,coeff(k)));sgn=next(x for x in row if x);row=tuple(-x for x in row) if sgn<0 else tuple(row)
    if row in seen:continue
    seen.add(row);out.write(json.dumps({'target':[q,j,rho],'trial':it,'approx_abs_norm':float(ns[k]),'terms':[[i,c] for i,c in enumerate(row) if c]},separators=(',',':'))+'\n')
  accept(B,lambda k:C[k])
  for s in [-1,1]:accept(B[left]+s*B[right],lambda k:C[left[k]]+s*C[right[k]])
  if it%3==0:
   a,b,c=abc
   for s,t in [(1,1),(1,-1),(-1,1),(-1,-1)]:accept(B[a]+s*B[b]+t*B[c],lambda k:C[a[k]]+s*C[b[k]]+t*C[c[k]])
  if it%4==0:
   aa,bb,cc,dd=quad
   for ss,tt,uu in product([-1,1],repeat=3):
    accept(B[aa]+ss*B[bb]+tt*B[cc]+uu*B[dd],lambda k:C[aa[k]]+ss*C[bb[k]]+tt*C[cc[k]]+uu*C[dd[k]])
 out.flush();saved_targets.append([q,j,rho]);print('target',ordinal+1,q,j,rho,'new',len(seen)-before,'total',len(seen),'seconds',round(time.perf_counter()-start,1),flush=True)
 (O/(prefix+'_targets.json')).write_text(json.dumps(saved_targets))
out.close()
