import math,json,itertools
from pathlib import Path
counts={};states=0;miss1=miss2=0;examples=[]
for N in (100,200,400,800):
 count=0
 for m in range(N+(N%2==0),2*N+1,2):
  lo=(m+9)//10;hi=m//8
  for n in range(lo+(lo%2),hi+1,2):
   if math.gcd(m,n)!=1:continue
   A=m*m-n*n;B=2*m*n;k=m*m+n*n
   g=2*B;h=1;u=A*A;v=2*B*k;R=A*A+2*B*B;tau=R
   e1=2*A*B;e2=2*B*B;e3=u
   a=u;b=v;c=R;q=1;D=R;s=8*A*B**3;W=a+b;d=a-b
   assert A%2==1 and B%4==0 and A*A+B*B==k*k
   assert math.gcd(A,B)==1 and math.gcd(h,g)==1
   assert u*u+(g*k)**2==tau*tau and math.gcd(u,g*k)==1
   assert math.gcd(A*B,tau)==math.gcd(g,tau)==math.gcd(k,tau)==1
   assert math.gcd(e1,e2)==g and math.gcd(e1,e2,e3)==1
   assert all(math.gcd(e,R)==1 for e in (e1,e2,e3))
   assert e1*e1+e2*e2+e3*e3==R*R
   assert W*W-2*tau*tau*q**4==-d*d and d>0
   assert s*(W+d)==4*g*g*A*B*u
   assert s*a==2*e1*e2*e3 and math.gcd(s,D)==1
   assert c==tau*q*q and D==R//q
   G=R*R;U=G*b;V=G*a;NT=s
   assert U*U+V*V==R**6 and math.gcd(U,V)==G
   assert math.gcd(U+V,R**3)==math.gcd(U-V,R**3)==G
   assert math.gcd(NT,R*R)==q*q
   assert NT*V==2*e1*e2*e3*R*R
   assert U%2==0 and V%2==1 and a%2==1  # excludes original product phase
   assert (2*e1*e2*e3)%b!=0  # swapping to the even phase leg cannot keep s integral
   assert R<=18*N**4 and R*4096>=3969*N**4
   assert min(a,b)*320>=N**4 and d*320>=N**4
   f1sq=e2*e2+e3*e3;f2sq=e1*e1+e3*e3
   miss1+=math.isqrt(f1sq)**2!=f1sq;miss2+=math.isqrt(f2sq)**2!=f2sq
   count+=1;states+=1
   if len(examples)<3:examples.append({'m':m,'n':n,'edges':[e1,e2,e3],'R':R,'fake_phase':[a,b,c],'s':s})
 counts[str(N)]=count
modcases=0
# Necessary mod8 assignments for one odd edge and two edges divisible by4.
for R in (1,3,5,7):
 for odd_i in range(3):
  esets=[(1,3,5,7) if i==odd_i else (0,4) for i in range(3)]
  fsets=[(0,4) if i==odd_i else (1,3,5,7) for i in range(3)]
  for e in itertools.product(*esets):
   for f in itertools.product(*fsets):
    assert sum(x*x for x in e)%8==R*R%8
    assert all((e[i]*e[i]+f[i]*f[i]-R*R)%8==0 for i in range(3))
    U=e[0]*e[1]*e[2]-e[0]*f[1]*f[2]-e[1]*f[0]*f[2]-e[2]*f[0]*f[1]
    V=f[0]*e[1]*e[2]+f[1]*e[0]*e[2]+f[2]*e[0]*e[1]-f[0]*f[1]*f[2]
    NT=sum(e[i]*f[i] for i in range(3))
    assert U%2==1 and V%4==0 and NT%4==0
    modcases+=1
out={'card':'M3-T11-189','status':'PASS','counterstates_by_dyadic_N':counts,'counterstates_checked':states,'all_counterstates_fail_original_phase_parity':True,'all_swapped_even_phase_legs_fail_s_integrality':True,'necessary_mod8_assignments_checked':modcases,'finite_missing_face_nonsquares':[miss1,miss2],'examples':examples,'physical_endpoints_enumerated':0,'scope':'Projected receiver counterstates and necessary parity assignments, not physical endpoints. Finite nonsquare checks are not an all-parameter nonexistence proof.'}
Path('M3-T11-189-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
