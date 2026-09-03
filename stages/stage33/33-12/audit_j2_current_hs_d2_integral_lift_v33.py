#!/usr/bin/env python3
"""V33 diagnostic: test the current J2 HS d2 integral-lift obstruction.

For V32, z(cc)=0 and z(ct)=b in Pic(S)/2.  Vanishing of the Bockstein/HS d2
would require an integral adjustment of the rational half-lift b/2.  Writing
n=b+2y gives the exact system A*y=d, where n must be C-invariant and
T-anti-invariant.  An inconsistency modulo 2 is therefore already a complete
nonvanishing certificate.  The diagnostic also emits the exact integer row
combination behind that parity contradiction.
"""
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
S33=HERE.parent
PIC=S33/'33-07'/'retained-picard-base-sparse.json'
V32=HERE/'j2-current-v4-pic2-cocycle-v32.json'
PIC_SHA='e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49'
V32_SHA='e91a7b701690efde3884ca1edc2182b25033a3ff6c7d89bcb8092d02f5a50a7e'
N=64

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def locked(path,expected):
 o=json.loads(path.read_text(encoding='utf-8')); b=dict(o); claimed=b.pop('canonical_sha256'); assert claimed==expected==csha(b),(path.name,claimed,csha(b)); return o
def expand_int(obj):
 rows=[]
 for sparse in obj['matrix_64x64_sparse_rows_1based']:
  row=[0]*N
  for col,value in sparse: assert 1<=col<=N and row[col-1]==0; row[col-1]=int(value)
  rows.append(row)
 assert len(rows)==N; return rows
def rowmul(v,m): return [sum(v[i]*m[i][j] for i in range(N)) for j in range(N)]
def make_system(c,t,b):
 a=[]
 for j in range(N): a.append([c[i][j]-int(i==j) for i in range(N)])
 for j in range(N): a.append([t[i][j]+int(i==j) for i in range(N)])
 ab=[sum(row[i]*b[i] for i in range(N)) for row in a]; assert all(x%2==0 for x in ab)
 return a,[-(x//2) for x in ab],ab
def solve_mod2_with_certificate(a,d):
 m=len(a); rows=[]
 for r in range(m): rows.append([sum((a[r][j]&1)<<j for j in range(N)),d[r]&1,1<<r])
 pivot_row=0; pivots=[]
 for col in range(N):
  p=next((r for r in range(pivot_row,m) if (rows[r][0]>>col)&1),None)
  if p is None: continue
  rows[pivot_row],rows[p]=rows[p],rows[pivot_row]; base=rows[pivot_row]
  for r in range(m):
   if r!=pivot_row and ((rows[r][0]>>col)&1): rows[r][0]^=base[0]; rows[r][1]^=base[1]; rows[r][2]^=base[2]
  pivots.append(col); pivot_row+=1
 contradiction=next((row for row in rows if row[0]==0 and row[1]==1),None)
 if contradiction is not None:
  mask=contradiction[2]; lam=[(mask>>r)&1 for r in range(m)]
  lhs=[sum(lam[r]*a[r][j] for r in range(m))&1 for j in range(N)]; rhs=sum(lam[r]*d[r] for r in range(m))&1
  assert lhs==[0]*N and rhs==1
  return {'consistent_mod2':False,'left_null_certificate_lambda_f2':lam,'lambda_A_mod2_zero':True,'lambda_d_mod2':1,'rank_A_mod2':len(pivots)}
 solution=[0]*N
 for r,col in enumerate(pivots): solution[col]=rows[r][1]
 for r in range(m): assert (sum((a[r][j]&1)*solution[j] for j in range(N))^(d[r]&1))==0
 return {'consistent_mod2':True,'one_solution_y_mod2':solution,'rank_A_mod2':len(pivots),'higher_integral_lifting_required':True}
def main():
 pic=locked(PIC,PIC_SHA); v32=locked(V32,V32_SHA); c=expand_int(pic['objects']['cc']); t=expand_int(pic['objects']['ct']); b=v32['full_surface_pullback']['ct_fullPic64_f2']
 assert v32['full_surface_pullback']['cc_fullPic64_f2']==[0]*N and len(b)==N and all(x in (0,1) for x in b)
 ident=[[int(i==j) for j in range(N)] for i in range(N)]
 def mm(x,y): return [[sum(x[i][k]*y[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
 assert mm(c,c)==ident and mm(t,t)==ident and mm(c,t)==mm(t,c)
 assert [x&1 for x in rowmul(b,c)]==b and [x&1 for x in rowmul(b,t)]==b
 a,d,ab=make_system(c,t,b); mod2=solve_mod2_with_certificate(a,d)
 witness=None
 if not mod2['consistent_mod2']:
  lam=mod2['left_null_certificate_lambda_f2']; support=[r for r,x in enumerate(lam) if x]
  combo=[sum(lam[r]*a[r][j] for r in range(len(a))) for j in range(N)]; combo_d=sum(lam[r]*d[r] for r in range(len(a)))
  assert all(x%2==0 for x in combo) and combo_d%2==1
  witness={'lambda_support_equations_1based':[r+1 for r in support],'combined_A_row_sparse_1based':[[j+1,x] for j,x in enumerate(combo) if x],'combined_A_row_all_even':True,'combined_d':combo_d,'combined_d_odd':True,'mod2_contradiction':'0 = 1'}
  if len(support)==1:
   r=support[0]; witness['singleton_equation']={'equation_1based':r+1,'block':'C_MINUS_I' if r<N else 'T_PLUS_I','output_coordinate_1based':r+1 if r<N else r-N+1,'A_dot_b':ab[r],'d':d[r],'A_row_sparse_1based':[[j+1,x] for j,x in enumerate(a[r]) if x]}
 result={'success':True,'schema':'STAGE33_12_J2_CURRENT_HS_D2_INTEGRAL_LIFT_V33_DIAGNOSTIC','source_locks':{'v32_canonical_sha256':V32_SHA,'retained_picard_base_sparse_canonical_sha256':PIC_SHA},'integral_lift_system':{'unknowns':N,'equations':len(a),'formula':'A*y=d for n=b+2*y with n*(C-I)=0 and n*(T+I)=0','rational_half_lift':'b/2'},'mod2_test':mod2,'exact_parity_witness':witness,'interpretation':'HS_D2_NONZERO_ALREADY_CERTIFIED_BY_PARITY_OBSTRUCTION' if not mod2['consistent_mod2'] else 'PARITY_LEVEL_LIFT_EXISTS_HIGHER_INTEGRAL_LIFTING_STILL_OPEN','firewall':{'standard_kummer_column_promoted':False,'stage33_12_closed_exact':False,'stage33_13_released':False,'theorem_credit':False,'receiver_credit':False,'endpoint_credit':False}}
 print(json.dumps(result,sort_keys=True,separators=(',',':')))
if __name__=='__main__': main()
