import json, math
from fractions import Fraction
from pathlib import Path
# Independent integer polynomial determinant, no symbolic resultant call.
def det_bareiss(mat):
    A=[row[:] for row in mat]; prev=1; sign=1
    for k in range(len(A)-1):
        if not A[k][k]:
            j=next(j for j in range(k+1,len(A)) if A[j][k])
            A[k],A[j]=A[j],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,len(A)):
            for j in range(k+1,len(A)):
                q=A[i][j]*pivot-A[i][k]*A[k][j]
                assert q%prev==0
                A[i][j]=q//prev
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]

def mul_matrix(aa,bb):
    nn=aa*aa+bb*bb
    coeff=[-aa*aa*nn**3,6*aa*bb*nn**2,nn*(11*aa*aa-bb*bb),-8*aa*bb]
    M=[[0]*4 for _ in range(4)]
    for j in range(3):M[j+1][j]=1
    for i in range(4):M[i][3]=-coeff[i]
    return nn,M

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def v(q,p):
    if q==0:return None
    k=0
    while q%p==0:q//=p;k+=1
    return k

primitive=0; beta_checks=0; gamma_checks=0; support_checks=0; discriminant_checks=0
primes=[3,5,7,11,13,17,19,23,29,31,37,41,43]
examples=[]
for aa in range(-12,13):
  if not aa:continue
  for bb in range(1,13):
    if math.gcd(aa,bb)!=1:continue
    primitive+=1; nn,M=mul_matrix(aa,bb); MM=mm(M,M)
    gamma=[[aa*nn*M[i][j]-bb*MM[i][j] for j in range(4)] for i in range(4)]
    assert det_bareiss(gamma)==-(aa*aa*nn**3*(aa*aa+2*bb*bb))**2
    gamma_checks+=1
    gc=[1,-8*aa*bb,nn*(11*aa*aa-bb*bb),6*aa*bb*nn**2,-aa*aa*nn**3]
    deriv=[4*gc[0],3*gc[1],2*gc[2],gc[3]]
    syl=[]
    for shift in range(3):syl.append([0]*shift+gc+[0]*(2-shift))
    for shift in range(4):syl.append([0]*shift+deriv+[0]*(3-shift))
    assert det_bareiss(syl)==16*aa*aa*nn**8*(2*bb*bb-25*aa*aa)**3
    discriminant_checks+=1
    for mz,nz in [(0,1),(1,1),(-1,1),(2,3),(-2,5),(7,2)]:
      mat=[[nn*mz*(i==j)-nz*M[i][j] for j in range(4)] for i in range(4)]
      fh=nn*mz**4-8*aa*bb*mz**3*nz+(11*aa*aa-bb*bb)*mz**2*nz**2+6*aa*bb*mz*nz**3-aa*aa*nz**4
      assert det_bareiss(mat)==nn**3*fh
      beta_checks+=1
    for p in primes:
      if (2*aa*nn*(2*bb*bb-25*aa*aa))%p==0:continue
      # alpha is a unit. If b is a unit, the only possible gamma zero
      # lies on a single degree-one factor; its norm valuation is even.
      gn=-(aa*aa*nn**3*(aa*aa+2*bb*bb))**2
      assert v(gn,p)%2==0
      if bb%p:
        root=(aa*nn*pow(bb,-1,p))%p
        gp=lambda x:(x**4-8*aa*bb*x**3+nn*(11*aa*aa-bb*bb)*x*x+6*aa*bb*nn**2*x-aa*aa*nn**3)%p
        if gp(root)==0:
          deriv=(4*root**3-24*aa*bb*root**2+2*nn*(11*aa*aa-bb*bb)*root+6*aa*bb*nn**2)%p
          assert deriv!=0
          if len(examples)<8:examples.append({'a':aa,'b':bb,'p':p,'norm_valuation':v(gn,p),'root':root})
      else:assert gn%p
      support_checks+=1

out={'symbolic_identities':'separate Wolfram exact verification; not performed by this standard-library script','independent_discriminant_determinants':discriminant_checks,'primitive_u_packets':primitive,'independent_beta_norm_determinants':beta_checks,'independent_gamma_norm_determinants':gamma_checks,'good_prime_support_checks':support_checks,'examples':examples,'physical_endpoint_enumeration':False,'global_counting_credit':False,'class_groups_computed':False,'status':'PASS'}
Path('M3-T11-123-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
