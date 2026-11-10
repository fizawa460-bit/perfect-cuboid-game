"""Finite discovery for the requested prime-ideal targets; not exhaustive."""
import json,sys,time,itertools,math
from pathlib import Path
import numpy as np
from flint import fmpz_mat,nmod_poly
BASE=Path(__file__).resolve().parents[1]/'row393';OUT=Path(__file__).resolve().parent
PARENT=BASE/'parent392/parent391/parent390/parent389/parent388/parent381'
sys.path.insert(0,str(PARENT));from verify_row380 import prime_factors
if not __debug__:raise RuntimeError('Python -O is unsupported')
bas=json.loads((BASE/'discovery/scan_basis.json').read_text());zk=list(zip(bas['basis_numerators'],bas['basis_denominators']))
EE=np.array(json.loads((BASE/'discovery/embeddings.json').read_text()));EE=EE[...,0]+1j*EE[...,1]
target=[tuple(map(int,z.split(':'))) for z in sys.argv[1].split(',')];tag='_'.join(f'{p}-{j}' for p,j in target);res=[];roots=[]
for p,j in target:
 _,factors=prime_factors(p);g=next(g for g,e,k in factors if k==j);assert g.degree()==1
 rt=-int(g[0])%p;roots.append(rt)
 res.append([int(nmod_poly([c*pow(den,-1,p)%p for c in h],p)%g) if False else int((nmod_poly([c*pow(den,-1,p)%p for c in h],p)%g)[0]) for h,den in zk])
N=math.prod(p for p,j in target)
rr=[sum(v*(N//p)*pow(N//p,-1,p) for v,(p,j) in zip(vs,target))%N for vs in zip(*res)]
k=next(k for k,t in enumerate(rr) if math.gcd(t,N)==1);iv=pow(rr[k],-1,N)
M=[[int(i==j) for j in range(105)] for i in range(105)];M[k][k]=N
for i in range(105):
 if i!=k:
  c=rr[i]*iv%N;M[i][k]=-(c-N if c>N//2 else c)
assert all(sum(c*v for c,v in zip(row,rr))%N==0 for row in M)
# Reduce integer coefficient lengths first, before floating embedding evaluation.
MM=fmpz_mat(M).lll(delta=0.99);M=MM.tolist()
assert abs(int(MM.det()))==N
assert all(sum(c*v for c,v in zip(row,rr))%N==0 for row in M)
R=np.array(M,dtype=float)@EE;R=np.column_stack((R[:,:7].real,np.sqrt(2)*R[:,7:].real,np.sqrt(2)*R[:,7:].imag))
left,right=np.triu_indices(105,1);abc=np.array(list(itertools.combinations(range(64),3))).T;quad=np.array(list(itertools.combinations(range(48),4))).T
seen=set();out=open(OUT/f'{tag}_terms.jsonl','w');rng=np.random.default_rng(202611106000+sum(p*(j+1) for p,j in target));start=time.perf_counter()
for it in range(48):
 width=[2.3,4.7,7.1,10.9,13.7,5.9][it%6];scales=rng.uniform(-width,width,56)
 if it%3==0:
  scales=np.zeros(56);ids=rng.choice(56,8,replace=False);scales[ids]=rng.uniform(-width,width,8)
 w=2.0**np.concatenate((scales,scales[7:]));A=R*w*1e9
 while np.max(np.abs(A))>2**59:A/=10
 _,U=fmpz_mat(np.round(A).astype(np.int64).tolist()).lll(transform=True,delta=0.99)
 CC=(U*MM).tolist();C=np.array(CC,dtype=np.int64);BB=C.astype(float)@EE
 assert all(sum(c*v for c,v in zip(row,rr))%N==0 for row in CC)
 def accept(vals,coeff):
  ab=np.abs(vals);ns=ab[:,:7].prod(1)*np.square(ab[:,7:].prod(1))
  for k in np.flatnonzero((ns>N*0.99)&(ns<5e24)):
   row=list(map(int,coeff(k)));g=math.gcd(*row);row=[x//g for x in row]
   if next(x for x in row if x)<0:row=[-x for x in row]
   tup=tuple(row)
   if tup in seen:continue
   if any(sum(c*v for c,v in zip(row,rs))%p for rs,(p,j) in zip(res,target)):continue
   seen.add(tup);out.write(json.dumps(dict(target=target,trial=it,approx_abs_norm=float(ns[k]),method='complement_wave6',terms=[[i,c] for i,c in enumerate(row) if c]),separators=(',',':'))+'\n')
 accept(BB,lambda k:C[k])
 for sg in [-1,1]:accept(BB[left]+sg*BB[right],lambda k:C[left[k]]+sg*C[right[k]])
 if it%2==0:
  a,b,c=abc
  for sg,tg in itertools.product([-1,1],repeat=2):accept(BB[a]+sg*BB[b]+tg*BB[c],lambda k:C[a[k]]+sg*C[b[k]]+tg*C[c[k]])
 if it%4==0:
  a,b,c,d=quad
  for sg,tg,ug in itertools.product([-1,1],repeat=3):accept(BB[a]+sg*BB[b]+tg*BB[c]+ug*BB[d],lambda k:C[a[k]]+sg*C[b[k]]+tg*C[c[k]]+ug*C[d[k]])
 out.flush();print('trial',it+1,'candidates',len(seen),'seconds',round(time.perf_counter()-start,2),flush=True)
out.close();json.dump(dict(target=target,roots=roots,ideal_norm=N,coefficient_basis_det=N,candidates=len(seen),trials=48,complete=False),open(OUT/f'{tag}_result.json','w'),indent=2)
