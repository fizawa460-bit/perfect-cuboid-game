#!/usr/bin/env python3
"""Exact residual after exhausting simple Q-rational linear and parity unit channels."""
import hashlib,io,json,os,urllib.parse,urllib.request,zipfile
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent;REPO="fizawa460-bit/perfect-cuboid-game"
AID=9505735040;ADIG="75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87";ACERT="2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1"
GID=9513712470;GDIG="4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637"
class R(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,h,newurl):
  n=super().redirect_request(req,fp,code,msg,h,newurl)
  if n is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:n.remove_header("Authorization")
  return n
def dl(i,d):
 t=os.environ.get("GITHUB_TOKEN");
 if not t:raise SystemExit("GITHUB_TOKEN required")
 req=urllib.request.Request(f"https://api.github.com/repos/{REPO}/actions/artifacts/{i}/zip",headers={"Authorization":f"Bearer {t}","Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"perfect-cuboid-stage33/3.6"})
 with urllib.request.build_opener(R()).open(req,timeout=90) as r:b=r.read()
 if hashlib.sha256(b).hexdigest()!=d:raise SystemExit("artifact digest mismatch")
 return zipfile.ZipFile(io.BytesIO(b))
with dl(AID,ADIG) as z:
 n=next(x for x in z.namelist() if x.endswith('br0a-artifact-certificate.json'));b=z.read(n)
 if hashlib.sha256(b).hexdigest()!=ACERT:raise SystemExit('BR0A cert mismatch')
 br=json.loads(b)
with dl(GID,GDIG) as z:linear=json.loads(z.read('linear-factor-unit-lifts.json'))
wide=json.load(open(HERE/'wide-q-unit-generators.json'));par=json.load(open(HERE/'parity-q-units.json'))
K=sp.Matrix(br['unit_divisor_relation_kernel_basis']);Ks=K[:,:24]
if K.shape!=(14,72) or K.rank()!=14 or Ks.rank()!=14:raise SystemExit('U_D regression')
if wide['usable_ratio_coordinate_rank']!=11 or wide['missing_unit_rank']!=3:raise SystemExit('wide channel regression')
if wide['usable_ratio_coordinate_smith_nonzero_diagonal']!=[1]*8+[2]*3:raise SystemExit('wide SNF regression')
if par['combined_rank']!=11 or par['missing_unit_rank']!=3 or any(x['both_sections_boundary_only'] for x in par['parity_unit_ratios']):raise SystemExit('parity regression')
W=sp.Matrix([r['coordinates_in_audited_U_D_basis'] for r in wide['usable_boundary_unit_ratios']])
if W.rank()!=11:raise SystemExit('wide matrix rank')
# LLL exposes a short integral basis of the full relation lattice. Pick the
# first three short rows that successively increase the Q-span of the known
# explicit-function channel. These are exact target principal divisors for the
# next reconstruction leaf.
L=Ks.lll();cur=W;targets=[];rank=11
for i,row in enumerate(L.tolist()):
 # convert side vector to the unique U_D coordinate vector
 sol=list(sp.linsolve((Ks.T,sp.Matrix(row))))
 if len(sol)!=1:raise SystemExit('LLL coordinate solve')
 coord=[int(x) for x in sol[0]]
 nr=cur.col_join(sp.Matrix([coord])).rank()
 if nr>rank:
  full=[int(x) for x in list(sp.Matrix(1,14,coord)*K)]
  targets.append({'target_id':f'MISSING_QUNIT_DIRECTION_{len(targets)+1}','lll_row_index_1based':i+1,'coordinates_in_audited_U_D_basis':coord,'side_divisor_24':row,'full_principal_divisor_target_72':full,'required_function_property':'find f in Q(S)^* with div(f)=this 72-component divisor exactly'})
  cur=cur.col_join(sp.Matrix([coord]));rank=nr
  if rank==14:break
if len(targets)!=3 or rank!=14:raise SystemExit('could not isolate three missing directions')
cert={'schema':'STAGE33_08_MISSING_QUNIT_PRINCIPAL_FUNCTION_KERNEL_V1','source_locks':{'br0a_artifact_id':AID,'br0a_artifact_sha256':ADIG,'br0g_artifact_id':GID,'br0g_artifact_sha256':GDIG,'linear_factor_unit_lifts_sha256':linear['canonical_sha256'],'wide_q_unit_sha256':wide['canonical_sha256'],'parity_q_unit_sha256':par['canonical_sha256']},'full_unit_lattice_rank':14,'explicit_simple_q_rational_unit_channel_rank':11,'explicit_simple_channel_smith_nonzero_diagonal':[1]*8+[2]*3,'quotient_by_explicit_simple_channel':'Z^3 direct_sum (Z/2)^3','missing_free_rank':3,'missing_target_principal_divisors':targets,'coordinate_hyperplane_search_exhausted':True,'triple_sign_parity_candidate_search_exhausted':True,'parity_candidates_rejected_because_interior_curve_support':True,'new_kernel_id':'R33-BR2B-QUNIT-MISSING-3D-PRINCIPAL-FUNCTION-RECONSTRUCTION','next_exact_leaf':'L33-08-CONSTRUCT-RATIONAL-FUNCTIONS-FOR-3-LLL-PRINCIPAL-DIVISORS','j2_exact_evaluable_representative_already_complete':True,'br0b_left_filtration_exact_representatives_complete':False,'every_stage33_07_relevant_class_accounted':True,'every_surviving_class_has_primary_order_and_provenance':True,'every_surviving_class_has_exact_evaluable_representative':False,'ramification_support_complete':False,'denominator_support_complete':False,'equivalence_independence_certificates_complete':False,'physical_open_domain_certified':False,'br2b':'RUNNING','unresolved_unknown_in_scope':4,'unit_status':'RUNNING','unit_closed':False,'downstream_released':False,'stage33_progress':'7/11','stage33_09_released':False,'next_expected_command':'Stage33-main-batch','theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();(HERE/'missing-q-unit-kernel.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'explicit_rank':11,'missing_free_rank':3,'quotient':cert['quotient_by_explicit_simple_channel'],'new_kernel_id':cert['new_kernel_id'],'next_exact_leaf':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
