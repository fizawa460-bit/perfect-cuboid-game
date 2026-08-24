#!/usr/bin/env python3
"""Recover exceptional valuations from the audited rank-14 unit lattice.

The 18 linear-factor pilot already determines exact valuations on the first 24
side components.  The projection U_D -> Z^24 is injective (rank 14), so any
principal divisor supported on the physical boundary has at most one completion
on the 48 exceptional components.  This avoids guessing total-transform
multiplicities at the singular points.
"""
import hashlib, io, json, os, pathlib, urllib.parse, urllib.request, zipfile
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

ROOT=pathlib.Path(__file__).resolve().parent
REPO="fizawa460-bit/perfect-cuboid-game"
BR0A_ARTIFACT_ID=9505735040
BR0A_ARTIFACT_URL=f"https://api.github.com/repos/{REPO}/actions/artifacts/{BR0A_ARTIFACT_ID}/zip"
BR0A_ARTIFACT_SHA256="75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87"
BR0A_CERTIFICATE_SHA256="2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1"

class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        newreq=super().redirect_request(req,fp,code,msg,headers,newurl)
        if newreq is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:
            newreq.remove_header("Authorization")
        return newreq

def load_br0a():
    token=os.environ.get("GITHUB_TOKEN")
    if not token: raise SystemExit("GITHUB_TOKEN required")
    req=urllib.request.Request(BR0A_ARTIFACT_URL,headers={"Authorization":f"Bearer {token}","Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"perfect-cuboid-stage33/2.0"})
    opener=urllib.request.build_opener(StripCrossHostAuthRedirect())
    with opener.open(req,timeout=60) as r: raw=r.read()
    if hashlib.sha256(raw).hexdigest()!=BR0A_ARTIFACT_SHA256: raise SystemExit("BR0A artifact digest mismatch")
    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        name=next(n for n in zf.namelist() if n.endswith("br0a-artifact-certificate.json"))
        b=zf.read(name)
    if hashlib.sha256(b).hexdigest()!=BR0A_CERTIFICATE_SHA256: raise SystemExit("BR0A certificate digest mismatch")
    return json.loads(b)

def row_lift(target,Kside):
    sol=list(sp.linsolve((Kside.T,sp.Matrix(target))))
    if len(sol)!=1: raise SystemExit("side valuation does not have a unique solution set")
    tup=sol[0]
    if any(x.free_symbols for x in tup): raise SystemExit("side projection is not injective")
    if any(sp.denom(x)!=1 for x in tup): raise SystemExit("linear-factor ratio side valuation has no integral unit lift")
    return [int(x) for x in tup]

br=load_br0a()
diag=json.loads((ROOT/"q-unit-pullback-diagnostic.json").read_text())
K=sp.Matrix(br["unit_divisor_relation_kernel_basis"])
if K.shape!=(14,72) or K.rank()!=14: raise SystemExit("audited U_D shape regression")
Ks=K[:,:24]
if Ks.rank()!=14: raise SystemExit("side projection of U_D lost injectivity")

names=diag["factor_names"]
divs=diag["factor_divisor_vectors_72"]
side=[v[:24] for v in divs]
base=side[0]
records=[]
coeff_rows=[]
full_rows=[]
for i in range(1,len(names)):
    target=[int(a-b) for a,b in zip(side[i],base)]
    coeff=row_lift(target,Ks)
    full=sp.Matrix(1,14,coeff)*K
    full=[int(x) for x in list(full)]
    if full[:24]!=target: raise SystemExit("unique lift side regression")
    records.append({
      "ratio":f"({names[i]})/({names[0]})",
      "side_valuation_24":target,
      "coordinates_in_audited_U_D_basis":coeff,
      "full_divisor_72":full,
      "exceptional_valuation_48":full[24:],
    })
    coeff_rows.append(coeff); full_rows.append(full)
C=sp.Matrix(coeff_rows)
span_rank=C.rank()
if span_rank!=11: raise SystemExit(f"linear-factor ratio span rank regression: {span_rank}")
S=smith_normal_form(C,domain=sp.ZZ)
snf=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
if snf!=[1,1,1,1,1,2,2,2,2,2,2]: raise SystemExit(f"unexpected linear-factor SNF: {snf}")

cert={
  "schema":"STAGE33_04_LINEAR_FACTOR_UNIT_LIFTS_V1",
  "source_locks":{
    "br0a_artifact_id":BR0A_ARTIFACT_ID,
    "br0a_artifact_sha256":BR0A_ARTIFACT_SHA256,
    "br0a_certificate_sha256":BR0A_CERTIFICATE_SHA256,
    "unit_kernel_sha256":br["unit_divisor_relation_kernel_basis_sha256"],
    "q_unit_pullback_diagnostic_sha256":diag["canonical_sha256"],
  },
  "unit_lattice_rank":14,
  "unit_side_projection_rank":14,
  "unit_side_projection_injective":True,
  "linear_factor_count":18,
  "linear_factor_ratio_count":17,
  "all_17_ratio_side_valuations_have_unique_integral_unit_lifts":True,
  "linear_factor_ratio_span_rank":span_rank,
  "linear_factor_ratio_coordinate_smith_nonzero_diagonal":snf,
  "missing_unit_lattice_rank_after_linear_factor_channel":14-span_rank,
  "ratio_lifts":records,
  "explicit_rational_functions_materialized":17,
  "full_rank14_q_unit_basis_materialized":False,
  "next_exact_leaf":"L33-04-FIND-3-MORE-Q-UNIT-DIRECTIONS-OUTSIDE-LINEAR-FACTOR-SPAN",
  "q_defined_brauer_class_independence_certified":False,
  "physical_open_unramified_kernel_complete":False,
  "theorem_credit":False,
  "endpoint_credit":False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode(); cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(ROOT/"linear-factor-unit-lifts.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"unit_side_projection_rank":14,"linear_factor_ratio_span_rank":span_rank,"missing_unit_directions":14-span_rank,"next_exact_leaf":cert["next_exact_leaf"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
