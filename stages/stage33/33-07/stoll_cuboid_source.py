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
 """Run the Stage33 Q-automorphism certificate in two exact Magma phases.

 The public calculator accepts the pinned Picard+Smith and Picard+automorphism
 computations separately, but returns HTTP 500 when both large computations are
 retained in one request.  Freeze the Smith right transform from phase 1 and
 inject that exact integer matrix into phase 2; no mathematical approximation is
 introduced.
 """
 smith_start=code.index("D, _, V := SmithForm(pmPic")
 split_candidates=[x for x in (code.find(STOP_MARKER),code.find("\nactperm := func<g, perm")) if x>=0]
 if not split_candidates: raise SystemExit("cannot isolate pinned Picard core for split Magma run")
 core_end=min(split_candidates)
 core_code=code[:core_end]
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
 V=[]
 for r in range(1,65):
  row=[int(x) for x in _grab_magma_literal(smith_stdout,f"SPLIT_SMITH_V_ROW_{r}")]
  if len(row)!=64: raise SystemExit("split Smith V row width regression")
  V.append(row)
 if len(diag)!=64: raise SystemExit("split Smith diagonal width regression")
 pos=[j+1 for j,d in enumerate(diag) if abs(d)>1]
 mods=[abs(diag[j-1]) for j in pos]
 if mods != [2]*4+[4]*6+[8]*4:
  raise SystemExit(f"split Smith invariant regression: {mods}")
 scales=[m//2 for m in mods]
 flat=[x for row in V for x in row]
 smith_end=code.index("Vin := V^-1;",smith_start)+len("Vin := V^-1;")
 replacement=(
  "pos := "+repr(pos)+";\n"
  "mods := "+repr(mods)+";\n"
  "scales := "+repr(scales)+";\n"
  "V := Matrix(Integers(),64,64,"+repr(flat)+");\n"
  "Vin := V^-1;"
 )
 phase2=code[:smith_start]+replacement+code[smith_end:]
 stdout,auto_attempt=_run_magma_once(
  phase2,timeout,label+" [automorphism phase]",user_agent)
 return stdout,max(smith_attempt,auto_attempt)

def run_magma(code,timeout,label,user_agent="perfect-cuboid-stage33/2.6"):
 if "STAGE33_Q_AUTOMORPHISM_DONE" in code and "SmithForm(pmPic" in code:
  return _run_q_automorphism_split(code,timeout,label,user_agent)
 return _run_magma_once(code,timeout,label,user_agent)
