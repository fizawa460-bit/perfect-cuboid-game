#!/usr/bin/env python3
import itertools,json,runpy,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EQ='stages/stage36/36-09EQ/rho-legendre-graph-leaf-pivot-preflight.json'
EQ_SOURCE='stages/stage36/36-09EQ/rho-legendre-graph-leaf-pivot-source-lock.md'
EQ_VERIFY='stages/stage36/verify_stage36_36_09EQ.py'
SOURCE='stages/stage36/36-09ER/rho-legendre-core-parity-source-lock.md'
CERT='stages/stage36/36-09ER/rho-legendre-core-parity-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EQ:'ff4f8215b5e607c278b01f65aa858a5f038e0b35',
 EQ_SOURCE:'08ff42c1670a8dddffbbe9b9d81ef31934437af4',
 EQ_VERIFY:'bcae53e30d7cc22832365eaae3fd3d205b730b75',
 SOURCE:'b518e1cd8487a7a99a9121a0d4ccb253d4ff751a',
 CERT:'2994b87f098fad43d79cec17468889f72724b24b',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
eq=load(EQ);c=load(CERT)
assert eq['leaf_pivot_criterion']['sufficient_for_rank_2n_minus_2'] is True
assert eq['nonnecessity_witness']['orbit']=='O(3/47)'

# Reuse the exact-green EQ arithmetic construction after immutable hash locking it.
ns=runpy.run_path(str(ROOT/EQ_VERIFY))
matrix_support=ns['matrix_support'];peel=ns['peel'];rank=ns['rank']
datum=ns['datum'];W_for=ns['W_for'];support_loc=ns['support_loc'];nullspace=ns['nullspace']

# Canonical matrix with row/column metadata, using the same EP/EQ formulas.
def matrix_support_meta(a,b):
 odd,labels,eps=datum(a,b);G=[-1,2]+odd;ambient=2*len(G);rows=[];rowmeta=[]
 for v in ['infinity',2]+odd:
  W,dl=W_for(v,labels,eps);orth=nullspace(W,2*dl);loc=[support_loc(g,v) for g in G]
  for zi,z in enumerate(orth):
   z1=z[:dl];z2=z[dl:];row=[0]*ambient
   for j,bits in enumerate(loc):
    row[j]=sum(x*y for x,y in zip(z1,bits))&1
    row[len(G)+j]=sum(x*y for x,y in zip(z2,bits))&1
   rows.append(tuple(row));rowmeta.append((v,zi))
 colmeta=[('x',g) for g in G]+[('y',g) for g in G]
 return tuple(rows),G,rowmeta,colmeta

def perfect_matching_count(M):
 n=len(M);count=0
 for p in itertools.permutations(range(n)):
  if all(M[i][p[i]] for i in range(n)):count+=1
 return count

def label_row(s):
 # certificate row label '(q,i)'
 q,i=s[1:-1].split(',')
 return (int(q),int(i))
def label_col(s):
 # certificate column label 'x[q]' or 'y[q]'
 return (s[0],int(s[2:-1]))

# Validate parity identity on the two retained core matrices directly.
for key in ['rows_3_47_and_22_25','rows_25_22_and_47_3']:
 d=c['orbit_3_47_core_certificates'][key];H=d['core_matrix']
 assert len(H)==d['core_size'] and all(len(r)==d['core_size'] for r in H)
 pm=perfect_matching_count(H)
 assert pm==9==d['perfect_matching_count'] and pm%2==1
 assert rank(H)==d['core_size']==d['core_rank']

# Reconstruct each core from the actual residual graph, then combine it with all leaf pivots
# to obtain an explicit full (2n-2)-minor of the original support matrix.
case_map={
 (3,47):'rows_3_47_and_22_25',
 (22,25):'rows_3_47_and_22_25',
 (25,22):'rows_25_22_and_47_3',
 (47,3):'rows_25_22_and_47_3',
}
for (a,b),key in case_map.items():
 d=c['orbit_3_47_core_certificates'][key]
 M,G,rowmeta,colmeta=matrix_support_meta(a,b);n=len(G)
 seq,R,C=peel(M)
 assert n==10 and len(seq)==d['leaf_pivot_count']
 assert len(seq)+d['core_size']==2*n-2==18
 residual_rows=[rowmeta[i] for i in R];residual_cols=[colmeta[j] for j in C]
 target_rows=[label_row(s) for s in d['core_row_labels']]
 target_cols=[label_col(s) for s in d['core_column_labels']]
 assert all(x in residual_rows for x in target_rows)
 assert all(x in residual_cols for x in target_cols)
 ri=[R[residual_rows.index(x)] for x in target_rows]
 ci=[C[residual_cols.index(x)] for x in target_cols]
 H=[[M[i][j] for j in ci] for i in ri]
 assert H==d['core_matrix'],((a,b),H,d['core_matrix'])
 assert perfect_matching_count(H)==9 and rank(H)==d['core_size']
 # Combine all leaf pivot rows/columns with the odd core. The resulting selected minor is 18x18 and nonsingular.
 prow=[x[0] for x in seq];pcol=[x[1] for x in seq]
 rows=prow+ri;cols=pcol+ci
 assert len(rows)==len(set(rows))==18 and len(cols)==len(set(cols))==18
 full_minor=[[M[i][j] for j in cols] for i in rows]
 assert rank(full_minor)==18
 assert rank(M)==18 and 2*n-rank(M)==2

# EO closure replay: all and only 24 exact max-rank rows are covered by either the EQ leaf-only
# certificate or the ER leaf-plus-core certificate.
leaf20={tuple(x) for x in eq['deterministic_replay']['leaf_certified_rows']}
core4=set(case_map)
covered=leaf20|core4
assert len(leaf20)==20 and len(core4)==4 and len(covered)==24
dim2=set()
for a in range(1,51):
 for b in range(1,51):
  if a==b or __import__('math').gcd(a,b)!=1:continue
  M,G=matrix_support(a,b)
  if 2*len(G)-rank(M)==2:dim2.add((a,b))
assert len(dim2)==24 and dim2==covered
cl=c['eo_graph_certificate_closure']
assert cl['exact_sel2_dimension_2_row_count']==24
assert cl['leaf_only_certificate_count']==20
assert cl['leaf_plus_core_certificate_count']==4
assert cl['graph_certified_max_rank_row_count']==24
assert cl['false_positive_count']==0
assert cl['all_exact_EO_max_rank_rows_have_graph_certificates'] is True

crit=c['odd_matching_parity_criterion']
assert crit['required_core_size']=='m=2n-2-k'
assert crit['determinant_identity']=='det_F2(H)=perfect_matching_count(H) mod 2'
assert crit['sufficient_for_nonzero_2n_minus_2_minor'] is True
assert crit['sufficient_for_rank_2n_minus_2'] is True
assert crit['sufficient_for_Sel2_dimension_2'] is True
assert c['route_result']['next_leaf']=='36-09ES_RHO_LEGENDRE_PATTERN_CLASSIFICATION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09ER verified: odd perfect-matching parity in a residual Legendre core, combined with EQ leaf pivots, gives a nonzero (2n-2)-minor. O(3/47) has exact 6x6/8x8 core certificates with 9 matchings, completing graph certificates for all 24 EO max-rank rows. No exhaustive/full receiver/endpoint credit.')
