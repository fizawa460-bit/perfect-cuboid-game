#!/usr/bin/env python3
"""Saturate the full rank-14 Q-unit lattice with exact low-degree boundary sections.

The earlier Stage33-04/08 scans found the obvious two-term/coordinate channel has
rank 11.  Three primitive pair-interaction units raise the Q-rank to 14 but
leave an index 2^6 sublattice.  The missing saturation is supplied by exact
low-degree Q-rational linear sections coming from two identities:

  (x+y+z)^2 = 2(z+x)(z+y)                       if z^2=x^2+y^2,

and, when p^2+q^2=r^2+s^2,

  (p+q+r+s)(p+q-r-s) = 2(pq-rs).

For the cuboid surface the relevant bilinear factors have product equal to a
square monomial in a_i, so all curated sections have divisor supported on the
24 physical side conics (and exceptional divisors after resolution).  Magma
independently verifies boundary-only support and exact side multiplicities.
The audited U_D -> Z^24 side projection is injective, so those side valuations
recover the exact full 72-component principal divisor without guessing
exceptional multiplicities.
"""
import hashlib, io, itertools, json, os, re, time, urllib.error, urllib.parse, urllib.request, xml.etree.ElementTree as ET, zipfile
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

HERE=Path(__file__).resolve().parent
REPO="fizawa460-bit/perfect-cuboid-game"
BR0A_ID=9505735040
BR0A_DIG="75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87"
BR0A_CERT="2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1"
UP="https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"
UP_BLOB="0422b69847f2afb97cb7b3ed02ebef91279f61b1"
STOP="// Genus 3 hyperelliptic curves of degree 8"
MAGMA="https://magma.maths.usyd.edu.au/xml/calculator.xml"

BASE_FORMS=[
 ("b3-a2","b3-a2"),("b3+a2","b3+a2"),("b2-a3","b2-a3"),("b2+a3","b2+a3"),("c-b1","c-b1"),("c+b1","c+b1"),
 ("b1-a3","b1-a3"),("b1+a3","b1+a3"),("b3-a1","b3-a1"),("b3+a1","b3+a1"),("c-b2","c-b2"),("c+b2","c+b2"),
 ("b2-a1","b2-a1"),("b2+a1","b2+a1"),("b1-a2","b1-a2"),("b1+a2","b1+a2"),("c-b3","c-b3"),("c+b3","c+b3"),
 ("a1","a1"),("a2","a2"),("a3","a3")
]
FACE=[]
for tag,x,y,z in [("12","a1","a2","b3"),("13","a1","a3","b2"),("23","a2","a3","b1")]:
 for sx,sy in itertools.product((1,-1), repeat=2):
  expr=f"{z}{'+' if sx>0 else '-'}{x}{'+' if sy>0 else '-'}{y}"
  FACE.append((f"F{tag}_{'p' if sx>0 else 'm'}{'p' if sy>0 else 'm'}",expr))
QUART=[]
for tag,p,q,r,s in [("A","b1","b3","a2","c"),("B","b1","b2","a3","c"),("C","b2","b3","a1","c")]:
 for sq,sr,ss in itertools.product((1,-1), repeat=3):
  expr=p+('+' if sq>0 else '-')+q+('+' if sr>0 else '-')+r+('+' if ss>0 else '-')+s
  QUART.append((f"Q{tag}_{'p' if sq>0 else 'm'}{'p' if sr>0 else 'm'}{'p' if ss>0 else 'm'}",expr))
FORMS=BASE_FORMS+FACE+QUART

class R(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,h,newurl):
  n=super().redirect_request(req,fp,code,msg,h,newurl)
  if n is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:n.remove_header("Authorization")
  return n

def openr(req,to):
 last=None
 for d in (0,5,15):
  if d: time.sleep(d)
  try:return urllib.request.build_opener(R()).open(req,timeout=to)
  except (urllib.error.URLError,TimeoutError) as e:last=e
 raise last

def gblob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def load_br0a():
 t=os.environ.get("GITHUB_TOKEN")
 if not t:raise SystemExit("GITHUB_TOKEN required")
 req=urllib.request.Request(f"https://api.github.com/repos/{REPO}/actions/artifacts/{BR0A_ID}/zip",headers={"Authorization":f"Bearer {t}","Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"perfect-cuboid-stage33/4.0"})
 with openr(req,90) as r:b=r.read()
 if hashlib.sha256(b).hexdigest()!=BR0A_DIG:raise SystemExit("BR0A artifact digest mismatch")
 with zipfile.ZipFile(io.BytesIO(b)) as z:
  n=next(x for x in z.namelist() if x.endswith("br0a-artifact-certificate.json"));bb=z.read(n)
 if hashlib.sha256(bb).hexdigest()!=BR0A_CERT:raise SystemExit("BR0A certificate digest mismatch")
 return json.loads(bb)

def lift(v,Ks):
 sol=list(sp.linsolve((Ks.T,sp.Matrix(v))))
 if len(sol)!=1:return None
 t=sol[0]
 if any(x.free_symbols for x in t) or any(sp.denom(x)!=1 for x in t):return None
 return [int(x) for x in t]

def ints(s):return [int(x.strip()) for x in s.replace("\n"," ").split(",") if x.strip()]

def prodexpr(exps,ratios):
 num=[];den=[]
 for e,r in zip(exps,ratios):
  if e>0:num.append(f"({r})" if e==1 else f"({r})^{e}")
  elif e<0:
   ee=-e;den.append(f"({r})" if ee==1 else f"({r})^{ee}")
 return (" * ".join(num) if num else "1")+" / "+(" * ".join(den) if den else "1")

br=load_br0a();K=sp.Matrix(br["unit_divisor_relation_kernel_basis"]);Ks=K[:,:24]
if K.shape!=(14,72) or K.rank()!=14 or Ks.rank()!=14:raise SystemExit("audited U_D regression")
req=urllib.request.Request(UP,headers={"User-Agent":"perfect-cuboid-stage33/4.0"})
with openr(req,60) as r:u=r.read()
if gblob(u)!=UP_BLOB:raise SystemExit("upstream blob mismatch")
text=u.decode();core=text[:text.index(STOP)]
forms_magma=",".join(expr for _,expr in FORMS)
extra=f'''\nforms := [{forms_magma}];\nprintf "STAGE33_08_SAT_BEGIN\\n";\nfor k in [1..#forms] do\n C:=Scheme(S,forms[k]); CC:=C; sm:=[];\n for j in [1..24] do\n  m:=0; while IsSubscheme(C1s[j],CC) do m+:=1; CC:=Difference(CC,C1s[j]); end while; Append(~sm,m);\n end for;\n printf "FACTOR=%o\\n",k; printf "SIDE=%o\\n",sm; printf "BOUNDARY_ONLY=%o\\n",Dimension(CC) lt 1;\nend for;\nprintf "STAGE33_08_SAT_END\\n";\n'''
payload=urllib.parse.urlencode({"input":"SetColumns(0);\nquick := true;\n"+core+extra}).encode()
req=urllib.request.Request(MAGMA,data=payload,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml","Referer":"https://magma.maths.usyd.edu.au/calc/","User-Agent":"perfect-cuboid-stage33/4.0"},method="POST")
with openr(req,300) as r:raw=r.read().decode("utf-8",errors="replace")
root=ET.fromstring(raw);lines=[]
for res in root.findall(".//results"):
 for line in res.findall(".//line"):lines.append("".join(line.itertext()))
out="\n".join(lines)+"\n";(HERE/"saturated-q-unit-magma-stdout.txt").write_text(out)
if "STAGE33_08_SAT_END" not in out or any(x in out for x in ("Runtime error","Internal error","Assertion failed","User error")):
 print(out);raise SystemExit("saturation Magma scan failed")
blocks=re.findall(r"FACTOR=(\d+)\nSIDE=\[(.*?)\]\nBOUNDARY_ONLY=(true|false)",out,re.S|re.I)
if len(blocks)!=len(FORMS):raise SystemExit(f"parse count {len(blocks)} != {len(FORMS)}")
sections=[]
for ks,ss,bo in blocks:
 i=int(ks)-1;side=ints(ss)
 if len(side)!=24:raise SystemExit("side shape")
 sections.append({"name":FORMS[i][0],"expression":FORMS[i][1],"side_valuation_24":side,"boundary_only":bo.lower()=="true"})
base=sections[0]
if not base["boundary_only"]:raise SystemExit("base factor lost boundary support")
records=[]
for s in sections[1:]:
 target=[a-b for a,b in zip(s["side_valuation_24"],base["side_valuation_24"])]
 coeff=lift(target,Ks) if s["boundary_only"] else None
 rec={"ratio_id":s["name"],"rational_function":f"({s['expression']})/({base['expression']})","numerator":s["expression"],"denominator":base["expression"],"boundary_only":s["boundary_only"],"side_valuation_24":target,"integral_U_D_lift":coeff is not None}
 if coeff is not None:
  rec["coordinates_in_audited_U_D_basis"]=coeff
  rec["full_divisor_72"]=[int(x) for x in list(sp.Matrix(1,14,coeff)*K)]
 records.append(rec)
usable=[r for r in records if r["integral_U_D_lift"]]
C=sp.Matrix([r["coordinates_in_audited_U_D_basis"] for r in usable])
rank=int(C.rank()) if usable else 0
Sdm,Udm,Vdm=smith_normal_decomp(DomainMatrix.from_Matrix(C).convert_to(ZZ));S,U,V=Sdm.to_Matrix(),Udm.to_Matrix(),Vdm.to_Matrix()
if U*C*V!=S:raise SystemExit("Smith decomposition regression")
diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
full=rank==14 and diag==[1]*14
basis=[]
if full:
 UC=U*C
 ratios=[r["rational_function"] for r in usable]
 for i in range(14):
  exps=[int(U[i,j]) for j in range(U.cols)]
  coord=[int(x) for x in list(UC.row(i))]
  div=[int(x) for x in list(sp.Matrix(1,14,coord)*K)]
  basis.append({"unit_id":f"QUNIT_SAT_{i+1:02d}","generator_exponents":exps,"rational_function":prodexpr(exps,ratios),"coordinates_in_audited_U_D_basis":coord,"full_divisor_72":div})
 if abs(int(sp.Matrix([b["coordinates_in_audited_U_D_basis"] for b in basis]).det()))!=1:raise SystemExit("saturated basis determinant")
cert={
 "schema":"STAGE33_08_SATURATED_Q_UNIT_GENERATORS_V1",
 "source_locks":{"br0a_artifact_id":BR0A_ID,"br0a_artifact_sha256":BR0A_DIG,"br0a_certificate_sha256":BR0A_CERT,"upstream_git_blob_sha1":UP_BLOB},
 "identity_adapters":{
  "face_half_angle":"(x+y+z)^2=2(z+x)(z+y) for z^2=x^2+y^2",
  "four_term":"(p+q+r+s)(p+q-r-s)=2(pq-rs) for p^2+q^2=r^2+s^2",
  "pair_norms":["(b1*b3-a2*c)(b1*b3+a2*c)=a1^2*a3^2","(b1*b2-a3*c)(b1*b2+a3*c)=a1^2*a2^2","(b2*b3-a1*c)(b2*b3+a1*c)=a2^2*a3^2"]
 },
 "candidate_section_count":len(FORMS),"boundary_only_section_count":sum(s["boundary_only"] for s in sections),"sections":sections,
 "usable_ratio_count":len(usable),"usable_ratios":usable,"coordinate_rank":rank,"smith_nonzero_diagonal":diag,
 "full_rank14_saturated_unit_lattice_generated":full,"explicit_rank14_q_unit_basis":basis,"missing_unit_rank":14-rank,
 "basis_saturated_equals_audited_U_D":full,"all_basis_functions_q_rational":full,"all_basis_divisors_supported_on_physical_boundary":full,
 "previous_missing_kernel":"R33-BR2B-QUNIT-MISSING-3D-PRINCIPAL-FUNCTION-RECONSTRUCTION",
 "previous_missing_kernel_discharged":full,
 "next_exact_leaf":"L33-08-BR0B-RIGHT-FILTRATION-EXPLICIT-REPRESENTATIVES" if full else "L33-08-EXPAND-LOW-DEGREE-BOUNDARY-SECTIONS",
 "unit_status":"RUNNING","unit_closed":False,"downstream_released":False,"stage33_09_released":False,"theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_nonexistence_claim":False
}
raw=json.dumps(cert,sort_keys=True,separators=(",",":")).encode();cert["canonical_sha256"]=hashlib.sha256(raw).hexdigest();(HERE/"saturated-q-unit-generators.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"candidates":len(FORMS),"boundary_only":cert["boundary_only_section_count"],"usable":len(usable),"rank":rank,"smith":diag,"full_rank14_saturated":full,"missing_rank":14-rank,"previous_missing_kernel_discharged":cert["previous_missing_kernel_discharged"],"next":cert["next_exact_leaf"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
