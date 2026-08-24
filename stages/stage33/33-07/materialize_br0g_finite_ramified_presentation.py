#!/usr/bin/env python3
import hashlib, io, json, os, urllib.parse, urllib.request, zipfile
from itertools import combinations
from pathlib import Path
from collections import Counter
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_form

HERE=Path(__file__).resolve().parent
REPO='fizawa460-bit/perfect-cuboid-game'
ARTIFACTS={
  'br0a':(9505735040,'75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87'),
  'br0g':(9513712470,'4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637'),
}
class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        nr=super().redirect_request(req,fp,code,msg,headers,newurl)
        if nr is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:
            nr.remove_header('Authorization')
        return nr

def download(key):
    aid,expected=ARTIFACTS[key]; tok=os.environ.get('GITHUB_TOKEN')
    if not tok: raise SystemExit('GITHUB_TOKEN required')
    req=urllib.request.Request(f'https://api.github.com/repos/{REPO}/actions/artifacts/{aid}/zip',headers={
      'Authorization':f'Bearer {tok}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'perfect-cuboid-stage33/2.3'})
    with urllib.request.build_opener(StripCrossHostAuthRedirect()).open(req,timeout=90) as r: raw=r.read()
    got=hashlib.sha256(raw).hexdigest()
    if got!=expected: raise SystemExit(f'{key} artifact digest mismatch {got}')
    return zipfile.ZipFile(io.BytesIO(raw))

def jload(z,n): return json.loads(z.read(n))
def bits(row):
    x=0
    for i,b in enumerate(row):
        if int(b)&1: x|=1<<i
    return x

def gf2_rank(rows):
    piv={}
    for row in rows:
        x=row if isinstance(row,int) else bits(row)
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)

def build_solver(basis):
    piv={}
    for i,row in enumerate(basis):
        x=bits(row); c=1<<i
        while x:
            p=x.bit_length()-1
            if p in piv:
                bx,bc=piv[p];x^=bx;c^=bc
            else:
                piv[p]=(x,c);break
        if not x: raise SystemExit('basis not independent')
    def solve(row):
        x=bits(row); c=0
        while x:
            p=x.bit_length()-1
            if p not in piv: raise SystemExit('vector outside certified 61D span')
            bx,bc=piv[p];x^=bx;c^=bc
        return [(c>>i)&1 for i in range(len(basis))]
    return solve

def snf_counter(rel):
    D=smith_normal_form(sp.Matrix(rel),domain=ZZ)
    diag=[abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i]!=0]
    return Counter(diag),diag

with download('br0a') as z:
    br0a=jload(z,'br0a-artifact-certificate.json')
with download('br0g') as z:
    sk=jload(z,'boundary-residue-skeleton.json')
    us=jload(z,'unit-symbol-residue-span.json')
    qr=jload(z,'qfixed17-graph-residual.json')
    tp=jload(z,'two-primary-prime-power-gersten-descent.json')

K=br0a['unit_divisor_relation_kernel_basis']
if len(K)!=14 or any(len(r)!=72 for r in K): raise SystemExit('BR0A unit kernel shape regression')
if br0a['unit_divisor_relation_kernel_basis_sha256']!=us['source_locks']['unit_kernel_sha256']:
    raise SystemExit('Stage33-04 unit-symbol source lock does not match BR0A')
edges=[(int(e['side_vertex'])-1,int(e['exceptional_vertex'])-1) for e in sk['codim2_crossings']]
if len(edges)!=144: raise SystemExit('crossing count regression')

all_rows=[];all_pairs=[]
for i,j in combinations(range(14),2):
    vi,vj=K[i],K[j]
    row=[(vi[a]*vj[b]-vi[b]*vj[a])&1 for a,b in edges]
    all_rows.append(row);all_pairs.append([i+1,j+1])
if len(all_rows)!=91 or gf2_rank(all_rows)!=44: raise SystemExit('unit-symbol rank regression')
ind=[];pairs=[];rr=0
for pair,row in zip(all_pairs,all_rows):
    nr=gf2_rank(ind+[row])
    if nr>rr:ind.append(row);pairs.append(pair);rr=nr
if pairs!=us['independent_symbol_pairs_1based'] or ind!=us['independent_secondary_residue_patterns']:
    raise SystemExit('independent unit-symbol basis mismatch')

R=qr['qfixed_residual_basis_edge_vectors_144']
if len(R)!=17 or any(len(r)!=144 for r in R): raise SystemExit('qfixed17 shape regression')
if gf2_rank(ind)!=44 or gf2_rank(R)!=17 or gf2_rank(ind+R)!=61: raise SystemExit('44+17 decomposition regression')
solve=build_solver(ind+R)
Ovec=[];Ocoords=[]
for g in tp['order4_generators']:
    v=[0]*144
    for eid in g['double_support_geometric_edges_1based']: v[int(eid)-1]=1
    Ovec.append(v);Ocoords.append(solve(v))
if len(Ovec)!=12 or gf2_rank(Ovec)!=12: raise SystemExit('order4 double rank regression')
if [c[44:] for c in Ocoords]!=tp['order4_double_coordinates_in_old_qfixed17_quotient']:
    raise SystemExit('order4 quotient coordinates regression')
proj_rank=gf2_rank([c[44:] for c in Ocoords])
if proj_rank!=3 or 12-proj_rank!=9: raise SystemExit('order4/unit intersection regression')

N=73; rel=[]
for i in range(61):
    row=[0]*N;row[i]=2;rel.append(row)
for k,c in enumerate(Ocoords):
    row=[0]*N
    for i,b in enumerate(c):
        if b: row[i]=-1
    row[61+k]=2;rel.append(row)
full_count,full_diag=snf_counter(rel)
if full_count!=Counter({1:12,2:49,4:12}): raise SystemExit(f'full SNF regression {full_count}')

relq=[]; nq=29
for i in range(17):
    row=[0]*nq;row[i]=2;relq.append(row)
for k,c in enumerate(Ocoords):
    row=[0]*nq
    for i,b in enumerate(c[44:]):
        if b: row[i]=-1
    row[17+k]=2;relq.append(row)
q_count,q_diag=snf_counter(relq)
if q_count!=Counter({1:3,2:23,4:3}): raise SystemExit(f'diagnostic quotient SNF regression {q_count}')

cert={
 'schema':'STAGE33_07_BR0G_FINITE_RAMIFIED_RESIDUE_PRESENTATION_V1',
 'source_locks':{
   'br0a_artifact_id':ARTIFACTS['br0a'][0],'br0a_artifact_sha256':ARTIFACTS['br0a'][1],
   'br0g_artifact_id':ARTIFACTS['br0g'][0],'br0g_artifact_sha256':ARTIFACTS['br0g'][1],
   'unit_kernel_sha256':br0a['unit_divisor_relation_kernel_basis_sha256'],
   'boundary_skeleton_sha256':sk['canonical_sha256'],'unit_symbol_span_sha256':us['canonical_sha256'],
   'qfixed17_sha256':qr['canonical_sha256'],'two_primary_prime_power_sha256':tp['canonical_sha256'],
 },
 'crossing_coordinate_count':144,
 'unit_symbol_candidate_count':91,'unit_symbol_rank_f2':44,
 'unit_symbol_basis_pairs_1based':pairs,
 'graph_residual_rank_f2':17,'combined_exponent_two_rank_f2':61,
 'order4_generator_count':12,'order4_double_rank_f2':12,
 'order4_double_coordinates_in_U44_R17_basis':Ocoords,
 'order4_double_projection_to_R17_rank_f2':3,
 'order4_double_intersection_U44_rank_f2':9,
 'residue_presentation_generators':{'U_order2':44,'R_order2':17,'O_nominal_order4':12},
 'residue_relation_matrix_generator_order':'U01..U44,R01..R17,O01..O12',
 'residue_relation_matrix_73x73':rel,
 'residue_relation_smith_nonzero_diagonal':full_diag,
 'finite_ramified_boundary_residue_module':'(Z/2)^49 direct_sum (Z/4)^12',
 'finite_ramified_boundary_residue_module_exact':True,
 'diagnostic_quotient_by_U44_relation_matrix_29x29':relq,
 'diagnostic_quotient_smith_nonzero_diagonal':q_diag,
 'diagnostic_quotient_by_U44':'(Z/2)^23 direct_sum (Z/4)^3',
 'diagnostic_quotient_not_promoted_to_final_class_group':True,
 'firewall':{
   'this_is_boundary_residue_level_not_yet_full_global_BrU_relation_matrix':True,
   'order4_double_zero_boundary_proper_offset_not_assumed_zero':True,
   'br0b_constant_character_overlap_not_mixed_into_finite_ramified_matrix':True,
   'j2_zero_boundary_class_not_quotiented_here':True,
 },
 'parallel_leaf_complete':True,
 'current_main_residual_preserved':'R33-BR2A-BR0B-RIGHT-FILTRATION-BOUNDARY-LIFT-AND-FINITE-RAMIFIED-INTEGRATION',
 'next_exact_leaf':'L33-07-MATERIALIZE-H1-PICU-FIVE-PLUS-QUADRATIC-LIFT-BOUNDARY-RESIDUES-AND-MATCH-RAMIFIED-MODULE',
 'relation_matrix_exact_for_boundary_finite_ramified_residue_branch':True,
 'relation_matrix_exact_for_full_two_primary_BrU_branch':False,
 'symbol_matrix_exact_for_boundary_exponent_two_branch':True,
 'complete_relevant_q_defined_class_list_for_stage33_brauer_scope':False,
 'unresolved_unknown_in_scope':1,'unit_status':'RUNNING','unit_closed':False,'downstream_released':False,
 'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(canonical).hexdigest()
(HERE/'br0g-finite-ramified-residue-presentation.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'unit_rank':44,'residual_rank':17,'combined_rank':61,'order4_double_rank':12,
 'full_snf_counts':dict(full_count),'diagnostic_snf_counts':dict(q_count),'remaining_kernel':cert['current_main_residual_preserved'],
 'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
