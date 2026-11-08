#!/usr/bin/env python3
"""Exact standard-library verification of rational-divisor local fake images at five odd bad primes.
Uses archived parent polynomial coefficients and OLD factorizations, no external CAS.
Independent square-character methods: finite field norm by resultant and multiplication matrix det.
"""
import json, hashlib, itertools, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent
PRE = {
 'signed18_genus17_rank6_certificate.json': 'PARENT6',
 'signed18_c2_true_local_kummer_dimensions_certificate.json':'PARENT345',
 'row352_infinity_kernel_rank7_certificate.json':'PARENT352',
}

def trim(a,p):
 a=[z%p for z in a]
 while len(a)>1 and a[-1]==0:a.pop()
 return a

def mul(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    c[i+j]=(c[i+j]+x*y)%p
 return trim(c,p)

def divmodp(a,b,p):
 a=trim(a,p);b=trim(b,p)
 assert b[-1]%p
 q=[0]*max(1,len(a)-len(b)+1)
 inv=pow(b[-1],-1,p)
 while len(a)>=len(b) and not(len(a)==1 and a[0]==0):
  k=len(a)-len(b);z=a[-1]*inv%p;q[k]=z
  for j,bv in enumerate(b):a[j+k]=(a[j+k]-z*bv)%p
  a=trim(a,p)
 return trim(q,p),a

def rem(a,b,p):return divmodp(a,b,p)[1]

def resultant(a,b,p):
 a=trim(a,p);b=trim(b,p);out=1
 while len(b)>1:
  m,n=len(a)-1,len(b)-1
  r=rem(a,b,p)
  if len(r)==1 and r[0]==0:return 0
  rr=len(r)-1
  out=out*(-1 if (m*n)&1 else 1)*pow(b[-1],m-rr,p)%p
  a,b=b,r
 return out*pow(b[0],len(a)-1,p)%p

def field_norm_by_matrix(f,g,p):
 n=len(f)-1
 assert f[-1]==1
 mat=[[0]*n for _ in range(n)]
 for j in range(n):
  vals=[0]*j+[z%p for z in g]
  rems=rem(vals,f,p)
  for i,z in enumerate(rems):mat[i][j]=z
 det=1
 for c in range(n):
  pivot=next((i for i in range(c,n) if mat[i][c]!=0),None)
  if pivot is None:return 0
  if pivot!=c:mat[pivot],mat[c]=mat[c],mat[pivot];det=(-det)%p
  d=mat[c][c];det=det*d%p;inv=pow(d,-1,p)
  for i in range(c+1,n):
   if mat[i][c]:
    fac=mat[i][c]*inv%p
    for j in range(c+1,n):mat[i][j]=(mat[i][j]-fac*mat[c][j])%p
    mat[i][c]=0
 return det

def legbit(a,p):
 assert a%p,'not a residue unit'
 s=pow(a%p,(p-1)//2,p)
 assert s in (1,p-1)
 return int(s==p-1)

def rank(rows):
 piv={}
 for v in rows:
  v0=v
  while v0:
   k=v0.bit_length()-1
   if k in piv:v0^=piv[k]
   else:piv[k]=v0;break
 return len(piv)

def basis_in_quotient(rows,scal):
 piv=[];rv=[]
 for i,r in enumerate(rows):
  rnk=rank(rv+[scal])
  if rank(rv+[scal,r])>rnk:
   piv.append(i);rv.append(r)
 return piv,rank(rv+[scal])-int(scal!=0)

def run():
 d6=json.loads((ROOT/'signed18_genus17_rank6_certificate.json').read_text())
 d345=json.loads((ROOT/'signed18_c2_true_local_kummer_dimensions_certificate.json').read_text())
 d352=json.loads((ROOT/'row352_infinity_kernel_rank7_certificate.json').read_text())
 h=d6['h2_coefficients_ascending']
 assert len(h)==37 and h[-1]==1 and h[0]==1
 names=d6['class_order'];gs=d6['class_G_coefficients_ascending'];degrees=d6['class_degree_basepoint']
 assert len(names)==len(gs)==len(degrees)==6
 out=[]
 for item in d345['local_primes_odd']:
  p=item['p'];ff=item['factors'];fact=[z['coefficients_ascending_mod_p'] for z in ff]
  factmulti=[z['multiplicity'] for z in ff]
  facp=[1]
  for f,m in zip(fact,factmulti):
   for _ in range(m):facp=mul(facp,f,p)
  assert facp==trim(h,p),(p,'bad factorization')
  assert all(z[-1]==1 for z in fact)
  normtheta=[((-1)**(len(f)-1)*f[0])%p for f in fact]
  signrows=[];modres=[]
  for name,g,d in zip(names,gs,degrees):
   row=[];vals=[]
   for f,nt in zip(fact,normtheta):
    x=resultant(f,g,p)
    y=field_norm_by_matrix(f,g,p)
    assert x==y,(p,name,'bad resultant',x,y)
    assert x%p and nt%p,(p,name,'nonunit residue G(theta)')
    v=x*pow(nt,-d,p)%p
    row.append(legbit(v,p));vals.append(v)
   signrows.append(row)
   modres.append(vals)
  scalar=[(len(f)-1)%2 for f in fact]
  scalarmask=sum(z<<i for i,z in enumerate(scalar))
  masks=[sum(z<<i for i,z in enumerate(row)) for row in signrows]
  bs,locfake=basis_in_quotient(masks,scalarmask)
  dim=d345['local_true_Kummer_J(Qv)/2_dimensions'][str(p)]
  assert locfake<=dim,(p,locfake,dim)
  has_odd_orbit=any(z['degree']%2==1 and z['multiplicity']==1 for z in ff)
  # 1^2 ramified pair has even orbit, and other distinct factors have Frobenius cycles of their degree.
  # Invariant odd subset exists if and only if any unramified Frobenius orbit is odd.
  local_D_inf_nonzero=not has_odd_orbit
  if local_D_inf_nonzero:
   assert not (len(ff)>0 and any(z['multiplicity']==1 and z['degree']==1 for z in ff))
  # At p=2843 the six rational divisors leave exactly one missing local direction.
  # A Hensel-lifted local point P4=(4,y), y^2=h2(4), y≡310 mod2843, supplies it.
  point4=None
  extra_local_fake=0
  if p==2843:
   x4=4
   h4=0
   for z in h[::-1]: h4=(h4*x4+z)%p
   assert h4==2281 and (310*310)%p==h4 and (2*310)%p!=0
   point4_bits=[]
   for f,nt in zip(fact,normtheta):
    ev=0
    for c in f[::-1]:ev=(ev*x4+c)%p
    assert ev!=0
    # x-θ / (0-θ) = (θ-x) / θ. Norm = f(x)/f(0).
    # Independently check via resultant and multiplication determinant.
    r=resultant(f,[(-x4)%p,1],p)
    m=field_norm_by_matrix(f,[(-x4)%p,1],p)
    assert r==m==((-1)**(len(f)-1)*ev)%p
    b=legbit(ev*pow(f[0],-1,p)%p,p)
    point4_bits.append(b)
   assert point4_bits==[1,1,0,0,1,1]
   pointmask=sum(z<<i for i,z in enumerate(point4_bits))
   assert rank(masks+[scalarmask,pointmask])-int(scalarmask!=0)==locfake+1
   extra_local_fake=1
   point4={'p':p,'X':x4,'Y_mod_p':310,'h2_X_mod_p':h4,
     'square_root_Hensel_derivative_mod_p':2*310%p,
     'quadratic_character_bits':point4_bits,
     'local_divisor':'[(4,y2843)-(0,1)] with y2843 congruent 310 modulo 2843 and y2843^2=h2(4)'}
  generated_dim=locfake+int(local_D_inf_nonzero)+extra_local_fake
  assert generated_dim<=dim,(p,'too many local points',generated_dim,dim)
  out.append(dict(p=p, factor_degrees=[z['degree'] for z in ff],multiplicities=factmulti,
    six_divisor_names=names,unit_residue_quadratic_character_bits=signrows,
    rational_scalar_bit_vector=scalar,mod_p_residues_of_norm_G_over_theta_power=modres,
    six_rational_divisor_image_fake_rank=locfake,
    rank_basis_of_six=[names[i] for i in bs],
    full_true_local_generators=[names[i] for i in bs]+(['D_infinity'] if local_D_inf_nonzero else [])+(['P4_p2843'] if point4 else []),
    local_D_infinity_nonzero=local_D_inf_nonzero,
    additional_local_point_X4=point4,
    explicit_true_Kummer_span_dimension=generated_dim,
    true_local_Kummer_dimension_from_old_row345=dim,
    explicit_generators_span_full_true_Kummer=generated_dim==dim))
  print(p,'factor degrees',out[-1]['factor_degrees'], 'fake rank',locfake,
        'basis',out[-1]['rank_basis_of_six'], 'Dinf nonzero',local_D_inf_nonzero,
        'true span',generated_dim,'of',dim, 'FULL',generated_dim==dim)
 assert [x['explicit_true_Kummer_span_dimension'] for x in out]==[4,1,2,1,2]
 assert [x['true_local_Kummer_dimension_from_old_row345'] for x in out]==[4,1,2,1,2]
 assert [x['explicit_generators_span_full_true_Kummer'] for x in out]==[True,True,True,True,True]
 return {'scope':'Stage35EX BranchB R3-07 signed±18 fixed genus17 C2 only',
 'source_certificates_sha256':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in PRE},
 'method':'exact standard library polynomial Euclidean resultant and independent finite-field multiplication matrix determinant; Legendre of norm gives quadratic character in F_p^f; all G(theta)/theta^d are residue units; global true rational divisors span local image',
 'odd_bad_primes':out,
 'new_theorem':'All five odd bad p TRUE Kummer images have explicit proven generators: four are spanned by seven global rational divisor classes; p2843 has an additional locally Hensel-lifted divisor at X=4 giving the fourth dimension.',
 'note':'At p23910039195629: no odd Galois branch orbit, and M(Qp)->mu2(Qp) parity zero; hence local D_infinity Kummer nonzero and adds 1 invisible-fake dimension. At other odd bad p local Dinf divisible by2 since a Qp-Weierstrass point exists in degree1 unramified factor.',
 'boundaries':'No true global 2-Selmer numerical bound; class group2 and Sunits completion unknown; this does NOT exclude original signed source.'}

if __name__=='__main__':
 d=run()
 if '--write' in sys.argv:
  f=ROOT/'r3_07_odd_bad_local_images_certificate.json'
  f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
  print('written',f)
 print('PASS')
