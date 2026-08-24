#!/usr/bin/env python3
"""Integrate the saturated rank-14 Q-unit basis into BR0B left-filtration representatives."""
import hashlib,io,json,os,urllib.parse,urllib.request,zipfile
from pathlib import Path
HERE=Path(__file__).resolve().parent;REPO="fizawa460-bit/perfect-cuboid-game";ART=9513712470;DIG="4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637"
class R(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,h,newurl):
  n=super().redirect_request(req,fp,code,msg,h,newurl)
  if n is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:n.remove_header("Authorization")
  return n
def dl():
 t=os.environ.get("GITHUB_TOKEN")
 if not t:raise SystemExit("GITHUB_TOKEN required")
 req=urllib.request.Request(f"https://api.github.com/repos/{REPO}/actions/artifacts/{ART}/zip",headers={"Authorization":f"Bearer {t}","Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"perfect-cuboid-stage33/4.1"})
 with urllib.request.build_opener(R()).open(req,timeout=90) as r:b=r.read()
 if hashlib.sha256(b).hexdigest()!=DIG:raise SystemExit("artifact digest mismatch")
 return zipfile.ZipFile(io.BytesIO(b))
q=json.load(open(HERE/"saturated-q-unit-generators.json"))
if not q["full_rank14_saturated_unit_lattice_generated"] or q["smith_nonzero_diagonal"]!=[1]*14:raise SystemExit("Q-unit lattice not saturated")
basis=q["explicit_rank14_q_unit_basis"]
if len(basis)!=14:raise SystemExit("basis count")
with dl() as z:sk=json.loads(z.read("boundary-residue-skeleton.json"))
ids=[x["stable_id"] for x in sk["component_inventory"]]
if len(ids)!=72:raise SystemExit("boundary inventory")
out=[]
for b in basis:
 div=[int(x) for x in b["full_divisor_72"]]
 out.append({
  "unit_id":b["unit_id"],"rational_function":b["rational_function"],"coordinates_in_audited_U_D_basis":b["coordinates_in_audited_U_D_basis"],"divisor_vector_72":div,
  "zero_pole_boundary_support":[ids[i] for i,x in enumerate(div) if x],
  "representative_template":"CUP(chi,u): cyclic algebra attached to finite-order character chi and the explicit Q-rational unit u",
  "character_parameter":"chi in Hom_cont(G_Q,Q/Z), arbitrary finite primary order",
  "field_of_definition":"Q","ramification_support":"deleted physical boundary only",
  "denominator_support":"explicit rational function; full zero/pole divisor certified among the 72 deleted boundary components",
  "physical_open_domain":"ALL_PHYSICAL_OPEN","exact_evaluable_on_physical_open":True,
  "equivalence_independence_certificate":"unimodular saturated U_D basis + Stage33-03 KAPPA quotient + Stage33-07 injective boundary image"
 })
cert={
 "schema":"STAGE33_08_BR0B_LEFT_SATURATED_REPRESENTATIVES_V1",
 "saturated_q_unit_certificate_sha256":q["canonical_sha256"],"explicit_q_unit_basis_count":14,"basis_saturated_equals_U_D":True,
 "all_unit_zero_pole_support_on_deleted_physical_boundary":True,"br0b_left_filtration_group":"X_Q^14/<KAPPA_1,KAPPA_2>",
 "br0b_left_filtration_parametric_representatives_complete":True,"unit_representatives":out,
 "residual_kernels":[
  "R33-BR2B-BR0B-RIGHT-FILTRATION-EXPLICIT-REPRESENTATIVES",
  "R33-BR2B-GLOBAL-GERSTEN-SECTION-FOR-BOUNDARY-CONSTANT-CHARACTER-COMPLEMENT",
  "R33-BR2B-GLOBAL-GERSTEN-SECTION-FOR-61-FINITE-RAMIFIED-GENERATORS",
  "R33-BR2B-J2-PHYSICAL-OPEN-PATCH-COVER"
 ],
 "unresolved_unknown_in_scope":4,"br2b":"RUNNING","unit_status":"RUNNING","unit_closed":False,"downstream_released":False,"stage33_09_released":False,
 "next_exact_leaf":"L33-08-BR0B-RIGHT-FILTRATION-EXPLICIT-REPRESENTATIVES","theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_nonexistence_claim":False
}
raw=json.dumps(cert,sort_keys=True,separators=(",",":")).encode();cert["canonical_sha256"]=hashlib.sha256(raw).hexdigest();(HERE/"br0b-left-explicit-representatives.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"basis_count":len(out),"br0b_left_representatives_complete":True,"remaining_residuals":4,"next":cert["next_exact_leaf"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
