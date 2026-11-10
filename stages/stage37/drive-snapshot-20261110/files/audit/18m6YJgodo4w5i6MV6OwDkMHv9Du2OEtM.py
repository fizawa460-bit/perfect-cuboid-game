from math import gcd,prod
from pathlib import Path
import json
def forms(a):
 s=sum(x*x for x in a);return [s]+[s-2*x*x for x in a]
counts={'ap_impostors':0}
for k in range(1000):
 n=241+8670*k;R=17*n;a=[6*n+5,6*n+3,3*n+4]
 f=forms(a);assert f==[81*n*n+120*n+50,9*n*n,9*n*n+48*n+32,63*n*n+72*n+18]
 assert gcd(gcd(a[0],a[1]),a[2])==1
 assert all(x%2 for x in a) and all(gcd(x,R)==1 for x in a)
 assert f[0]%289==0 and all(f[j]%17 for j in (1,2,3))
 assert all(gcd(n,f[j])==1 for j in (0,2,3))
 q=[17,n,1,1];assert prod(q)==R
 assert all(f[j]%(q[j]*q[j])==0 for j in range(4))
 z=[f[j]//(q[j]*q[j]) for j in range(4)]
 assert z[1]==9 and [x%8 for x in z]==[3,1,1,1]
 assert prod(f)%(R*R)==0 and all(x%(R*R) for x in f)
 H=max(a);assert 25*H*H>=R*R and H*H<=2*R*R
 # Stronger138 Cauchy height lower bound: 3H^2/R^2>=3-2sqrt2.
 t=3*H*H-3*R*R;assert t<0 and t*t<=8*R**4
 assert all(x*x<=2*R*R for x in a)
 assert (2*R*R-a[1]*a[1])%3==2
 assert q[1]**4>=R and all(gcd(q[i],q[j])==1 for i in range(4) for j in range(i))
 counts['ap_impostors']+=1
out={'card':'M3-T11-142','status':'PASS','counts':counts,'family':{'n0':241,'step':8670,'R_multiplier':17,'Hc':1,'q':[17,'n',1,1],'zeta1':9},'physical_endpoints_enumerated':0,'family_is_physical':False,'original_T11_packet_masks_verified':False,'monic_signed_lift_verified':False,'global_counting_credit':0,'external_audit':False}
Path('M3-T11-142-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
