import json,sys,time
from pathlib import Path
DATA=Path(__file__).resolve().parent
(DATA/'rerun').mkdir(exist_ok=True)
from itertools import combinations,product
import numpy as np
from flint import fmpz_mat,nmod_mat,nmod_poly
sys.path.insert(0,str((DATA.parent/'parent391'/'parent390'/'parent389'/'parent388'/'parent381')))
from verify_row380 import prime_factors
HERE=(DATA/'rerun'); data=json.loads((DATA/'scan_basis.json').read_text())
zk=list(zip(data['basis_numerators'],data['basis_denominators']))
E=np.array(json.loads((DATA/'embeddings.json').read_text()));E=E[...,0]+1j*E[...,1]
pair=json.loads((DATA/'descent_pairs392.json').read_text())[int(sys.argv[1])];prefix='shardd'+sys.argv[1];targets=[pair['target']]
anchors=[]
for q,j in [pair['anchor']]:
 gn,ff=prime_factors(q);g=next(g for g,e,k in ff if k==j);assert g.degree()==1
 h,rem=divmod(gn,g);assert rem.is_zero()
 B=nmod_mat([[h0*pow(den,-1,q)%q for h0 in (num+[0]*(105-len(num)))] for num,den in zk],q)
 v=(nmod_mat([[int(h[k]) for k in range(105)]],q)*B.inv()).tolist()[0];v=list(map(int,v));k=next(k for k,x in enumerate(v) if x)
 v=[x*pow(v[k],-1,q)%q for x in v];v=[x-q if x>q//2 else x for x in v]
 Mq=np.eye(105,dtype=np.int64)*q;Mq[k]=v
 assert abs(int(fmpz_mat(Mq.tolist()).det()))==q**104
 # Every row of Mq lies in the complementary ideal (q)/Q: divisibility by G/(X-r) modulo q.
 for row in Mq:
  pol=nmod_poly([0],q)
  for i,c in enumerate(row):
   if c:pol+=int(c)*nmod_poly([a*pow(zk[i][1],-1,q)%q for a in zk[i][0]],q)
  assert (pol%h).is_zero()
 anchors.append((q,j,-int(g[0])%q,Mq))
seen=set();out=(HERE/(prefix+'_terms.jsonl')).open('w');start=time.perf_counter();left,right=np.triu_indices(105,1)
abc=np.array(list(combinations(range(22),3))).T;quad=np.array(list(combinations(range(12),4))).T;saved=[]
for ordinal,(p,j,N) in enumerate(targets):
 target_j=j;_,ff=prime_factors(p);g=next(g for g,e,k in ff if k==target_j);f=g.degree();rho=-int(g[0])%p if f==1 else list(map(int,g))
 residues=[]
 for h,d in zk:
  r=nmod_poly([c*pow(d,-1,p)%p for c in h],p)%g;residues.append([int(r[k]) for k in range(f)])
 before=len(seen);rng=np.random.default_rng(3910000+p*41+target_j);used_anchors=[]
 for it in range(12):
  q,qj,qr,Mq=anchors[it%len(anchors)];assert p!=q
  res=(Mq@np.array(residues,dtype=np.int64))%p;piv={};selected=[]
  for i,col in enumerate(res):
   v=list(map(int,col))
   for k,w in sorted(piv.items()):
    c=v[k]
    if c:v=[(a-c*b)%p for a,b in zip(v,w)]
   if any(v):
    k=next(k for k,c in enumerate(v) if c);inv=pow(v[k],-1,p);piv[k]=[c*inv%p for c in v];selected.append(i)
   if len(selected)==f:break
  assert len(selected)==f
  V=nmod_mat([[int(res[selected[col],row]) for col in range(f)] for row in range(f)],p).inv().tolist()
  Mp=np.eye(105,dtype=np.int64)
  for i in range(105):
   if i in selected:Mp[i,i]=p;continue
   coeff=[sum(int(a)*int(b) for a,b in zip(row,res[i]))%p for row in V]
   for k,c in zip(selected,coeff):Mp[i,k]=-(c-p if c>p//2 else c)
  M=Mp@Mq;M=np.array(fmpz_mat(M.tolist()).lll(delta=0.99).tolist(),dtype=np.int64);assert np.all((M@np.array(residues,dtype=np.int64))%p==0)
  R=M@E/q;R=np.column_stack((R[:,:7].real,np.sqrt(2)*R[:,7:].real,np.sqrt(2)*R[:,7:].imag))
  width=[1.5,3.1,6.1,10.5][it//3];scales=rng.uniform(-width,width,56)
  if it==0:scales[:]=0
  w=2.0**np.concatenate((scales,scales[7:]));A=R*w*1e9
  while np.max(np.abs(A))>2**60:A/=10
  _,U=fmpz_mat(np.round(A).astype(np.int64).tolist()).lll(transform=True,delta=0.99);z=U.tolist()
  assert max(abs(int(x)) for row in z for x in row)*int(np.max(np.abs(M)))*105<2**59
  C=np.array(z,dtype=np.int64)@M;B=C@E/q
  def accept(vals,coeff):
   a=np.abs(vals);ns=a[:,:7].prod(1)*np.square(a[:,7:].prod(1))
   for k in np.flatnonzero((ns>1e-8)&(ns<2e17)):
    row=list(map(int,coeff(k)));sgn=next(x for x in row if x);row=tuple(-x for x in row) if sgn<0 else tuple(row)
    if row in seen:continue
    seen.add(row);out.write(json.dumps({'target':[p,target_j,rho],'anchor':[q,qj,qr],'method':'large_prime_pair_descent','fractional_ideal':'P/Q','fractional_denominator':q,'trial':it,'approx_fractional_abs_norm':float(ns[k]),'terms':[[i,c] for i,c in enumerate(row) if c]},separators=(',',':'))+'\n')
  accept(B,lambda k:C[k])
  for s in [-1,1]:accept(B[left]+s*B[right],lambda k:C[left[k]]+s*C[right[k]])
  if it%3==0:
   a,b,c=abc
   for s,t in [(1,1),(1,-1),(-1,1),(-1,-1)]:accept(B[a]+s*B[b]+t*B[c],lambda k:C[a[k]]+s*C[b[k]]+t*C[c[k]])
  if it%6==0:
   aa,bb,cc,dd=quad
   for s,t,u in product([-1,1],repeat=3):accept(B[aa]+s*B[bb]+t*B[cc]+u*B[dd],lambda k:C[aa[k]]+s*C[bb[k]]+t*C[cc[k]]+u*C[dd[k]])
  used_anchors.append([q,qj,qr])
 out.flush();saved.append({'target':[p,target_j,rho],'trials':12,'anchors':used_anchors})
 (HERE/(prefix+'_targets.json')).write_text(json.dumps(saved))
 print('target',ordinal+1,p,target_j,rho,'new',len(seen)-before,'total',len(seen),'seconds',round(time.perf_counter()-start,1),flush=True)
out.close()
