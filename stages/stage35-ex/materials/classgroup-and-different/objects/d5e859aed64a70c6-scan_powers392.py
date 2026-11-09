import json,sys,time
from pathlib import Path
DATA=Path(__file__).resolve().parent
(DATA/'rerun').mkdir(exist_ok=True)
from itertools import combinations,product
import numpy as np
from flint import fmpz_mat
sys.path.insert(0,str((DATA.parent/'parent391'/'parent390'/'parent389'/'parent388'/'parent381')))
from verify_row380 import prime_factors,G
HERE=DATA;O=(DATA/'rerun')
d=json.loads((HERE/'scan_basis.json').read_text());zk=list(zip(d['basis_numerators'],d['basis_denominators']));assert zk[0]==([1],1)
E=np.array(json.loads((HERE/'embeddings.json').read_text()));E=E[...,0]+1j*E[...,1]
front=json.loads(((DATA.parent/'parent391')/'relation_certificate391.json').read_text())['remaining_formal_basis']
a,b=int(sys.argv[1]),int(sys.argv[2]);prefix=f'shardp{a}_{b}';out=(O/(prefix+'_terms.jsonl')).open('w');seen=set();saved=[];start=time.perf_counter()
left,right=np.triu_indices(105,1);abc=np.array(list(combinations(range(40),3))).T;quad=np.array(list(combinations(range(20),4))).T
gc=list(map(int,G));gd=[i*c for i,c in enumerate(gc)][1:]
def ev(h,x,m):
 v=0
 for c in reversed(h):v=(v*x+c)%m
 return v
for ordinal,(p,j,N) in enumerate(front[a:b]):
 target_j=j;_,ff=prime_factors(p);g=next(g for g,e,k in ff if k==j);assert g.degree()==1 and N==p
 rho=-int(g[0])%p;der=pow(ev(gd,rho,p),-1,p);lifts={1:rho};m=p;r=rho
 for k in range(2,8):
  correction=ev(gc,r,m*p)//m;r=(r-correction*der*m)%(m*p);m*=p;assert ev(gc,r,m)==0;lifts[k]=r
 before=len(seen);trace=[]
 for power in [3,5,7]:
  modulus=p**power;r=lifts[power];res=[ev(h,r,modulus)*pow(den,-1,modulus)%modulus for h,den in zk]
  M=[[int(i==k) for k in range(105)] for i in range(105)];M[0][0]=modulus
  for i in range(1,105):M[i][0]=-(res[i]-modulus if res[i]>modulus//2 else res[i])
  # Exact coordinate LLL avoids huge/cancelling HNF entries before floating point embeddings.
  M=fmpz_mat(M).lll(delta=0.99).tolist();assert max(abs(int(x)) for row in M for x in row)<2**30
  assert all(sum(int(c)*res[i] for i,c in enumerate(row))%modulus==0 for row in M)
  assert abs(int(fmpz_mat(M).det()))==modulus
  M=np.array(M,dtype=np.int64);R=M@E;R=np.column_stack((R[:,:7].real,np.sqrt(2)*R[:,7:].real,np.sqrt(2)*R[:,7:].imag))
  rng=np.random.default_rng(3921000+p*43+target_j+power*997)
  for it in range(4):
   width=[0.0,2.0,4.0,7.0][it];scales=rng.uniform(-width,width,56);w=2.0**np.concatenate((scales,scales[7:]));A=R*w*1e9
   while np.max(np.abs(A))>2**60:A/=10
   _,U=fmpz_mat(np.round(A).astype(np.int64).tolist()).lll(transform=True,delta=0.99);u=U.tolist()
   assert max(abs(int(x)) for row in u for x in row)*int(np.max(np.abs(M)))*105<2**59
   C=np.array(u,dtype=np.int64)@M;B=C@E;trial_best=[]
   def accept(vals,coeff):
    v=np.abs(vals);ns=v[:,:7].prod(1)*np.square(v[:,7:].prod(1));ratio=ns/float(modulus)
    for k in sorted(np.flatnonzero((ratio>0.01)&(ratio<2e24)),key=lambda k:ratio[k])[:3]:
     row=list(map(int,coeff(k)));sgn=next(x for x in row if x);row=tuple(-x for x in row) if sgn<0 else tuple(row)
     trial_best.append((float(ratio[k]),row))
   accept(B,lambda k:C[k])
   for s in [-1,1]:accept(B[left]+s*B[right],lambda k:C[left[k]]+s*C[right[k]])
   if it%2==0:
    aa,bb,cc=abc
    for s,t in product([-1,1],repeat=2):accept(B[aa]+s*B[bb]+t*B[cc],lambda k:C[aa[k]]+s*C[bb[k]]+t*C[cc[k]])
   if it==0:
    aa,bb,cc,dd=quad
    for s,t,u in product([-1,1],repeat=3):accept(B[aa]+s*B[bb]+t*B[cc]+u*B[dd],lambda k:C[aa[k]]+s*C[bb[k]]+t*C[cc[k]]+u*C[dd[k]])
   for ratio,row in sorted(trial_best)[:12]:
    if row in seen:continue
    seen.add(row);out.write(json.dumps({'target':[p,target_j,rho],'power':power,'lifted_root':r,'ideal_norm':modulus,'trial':it,'method':'odd_prime_ideal_powers','approx_norm_ratio':ratio,'terms':[[i,c] for i,c in enumerate(row) if c]},separators=(',',':'))+'\n')
  trace.append({'power':power,'lifted_root':r,'modulus':modulus,'trials':4})
 out.flush();saved.append({'target':[p,target_j,rho],'powers':trace});(O/(prefix+'_targets.json')).write_text(json.dumps(saved))
 print('target',ordinal+1,p,target_j,rho,'new',len(seen)-before,'total',len(seen),'seconds',round(time.perf_counter()-start,1),flush=True)
out.close()
