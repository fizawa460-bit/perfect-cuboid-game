#!/usr/bin/env python3
"""Side-effect-free pinned Testa--Stoll source/Magma transport helper."""
import ast
import hashlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UPSTREAM_URL=(
 "https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/"
 "51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"
)
UPSTREAM_BLOB="0422b69847f2afb97cb7b3ed02ebef91279f61b1"
SKIP_START="// Genus 3 hyperelliptic curves of degree 8"
SKIP_END="// Set up the intersection pairing"
STOP_MARKER="// The automorphism group (see Proposition 4)"
MAGMA_URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER="https://magma.maths.usyd.edu.au/calc/"
RETRY_DELAYS=(0,5,15,30)

def git_blob_sha(data):
 return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def urlopen_retry(req,timeout,label):
 last=None
 for attempt,delay in enumerate(RETRY_DELAYS,1):
  if delay: time.sleep(delay)
  try: return urllib.request.urlopen(req,timeout=timeout),attempt
  except urllib.error.HTTPError as exc:
   last=exc
   body=exc.read().decode("utf-8",errors="replace")
   preview=body[:8000].replace("\r","")
   print(f"{label} HTTP failure {attempt}/{len(RETRY_DELAYS)}: HTTP {exc.code} {exc.reason}")
   if preview:
    print(f"{label} HTTP response body begin")
    print(preview)
    print(f"{label} HTTP response body end")
  except (urllib.error.URLError,TimeoutError) as exc:
   last=exc; print(f"{label} transient failure {attempt}/{len(RETRY_DELAYS)}: {exc}")
 raise last

def load_pinned_source():
 req=urllib.request.Request(UPSTREAM_URL,headers={"User-Agent":"perfect-cuboid-stage33/2.6"})
 resp,attempt=urlopen_retry(req,60,"pinned Stoll source")
 with resp: raw=resp.read()
 got=git_blob_sha(raw)
 if got!=UPSTREAM_BLOB: raise SystemExit(f"upstream blob mismatch {got}")
 text=raw.decode("utf-8")
 a=text.index(SKIP_START); b=text.index(SKIP_END,a); c=text.index(STOP_MARKER,b)
 core=text[:a]+"\n// Stage33-07 skips unused degree-8 curves.\n"+text[b:c]
 return text,core,got,attempt

def _run_magma_once(code,timeout,label,user_agent):
 payload=urllib.parse.urlencode({"input":code}).encode()
 req=urllib.request.Request(MAGMA_URL,data=payload,headers={
  "Content-Type":"application/x-www-form-urlencoded",
  "Accept":"text/html, application/xml, application/xhtml+xml",
  "Referer":MAGMA_REFERER,"User-Agent":user_agent},method="POST")
 resp,attempt=urlopen_retry(req,timeout,label)
 with resp: raw=resp.read().decode("utf-8",errors="replace")
 root=ET.fromstring(raw); lines=[]
 for result in root.findall(".//results"):
  for line in result.findall(".//line"): lines.append("".join(line.itertext()))
 return "\n".join(lines)+"\n",attempt

def _grab_magma_literal(stdout,name):
 m=re.search(rf"^{re.escape(name)}=(.+)$",stdout,re.M)
 if not m: raise SystemExit(f"missing split-Magma output {name}")
 return ast.literal_eval(m.group(1))

def _run_q_automorphism_split(code,timeout,label,user_agent):
 """Run the Q-automorphism certificate as two light Magma jobs plus local algebra.

 The public calculator accepts Picard+Smith and Picard+automorphism separately,
 but can return HTTP 500 when the Smith transport and automorphism computation
 live in one request.  Phase 1 freezes the exact Smith transform.  Phase 2 only
 emits boundary permutations and exact 64x64 Picard actions.  Python/SymPy then
 performs the integral Smith-coordinate transport locally.  No approximation or
 change of basis is introduced.
 """
 from sympy import Matrix, eye

 smith_start=code.index("D, _, V := SmithForm(pmPic")
 split_candidates=[x for x in (code.find(STOP_MARKER),code.find("\nactperm := func<g, perm")) if x>=0]
 if not split_candidates: raise SystemExit("cannot isolate pinned Picard core for split Magma run")
 core_end=min(split_candidates)
 core_code=code[:core_end]

 # Phase 1: exact Smith transform only.
 smith_code=core_code+r'''
Dsplit, _, Vsplit := SmithForm(pmPic);
diagsplit := [Abs(Integers()!Dsplit[j,j]) : j in [1..64]];
printf "SPLIT_SMITH_DIAG=%o\n", diagsplit;
for r in [1..64] do
  printf "SPLIT_SMITH_V_ROW_%o=%o\n", r, Eltseq(Vsplit[r]);
end for;
printf "STAGE33_SPLIT_SMITH_DONE\n";
'''
 smith_stdout,smith_attempt=_run_magma_once(
  smith_code,timeout,label+" [Smith phase]",user_agent)
 if "STAGE33_SPLIT_SMITH_DONE" not in smith_stdout:
  print(smith_stdout); raise SystemExit("split Smith phase failed")
 diag=[int(x) for x in _grab_magma_literal(smith_stdout,"SPLIT_SMITH_DIAG")]
 Vrows=[]
 for r in range(1,65):
  row=[int(x) for x in _grab_magma_literal(smith_stdout,f"SPLIT_SMITH_V_ROW_{r}")]
  if len(row)!=64: raise SystemExit("split Smith V row width regression")
  Vrows.append(row)
 if len(diag)!=64: raise SystemExit("split Smith diagonal width regression")
 pos=[j for j,d in enumerate(diag) if abs(d)>1]
 mods=[abs(diag[j]) for j in pos]
 if mods != [2]*4+[4]*6+[8]*4:
  raise SystemExit(f"split Smith invariant regression: {mods}")
 scales=[m//2 for m in mods]

 # Phase 2: the pinned upstream automorphism/Galois block is already present in
 # code[:smith_start].  Emit only exact permutations and Picard matrices; do no
 # Smith algebra inside Magma.
 auto_code=code[:smith_start]+r'''
selectedSplit := [1,2,4,5,6,7,8,9];
for r in [1..64] do
  printf "SPLIT_GALCC_G_ROW_%o=%o\n", r, [ccPic[r,c] : c in [1..64]];
  printf "SPLIT_GALCT_G_ROW_%o=%o\n", r, [ctPic[r,c] : c in [1..64]];
end for;
for z in [1..#selectedSplit] do
  idx := selectedSplit[z];
  printf "SPLIT_AUTO_%o_SIDE=%o\n", z, perms[idx][1..24];
  printf "SPLIT_AUTO_%o_POINT=%o\n", z,
    [perms[idx][#Cs+j]-#Cs : j in [1..#pts]];
  for r in [1..64] do
    printf "SPLIT_AUTO_%o_G_ROW_%o=%o\n", z, r,
      [action[idx][r,c] : c in [1..64]];
  end for;
end for;
printf "STAGE33_SPLIT_AUTOMORPHISM_DONE\n";
'''
 auto_stdout,auto_attempt=_run_magma_once(
  auto_code,timeout,label+" [automorphism geometry phase]",user_agent)
 if "STAGE33_SPLIT_AUTOMORPHISM_DONE" not in auto_stdout:
  print(auto_stdout); raise SystemExit("split automorphism geometry phase failed")

 def matrix_from_rows(prefix):
  rows=[]
  for r in range(1,65):
   row=[int(x) for x in _grab_magma_literal(auto_stdout,f"{prefix}_ROW_{r}")]
   if len(row)!=64: raise SystemExit(f"{prefix}: Picard row width regression")
   rows.append(row)
  return Matrix(rows)

 Gcc=matrix_from_rows("SPLIT_GALCC_G")
 Gct=matrix_from_rows("SPLIT_GALCT_G")
 Gs=[matrix_from_rows(f"SPLIT_AUTO_{z}_G") for z in range(1,9)]
 I=eye(64)
 if Gcc*Gcc != I or Gct*Gct != I or Gcc*Gct != Gct*Gcc:
  raise SystemExit("split Galois Picard action regression")
 for z,G in enumerate(Gs,1):
  if G*G != I or G*Gcc != Gcc*G or G*Gct != Gct*G:
   raise SystemExit(f"split automorphism {z}: involution/commutation regression")

 V=Matrix(Vrows)
 Vin=V.inv()
 if any(x.q != 1 for x in Vin):
  raise SystemExit("split Smith right transform is not unimodular")

 def at2_rows(G):
  # All requested actions are involutions, so G^-1=G exactly.
  B=Vin*G.T*V
  if any(x.q != 1 for x in B):
   raise SystemExit("split discriminant transport ceased to be integral")
  rows=[]
  for a in range(14):
   row=[]
   for b in range(14):
    num=scales[a]*int(B[pos[a],pos[b]])
    if num % scales[b]:
     raise SystemExit("split A_T[2] transport divisibility regression")
    row.append((num//scales[b])&1)
   rows.append(row)
  return rows

 cc2=at2_rows(Gcc); ct2=at2_rows(Gct); autos2=[at2_rows(G) for G in Gs]
 lines=[]
 for r in range(14):
  lines.append(f"GALCC_ROW_{r+1}={cc2[r]}")
  lines.append(f"GALCT_ROW_{r+1}={ct2[r]}")
 for z in range(1,9):
  side=_grab_magma_literal(auto_stdout,f"SPLIT_AUTO_{z}_SIDE")
  point=_grab_magma_literal(auto_stdout,f"SPLIT_AUTO_{z}_POINT")
  lines.append(f"AUTO_{z}_SIDE={side}")
  lines.append(f"AUTO_{z}_POINT={point}")
  for r,row in enumerate(autos2[z-1],1):
   lines.append(f"AUTO_{z}_AT2_ROW_{r}={row}")
 lines.append("STAGE33_Q_AUTOMORPHISM_DONE")
 return "\n".join(lines)+"\n",max(smith_attempt,auto_attempt)

def run_magma(code,timeout,label,user_agent="perfect-cuboid-stage33/2.6"):
 if "STAGE33_Q_AUTOMORPHISM_DONE" in code and "SmithForm(pmPic" in code:
  return _run_q_automorphism_split(code,timeout,label,user_agent)
 return _run_magma_once(code,timeout,label,user_agent)
