#!/usr/bin/env python3
"""Materialize two exact Stage33-08 representative blocks.

(1) U01..U44: the audited exponent-two unit-symbol generators become explicit
    quaternion symbols (u_i,u_j)_2 using the saturated Q-rational U_D basis.
    Since every u_i is a unit on the physical open, these representatives are
    evaluable on the entire physical open.

(2) J2: source-lock the exact Q-defined Creutz--Viray corestriction CSA from
    Stage33-05 and record its current dense evaluation patch.  This leaf does
    not claim a full physical-open patch cover; that remains a smaller explicit
    residual.
"""
import hashlib, io, json, os, urllib.parse, urllib.request, zipfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO="fizawa460-bit/perfect-cuboid-game"
S33_07_ART=9521076746
S33_07_DIG="c9de08cff9ce04b0bfe1fd216e176996437d44fa7c841673f037400ad8e47dca"
J2_SCRIPT_BLOB="a63be5592c793c3812da99275478f14dd0d2687b"
J2_SCRIPT_PATH="stages/stage33/33-05/j2_arithmetic_descent.py"

class R(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,h,newurl):
  n=super().redirect_request(req,fp,code,msg,h,newurl)
  if n is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:n.remove_header("Authorization")
  return n

def download_artifact():
 t=os.environ.get("GITHUB_TOKEN")
 if not t:raise SystemExit("GITHUB_TOKEN required")
 req=urllib.request.Request(f"https://api.github.com/repos/{REPO}/actions/artifacts/{S33_07_ART}/zip",headers={"Authorization":f"Bearer {t}","Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"perfect-cuboid-stage33/4.2"})
 with urllib.request.build_opener(R()).open(req,timeout=90) as r:b=r.read()
 if hashlib.sha256(b).hexdigest()!=S33_07_DIG:raise SystemExit("Stage33-07 artifact digest mismatch")
 return zipfile.ZipFile(io.BytesIO(b))

q=json.load(open(HERE/"saturated-q-unit-generators.json"))
left=json.load(open(HERE/"br0b-left-explicit-representatives.json"))
if not q["full_rank14_saturated_unit_lattice_generated"] or q["smith_nonzero_diagonal"]!=[1]*14:raise SystemExit("saturated U_D regression")
units=q["explicit_rank14_q_unit_basis"]
if len(units)!=14 or len(left["unit_representatives"])!=14:raise SystemExit("unit basis count regression")

with download_artifact() as z:
 finite=json.loads(z.read("br0g-finite-ramified-residue-presentation.json"))
 global2=json.loads(z.read("global-two-primary-presentation.json"))
 j2pull=json.loads(z.read("j2-endpoint-q2-pullback.json"))

pairs=[[int(a),int(b)] for a,b in finite["unit_symbol_basis_pairs_1based"]]
if len(pairs)!=44:raise SystemExit("U44 pair count regression")
if finite["residue_presentation_generators"]["U_order2"]!=44:raise SystemExit("U44 generator regression")

u44=[]
for k,(i,j) in enumerate(pairs,1):
 ui,uj=units[i-1],units[j-1]
 u44.append({
  "class_id":f"U{k:02d}","primary_order":2,"provenance":"BR0G_RAMIFIED_UNIT_SYMBOL",
  "field_of_definition":"Q","unit_pair_1based":[i,j],
  "symbol_or_algebra_representative":f"({ui['rational_function']}, {uj['rational_function']})_2",
  "first_slot_unit_id":ui["unit_id"],"second_slot_unit_id":uj["unit_id"],
  "ramification_support":"deleted physical boundary only",
  "denominator_support":"deleted physical boundary only; both slots are units on U=S\\D",
  "equivalence_independence_certificate":"Stage33-07 audited U44 basis pair list + Stage33-08 saturated unimodular U_D basis",
  "physical_open_domain":"ALL_PHYSICAL_OPEN",
  "exact_evaluable_representative":True
 })

# Exact source-locked J2 formula from Stage33-05 j2_arithmetic_descent.py.
branch="t^2*(1-alpha^2)^2 + alpha^2*(1-t^2)^2"
ell="4*(alpha^2*t^2+t^4-4*t^2+2)/((t^2-1)*(t^2-2*t-1))"
j2_csa=("Cor_{L(C)/Q(t)(C)}((ell_J2, s-alpha)_2), "
        "L=Q(t)[alpha]/(t^2*(1-alpha^2)^2+alpha^2*(1-t^2)^2), "
        "ell_J2=4*(alpha^2*t^2+t^4-4*t^2+2)/((t^2-1)*(t^2-2*t-1))")
if j2pull["j2_endpoint_pullback_nonzero_certified"] is not True or global2["complete_inventory"]["proper_k3"]["class_id"]!="J2":raise SystemExit("J2 audited inventory regression")
j2={
 "class_id":"J2","primary_order":2,"provenance":"BR2_K3","field_of_definition":"Q",
 "branch_algebra":f"L=Q(t)[alpha]/({branch})","ell_J2":ell,
 "symbol_or_algebra_representative":j2_csa,
 "ramification_support":"NONE_ON_PROPER_CUBOID_SURFACE; Stage33-05 arithmetic unramifiedness and Stage33-07 proper-pullback audit",
 "denominator_support_current_formula":"(t^2-1)*(t^2-2*t-1)=0 or second quaternion slot s-alpha=0 require a different local presentation/patch",
 "equivalence_independence_certificate":"Stage33-05 Q descent + Stage33-07 endpoint nonzero/nonconstant and independence from boundary-residue classes",
 "physical_open_domain_current_patch":"D((t^2-1)*(t^2-2*t-1)*(s-alpha)) in the branch-algebra chart",
 "generic_dense_patch_evaluable":True,
 "full_physical_open_patch_cover_complete":False,
 "exact_evaluable_representative_on_current_patch":True
}

cert={
 "schema":"STAGE33_08_U44_AND_J2_EXPLICIT_REPRESENTATIVES_V1",
 "source_locks":{
  "saturated_q_unit_certificate_sha256":q["canonical_sha256"],
  "br0b_left_certificate_sha256":left["canonical_sha256"],
  "stage33_07_artifact_id":S33_07_ART,"stage33_07_artifact_sha256":S33_07_DIG,
  "br0g_finite_ramified_certificate_sha256":finite["canonical_sha256"],
  "global_two_primary_certificate_sha256":global2["canonical_sha256"],
  "j2_endpoint_pullback_certificate_sha256":j2pull["canonical_sha256"],
  "j2_stage33_05_script_path":J2_SCRIPT_PATH,"j2_stage33_05_script_git_blob_sha1":J2_SCRIPT_BLOB
 },
 "u44_generator_count":44,"u44_explicit_representatives_complete":True,"u44_representatives":u44,
 "u44_all_evaluable_on_full_physical_open":True,
 "finite_ramified_total_presentation":"(Z/2)^49 direct_sum (Z/4)^12",
 "finite_ramified_unit_symbol_prefix_explicit_count":44,
 "finite_ramified_remaining_non_unit_symbol_generators":{"R_order2":17,"O_nominal_order4":12},
 "j2":j2,"j2_generic_exact_representative_complete":True,"j2_full_patch_cover_complete":False,
 "remaining_representative_kernels":[
  "R33-BR2B-GLOBAL-GERSTEN-SECTION-FOR-BOUNDARY-CONSTANT-CHARACTER-COMPLEMENT",
  "R33-BR2B-GLOBAL-GERSTEN-SECTION-FOR-R17-AND-O12-FINITE-RAMIFIED-GENERATORS",
  "R33-BR2B-J2-PHYSICAL-OPEN-PATCH-COVER"
 ],
 "unresolved_unknown_in_scope":3,
 "br2b":"RUNNING","unit_status":"RUNNING","unit_closed":False,"downstream_released":False,"stage33_09_released":False,
 "next_exact_leaf":"L33-08-MATERIALIZE-R17-O12-GLOBAL-GERSTEN-SECTIONS-OR-SMALLEST-SECTION-KERNEL",
 "theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_nonexistence_claim":False
}
raw=json.dumps(cert,sort_keys=True,separators=(",",":")).encode();cert["canonical_sha256"]=hashlib.sha256(raw).hexdigest();(HERE/"u44-j2-explicit-representatives.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"U44_explicit":44,"U44_full_physical_open":True,"J2_generic_exact":True,"J2_patch_cover_complete":False,"finite_ramified_remaining":"R17+O12","remaining_kernels":3,"next":cert["next_exact_leaf"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
