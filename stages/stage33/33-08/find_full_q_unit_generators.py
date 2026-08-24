#!/usr/bin/env python3
"""Search a wider exact Q-rational linear-section channel for all 14 units.

The Stage33-04 linear-factor channel produced only rank 11 in U_D.  This leaf
adds the seven coordinate hyperplanes a1,a2,a3,b1,b2,b3,c.  For every linear
section Magma first checks that its curve support outside the 24 side boundary
components is zero-dimensional.  Only such boundary-only sections are allowed.
The audited U_D -> Z^24 side projection is injective, so side valuations then
recover the unique full 72-component principal divisor exactly, without any
ad-hoc exceptional multiplicity convention.
"""
import hashlib, io, itertools, json, os, re, time, urllib.error, urllib.parse, urllib.request, xml.etree.ElementTree as ET, zipfile
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

HERE=Path(__file__).resolve().parent
REPO="fizawa460-bit/perfect-cuboid-game"
BR0A_ARTIFACT_ID=9505735040
BR0A_ARTIFACT_SHA256="75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87"
BR0A_CERTIFICATE_SHA256="2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1"
UPSTREAM_URL="https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"
UPSTREAM_BLOB="0422b69847f2afb97cb7b3ed02ebef91279f61b1"
STOP_MARKER="// Genus 3 hyperelliptic curves of degree 8"
MAGMA_URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
RETRY=(0,5,15)
NAMES=[
 "b3-a2","b3+a2","b2-a3","b2+a3","c-b1","c+b1",
 "b1-a3","b1+a3","b3-a1","b3+a1","c-b2","c+b2",
 "b2-a1","b2+a1","b1-a2","b1+a2","c-b3","c+b3",
 "a1","a2","a3","b1","b2","b3","c"
]

class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        nr=super().redirect_request(req,fp,code,msg,headers,newurl)
        if nr is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:
            nr.remove_header("Authorization")
        return nr

def urlopen_retry(req,timeout):
    last=None
    for delay in RETRY:
        if delay: time.sleep(delay)
        try: return urllib.request.build_opener(StripCrossHostAuthRedirect()).open(req,timeout=timeout)
        except (urllib.error.URLError,TimeoutError) as e: last=e
    raise last

def git_blob_sha(b): return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def load_br0a():
    tok=os.environ.get("GITHUB_TOKEN")
    if not tok: raise SystemExit("GITHUB_TOKEN required")
    req=urllib.request.Request(f"https://api.github.com/repos/{REPO}/actions/artifacts/{BR0A_ARTIFACT_ID}/zip",
      headers={"Authorization":f"Bearer {tok}","Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"perfect-cuboid-stage33/3.2"})
    with urlopen_retry(req,90) as r: raw=r.read()
    if hashlib.sha256(raw).hexdigest()!=BR0A_ARTIFACT_SHA256: raise SystemExit("BR0A artifact digest mismatch")
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        n=next(x for x in z.namelist() if x.endswith("br0a-artifact-certificate.json")); b=z.read(n)
    if hashlib.sha256(b).hexdigest()!=BR0A_CERTIFICATE_SHA256: raise SystemExit("BR0A cert digest mismatch")
    return json.loads(b)

def lift_side(target,Ks):
    sols=list(sp.linsolve((Ks.T,sp.Matrix(target))))
    if len(sols)!=1: return None
    s=sols[0]
    if any(x.free_symbols for x in s) or any(sp.denom(x)!=1 for x in s): return None
    return [int(x) for x in s]

def parseints(s): return [int(x.strip()) for x in s.replace("\n"," ").split(",") if x.strip()]

def expr_product(exps,ratio_names):
    pos=[]; neg=[]
    for e,r in zip(exps,ratio_names):
        if e>0: pos.append(f"({r})^{e}" if e!=1 else f"({r})")
        elif e<0:
            ee=-e; neg.append(f"({r})^{ee}" if ee!=1 else f"({r})")
    return (" * ".join(pos) if pos else "1") + " / " + (" * ".join(neg) if neg else "1")

br=load_br0a(); K=sp.Matrix(br["unit_divisor_relation_kernel_basis"])
if K.shape!=(14,72) or K.rank()!=14: raise SystemExit("U_D regression")
Ks=K[:,:24]
if Ks.rank()!=14: raise SystemExit("U_D side projection lost injectivity")

req=urllib.request.Request(UPSTREAM_URL,headers={"User-Agent":"perfect-cuboid-stage33/3.2"})
with urlopen_retry(req,60) as r: upstream=r.read()
if git_blob_sha(upstream)!=UPSTREAM_BLOB: raise SystemExit("upstream blob mismatch")
core=upstream.decode()[:upstream.decode().index(STOP_MARKER)]
extra=r'''
forms := [
  b3-a2,b3+a2,b2-a3,b2+a3,c-b1,c+b1,
  b1-a3,b1+a3,b3-a1,b3+a1,c-b2,c+b2,
  b2-a1,b2+a1,b1-a2,b1+a2,c-b3,c+b3,
  a1,a2,a3,b1,b2,b3,c
];
printf "STAGE33_08_WIDE_QUNIT_BEGIN\n";
for k in [1..#forms] do
  C := Scheme(S,forms[k]); CC := C; sm := [];
  for j in [1..24] do
    m := 0;
    while IsSubscheme(C1s[j],CC) do m +:= 1; CC := Difference(CC,C1s[j]); end while;
    Append(~sm,m);
  end for;
  printf "FACTOR=%o\n",k;
  printf "SIDE=%o\n",sm;
  printf "BOUNDARY_ONLY=%o\n", Dimension(CC) lt 1;
end for;
printf "STAGE33_08_WIDE_QUNIT_END\n";
'''
code="SetColumns(0);\nquick := true;\n"+core+"\n"+extra
payload=urllib.parse.urlencode({"input":code}).encode()
req=urllib.request.Request(MAGMA_URL,data=payload,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml","Referer":"https://magma.maths.usyd.edu.au/calc/","User-Agent":"perfect-cuboid-stage33/3.2"},method="POST")
with urlopen_retry(req,300) as r: raw=r.read().decode("utf-8",errors="replace")
root=ET.fromstring(raw); lines=[]
for result in root.findall(".//results"):
    for line in result.findall(".//line"): lines.append("".join(line.itertext()))
out="\n".join(lines)+"\n"; (HERE/"wide-q-unit-magma-stdout.txt").write_text(out)
if "STAGE33_08_WIDE_QUNIT_END" not in out or any(x in out for x in ("Runtime error","Internal error","Assertion failed","User error")):
    print(out); raise SystemExit("Magma wide Q-unit scan failed")
blocks=re.findall(r"FACTOR=(\d+)\nSIDE=\[(.*?)\]\nBOUNDARY_ONLY=(true|false)",out,re.S|re.I)
if len(blocks)!=len(NAMES): raise SystemExit(f"factor parse count {len(blocks)}")
sections=[]
for ks,ss,bo in blocks:
    k=int(ks)-1; side=parseints(ss)
    if len(side)!=24: raise SystemExit("side shape")
    sections.append({"name":NAMES[k],"side_valuation_24":side,"boundary_only":bo.lower()=="true"})
base=sections[0]
if not base["boundary_only"]: raise SystemExit("base factor no longer boundary-only")
records=[]
for s in sections[1:]:
    target=[a-b for a,b in zip(s["side_valuation_24"],base["side_valuation_24"])]
    coeff=lift_side(target,Ks) if s["boundary_only"] else None
    rec={"ratio":f"({s['name']})/({base['name']})","numerator":s["name"],"denominator":base["name"],"boundary_only_numerator":s["boundary_only"],"side_valuation_24":target,"integral_U_D_lift":coeff is not None}
    if coeff is not None:
        full=[int(x) for x in list(sp.Matrix(1,14,coeff)*K)]
        rec["coordinates_in_audited_U_D_basis"]=coeff; rec["full_divisor_72"]=full
    records.append(rec)
usable=[r for r in records if r["integral_U_D_lift"]]
C=sp.Matrix([r["coordinates_in_audited_U_D_basis"] for r in usable])
rank=int(C.rank()) if usable else 0
Sdm,Udm,Vdm=smith_normal_decomp(DomainMatrix.from_Matrix(C).convert_to(ZZ))
S,U,V=Sdm.to_Matrix(),Udm.to_Matrix(),Vdm.to_Matrix()
diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
full_saturated = rank==14 and diag==[1]*14
basis=[]
if full_saturated:
    Vinv=V.inv()
    if any(sp.Rational(x).q!=1 for x in Vinv): raise SystemExit("Smith V inverse nonintegral")
    # U*C*V=S. First 14 nonzero Smith rows therefore give an explicit
    # unimodular basis after row-combining the usable rational ratios.
    UC=U*C
    for i in range(14):
        exps=[int(U[i,j]) for j in range(U.cols)]
        coord=[int(x) for x in list(UC.row(i))]
        full=[int(x) for x in list(sp.Matrix(1,14,coord)*K)]
        basis.append({"unit_id":f"QUNIT_WIDE_{i+1:02d}","product_exponents_on_usable_ratios":exps,"rational_function":expr_product(exps,[r["ratio"] for r in usable]),"coordinates_in_audited_U_D_basis":coord,"full_divisor_72":full})
    if abs(int(sp.Matrix([b["coordinates_in_audited_U_D_basis"] for b in basis]).det()))!=1: raise SystemExit("constructed wide unit basis is not unimodular")
cert={"schema":"STAGE33_08_WIDE_Q_UNIT_GENERATOR_SCAN_V1","source_locks":{"br0a_artifact_id":BR0A_ARTIFACT_ID,"br0a_artifact_sha256":BR0A_ARTIFACT_SHA256,"br0a_certificate_sha256":BR0A_CERTIFICATE_SHA256,"upstream_git_blob_sha1":UPSTREAM_BLOB},"candidate_linear_section_count":len(NAMES),"candidate_names":NAMES,"sections":sections,"usable_boundary_unit_ratios":usable,"usable_ratio_count":len(usable),"usable_ratio_coordinate_rank":rank,"usable_ratio_coordinate_smith_nonzero_diagonal":diag,"full_rank14_saturated_unit_lattice_generated":full_saturated,"explicit_rank14_q_unit_basis":basis,"missing_unit_rank":14-rank,"all_basis_functions_q_rational":bool(full_saturated),"all_basis_divisors_supported_on_physical_boundary":bool(full_saturated),"next_exact_leaf":"L33-08-INTEGRATE-WIDE-QUNIT-BASIS" if full_saturated else "L33-08-EXPAND-Q-RATIONAL-BOUNDARY-SECTION-SEARCH","unit_status":"RUNNING","unit_closed":False,"theorem_credit":False,"endpoint_credit":False}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode(); cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest(); (HERE/"wide-q-unit-generators.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"boundary_only_section_count":sum(s['boundary_only'] for s in sections),"usable_ratio_count":len(usable),"rank":rank,"smith":diag,"full_rank14_saturated":full_saturated,"missing_unit_rank":14-rank,"next":cert["next_exact_leaf"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
