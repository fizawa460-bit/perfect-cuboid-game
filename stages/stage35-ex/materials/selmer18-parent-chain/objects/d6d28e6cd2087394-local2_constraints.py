from local2_arithmetic import *

def nullspace_rows(rows,width):
 a=list(rows);piv=[];r=0
 for col in range(width):
  k=next((k for k in range(r,len(a))if(a[k]>>col)&1),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  for k in range(len(a)):
   if k!=r and((a[k]>>col)&1):a[k]^=a[r]
  piv.append(col);r+=1
 out=[]
 for col in range(width):
  if col in piv:continue
  v=1<<col
  for k,p in enumerate(piv):
   if(a[k]>>col)&1:v|=1<<p
  out.append(v)
 return out

def norm_unit_mod8(a):
 mat=(np.einsum('i,ijk->kj',a,TABLE,optimize=False)%8).tolist()
 det=1
 for i in range(36):
  j=next((j for j in range(i,36)if mat[j][i]&1),None)
  if j is None:raise ValueError('nonunit norm matrix')
  if i!=j:mat[i],mat[j]=mat[j],mat[i];det=-det
  pivot=mat[i][i];det=det*pivot%8;ii=pow(pivot,-1,8)
  for j in range(i+1,36):
   c=mat[j][i]*ii%8
   if c:
    for k in range(i,36):mat[j][k]=(mat[j][k]-c*mat[i][k])%8
 return det%8

def solve_columns(columns,target):
 piv={}
 for i,v in enumerate(columns):
  w=1<<i
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=(v,w);break
   v^=piv[k][0];w^=piv[k][1]
 v=target;w=0
 while v:
  k=v.bit_length()-1
  if k not in piv:raise ValueError('not solvable')
  v^=piv[k][0];w^=piv[k][1]
 return w

def build_constraints(cert):
 chars=[int(cert['scalar_minus1_character_hex'],16)]+[int(r['character_hex'],16)for r in cert['selected_fake_basis']]
 constraints=nullspace_rows(chars,38)
 gens=[GEN[(level,k)]for level in(1,3,5)for k in range(12)]
 cs=[unit_class(a)for a in gens]
 for k in range(12):
  a=(ONE+mul(power(U,6),lift(1<<k)))%MOD;c=unit_class(a)
  if rank(cs+[c])>rank(cs):gens.append(a);cs.append(c)
  if len(cs)==38:break
 evalcolumns=[sum(((c>>p)&1)<<i for i,c in enumerate(cs))for p in range(38)]
 norm_bits=[[],[]]
 for a in gens:
  n=norm_unit_mod8(a)
  norm_bits[0].append(int(n in(3,7)));norm_bits[1].append(int(n in(3,5)))
 normrows=[solve_columns(evalcolumns,sum(b<<i for i,b in enumerate(bits)))for bits in norm_bits]
 if len(constraints)!=19 or rank(normrows)!=2:raise ValueError('constraint counts')
 if any((h&c).bit_count()%2 for h in normrows for c in chars):raise ValueError('image norm not square')
 return{'unit_fake_image_constraints_hex':[hex(h)for h in constraints],
  'unit_constraint_rank':19,'unit_norm_characters_hex':[hex(h)for h in normrows],
  'unit_norm_rank':2,'extra_unit_constraints_after_norm':17,
  'valuation_condition':'v_p4(alpha)=v_p8(alpha) mod2; then choose a unit representative modulo local squares and Q2 scalars',
  'full_fake_ambient_dim':38,'full_fake_norm_kernel_dim':36,'extra_local_constraints_after_norm':18,
  'global_independent_codimension_not_computed':True}

if __name__=='__main__':
 p=ROOT/'dyadic_full_kummer_certificate.json';cert=json.loads(p.read_text())
 cert['local_constraint_interface']=build_constraints(cert)
 p.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(cert['local_constraint_interface'],ensure_ascii=False))
