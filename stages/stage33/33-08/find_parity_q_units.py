#!/usr/bin/env python3
"""Recover the three missing Q-units from triple-sign parity on the 3x8 side conics."""
import hashlib, io, json, os, re, time, urllib.error, urllib.parse, urllib.request, xml.etree.ElementTree as ET, zipfile
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
HERE=Path(__file__).resolve().parent; REPO="fizawa460-bit/perfect-cuboid-game"
BR0A_ID=9505735040; BR0A_DIG="75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87"; BR0A_CERT="2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1"
BR0G_ID=9513712470; BR0G_DIG="4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637"
UP="https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"; UP_BLOB="0422b69847f2afb97cb7b3ed02ebef91279f61b1"; STOP="// Genus 3 hyperelliptic curves of degree 8"; MAGMA="https://magma.maths.usyd.edu.au/xml/calculator.xml"
NAMES=["P1_PLUS","P1_MINUS","P2_PLUS","P2_MINUS","P3_PLUS","P3_MINUS"]
EXPRS=["a2*a3*b1+b2*b3*c","a2*a3*b1-b2*b3*c","a1*a3*b2+b1*b3*c","a1*a3*b2-b1*b3*c","a1*a2*b3+b1*b2*c","a1*a2*b3-b1*b2*c"]
class R(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,h,newurl):
  n=super().redirect_request(req,fp,code,msg,h,newurl)
  if n is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:n.remove_header("Authorization")
  return n
def openr(req,to):
 last=None
 for d in (0,5,15):
  if d:time.sleep(d)
  try:return urllib.request.build_opener(R()).open(req,timeout=to)
  except (urllib.error.URLError,TimeoutError) as e:last=e
 raise last
def gblob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def dl(id,dig):
 t=os.environ.get("GITHUB_TOKEN");
 if not t:raise SystemExit("GITHUB_TOKEN required")
 req=urllib.request.Request(f"https://api.github.com/repos/{REPO}/actions/artifacts/{id}/zip",headers={"Authorization":f"Bearer {t}","Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"perfect-cuboid-stage33/3.4"})
 with openr(req,90) as r:b=r.read()
 if hashlib.sha256(b).hexdigest()!=dig:raise SystemExit("artifact digest mismatch")
 return zipfile.ZipFile(io.BytesIO(b))
with dl(BR0A_ID,BR0A_DIG) as z:
 n=next(x for x in z.namelist() if x.endswith("br0a-artifact-certificate.json")); bb=z.read(n)
 if hashlib.sha256(bb).hexdigest()!=BR0A_CERT:raise SystemExit("BR0A cert mismatch")
 br=json.loads(bb)
with dl(BR0G_ID,BR0G_DIG) as z: linear=json.loads(z.read("linear-factor-unit-lifts.json"))
K=sp.Matrix(br["unit_divisor_relation_kernel_basis"]);Ks=K[:,:24]
if K.shape!=(14,72) or K.rank()!=14 or Ks.rank()!=14:raise SystemExit("U_D regression")
req=urllib.request.Request(UP,headers={"User-Agent":"perfect-cuboid-stage33/3.4"})
with openr(req,60) as r:u=r.read()
if gblob(u)!=UP_BLOB:raise SystemExit("upstream blob")
text=u.decode();core=text[:text.index(STOP)]
extra=r'''
forms := [a2*a3*b1+b2*b3*c,a2*a3*b1-b2*b3*c,a1*a3*b2+b1*b3*c,a1*a3*b2-b1*b3*c,a1*a2*b3+b1*b2*c,a1*a2*b3-b1*b2*c];
printf "STAGE33_08_PARITY_BEGIN\n";
for k in [1..#forms] do
 C:=Scheme(S,forms[k]); CC:=C; sm:=[];
 for j in [1..24] do
  m:=0; while IsSubscheme(C1s[j],CC) do m+:=1; CC:=Difference(CC,C1s[j]); end while; Append(~sm,m);
 end for;
 printf "FACTOR=%o\n",k; printf "SIDE=%o\n",sm; printf "BOUNDARY_ONLY=%o\n",Dimension(CC) lt 1;
end for;
printf "STAGE33_08_PARITY_END\n";
'''
payload=urllib.parse.urlencode({"input":"SetColumns(0);\nquick := true;\n"+core+"\n"+extra}).encode(); req=urllib.request.Request(MAGMA,data=payload,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml","Referer":"https://magma.maths.usyd.edu.au/calc/","User-Agent":"perfect-cuboid-stage33/3.4"},method="POST")
with openr(req,300) as r:raw=r.read().decode("utf-8",errors="replace")
root=ET.fromstring(raw); lines=[]
for res in root.findall(".//results"):
 for line in res.findall(".//line"):lines.append("".join(line.itertext()))
out="\n".join(lines)+"\n";(HERE/"parity-q-unit-magma-stdout.txt").write_text(out)
if "STAGE33_08_PARITY_END" not in out or any(x in out for x in ("Runtime error","Internal error","Assertion failed","User error")):print(out);raise SystemExit("parity Magma fail")
def ints(s):return [int(x.strip()) for x in s.replace("\n"," ").split(",") if x.strip()]
blocks=re.findall(r"FACTOR=(\d+)\nSIDE=\[(.*?)\]\nBOUNDARY_ONLY=(true|false)",out,re.S|re.I)
if len(blocks)!=6:raise SystemExit("parse parity")
secs=[]
for ks,ss,bo in blocks:secs.append({"name":NAMES[int(ks)-1],"expression":EXPRS[int(ks)-1],"side":ints(ss),"boundary_only":bo.lower()=="true"})
if any(len(s["side"])!=24 for s in secs):raise SystemExit("side shape")
def lift(v):
 sol=list(sp.linsolve((Ks.T,sp.Matrix(v))))
 if len(sol)!=1:return None
 t=sol[0]
 if any(x.free_symbols for x in t) or any(sp.denom(x)!=1 for x in t):return None
 return [int(x) for x in t]
par=[]
for j in range(3):
 a,b=secs[2*j],secs[2*j+1]; target=[x-y for x,y in zip(a["side"],b["side"])]
 coeff=lift(target) if a["boundary_only"] and b["boundary_only"] else None
 par.append({"unit_id":f"PARITY_UNIT_{j+1}","rational_function":f"({a['expression']})/({b['expression']})","numerator":a["expression"],"denominator":b["expression"],"both_sections_boundary_only":a["boundary_only"] and b["boundary_only"],"side_valuation_24":target,"integral_U_D_lift":coeff is not None,"coordinates_in_audited_U_D_basis":coeff,"full_divisor_72":[int(x) for x in list(sp.Matrix(1,14,coeff)*K)] if coeff is not None else None})
lin=[[int(x) for x in r["coordinates_in_audited_U_D_basis"]] for r in linear["ratio_lifts"]]
if len(lin)!=17:raise SystemExit("linear artifact regression")
rows=lin+[p["coordinates_in_audited_U_D_basis"] for p in par if p["coordinates_in_audited_U_D_basis"] is not None]
C=sp.Matrix(rows);Sdm,Udm,Vdm=smith_normal_decomp(DomainMatrix.from_Matrix(C).convert_to(ZZ));S,U,V=Sdm.to_Matrix(),Udm.to_Matrix(),Vdm.to_Matrix();rank=int(C.rank());diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0];full=rank==14 and diag==[1]*14
basis=[]
if full:
 UC=U*C
 funcs=[r["ratio"] for r in linear["ratio_lifts"]]+[p["rational_function"] for p in par]
 for i in range(14):
  exp=[int(U[i,j]) for j in range(U.cols)];coord=[int(x) for x in list(UC.row(i))];div=[int(x) for x in list(sp.Matrix(1,14,coord)*K)]
  numer=[];denom=[]
  for e,f in zip(exp,funcs):
   if e>0:numer.append(f"({f})^{e}" if e!=1 else f"({f})")
   elif e<0:denom.append(f"({f})^{-e}" if e!=-1 else f"({f})")
  basis.append({"unit_id":f"QUNIT_FULL_{i+1:02d}","generator_exponents":exp,"rational_function":f"{' * '.join(numer) if numer else '1'} / {' * '.join(denom) if denom else '1'}","coordinates_in_audited_U_D_basis":coord,"full_divisor_72":div})
 if abs(int(sp.Matrix([b["coordinates_in_audited_U_D_basis"] for b in basis]).det()))!=1:raise SystemExit("basis determinant")
cert={"schema":"STAGE33_08_TRIPLE_PARITY_Q_UNITS_V1","source_locks":{"br0a_artifact_id":BR0A_ID,"br0a_artifact_sha256":BR0A_DIG,"br0g_artifact_id":BR0G_ID,"br0g_artifact_sha256":BR0G_DIG,"linear_factor_unit_lifts_sha256":linear["canonical_sha256"],"upstream_git_blob_sha1":UP_BLOB},"parity_sections":secs,"parity_unit_ratios":par,"linear_rank_before":linear["linear_factor_ratio_span_rank"],"combined_rank":rank,"combined_smith_nonzero_diagonal":diag,"full_rank14_saturated_unit_lattice_generated":full,"explicit_rank14_q_unit_basis":basis,"missing_unit_rank":14-rank,"next_exact_leaf":"L33-08-INTEGRATE-FULL-QUNIT-BASIS" if full else "L33-08-SEARCH-NONLINEAR-BOUNDARY-UNITS","unit_status":"RUNNING","unit_closed":False,"theorem_credit":False,"endpoint_credit":False}
raw=json.dumps(cert,sort_keys=True,separators=(",",":")).encode();cert["canonical_sha256"]=hashlib.sha256(raw).hexdigest();(HERE/"parity-q-units.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"parity_boundary_only":[p["both_sections_boundary_only"] for p in par],"parity_integral_lifts":[p["integral_U_D_lift"] for p in par],"combined_rank":rank,"smith":diag,"full_rank14_saturated":full,"missing_unit_rank":14-rank,"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
