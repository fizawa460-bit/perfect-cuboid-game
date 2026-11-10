"""Finite discovery only: QR ideal, not an exhaustive class group computation."""
import json,sys,time,itertools,math
from pathlib import Path
import numpy as np
from flint import fmpz_mat,nmod_poly,nmod_mat
BASE=Path(__file__).resolve().parents[1]/'row393';OUT=Path(__file__).resolve().parent
PARENT=BASE/'parent392/parent391/parent390/parent389/parent388/parent381'
sys.path.insert(0,str(PARENT));from verify_row380 import prime_factors,G
if not __debug__:raise RuntimeError('Python -O is unsupported')
bas=json.loads((BASE/'discovery/scan_basis.json').read_text());zk=list(zip(bas['basis_numerators'],bas['basis_denominators']))
EE=np.array(json.loads((BASE/'discovery/embeddings.json').read_text()));EE=EE[...,0]+1j*EE[...,1]
target=[(667801,3),(15849133,0)];res=[];roots=[]
for p,j in target:
 _,factors=prime_factors(p);g=next(g for g,e,k in factors if k==j);assert g.degree()==1
 rt=-int(g[0])%p;roots.append(rt)
 res.append([int(nmod_poly([c*pow(den,-1,p)%p for c in h],p)%g) if False else int((nmod_poly([c*pow(den,-1,p)%p for c in h],p)%g)[0]) for h,den in zk])
q,r=[x[0] for x in target];N=q*r**104
power_rows=[]
for h,den in zk:
 hp=[c*pow(den,-1,r)%r for c in h]+[0]*(105-len(h));power_rows.append(hp)
Gmod=nmod_poly(list(map(int,G)),r);H,rem=divmod(Gmod,nmod_poly([-roots[1],1],r));assert rem==0
hpower=[int(H[j]) for j in range(105)]
hvec=(nmod_mat([hpower],r)*nmod_mat(power_rows,r).inv()).tolist()[0];hvec=list(map(int,hvec))
k=next(k for k,t in enumerate(hvec) if t);iv=pow(hvec[k],-1,r);hvec=[t*iv%r for t in hvec];hvec=[t-r if t>r//2 else t for t in hvec]
MR=[[r*int(i==j) for j in range(105)] for i in range(105)];MR[k]=hvec
rq=[sum(c*v for c,v in zip(row,res[0]))%q for row in MR];l=next(j for j,t in enumerate(rq) if t);iv=pow(rq[l],-1,q)
MQ=[[int(i==j) for j in range(105)] for i in range(105)];MQ[l][l]=q
for i in range(105):
 if i!=l:
  c=rq[i]*iv%q;MQ[i][l]=-(c-q if c>q//2 else c)
MM=(fmpz_mat(MQ)*fmpz_mat(MR)).lll(delta=0.99);M=MM.tolist()
assert abs(int(MM.det()))==N
assert all(sum(c*v for c,v in zip(row,res[0]))%q==0 for row in M)
assert all(all((row[j]-row[k]*hvec[j])%r==0 for j in range(105)) for row in M)
R=(np.array(M,dtype=float)/r)@EE;R=np.column_stack((R[:,:7].real,np.sqrt(2)*R[:,7:].real,np.sqrt(2)*R[:,7:].imag))
left,right=np.triu_indices(105,1);abc=np.array(list(itertools.combinations(range(64),3))).T;quad=np.array(list(itertools.combinations(range(24),4))).T
seen=set();out=open(OUT/'inverse_terms.jsonl','w');rng=np.random.default_rng(39482715849133);start=time.perf_counter()
for it in range(24):
 width=[2.3,4.7,7.1,10.9,13.7,5.9][it%6];scales=rng.uniform(-width,width,56)
 if it%3==0:
  scales=np.zeros(56);ids=rng.choice(56,8,replace=False);scales[ids]=rng.uniform(-width,width,8)
 w=2.0**np.concatenate((scales,scales[7:]));A=R*w*1e9
 while np.max(np.abs(A))>2**59:A/=10
 _,U=fmpz_mat(np.round(A).astype(np.int64).tolist()).lll(transform=True,delta=0.99)
 CC=(U*MM).tolist();C=np.array(CC,dtype=np.int64);BB=(C.astype(float)/r)@EE
 assert all(sum(c*v for c,v in zip(row,res[0]))%q==0 for row in CC)
 assert all(all((row[j]-row[k]*hvec[j])%r==0 for j in range(105)) for row in CC)
 def accept(vals,coeff):
  ab=np.abs(vals);ns=ab[:,:7].prod(1)*np.square(ab[:,7:].prod(1))
  for k in np.flatnonzero((ns>(q/r)*0.99)&(ns<5e19)):
   row=list(map(int,coeff(k)));g=math.gcd(*row);row=[x//g for x in row]
   if next(x for x in row if x)<0:row=[-x for x in row]
   tup=tuple(row)
   if tup in seen:continue
   seen.add(tup);out.write(json.dumps(dict(target=target,trial=it,approx_abs_norm=float(ns[k]),method='new_Q667801_R15849133_inverse_pair_ideal',odd_denominator=r,terms=[[i,c] for i,c in enumerate(row) if c]),separators=(',',':'))+'\n')
 accept(BB,lambda k:C[k])
 for sg in [-1,1]:accept(BB[left]+sg*BB[right],lambda k:C[left[k]]+sg*C[right[k]])
 if it%2==0:
  a,b,c=abc
  for sg,tg in itertools.product([-1,1],repeat=2):accept(BB[a]+sg*BB[b]+tg*BB[c],lambda k:C[a[k]]+sg*C[b[k]]+tg*C[c[k]])
 if it%4==0:
  a,b,c,d=quad
  for sg,tg,ug in itertools.product([-1,1],repeat=3):accept(BB[a]+sg*BB[b]+tg*BB[c]+ug*BB[d],lambda k:C[a[k]]+sg*C[b[k]]+tg*C[c[k]]+ug*C[d[k]])
 out.flush();print('trial',it+1,'candidates',len(seen),'seconds',round(time.perf_counter()-start,2),flush=True)
out.close();json.dump(dict(target=target,roots=roots,ideal_norm=N,coefficient_basis_det=N,candidates=len(seen),trials=24,complete=False),open(OUT/'inverse_scan_result.json','w'),indent=2)
